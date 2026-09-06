# Provenance

This file maps runtime behavior to the selected source register. User requests
define the product; sources support the method; local notes are attributed
heuristics. All eight source hashes matched `rebuild-contract.yaml` on
2026-09-05.

## Runtime mapping

| Runtime behavior | Support | Scope |
|---|---|---|
| Break an issue into basic truths and rebuild from them | CLM-UT-01 | Direct source |
| Repeated why questions are adaptive and causal, not a fixed five | CLM-UT-02 | Direct source |
| Six Socratic lenses guide question selection | CLM-UT-03 | Direct source |
| Public skills are explicitly invoked | CLM-GRILL-00 plus product decision | Upstream pattern and Codex metadata |
| Ask only questions whose prerequisites are settled | CLM-GRILL-01 | Direct source, adapted from whole-frontier rounds to one useful question |
| Agent investigates accessible facts; user owns decisions | CLM-GRILL-02 | Direct source |
| Advisory reasoning does not execute the resulting plan | CLM-GRILL-03 plus product boundary | Direct source and product decision |
| Reframe a possible symptom before committing to a cause | CLM-MOC-01 | Local-note heuristic |
| Stop at a practical layer that supports rebuilding | CLM-MOC-02 | Local-note heuristic |
| Teach-back can expose a remaining knowledge gap | CLM-MOC-03 | Local-note heuristic; not proof of mastery |

## Product design decisions

- One useful question per Ask response reduces pressure and lets new evidence
  shape the next turn. This intentionally differs from the upstream
  whole-frontier interaction.
- Ask can give a short prerequisite explanation so a knowledge gap does not
  force a skill switch.
- Brainstorm performs its own clarification and does not load Ask.
- Decide uses only criteria that can change the current choice.
- Learn means understanding a concept currently blocking the work, following
  the user's direct choice; it is not a retrospective.

## Sources observed

The authoritative build-time register is
`/Users/quanglaam/fp-brain-rebuild-planning/rebuild-contract.yaml`; it is not a
runtime dependency. Observed sources were Untools First Principles, Matt
Pocock's `grill-me` and `grilling` skills, the local First Principles MOC, and
the selected local notes on framing, Five Whys, actionable stopping depth, and
the Feynman technique.
