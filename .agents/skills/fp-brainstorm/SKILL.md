---
name: fp-brainstorm
description: Develop distinct solution directions from clarified facts and principles.
---

# FP Brainstorm

Read [`../../../method/CORE.md`](../../../method/CORE.md) completely, then use
the shared method with the workflow below. Do not load or invoke another FP
skill; clarification is part of this workflow.

## Outcome

Give the user a small set of meaningfully different directions, show what each
direction is built from, and surface the assumptions worth testing. End when the
user has a direction worth investigating or asks to stop.

## Workflow

1. Choose between clarification and generation before drafting the response.
   These are mutually exclusive modes for this turn:
   - **Clarify:** if a missing fact or ambiguous term could change the proposed
     mechanisms, output only the single highest-value question and stop. No
     directions, examples of solutions, recommendation, or offer follows it.
   - **Generate:** if the supplied facts support useful directions, continue
     below without a mandatory interview.
   For status or feedback problems, establish which user action/event needs
   confirmation and which states the system can actually observe. A phrase
   describing an outcome does not establish either fact. Do not silently choose
   one meaning of an ambiguous event, invent a lifecycle or integrations around
   it, and ask what it means at the end.
   Assumption labels are for uncertainties within a grounded direction; they
   do not substitute for clarifying the event the whole direction is about or
   a missing capability that would materially change that direction.
2. Extract the observations, available system states, user needs, and practical
   constraints already established. Treat app-specific facts as scoped facts,
   not universal principles.
3. Generate a few directions that differ in mechanism, experience, or trade-off,
   not merely in wording or visual treatment. Follow an exact count when the
   user requests one.
4. For each direction, state:
   - which known fact, need, or principle it uses;
   - how it would work from the user's perspective;
   - its main trade-off;
   - the most important unverified assumption or test, when relevant.
5. Help the user select one direction for further investigation. Keep execution
   outside this advisory skill.
