# 06 — Validation Checklist

Confirm the lab's result actually satisfies `RA-01` before considering it complete.

## Grounding (K-01)

- [ ] For 10 sampled knowledge-question answers, every claim in each answer traces to a specific, identifiable source document — not asserted from model memory.
- [ ] Citations resolve to the actual content that was retrieved and authorized for that query, not a generic or mismatched reference.

## Fabric governance (K-02)

- [ ] An employee without IT-staff role, when asking an IT-administrative-procedure question, receives a response that does not surface restricted content (test with an actual restricted query, not just a policy review).
- [ ] Access-control filtering is confirmed to happen before ranking/budgeting, not after generation — trace a single request through the pipeline and confirm the order.

## Federation (K-03)

- [ ] HR and IT content are confirmed to be queried live from their owning systems, not copied into a third store (check the actual connector implementation, not just the design doc).
- [ ] A cross-source question (leave + equipment request) produces an answer citing both an HR and an IT source correctly.

## Freshness (E-01)

- [ ] A test change to a source document (e.g., a modified PTO policy) is reflected in the capability's answers within the tuned polling window for that source.
- [ ] Per-source polling cadence is confirmed to differ appropriately between HR and IT (not a single global interval).

## Context budgeting (I-02)

- [ ] For a cross-source question, confirm the assembled context contains the highest-relevance content across both sources jointly, not a fixed per-source split regardless of relevance.

## Structured-question routing (DF-03)

- [ ] The help desk phone number question is confirmed to return the exact, current value via direct lookup, with zero variance across repeated identical queries.

## Sign-off

Do not mark this lab complete until every checked item above has been verified against the actual running implementation, not the design intent — consistent with this framework's evidence-over-assertion principle applied to the lab itself.
