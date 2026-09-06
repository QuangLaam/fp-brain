# Response-mode repair: authorized scope

Date: 2026-09-06

The user authorized a clean baseline commit, followed by separate handling of
A1, A3, and B1. This is a new repair cycle. Historical acceptance runs, their
stop conditions, fixtures, reports, and raw evidence remain unchanged.

Changes are restricted to Ask and Brainstorm. Ask selects one response mode
per turn and separates observation from a user-supplied causal hypothesis.
Brainstorm resolves a material event/capability ambiguity before generating
directions. Core, Decide, Learn, and all skill metadata remain unchanged.

Run the three failed cases A1/A3/B1 once each, followed by the four existing
regression cases for these two skills: A2/A4/A5/B2. Use the exact stored fixture
messages, without adding the rubric to the test conversation. No automatic
retry or editing while a case runs. An unresolved failure is reported honestly.
Decide/Learn and Desktop picker tests are outside this run.

The supervisor script captures exact command arguments, raw stdout/stderr,
exit status, thread IDs, persistent session copies, source hashes, and host
version. Each case starts a fresh native context; later messages resume only
that case. Initial and resumed commands both set read-only sandbox and approval
never. User config, plugins, and memories are disabled as in the earlier run.
The supervisor writes evidence; the tested skill does not write artifacts.

After execution, inspect actual selected skill paths, completed core reads,
configuration on every turn, attempted tool actions, and complete responses.
File validation and hashes alone do not establish native behavioral acceptance.
