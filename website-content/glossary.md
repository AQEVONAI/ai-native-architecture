---
status: content-prep-only
target_audience: enterprise architects, CTOs, technical buyers
last_reviewed: 2026-08-24
---

# Glossary

Plain-language definitions of terms used across AQEVON's AI-native architecture content. For the fuller, more formal internal version of this glossary (including the E/S/P classification system), see `framework/terminology.md` in the underlying research repository.

**AI-Native Architecture** — designing AI as a first-class architectural concern from the start, with the same rigor traditionally applied to security, observability, and change management — not bolted onto an existing system afterward.

**Autonomy Gradient** — a six-level scale (A0–A5) describing how independently an AI capability is allowed to act, from pure human decision-making to full autonomous execution.

**AI Capability Envelope** — the explicit definition of what an AI capability exists to do, what it can know, how it reasons, what tools it can use, what authority it acts under, and what actions it can take.

**Bounded Agent** — an AI agent whose access and actions are explicitly scoped and enforced, not just described in an instruction it may or may not follow.

**Enterprise Knowledge Fabric** — a governed layer connecting an organization's documents, structured data, and systems, so AI capabilities can retrieve current, access-controlled information without it living in one centralized, hard-to-maintain store.

**Grounded Retrieval** — ensuring an AI-generated answer traces back to a specific, real source, rather than being generated purely from the model's own training.

**Execution Trace** — a complete, queryable record of what an AI capability did for a given request: what it looked up, what it decided, what action it took, and who or what it was acting for.

**Evaluation Gate** — a required quality check a change to an AI capability must pass before it's allowed to reach production.

**Policy-Bounded Action** — constraining what an AI capability may do using an enforced, machine-checkable rule, instead of a prompt instruction it might not follow.

**Identity-Carrying Agent** — an AI agent whose every action is attributed to a specific, accountable identity — the person or system it's acting for — rather than a shared, anonymous credential.

**Anti-Pattern** — a specific, recurring way AI-native architecture goes wrong, named so it can be recognized and avoided rather than rediscovered the hard way.
