---
id: AP-07
name: Single-Model Dependency
also_known_as: "Hard-Coded Model Choice"
severity: high
last_reviewed: 2026-08-24
---

# AP-07 — Single-Model Dependency

## Problem Summary

Architecting a system around one specific model provider and version, hard-coded throughout the application, with no routing, fallback, or degradation path if that model becomes unavailable, is deprecated, or is measurably outperformed by an alternative.

## Also Known As

Hard-Coded Model Choice; "we built it on Model X."

## Symptoms

- Model identifiers and provider-specific API calls are scattered directly through application code rather than behind a routing abstraction.
- No defined fallback behavior exists if the primary model provider has an outage or deprecates the specific model version in use.
- Model-version upgrades require broad application code changes rather than a routing configuration change.

## Root Cause

Building directly against a single model provider's API is the fastest path to a working initial capability, and the cost of that architectural shortcut is invisible until the model changes, degrades, or becomes unavailable — at which point the coupling throughout the codebase makes response difficult and slow exactly when speed matters most.

## Why It Happens

Early-stage development reasonably prioritizes getting something working; introducing a routing abstraction (`I-01`) and fallback design (`O-03`) before there is a proven need can feel like premature engineering — but the coupling this creates is expensive to unwind later, and provider-level outages or deprecations are a "when," not an "if," at sufficient time horizon.

## Consequences

- A provider outage or deprecation becomes an application-wide incident rather than an absorbed, routed-around event.
- No mechanism exists to benefit from a better-performing or lower-cost alternative model without a significant re-engineering effort.
- Evaluation (`O-02`) of the current model against alternatives has no operational path to act on its findings even if a clearly better option is identified.

## How to Recognize It

Ask: if the primary model provider had a multi-hour outage right now, what would happen to this capability? If the honest answer is "it would simply be down, with no fallback," this anti-pattern is present.

## A Worked (Illustrative) Example

*Illustrative scenario:* A customer-facing AI capability is built directly against a single model provider's API, with model-specific prompt formatting and API calls embedded throughout the application code. When that provider experiences a multi-hour outage, the capability goes fully offline with no fallback, and restoring service requires waiting out the outage rather than routing to an alternate model — because no routing abstraction (`I-01`) or defined degradation behavior (`O-03`) existed to fall back to. A team that had built the same capability behind a routing layer, even with only a single model configured initially, would have been able to add and switch to a fallback route in minutes rather than being fully dependent on the outage's resolution.

## Corrective Pattern(s)

`I-01` (Model Routing — the direct corrective pattern, decoupling model selection from application logic), `O-03` (Graceful AI Degradation — defines what happens during the routing gap or full unavailability), `O-02` (AI Evaluation Gate — provides the evidence base for safely adding or switching to an alternate route).

## Related Anti-Patterns

None directly overlapping; this anti-pattern is primarily an operational-resilience concern distinct from the governance/security-focused anti-patterns elsewhere in this set.

## Evidence / Prevalence

Analogous to well-established software-architecture concerns around vendor lock-in and single points of failure generally. AQEVON names its specific manifestation for AI-native systems given the currently fast-moving pace of model releases, deprecations, and provider-level incidents relative to more mature infrastructure categories.

## Revision History

- 0.1.0 (2026-08-24) — Initial anti-pattern card.
