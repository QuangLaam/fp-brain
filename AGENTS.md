# FP-Brain repository guidance

This repository contains four explicit, advisory first-principles skills. Keep
runtime work read-only and side-effect free. A request to build, edit, install,
execute, delegate, commit, or publish is outside an FP skill and needs separate
authorization.

The shared method is [`method/CORE.md`](method/CORE.md). Public skill entrypoints
are under `.agents/skills/fp-{ask,brainstorm,decide,learn}/`. Each entrypoint
must reach the core through its repository-relative link and must not depend on
global FP skills, plugins, hooks, planning files, archives, or another FP skill.

For acceptance work, use [`evals/acceptance.md`](evals/acceptance.md) and record
actual evidence in `evals/results.md`. Syntax checks, hashes, or simulations do
not establish native behavioral acceptance.
