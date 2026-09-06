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

1. Check whether the desired outcome, affected user, and relevant constraints
   are clear enough to generate useful directions. If an answer is needed first,
   ask the single highest-value question instead of listing generic ideas. When
   the missing answer or an ambiguous term could materially change the
   directions, make the response clarification-only: ask that question and stop.
   This includes uncertainty about which user event is being discussed or which
   system states are available. Do not require an interview when the supplied
   facts are already sufficient.
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
