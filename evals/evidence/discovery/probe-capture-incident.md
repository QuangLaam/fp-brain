# Discovery probe capture incident

Date: 2026-09-05
Host: `codex-cli 0.151.0`
Model requested: `gpt-5.4-mini`

Three discovery-only probes were executed once for `fp-brainstorm`,
`fp-decide`, and `fp-learn`. Each used `--sandbox read-only`,
`approval_policy="never"`, `--ignore-user-config`, `--ephemeral`,
`skip_host_skill_discovery`, disabled plugins, and disabled memories.

The commands exited successfully, but the wrapper's patch step did not create
the intended JSONL files. Because the runs were ephemeral, the original stdout
and thread IDs could not be recovered. No conclusion about the resolved skill
path is drawn from these runs, and they were not repeated.

Recorded stdout byte counts:

- `fp-brainstorm`: 32,104
- `fp-decide`: 33,108
- `fp-learn`: 45,320

Classification: `ENVIRONMENT / EVIDENCE-CAPTURE FAILURE`.

## Correction — 2026-09-05

The six intended files were later found under the wrong working directory:
`/Users/quanglaam/evals/evidence/discovery/`. The earlier statement that the
JSONL files were not created and could not be recovered is incorrect.

The three JSONL files begin with runner stderr/warnings before the JSON events;
that mixed framing does not mean the traces are missing. Each file contains a
`thread.started` event, completed tool events, a final agent message, and a
`turn.completed` event.

The recovered tool traces establish:

- Brainstorm read `/Users/quanglaam/.agents/skills/fp-brainstorm/SKILL.md` and
  `/Users/quanglaam/fp-brain/method/CORE.md`.
- Decide read `/Users/quanglaam/.agents/skills/fp-decide/SKILL.md` and
  `/Users/quanglaam/fp-brain/method/CORE.md`.
- Learn read `/Users/quanglaam/.agents/skills/fp-learn/SKILL.md`, the rebuilt
  core, and the legacy `_fp-brain-runtime/FP_KERNEL.md` plus
  `_fp-brain-runtime/commands/learn.md`.

Therefore these probes are now classified as **recovered discovery FAIL** due
to global legacy resolution, not evidence-capture failure and not rebuilt
source behavior failure. Exact byte copies and hashes are retained at
`/Users/quanglaam/fp-brain/evals/evidence/2026-09-05-legacy-cleanup-native/prior-discovery-correction/`.
