# Anti-Patterns

8 recurring failure modes observed (or reliably anticipated, where marked) in AI-native architecture efforts. Each anti-pattern names the corrective pattern(s) in `patterns/` that address it directly — anti-patterns and patterns are two views of the same underlying architectural discipline, not a separate taxonomy.

| ID | Name | Corrected By |
|---|---|---|
| [AP-01](AP-01-agent-by-default.md) | Agent by Default | `A-01`, `A-02`, `C-01` |
| [AP-02](AP-02-rag-everything.md) | RAG Everything | `K-01`, `K-02` |
| [AP-03](AP-03-prompt-as-policy.md) | Prompt-as-Policy | `C-02` |
| [AP-04](AP-04-vector-database-as-knowledge-architecture.md) | Vector Database as Knowledge Architecture | `K-02`, `K-03`, `E-01` |
| [AP-05](AP-05-context-dumping.md) | Context Dumping | `I-02`, `K-01`, `I-03` |
| [AP-06](AP-06-autonomous-privilege-creep.md) | Autonomous Privilege Creep | `A-01`, `A-02`, `C-02`, `C-03` |
| [AP-07](AP-07-single-model-dependency.md) | Single-Model Dependency | `I-01`, `O-03`, `O-02` |
| [AP-08](AP-08-human-in-the-loop-theater.md) | Human-in-the-Loop Theater | `C-01`, `A-03`, `O-01` |

## Standard anti-pattern card

```markdown
---
id:
name:
also_known_as:
severity:
last_reviewed:
---
# AP-ID — Name

## Problem Summary
## Also Known As
## Symptoms
## Root Cause
## Why It Happens
## Consequences
## How to Recognize It
## A Worked (Illustrative) Example
## Corrective Pattern(s)
## Related Anti-Patterns
## Evidence / Prevalence
## Revision History
```

`severity` is a qualitative indicator (`low`, `moderate`, `high`, `critical`) reflecting typical downstream consequence, not likelihood — a low-likelihood anti-pattern with catastrophic consequence (e.g., unbounded autonomous privilege) is still rated high or critical.

The "Worked (Illustrative) Example" section is explicitly labeled as illustrative — a representative composite scenario, not a specific named incident — consistent with the evidence-over-assertion principle in `framework/principles.md`.
