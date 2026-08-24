---
id: DF-02
name: Choosing an Autonomy Level
decision: Which of the A0–A5 autonomy levels is justified for a specific AI-native capability.
related_patterns: [A-01, A-02, C-01, C-02, O-02]
last_reviewed: 2026-08-24
---

# DF-02 — Choosing an Autonomy Level

## The Decision

For a given AI capability (already determined to be agentic per `DF-01`, if applicable), assign one of the six autonomy levels defined in `A-01` — A0 through A5 — and record the justification.

## Why This Is Hard

Autonomy level is often decided implicitly, by default framework behavior or by whoever configured the system last, rather than as a deliberate risk decision. It is hard because the right inputs — measured confidence, reversibility, regulatory constraint, whether an enforcement mechanism actually exists — span technical, risk, and compliance considerations that are not usually owned by the same person, and because organizational ambition ("we want to be autonomous") can pull toward a higher level than the evidence supports.

## Decision Inputs

- **Business impact if wrong** — what is the actual consequence of an incorrect action at this step?
- **Reversibility** — can an incorrect action be cheaply and quickly undone, or is it effectively permanent once taken?
- **Measured confidence** — what does `O-02` evaluation data actually show for this capability, not what is assumed or hoped?
- **Regulatory constraint** — does an external requirement impose a ceiling on autonomy regardless of technical confidence?
- **Enforcement readiness** — does a `C-02` policy enforcement point or `C-01` authorization boundary actually exist for this capability, or would a higher autonomy assignment be unsupported by any real control?
- **Observability readiness** — is `O-01` execution tracing in place, sufficient to catch and investigate a problem at the proposed level?

## Decision Tool

| Business Impact if Wrong | Reversibility | Measured Confidence | Recommended Ceiling |
|---|---|---|---|
| Low | High (cheap, fast undo) | Any | Up to A4, pending enforcement readiness |
| Low | Low (hard to undo) | High, evaluated | A3 (human approval before irreversible low-impact action) |
| High | High | High, evaluated, enforcement in place | A3–A4 with strong `C-02` policy boundary |
| High | Low | Any | A1–A2 (recommendation/preparation only) until reversibility or confidence materially improves |
| Any | Any | Not yet measured (no `O-02` evaluation data) | A0–A2 — do not assign A3+ on assumed confidence |
| Any | Any | Regulatory ceiling below the above | Regulatory ceiling governs, regardless of technical readiness |

A5 (fully autonomous, no policy-bounded ceiling) should be reserved for narrowly scoped, low-impact, highly reversible actions only, and treated as an exception requiring explicit justification even when the table above would otherwise support A4.

## Recommendation Guidance

Assign the lowest autonomy level that still delivers the capability's required value, then increase deliberately as evidence (measured confidence, track record, enforcement maturity) accumulates — not the other way around. Never assign A3 or above without a corresponding, actually implemented `C-01` or `C-02` mechanism; an autonomy level unsupported by real enforcement is not a documented risk decision, it is `AP-06` (Autonomous Privilege Creep) waiting to happen.

## Common Mistakes

- Assigning an autonomy level based on the model's demonstrated capability in a demo, rather than measured production confidence (`O-02`).
- Treating autonomy level as a one-time decision rather than something `E-02`'s evolution loop should periodically re-justify as evidence changes.
- Assigning A4/A5 to a capability with no enforcement mechanism in place, effectively operating at an undocumented, unenforced autonomy level regardless of what is recorded.

## Related Patterns

`A-01` (the pattern this decision directly implements), `A-02` (how to architect the agent once the level is assigned), `C-01`/`C-02` (the enforcement mechanisms that make A3+ defensible), `O-02` (the evaluation data this decision should be grounded in).

## Revisit Triggers

Any material change to the inputs above: an evaluation result showing lower-than-assumed confidence, a new regulatory constraint, an incident, or a sustained pattern of `A-03` handoffs suggesting the capability is consistently operating at the edge of its assigned level.

## Revision History

- 0.1.0 (2026-08-24) — Initial decision guide.
