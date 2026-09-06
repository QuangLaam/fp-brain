"""Package/lifecycle safety tests; these do not grade model behavior."""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('manage_fp', ROOT / 'scripts/manage-fp.py')
fp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fp)


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='fp package tests ')
        self.root = Path(self.tmp.name).resolve()
        self.source = self.root / 'independent candidate with spaces'
        shutil.copytree(ROOT / 'skills/fp', self.source)
        self.skills = self.root / 'discovery with spaces'
        self.skills.mkdir()
        self.state = self.root / 'management outside discovery'
        self.manager = fp.Manager(self.skills, self.state)
        self.target = self.skills / 'fp'
        self.original = fp.validate(self.source)
        self.sentinel = self.skills / 'other-skill.txt'
        self.sentinel.write_text('unrelated user content')

    def tearDown(self):
        self.assertEqual(self.sentinel.read_text(), 'unrelated user content')
        self.tmp.cleanup()

    def install(self):
        return self.manager.run('install', self.source)

    def changed_source(self):
        file = self.source / 'SKILL.md'
        file.write_text(file.read_text().replace('1.0.0-candidate.1', '1.0.0-candidate.2'))
        return fp.validate(self.source)

    def test_independent_copy_and_read_only_dry_run(self):
        self.assertEqual(self.original, fp.validate(ROOT / 'skills/fp'))
        result = self.manager.run('dry-run', self.source)
        self.assertTrue(result['change'])
        self.assertFalse(self.state.exists())
        self.assertFalse(self.target.exists())

    def test_install_idempotent_uninstall_and_two_rollbacks(self):
        self.install()
        self.assertEqual(fp.validate(self.target), self.original)
        manifest = self.manager.manifest_path.read_bytes()
        self.assertEqual(self.install()['status'], 'UNCHANGED')
        self.assertEqual(self.manager.manifest_path.read_bytes(), manifest)
        self.manager.run('uninstall')
        self.assertFalse(self.target.exists())
        self.manager.run('rollback')
        self.assertEqual(fp.validate(self.target), self.original)
        self.manager.run('rollback')
        self.assertFalse(self.target.exists())
        self.assertEqual(self.manager.read_state()['history'], [])

    def test_upgrade_and_rollback_restore_exact_previous_version(self):
        self.install()
        updated = self.changed_source()
        self.install()
        self.assertEqual(fp.validate(self.target), updated)
        self.manager.run('rollback')
        self.assertEqual(fp.validate(self.target), self.original)

    def test_unmanaged_target_never_overwritten_or_removed(self):
        self.target.mkdir()
        user = self.target / 'personal.md'
        user.write_text('preserve')
        for command in ['dry-run', 'install', 'uninstall', 'rollback']:
            with self.subTest(command=command), self.assertRaises(fp.Conflict):
                self.manager.run(command, self.source if command in {'install','dry-run'} else None)
            self.assertEqual(user.read_text(), 'preserve')

    def test_edited_managed_file_blocks_all_mutations(self):
        self.install()
        user = self.target / 'references/core.md'
        user.write_text(user.read_text() + '\nUser change.\n')
        contents = user.read_bytes()
        for command in ['dry-run', 'install', 'uninstall', 'rollback']:
            with self.subTest(command=command), self.assertRaises(fp.Conflict):
                self.manager.run(command, self.source if command in {'install','dry-run'} else None)
            self.assertEqual(user.read_bytes(), contents)

    def test_extra_file_or_empty_dir_blocks_deletion(self):
        self.install()
        for name, is_dir in [('personal.md', False), ('empty-user-directory', True)]:
            extra = self.target / name
            extra.mkdir() if is_dir else extra.write_text('user content')
            with self.assertRaises(fp.Conflict):
                self.manager.run('uninstall')
            self.assertTrue(extra.exists())
            extra.rmdir() if is_dir else extra.unlink()

    def test_missing_managed_target_is_drift(self):
        self.install()
        shutil.rmtree(self.target)
        with self.assertRaises(fp.Conflict):
            self.install()

    def test_invalid_policy_or_missing_file_fails_before_install(self):
        f = self.source / 'agents/openai.yaml'
        f.write_text(f.read_text().replace('false', 'true'))
        with self.assertRaises(fp.Conflict):
            self.install()
        self.assertFalse(self.target.exists())
        f.unlink()
        with self.assertRaises(fp.Conflict):
            fp.validate(self.source)

    def test_extra_source_file_and_empty_dir_rejected(self):
        extra = self.source / 'userdata.json'
        extra.write_text('{}')
        with self.assertRaises(fp.Conflict):
            fp.validate(self.source)
        extra.unlink()
        (self.source / 'evals').mkdir()
        with self.assertRaises(fp.Conflict):
            fp.validate(self.source)

    def test_package_reference_escapes_and_missing_links_rejected(self):
        file = self.source / 'SKILL.md'
        original = file.read_text()
        for reference in ['../../outside.md','/etc/passwd','https://example.com/runtime','references/absent.md','references/%2e%2e/core.md']:
            with self.subTest(reference=reference):
                file.write_text(original + f'\n[dependency]({reference})\n')
                with self.assertRaises(fp.Conflict):
                    fp.validate(self.source)
        file.write_text(original + '\n[dependency][external]\n[external]: /etc/passwd\n')
        with self.assertRaises(fp.Conflict):
            fp.validate(self.source)

    def test_package_symlink_even_within_package_rejected(self):
        file = self.source / 'references/core.md'
        file.unlink()
        file.symlink_to(self.source / 'references/methods.md')
        with self.assertRaises(fp.Conflict):
            fp.validate(self.source)

    def test_symlink_ancestor_target_state_and_dangling_link_rejected(self):
        link = self.root / 'redirect'
        link.symlink_to(self.skills, target_is_directory=True)
        with self.assertRaises(fp.Conflict):
            fp.Manager(link, self.state)
        self.target.symlink_to(self.root / 'does-not-exist')
        with self.assertRaises(fp.Conflict):
            self.install()
        self.target.unlink()
        if self.state.exists():
            shutil.rmtree(self.state)
        self.state.symlink_to(self.root / 'another-missing')
        with self.assertRaises(fp.Conflict):
            fp.Manager(self.skills, self.state)

    def test_state_inside_discovery_or_parent_rejected(self):
        for state in [self.skills, self.skills / 'backup', self.root]:
            with self.subTest(state=state), self.assertRaises(fp.Conflict):
                fp.Manager(self.skills, state)

    def test_managed_target_cannot_be_source(self):
        self.install()
        with self.assertRaises(fp.Conflict):
            self.manager.run('install', self.target)

    def test_unmanaged_state_directory_preserved(self):
        self.state.mkdir()
        file = self.state / 'notes'
        file.write_text('mine')
        with self.assertRaises(fp.Conflict):
            self.install()
        self.assertEqual(file.read_text(), 'mine')
        self.assertFalse(self.target.exists())

    def test_manifest_target_and_backup_traversal_rejected(self):
        self.install()
        self.changed_source()
        self.install()
        original = self.manager.manifest_path.read_text()
        data = json.loads(original)
        data['target'] = str(self.skills / 'other')
        self.manager.manifest_path.write_text(json.dumps(data))
        with self.assertRaises(fp.Conflict):
            self.manager.run('uninstall')
        data = json.loads(original)
        data['history'][-1]['before']['backup'] = '../../outside'
        self.manager.manifest_path.write_text(json.dumps(data))
        with self.assertRaises(fp.Conflict):
            self.manager.run('rollback')
        self.assertTrue(self.target.exists())

    def test_manifest_hash_path_escape_rejected(self):
        self.install()
        data = self.manager.read_state()
        data['current']['files']['../../outside'] = '0' * 64
        self.manager.manifest_path.write_text(json.dumps(data))
        with self.assertRaises(fp.Conflict):
            self.manager.run('uninstall')

    def test_backup_drift_or_symlink_blocks_rollback(self):
        self.install()
        self.changed_source()
        self.install()
        state = self.manager.read_state()
        backup = self.state / 'backups' / state['history'][-1]['before']['backup']
        user = backup / 'references/core.md'
        user.write_text('modified backup')
        current = fp.validate(self.target)
        with self.assertRaises(fp.Conflict):
            self.manager.run('rollback')
        self.assertEqual(fp.validate(self.target), current)
        shutil.rmtree(backup)
        backup.symlink_to(self.source, target_is_directory=True)
        with self.assertRaises(fp.Conflict):
            self.manager.run('rollback')

    def test_manifest_publish_failure_restores_existing_target(self):
        self.install()
        self.changed_source()
        manifest = self.manager.manifest_path.read_bytes()
        with patch.object(self.manager, 'save', side_effect=OSError('injected publish failure')):
            with self.assertRaises(OSError):
                self.install()
        self.assertEqual(fp.validate(self.target), self.original)
        self.assertEqual(self.manager.manifest_path.read_bytes(), manifest)

    def test_manifest_publish_failure_restores_initial_absence(self):
        with patch.object(self.manager, 'save', side_effect=OSError('injected publish failure')):
            with self.assertRaises(OSError):
                self.install()
        self.assertFalse(self.target.exists())
        self.assertFalse(self.manager.manifest_path.exists())

    def test_late_edit_before_displacement_is_restored_on_upgrade_and_uninstall(self):
        self.install()
        self.changed_source()
        real_replace = fp.os.replace
        for command in ['install', 'uninstall']:
            # Restore the known managed bytes before exercising each race independently.
            original_text = (ROOT / 'skills/fp/references/core.md').read_text()
            (self.target / 'references/core.md').write_text(original_text)
            manifest = self.manager.manifest_path.read_bytes()

            def inject(src, dst):
                if Path(src) == self.target and Path(dst).name == 'old':
                    (self.target / 'references/core.md').write_text(original_text + '\nLate user edit.\n')
                return real_replace(src, dst)

            with self.subTest(command=command), patch.object(fp.os, 'replace', side_effect=inject):
                with self.assertRaises(fp.Conflict):
                    self.manager.run(command, self.source if command == 'install' else None)
            self.assertIn('Late user edit.', (self.target / 'references/core.md').read_text())
            self.assertEqual(self.manager.manifest_path.read_bytes(), manifest)

    def test_edit_after_displaced_check_survives_successful_commit(self):
        self.install()
        self.changed_source()
        real_save = self.manager.save

        def inject(data):
            displaced = list(self.state.glob('.operation-*/old'))
            self.assertEqual(len(displaced), 1)
            with (displaced[0] / 'references/core.md').open('a') as stream:
                stream.write('\nVery late user edit.\n')
            real_save(data)

        with patch.object(self.manager, 'save', side_effect=inject):
            result = self.install()
        recovery = Path(result['displaced_recovery'])
        self.assertTrue(recovery.is_relative_to(self.state))
        self.assertIn('Very late user edit.', (recovery / 'references/core.md').read_text())
        self.assertEqual(fp.validate(self.target), fp.validate(self.source))

    def test_cli_validation_and_conflict_exit_code(self):
        command = [sys.executable, str(ROOT/'scripts/manage-fp.py')]
        result = subprocess.run(command + ['validate','--source',str(self.source)],capture_output=True,text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), self.original)
        self.target.mkdir()
        result = subprocess.run(command + ['install','--source',str(self.source),'--skills-dir',str(self.skills),'--state-dir',str(self.state)],capture_output=True,text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn('conflict', result.stderr.lower())


if __name__ == '__main__':
    unittest.main()
