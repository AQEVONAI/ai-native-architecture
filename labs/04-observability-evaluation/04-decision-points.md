# 04 — Decision Points

## DF-10 — Build vs. Buy for Observability & Evaluation

**Applied at:** the initial decision of how to implement this lab's trace/evaluation infrastructure.

**Decision:** This lab builds a minimal reference implementation rather than adopting a commercial/open-source platform, for pedagogical reasons — it makes the required schema and enforcement logic explicit and inspectable. A real deployment following this lab should apply `DF-10`'s decision tree properly: given the tooling maturity found in `research/sources.md`, most organizations should adopt existing tracing/evaluation tooling and build only the thin schema-mapping layer this lab's Step 1 defines, rather than building the full stack this lab walks through for teaching purposes.

## Choosing a shared schema over per-capability logging

**Applied at:** Step 1 of the implementation guide.

**Decision:** One schema with capability-specific nested fields, rather than two entirely separate logging systems. This is a direct application of `RA-05`'s composite-architecture guidance that Operations-domain infrastructure should be shared across capabilities rather than duplicated — the value of `E-02`'s aggregation step in Step 6 depends on being able to query trace and evaluation data consistently across capabilities.

## DF-06 revisited — using O-02 evidence toward Lab 03's split-level question

**Applied at:** connecting this lab's evaluation data back to Lab 03's Exercise 2 (the A3/A4 classification question).

**Decision:** This lab's evaluation suite (Step 3) is scoped to the support assistant, not the ticket agent, in its initial build — extending it to the ticket agent's policy-permitted action correctness is deliberately left as this lab's `07-exercises.md`, since it directly supplies the evidence Lab 03's Exercise 2 and `04-decision-points.md` flagged as needed before revisiting that agent's autonomy classification.

## What would change this lab's decisions

Once evaluation data volume justifies it, revisit `DF-10` in earnest for a production deployment — this lab's reference implementation is not intended to be operated at production scale indefinitely.
