# 04 — Decision Points

## DF-09 — Choosing a Reference Architecture

**Applied at:** the initial scoping of this new capability.

**Decision:** This capability draws primarily from `RA-01` (Knowledge — answering workload questions) with a layered-in `RA-03`-style component (Autonomy/Control — the suggestion capability), exactly matching `DF-09`'s guidance that most real capabilities draw from one primary RA and layer in components from others, rather than mapping cleanly to a single reference architecture.

## DF-02 — Choosing an Autonomy Level

**Applied at:** Step 3 of the implementation guide.

**Decision:** A2, for the reasons stated in Step 3 — no evaluation history yet, and the capability's design deliberately excludes any execution authority at all (it can only suggest), making A2's "preparation only" framing a precise fit rather than an approximation. This is a good illustration of `DF-02`'s core guidance ("assign the lowest autonomy level that still delivers the capability's required value") applied to a brand-new capability with zero track record.

## DF-04 / DF-05 — Fabric and Federation, Revisited

**Applied at:** Step 1-2, adding the ticket-system source.

**Decision:** Federate (not centralize) the ticket-system data, consistent with `DF-05`'s standard reasoning — it's an actively maintained system of record. Unlike Lab 01's original `DF-04` analysis (which found the fabric was justified immediately because the first capability's own needs already spanned multiple sources), this decision point is now trivial: the fabric already exists, so `DF-04`'s question ("should we build the fabric") doesn't need to be re-asked — only `DF-03`'s question (should this specific new source be centralized or federated) is live, and it resolves the same way HR/IT did.

## The genuinely interesting decision: NOT reusing Lab 03's Envelope

**Applied at:** Step 3.

**Decision:** Even though this new capability is conceptually related to Lab 03's ticket agent (both concern ticket assignment), this lab deliberately does not reuse Lab 03's Envelope or autonomy-level assignment — each capability gets its own, per `A-01`'s requirement that autonomy be assigned per-capability based on that capability's own actual risk and action scope, not inherited from a topically related but architecturally distinct capability. This is worth calling out explicitly because "these are similar, let's just reuse the config" is a plausible-sounding shortcut that would actually violate `A-01`'s core discipline.
