---
id: DF-09
name: Choosing a Reference Architecture
decision: Which of RA-01 through RA-05 best matches a given capability's scenario, as a starting composition to adapt.
related_patterns: [K-02, A-02, O-01]
last_reviewed: 2026-08-24
---

# DF-09 — Choosing a Reference Architecture

## The Decision

Given a specific capability's requirements, decide which reference architecture in `reference-architectures/` provides the best starting composition of patterns to adapt, rather than composing patterns from scratch for every new capability.

## Why This Is Hard

Real capabilities rarely map cleanly to exactly one reference architecture's scenario description — a capability might primarily be a knowledge-retrieval scenario (`RA-01`) but also need to remember user preferences (`RA-02`'s territory), or a bounded agent (`RA-03`) that also needs full evaluation gating (`RA-04`). The difficulty is choosing a sensible starting composition and correctly identifying which additional reference architecture's patterns need to be layered in, rather than either over-fitting to one RA and missing a real requirement, or trying to build the full `RA-05` composite for a capability that doesn't yet warrant it.

## Decision Inputs

- Does the capability's core value come from answering questions grounded in enterprise knowledge? (→ `RA-01` territory)
- Does the capability need to remember user-specific context across sessions? (→ `RA-02` territory)
- Does the capability take multi-step autonomous action with real-world consequence? (→ `RA-03` territory)
- Is this an initial capability, or does the organization already have production AI capabilities needing shared observability infrastructure? (→ `RA-04`, likely needed regardless of which other RA applies)
- Does the organization have multiple capabilities in production, warranting investment in the full composite? (→ `RA-05`)

## Decision Tool

```
Start here for any new capability:

1. Does it primarily answer questions from enterprise knowledge?
   → Start from RA-01.

2. Does it ALSO need to remember user-specific context across
   sessions?
   → Layer in RA-02's I-03/C-03 components.

3. Does it take autonomous, consequential action (not just
   answer questions)?
   → Layer in RA-03's A-01/A-02/C-02 components. If the
     capability is PRIMARILY an autonomous agent rather than
     primarily a knowledge-retrieval capability, start from
     RA-03 instead and layer in RA-01's knowledge components
     as one of the agent's steps.

4. Regardless of the above: is this capability going to
   production?
   → RA-04's O-01/O-02/O-03 components are required, not
     optional, per this framework's baseline observability
     requirement (see O-01, "When to Use").

5. Is this the organization's second, third, or later AI-native
   capability, sharing infrastructure with prior ones?
   → Consult RA-05 for how this capability's components should
     integrate with already-existing shared infrastructure
     (fabric, observability backbone) rather than duplicating it.
```

## Recommendation Guidance

Treat the reference architectures as composable starting points, not mutually exclusive categories — most real capabilities end up drawing primarily from one RA and layering in specific components from one or two others. `RA-04`'s observability components are the one layer that should be included essentially unconditionally for any production capability. Do not attempt to build toward `RA-05` directly for a first capability — let it emerge as described in `RA-05`'s own deployment considerations.

## Common Mistakes

- Selecting a single reference architecture and treating its pattern list as exhaustive for the capability's actual needs, missing a required layer (most commonly, skipping `RA-04`'s observability components because the capability's primary scenario is `RA-01` or `RA-03`).
- Attempting to implement `RA-05` in full for an organization's first AI-native capability, well before the multi-capability shared-infrastructure need that justifies it exists.

## Related Patterns

This guide references reference architectures rather than individual patterns directly; see each RA's own Pattern Composition table for its specific pattern list.

## Revisit Triggers

A capability's scope expanding to include a scenario (memory, autonomous action) not covered by its original RA selection; the organization's capability portfolio growing to a size that warrants `RA-05` composite planning.

## Revision History

- 0.1.0 (2026-08-24) — Initial decision guide.
