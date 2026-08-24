# 01 — Scenario and Objectives

## Scenario

With the support assistant (Labs 01–02) and ticket agent (Lab 03) both in production, sharing the observability backbone built in Lab 04, the organization now wants a third capability: a manager-facing assistant that answers questions like "how is my team's ticket load looking this week" and can suggest (not automatically execute) rebalancing assignments across team members. This is exactly the scenario `RA-05`'s deployment guidance anticipates — a second/third capability revealing whether the organization's shared infrastructure actually holds up under reuse, or whether each capability has secretly been building its own siloed version of Knowledge, Control, and Operations concerns.

## Objectives Framed as a Reuse Audit

Rather than treating this as a from-scratch build, this lab is structured as an audit: for each of the six domains, determine what can be reused directly from Labs 01–04's infrastructure, what needs extension, and what is genuinely new to this capability.

## Success Criteria

- The new capability's knowledge questions (ticket load, team composition) are answered by extending the existing `K-02` fabric with a new federated source (the ticket system's own data, not yet a federated source in Labs 01–04), not by building a parallel retrieval stack.
- The new capability's rebalancing suggestions reuse the `A-01`/`A-02` Envelope discipline from Lab 03, with a distinct, separately justified autonomy-level assignment (suggestions require human confirmation, unlike Lab 03's permitted-path automatic execution) — reusing the pattern, not necessarily reusing the same level.
- The new capability's actions and answers write to the same `O-01` trace store from Lab 04, queryable alongside the other two capabilities' data, without a separate observability system.
- Running `assessment/assessment-questionnaire.md` against the resulting three-capability portfolio produces a materially different, richer profile than `assessment/worked-example.md`'s original two-capability assessment — demonstrating the assessment framework's own value increases as the portfolio matures.

## What This Lab Does Not Cover

Full implementation detail for the new capability is intentionally lighter than Labs 01–04 — this lab's focus is the reuse/extension/new-build audit and the resulting portfolio-level assessment, not a fifth complete build-out.
