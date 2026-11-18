# FP

FP is an advisory skill for first-principles thinking to clarify problems, test assumptions, develop grounded directions, and learn through work. You invoke a single entrypoint: **`$fp`**.

```text
$fp
I am facing this problem: ...
Help me clarify before choosing a solution. Ask what is missing if needed.
```

You can request direct explanation, Socratic questioning, or 5 Whys, redirect, and stop at any time. FP provides advisory reasoning and read-only research; it does not edit files, execute plans, delegate tasks, or write memories. It can use relevant context when provided by the host, but does not require memory to operate.
When missing information could change the conclusion, FP asks a short interview in rounds; you can skip it and request a direct answer.
For problem definition, FP maps material unknowns and asks the next independent
questions whose prerequisites are settled. It stops at a usable framing with
remaining uncertainty explicit; request deeper grilling when you want to explore
further branches. This remains part of the single `$fp` entry.

Within `$fp`, you can also ask to re-explain a confusing message, draft questions
for someone who holds missing information, or prepare a handoff for another
session. These adaptations of `wait-what`, `to-questionnaire`, and `handoff`
produce conversation output only; they do not save/send documents or start
another agent. They require no extra skills, glossary, or particular tech stack.

The canonical source is at [skills/fp](skills/fp/SKILL.md), consisting of exactly 5 Git-tracked files with all required references contained within the package. When the folder you invoke `$fp` in has knowledge packs under `knowledge/` (as this repository does), FP can read the relevant one as optional read-only evidence; it works the same without them. See [installation and update guide](docs/install.md).

## Status and Verification Evidence

- **Host parity (journal record)**: The journal records a synchronized canonical 5-file package across the repo, Codex (`~/.agents/skills/fp`), and Antigravity (`~/.gemini/config/skills/fp`) with matching SHA-256 hashes, sharing the sole trigger `$fp`.
- **Codex CLI (journal record, 2026-10-09)**: The journal records testing the historical clarification defect (C1) on `codex-cli 0.159.3` (`gpt-6-astra`) across 3 independent runs. Its independent evaluation reported the defects NOT REPRODUCED on the current runtime.
- **Scope & limits**: These are journaled results from sampled sessions; behavior in other contexts has not been established by those records.

## Working on this repository with Codex

Open this repository folder in Codex. The root [AGENTS.md](AGENTS.md) provides
project instructions for maintaining the package and verifying changes. This is
a Markdown/YAML project; no build command or dependency setup is required.

Maintaining FP and using `$fp` are separate tasks. The canonical `skills/fp/`
folder is the source package. To make `$fp` available in Codex, follow the
[installation guide](docs/install.md); editing this repository does not update
an installed copy. After changing repository instructions, start a fresh chat
in this folder to verify that Codex loads the updated guidance.

## Origins

1. [Untools — First principles](https://untools.co/first-principles/): Deconstruct problems to foundational truths and reconstruct grounded solutions.
2. Local first-principles notes: 42 foundational research notes recoverable through Git history at commit `c561a5c`; not all have been incorporated into FP.
3. [Matt Pocock Productivity](https://github.com/mattpocock/skills/tree/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity): `grilling`, `wait-what`, `to-questionnaire`, and `handoff`, reviewed on 2026-10-22 and adapted for FP's advisory/read-only scope. Grilling supplies the decision-tree/frontier mechanism, bounded to useful problem definition; upstream delegation, file-writing and skill dependencies are not imported. Future upstream changes need review rather than automatic synchronization.

Historical plans and evaluation reports are preserved in Git history at commits `76b4df2` and `fe07378`.



