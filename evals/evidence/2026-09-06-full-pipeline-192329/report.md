# Full native FP acceptance — 2026-09-06

**Behavioral result: 7 PASS / 5 FAIL / 0 NOT_RUN across the 12 fixtures.**
Failures: A1, A2, B1, D3, L2. Repo-local CLI discovery is PASS for all four
skills. The separate ordinary-prompt probe is PASS. Desktop picker and
real-user Ask usefulness are both NOT_RUN. This is not full product acceptance.

This is a fresh user-authorized full cycle on commit
`7c894c2` using `codex-cli 0.151.0` and `gpt-5.4-mini`. Each fixture was run
once in a fresh native session; turns within a fixture were resumed in order.
There were no retries, runtime edits, rubric edits, global config edits, or
commits. Two sessions maximum ran concurrently. The parent reviewer also
independently reviewed the disputed A2, D3, and L2 judgments.

## Per-criterion review

| Case | Result | Criteria met and failed |
|---|---|---|
| A1 | **FAIL** | U1 asks one useful question. Responses use the user's preceding observations; U3 gives an appropriately tentative statement for confirmation. But U2 already concludes that the problem is premature solutions and asks for confirmation before the desired help arrives at U3: clarification before conclusion FAIL. No prompt-skill diagnosis, immediate solution, or demand for root cause. |
| A2 | **FAIL** | The API explanation and designer bridge are correct; U2/U3 cover button → request → backend/database → response → UI. There is no Why loop, forced guessing, or unnecessary interview. Concision FAIL: U3 repeats the same flow as an opening chain, seven steps with two JSON examples, and a final chain, then adds another offer. This violates the existing short-explanation criterion; no new word-count threshold was introduced. |
| A3 | PASS | U1 asks for the observed drop-off. U2 restates the 8/10 observation without supplying a causal hypothesis. The user supplies the first hypothesis at U3; the agent explicitly calls it a hypothesis and asks for evidence. U4 asks for a test that can distinguish the user's explanation from another possibility. No cause is claimed proven. The fixture does not exercise the separate 'user cannot form any hypothesis' branch. |
| A4 | PASS | U2 stops interviewing and summarizes knowns/unknowns, including the absence of evidence and reproduction. It adds no question and no causal conclusion. The example problems remain unknown possibilities rather than established facts. |
| A5 | PASS | U1 treats phone reluctance as a hypothesis. U2 shifts to observing the submit button when the user checks it, without claiming a reproduced defect or presuming a downstream diagnostic result. U3 accepts the reproduction step and stops. It does not keep exploring phone reluctance. The unverified status is preserved by the future/conditional wording rather than an explicit knowns/unknowns statement. |
| B1 | **FAIL** | U1 clarifies rather than producing generic ideas. U2 nevertheless declares sufficient context and assumes 'order sent' means shipping: warehouse/carrier timeline, shipping time/tracking number, and proactive shipment alerts. It should clarify the unresolved meaning before generating these directions. U3 recovers with processing/success/failure feedback and delayed-response trade-offs, but recovery does not undo the U2 failure. No sibling Ask is loaded, and app facts are not presented as universal laws. |
| B2 | PASS | Three materially different mechanisms: disabling/changing the control according to known states, explicit action guidance, and retry safety conditioned on backend deduplication. Each connects to processing/success/failure or uncertainty about retry; assumptions are called out. The third needs backend support and is not established as available. No fabricated research result. |
| D1 | PASS | Recommends A because two days fits the three-day deadline and self-maintenance preference; explains lower customization as the trade-off. Does not re-ask known priorities, choose B merely for scale, fabricate an A/B property, or implement the choice. |
| D2 | PASS | U1 asks the missing priority without choosing or ranking either option. U2 recommends A using the newly supplied within-week validation goal and lack of customization need; explains the condition under which B becomes relevant. Does not ask the deadline again or implement anything. |
| D3 | **FAIL** | Correctly rejects migration based solely on a blog's 10x claim, names missing workload/configuration evidence, proposes testing, and does not fabricate tool identities/measurements or migrate. However, it never recognizes that the identities of X/Y and the concrete source are absent: that stated acceptance criterion is unmet. Native fact-research capability remains untested because this fixture supplies neither a concrete tool nor an accessible source. |
| L1 | PASS | Bridges Figma variants to state/data controlling UI and form behavior. U2 maps idle/submitting/success/error to the form. U3 rejects the 'only button color' misconception and gives a concrete counterexample: visually gray is not logically disabled. Explanations are expansive but remain about this concept and form example rather than opening a programming course. No root-cause demand or acceptance of the misconception. |
| L2 | **FAIL** | U2 stops immediately, with no mandatory teach-back, retrospective, or mastery claim. U1's confirmation is unsound: it says the user's correct definition needs correction, then contrasts submitting with 'real data'. This can teach a false separation between state and data instead of confirming the correct understanding with a useful scope limit. |

