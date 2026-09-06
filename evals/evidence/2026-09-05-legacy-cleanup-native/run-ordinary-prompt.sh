#!/bin/bash
set -u

evidence_root=/Users/quanglaam/fp-brain/evals/evidence/2026-09-05-legacy-cleanup-native/ordinary-prompt
mkdir -p "$evidence_root"

codex exec \
  -C /Users/quanglaam/fp-brain \
  --sandbox read-only \
  -c 'sandbox_mode="read-only"' \
  -c 'approval_policy="never"' \
  --ignore-user-config \
  --enable skip_host_skill_discovery \
  --disable plugins \
  --disable memories \
  -m gpt-5.4-mini \
  --json \
  'Giải thích ngắn gọn loading state là gì trong UI.' \
  >"$evidence_root/stdout.jsonl" \
  2>"$evidence_root/stderr.txt"
status=$?
printf '%s\n' "$status" >"$evidence_root/exit.txt"

if [ "$status" -eq 0 ]; then
  thread_id=$(jq -r 'select(.type == "thread.started") | .thread_id' "$evidence_root/stdout.jsonl" | head -n 1)
  if [ -n "$thread_id" ] && [ "$thread_id" != null ]; then
    printf '%s\n' "$thread_id" >"$evidence_root/thread-id.txt"
  fi
fi
