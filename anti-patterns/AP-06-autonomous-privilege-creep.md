---
id: AP-06
name: Autonomous Privilege Creep
also_known_as: "Scope Drift"
severity: critical
last_reviewed: 2026-08-24
---

# AP-06 — Autonomous Privilege Creep

## Problem Summary

An agent's effective authority — the tools it can call, the data it can access, the actions it can take — expands over time without a corresponding, deliberate policy decision, typically through incremental additions each of which seemed individually reasonable.

## Also Known As

Scope Drift; "it already had that tool, so we just added one more."

## Symptoms

- An agent's current tool/access list is longer than what its originally documented Envelope (`A-02`) specified, with no record of when or why each addition was approved.
- No one can produce, on request, a current and accurate description of everything a given agent is actually able to do.
- The agent's autonomy level (`A-01`) has not been re-evaluated since additional access was granted, even though the risk profile implied by that access has changed.

## Root Cause

Incremental scope additions are typically made to solve an immediate, narrow problem ("the agent needs to also check this one other system for this one use case") without revisiting the agent's overall Envelope and autonomy-level assignment as a whole — each addition is locally reasonable, but the aggregate effect is an agent materially more powerful than its original risk assessment accounted for.

## Why It Happens

Re-running a full Envelope and autonomy-level review for every scope change is more process overhead than simply adding the needed tool access, and the connection between "one more tool" and "the agent's overall risk profile has shifted" is easy to overlook when each change is considered in isolation.

## Consequences

- The agent's actual authority silently exceeds what was ever explicitly reviewed or approved at the aggregate level.
- Governance artifacts (the documented Envelope, the autonomy-level justification) become inaccurate, undermining their value as a basis for risk decisions.
- Combined with `AP-03` (Prompt-as-Policy), unreviewed scope expansion becomes not just undesirable but actually exploitable, since there may be no enforced boundary catching the drift.

## How to Recognize It

Compare the agent's currently documented Envelope (tools, knowledge access, authority) against its actual current configuration. Any discrepancy — access granted that isn't reflected in the documented scope, or vice versa — is direct evidence of this anti-pattern.

## A Worked (Illustrative) Example

*Illustrative scenario:* An internal agent originally scoped to read-only access on a ticketing system, at autonomy level A2, has three additional tool integrations added over six months to address specific requests — a write-capable ticket-update tool, a customer-record lookup tool, and a notification-send tool — each added without revisiting the original A2 assignment or the documented Envelope. Eighteen months later, the agent is effectively operating with write access and cross-system reach that would, if assessed fresh today, likely warrant A3 (human-approved execution) rather than its still-recorded A2 designation — but no review has occurred to catch this, because each individual addition felt too small to trigger one.

## Corrective Pattern(s)

`A-01` (Autonomy Gradient — re-evaluation on a defined cadence and whenever a material input changes is the direct structural corrective), `A-02` (Bounded Agent — enforced scope makes drift visible and blockable rather than silent), `C-02` (Policy-Bounded Action — enforced policy that must be deliberately updated, rather than access that can silently accumulate), `C-03` (Identity-Carrying Agent — makes per-identity access auditable, surfacing drift more readily).

## Related Anti-Patterns

`AP-01` (Agent by Default — agents built with generous initial scope have more room to drift), `AP-03` (Prompt-as-Policy — the mechanism that often allows drift to become exploitable rather than merely undesirable).

## Evidence / Prevalence

The general pattern (privilege creep through incremental, individually-justified access grants) is a well-established concern in traditional access-management and security practice, predating AI-specific systems. AQEVON's framing names its specific manifestation in agentic AI systems, where the pace and informality of tool-integration changes can outstrip the cadence of formal access review even more readily than in traditional application permissioning.

## Revision History

- 0.1.0 (2026-08-24) — Initial anti-pattern card.
