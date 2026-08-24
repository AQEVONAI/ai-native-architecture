---
id: DF-08
name: When to Introduce Governed Memory
decision: Whether a capability needs cross-session, persisted memory (I-03) at all, versus remaining stateless per session.
related_patterns: [I-03, C-01, C-03, K-02]
last_reviewed: 2026-08-24
---

# DF-08 — When to Introduce Governed Memory

## The Decision

Decide whether a capability should persist user- or entity-specific context across sessions under `I-03`'s governance discipline, or remain stateless, treating every session independently.

## Why This Is Hard

Memory is an easy feature to add incrementally ("let's just remember this one thing") and each individual addition can feel low-risk, but `I-03` requires real governance investment (classification, ownership, retention, deletion) from the very first memory write — there is no safe way to "add memory casually now, govern it properly later" without accumulating exactly the ungoverned-memory risk `I-03` and `AP-05` describe. The decision is hard because the cost of governance is paid upfront, while the cost of skipping it is deferred and often invisible until a compliance or trust incident surfaces it.

## Decision Inputs

- Does the capability's value proposition genuinely depend on remembering something across sessions, or would restating context each session be an acceptable (even if slightly less convenient) alternative?
- Does the organization operate under a regulatory regime with data-subject rights (access, correction, deletion) that unmanaged memory would put at risk?
- Is reliable per-user identity (`C-03`) available to scope memory correctly?
- Is there organizational capacity to own the ongoing retention/deletion enforcement `I-03` requires, not just the initial implementation?

## Decision Tool

```
Would the capability's core value proposition be meaningfully
degraded by NOT remembering anything across sessions?
│
├── NO → Remain stateless. Simpler, no governance burden, no
│        deletion/retention obligation. Revisit if user feedback
│        or usage data later shows this assumption was wrong.
│
└── YES → Is reliable per-user/entity identity (C-03) available
          to scope memory correctly?
          │
          ├── NO → Do not introduce memory yet — unscoped memory
          │        risks cross-identity leakage. Establish C-03
          │        first.
          │
          └── YES → Is there organizational capacity to own
              ongoing retention/deletion enforcement, not just
              initial build?
              │
              ├── NO → Defer. A memory feature built without
              │        this capacity will accumulate exactly the
              │        governance debt I-03 and AP-05 describe.
              │
              └── YES → Introduce I-03 Governed Memory, scoped
                  to C-03 identity, governed consistently with
                  K-02.
```

## Recommendation Guidance

Treat "should this remember things" as a genuine architectural decision with a real governance cost, not a default feature to add because the underlying model technically supports it. When memory is justified, build the classification/ownership/retention discipline in from the first write — retrofitting governance onto an already-accumulated, ungoverned memory store is materially harder than building it in from the start.

## Common Mistakes

- Adding memory incrementally, one "let's just remember this" feature at a time, without ever formally deciding to take on `I-03`'s governance obligations — this is how ungoverned memory accumulates even in organizations that would never have approved it as a deliberate decision.
- Delaying a genuinely valuable memory feature indefinitely out of governance caution, when the actual blocker is a solvable capacity gap rather than a fundamental unsuitability.

## Related Patterns

`I-03` (the pattern this decision leads to), `C-03` (a hard prerequisite), `K-02` (the governance model memory should be held to consistently), `AP-05` (the failure mode of skipping this decision's governance requirement).

## Revisit Triggers

A regulatory change introducing new data-subject rights; user-facing evidence that statelessness is a real value gap; organizational capacity for retention/deletion enforcement newly becoming available.

## Revision History

- 0.1.0 (2026-08-24) — Initial decision guide.
