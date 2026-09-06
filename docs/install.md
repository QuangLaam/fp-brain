# FP package lifecycle

The candidate source is `skills/fp/`. It has one explicit entry and five allowlisted
files, all references internal. The management script is separate maintenance
work; FP never invokes it. Package checks do not establish native behavior,
Desktop discovery, picker behavior or user usefulness.

Requires Python 3.9+ on a POSIX host (uses `fcntl` locking; tested on macOS). No
third-party Python dependencies are needed for package/lifecycle tests. The
supplemental OpenAI skill validator uses its own installed dependencies.

## Review and staging

Run from the repository:

```sh
python3 -B scripts/manage-fp.py validate
python3 -B -m unittest discover -s tests -p test_fp_package.py -v
```

Lifecycle operations require an explicit existing `--skills-dir`; the only target
is its `fp` child. Choose a dedicated `--state-dir` outside every skill-discovery
root, separate from the source and on the same filesystem as the target. Do not
use a repository root or an existing general-purpose data directory for state.
For staging use a temporary directory with separate `discovery` and `state`
children. Use canonical paths without symlinks, including ancestors (on macOS,
`/private/var/...` rather than the `/var/...` alias).

```sh
python3 -B scripts/manage-fp.py dry-run --skills-dir '/absolute/staging/discovery' --state-dir '/absolute/staging/state'
python3 -B scripts/manage-fp.py install --skills-dir '/absolute/staging/discovery' --state-dir '/absolute/staging/state'
python3 -B scripts/manage-fp.py uninstall --skills-dir '/absolute/staging/discovery' --state-dir '/absolute/staging/state'
python3 -B scripts/manage-fp.py rollback --skills-dir '/absolute/staging/discovery' --state-dir '/absolute/staging/state'
```

Dry-run writes nothing, including no lock or state directory. Install is
idempotent for the exact current candidate. A new installation starts from an
absent target; an existing unmanaged target is a conflict even if its bytes look
identical. An upgrade backs up the previous managed version. Uninstall verifies
current bytes and removes only the managed package. Rollback undoes the latest
successful install/uninstall; repeated rollback walks the history back to initial
absence. Idempotent install and already-absent uninstall do not add history.

The manifest records schema, exact target, current version, all file hashes,
package hash and operation history. Each history entry records before/after state
and its verified backup identifier when a previous package existed. Backups and
manifest stay outside discovery. All changes to or extras in a managed package,
including empty directories, block replacement/removal. Missing targets, changed
backups, invalid manifests and symlinks also block dependent operations. The
script has no force flag. Preserve conflicting work and resolve it separately.

Every operation that displaces a previous target keeps that exact tree at the
returned `displaced_recovery` path (`.operation-*/old` under the state root), in
addition to the verified pre-operation backup. It is never automatically deleted:
an editor with an already-open file handle could write to it even after the final
check. Inspect retained recovery trees before any separately authorized cleanup.

An exclusive state lock serializes this tool's operations. File publication uses
same-filesystem renames, with immediate restoration on ordinary publish errors.
Unexpected process/power failure between target rename and manifest publication
can leave detectable drift or an `.operation-*` recovery directory. Do not delete
that directory or retry with a fresh manifest; inspect and reconcile using the
saved hashes/backup first. This small tool is not a database transaction or a
protection against hostile concurrent local processes.

## Real install gate and target

Only proceed after the final package snapshot passes independent review and the
frozen native acceptance suite. Use the exact tested version/hash; renaming a
candidate version after tests changes the package and invalidates that evidence.
User authorization already covers this plan's later installation and migration;
the gate is evidence, not repeated permission.

On the target machine the planned real values are:

- Discovery: `/Users/quanglaam/.agents/skills`
- Managed target: `/Users/quanglaam/.agents/skills/fp`
- Exclusive lifecycle state: `/Users/quanglaam/.local/share/fp-brain/managed-fp`

Reinspect conflicts, run dry-run with those explicit roots, then install only the
accepted candidate. Record command output, manifest and installed file hashes.
No global host settings, AK skills or another FP repository are part of this
operation. Do not put another `fp` in this repo's `.agents/skills`.

After install, perform the single separate-repo native preflight before retiring
old entries. Apply the reviewed `plans/2026-09-06-fp-rebuild/migration-preview.patch`
only if its current-file checks still pass; it retires eight entry/metadata files,
updates the active README/repo guidance and labels old core historical. Existing
personal instructions and historical evidence remain preserved. The patch is
prepared for review and is not applied in Phase 02.

Then collect source-repo, separate-repo and projectless selected-path evidence,
Desktop picker observation, and the real user-selected trial. These are separate
claims. Tool access unavailable for Desktop observation is BLOCKED/NOT_RUN, not
proof the installed skill failed. Do not bypass tool restrictions. An observed
post-retirement behavioral failure triggers the scoped plan rollback; protect
any new drift first. Missing UI evidence or missing user feedback leaves product
acceptance incomplete and does not by itself establish an installation defect.

For repo rollback, first check the exact migration diff in reverse, then reverse
only that patch if no new edits conflict. For global rollback, use the same state
root and `rollback` command to undo the installation/upgrade. Never reset the
whole repository or delete an unmanaged global directory. Restored-file checks
are recovery verification, not an extra native acceptance run.
