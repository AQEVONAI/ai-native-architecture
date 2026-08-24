# Prior-Art & Differentiation Matrix

For each pattern, the closest prior art found (per `research-methodology.md` and `sources.md`), the resulting classification, and whether this August 2026 research pass confirmed the pattern's original classification hypothesis or required a correction. Corrections are logged explicitly — see `differentiation.md` for the narrative explanation of each one — rather than silently applied, consistent with the evidence-over-assertion principle in `framework/principles.md`.

| ID | Pattern | Closest Prior Art Found | Original Hypothesis | Research Outcome | Current Classification |
|---|---|---|---|---|---|
| K-01 | Grounded Retrieval | Standard RAG citation/grounding practice, broadly documented industry-wide | E | Confirmed | E |
| K-02 | Enterprise Knowledge Fabric | Hybrid RAG (vector + graph, ~85% enterprise adoption projected by 2026 per Trantor/NStarX); GraphRAG (Neo4j as de facto standard) | S/P | Confirmed, with stronger citation for the retrieval-mechanics half; governance-first framing still not consistently found | S/P |
| K-03 | Knowledge Federation | Data Mesh's "federated computational governance" (Informatica, OvalEdge) | S | Confirmed, strong match | S |
| I-01 | Model Routing | RouteLLM (LMSYS/Berkeley), vLLM Semantic Router, Martian, Not Diamond, OpenRouter — a mature, named product category | E | Confirmed, strong match | E |
| I-02 | Context Budgeting | "Lost in the middle" phenomenon is well-documented research (Atlan, arXiv:2510.10276); deliberate ranked-budget-allocation as a named architectural pattern less consistently found | S/P | Confirmed | S/P |
| I-03 | Governed Memory | "AI Memory" as an emerging named category (Atlan); governance-first framing (ownership, retention, deletion at write time) not consistently found | P | Confirmed | P |
| A-01 | Autonomy Gradient | Directly comparable graduated autonomy scales already exist: Open Data Science / Datasaur's "Levels 1–5" framework, Cloud Security Alliance's "Autonomy Levels for Agentic AI" (Jan 2026), Fluree's "Six Levels of the Autonomous Enterprise" — several explicitly using the same SAE-levels analogy AQEVON's A-01 uses | P | **Correction required** — comparable prior art found; not a first-of-its-kind proposal | S (corrected from P) |
| A-02 | Bounded Agent | Least-privilege applied to AI agents is an active, named practice (Petronella Tech, Oso, WorkOS, Permit.io) | S | Confirmed, strong match | S |
| A-03 | Agent Handoff | OpenAI Swarm's "handoffs" primitive and AutoGen's "Handoffs" design pattern are directly, specifically comparable for the agent-to-agent half; human-escalation handoff is long-established separately | E/S | Confirmed, with stronger and more specific citation than originally available | E/S |
| C-01 | Human Authorization Boundary | Human-in-the-loop approval workflows, established broadly (change-approval boards, transaction approval limits) | E/S | Confirmed | E/S |
| C-02 | Policy-Bounded Action | Open Policy Agent (OPA)/Rego and Cedar as named, established policy-as-code engines, including AI-agent-specific application (Permit.io, Jit, Petronella Tech) | S | Confirmed, strong match | S |
| C-03 | Identity-Carrying Agent | "Agentic identity" is an actively emerging named concept (WorkOS: composite short-lived identity, Zero Standing Permissions; Oso) — closer to an emerging practice than a pure proposal | P | **Watch** — meaningfully closer to existing practice than originally assessed; not yet consistently established enough to reclassify to S outright | P (flagged for re-review next cycle; see `differentiation.md`) |
| O-01 | AI Execution Trace | LangSmith, Langfuse, Arize, Braintrust — a mature, named tooling category for AI-specific execution tracing | S | Confirmed, arguably conservative given tooling maturity found | S |
| O-02 | AI Evaluation Gate | CI/CD evaluation gates are described as standard production practice by 2026 (Arize, Braintrust, Galtea, AppScale's "5 Gates" pipeline) | S | Confirmed, evidence stronger than originally available; approaching established practice | S (trending toward E/S next cycle) |
| O-03 | Graceful AI Degradation | General circuit-breaker pattern, established; AI-specific fallback/uptime routing features exist in commercial routers (Requesty) but a named, general "graceful AI degradation" pattern with explicit degradation signaling not found | S/P | Confirmed | S/P |
| E-01 | Knowledge Evolution Loop | Change-data-capture and incremental indexing, established generally; framed specifically as a knowledge-fabric freshness loop, not found | S/P | Confirmed | S/P |
| E-02 | AI Architecture Evolution Loop | No directly comparable named practice found | P | Confirmed — no correction | P |

## How to read "Research Outcome"

- **Confirmed** — the original classification hypothesis, recorded when the pattern card was first written, held up against this research pass.
- **Correction required** — research found prior art materially closer than the original hypothesis assumed, and the classification was changed as a direct result. See `differentiation.md`.
- **Watch** — research found evidence trending toward a classification change, but not yet strong enough to warrant one; flagged explicitly for re-review at the next research cycle rather than left unexamined.

## Anti-patterns

Anti-patterns are not separately classified E/S/P (they describe failure modes, not claimed architectural contributions), but their prevalence claims were checked against the same source set. No anti-pattern's "Evidence / Prevalence" section required correction in this research pass; `AP-01` and `AP-05` remain the two anti-patterns AQEVON found the least amount of already-published formal analysis for (informally discussed, not yet the subject of dedicated published articles at the time of research) — see each card's Evidence / Prevalence section.

## Revision History

- 0.1.0 (2026-08-24) — Initial matrix, covering all 17 patterns against the August 2026 research pass. One classification correction applied (A-01), one flagged for future review (C-03).
