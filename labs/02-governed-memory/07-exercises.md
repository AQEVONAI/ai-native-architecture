# 07 — Exercises

## Exercise 1 — A third memory category

The organization wants to add a "communication style" memory category distinct from "preference" (e.g., inferred from interaction patterns rather than explicitly stated) with its own, more conservative retention policy. Design the classification and retention rule for this new category, and explain why treating it identically to "preference" would be a governance gap.

## Exercise 2 — Deletion during an active recommendation

An employee submits a deletion request while a high-consequence recommendation (from Step 5) is pending their confirmation. What should happen to the pending recommendation, and why? Consider both the immediate UX and the governance implications.

## Exercise 3 — Cross-employee memory leakage, root-cause practice

During testing, you discover that Employee B's session briefly displayed a recommendation that referenced content that could only have come from Employee A's reported issue. Walk through the likely root causes (in order of likelihood) and how you would confirm which one actually occurred using this lab's implementation's logging.

## Exercise 4 — Revisit DF-06 with evidence

Six months after launch, evaluation data (hypothetically, from a Lab 04-style setup) shows the expedited-replacement recommendation has been correct in 98% of cases when surfaced, with no incidents traced to stale memory. Using `DF-06`'s decision tree, argue both for and against moving this specific action from `C-01` to `C-02`, and state which side you find more persuasive and why.
