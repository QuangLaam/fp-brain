#!/usr/bin/env python3
"""Manage one self-contained FP package. This is never called by FP runtime."""
import argparse
import contextlib
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import sys
import tempfile
import uuid

FILES = frozenset({'SKILL.md', 'agents/openai.yaml', 'references/core.md',
                   'references/methods.md', 'references/learning-context.md'})
DIRS = frozenset({'agents', 'references'})
DEFAULT_SOURCE = Path(__file__).resolve().parents[1] / 'skills' / 'fp'


class Conflict(ValueError):
    pass


def fail(message):
    raise Conflict(message)


def safe_path(value):
    """Reject symlinks, including dangling links and ancestor redirects."""
    path = Path(os.path.abspath(value))
    for node in [path, *path.parents]:
        if node.is_symlink():
            fail(f'Symlink path is not permitted: {node}')
    return path


def digest(data):
    return hashlib.sha256(data).hexdigest()


def inventory(root):
    root = safe_path(root)
    if not root.is_dir():
        fail(f'Package directory unavailable: {root}')
    hashes, dirs = {}, set()
    for entry in root.rglob('*'):
        mode = entry.lstat().st_mode
        rel = entry.relative_to(root).as_posix()
        if stat.S_ISLNK(mode):
            fail(f'Symlink in package: {rel}')
        if stat.S_ISDIR(mode):
            dirs.add(rel)
        elif stat.S_ISREG(mode):
            hashes[rel] = digest(entry.read_bytes())
        else:
            fail(f'Non-regular package entry: {rel}')
    if set(hashes) != FILES or dirs != DIRS:
        fail(f'Unexpected/missing package entries: files={sorted(set(hashes)^FILES)}, dirs={sorted(dirs^DIRS)}')
    return hashes


def validate(source):
    source = safe_path(source)
    hashes = inventory(source)
    text = (source / 'SKILL.md').read_text()
    fm = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    if not fm or not re.search(r'^name: fp$', fm[1], re.M):
        fail('Missing FP frontmatter/name')
    if not re.search(r'^description: .+', fm[1], re.M):
        fail('Missing description')
    version = re.search(r'^  version: "([A-Za-z0-9.\-]+)"$', fm[1], re.M)
    if not version:
        fail('Missing metadata version')
    policy = (source / 'agents/openai.yaml').read_text()
    if not re.search(r'^policy:\n  allow_implicit_invocation: false\s*\Z', policy, re.M):
        fail('Explicit-only invocation policy required')
    # This package intentionally uses a narrow set of inline Markdown links only.
    # Reject other reference syntaxes rather than silently missing dependencies.
    for rel in FILES:
        if not rel.endswith('.md'):
            continue
        body = (source / rel).read_text()
        if re.search(r'\]\s*\[|^\s*\[[^\]]+\]:|<\s*(?:a|img)\b|\[\[', body, re.M | re.I):
            fail(f'Unsupported reference syntax: {rel}')
        for ref in re.findall(r'\[[^\]]*\]\(([^)]+)\)', body):
            if re.search(r'[:\\%\s]', ref) or ref.startswith('/'):
                fail(f'External or ambiguous reference: {ref}')
            dest = (source / rel).parent / ref.split('#', 1)[0]
            resolved = dest.resolve()
            if not resolved.is_relative_to(source) or not resolved.is_file():
                fail(f'Missing or escaping reference: {ref}')
    return {'version': version[1], 'files': hashes,
            'package_hash': digest(json.dumps(hashes, sort_keys=True).encode())}


def hash_map(value):
    return isinstance(value, dict) and set(value) == FILES and all(
        isinstance(v, str) and re.fullmatch('[0-9a-f]{64}', v) for v in value.values())


