# Ask grounding — supervised native rerun

Date: 2026-09-06

Host/model: codex-cli 0.151.0 / gpt-5.4-mini. Two fresh cases, seven completed
turns, one supervised rerun after the first candidate. Exact tested source
hashes, commands, fixtures, and raw sessions are stored alongside this report.

| Case | Result | Criterion review |
|---|---|---|
| A1 | FAIL | U1 asks a useful question. U2 gives a tentative problem statement and asks for confirmation before the user's desired help arrives at U3. That violates the clarification-only boundary and reproduces the original early-conclusion failure. U3 stays closer to supplied facts and no longer offers a prompting framework, but does not undo U2. |
| A3 | PASS | U1 asks where abandonment occurs; U2 neutrally invites the user's explanation without suggesting causes; U3 explicitly names it as a hypothesis and asks for support or contradictory evidence; U4 asks how to verify it. No cause is presented as proven. |

Total: **1 PASS, 1 FAIL**. No further repair or rerun was performed in this
cycle. The acceptance rubric and exact fixture messages were not changed.

## Evidence and limits

- Both cases load the correct repo-local Ask source, matching this directory's
  `source-hashes.json`, and read the complete shared core through completed tool
  calls. No legacy/sibling skill, eval rubric, or evidence file is read.
- All seven turns record gpt-5.4-mini, approval never, and read-only sandbox;
  all have zero process exit status and `turn.completed`.
- A1 is an observed instruction-following failure with the final source. It is
  not evidence of legacy FP resolution. Text instructions did not reliably
  enforce the clarification boundary in this model/context.
- First-run B1/B2 PASS still applies to the unchanged Brainstorm source. A2,
  A4, and A5 passed on the first Ask candidate and were not rerun after this
  narrow change. They are regression evidence for that candidate, not a fresh
  complete acceptance run of the final Ask source.
- Decide, Learn, implicit invocation, Desktop picker, real-use usefulness,
  other models, and general production advice quality were not tested here.

## Disposition

Two of the three target cases have passing native evidence on their final
skill sources: A3 and B1. A1 remains **OPEN / NOT ACCEPTED**. Retain the explicit
boundaries and the failed traces; do not introduce a fixed question count,
fixture-specific answers, or a larger runtime solely to obtain a PASS.
