# Decision Framework

10 guides for the recurring architectural decisions this framework's patterns require but do not, by themselves, answer. A pattern card describes how to build something well once you've decided to build it; a decision guide helps decide whether, when, and which variant to build in the first place.

| ID | Guide | Core Question |
|---|---|---|
| [DF-01](DF-01-should-this-be-agentic.md) | Should This Be Agentic? | Does this task actually require multi-step, tool-using autonomy? |
| [DF-02](DF-02-choosing-an-autonomy-level.md) | Choosing an Autonomy Level | Which of A0–A5 is justified for this specific capability? |
| [DF-03](DF-03-rag-vs-structured-query-vs-knowledge-fabric.md) | RAG vs. Structured Query vs. Knowledge Fabric | Which retrieval mechanism fits this question type? |
| [DF-04](DF-04-when-to-build-a-knowledge-fabric.md) | When to Build an Enterprise Knowledge Fabric | Is the full K-02 fabric warranted, or is simpler retrieval sufficient? |
| [DF-05](DF-05-centralize-or-federate-knowledge-sources.md) | Centralize or Federate Knowledge Sources | Should sources be consolidated or queried in place? |
| [DF-06](DF-06-human-authorization-vs-policy-bounded-execution.md) | Human Authorization vs. Policy-Bounded Execution | Per-action approval, or an enforced autonomous boundary? |
| [DF-07](DF-07-single-model-vs-model-routing.md) | Single Model vs. Model Routing | Is a routing layer worth the added complexity yet? |
| [DF-08](DF-08-when-to-introduce-governed-memory.md) | When to Introduce Governed Memory | Does this capability need cross-session persistence at all? |
| [DF-09](DF-09-choosing-a-reference-architecture.md) | Choosing a Reference Architecture | Which of RA-01–RA-05 matches this scenario? |
| [DF-10](DF-10-build-vs-buy-observability-evaluation.md) | Build vs. Buy for Observability & Evaluation | Build O-01/O-02 infrastructure, or adopt existing tooling? |

## How these guides are structured

Each guide states the decision, why it is genuinely hard (not just a checklist), the concrete inputs that should inform it, a decision tool (tree, matrix, or worked heuristic), common mistakes seen in each direction, and explicit triggers for revisiting a decision already made — consistent with this framework's general position that architectural decisions are not permanent, but should not be revisited on a whim either.

## Relationship to patterns, reference architectures, and assessment

Decision guides point to specific patterns (`patterns/`) and reference architectures (`reference-architectures/`) as their recommended outcomes, and to `assessment/` for how an organization's overall maturity should inform how aggressively to pursue any given recommendation.
