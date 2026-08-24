# 08 — Solutions and Discussion

## Exercise 1 — A third memory category

An inferred "communication style" category should carry a more conservative retention policy than explicitly stated preferences, because it is derived rather than directly confirmed by the employee — it is more likely to be wrong, and the employee has less direct awareness it's being stored (they didn't state it, it was inferred). A reasonable design: shorter retention (e.g., 90 days, re-derived rather than accumulated indefinitely) and a lower confidence threshold for actually acting on it (e.g., only used to lightly adjust response tone, never surfaced as a citable fact the way a `reported_issue` might be). Treating it identically to explicit "preference" would understate its lower reliability and the reduced employee awareness of its existence — both direct governance concerns under `I-03`.

## Exercise 2 — Deletion during an active recommendation

The correct behavior is to cancel the pending recommendation as part of fulfilling the deletion request, not leave it pending on now-deleted underlying memory. Continuing to display a recommendation whose evidentiary basis has just been deleted is both a UX inconsistency and arguably a governance failure — the deletion request should be honored completely, not partially. This exercise illustrates why deletion handling (Step 6) can't be designed in isolation from every other component that might reference memory at the moment of deletion.

## Exercise 3 — Cross-employee memory leakage, root-cause practice

In likely order: (1) an identity-binding failure at Step 1 — the session was somehow associated with the wrong identity before memory retrieval occurred; (2) a retrieval-scoping bug at Step 4 — the identity binding was correct, but the retrieval query itself failed to filter by owner correctly (e.g., a missing WHERE clause, or a caching layer serving a stale, wrong-identity result); (3) an extraction-time misattribution — Employee A's memory was written with Employee B's identity as owner due to a bug at Step 3, so the "leak" is actually a write-time error surfacing at read time. Distinguishing these requires the execution trace this lab's base implementation doesn't fully include — this is a concrete illustration of why Lab 04's observability instrumentation is not merely a nice-to-have; without it, this exercise's root-cause investigation would be significantly harder in a real incident than it is in this hypothetical.

## Exercise 4 — Revisit DF-06 with evidence

**For moving to C-02:** 98% correctness with zero traced incidents is strong evidence; `DF-06`'s tree explicitly supports transitioning toward policy-bounded execution as evaluation evidence accumulates, and continuing to require manual confirmation for a well-evidenced, low-risk recommendation may itself risk becoming `AP-08` (Human-in-the-Loop Theater) if employees start reflexively confirming without genuine review.

**Against moving to C-02:** 98% is not 100%, and the 2% failure mode specifically involves stale memory informing a real-world action (an actual expedited replacement) — unlike many `C-02`-appropriate actions, this one's failure mode is not cheaply reversible (equipment has already shipped). `DF-06`'s reversibility input weighs against automatic execution even at high measured confidence.

**More persuasive:** the reversibility argument is the stronger one here — `DF-06`'s decision tool explicitly separates "high volume, encodable" (favoring `C-02`) from "high, hard-to-reverse consequence" (favoring `C-01`) as two different gates, and this action fails the second gate regardless of how well it passes the first. A more defensible middle path would be tightening the `C-01` boundary's friction (e.g., single-click confirmation instead of a multi-step form) rather than removing it — improving the UX cost of the check without removing the check itself.
