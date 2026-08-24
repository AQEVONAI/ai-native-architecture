# Patterns

17 architecture patterns across six domains, organized by the meta-model in [`framework/meta-model.md`](../framework/meta-model.md). Every pattern uses the same standard card structure and is registered in [`index.yaml`](index.yaml), validated against [`pattern-schema.yaml`](pattern-schema.yaml).

## Domains

| Domain | Directory | Patterns |
|---|---|---|
| Knowledge | [`knowledge/`](knowledge/) | K-01 Grounded Retrieval, K-02 Enterprise Knowledge Fabric, K-03 Knowledge Federation |
| Intelligence | [`intelligence/`](intelligence/) | I-01 Model Routing, I-02 Context Budgeting, I-03 Governed Memory |
| Autonomy | [`autonomy/`](autonomy/) | A-01 Autonomy Gradient, A-02 Bounded Agent, A-03 Agent Handoff |
| Control | [`control/`](control/) | C-01 Human Authorization Boundary, C-02 Policy-Bounded Action, C-03 Identity-Carrying Agent |
| Operations | [`operations/`](operations/) | O-01 AI Execution Trace, O-02 AI Evaluation Gate, O-03 Graceful AI Degradation |
| Evolution | [`evolution/`](evolution/) | E-01 Knowledge Evolution Loop, E-02 AI Architecture Evolution Loop |

## Standard pattern card

Every pattern Markdown file begins with YAML front-matter and follows this exact section order:

```markdown
---
id:
name:
domain:
classification:
status:
version:
last_reviewed:
---
# Pattern ID — Pattern Name

## Intent
## Context
## Problem
## Forces
## Solution
## Architecture
## Sequence / Behavior
## When to Use
## When NOT to Use
## Benefits
## Trade-offs
## Security Considerations
## Governance Considerations
## Reliability Considerations
## Observability Considerations
## Related Patterns
## Dependencies
## Anti-Patterns
## Known Uses / Evidence
## Vendor Mappings
## Research Questions
## Revision History
```

## Front-matter fields

| Field | Values |
|---|---|
| `id` | Stable pattern ID, e.g. `K-02`. Never reused or renumbered once published. |
| `name` | Pattern name, matched exactly in `index.yaml`. |
| `domain` | One of: `knowledge`, `intelligence`, `autonomy`, `control`, `operations`, `evolution`. |
| `classification` | `E` (Established), `S` (Synthesized), `P` (Proposed), or a combined form (`S/P`, `E/S`). See [`framework/terminology.md`](../framework/terminology.md). |
| `status` | `proposed`, `research`, `validated`, `published`, `mature`, or `deprecated`. See [`GOVERNANCE.md`](../GOVERNANCE.md). |
| `version` | Independent semantic version for this pattern. See [`VERSIONING.md`](../VERSIONING.md). |
| `last_reviewed` | ISO date of last substantive review. |

## Why this structure

The structure is deliberately exhaustive rather than a "shallow definition" format, per the repository's quality bar (`framework/principles.md` §6): every pattern must be usable by a working architect to make a real design decision, not just recognize a term. `Security`, `Governance`, `Reliability`, and `Observability Considerations` are separated rather than folded into a general "considerations" section because AI-native patterns fail differently across each of these dimensions, and conflating them has historically led to security-relevant trade-offs being buried in generic prose.
