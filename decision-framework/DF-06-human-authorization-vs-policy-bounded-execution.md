---
id: DF-06
name: Human Authorization vs. Policy-Bounded Execution
decision: Whether an autonomous action should require per-instance human approval (C-01) or may execute automatically within an enforced policy boundary (C-02).
related_patterns: [A-01, C-01, C-02, O-02]
last_reviewed: 2026-08-24
---

# DF-06 — Human Authorization vs. Policy-Bounded Execution

## The Decision

For an action a capability at autonomy level A3 or above may take, decide whether it should route through a human authorization boundary (`C-01`) before every execution, or may proceed automatically as long as it satisfies an enforced policy (`C-02`).

## Why This Is Hard

Both mechanisms are legitimate controls, and the choice is frequently made by default (whichever was easier to implement first) rather than by matching the mechanism to the action's actual risk and review characteristics. Choosing human authorization for high-volume, low-variance actions leads directly to `AP-08` (Human-in-the-Loop Theater); choosing policy-bounded execution for actions with genuinely high, hard-to-encode-in-policy consequence removes a check that may have been the only thing catching a real error.

## Decision Inputs

- Action volume — how many instances of this action occur per unit time, and does that volume exceed realistic human review capacity?
- Encodability — can the conditions under which this action is safe be expressed as a machine-evaluable policy, or does correctness genuinely depend on contextual human judgment that resists encoding?
- Consequence and reversibility — what happens if this specific action is wrong, and how easily can it be undone?
- Measured confidence — does `O-02` evaluation data support the capability's reliability at this action type specifically?

## Decision Tool

```
Is the volume of this action high enough that per-instance human
review would exceed realistic reviewer capacity (risking AP-08)?
│
├── YES → Can the conditions for "safe to execute" be expressed
│         as machine-evaluable policy?
│         │
│         ├── YES → C-02 Policy-Bounded Action. Invest in policy
│         │         definition quality, since it is now the sole
│         │         real-time check.
│         │
│         └── NO → This is a signal the action needs to be
│             decomposed — find the sub-decision that IS
│             encodable, and reserve C-01 only for the
│             genuinely judgment-dependent remainder.
│
└── NO (volume is low enough for genuine review) → Does the
     action have high, hard-to-reverse consequence if wrong?
     │
     ├── YES → C-01 Human Authorization Boundary, with real
     │         decision-relevant context provisioned (not a raw
     │         log) — see C-01's design guidance directly.
     │
     └── NO → Either mechanism is defensible; C-02 reduces
         friction where volume may grow, C-01 preserves a
         review habit for a still-maturing capability.
```

## Recommendation Guidance

Prefer `C-01` early in a capability's life, while measured confidence is still being established, and transition toward `C-02` as evaluation evidence (`O-02`) accumulates and the action's safe conditions become well enough understood to encode as policy — this progression should itself be a deliberate, evidence-based decision recorded via `A-01`'s autonomy-level reassessment, not an unplanned drift.

## Common Mistakes

- Defaulting to `C-01` for high-volume actions "to be safe," without recognizing that volume alone will force the review into rubber-stamping (`AP-08`) regardless of intent.
- Defaulting to `C-02` before the safe-execution conditions are actually well understood, encoding an incomplete or wrong policy that then runs unchecked.

## Related Patterns

`A-01` (the autonomy-level decision this choice implements), `C-01`, `C-02` (the two mechanisms being chosen between), `O-02` (the evidence base this decision should draw on).

## Revisit Triggers

Action volume crossing a threshold where the current mechanism's assumptions (reviewable volume, or well-understood policy conditions) no longer hold; an incident revealing the current mechanism failed to catch an error it was assumed to catch.

## Revision History

- 0.1.0 (2026-08-24) — Initial decision guide.
