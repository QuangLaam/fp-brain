# FP-Brain repository guidance

The current product is one explicit advisory skill, `fp`. Its canonical entry is
`skills/fp/SKILL.md`; all runtime references stay inside `skills/fp/`.

FP provides advice and read-only research. Writing files, executing experiments,
installing, committing, publishing or delegating is a separately authorized task
outside FP. Preserve current user goals, method overrides and stop requests;
memory is optional and must not be written by FP.

Keep maintenance small and reversible. The active guides are `README.md` and
`docs/install.md`. Do not recreate a custom
installer, acceptance framework or automatic repair loop for ordinary use.

This public repository begins with a clean snapshot. Private historical notes,
plans and session logs are excluded. Report file inspection separately from
observed conversation behavior.

## Working in Codex

This repository contains a Markdown/YAML skill package; there is no application
build, dependency installation, or automated test suite to run.

- For product context, read `README.md`. For installation, updates, or host
  discovery issues, read `docs/install.md` before changing an installed copy.
- For skill maintenance, inspect `skills/fp/SKILL.md` and its referenced files.
  Treat their instructions as the product being edited; invoke FP only when the
  user explicitly requests `$fp`.
- Edit the canonical package first. Repository edits do not synchronize installed
  copies. Update a host installation only when the task includes that host.
- Keep host-specific discovery and installation details in `docs/install.md`;
  keep the runtime package self-contained.

## Verification

Before handing off a change:

1. Run `git diff --check` and inspect `git diff --stat` and `git diff` for scope.
2. For package changes, check that relative references resolve inside `skills/fp/`
   and that `agents/openai.yaml` preserves explicit invocation
   (`allow_implicit_invocation: false`).
3. For installation changes, compare all five canonical files with the selected
   target using the procedure in `docs/install.md`.
4. For behavior changes, report static checks separately from any actual fresh
   session test. If no conversation test ran, state that behavior is unverified.
