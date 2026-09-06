# Acceptance results

## Current status — 2026-09-06

This table distinguishes current file inspection from dated native evidence.
Historical records below remain unchanged. PASS applies only to the named
case, source version, and host/model; it is not full product acceptance.

| Check | Current status | Latest evidence / limit |
|---|---|---|
| Runtime contents and dependencies | PASS (file inspection, 2026-09-06) | Exactly four repo-local skills; all core links resolve inside this repo; no legacy runtime dependency. |
| Global legacy paths | ABSENT (file inspection, 2026-09-06) | Seven `fp-*` names and `_fp-brain-runtime` are absent at the exact paths checked under `~/.agents/skills`, `~/.codex/skills`, and `~/.claude/skills`. This is not a scan of every host cache. |
| Repo-local native discovery | Observed for all four, on dated runs | Ask/Brainstorm: 2026-09-06 repair traces. Decide/Learn: [2026-09-05 post-cleanup run](evidence/2026-09-05-legacy-cleanup-native/native-run-report.md). |
| Ask A1 | FAIL / OPEN (2026-09-06, final source) | [Supervised rerun](evidence/2026-09-06-ask-grounding-rerun/report.md): U2 still concludes before desired help is clarified. |
| Ask A3 | PASS (2026-09-06, final source) | Same supervised rerun: user forms the first hypothesis; the agent explicitly labels it and asks for verification. |
| Ask A2/A4/A5 | PASS on first repair candidate only (2026-09-06) | [First repair run](evidence/2026-09-06-response-modes/report.md). Not rerun after the narrow conclusion/hypothesis wording correction. |
| Brainstorm B1/B2 | PASS (2026-09-06, current source) | First repair run: clarify before generation; preserve three distinct grounded directions when input is sufficient. |
| Decide D1–D3 | 3 PASS (2026-09-05, unchanged source) | [Earlier bounded rerun](evidence/2026-09-05-question-then-stop-rerun/native-rerun-report.md). Not rerun in this repair. |
| Learn L1–L2 | 2 PASS (2026-09-05, unchanged source) | Post-cleanup run. Not rerun in this repair. |
| Ordinary prompt / implicit invocation | PASS in one native case (2026-09-05) | Post-cleanup run; all four metadata files still set explicit-only invocation. No new implicit-invocation test. |
| Evidence integrity | PASS (2026-09-06) | All 255 historical manifest entries still match; new runs include source hashes, raw sessions, integrity summaries, and artifact manifests. Hash integrity is not behavioral acceptance. |
| Codex Desktop picker / real-use Ask trial | NOT_RUN | No fresh picker evidence or direct user trial feedback. |

**Target repair status: A3 and B1 accepted in the observed native runs; A1
remains open.** The first repair run was 5 PASS / 2 FAIL; the single supervised
A1/A3 rerun was 1 PASS / 1 FAIL. These are separate runs on different Ask
revisions, not one fully passing final-source suite.

## Historical records — initial build and subsequent runs

Date: 2026-09-05  
Repository: `/Users/quanglaam/fp-brain`  
Host: `codex-cli 0.151.0`

## Summary

