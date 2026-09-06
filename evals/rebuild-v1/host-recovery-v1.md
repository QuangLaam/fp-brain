# Bounded host recovery v1

Authorized by the coordinating parent after the first native attempt on
2026-09-06. This is an additive execution-protocol amendment. The frozen
cases, messages, branch predicates, rubric, source data and freeze manifest
remain unchanged.

The preserved campaign is
`evals/evidence/2026-09-06-fp-rebuild-native-bounded-01/`. Batch 1 consumed
one N01 session, `01a07767-4158-7803-953d-c03410d67d8f`. CLI 0.151.0 returned
HTTP 400 stating that gpt-6-astra requires a newer Codex version. The raw
trace contains no model response or model tool call. This is a host
compatibility block, not a behavioral failure or a free attempt. Its ledger,
raw evidence, diagnostics and outcomes must remain intact.

## One final batch

Batch 2 consumes the only allowed repair opportunity as a **host setup
repair**. It uses the already installed desktop executable directly:

- Path: `/Applications/ChatGPT.app/Contents/Resources/codex`
- Version: `codex-cli 0.153.4`
- SHA256: `a30ec314bbd0e3721632234d07db7c99855db3b9f1e32dbe8c791947f07e7629`

No installation, update, global configuration change, model change, runtime
package repair, third batch, budget reset, or automatic retry is authorized.
The path, version and executable hash are stored per batch and verified before
each initial/resumed turn. If any pin changes, stop without a replacement run.

The same immutable five-file candidate is allowed for this exception only:
runner tree SHA256
`c79d1e0425c914c87800bfe2ad91d0e89f94565be7a97bf788fd4939833ad843`.
The management manifest hash
`3201cfb458bb7b51d81c5913965f8f1a729121f7fba0dc3d25026402397e6aa2`
uses a different aggregate encoding over the same file map. The runner must
verify that batch 2's map and tree hash equal batch 1's immutable candidate.

The exception requires all of the following before creating batch 2:
exactly one existing batch; exactly one consumed session, N01; its recorded
execution error is the stated CLI/model incompatibility; its complete raw
trace contains no assistant response or model tool call; no case is running
or awaiting a followup; and an explicit parent review gate and repair evidence
reference are supplied. It cannot be reused for a behavioral failure.

## Evidence and acceptance

The 52-session global ceiling and two-concurrent-session ceiling remain.
Batch 2 contains the same 26 authorized slots: N01-N20, the five specified
independent repeats, and the ordinary prompt. A complete batch 2 therefore
uses 27 sessions cumulatively, including the blocked batch 1 attempt. Unused
capacity does not authorize any third batch or additional probes.

Model and reasoning remain gpt-6-astra/high. Initial and resume keep explicit
read-only sandbox, approval-never, ignored user config, disabled plugins and
memories, and the agreed host-skill-discovery setting. N14 alone enables live
web. Host execpolicy rules remain active. Candidate, executable and config
must stay fixed throughout the final batch (apart from N14's predefined web
capability). All 26 final slots must pass on that one snapshot for native
acceptance; batch 1 contributes no behavioral PASS to the final result.

The first N01 turn remains the provenance gate and consumes its normal slot.
Pause after that turn for the parent's independent review of actual injected
skill path/content, model/config and ambient context. Do not start another
case or send a followup until the parent explicitly releases it. A catalog
listing alone is not a selected skill, and staging flags alone do not prove
complete isolation. Normalize filesystem aliases when comparing paths while
preserving their original spellings in evidence.

Before any batch 2 session, the amended runner receives harness-only tests
and independent parent review. Harness tests consume no model sessions and
are never reported as behavioral acceptance.
