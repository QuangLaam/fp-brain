# Ask grounding — supervised rerun scope

Date: 2026-09-06

The first repair run fixed the earlier U2 failures, but complete transcript
review left A1 and A3 unaccepted. This is the single supervised rerun after the
narrow correction described in the first run's report, within the user's
authorization to handle the three failing cases.

Only Ask changes: its conclusion must reflect supplied facts and invite
confirmation without a solution offer; its post-hypothesis question must
explicitly name the explanation as a hypothesis. Brainstorm and all other
runtime files remain unchanged from the first candidate.

Run only A1 and A3, once each, with their unchanged fixture messages and the
same capture harness, model, and isolation settings. No automatic retry. Any
remaining failure is retained and reported; do not broaden this run or claim
that earlier Ask regression cases were rerun against this final source.

The supervisor captures all artifacts in this new directory. Both initial and
resumed test turns use read-only sandbox and approval never. The tested skill
does not create the evidence files. See `source-hashes.json`, `fixtures.json`,
and each turn's command array for the exact tested inputs and configuration.
