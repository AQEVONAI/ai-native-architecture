# Reference Architectures

5 reference architectures showing how the 17 patterns in `patterns/` compose into coherent, deployable architectures for common enterprise AI-native scenarios. Where a pattern card describes one architectural concern in isolation, a reference architecture shows how several patterns fit together end-to-end for a specific scenario — including the integration points and trade-offs that only become visible at composition time.

| ID | Name | Scenario | Primary Patterns Composed |
|---|---|---|---|
| [RA-01](RA-01-grounded-enterprise-knowledge-retrieval.md) | Grounded Enterprise Knowledge Retrieval | An AI capability answers questions grounded in governed, federated enterprise knowledge | `K-01`, `K-02`, `K-03`, `E-01`, `I-02` |
| [RA-02](RA-02-governed-ai-memory-personalization.md) | Governed AI Memory & Personalization | A capability persists and reuses user context across sessions under full governance | `I-03`, `C-01`, `C-03`, `K-02` |
| [RA-03](RA-03-bounded-autonomous-agent.md) | Bounded Autonomous Agent | A multi-step agent takes real-world action within an enforced autonomy and policy boundary | `A-01`, `A-02`, `C-02`, `C-03`, `O-01` |
| [RA-04](RA-04-ai-observability-evaluation.md) | AI Observability & Evaluation | Full-stack tracing, evaluation gating, and degradation handling for production AI capabilities | `O-01`, `O-02`, `O-03`, `E-02` |
| [RA-05](RA-05-composite-ai-native-enterprise-architecture.md) | Composite AI-Native Enterprise Architecture | The flagship, full six-domain composition — how a mature AI-native architecture looks end-to-end | All 17 patterns |

## Relationship to patterns and labs

Reference architectures are conceptual — they show composition and integration, not vendor-specific configuration. `labs/` (Phase 8) provides hands-on, narrower walkthroughs building toward pieces of these architectures. `decision-framework/` (Phase 6) helps determine which reference architecture, and which pattern variations within it, fit a specific organization's situation.

## Standard reference architecture structure

```markdown
---
id:
name:
scenario:
patterns_composed: []
last_reviewed:
---
# RA-ID — Name

## Scenario
## When This Architecture Fits
## When It Doesn't Fit
## Architecture Overview (diagram)
## Component Breakdown
## Pattern Composition (table: pattern -> role in this architecture)
## Data / Control Flow
## Integration Points and Seams
## Deployment Considerations
## Security & Governance Considerations
## Known Limitations and Open Trade-offs
## Vendor-Neutral Implementation Notes
## Related Reference Architectures
## Revision History
```