| Check | Result | Evidence |
|---|---|---|
| Eight selected source hashes | PASS | All bytes matched `rebuild-contract.yaml` before implementation. |
| Four `SKILL.md` packages | PASS (structural only) | Codex `quick_validate.py` returned `Skill is valid!` for all four. |
| Four shared-core references | PASS (structural only) | Each `../../../method/CORE.md` resolved to `/Users/quanglaam/fp-brain/method/CORE.md`. |
| Explicit-only picker metadata | PASS (file validation only) | Every `agents/openai.yaml` sets `policy.allow_implicit_invocation: false`; native picker behavior was not verified. |
| Repo-local native skill discovery | FAIL | Both `$fp-ask` probes loaded `/Users/quanglaam/.agents/skills/fp-ask/SKILL.md` before or instead of the repo-local entrypoint. |
| A1–A5 | NOT_RUN | No valid multi-turn run loaded only the target Ask skill and core. A1 discovery probes are retained below but are not acceptance. |
| B1–B2 | NOT_RUN | Blocked by the same unresolved repo-local discovery issue; no simulation was promoted to native evidence. |
| D1–D3 | NOT_RUN | Blocked by the same unresolved repo-local discovery issue; no simulation was promoted to native evidence. |
| L1–L2 | NOT_RUN | Blocked by the same unresolved repo-local discovery issue; no simulation was promoted to native evidence. |
| Ordinary prompt / implicit invocation | NOT_RUN | A clean host context was unavailable, so natural model behavior could not be distinguished from FP loading. |
| Real-use Ask trial | NOT_RUN | The user was invited during the build; no real problem or feedback was received in this run. |

No behavioral case is marked PASS. Structure, syntax, hashes, and a plausible
single response are not substitutes for a clean native transcript.

## Runtime hashes

```text
a8755c07fd8e3526b8d04ec476b44dbcd10ef2511b82cc6a84b1f218a4e86485  method/CORE.md
a694b44cef91701a13c452b8ecff4a53552ae8fbaf4fdf8cec886da49da597e2  .agents/skills/fp-ask/SKILL.md
9538c06c59a3b31da9700835454b1059c4e672142bef01b16391b4d119bcc38d  .agents/skills/fp-brainstorm/SKILL.md
e2408f76b4320ddf7278f9ed125f5536c669b1dd1cbe529c36663c24755d8d75  .agents/skills/fp-decide/SKILL.md
c37af668e14546c18a698e00ba68c7fa7b16cab504ab4f62027c248fe8c37905  .agents/skills/fp-learn/SKILL.md
```

## A1 native discovery attempt 1 — invalid for acceptance

Configuration:

```text
codex exec -C /Users/quanglaam/fp-brain \
  --sandbox read-only \
  -c 'approval_policy="never"' \
  --ignore-user-config \
  --ephemeral \
  --json \
  '$fp-ask

“Tôi làm việc với AI thấy rất mệt. Tôi không biết phải hỏi gì.”'
```

Model: not pinned; the JSONL stream did not expose the resolved default model.  
Thread ID emitted by ephemeral runner: `01a07181-3c31-7b92-b969-f4d3f792fbe7`.

User:

> Tôi làm việc với AI thấy rất mệt. Tôi không biết phải hỏi gì.

Assistant message before tool calls:

> Mình sẽ dùng `fp-ask` để tách cảm giác “mệt” khỏi vấn đề thật sự cần quyết định,
> rồi đưa ra một cách làm đủ nhẹ để bạn áp dụng ngay. Vì đây là kỹ năng tư vấn,
> mình sẽ giữ mọi thứ chỉ-đọc và không thay đổi repository.

Tool trace:

```text
/bin/zsh -lc "sed -n '1,240p' /Users/quanglaam/.agents/skills/fp-ask/SKILL.md"
/bin/zsh -lc "sed -n '1,260p' .agents/skills/fp-ask/SKILL.md && sed -n '1,260p' FP_KERNEL.md && sed -n '1,300p' commands/ask.md"
/bin/zsh -lc "wc -l method/CORE.md && sed -n '1,400p' method/CORE.md"
```

The first call read the global pointer and contaminated the run. The second
read the repo-local skill, then failed on the two old-runtime paths. The third
read the target core successfully. The loaded repo-local file and core are the
same byte versions identified by the hashes above; the global pointer directed
the agent to `FP_KERNEL.md` and `commands/ask.md`, neither of which exists in the
rebuilt repository.

Final assistant message:

> “Mệt” là điều bạn quan sát được; “không biết hỏi gì” có thể chỉ là biểu hiện,
> chưa chắc là nguyên nhân.
>
> Hãy lấy một tình huống thật gần đây: **Lần gần nhất mở AI rồi bị khựng lại,
> bạn đang muốn hoàn thành việc gì?**

