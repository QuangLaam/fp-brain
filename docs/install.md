# Installing and Updating FP

The canonical source is the `skills/fp/` directory in this repository, containing exactly five runtime files:
- `SKILL.md`
- `agents/openai.yaml`
- `references/core.md`
- `references/learning-context.md`
- `references/methods.md`

Run the copy commands from the root of your downloaded or cloned repository.
License and attribution notices are included in `references/core.md`; preserve
that file when installing or redistributing the package.

## 1. Target Locations by Host

- **Codex / Universal agents**: `~/.agents/skills/fp/`
- **Antigravity IDE**: `~/.gemini/config/skills/fp/`

## 2. Installation and Update Steps

Select your target directory `TARGET`:
```sh
TARGET="$HOME/.agents/skills/fp"   # or "$HOME/.gemini/config/skills/fp"
```

1. **Inspect and backup (if existing target present)**:
   If `TARGET` already exists, back it up outside the directory before updating:
   ```sh
   [ -d "$TARGET" ] && backup_dir="$(mktemp -d /tmp/fp-skill-backup.XXXXXXXX)" && cp -r "$TARGET" "$backup_dir/fp" && printf 'Backup: %s\n' "$backup_dir/fp"
   ```

2. **Copy the five canonical files**:
   Create target subdirectories and copy each tracked file explicitly (avoiding `cp -R` to prevent OS metadata files such as `.DS_Store`):
   ```sh
   mkdir -p "$TARGET/agents" "$TARGET/references"
   cp skills/fp/SKILL.md "$TARGET/SKILL.md"
   cp skills/fp/agents/openai.yaml "$TARGET/agents/openai.yaml"
   cp skills/fp/references/core.md "$TARGET/references/core.md"
   cp skills/fp/references/learning-context.md "$TARGET/references/learning-context.md"
   cp skills/fp/references/methods.md "$TARGET/references/methods.md"
   ```

3. **Verify Content by Comparison**:
   Ensure all five files match the source repository:
   ```sh
   for f in SKILL.md agents/openai.yaml references/core.md references/learning-context.md references/methods.md; do
     diff -q "skills/fp/$f" "$TARGET/$f" || echo "Mismatch: $f"
   done
   ```

## 3. Post-Installation Verification

1. **Discovery check**: Open a fresh session on the host and invoke `$fp`. If the host fails to load the skill, check the installation directory and startup logs.
2. **Behavioral check**: Ask an exploratory question (e.g., *"I want to improve my workflow but don't know where to start"*). Observe whether FP asks a concrete clarifying question about your specific situation, and verify that it remains strictly advisory without modifying files or executing unauthorized actions.
