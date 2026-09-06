# Native acceptance after global legacy cleanup

Date: 2026-09-05  
Host: `codex-cli 0.151.0`  
Model: `gpt-5.4-mini`  
Working directory: `/Users/quanglaam/fp-brain`

Every initial process used both `--sandbox read-only` and
`sandbox_mode="read-only"`; every resume repeated `sandbox_mode="read-only"`.
All initial and resumed turns used `approval_policy="never"`, disabled plugins
and memories, ignored user config, enabled `skip_host_skill_discovery`, and kept
the same model. The native rollouts record `gpt-5.4-mini`, `never`, and
`read-only` in every `turn_context`.

Exact command shapes are preserved in `discovery-command.txt`,
`behavior-command.txt`, and `ordinary-prompt-command.txt`. Exact fixture turns
and batching are preserved in `run-behavior-cases.sh`. Raw stdout, raw stderr,
exit status, thread ID, and the native session rollout are retained separately.

## Cleanup

The eight authorized targets were verified as real directories with no
symlinks, identified by content and tree digests in
`legacy-cleanup-manifest.md`, then deleted without a backup. All eight were
confirmed absent. The following protected paths remained present:

- `/Users/quanglaam/.agents/skills`
- `/Users/quanglaam/.agents`
- `/Users/quanglaam/fp-brain`
- `/Users/quanglaam/Documents/_Projects/fp-brain-codex`

## Prior evidence correction

The earlier claim that three JSONL traces were missing was disproved. They were
found under `/Users/quanglaam/evals/evidence/discovery/`, beginning with raw
runner stderr/warnings before valid JSON events. Each contains
`thread.started`, complete tool records, an agent message, and
`turn.completed`. Exact byte copies and matching hashes are retained in
`prior-discovery-correction/`. The recovered traces prove global legacy
resolution for Brainstorm and Decide; Learn additionally loaded
`_fp-brain-runtime`.

## Discovery

Each probe was a new ephemeral process and ran once. PASS requires a completed
tool trace that read the repo-local entrypoint and shared core, with no global
legacy, sibling skill, archive, or eval read.

| Skill | Result | Raw stdout SHA-256 | Loaded by completed command tool trace |
|---|---|---|---|
| Ask | PASS | `90879031787aeba98b40ccb41d3f2f1b71107c67cc1afc320ce79aa8d29ba40c` | `/Users/quanglaam/fp-brain/.agents/skills/fp-ask/SKILL.md`; `/Users/quanglaam/fp-brain/method/CORE.md` |
| Brainstorm | PASS | `727059dbf2f0439c589c1af5e0464fd2d46ff7f14245257501ef2e97583a1337` | `/Users/quanglaam/fp-brain/.agents/skills/fp-brainstorm/SKILL.md`; `/Users/quanglaam/fp-brain/method/CORE.md` |
| Decide | PASS | `628fa231a08f863598ecb06ad4f6c312cbb4c9eadaf6d0568f53377f72637259` | `/Users/quanglaam/fp-brain/.agents/skills/fp-decide/SKILL.md`; `/Users/quanglaam/fp-brain/method/CORE.md` |
| Learn | PASS | `fd402d43111b4b9ec3ee4f80be078bbd65fd51e7dc30fd78bd87fcff7cdbd7ec` | `/Users/quanglaam/fp-brain/.agents/skills/fp-learn/SKILL.md`; `/Users/quanglaam/fp-brain/method/CORE.md` |

All four stdout traces contain `turn.completed` and all four exit statuses are
zero. Raw stderr retains host warnings, including malformed unrelated global
agent roles and a post-completion model-refresh timeout on Learn; these do not
replace or erase the completed JSON event trace.

## Behavioral cases

The 12 cases started in 12 fresh native contexts and were not retried. The
native `skills.selected_skill_instructions` event inside each copied session
rollout records the exact repo-local entrypoint path and its content. Each
initial turn also has a completed command tool read of `method/CORE.md`. A scan
found no reads of `evals`, global FP paths, `_fp-brain-runtime`, sibling FP
skills, or archives. Later fixture messages were sent only through the captured
thread ID.

