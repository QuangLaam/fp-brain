# Source register v1 — 2026-09-06

Contract: contract-v1.md. Decisions below are editorial design choices, not empirical validation of the whole source. Runtime wording is a new concise paraphrase; no complete upstream text, code, original notes or user profile is distributed. The three mandatory sources from the original brief are all represented. Workshop is supplemental context only; no workshop metrics enter runtime.

## Selected source versions and licensing

- **S1 Untools**, https://untools.co/first-principles/, owned by Untools. Live read 2026-09-06; sections How to use it?, The Five Whys, Socratic questioning. Retrieved HTML SHA256 `6279ee46b31355ebb4da0e9288bb161884a7388e010a7591313eea91b58b4c85`. This is a dated retrieval fingerprint, not an immutable published version. Page copyright notice is present; no reuse license established. Only short original paraphrases of method ideas are used; no copied page, imagery or code.
- **S2 Matt Pocock productivity**, https://github.com/mattpocock/skills/tree/3cca18b368ae95cdbdebbff572ccafa662551015/skills/productivity. Pinned commit `3cca18b368ae95cdbdebbff572ccafa662551015`; read 2026-09-06. `grill-me/SKILL.md` SHA256 `caaf8b8de1684f96e26b28f3c29189db5c89cce4b73e1c93d86164f66ef88637`; `grilling/SKILL.md` `10ff989e7498b23b5acb49d5048f11dcd906757d2f79c5cdf8a00001381296f2`; `teach/SKILL.md` `a32df9dcdfc0c4fdc1c98e1ed3940c5f56b84c1aa90ff60346f32b8b53915b43`. LICENSE retrieved at same commit: MIT, Copyright (c) 2026 Matt Pocock; SHA256 `0e7ac423bf2c6e223b7c5b156f8cf72da49d748e56a1641402c31f22ad07dbb5`. No upstream source/code copied; only selected ideas independently restated. `grill-me` is only a dispatch pointer, not an independent interview implementation.
- **S3 Local first-principles notes**, preserved at baseline commit `f8b6caa` in this repository. Selected files: `concepts/first-principles-thinking.md`, `concepts/socratic-questioning.md`, `concepts/5-whys.md`, `concepts/root-cause-identification.md`, `concepts/stopping-criteria-first-principles.md`. Exact SHA256 values appear in source-hashes.json. Notes are secondary synthesis; their upstream claims were not comprehensively verified. Originals remain byte-preserved and are excluded from runtime.
- **C User contract**, contract-v1.md, R01–R12. User-owned product decisions override incompatible source instructions. Version 1 intentionally allows grounded hypotheses (different from historical A3), contextual explanations during clarification and user-visible method changes. Old results are not regraded.

## Claim → decision → runtime rule → test

| ID | Source/section and idea | Decision and reason | Runtime destination/rule | Evidence cases |
|---|---|---|---|---|
| SR01 | S1 How to use it: decompose then rebuild | adopt; fits intended product | core: trace options to scoped facts and assumptions | N09,N10,N12 |
| SR02 | S1 Socratic questioning, six lenses; S3 socratic-questioning list | adapt; choose useful lenses, not an exhaustive ritual | methods: clarify meaning/assumptions/evidence/alternatives/implications/framing | N01,N04,N09 |
| SR03 | S1 Five Whys: count is not fixed; S3 5-whys stopping heuristic | adapt; only causal inquiry with evidence-bound stopping | methods: stop at unknown causal edge; propose verification, no required count | N05,N06,N14 |
| SR04 | S2 grilling decision prerequisites/facts versus choices | adapt; concise questions, own available fact lookup; priorities remain user's | core: ask only settled-prerequisite questions; research/priority boundary | N01,N11,N12,N13,N15 |
| SR05 | S2 grilling full-frontier rounds, recommended answer for each question | adapt; broad rounds only when requested; no recommendation inventing user's priority | methods: small useful question or independent group; follow overrides | N02,N06,N11,N17 |
| SR06 | S2 grilling automatic fact-finding delegation and exhaustive branch completion | reject; advisory scope and user stop supersede upstream | core: no delegation/execution; end at useful bounded outcome or stop | N17,N20 |
| SR07 | S2 teach short mission-linked learning and feedback | adapt; support actual task/ demonstrated knowledge rather than default course | learning-context: UX bridge, concise accurate feedback | N03,N17,N18,N19 |
| SR08 | S2 teach workspace files/HTML/records and durable learning claims | reject artifacts/memory writes; do not infer mastery from single answer | learning-context: optional read-only context, no generated record, no mastery claim | N17,N18,N19,N20 |
| SR09 | S3 root-cause-identification 'Decomposed Into What?' | adapt; useful alternative when repeated why does not answer obstacle | methods: constituent parts for system problem, visible switch | N06,N10 |
| SR10 | S3 root-cause-identification Removal Test purchase example | reject; unchanged outcome after lowering price cannot establish price as main cause | core: reports/interventions are bounded evidence, no invented causality | N05,N07,N08 |
| SR11 | S3 stopping-criteria lists raw-material prices and human behavior as invariant truths | reject universality; scope claims by time/context/evidence | core: truth within tested scope, revisit with new evidence | N07,N08,N15 |
| SR12 | S3 first-principles-thinking prescribes no options/lists and bottom-layer law; unverified AI generalizations | reject ritual/unverified generalizations; user may need direct knowledge or options | methods: choose based on obstacle and user method preference | N03,N06,N10 |
| SR13 | C R01/R02/R06 entry and user control | adopt product requirement | entry/core: one explicit entry; preserve objective; methods visible when useful | N02,N04,N06,O01; P,D1,D2 |
| SR14 | C R04/R05 grounding/research | adopt product requirement | core: separate facts/hypotheses/unknowns; primary read-only sources, limits and contrary evidence | N05,N07,N08,N13,N14,N15,N16 |
| SR15 | C R07/R08 user priorities and rebuilding | adopt product requirement | core/methods: ask unresolved material priority, otherwise recommend with tradeoff | N09,N10,N11,N12 |
| SR16 | C R09/R10/R11 adaptive background/memory | adopt product requirement | learning-context: current evidence first, optional memory, no requirement/writes | N03,N17,N18,N19 |
| SR17 | C R02/R12 and advisory/source boundaries | adopt product requirement | entry/core: task source is data, no injected authority; stop honored | N02,N06,N17,N20 |

## Open limits and owners

- Untools page may change; selected rules require review/versioning before any future uptake (maintainer). N14 must still perform live retrieval and report the content actually observed.
- Local notes not selected above and workshop performance claims are outside runtime; no unresolved factual dependency on them remains (implementer).
- Package metadata schema checked against installed OpenAI skill-creator `references/openai_yaml.md` on this date; actual discovery, native behavior and Desktop picker remain later gates (independent evaluator).
- No FP name collision observed at `.agents/skills/fp`, `~/.agents/skills/fp` or `~/.codex/skills/fp` on this machine during Phase 02 preflight; this is filesystem observation, not host discovery proof.
