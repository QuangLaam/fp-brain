#!/usr/bin/env python3
"""Extract reviewable transcripts and verify recorded native evidence, never rerun."""
import hashlib
import json
import re
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read_events(p):
    return [json.loads(line) for line in p.read_text().splitlines() if line.strip()]


def main():
    fixtures = json.loads((OUT / 'fixtures.json').read_text())
    integrity = {}
    transcript = ['# Full native transcripts\n\nExact prompts and all assistant commentary/final messages.\n']
    for case, (skill, messages) in fixtures.items():
        directory = OUT / 'cases' / case
        trace = directory / 'session-rollout.jsonl'
        if not trace.exists():
            integrity[case] = {'capture_error': True}
            continue
        events = read_events(trace)
        contexts = [e['payload'] for e in events if e['type'] == 'turn_context']
        items = [e['payload'] for e in events if e['type'] == 'response_item']
        calls = [x for x in items if x.get('type') in ('function_call', 'custom_tool_call')]
        outputs = [x for x in items if x.get('type') in ('function_call_output', 'custom_tool_call_output')]
        injected = []
        for item in items:
            if item.get('type') != 'message':
                continue
            text = ''.join(c.get('text', '') for c in item.get('content', []))
            for m in re.finditer(r'<skill>\s*<name>(.*?)</name>\s*<path>(.*?)</path>\n(.*?)\n</skill>', text, re.S):
                name, path, body = m.groups()
                injected.append({'name': name, 'path': path,
                                 'source_content_match_ignoring_trailing_newline': body.rstrip('\n') == Path(path).read_text().rstrip('\n'),
                                 'source_sha256': digest(Path(path))})
        core = (ROOT / 'method/CORE.md').read_text().rstrip('\n')
        core_outputs = [x for x in outputs if core in str(x.get('output', ''))]
        expected_path = str(ROOT / '.agents/skills' / skill / 'SKILL.md') if skill else None
        per_turn = []
        transcript.append(f'\n## {case}\n')
        for n, message in enumerate(messages, 1):
            prefix = directory / f'turn-{n}'
            stream = read_events(prefix.with_suffix('.stdout.jsonl'))
            cmd = json.loads(prefix.with_suffix('.command.json').read_text())
            transcript.append(f'\n### U{n}\n\n{message}\n\n### Assistant {n}\n')
            for entry in stream:
                if entry.get('type') == 'item.completed' and entry.get('item', {}).get('type') == 'agent_message':
                    transcript.append(entry['item']['text'] + '\n')
            per_turn.append({'turn': n,
                             'exit': int(prefix.with_suffix('.exit.txt').read_text()),
                             'completed': any(e.get('type') == 'turn.completed' for e in stream),
                             'command_explicit_read_only_never': 'sandbox_mode="read-only"' in cmd and 'approval_policy="never"' in cmd,
                             'command_isolated_flags': all(f in cmd for f in ['--ignore-user-config', 'skip_host_skill_discovery', 'plugins', 'memories'])})
        integrity[case] = {
            'expected_skill': expected_path,
            'injected_skills': injected,
            'selected_skill_matches': (len(injected) == 1 and injected[0]['path'] == expected_path) if skill else not injected,
            'full_core_in_tool_output': bool(core_outputs),
            'core_output_call_ids': [x.get('call_id') for x in core_outputs],
            'context_count': len(contexts),
            'all_contexts_expected': len(contexts) == len(messages) and all(c.get('model') == 'gpt-5.4-mini' and c.get('approval_policy') == 'never' and c.get('sandbox_policy', {}).get('type') == 'read-only' for c in contexts),
            'per_turn': per_turn,
            'calls': [{'name': x.get('name'), 'arguments': x.get('arguments', x.get('input')), 'call_id': x.get('call_id')} for x in calls],
            'tool_outputs': outputs,
            'trace_sha256': digest(trace),
        }
    (OUT / 'integrity.json').write_text(json.dumps(integrity, ensure_ascii=False, indent=2) + '\n')
    (OUT / 'transcripts.md').write_text('\n'.join(transcript))
    print(json.dumps({c: {k: v[k] for k in ['selected_skill_matches', 'full_core_in_tool_output', 'context_count', 'all_contexts_expected']} if not v.get('capture_error') else v for c, v in integrity.items()}, indent=2))


if __name__ == '__main__':
    main()
