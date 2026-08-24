# 01 — Scenario and Objectives

## Scenario

Following Lab 01's launch, employee feedback indicates the support assistant would be more useful if it remembered two things across sessions: stated communication preferences (some employees want concise answers, others want full policy citations every time) and recently reported issues (so a follow-up question like "any update on my laptop request" doesn't require the employee to re-explain context already given in a prior session).

## Why This Requires Deliberate Design, Not Just "Turning On Memory"

The underlying model/platform used for Lab 01 may offer a memory feature that can be enabled with minimal configuration. This lab exists because enabling that feature without deliberate governance design would violate `I-03`'s core requirement — every memory item needs an owner, a classification, and a retention policy from the moment it is written, not retrofitted later. Skipping this step is exactly how `AP-05` (Context Dumping, applied to persisted memory) accumulates.

## Success Criteria

- Every stored memory item has a recorded owner (the employee it pertains to), a classification (e.g., "stated preference" vs. "reported issue," each with different sensitivity and retention implications), and a retention policy, at write time.
- Memory retrieval for a given session is scoped strictly to the requesting employee's own identity — no cross-employee memory leakage, verified with an actual test.
- An employee can request deletion of their stored memory, and the request is honored within a defined window.
- If a memory-informed answer would materially change a high-consequence outcome (this lab's example: memory suggesting an employee is eligible for an expedited equipment replacement due to a previously reported issue), the assistant surfaces this as a recommendation requiring the employee's own confirmation, rather than acting on stale memory automatically.

## What This Lab Does Not Cover

Autonomous action beyond surfacing recommendations (Lab 03) and full observability instrumentation (Lab 04) are out of scope here.
