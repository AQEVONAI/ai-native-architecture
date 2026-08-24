---
status: placeholder — not implemented
last_reviewed: 2026-08-24
---

# Future: Architecture Decision Engine

A forward-looking design note, not a specification for current implementation. This document exists to record the intended direction so it isn't lost, and to explicitly mark it as **not in scope** for this repository's current build.

## The idea

`decision-framework/`'s 10 guides currently require a human to work through a decision tree manually, informed by `patterns/index.yaml` and `assessment/` results. An architecture decision engine would make this queryable: given a description of a capability's requirements (question types, action scope, consequence profile, existing infrastructure), it would traverse the same decision logic currently written in prose and recommend a specific reference architecture, pattern composition, and autonomy-level starting point — essentially, `decision-framework/` made executable.

## Why this isn't built now

Three reasons, in order of importance:

1. **The decision logic itself isn't stable yet.** This repository is at `v0.x` (Research status). Several decision guides reference classifications and pattern relationships that are still subject to revision via the research cycle described in `research/research-methodology.md` — automating decision logic that's still actively being corrected (see `research/differentiation.md`'s A-01 correction) risks encoding a wrong answer with false authority.
2. **The inputs an engine would need aren't yet machine-readable.** `patterns/index.yaml` and `pattern-schema.yaml` are a solid foundation, but `decision-framework/`'s guides are currently prose with embedded decision trees — turning those into a structured, machine-evaluable format (the prerequisite for any engine) is itself a nontrivial project not yet scoped.
3. **Explicit scope discipline.** This repository's build was paced deliberately (see `CONTRIBUTING.md` and the phased commit history) to avoid generating speculative tooling ahead of a stable content foundation. An engine built on an unstable foundation would need to be substantially rebuilt anyway once the foundation stabilizes — better to wait.

## What a future implementation would likely need

- A structured, machine-evaluable version of each `decision-framework/` guide's decision tree (not just prose), likely as its own schema alongside `pattern-schema.yaml`.
- A stable, tagged release of this repository to build against (per `VERSIONING.md`), not `main`.
- A clear position on how engine recommendations relate to human judgment — almost certainly as a starting recommendation requiring human review, not an autonomous architecture-selection tool, consistent with this framework's own `A-01`/`C-01` discipline applied reflexively to itself.
- Integration with `assessment/` results, so recommendations are informed by an organization's actual current maturity profile, not a generic one-size-fits-all recommendation.

## What would trigger picking this up

A stable `v1.0.0` tagged release (per `VERSIONING.md`) with `decision-framework/` guides mature enough that their content has stopped changing materially across research cycles, combined with actual demand from AQEVON's own engagement practice for faster decision-framework navigation than the current prose guides support.

## Status

Not scheduled. This document should be revisited at the next major version milestone, not before.
