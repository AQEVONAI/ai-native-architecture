# 06 — Validation Checklist

## Reuse verification (the core purpose of this lab)

- [ ] Confirm the new ticket-system connector was registered with the existing `K-02`/`K-03` fabric with zero changes required to the fabric's core authorization logic (if changes were required, record what and why — see `05-common-pitfalls.md`).
- [ ] Confirm the new capability's trace records appear in the same trace store/query interface as the support assistant and ticket agent, using the shared schema extended in Step 4.
- [ ] Confirm the `E-02` review cycle's next scheduled run includes the new capability in its aggregation without manual intervention (or record what manual intervention was actually required).

## Independent Envelope/autonomy verification

- [ ] Confirm the new capability's Envelope explicitly excludes any execute/write tool — attempt to have it perform an action beyond suggestion and confirm no such capability exists (not merely that it's discouraged).
- [ ] Confirm the new capability's autonomy-level justification is recorded as its own artifact, independently justified, not a copy of Lab 03's.

## Access scoping

- [ ] A manager can only see their own team's ticket workload data — test with a manager identity attempting to query another team's data.

## Portfolio-level assessment

- [ ] Run `assessment/assessment-questionnaire.md` against the resulting three-capability portfolio. Confirm the resulting profile is recorded and compared explicitly against `assessment/worked-example.md`'s original profile — proceed to `07-exercises.md` Exercise 1 for this comparison in depth.

## Sign-off

The reuse-verification items are the most important in this checklist — they are the actual test of whether `RA-05`'s shared-infrastructure claim held up in practice for this lab's scenario, not just in the design intent stated in `02-architecture-walkthrough.md`.
