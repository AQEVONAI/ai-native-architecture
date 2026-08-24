# Differentiation

What AQEVON's AI-Native Architecture Pattern Language actually contributes, stated plainly and without overclaiming, in light of the prior art found during the August 2026 research pass (`prior-art-differentiation-matrix.md`). This document exists so that AQEVON's own team, and eventually the market, can see exactly where this framework organizes existing practice versus where it proposes something not found elsewhere — the same E/S/P honesty this framework requires of every individual pattern, applied to the framework as a whole.

## The honest headline

Most of what makes AI-native architecture work — grounded retrieval, model routing, policy-as-code authorization, execution tracing, evaluation gates — is not new, and this framework does not claim otherwise. Of the 17 patterns cataloged, 2 are classified fully Established (`K-01`, `I-01`), and a majority carry at least a partial Established or Synthesis classification. This is by design, not a shortcoming: `framework/principles.md` treats prior-art honesty as a governing principle specifically because the AI architecture field is currently full of frameworks that overstate their novelty, and AQEVON is deliberately positioning against that pattern.

What AQEVON contributes, where it does, falls into three categories:

### 1. A unifying meta-model connecting previously separate practices

Model routing (`I-01`), execution tracing (`O-01`), policy-as-code authorization (`C-02`), and knowledge grounding (`K-01`) are each independently established, but the research pass found no existing framework that organizes all of them under one coherent six-domain meta-model with explicit cross-domain relationships (see `framework/meta-model.md`). This connective structure — not any single pattern within it — is where the strongest, most defensible differentiation claim lives.

### 2. Specific syntheses applying established principles to AI-native concerns

Several patterns take a genuinely established principle from an adjacent field and apply it specifically to an AI-native architectural concern in a way not found packaged this way elsewhere:

- `A-02` (Bounded Agent) applies the decades-established principle of least privilege specifically through the AI Capability Envelope's six facets.
- `K-03` (Knowledge Federation) applies Data Mesh's federated-governance principle specifically to AI knowledge retrieval across independently governed sources.
- `O-03` (Graceful AI Degradation) applies the established circuit-breaker pattern specifically to AI-native dependency types (model quality degradation, knowledge staleness) with an explicit degradation-signaling requirement not consistently found in general-purpose resilience literature.

These are honestly classified `S` or `S/P`, not `P` — the underlying principle is not AQEVON's contribution, the specific application is.

### 3. A small set of genuinely proposed, evidence-required concepts

Three patterns — `I-03` (Governed Memory), `C-03` (Identity-Carrying Agent, flagged for review, see below), and `E-02` (AI Architecture Evolution Loop) — remain classified with a `P` component because no directly comparable named practice was found during this research pass. These are AQEVON's actual novel hypotheses, and are labeled as hypotheses, not established fact, in every place they appear in the catalog.

## Corrections this research pass required

Prior-art honesty is only meaningful if it results in actual corrections when evidence warrants one. Two findings from this pass are recorded here in full, not summarized away:

### A-01 (Autonomy Gradient): P → S

AQEVON's original hypothesis for `A-01` treated the A0–A5 autonomy scale, and its analogy to SAE's levels of driving automation, as a proposed AQEVON contribution. This research pass found that comparable graduated-autonomy frameworks already exist and are gaining traction as of the time of research — most notably a "Levels 1–5" framework for agentic AI (Open Data Science / Datasaur) and the Cloud Security Alliance's January 2026 "Autonomy Levels for Agentic AI," both of which explicitly draw the same SAE-levels analogy AQEVON's `A-01` uses. Fluree's "Six Levels of the Autonomous Enterprise" is a further independent example of the same graduated-scale approach.

This is not a superficial coincidence — the core mechanism (a small number of ordered levels, explicit human-oversight requirements decreasing as level increases, an SAE-borrowed structure) matches closely enough that classifying `A-01` as a AQEVON-original proposal would not be honest. `A-01`'s classification has been corrected to `S` — synthesis of an approach that, evidence now shows, others have also independently converged on, applied within AQEVON's specific six-domain meta-model and connected explicitly to the `C-01`/`C-02` control mechanisms and `O-01` observability requirements that make a given level defensible. The pattern card, front-matter, and `patterns/index.yaml` have been updated accordingly (see each file's Revision History).

This correction does not diminish `A-01`'s importance to the framework — it remains a flagship concept — but it does change the honest answer to "did AQEVON invent this," and that answer matters more than preserving an aspirational classification.

### C-03 (Identity-Carrying Agent): flagged for review, not yet corrected

Research found "agentic identity" — composite, short-lived, delegation-scoped identity specifically for AI agents — is an actively emerging named concept, most concretely described by WorkOS's access-control guidance (workload identity, end-user identity, resource identity as three distinct layers; "Zero Standing Permissions" as an explicit principle) and echoed by Oso. This is meaningfully closer to established practice than `C-03`'s original `P` classification assumed.

It was not corrected to `S` in this pass because the specific framing AQEVON uses — a fully carried identity propagated through every layer of multi-step agent execution, evaluated at every downstream authorization point — was not found described with that exact completeness in the sources reviewed; the WorkOS/Oso material describes the identity-layer taxonomy clearly but not, as consistently, the full propagation-through-execution requirement. Rather than force a classification decision on ambiguous evidence, `C-03` is flagged explicitly for re-review at the next research cycle (see `research-methodology.md`), which is the conservative, honest choice this framework's own principles require when evidence is suggestive but not conclusive.

## What this means going forward

`E-02` (AI Architecture Evolution Loop) applies to AQEVON's own catalog, not only to the systems it describes — this research pass and its corrections are that loop in action, applied to the framework's own classifications. Every future research cycle should be expected to produce at least one classification change as the field moves; a research pass that confirms every existing hypothesis without exception would itself be a signal the research was not conducted rigorously enough.

## Revision History

- 0.1.0 (2026-08-24) — Initial differentiation document. Recorded the A-01 classification correction (P→S) and the C-03 review flag, both applied during this research pass.
