# Native attempt 01 — blocked before model output

Gate remains **PACKAGE_VALIDATED**. Native status: **BLOCKED_HOST_MODEL_COMPATIBILITY**. No behavioral PASS/FAIL has been established; installation and migration remain **NOT_RUN**.

The first N01 turn used Codex CLI **0.151.0**, `gpt-6-astra`, reasoning `high`, read-only sandbox and approval policy `never`. The host rejected the model with HTTP 400 stating that it requires a newer Codex app or CLI. The attempt ran from 2026-09-06 15:47:29 UTC to 15:47:43 UTC, returned exit 1 and produced **no assistant output**. No followup or additional session was launched. See [diagnostic extraction](N01-first-turn-diagnostics.json), [invocation](batch-1/N01/turn-01/invocation.json), [raw output](batch-1/N01/turn-01/stdout.jsonl), [result](batch-1/N01/turn-01/result.json) and [budget ledger](ledger.jsonl).

## Budget and case status

**1/52 sessions consumed**, with 51 slots numerically unconsumed under the existing budget. This count is not permission to bypass the setup stop condition or automatically retry N01. No runtime repair was performed; no full batch completed.

| Cases / slots | Current status |
|---|---|
| N01, first attempt | BLOCKED_HOST_MODEL_COMPATIBILITY; behavior NOT_GRADED; first turn only |
| N02, N03, N04, N05, N06, N07, N08, N09, N10, N11, N12, N13, N14, N15, N16, N17, N18, N19, N20 | NOT_RUN |
| Independent repeats N02, N05, N08, N11, N20 | NOT_RUN |
| O01 ordinary prompt | NOT_RUN |
| All potential second-batch sessions | NOT_RUN; no second batch started |

## What the evidence does and does not establish

The injected staged `SKILL.md` path resolves to the expected entry, and its body exactly matches the staged bytes: SHA256 `273a642e020a4fdb71f672e7167be212ad6c4f1d6b150adaf77b4f11ab0cd9ea`. The five package file maps match. Management package hash `3201cfb458bb7b51d81c5913965f8f1a729121f7fba0dc3d25026402397e6aa2` and runner tree hash `c79d1e0425c914c87800bfe2ad91d0e89f94565be7a97bf788fd4939833ad843` encode those same file hashes differently; this is not a candidate mismatch.

The raw turn context confirms `gpt-6-astra`/`high`, sandbox `read-only`, approval `never`. However, **165 ambient non-FP catalog entries** remained in developer context, despite requested discovery isolation. No FP rows appeared in that ambient catalog. Entry injection is verified, but complete clean context is **not proven**, and there is no observed model behavior or reference-reading behavior to grade. The original raw result remains `EXECUTION_ERROR` / `NOT_GRADED`; this report adds the diagnostic classification without editing it.

Candidate and workspace files were unchanged; temporary authentication material was removed according to the diagnostic record. Raw evidence, frozen fixtures/rubric, runtime, and historical outcomes are preserved.

## Next boundary

Hold dependent native execution while the parent performs a read-only investigation of available compatible runtimes and context isolation. No host upgrade, model substitution, rerun, runtime repair, install or migration follows automatically from this report. Continue only with a compatible, documented setup and an explicit accounted continuation decision within the approved budget. Product/UI/usefulness claims remain unestablished. See [current implementation status](../../../plans/2026-09-06-fp-rebuild/implementation-status.md).

## Recovery preparation (not launched)

Recovery preparation update: the parent reports finding an already installed Desktop CLI at `/Applications/ChatGPT.app/Contents/Resources/codex`, version **0.153.4**, through read-only inspection. No installation/update was needed. The [host-only protocol amendment](../../rebuild-v1/host-recovery-v1.md) is now prepared for the **second and final batch**, keeping the same candidate and model; no third batch or runtime repair is allocated. The executable is pinned to SHA256 `a30ec314bbd0e3721632234d07db7c99855db3b9f1e32dbe8c791947f07e7629`. No recovery launch is claimed; harness checks and parent review are required before launch, followed by a pause at the first N01 turn for provenance review. A complete final batch would total 27 sessions including the blocked attempt; unused budget does not authorize extra runs. The original N01 block and 1/52 count remain unchanged.
