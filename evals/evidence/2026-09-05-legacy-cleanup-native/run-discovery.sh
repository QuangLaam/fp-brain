#!/bin/bash
set -u

evidence_root=/Users/quanglaam/fp-brain/evals/evidence/2026-09-05-legacy-cleanup-native/discovery
mkdir -p "$evidence_root"

run_probe() {
  skill_name="$1"
  prompt="\$${skill_name}

Discovery-only probe. Use read-only terminal tools to read the skill entrypoint you resolved and every shared method file that entrypoint instructs you to read. Do not read any evals, acceptance criteria, test fixtures, memories, sibling FP skill, archive, or legacy runtime. Do not solve a behavioral task. In the final response, report the exact absolute paths actually read."

  codex exec \
    -C /Users/quanglaam/fp-brain \
    --sandbox read-only \
    -c 'sandbox_mode="read-only"' \
    -c 'approval_policy="never"' \
    --ignore-user-config \
    --ephemeral \
    --enable skip_host_skill_discovery \
    --disable plugins \
    --disable memories \
    -m gpt-5.4-mini \
    --json \
    "$prompt" \
    >"$evidence_root/${skill_name}.stdout.jsonl" \
    2>"$evidence_root/${skill_name}.stderr.txt"
  status=$?
  printf '%s\n' "$status" >"$evidence_root/${skill_name}.exit.txt"
}

run_probe fp-ask
run_probe fp-brainstorm
run_probe fp-decide
run_probe fp-learn
