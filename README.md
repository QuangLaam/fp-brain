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

The canonical source is at [skills/fp](skills/fp/SKILL.md), consisting of exactly 5 runtime files with all references contained within the package. See [installation and update guide](docs/install.md).

## Status and verification

Current version: **1.0.0-candidate.5**. This is a candidate for practical use and
feedback, not a validated stable release.

This public snapshot starts a new history. Private development logs, research
notes and historical conversation evidence are not included. Earlier private
session results do not establish the behavior of this snapshot.

Publication preparation checks cover package structure, internal links, explicit
invocation and common credential patterns. No fresh conversation test has been
run for this public snapshot. Verify discovery and behavior on your host using
the [installation guide](docs/install.md).

## Working on this repository with Codex

Open this repository folder in Codex. The root [AGENTS.md](AGENTS.md) provides
project instructions for maintaining the package and verifying changes. This is
a Markdown/YAML project; no build command or dependency setup is required.

Maintaining FP and using `$fp` are separate tasks. The canonical `skills/fp/`
folder is the source package. To make `$fp` available in Codex, follow the
[installation guide](docs/install.md); editing this repository does not update
an installed copy. After changing repository instructions, start a fresh chat
in this folder to verify that Codex loads the updated guidance.

## Origins and license

FP is distributed under the [MIT License](LICENSE). Adapted portions retain
Matt Pocock's copyright notice. See [attribution and source scope](ATTRIBUTION.md)
for the pinned upstream version, adaptation details and conceptual references.
The five-file runtime package also carries these notices in
[the core reference](skills/fp/references/core.md#license-and-attribution), so
manual installation preserves them.
