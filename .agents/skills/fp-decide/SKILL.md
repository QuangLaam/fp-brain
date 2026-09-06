---
name: fp-decide
description: Compare options and make a conditional recommendation from user priorities and evidence.
---

# FP Decide

Read [`../../../method/CORE.md`](../../../method/CORE.md) completely, then use
the shared method with the workflow below.

## Outcome

Give the user a clear comparison and an evidence-bounded recommendation while
leaving the final choice with them. Do not implement the chosen option.

## Workflow

1. Name the decision and options. Preserve the scope of any supplied facts;
   fixture data and claims are not automatically real-world facts.
2. Identify the criteria that can materially change the choice, such as time,
   maintainability, flexibility, risk, cost, or learning value. Use only the
   relevant criteria, not a fixed scorecard.
3. Separate missing facts from missing priorities:
   - investigate accessible facts through permitted read-only tools when the
     subject and source are concrete;
   - ask one focused question when a user-owned goal, constraint, or priority is
     unresolved and could change the recommendation. In that situation, make the
     response question-only and stop. Do not add a default, ranking, conditional
     preference, or invented consequence before the user answers. When the
     priorities are already clear, recommend directly without an interview.
4. Compare each option against the known criteria. Do not invent properties,
   benchmarks, or user priorities.
5. Recommend the option best aligned with the stated priorities, explain the
   decisive reason and main trade-off, and state the condition that would change
   the recommendation when useful.

If evidence is too weak for a responsible recommendation, recommend the smallest
useful verification instead of converting the uncertainty into a preference.
