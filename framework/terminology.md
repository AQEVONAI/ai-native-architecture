---
title: AQEVON Terminology
version: 0.1
status: research
last_reviewed: 2026-08-24
---

# AQEVON Terminology

This glossary defines terms as they are used **within this repository**. Several terms (RAG, agent, control plane) already have broad industry meanings; where AQEVON's usage narrows or extends a common term, that is stated explicitly. Consistent use of this vocabulary across every pattern, reference architecture, decision guide, and assessment document is a repository-wide requirement — see `GOVERNANCE.md`.

## Core terms

**AI-Native Architecture**
An architectural approach in which AI capability (knowledge, reasoning, autonomous action) is a first-class, governed part of the system design — not a bolt-on integration. A system is AI-native to the degree its knowledge, intelligence, and autonomy are architected with explicit control, operations, and evolution disciplines, rather than assembled ad hoc around a model API call.

**AI-Native Capability**
A discrete unit of system behavior that knows (draws on governed knowledge), reasons (uses a model or reasoning process), and may act (executes with some degree of autonomy). The unit of analysis for AQEVON's meta-model and the AI Capability Envelope pattern.

**Enterprise Knowledge Fabric**
A governed logical knowledge layer spanning documents, structured data, applications, APIs, engineering systems, entities, relationships, provenance, and permissions — distinct from, and a superset of, a vector database. See pattern `K-02` and reference architecture `RA-01`.

**Autonomy Gradient**
A six-level scale (A0–A5) describing the degree of independent action an AI capability is architected to have, from full human decision-making (A0) to fully autonomous execution (A5). See pattern `A-01`.

**AI Capability Envelope**
The explicit boundary around what an AI capability is allowed to know, decide, access, and change, expressed through six facets: Purpose, Knowledge, Reasoning, Tools, Authority, Action. See `framework/aqevon-ai-native-architecture.md` §Flagship Concepts.

**AI Control Plane**
The architectural layer responsible for identity, policy, risk classification, and authority enforcement across AI capabilities — the mechanism that makes the Control domain real at runtime, not just on paper. See reference architecture `RA-02`.

**AI Architecture Evolution Loop**
The recurring cycle (Observe → Evaluate → Discover → Redesign → Validate → Deploy → Observe) by which AI-native architecture is deliberately changed in response to operational and evaluation signal, rather than drifting silently. See pattern `E-02`.

**Bounded Agent**
An agentic capability whose tools, knowledge access, autonomy level, and authority are explicitly scoped and enforced, as opposed to an open-ended agent with broad, implicit access. See pattern `A-02` and anti-pattern `AP-01`.

**Grounded Retrieval**
Retrieval-augmented generation in which every generated claim is traceable to a specific retrieved source, with citation, rather than retrieval used only to bias generation without traceability. See pattern `K-01`.

**Governed Memory**
Persistent context (conversation history, user preferences, prior decisions) that is stored, scoped, and retrieved under the same access-control and provenance discipline as any other enterprise knowledge asset, rather than an unmanaged accumulation of prior interactions. See pattern `I-03`.

**Identity-Carrying Agent**
An agent architecture in which every action the agent takes is attributable to a specific, auditable identity (the invoking user, a scoped service identity, or a delegated identity) rather than a shared, ambient credential. See pattern `C-03`.

## Classification terms

**Established (E)**
A concept already recognized and documented in existing industry or academic literature. AQEVON's contribution, if any, is applying or contextualizing it within the meta-model — not originating it.

**Synthesized (S)**
AQEVON combines, reframes, or elevates existing concepts into a higher-order architectural formulation not previously documented in this specific combination.

**Proposed (P)**
An architectural hypothesis put forward by AQEVON that requires further research, prior-art validation, and real-world evidence before it can be considered established or even fully synthesized.

A pattern may carry a combined classification (e.g., `S/P`) where part of its formulation is synthesis of known concepts and part is a genuinely novel hypothesis. See `research/prior-art-differentiation-matrix.md` for the full classification review and `GOVERNANCE.md` for how classification changes over a pattern's lifecycle.

## Pattern lifecycle terms

See `GOVERNANCE.md` for full definitions of **Proposed → Research → Validated → Published → Mature → Deprecated**.

## Usage discipline

- Use "AI-native architecture," not "AI architecture" or "intelligent architecture," when referring to this framework's subject matter.
- Use "Enterprise Knowledge Fabric," not "knowledge base," "knowledge graph" (a component of the Fabric, not a synonym for it), or "RAG system," when referring to the governed knowledge layer pattern.
- Use "Autonomy Gradient," not "autonomy levels" or "AI maturity," when referring to the A0–A5 scale specifically.
- Do not use "AI Capability Envelope" interchangeably with "agent scope" — the Envelope applies to any AI-native capability, not only agentic ones.
- Do not use "AI Control Plane" to mean any single product or platform; it names an architectural layer that may be implemented by multiple systems working together.
