# 08 — Solutions and Discussion

## Exercise 1 — Add a third source

Adding Finance requires: a new connector returning content plus access metadata (role-based, per the existing pattern), and no change to the fabric-layer authorization logic itself if it was built generically (evaluating arbitrary role-based access metadata rather than hard-coded HR/IT-specific rules). If the original implementation hard-coded authorization logic per source rather than generically, this exercise surfaces that design debt — a well-built `K-02` fabric's authorization layer should be source-agnostic, taking access metadata as input rather than encoding per-source rules.

## Exercise 2 — Staleness incident response

With only the artifacts this lab's base implementation produces, this failure would likely go undetected until a user reports an answer citing outdated content — a reactive, late detection. This is the gap `E-01`'s Observability Considerations section flags: "a silently broken change-detection mechanism... produces exactly the staleness this pattern is meant to prevent, while appearing operationally healthy." The fix is adding an explicit health signal per source — last successful poll time, exposed as a monitorable metric — which this lab's base implementation does not include and Lab 04 (Observability) would formally add.

## Exercise 3 — Structured-question misclassification

A test suite here should include a representative sample of borderline questions specifically designed to probe the structured/unstructured boundary, evaluated against expected routing outcomes — this is a direct application of `O-02` (AI Evaluation Gate)'s principle, applied narrowly to the router component rather than the full capability. The correction itself (moving "average resolution time" to the knowledge-retrieval path) is straightforward once caught; the harder lesson is that the router's classification set needs its own evaluation discipline, not just the end-to-end answer quality evaluation.

## Exercise 4 — Cross-source ranking fairness

This is a legitimate, subtle failure: relevance scores from two different connectors/retrieval mechanisms are not automatically comparable on the same scale, even if both are technically "ranked." A fix requires either calibrating both sources' relevance scores to a comparable scale before joint ranking, or using a unified ranking model that scores candidates from both sources consistently rather than trusting each connector's own internal scoring. This is indeed a subtler version of `AP-05`'s concern — the lab's design avoids naive dumping, but a miscalibrated ranking step can reproduce a milder version of the same underlying problem (the wrong content effectively winning the budget allocation) without looking like the anti-pattern on the surface.

## Exercise 5 — DF-04 boundary case

If HR-only was the initial six-month state, `DF-04`'s standard incremental guidance would likely have applied: start with `K-01` single-source retrieval for HR, and build toward `K-02`/`K-03` federation once IT's addition created genuine cross-source need — this lab's actual scenario (both sources present at launch) is the less common but real case `04-decision-points.md` calls out as an exception to the more typical incremental path. The migration itself would involve introducing the fabric layer as a new abstraction in front of the existing `K-01` retrieval (which becomes one of the fabric's federated sources), then adding the IT connector alongside it — a real but manageable refactor, not a full rebuild, provided the original `K-01` implementation kept retrieval and generation reasonably separable.