## Additional observed concerns

- A3 U2 meets this causal-hypothesis fixture but still gives a problem summary
  rather than neutrally inviting the user's explanation as the current Ask
  source requests. A3 PASS does not establish complete source adherence.
- L1 is verbose, and its U1 starts with 'right halfway' even though the user
  has expressed unfamiliarity rather than an incorrect explanation. These are
  quality concerns beyond the core concept/application checks it passes.
- A1 contains stray Persian text; L1 contains stray Hebrew text. The Vietnamese
  responses are otherwise understandable. These were not substituted for the
  existing behavioral failure criteria.
- D3's offer to devise a benchmark in '1–2 hours' has no supporting scope or
  workload information. It is an unsupported estimate, not an observed result.

## Native evidence and integrity

- **29/29 turns** completed with process exit 0 and native `turn.completed`:
  28 fixture turns plus one ordinary translation probe, across **13 persisted
  native sessions**. `cases/*/session-origin.txt` records original session paths;
  copied raw traces are `cases/*/session-rollout.jsonl`.
- Every initial and resumed command explicitly contains
  `-c sandbox_mode="read-only"` and `-c approval_policy="never"`. The capture
  also uses `--ignore-user-config`, enables `skip_host_skill_discovery`, disables
  `plugins` and `memories`, and pins `-m gpt-5.4-mini`. Initial exec commands
  additionally contain `--sandbox read-only`. All 29 actual native contexts
  report the expected model, read-only sandbox, and approval never.
- **12/12 fixture sessions** inject exactly the requested repo-local SKILL at
  `/Users/quanglaam/fp-brain/.agents/skills/fp-{ask,brainstorm,decide,learn}/SKILL.md`.
  Injected contents match the source after ignoring only the host-added trailing
  newline. Source files have exact byte SHA-256 values in `source-hashes.json`.
- **12/12 fixture sessions** complete tool calls whose outputs include the
  entire `method/CORE.md`. All 13 model tool calls are read-only `sed` commands
  (some also print a separator); they read only CORE and, for several cases,
  the same selected skill. All tool outputs have exit 0. There are no
  sibling/legacy/eval/archive reads or attempted mutations in these traces.
- The ordinary prompt is a translation request, exactly recorded in
  `fixtures.json`. It produces the translation, injects no SKILL body, reads
  no CORE, and makes zero tool calls. A natural response is not being
  misclassified as implicit FP invocation.
- Pre/post runtime hashes match across all nine runtime/metadata files.
  The fixture messages were extracted directly from `evals/acceptance.md`,
  preserving multiline text; the tested agent never received the rubric.
- Raw stderr is retained. Each turn emits host warnings about 32 malformed
  global agent-role definitions lacking `name`; one host shell-snapshot cleanup
  warning reports an already-missing file. These did not prevent completion.
  They are host configuration observations, not evidence of legacy FP loading.
- `--ignore-user-config` and disabled memories/plugins do not mean a sterile
  host: normal built-in instructions, project instructions, and the available
  skills catalog still appear in native contexts. This run proves the actual
  selected/read FP sources, not the absence of all host influence. Native host
  session/snapshot persistence is separate from tested-model file actions.

## Artifacts and remaining limits

`run-cases.py` is the exact capture harness; `fixtures.json` has exact messages;
`cases/*/turn-*.command.json` has exact argv; per-turn stdout, stderr, and exit
files preserve raw outcomes. `review-evidence.py` extracts `transcripts.md`
and checks `integrity.json`; it never reruns the model. `artifact-hashes.txt`
hashes every evidence file except itself, and `created-files.txt` inventories
this directory including its own path and the manifest.

All new files belong only to this new evidence directory. Existing evidence
and source remain unchanged. The parent will update `evals/results.md` after
independent review. No runtime repair follows automatically from these results.

Desktop picker, direct real-user Ask feedback, other models, repeated-run
reliability, and native technical research are not established by this cycle.
The prior B1 PASS is preserved as dated evidence; this run demonstrates that
passing once did not make the clarification behavior reliable on the same
current source and model.
