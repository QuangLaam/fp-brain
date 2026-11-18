
## Main directories
- `skills/fp/`: canonical skill package. Contains `SKILL.md`, `agents/openai.yaml`, and `references/` (`core.md`, `learning-context.md`, `methods.md`).
- `docs/`: `install.md`, the installation and update guide.
- Root `AGENTS.md`: project instructions for maintaining the package.
- `knowledge/`: evidence packs (`first-principles`, `pocock-productivity-skills`) built with the `es-knowledge-forge` skill. Not part of the skill package; FP reads them only when the working directory has them. See "Knowledge packs" in `AGENTS.md`.

## Commands
- No install, build or test commands. The README states that no build command or dependency setup is required.
- Installed copies (e.g. `~/.agents/skills/fp`) are not updated by editing this repo. Follow `docs/install.md` to update them.
- After changing repo instructions, start a fresh Codex chat in this folder to confirm the updated guidance loads.

## Rules from the project docs
- Keep `skills/fp/` at exactly 5 Git-tracked files, with all required references inside the package.
- Do not import upstream skill dependencies or file-writing behavior into FP.
- Before changing FP's method content, read the matching pack document in `knowledge/` and its cited claims. `skills/fp/` may mention `knowledge/` only as an optional read; it must work without it.
- Do not hand-edit pack claims, sources, `_evidence/`, `_actions/` or `index.json`; use the knowledge builder CLI.


## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.
