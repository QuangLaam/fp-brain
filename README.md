# FP

FP is an advisory skill for first-principles thinking to clarify problems, test assumptions, develop grounded directions, and learn through work. You invoke a single entrypoint: **`$fp`**.

```text
$fp
I am facing this problem: ...
Help me clarify before choosing a solution. Ask what is missing if needed.
```

You can request direct explanation, Socratic questioning, or 5 Whys, redirect, and stop at any time. FP provides advisory reasoning and read-only research; it does not edit files, execute plans, delegate tasks, or write memories. It can use relevant context when provided by the host, but does not require memory to operate.

The canonical source is at [skills/fp](skills/fp/SKILL.md), consisting of exactly 5 Git-tracked files with all references contained within the package. See [installation and update guide](docs/install.md).

## Status and Verification Evidence

- **Host parity (journal record)**: The journal records a synchronized canonical 5-file package across the repo, Codex (`~/.agents/skills/fp`), and Antigravity (`~/.gemini/config/skills/fp`) with matching SHA-256 hashes, sharing the sole trigger `$fp`.
- **Codex CLI (journal record, 2026-10-09)**: The journal records testing the historical clarification defect (C1) on `codex-cli 0.159.3` (`gpt-6-astra`) across 3 independent runs. Its independent evaluation reported the defects NOT REPRODUCED on the current runtime.
- **Scope & limits**: These are journaled results from sampled sessions; behavior in other contexts has not been established by those records.

## Origins

1. [Untools — First principles](https://untools.co/first-principles/): Deconstruct problems to foundational truths and reconstruct grounded solutions.
2. Local first-principles notes: 42 foundational research notes recoverable through Git history at commit `c561a5c`; not all have been incorporated into FP.

Historical plans and evaluation reports are preserved in Git history at commits `76b4df2` and `fe07378`.



