# Scoring Guide

How to convert `assessment-questionnaire.md` answers into per-domain maturity ratings (`maturity-model.md`, levels 0–4), and how to interpret the resulting profile honestly.

## Scoring principle

Score conservatively when evidence is weak. An answer of "yes, we do that" with no artifact produced during the assessment should be scored at most one level above what is directly observable, not taken at face value — this mirrors the evidence-over-assertion principle applied to the assessment process itself, not just to the patterns it evaluates.

## Per-domain scoring

For each domain, review the corresponding questionnaire answers against the domain's row in `maturity-model.md`'s indicator table, and assign the highest level for which **all** indicators at that level and below are genuinely met with evidence — not the highest level for which any indicator is met. A domain with a Level 3 indicator met but a Level 1 indicator unmet scores at Level 1: maturity is not additive, and skipping foundational practice while showing an advanced one is itself a diagnostic signal (often indicating the advanced practice is narrower or shallower than it first appears).

| Domain | Primary Questions | Notes |
|---|---|---|
| Knowledge | 1–4 | Q2 (enforcement location) is the single most diagnostic question — a "yes we ground answers" (Q1) paired with application-layer-only access control (Q2 fails) caps the score at Level 1–2 regardless of Q1's answer. |
| Intelligence | 5–7 | Score Intelligence excluding Q7 if the organization has no memory feature in scope (per `DF-08` — absence of memory is not itself a deficiency); note this exclusion explicitly in the recorded result. |
| Autonomy | 8–10 | If the organization has no agentic capabilities, Autonomy should be recorded as "not yet applicable" rather than scored at Level 0 — a Level 0 score implies a gap that doesn't exist if there's nothing agentic to be immature about. |
| Control | 11–13 | Q12 (approval rate / time-to-decision) is the single most diagnostic question for detecting `AP-08` — a near-100% approval rate with fast decisions caps Control at Level 1 regardless of how the other questions score, since it indicates the boundary is not functioning as a genuine check. |
| Operations | 14–16 | Q14 (live reconstruction attempt) is the most rigorous test in the entire questionnaire — if the assessor cannot actually reconstruct a specific output's provenance during the assessment session, Operations cannot score above Level 1, regardless of what documentation claims. |
| Evolution | 17–19 | A review cycle that exists on paper but has "never actually run" or "run once at launch and never since" scores Level 1, not Level 2 — the cycle must be demonstrably recurring. |

## Overall profile interpretation

Do not average the six domain scores into one number — report the full six-domain profile. When a single summary is genuinely needed (e.g., for an executive audience), report the **minimum** domain score among domains that are actually in scope, not the average, and name which domain it is — the minimum is what determines the organization's actual exposure, since a weak Control score is not offset by a strong Knowledge score; the weakest domain is where an incident is most likely to originate.

## Common scoring pitfalls

- **Grading generosity creep** — an assessor familiar with the organization's intentions and roadmap tends to score based on plans rather than current, evidenced state. Score only what exists today.
- **Treating "not applicable" as "Level 0"** — a domain genuinely out of scope (e.g., Autonomy for a portfolio with zero agentic capabilities) should be marked not-applicable, not scored as a deficiency, per the Autonomy row above.
- **Averaging away an imbalance** — the specific value of a per-domain profile over a single score is surfacing imbalance (e.g., Autonomy racing ahead of Control); collapsing to an average erases the exact signal this assessment is designed to produce.

## Revision History

- 0.1.0 (2026-08-24) — Initial scoring guide.
