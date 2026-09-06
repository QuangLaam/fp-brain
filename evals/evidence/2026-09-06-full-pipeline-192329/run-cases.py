#!/usr/bin/env python3
"""Run all twelve authorized fixtures plus one ordinary probe once; never overwrite a case."""
import hashlib
import json
import os
import re
import concurrent.futures
from pathlib import Path
import shlex
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
FIXTURE_SOURCE = ROOT / 'evals/acceptance.md'
ORDER = ['A1','A2','A3','A4','A5','B1','B2','D1','D2','D3','L1','L2','ORDINARY']
COMMON = [
    '-c', 'sandbox_mode="read-only"', '-c', 'approval_policy="never"',
    '--ignore-user-config', '--enable', 'skip_host_skill_discovery',
    '--disable', 'plugins', '--disable', 'memories', '-m', 'gpt-5.4-mini', '--json',
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def events(path):
    for line in path.read_text().splitlines():
        try:
            yield json.loads(line)
        except ValueError:
            continue


def main():
    fixtures = {}
    content = FIXTURE_SOURCE.read_text()
    for match in re.finditer(r'^## ([ABDL]\d) —.*?\n(.*?)(?=^## |\Z)', content, re.M | re.S):
        case, body = match.groups()
        messages = re.findall(r'^U\d+: “(.*?)”(?=\n|$)', body, re.M | re.S)
        skill = {'A':'fp-ask','B':'fp-brainstorm','D':'fp-decide','L':'fp-learn'}[case[0]]
        fixtures[case] = (skill, messages)
    assert {c:len(fixtures[c][1]) for c in ORDER[:-1]} == {'A1':3,'A2':3,'A3':4,'A4':2,'A5':3,'B1':3,'B2':1,'D1':1,'D2':2,'D3':1,'L1':3,'L2':2}
    fixtures['ORDINARY'] = (None, ['Dịch câu sau sang tiếng Anh: “Tôi sẽ gửi bản thiết kế vào ngày mai.”'])
    cases = OUT / 'cases'
    cases.mkdir(exist_ok=False)
    runtime = sorted((ROOT / '.agents/skills').rglob('*')) + [ROOT / 'method/CORE.md']
    runtime = [p for p in runtime if p.is_file()]
    initial_hashes = {str(p.relative_to(ROOT)): digest(p) for p in runtime}
    (OUT / 'source-hashes.json').write_text(json.dumps(initial_hashes, indent=2) + '\n')
    (OUT / 'host-version.txt').write_text(subprocess.check_output(['codex', '--version'], text=True))
    (OUT / 'baseline-commit.txt').write_text(subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True))
    (OUT / 'fixtures.json').write_text(json.dumps({c: fixtures[c] for c in ORDER}, ensure_ascii=False, indent=2) + '\n')
    sessions = Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))) / 'sessions'
    def run_case(case):
        case_dir = cases / case
        case_dir.mkdir()
        skill, messages = fixtures[case]
        thread = None
        for n, message in enumerate(messages, 1):
            prompt = f'${skill}\n\n{message}' if n == 1 and skill else message
            cmd = (['codex', 'exec', '-C', str(ROOT), '--sandbox', 'read-only']
                   if n == 1 else ['codex', 'exec', 'resume', thread]) + COMMON + [prompt]
            prefix = case_dir / f'turn-{n}'
            prefix.with_suffix('.command.json').write_text(json.dumps(cmd, ensure_ascii=False, indent=2) + '\n')
            stdout = prefix.with_suffix('.stdout.jsonl')
            try:
                with stdout.open('w') as out, prefix.with_suffix('.stderr.txt').open('w') as err:
                    rc = subprocess.run(cmd, cwd=ROOT, stdout=out, stderr=err, timeout=180).returncode
            except subprocess.TimeoutExpired:
                rc = 124
            prefix.with_suffix('.exit.txt').write_text(f'{rc}\n')
            stream = list(events(stdout))
            if n == 1:
                thread = next((e['thread_id'] for e in stream if e.get('type') == 'thread.started'), None)
                if thread:
                    (case_dir / 'thread-id.txt').write_text(thread + '\n')
            complete = any(e.get('type') == 'turn.completed' for e in stream)
            print(f'{case} turn {n}: exit={rc}, completed={complete}', flush=True)
            if rc or not thread or not complete:
                (case_dir / 'stop.txt').write_text('Runner/completion failure; no later turns or retry.\n')
                break
        if thread:
            matches = list(sessions.glob(f'**/*{thread}.jsonl'))
            if len(matches) == 1:
                shutil.copyfile(matches[0], case_dir / 'session-rollout.jsonl')
                (case_dir / 'session-origin.txt').write_text(str(matches[0]) + '\n')
            else:
                (case_dir / 'capture-error.txt').write_text(f'Expected one session, found {len(matches)}\n')
        if {str(p.relative_to(ROOT)): digest(p) for p in runtime} != initial_hashes:
            raise RuntimeError('Runtime source changed during tests; stop without retry')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        list(pool.map(run_case, ORDER))
    (OUT / 'source-hashes-after.json').write_text(json.dumps({str(p.relative_to(ROOT)): digest(p) for p in runtime}, indent=2) + '\n')
    print('Run finished. Behavioral review is still required.', flush=True)


if __name__ == '__main__':
    main()