Meaning-based review: the final response itself asks one useful question and
does not force a root-cause guess, but the run loaded a global FP skill and old
runtime instructions. Result: **INVALID / NOT ACCEPTANCE**.

## A1 native discovery attempt 2 — one allowed rerun, invalid

The rerun added the available isolation controls and pinned the model:

```text
codex exec -C /Users/quanglaam/fp-brain \
  --sandbox read-only \
  -c 'approval_policy="never"' \
  --ignore-user-config \
  --ephemeral \
  --enable skip_host_skill_discovery \
  --disable plugins \
  --disable memories \
  -m gpt-5.4-mini \
  --json \
  '$fp-ask

“Tôi làm việc với AI thấy rất mệt. Tôi không biết phải hỏi gì.”'
```

Model: `gpt-5.4-mini`  
Thread ID emitted by ephemeral runner: `01a07184-5c58-71e0-828d-3900bb9fc224`.

User:

> Tôi làm việc với AI thấy rất mệt. Tôi không biết phải hỏi gì.

Assistant messages and tool trace, in order:

1. Assistant: “Tôi sẽ dùng skill `fp-ask` để trả lời theo khung hỏi - đáp của
   repo này, rồi đọc `SKILL.md` và `method/CORE.md` để bám đúng cách làm trước
   khi phản hồi.”
2. Tool: read `/Users/quanglaam/.agents/skills/fp-ask/SKILL.md` and
   `/Users/quanglaam/fp-brain/method/CORE.md`. The global pointer was still
   loaded; the repo-local Ask entrypoint was not read in this command.
3. Assistant: “Tôi đang đọc hai file gốc của runtime để không đoán mò về quy
   trình trả lời. Sau đó tôi sẽ chuyển câu của bạn thành một khung hỏi rất ngắn,
   dùng được ngay.”
4. Tool: tried `/Users/quanglaam/fp-brain/FP_KERNEL.md` and
   `/Users/quanglaam/fp-brain/commands/ask.md`; failed because the old-runtime
   paths do not exist.
5. Assistant: “`FP_KERNEL.md` không nằm ở chỗ skill pointer nói tới, nên tôi sẽ
   xác định đúng vị trí trong repo rồi mới trả lời. Sau đó tôi sẽ tóm lại theo
   cách ngắn nhất có thể, vì đây là một vấn đề ‘không biết hỏi gì’ chứ chưa phải
   vấn đề kỹ thuật.”
6. Tool: searched the target repo for old runtime paths; no matches.
7. Tool: listed visible repo files. Dotfiles were omitted, so the repo-local
   `.agents/skills/fp-ask/SKILL.md` was not recovered.

Exact tool calls:

```text
/bin/zsh -lc "sed -n '1,220p' /Users/quanglaam/.agents/skills/fp-ask/SKILL.md && printf '\n---CORE---\n' && sed -n '1,260p' /Users/quanglaam/fp-brain/method/CORE.md"
/bin/zsh -lc "sed -n '1,240p' /Users/quanglaam/fp-brain/FP_KERNEL.md && printf '\n---ASK---\n' && sed -n '1,260p' /Users/quanglaam/fp-brain/commands/ask.md"
/bin/zsh -lc "rg --files /Users/quanglaam/fp-brain | rg '(^|/)(FP_KERNEL\.md|ask\.md)$|commands/ask\.md|FP_KERNEL\.md'"
/bin/zsh -lc "rg --files /Users/quanglaam/fp-brain | sed -n '1,240p'"
```

Final assistant message:

