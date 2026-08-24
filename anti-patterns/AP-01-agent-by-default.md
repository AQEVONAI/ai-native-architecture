---
id: AP-01
name: Agent by Default
also_known_as: "Agentic-First Design"
severity: high
last_reviewed: 2026-08-24
---

# AP-01 — Agent by Default

## Problem Summary

Defaulting to an agentic architecture — multi-step, tool-using, autonomous — without first justifying it against simpler alternatives (a single well-grounded retrieval-and-answer capability, a deterministic workflow, a traditional application feature).

## Also Known As

Agentic-First Design; "just make it an agent."

## Symptoms

- A capability is built as a multi-step agent when the underlying task is, on inspection, a single well-defined transformation or lookup.
- Tool access and autonomy level are set generously "in case the agent needs it," rather than scoped to an analyzed task requirement.
- No documented `A-01` autonomy-level assessment exists — the capability was simply built agentic because that was the default pattern reached for.

## Root Cause

Agentic architecture is often the most discussed, most demoed, and most immediately available pattern in current AI tooling and literature, which creates a gravitational pull toward reaching for it first — independent of whether the task actually requires multi-step autonomous reasoning and tool use.

## Why It Happens

Agent frameworks are frequently the path of least resistance in current tooling, and building "an agent" can feel more sophisticated or more aligned with where the field is heading than building a narrower, simpler capability — even when the narrower capability would better serve the actual task with less risk and lower operating cost.

## Consequences

- Increased blast radius relative to the task's actual risk profile, since agentic capabilities inherently have a broader action surface than single-step capabilities.
- Higher operating cost (more model calls, more tool calls, more latency) for tasks that did not require it.
- Governance and security review burden scoped to "an autonomous agent" when the actual task warranted a much narrower review.

## How to Recognize It

Ask, for any agentic capability: what specific multi-step reasoning or tool-orchestration requirement makes this task unsuitable for a single grounded retrieval-and-answer (`K-01`) or a deterministic workflow? If the honest answer is "none in particular, it just seemed like the modern way to build it," this anti-pattern is present.

## A Worked (Illustrative) Example

*Illustrative scenario:* A team builds an autonomous agent to answer "what is our current PTO policy," complete with tool access to search multiple internal systems and synthesize a response. The task is, in fact, a single grounded lookup against one well-governed knowledge source — no multi-step reasoning or tool orchestration is required. The agentic implementation adds latency, cost, and an unnecessarily broad tool-access surface (including write-capable tools never actually needed for this task) relative to a `K-01` grounded-retrieval capability that would have answered the same question more cheaply, faster, and with a narrower, easier-to-govern action surface.

## Corrective Pattern(s)

`A-01` (Autonomy Gradient — requires an explicit, justified autonomy-level assignment for every capability, forcing the "why does this need to be agentic" question), `A-02` (Bounded Agent — for capabilities that are genuinely agentic, scopes them explicitly rather than broadly), `C-01` (Human Authorization Boundary — a lighter-weight alternative control for capabilities that don't warrant full autonomous execution).

## Related Anti-Patterns

`AP-06` (Autonomous Privilege Creep — a common downstream consequence once a capability is built agentic by default with generous, unscoped access).

## Evidence / Prevalence

Widely discussed informally across AI engineering practice as "should this even be an agent" — not yet the subject of formal published research at the time of writing, but a consistent theme in practitioner-facing architecture guidance. AQEVON's framing treats this as a named, recurring anti-pattern to make the underlying justification requirement explicit and enforceable via `A-01`.

## Revision History

- 0.1.0 (2026-08-24) — Initial anti-pattern card.
