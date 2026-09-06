# FP-Brain

FP-Brain is a local set of four explicit, advisory skills for reasoning from
first principles. It helps clarify problems, develop solution directions,
compare options, and understand concepts without executing work on the user's
behalf.

## Use the skills

- `$fp-ask` — clarify what you are stuck on, one useful question at a time.
- `$fp-brainstorm` — develop distinct directions from known facts and needs.
- `$fp-decide` — compare options against your priorities and available evidence.
- `$fp-learn` — understand a concept and apply it to the work in front of you.

Example:

```text
$fp-learn

I understand button variants in Figma, but I do not understand frontend state.
```

Each skill reads the shared method at [`method/CORE.md`](method/CORE.md). The
skills are explicit-only through their `agents/openai.yaml` policy, perform only
advisory responses and read-only research, and do not depend on one another or
on a global FP installation.

## Evidence status

The acceptance fixtures are in [`evals/acceptance.md`](evals/acceptance.md),
source mapping is in [`evals/provenance.md`](evals/provenance.md), and observed
results are in [`evals/results.md`](evals/results.md). Structural validation is
not the same as native behavioral acceptance; read the results before relying
on a PASS claim.