> Bạn không cần “biết hỏi hay” ngay. Vấn đề thường là câu hỏi đang ở mức quá mơ hồ.
>
> Cách nghĩ đúng là:
>
> - Không hỏi: “Làm sao dùng AI tốt hơn?”
> - Hỏi: “Tôi đang cố làm việc gì cụ thể, và AI nên giúp phần nào?”
>
> Mẫu tối thiểu để hỏi AI:
>
> ```text
> Mục tiêu: ...
> Bối cảnh: ...
> Đầu vào tôi có: ...
> Ràng buộc: ...
> Hãy làm 1 trong 3 việc:
> 1. làm rõ vấn đề,
> 2. đề xuất phương án,
> 3. tạo bản nháp để tôi chỉnh.
> Nếu thiếu dữ liệu, hãy hỏi lại trước.
> ```
>
> Ví dụ:
>
> ```text
> Tôi muốn viết landing page cho một sản phẩm AI.
> Bối cảnh: đối tượng là designer chuyển sang build sản phẩm.
> Đầu vào: chưa có cấu trúc nội dung.
> Ràng buộc: giọng điệu rõ ràng, không sáo rỗng, ngắn gọn.
> Hãy đề xuất 3 cấu trúc landing page và chọn cấu trúc tốt nhất.
> ```
>
> Nếu bạn đang mệt vì AI, thường là vì bạn đang dùng nó như “máy trả lời”, trong
> khi nên dùng nó như “người làm rõ vấn đề”.
>
> Một câu hỏi hữu ích hơn để bắt đầu là:
>
> ```text
> Hãy giúp tôi làm rõ vấn đề này bằng 5 câu hỏi ngắn trước khi đưa giải pháp.
> ```
>
> Nếu muốn, tôi có thể làm ngay cho bạn một `prompt khung` riêng cho công việc
> của bạn, theo 1 trong 4 loại:
> 1. viết
> 2. thiết kế
> 3. nghiên cứu
> 4. code / AI product

Meaning-based review: the response gives a solution before clarification,
asserts a likely cause without evidence, and does not ask exactly one useful
question. It fails A1's observable criteria, but because it did not load the
repo-local Ask skill it is evidence of **discovery FAIL**, not evidence that the
implemented Ask behavior itself failed.

## Host effects and stopping reason

Both probes were read-only and ephemeral. Even with user config, plugins, and
memories disabled, the host traversed `/Users/quanglaam/.agents/skills` above
the repository and resolved the older same-name pointer. The runner also emitted
warnings about malformed global agent-role definitions and skill-description
budget pressure. Those warnings did not originate in this repository.

The contract permits one rerun after a failure. Further prompts would test the
same contaminated path, so the remaining behavioral fixtures were not run. A
trustworthy next run needs a fresh host context that demonstrably resolves each
skill to `/Users/quanglaam/fp-brain/.agents/skills/.../SKILL.md` without first
loading the older `/Users/quanglaam/.agents/skills/fp-*` pointer.

## 2026-09-05 verification follow-up

The source and global-pointer hashes were rechecked with `codex-cli 0.151.0`.
The five rebuilt runtime hashes still match the values recorded above. The four
same-name global files are separate files with these hashes:

```text
35df1cb4995568a613443e2927acc8fea0ef4edc67d01adcb6395b70058d65c2  /Users/quanglaam/.agents/skills/fp-ask/SKILL.md
ad214fe7a565dd8f9e94e545902d8d726e1e3d1c494be9a9e71b8b48d9ef3f61  /Users/quanglaam/.agents/skills/fp-brainstorm/SKILL.md
7855e0e72975c7c041269123fbdcac7585b9e6c3dbb98caa652c93caf7605654  /Users/quanglaam/.agents/skills/fp-decide/SKILL.md
bbcdafb66d38fb6bf1e4874aa666db8517024af5057bd5f600ebd5edd1c15ac1  /Users/quanglaam/.agents/skills/fp-learn/SKILL.md
```

Each global file points to the obsolete rebuilt-repo paths `FP_KERNEL.md` and
`commands/{ask,brainstorm,decide,learn}.md`. Those paths do not exist in this
rebuild. File inspection alone does not prove which file a particular native
run loaded.

