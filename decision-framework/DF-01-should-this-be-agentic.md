---
id: DF-01
name: Should This Be Agentic?
decision: Whether a capability requires multi-step, tool-using, autonomous agent architecture, or is better served by a simpler single-step AI interaction.
related_patterns: [A-01, A-02, K-01]
last_reviewed: 2026-08-24
---

# DF-01 — Should This Be Agentic?

## The Decision

Before designing any capability's implementation, decide whether it genuinely requires agentic architecture — multiple reasoning steps, tool orchestration, intermediate decisions — or whether a single-step grounded retrieval-and-answer (`K-01`) or a deterministic workflow would serve the actual task better.

## Why This Is Hard

Agentic architecture is currently the most discussed, most demoed pattern in AI tooling, which creates a pull toward reaching for it regardless of actual task requirements (see `AP-01`, Agent by Default). The decision is hard specifically because building "an agent" can feel like the more sophisticated, more future-proof choice even when it isn't the right choice for the task at hand — there is no natural friction pushing back toward the simpler option.

## Decision Inputs

- Does the task require more than one distinct reasoning or retrieval step to complete, where the output of one step genuinely determines the input to the next?
- Does the task require calling more than one tool or system, with the choice of which tool to call depending on intermediate results?
- Is there a single, well-defined correct answer reachable via one grounded lookup or deterministic computation?
- What is the cost difference between an agentic and non-agentic implementation, in latency, model calls, and engineering/review complexity?

## Decision Tool

```
Does the task require multiple dependent steps or tool calls,
where the next step genuinely depends on this step's outcome?
│
├── NO → Single-step grounded retrieval (K-01) or deterministic
│         workflow. Do not build this agentic.
│
└── YES → Is the set of steps and tools actually fixed and
          predictable in advance (a known sequence)?
          │
          ├── YES → A deterministic multi-step workflow (not an
          │         autonomous agent) likely suffices — the agent's
          │         reasoning isn't doing anything a fixed pipeline
          │         couldn't, and a fixed pipeline is easier to
          │         secure, trace, and reason about.
          │
          └── NO (the path genuinely varies based on intermediate
              reasoning) → This is a legitimate case for agentic
              architecture. Proceed to DF-02 to assign an autonomy
              level, and design against A-02 (Bounded Agent).
```

## Recommendation Guidance

Default to the simplest architecture that satisfies the task's actual requirements. Agentic architecture should be a conclusion reached after this analysis, not a starting assumption. When in doubt between a fixed multi-step workflow and a true agent, prefer the fixed workflow — it is easier to secure, trace, and audit, and can be revisited toward agentic architecture later if the task's actual variability turns out to exceed what a fixed sequence can handle (see `E-02`'s evolution loop for how that revisiting should happen, on evidence rather than assumption).

## Common Mistakes

- Building an agent for a task with a genuinely fixed, predictable step sequence, paying the cost of enforcement and autonomy-level design for flexibility the task never uses.
- Building a single-step retrieval capability for a task that, on honest inspection, does require dependent multi-step reasoning — under-building is the less common but real mirror-image mistake, usually caused by trying to avoid agentic complexity reflexively rather than by genuine task analysis.

## Related Patterns

`A-01` (the next decision once agentic architecture is justified), `A-02` (how to bound the agent once built), `K-01` (the recommended non-agentic alternative for single-step grounded questions).

## Revisit Triggers

Revisit this decision if the task's actual observed variability in production consistently exceeds what the current (agentic or non-agentic) implementation handles — this is a signal the original analysis under- or over-estimated the task's real step-dependency structure.

## Revision History

- 0.1.0 (2026-08-24) — Initial decision guide.
