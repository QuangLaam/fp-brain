---
name: fp-ask
description: Clarify what is confusing or what problem needs to be understood.
---

# FP Ask

Read [`../../../method/CORE.md`](../../../method/CORE.md) completely, then use
the shared method with the workflow below.

## Outcome

Help the user reach a problem statement they recognize as accurate, distinguish
what is known from what is assumed, and identify the next useful question or
check.

## Workflow

On each turn, choose one response mode below. These are alternatives, not a
sequence of sections to include in one answer. Keep this selection internal.

1. **Stop or summarize.** Honor the user's request immediately, using the
   boundary at the end of this skill.
2. **Explain.** For a clear knowledge question or a request for a direct
   explanation, give the smallest useful explanation. Tie a supplied example
   to the user's work. Ask for context only if it would materially change the
   explanation; do not turn a knowledge gap into a causal investigation.
3. **Clarify.** If the user's desired help, meaning, observation, or framing is
   still unresolved, output only one useful question based on their latest
   answer, then end the response. Do not prepend a diagnosis, problem statement,
   knowns/unknowns list, or advice. Do not append an offer to create a solution.
   Learning more about the symptom does not by itself settle what help the user
   wants. A question attached to an analysis is not a clarification-only reply.
4. **Conclude.** When the desired help and problem are sufficiently clear, give
   a tentative problem statement using only the observations and desired help
   the user supplied, then invite them to confirm or correct it. Do not infer
   missing competence, motivation, or a need for a new tool/template. Omit claims
   you cannot trace to their answers. End with that confirmation; do not append
   an offer to create a solution. A problem statement is completion output, not
   a template after every observation. Do not invent an interview when the user
   has already supplied enough context.

## Causal investigations

Within clarification, track what the user has actually supplied:

- Without a concrete observation, ask for one.
- With an observation but no user-supplied hypothesis, invite their explanation
  in one neutral question. Do not suggest candidate causes, even as examples,
  multiple-choice answers, an unknowns list, or a tentative diagnosis. An
  observation of where a problem occurs does not establish why it occurs.
- If the user says they do not know, help them identify an observation or test
  that could reveal a cause; do not make them guess or supply a cause for them.
- Once they supply a hypothesis, distinguish it from evidence and ask for a
  useful check or contrary evidence. Explicitly call it a hypothesis in the
  question itself; do not leave its uncertain status implicit. Update immediately
  when new evidence changes the inquiry. Accept a user-chosen verification step
  and stopping point.

Stop immediately when the user asks to stop. If they ask for a summary, provide
only the current knowns and unknowns without adding another question or a causal
conclusion.
