# 05 — Common Pitfalls

## A near-miss: evaluation that reports but doesn't block

**How it would appear here:** Implementing Step 3's evaluation suite and Step 4's promotion pipeline such that a failing evaluation result is logged and visible on a dashboard, but the change still deploys regardless — satisfying the letter of "we have evaluation" while not satisfying `O-02`'s actual requirement that a failing change be blocked from promotion.

**How this lab avoids it:** Step 4 is explicit that "this must be a genuine block... not merely a report generated after deployment," and `06-validation-checklist.md` includes a specific test deploying an intentionally failing change and confirming it does not reach production.

**Why this is worth naming even though it's not a formally cataloged anti-pattern:** `research/sources.md`'s findings on CI/CD evaluation gates note this exact distinction (gates that block vs. tools that only report) as a real, common gap in practice — this lab treats it as a first-class pitfall precisely because it's easy to build the reporting half and stop there, believing the job is done.

## AP-07 — Single-Model Dependency (the O-03 angle)

**How it would appear here:** Building `O-03`'s degradation handling only for the IT-wiki source (as Step 5 does) and assuming that's sufficient, without recognizing the support assistant's underlying model itself is another dependency with no defined fallback — this lab's scope intentionally covers only the knowledge-source dependency, not model-level routing (that's `I-01`/`DF-07` territory, out of this lab's scope), but a full production deployment should not stop at this lab's boundary.

**How this lab avoids fully falling into it:** By scoping Step 5 explicitly and naming this gap here rather than implying the lab's `O-03` coverage is complete — see `07-exercises.md` Exercise 3.

## E-02 becoming a formality

**How it would appear here:** The monthly review cycle (Step 6) running and always concluding "no change warranted" without genuine scrutiny, becoming a scheduled non-event rather than a real review — the Evolution-domain analog of `AP-08`'s rubber-stamping concern, applied to architectural review rather than action approval.

**How this lab avoids it:** By requiring the decision record to be produced every cycle regardless of outcome (Step 6), creating a paper trail that would make a pattern of consistently empty reviews visible on inspection — visibility is not prevention, but it is the mechanism `E-02`'s own pattern card relies on for catching this failure mode.