One discovery-only probe was started for each of Brainstorm, Decide, and Learn
with the same model and isolation configuration as Ask attempt 2. The exact
command template was:

```text
codex exec -C /Users/quanglaam/fp-brain --sandbox read-only \
  -c 'approval_policy="never"' --ignore-user-config --ephemeral \
  --enable skip_host_skill_discovery --disable plugins --disable memories \
  -m gpt-5.4-mini --json \
  '$fp-{brainstorm|decide|learn}

Kiểm tra đường dẫn skill bạn đang sử dụng. Chỉ đọc các tệp hướng dẫn cần thiết rồi báo chính xác đường dẫn đã nạp; không giải bài toán hành vi nào.'
```

All three processes exited `0`, with stdout lengths 32,104, 33,108, and 45,320
bytes respectively. The orchestration wrapper failed to persist the captured
stdout, and `--ephemeral` left no recoverable session JSONL. Therefore the
resolved paths and thread IDs from those three probes are **UNVERIFIABLE** and
the probes are **INVALID AS EVIDENCE**. They must not be represented as PASS or
FAIL for repo-local discovery. They were not repeated.

Classification: **ENVIRONMENT / EVIDENCE-CAPTURE FAILURE**. This is not a
behavioral failure of the rebuilt skills and not an ambiguous fixture. No
behavioral acceptance case was run in this follow-up.

## 2026-09-05 correction to the verification follow-up

The six intended Brainstorm/Decide/Learn probe files were later found at
`/Users/quanglaam/evals/evidence/discovery/`. The prior statement that the
wrapper did not create the JSONL files and that their contents were
unrecoverable is incorrect. The files were written under the wrong working
directory.

Although raw runner stderr/warnings precede the JSON events, each recovered
JSONL contains a `thread.started` event, complete command tool records, a final
agent message, and `turn.completed`. The recovered commands and traces were
copied byte-for-byte, without deleting or overwriting the originals, to:

`/Users/quanglaam/fp-brain/evals/evidence/2026-09-05-legacy-cleanup-native/prior-discovery-correction/`

Recovered trace conclusions:

| Probe | Corrected result | Tool-trace evidence |
|---|---|---|
| Brainstorm | Discovery FAIL | Loaded `/Users/quanglaam/.agents/skills/fp-brainstorm/SKILL.md`, then the rebuilt core. |
| Decide | Discovery FAIL | Loaded `/Users/quanglaam/.agents/skills/fp-decide/SKILL.md`, then the rebuilt core. |
| Learn | Discovery FAIL | Loaded `/Users/quanglaam/.agents/skills/fp-learn/SKILL.md`, the rebuilt core, and legacy `_fp-brain-runtime/FP_KERNEL.md` plus `commands/learn.md`. |

This corrects evidence location and classification only. It does not convert
any behavioral fixture to PASS or FAIL: these were discovery probes, and their
failure is attributable to global legacy resolution rather than the rebuilt
skill source.

## 2026-09-05 post-cleanup native acceptance

This is a new, bounded run after removal of the eight user-authorized global FP
legacy targets. It does not rewrite or rerun the historical gates above.

Full evidence and criterion-by-criterion review:
`/Users/quanglaam/fp-brain/evals/evidence/2026-09-05-legacy-cleanup-native/native-run-report.md`.

