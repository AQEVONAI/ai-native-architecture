# 07 — Exercises

## Exercise 1 — Add a third source

A Finance team wants to add an expense-policy document set to the fabric, with its own access restrictions (some expense policies visible only to managers). Extend the federation layer to include this third source without breaking the existing HR/IT access-control guarantees. What changes at the fabric layer versus what's isolated to a new connector?

## Exercise 2 — Staleness incident response

Simulate a scenario where the E-01 polling job for the IT wiki silently fails for two weeks (the source changes but the fabric doesn't detect it). How would you detect this failure using only the artifacts this lab's implementation produces? What would you add to make this failure mode detectable sooner?

## Exercise 3 — Structured-question misclassification

The question-type router (Step 1) misclassifies "what is the average time to resolve an IT ticket" as a structured question, when it actually requires synthesizing information from multiple knowledge-base articles about SLA policies. Design a test suite that would have caught this misclassification before it reached production, and describe how you'd correct the router.

## Exercise 4 — Cross-source ranking fairness

The cross-source ranking step (Step 4) is found, on review, to systematically favor HR content over IT content for genuinely cross-source questions — not because HR content is more relevant, but because of how the two connectors' relevance scores happen to be calibrated differently. Propose a fix, and explain why this is a subtler version of the "context dumping" concern `AP-05` describes, even though this lab's design already includes ranking (unlike a naive dump-everything approach).

## Exercise 5 — DF-04 boundary case

Suppose this capability had launched with only HR content (no IT wiki yet), and the IT wiki was added six months later as the organization's second major knowledge source. Re-derive the `DF-04` decision for that scenario — would starting from `K-01` single-source retrieval and only later building the full `K-02`/`K-03` fabric have been the better sequencing? What would the migration from `K-01` to `K-02` have looked like?
