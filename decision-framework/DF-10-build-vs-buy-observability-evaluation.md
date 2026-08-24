---
id: DF-10
name: Build vs. Buy for Observability & Evaluation
decision: Whether to build custom O-01 execution-tracing and O-02 evaluation-gate infrastructure, or adopt existing commercial or open-source tooling.
related_patterns: [O-01, O-02, O-03]
last_reviewed: 2026-08-24
---

# DF-10 — Build vs. Buy for Observability & Evaluation

## The Decision

Decide whether to build custom infrastructure for AI execution tracing (`O-01`) and evaluation gating (`O-02`), or adopt existing tooling from the now-mature commercial and open-source category serving this need (see `research/sources.md`).

## Why This Is Hard

Unlike several other decisions in this framework, this one is not primarily a novelty-vs-established-practice question — the tooling category is genuinely mature as of this framework's research. The difficulty is instead in evaluating whether existing tooling actually satisfies this framework's specific requirements (structured trace schema covering identity, policy evaluation, and authorization decisions; evaluation gates wired into actual promotion blocking, not just reporting) or only appears to on the surface, and in weighing vendor lock-in and self-hosting requirements against build cost.

## Decision Inputs

- Does a candidate tool support the specific trace schema this framework requires (`O-01`): acting identity, retrieval provenance, policy evaluation outcomes, authorization decisions — not just latency/error logging?
- Does a candidate evaluation tool actually block promotion on failure, or only report scores after the fact (a meaningfully weaker guarantee than `O-02` requires)?
- Are there self-hosting, data-residency, or vendor-lock-in constraints that rule out commercial SaaS options?
- What is the organization's realistic capacity to build and maintain custom infrastructure to the same maturity level as existing tooling?

## Decision Tool

```
Does the organization have hard self-hosting or data-residency
requirements that rule out commercial SaaS observability/eval
tooling?
│
├── YES → Evaluate open-source, self-hostable options first
│         (e.g., self-hostable tracing platforms). Build custom
│         only for the specific gaps self-hosted tooling doesn't
│         cover (commonly: the O-01 identity/policy/authorization
│         schema fields this framework requires beyond generic
│         tracing).
│
└── NO → Evaluate commercial tooling against the SPECIFIC
          requirements above (not general "does it do LLM
          tracing/eval") before adopting. Where a strong fit
          exists, adopt rather than build — this category is
          mature enough that custom-building the whole stack
          is rarely justified in 2026. Build only the thin
          integration layer mapping this framework's schema
          onto the chosen tool's data model.
```

## Recommendation Guidance

Given the maturity of the LLM/agent observability and evaluation tooling category found during this framework's research pass, default to adopting existing tooling for the bulk of `O-01`/`O-02` infrastructure, and reserve custom-build effort for the specific schema and enforcement gaps — particularly ensuring evaluation gates genuinely block promotion rather than only reporting scores, and ensuring traces capture the identity/policy/authorization fields this framework's other patterns depend on, which general-purpose tracing tools may not include by default.

## Common Mistakes

- Building a fully custom tracing and evaluation stack from scratch in 2026, duplicating a mature tooling category's functionality at significant unnecessary cost.
- Adopting a tool for its tracing/dashboard capability without verifying its evaluation feature genuinely gates promotion — some tools report evaluation scores without actually blocking a failing change, which does not satisfy `O-02`'s requirement.

## Related Patterns

`O-01`, `O-02` (the patterns this decision implements), `O-03` (a related but distinct build-vs-buy question, since graceful degradation logic is less commonly a packaged commercial feature and more often requires custom implementation regardless of the tracing/evaluation choice).

## Revisit Triggers

A chosen tool being found to not actually block promotion as assumed (discovered via an incident where a failing evaluation still shipped); new regulatory or data-residency constraints emerging after initial tool selection.

## Revision History

- 0.1.0 (2026-08-24) — Initial decision guide.
