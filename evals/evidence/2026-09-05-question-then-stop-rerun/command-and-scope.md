# Command and rerun scope

Exactly ten native cases were scheduled once: A1-A5, B1-B2, and D1-D3. No
discovery probe, ordinary prompt, Learn case, or retry is part of this run.

Each case starts in a fresh context with the required `$fp-*` token and exact U1.
Later turns use the captured session ID. Initial and resumed turns use
`gpt-5.4-mini`, `sandbox_mode="read-only"`, `approval_policy="never"`, ignored
user config, `skip_host_skill_discovery`, disabled plugins, and disabled
memories. Initial turns additionally pass `--sandbox read-only`.

The executable command shapes and exact fixture messages are preserved in
`run-10-cases.sh`. Raw stdout, raw stderr, and exit status are written to
absolute paths below
`/Users/quanglaam/fp-brain/evals/evidence/2026-09-05-question-then-stop-rerun/cases/`.

## Source hashes under test

```text
ea48a689ac7ea1357405dbe42ad23df380417b66d0d6eed12465127b2631c045  /Users/quanglaam/fp-brain/.agents/skills/fp-ask/SKILL.md
5710daf20a8018bf839da3a7c7daecdd95bbec1906e50963cdf4b6b21ef46037  /Users/quanglaam/fp-brain/.agents/skills/fp-brainstorm/SKILL.md
d3eb5eca2cbf350399e6c73bdd686abd4291d7c3bcf4a1f4dd9e70a7a182b7e3  /Users/quanglaam/fp-brain/.agents/skills/fp-decide/SKILL.md
a8755c07fd8e3526b8d04ec476b44dbcd10ef2511b82cc6a84b1f218a4e86485  /Users/quanglaam/fp-brain/method/CORE.md
77d60b6e53b5415c1f693f98e0cb32e878715d30b599fc071298856935ba1efd  /Users/quanglaam/fp-brain/evals/acceptance.md
```
