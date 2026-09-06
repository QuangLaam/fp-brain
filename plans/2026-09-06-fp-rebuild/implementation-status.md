# FP rebuild implementation status — 2026-09-06

Current gate: **PACKAGE_VALIDATED**.
Native acceptance, real install, migration, discovery, UI and user trial: **NOT_RUN**.
No native budget consumed by the implementer.

## Preservation and contract

- Original HEAD `7c894c2`; scoped baseline `f8b6caa`, then branch `codex/fp-rebuild`.
- Verified 226-file checkpoint: `/var/folders/f4/1x7nmn4x4rg76xlt1wsrt2tr0000gn/T/fp-rebuild-checkpoint-9smdqawq`; manifest SHA256 `9b2c204fc432289f6110b761bbda0637a8fe18f5f1a7cc193ebfacb3ccd7387b`. Baseline preserves the scoped historical ledger/evidence, original notes and plan. Backup also preserves ignored metadata.
- Frozen evaluator assets committed **before runtime writes** as `1f0dd76` in `evals/rebuild-v1/`. Freeze SHA256 `dba2c0e32f70ecc48238cbea2673a6f4ee596c9d001fbb0d286c798356a96284`; fixture `fp-rebuild-fixtures-1`, rubric `fp-rebuild-rubric-1`, contract v1. Twenty cases, five independent repeats and ordinary = 26 sessions per batch, at most two batches/52 total, at most two concurrent, one bounded runtime repair.
- Three mandatory source families have selected versions, limitations and 17 decisions mapped to runtime rules/tests in `evals/rebuild-v1/source-register.md`. Original local claims are preserved; unsupported examples/universality were excluded. New hypothesis/clarification rubric does not regrade old evidence.

## Candidate and changes

Candidate `skills/fp/`, version `1.0.0-candidate.1`: one explicit entry with package-local core/method/learning references. Grounded hypotheses allowed; user goals/priorities/override/stop preserved; research read-only; current demonstrated understanding precedes optional old memory. No automatic delegation, artifact execution or memory writing.

Separate lifecycle maintenance: `scripts/manage-fp.py`, `tests/test_fp_package.py`, `docs/install.md`. Scope is exactly `fp` below an explicit discovery root and five allowlisted package files; manifests/backups are outside discovery. The script refuses unmanaged targets, drift, extras, symlinks and path escapes. It verifies backup/restoration and performs idempotent installs. POSIX stdlib only; same-filesystem rename required.

Migration preview is prepared in `migration-preview.patch` with `migration-before-hashes.json`; `git apply --check` passed. It changes 11 paths (retire eight old entry/metadata files, update README/AGENTS and mark old core historical). **It has not been applied**. Existing four entries, current README/AGENTS/core and all original notes/evidence stay active/unchanged through this gate.

## Validation observed

- `python3 -m unittest discover -s tests -p test_fp_package.py -v`: **23 tests PASS**. Tested independent copy in a path with spaces; read-only dry-run; new/idempotent/upgrade install; uninstall and repeated rollback to exact prior bytes/absence; unmanaged conflicts; user edits/extras/empty directories; deleted target; source/target/ancestor/backup symlinks; reference/path/manifest escapes; modified backups; manifest publish failures restoring previous target or original absence; CLI JSON and conflict exit status; late edits before displacement on upgrade/uninstall restored, and edits after the displaced-tree check preserved in durable recovery. Temporary fixtures only, no real global operation.
- OpenAI `skill-creator/scripts/quick_validate.py skills/fp`: **Skill is valid**.
- `python3 -B scripts/manage-fp.py validate`: final candidate validates; `candidate-manifest.json` records all five file hashes and package hash `3201cfb458bb7b51d81c5913965f8f1a729121f7fba0dc3d25026402397e6aa2`.
- Test development corrections: canonicalized test temp paths because macOS `/var` is a symlink; fixed multiline metadata matcher; passed pre-operation expected state into replacement so own staging directory does not look like unmanaged state. Independent review then found a P1 edit-loss window between the final check and target rename. Fixed by checking the displaced tree and retaining it permanently outside discovery after commit; three race scenarios are covered by two additional test methods. These were package implementation iterations, not native behavioral runs.

## Remaining and limits

Independent code reviewer confirmed the P1 fix and 23 tests on a clean snapshot; newly generated candidate `.DS_Store` then removed and all 23 tests passed again against the actual source. The package inventory intentionally continues to reject every extra file, including Finder metadata. Independent reviewer owns subsequent behavior review; native evaluator owns actual model/config/provenance and run budget. Package tests cannot prove model decisions or actual discovery. Do not change candidate bytes/version after native acceptance and then reuse its results.

A host tool restriction currently prevents automated Codex Desktop observation, per parent-agent preflight; D2 remains blocked/unobserved unless an authorized observation becomes available. This is an evidence-access limit, not an observed native/install defect. User trial feedback cannot be generated by the agent. The lifecycle tool detects ordinary drift and rolls back ordinary publication failures; abrupt process/power failure requires inspecting retained state/recovery directories, and hostile concurrent filesystem mutation is outside its transactional guarantee.