| Case | Result | Session rollout SHA-256 | Criterion-based review |
|---|---|---|---|
| A1 | FAIL | `8c50509e7455b732f2d9d4d32df1490a00694000a86fda00ce4ada6b3b459f9f` | U1 asked one useful question, but U2 stopped questioning and proposed a prompt-template solution before U3 clarified that the desired outcome was joint problem definition. The case did not ask one useful question on each clarification turn. |
| A2 | FAIL | `06a039a39629e3b1117e18a723c8b5b6b3117a9d34ca5adfb88bd128212c48c0` | U1 immediately delivered a broad API explanation instead of first locating the user's context or exact block. U2/U3 later gave the correct button to request to backend to database to response to UI flow, but the required first-turn behavior was missed. |
| A3 | FAIL | `5cb790533b8c39850e9dcdcf69731dc3b962567867b99aad1342ff9ca5573028` | U1 correctly asked for observations. After U2, however, the agent introduced privacy, trust, validation, and effort hypotheses and asked the user to choose a branch before the user supplied their own hypothesis. Later turns labeled uncertainty correctly, but the early hypothesis generation fails the case. |
| A4 | PASS | `b844fc2a3a403fb957b87c23f4997be1b861d659cf1625afd97d5ee9c4075698` | After the stop request, the agent summarized knowns and unknowns only, added no question, and asserted no cause. |
| A5 | PASS | `bc15fa8c8a8feaad90ac2e99e8a1d5ea44b0b7e0749414804a025cfae932ff09` | The initial phone concern stayed a hypothesis; the user report about the button was separated from a reproduced defect; after U3 the agent accepted reproduction as the next check and stopped the deeper inquiry. |
| B1 | FAIL | `61aeb4abec1e26df76a5c0a46e0c24c215bbd7e35e51806ab8b3772ab280f9a4` | U1 requested clarification, but U2 generated four shipment-oriented directions before the backend delay/state fact arrived at U3. It therefore fanned out before the fixture had supplied the facts needed to distinguish submission feedback from shipping status. |
| B2 | PASS | `acef411692097812241c117ff490c95d4186a69be9bbb68e6eda9424dae89356` | It produced exactly three materially different mechanisms, tied each to known processing/success/failure states and the resend need, and exposed a trade-off plus an assumption for each without inventing research results. |
| D1 | PASS | `71dcfcf3bb91b486861851d7bb8c35a529225098c354f12b60bcabeff186945e` | It recommended A from the stated three-day deadline and self-maintenance priority, while naming A's customization trade-off and the condition under which B would become relevant. |
| D2 | FAIL | `38246316e055fa36dd89d640f5bec81ba967b1433c5b287f6dc9df5f0220a29c` | U1 did ask the missing priority, but first declared A the practical default and attached unsupported cost/rework implications. That silently ranked speed before the user supplied the week-long validation goal. U2's later recommendation was aligned but does not erase the U1 failure. |
| D3 | PASS | `5ec25080f1d82e80dc6b6840819b6e8b2731da25048b398b32dba8b96a014800` | It treated 10x as an unverified claim, noted missing identities/config/workload, did not fabricate a benchmark or migrate, and recommended a bounded representative benchmark before any whole-product decision. |
| L1 | PASS | `6644554cc4b19f12e2d0307927712215ba79ccc380f0165df42e264f1e786c86` | It bridged Figma variants to live frontend data/state and the API-response loop, then corrected U3 with concrete behavior and data examples beyond button color. |
| L2 | PASS | `dfe1d2d89774b4cfc43fcf0ec5b79c35b2d8bf28bad533b252f36c884958474f` | It confirmed the user's model with a limited qualification about derived UI, did not claim mastery, and stopped immediately after U2. |

Behavioral fixture totals: **7 PASS, 5 FAIL, 0 NOT_RUN, 0
AMBIGUOUS_FIXTURE**.

## Ordinary prompt and manual evidence

The ordinary prompt ran once in a fresh native context without an FP name or
invocation token. Its session rollout hash is
`2217fa015dced93da953fc0eb8981106e4077df32cc353a4505e8af26fdb920d`.
It completed with exit zero and contains no
`skills.selected_skill_instructions` event and no repo-local FP selected path.
Result: **PASS for no observed implicit FP loading**. The natural content of the
model's answer was not used as evidence.

- Real-use Ask trial: **NOT_RUN**; there is no direct user problem plus feedback
  from a real use interaction in this maintenance run.
- Codex Desktop picker: **NOT_RUN**; there is no fresh user/UI picker evidence.

## Acceptance boundary

This run establishes clean repo-local native discovery and mixed behavioral
results for the exact fixtures above. It does not establish full product
acceptance, real-use Ask quality, or Desktop picker behavior. A green hash,
syntax result, exit code, or ordinary model response is not substituted for
those missing proofs.

Post-run verification confirmed that all nine files under `method/` and
`.agents/skills/` retained the exact source and metadata hashes captured before
cleanup. The repository remained on the unborn `main` branch with no commit
`HEAD`; its pre-existing untracked state was preserved. The six recovered
evidence originals outside the repo also retained their pre-copy hashes.
