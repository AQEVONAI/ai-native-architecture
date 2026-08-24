---
id: DF-07
name: Single Model vs. Model Routing
decision: Whether a capability should call one fixed model directly, or route requests across multiple models based on complexity, cost, and latency requirements.
related_patterns: [I-01, O-02, O-03]
last_reviewed: 2026-08-24
---

# DF-07 — Single Model vs. Model Routing

## The Decision

Decide whether an AI capability should integrate directly against a single, fixed model, or invest in a routing layer (`I-01`) that selects among multiple models per request.

## Why This Is Hard

A single-model integration is faster to build and reason about initially, and routing can feel like premature optimization for a capability still proving its basic value. But the coupling a single-model integration creates is exactly what produces `AP-07` (Single-Model Dependency) later — and retrofitting a routing layer onto a codebase built around one hard-coded model is significantly more expensive than building the abstraction from the start, even in a minimal form.

## Decision Inputs

- Request volume and cost sensitivity — at what scale does the cost difference between a uniformly expensive model and a routed mix become material? (Industry evidence suggests routing's cost benefit becomes significant at meaningful production scale — see `research/sources.md`.)
- Task complexity variance — does the capability handle a genuinely uniform task, or a mix of simple and complex requests that could be served by different-capability models?
- Resilience requirement — how costly would a single provider's outage or deprecation be to this capability specifically?
- Engineering maturity — is the team able to maintain routing logic and the evaluation (`O-02`) needed to validate routing decisions safely?

## Decision Tool

```
Is this capability's request mix genuinely uniform in complexity
(no meaningful simple/complex split), AND is it low enough volume
that cost optimization is not material?
│
├── YES → A single, well-chosen model is sufficient for now.
│         Still build behind a MINIMAL routing abstraction
│         (even with only one model configured) so that adding
│         a fallback route later (O-03) doesn't require a
│         rewrite — this is cheap insurance, not full I-01
│         investment.
│
└── NO (complexity varies, or volume/cost is material, or
     resilience matters) → Invest in I-01 Model Routing now.
     Pair with O-02 evaluation to validate routing decisions
     before they affect production traffic broadly.
```

## Recommendation Guidance

Even when full routing logic isn't yet justified, avoid hard-coding model-specific calls throughout application code — a thin abstraction layer costs little upfront and is the difference between "add a fallback route in an afternoon" and "an outage becomes a multi-day incident," per the illustrative scenario in `AP-07`.

## Common Mistakes

- Building directly against a single provider's API throughout the application, with no abstraction layer at all, treating routing as something to "add later" without preparing for it structurally.
- Building elaborate routing logic for a capability with genuinely uniform, low-volume request patterns where the added complexity has no realistic payoff.

## Related Patterns

`I-01` (the pattern this decision leads to), `O-02` (required to validate routing decisions are actually safe), `O-03` (the resilience benefit routing enables), `AP-07` (the anti-pattern this decision directly guards against).

## Revisit Triggers

Request volume or cost crossing a threshold where routing's savings become material; a provider outage or deprecation revealing the current architecture's coupling; task complexity variance increasing as the capability's scope grows.

## Revision History

- 0.1.0 (2026-08-24) — Initial decision guide.
