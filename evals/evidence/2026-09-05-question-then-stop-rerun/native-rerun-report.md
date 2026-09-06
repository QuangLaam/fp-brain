# Ask / Brainstorm / Decide bounded rerun

Date: 2026-09-05  
Repository: `/Users/quanglaam/fp-brain`  
Host/model: `codex-cli 0.151.0` / `gpt-5.4-mini`

## Result

Exactly A1-A5, B1-B2, and D1-D3 were run once each. Seven cases pass and
three fail. In accordance with the approved stop condition, no failed case was
edited or rerun.

| Case | Result | Trace SHA-256 | Review |
|---|---|---|---|
| A1 | **FAIL** | `b01bbbaf7b12a1d0f206eae3b5237f19655a60f0c8ccb40afe89917541e3c6bb` | U1 asks one useful question. At U2, while the response mode is still unresolved, the model supplies a problem statement, known/unknown analysis, and an offer of a solution instead of asking one question and stopping. |
| A2 | **PASS** | `90f97ff84c58a52e425f2417043759c243fd5477c0eeefedbce6f66c20a86a4f` | The clear knowledge question is answered directly without an unnecessary interview; U2/U3 connect button, frontend, API request, backend/database, response, and UI states. This is evaluated under the new A2 decision only. |
| A3 | **FAIL** | `ba287ac6fe131fe3e886c15708378cc4864b483817c7294c2a911b581b0728b1` | At U2 the model introduces the first candidate causes (`PII`, form weight, validation, insufficient value) before the user supplies a hypothesis. Later turns correctly label and test the user's hypothesis, but do not undo the U2 failure. |
| A4 | **PASS** | `c4087b40909c64d6dcc49c30ef15ec7abedd91c555f737d0bab0a1ff1d20ee12` | After the stop request, it gives only knowns and unknowns, with no further question or causal conclusion. |
| A5 | **PASS** | `eb055a2b75954c7b0e910551e85f417f526d792dced5450d6c370723ceaacd1e` | It updates the inquiry from the phone-number hypothesis to the reported button behavior, distinguishes the report from reproduction, then accepts the user's verification step and stops. |
| B1 | **FAIL** | `f22f03ac70dd8ad3589b713d814392b2d1ba2653c5b58465e058fff59707a5fa` | At U2, before the backend states and delay are known, the model lists four directions and recommends a combination. The U3 fact materially changes the directions, so U2 should have been clarification-only. |
| B2 | **PASS** | `533d34c4e14ef2e6a4d84e6476ebcf89e128447d39e9a6169d7d4ea6c070b0c5` | It gives exactly three materially different mechanisms, tied to known states and the retry need, with trade-offs and assumptions to test. |
| D1 | **PASS** | `61adfbf38ac7d5855d2c216710818280af27036cc206d1caf8b7ccace24c95d3` | It recommends A from the stated deadline and maintenance priority, and names the customization trade-off. |
| D2 | **PASS** | `96ed3e8d873f7339c1c3d2f3ae73a677b413ece925170529eb7675c5c201d85e` | U1 is one priority question and stops; after U2 it recommends A conditionally without asking again for an already-resolved deadline. |
| D3 | **PASS** | `ecae86a9e4dbe489ad06c05434e4389cc0de8110a59e114e16844518158806e3` | It treats the blog figure as an unverified claim, does not invent X/Y or migrate, and recommends a bounded workload-specific benchmark. |

The three failures are classified as **observed model non-compliance with the
updated source**, not three new source defects: the applicable Ask/Brainstorm
instructions explicitly contain the required stop or hypothesis boundary, the
fixtures supply the delayed information, and the native traces load the correct
repo-local skill and core. This run does not authorize another source change.

## Diff under test

- `fp-ask`: clarification-only response when a missing answer can change the
  problem or next action; direct concise explanation for a clear knowledge gap.
- `fp-brainstorm`: clarification-only response for material ambiguity,
  including user event and available system states; no mandatory interview when
  facts are sufficient.
- `fp-decide`: unresolved user-owned priority requires one question and stop;
  direct recommendation remains allowed when priorities are clear.
- `evals/acceptance.md`: A2 now accepts a direct knowledge explanation and
  records that historical results retain their original rubric.

Old to new hashes:

```text
fp-ask        a694b44cef91701a13c452b8ecff4a53552ae8fbaf4fdf8cec886da49da597e2
           -> ea48a689ac7ea1357405dbe42ad23df380417b66d0d6eed12465127b2631c045
fp-brainstorm 9538c06c59a3b31da9700835454b1059c4e672142bef01b16391b4d119bcc38d
           -> 5710daf20a8018bf839da3a7c7daecdd95bbec1906e50963cdf4b6b21ef46037
fp-decide     e2408f76b4320ddf7278f9ed125f5536c669b1dd1cbe529c36663c24755d8d75
           -> d3eb5eca2cbf350399e6c73bdd686abd4291d7c3bcf4a1f4dd9e70a7a182b7e3
acceptance    54c84e4b43bc159ca77f989de96518b0f79c05bf0141ab9d7d89fa72e5b26c4b
           -> 77d60b6e53b5415c1f693f98e0cb32e878715d30b599fc071298856935ba1efd
```

`quick_validate.py` passed for the three edited skill packages. This is
structural validation only.

## Native evidence integrity

- Every case has a fresh thread ID, the exact expected number of completed
  turns, zero process exit status, raw stdout/stderr, and the copied persistent
  native session rollout.
- Every rollout records `gpt-5.4-mini`, approval `never`, and read-only sandbox
  on every turn.
- Each selected-skill event contains the expected repo-local Ask, Brainstorm, or
  Decide path. Completed read-only tool calls load `method/CORE.md`; any repeated
  skill read is the same selected entrypoint. No sibling FP skill, legacy
  runtime, or eval rubric was read by a case.
- The runner, exact fixture messages, command shape, and source hashes are in
  `run-10-cases.sh` and `command-and-scope.md`. `artifact-hashes.txt` covers the
  complete evidence directory after this report is finalized.

## Acceptance limits

This proves only the observed behavior of these ten native fixture runs against
the updated rubric and source versions. It does not establish deterministic
model compliance, broad host behavior, ordinary-prompt non-invocation, Codex
Desktop picker/loading, real-user usefulness, or Learn behavior. Historical
results remain unchanged. `CORE.md`, Learn, skill metadata, and configuration
were outside the edit scope and retain their pre-run hashes.
