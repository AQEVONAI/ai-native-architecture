---
id: AP-08
name: Human-in-the-Loop Theater
also_known_as: "Rubber-Stamp Approval"
severity: high
last_reviewed: 2026-08-24
---

# AP-08 — Human-in-the-Loop Theater

## Problem Summary

A human approval step exists in name but not in practice — approvals are granted near-universally, quickly, and without the reviewer having genuine ability or time to catch a substantive error, such that the "human in the loop" provides the appearance of a safety control without its actual function.

## Also Known As

Rubber-Stamp Approval; "we have a human review every action."

## Symptoms

- Approval rate for a given authorization boundary is at or near 100%, with no evidence of substantive rejection or revision ever occurring.
- The context presented to the human reviewer at the point of approval is insufficient to actually evaluate the decision (a raw action log rather than a decision-relevant summary).
- Approval turnaround time is far shorter than the time a genuine review of the presented information would plausibly require.

## Root Cause

An authorization boundary (`C-01`) is added to satisfy a governance or safety requirement without designing what the reviewer actually needs to make a genuine judgment, or without accounting for whether the reviewer has realistic time and attention to review each request — the boundary is built to exist, not to function.

## Why It Happens

"Add a human approval step" is often treated as sufficient compliance with a safety or governance requirement, without follow-through on whether the approval step is actually informative and used — especially as request volume grows past what a reviewer can meaningfully evaluate per-item, at which point rubber-stamping becomes the only practically available behavior even for a well-intentioned reviewer.

## Consequences

- False assurance: the organization believes a meaningful safety control exists where, in practice, none does.
- Errors that a genuine review would have caught pass through unchecked, while the process overhead of the approval step is still incurred.
- When investigated after an incident, an approval log showing near-100% rubber-stamped approval undermines confidence in the entire governance framework's other controls, not just this one boundary.

## How to Recognize It

Examine approval-decision data (`O-01`) for a given authorization boundary: what is the approval rate, what is the median time-to-decision, and what context was the reviewer actually shown? An approval rate near 100% combined with review times too short for the presented context to have been read is strong evidence of this anti-pattern.

## A Worked (Illustrative) Example

*Illustrative scenario:* An organization requires human approval before an AI-drafted customer communication is sent, intending this as a genuine quality and safety check. As volume grows to several hundred drafts per day, the assigned reviewer — with no change to the review interface or time allotted — begins approving nearly every draft within seconds of it appearing, since genuinely reading each one is no longer feasible at that volume. A subsequent review finds the approval step has not meaningfully caught an error in over three months, despite several drafts in that period containing errors a careful read would have caught. The authorization boundary existed and was being exercised, but had stopped functioning as an actual safety control well before anyone recognized it — the volume had exceeded genuine review capacity without a corresponding redesign of the boundary's placement or context.

## Corrective Pattern(s)

`C-01` (Human Authorization Boundary — the direct corrective, specifically its requirement that placement account for genuine review capacity and that context be decision-relevant rather than a raw log dump), `A-03` (Agent Handoff — a well-designed handoff package is what makes genuine review possible in the time available), `O-01` (AI Execution Trace — the data source that makes this anti-pattern detectable in the first place, via approval-rate and review-time analysis).

## Related Anti-Patterns

`AP-01` (Agent by Default — capabilities built agentic by default sometimes add a token human-review step to address governance concern without genuine redesign), this anti-pattern is the specific failure mode `C-01`'s design guidance is written to prevent.

## Evidence / Prevalence

The general phenomenon (approval fatigue leading to rubber-stamping) is well documented in human-factors and process-safety research across domains well beyond AI, including manufacturing quality control and financial transaction approval. AQEVON names its specific manifestation for AI-native human-in-the-loop design, where approval volume can scale very quickly relative to an organization's ability to redesign the review process to match.

## Revision History

- 0.1.0 (2026-08-24) — Initial anti-pattern card.