| Check | Result |
|---|---|
| Global legacy cleanup | PASS: eight exact targets deleted without backup after identity/hash checks; protected roots retained. |
| Prior Brainstorm/Decide/Learn trace correction | PASS: six files recovered from the wrong cwd, copied byte-for-byte, and reclassified as discovery FAIL caused by global legacy resolution. |
| Repo-local discovery | PASS 4/4 by completed command tool trace for each repo-local entrypoint and shared core. |
| A1–A5 | 2 PASS, 3 FAIL: A4/A5 pass; A1/A2/A3 fail their stated interaction criteria. |
| B1–B2 | 1 PASS, 1 FAIL: B2 passes; B1 brainstorms before the delayed backend fact arrives. |
| D1–D3 | 2 PASS, 1 FAIL: D1/D3 pass; D2 silently defaults to A before user priority is known. |
| L1–L2 | 2 PASS, 0 FAIL. |
| Ordinary prompt / implicit FP loading | PASS: no selected-skill event or FP selected path; answer style was not used as evidence. |
| Real-use Ask trial | NOT_RUN: no direct user problem and feedback evidence. |
| Codex Desktop picker | NOT_RUN: no fresh UI/picker evidence. |

Behavioral fixture total: **7 PASS, 5 FAIL, 0 NOT_RUN, 0
AMBIGUOUS_FIXTURE**. No case was retried. Every case independently records the
repo-local selected skill path, core read, `gpt-5.4-mini`, read-only sandbox,
approval never, raw stdout/stderr, completion, thread ID, and session hash.

## 2026-09-05 question-then-stop bounded rerun

This section appends a new result; it does not revise the historical results
above. A2 is evaluated under the new decision recorded in `evals/acceptance.md`:
a clear knowledge question may receive a direct explanation without a mandatory
context interview.

Full report and trace hashes:
`/Users/quanglaam/fp-brain/evals/evidence/2026-09-05-question-then-stop-rerun/native-rerun-report.md`.

| Case | Result | Short reason |
|---|---|---|
| A1 | FAIL | U2 concludes and offers a solution while a material clarification is still unresolved. |
| A2 | PASS | Direct knowledge explanation; U2/U3 correctly connect UI action through API/backend to UI response. |
| A3 | FAIL | U2 introduces the first candidate causes before the user forms a hypothesis. |
| A4 | PASS | Honors stop and returns only knowns/unknowns. |
| A5 | PASS | Updates to new evidence, preserves uncertainty, and stops after the user's next check. |
| B1 | FAIL | U2 generates and recommends directions before the delayed backend-state fact. |
| B2 | PASS | Exactly three distinct, evidence-linked directions with assumptions. |
| D1 | PASS | Recommends A from known deadline/maintenance priorities and states the trade-off. |
| D2 | PASS | U1 asks one priority question and stops; U2 recommends A conditionally. |
| D3 | PASS | Rejects unsupported migration and proposes a bounded benchmark. |

Total: **7 PASS, 3 FAIL, 0 NOT_RUN, 0 AMBIGUOUS_FIXTURE**. Exactly one run per
case; no retry. The three failures are reported as observed model non-compliance
with explicit updated instructions. No follow-up fix or rerun was performed.


## 2026-09-06 repository baseline and separate behavior repair

- Baseline commit `aa99d99` preserves the four skills and all historical
  evidence, adds the current-status table and `.gitignore`, and excludes the
  removed Finder `.DS_Store` metadata.
- The separate repair changes only Ask and Brainstorm runtime instructions.
  Core, Decide, Learn, metadata, provenance, and the acceptance rubric remain
  unchanged. Ask chooses one response mode per turn; Brainstorm resolves
  material event/capability ambiguity before generating directions.
- [First repair run](evidence/2026-09-06-response-modes/report.md): A1/A3/B1 plus
  A2/A4/A5/B2 regression fixtures; 5 PASS / 2 FAIL across nineteen turns.
- Full review caught unsupported A1 conclusions and missing explicit A3
  hypothesis labeling. A narrow Ask correction received one
  [supervised A1/A3 rerun](evidence/2026-09-06-ask-grounding-rerun/report.md):
  1 PASS / 1 FAIL across seven turns. A3 passes; A1's early conclusion persists.
- No historical fixture/result was rewritten, no retry replaced a failed
  trace, and no full acceptance claim is made. Final Ask regression coverage
  remains limited as shown in the current-status table.