def snapshot_valid(value, backup=False):
    if value is None:
        return True
    keys = {'version', 'files', 'package_hash'} | ({'backup'} if backup else set())
    return (isinstance(value, dict) and set(value) == keys
            and isinstance(value['version'], str) and hash_map(value['files'])
            and value['package_hash'] == digest(json.dumps(value['files'], sort_keys=True).encode())
            and (not backup or (isinstance(value['backup'], str)
                 and re.fullmatch('[0-9a-f]{32}', value['backup']) is not None)))


def strip_backup(value):
    return None if value is None else {k: v for k, v in value.items() if k != 'backup'}


class Manager:
    def __init__(self, skills_dir, state_dir):
        self.skills = safe_path(skills_dir)
        self.state = safe_path(state_dir)
        self.target = safe_path(self.skills / 'fp')
        if not self.skills.is_dir():
            fail('skills-dir must be an existing dedicated skill discovery directory')
        if self.state == self.skills or self.state.is_relative_to(self.skills) or self.skills.is_relative_to(self.state):
            fail('State and discovery roots must not overlap')
        if self.state.exists() and not self.state.is_dir():
            fail('State root is not a directory')
        self.manifest_path = self.state / 'manifest.json'

    def read_state(self):
        safe_path(self.manifest_path)
        if not self.manifest_path.exists():
            if self.state.exists() and any(p.name != '.lock' for p in self.state.iterdir()):
                fail('Unmanaged state directory: no manifest')
            return {'schema': 1, 'target': str(self.target), 'current': None, 'history': []}
        try:
            data = json.loads(self.manifest_path.read_text())
        except (OSError, ValueError) as exc:
            fail(f'Invalid manifest: {exc}')
        if (not isinstance(data, dict) or set(data) != {'schema', 'target', 'current', 'history'}
                or data['schema'] != 1 or data['target'] != str(self.target)
                or not snapshot_valid(data['current']) or not isinstance(data['history'], list)):
            fail('Manifest schema/target mismatch')
        previous = None
        for event in data['history']:
            if (not isinstance(event, dict) or set(event) != {'operation', 'before', 'after'}
                    or event['operation'] not in {'install', 'uninstall'}
                    or not snapshot_valid(event['before'], backup=True)
                    or not snapshot_valid(event['after'])
                    or strip_backup(event['before']) != previous):
                fail('Invalid manifest history')
            previous = event['after']
        if previous != data['current']:
            fail('Manifest current state does not match history')
        return data

    def assert_current(self, current):
        safe_path(self.target)
        if current is None:
            if self.target.exists():
                fail('Unmanaged target conflict; no files changed')
        elif not self.target.exists() or validate(self.target) != current:
            fail('Managed target drift; no files changed')

    def save(self, data):
        fd, tmp = tempfile.mkstemp(prefix='.manifest-', dir=self.state)
        try:
            with os.fdopen(fd, 'w') as stream:
                json.dump(data, stream, indent=2)
                stream.write('\n')
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(tmp, self.manifest_path)
        finally:
            if os.path.exists(tmp):
                os.unlink(tmp)

    @contextlib.contextmanager
    def locked(self):
        self.state.mkdir(parents=True, exist_ok=True)
        safe_path(self.state / '.lock')
        # No symlink-follow on the lock itself, even in a shared state directory.
        fd = os.open(self.state / '.lock', os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX)
            yield
        finally:
            fcntl.flock(fd, fcntl.LOCK_UN)
            os.close(fd)

    def backup(self, current):
        if current is None:
            return None
        token = uuid.uuid4().hex
        parent = safe_path(self.state / 'backups')
        parent.mkdir(exist_ok=True)
        dest = parent / token
        shutil.copytree(self.target, dest)
        if validate(dest) != current:
            fail('Backup verification failed')
        return dict(current, backup=token)

    def replace(self, desired_source, desired, data, previous_current):
        """Replace via same-filesystem rename; restore target on ordinary failure.

        Manifest publish is last. A crash between rename and manifest publish
        yields a detected drift, never a silently overwritten user modification.
        """
        if self.state.stat().st_dev != self.skills.stat().st_dev:
            fail('State and target must be on the same filesystem for atomic rename')
        work = Path(tempfile.mkdtemp(prefix='.operation-', dir=self.state))
        staged, old = work / 'new', work / 'old'
        moved_old = published_new = False
        try:
            if desired is not None:
                shutil.copytree(desired_source, staged)
                if validate(staged) != desired:
                    fail('Staged copy differs from requested package')
            # Check again after staging to catch intervening edits.
            self.assert_current(previous_current)
            if self.target.exists():
                os.replace(self.target, old)
                moved_old = True
                if validate(old) != previous_current:
                    fail('Target changed during publication; restoring displaced tree')
            if desired is not None:
                os.replace(staged, self.target)
                published_new = True
            self.save(data)
            return str(old) if moved_old else None
        except BaseException:
            if published_new:
                # Only discard our own still-unmodified published package.
                if validate(self.target) != desired:
                    fail(f'Concurrent target drift: recovery preserved at {work}')
                os.replace(self.target, staged)
            if moved_old:
                os.replace(old, self.target)
            raise
        finally:
            # A writer may still hold an open handle into the displaced tree.
            # Never delete it after commit: even edits after our last check survive.
            if not old.exists():
                shutil.rmtree(work)

    def run(self, command, source=None):
        if source is not None:
            source = safe_path(source)
            if source == self.target or source.is_relative_to(self.state) or self.state.is_relative_to(source):
                fail('Source must be separate from managed target and state')
        candidate = validate(source) if command in {'install', 'dry-run'} else None
        # Dry-run is strictly read-only, including state/lock creation.
        if command == 'dry-run':
            state = self.read_state()
            self.assert_current(state['current'])
            return {'status': 'DRY_RUN', 'target': str(self.target), 'candidate': candidate,
                    'change': state['current'] != candidate, 'state_dir': str(self.state)}
        with self.locked():
            state = self.read_state()
            self.assert_current(state['current'])
            if command == 'install' and candidate == state['current']:
                return {'status': 'UNCHANGED', 'target': str(self.target), 'candidate': candidate}
            if command == 'uninstall' and state['current'] is None:
                return {'status': 'ABSENT', 'target': str(self.target)}
            if command == 'rollback':
                if not state['history']:
                    fail('No managed operation to roll back')
                event = state['history'][-1]
                desired = strip_backup(event['before'])
                restore = None
                if desired is not None:
                    restore = safe_path(self.state / 'backups' / event['before']['backup'])
                    if validate(restore) != desired:
                        fail('Backup drift; no files changed')
                updated = dict(state, current=desired, history=state['history'][:-1])
            else:
                desired = candidate if command == 'install' else None
                restore = source if command == 'install' else None
                before = self.backup(state['current'])
                event = {'operation': command, 'before': before, 'after': desired}
                updated = dict(state, current=desired, history=[*state['history'], event])
            recovery = self.replace(restore, desired, updated, state['current'])
            return {'status': command.upper() + '_OK', 'target': str(self.target),
                    'current': desired, 'manifest': str(self.manifest_path),
                    'displaced_recovery': recovery}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['validate', 'dry-run', 'install', 'uninstall', 'rollback'])
    parser.add_argument('--source', type=Path, default=DEFAULT_SOURCE)
    parser.add_argument('--skills-dir', type=Path, help='Existing discovery directory; only its fp child is managed')
    parser.add_argument('--state-dir', type=Path, help='Exclusive FP lifecycle state/backup directory outside discovery')
    args = parser.parse_args(argv)
    try:
        if args.command == 'validate':
            result = validate(args.source)
        else:
            if args.skills_dir is None or args.state_dir is None:
                parser.error('--skills-dir and --state-dir are required for lifecycle commands')
            result = Manager(args.skills_dir, args.state_dir).run(
                args.command, args.source if args.command in {'dry-run', 'install'} else None)
        print(json.dumps(result, indent=2))
        return 0
    except (Conflict, OSError, UnicodeError) as exc:
        print(f'FP management stopped: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
