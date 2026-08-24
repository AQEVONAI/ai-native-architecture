# Governance

This document defines how content in the AQEVON AI-Native Architecture repository is classified, reviewed, and matured. It applies to every pattern, anti-pattern, reference architecture, decision guide, and assessment document.

## Pattern lifecycle

Every pattern moves through a defined lifecycle, tracked in its front-matter `status` field:

```
Proposed → Research → Validated → Published → Mature → Deprecated
```

- **Proposed** — a pattern has been named and given an initial classification hypothesis (`E`/`S`/`P`) but has not yet been through prior-art review or scenario validation. Content may be incomplete.
- **Research** — the pattern has a complete standard pattern card (see `patterns/README.md`) but its prior-art classification and real-world applicability are still under active investigation.
- **Validated** — the pattern has passed all four validation requirements below.
- **Published** — a validated pattern that has been reviewed for public-facing readiness (see `website-content/` distinction between Established / Emerging / Research / Proposed).
- **Mature** — a published pattern with a stable definition across at least one major version, used in at least one documented reference architecture or lab without material revision.
- **Deprecated** — a pattern superseded by a newer formulation, or found through validation to be unsound. Deprecated patterns are not deleted; they remain in the repository with `status: deprecated` and a note pointing to their replacement, so historical references and external links do not break.

## Requirements for "Validated" status

A pattern may only move from **Research** to **Validated** once all four of the following are complete:

1. **Prior-art review** — a corresponding row exists in `research/prior-art-differentiation-matrix.md`, evaluated against TOGAF, Zachman, GoF/POSA, cloud-provider precedent (Azure/AWS/GCP), NIST, OWASP, and academic/research precedent, with either evidence or an explicit "Evidence required" marker for each.
2. **Evidence** — every non-obvious claim in the pattern's `Known Uses / Evidence` section is either sourced (linked in `research/sources.md`) or explicitly marked as an AQEVON hypothesis, never presented as an unsupported fact.
3. **Architecture scenario validation** — the pattern has been exercised in at least one architecture lab (`labs/`) or reference architecture (`reference-architectures/`) against a realistic enterprise scenario, and that usage is cross-referenced in the pattern's `Related Patterns` / `Known Uses` sections.
4. **Peer review** — a second reviewer (internal, until an external contributor process exists — see `CONTRIBUTING.md`) has confirmed the pattern's standard card is complete, its classification is defensible given the prior-art review, and it makes no unsupported originality claims per `framework/principles.md` §4.

## Classification governance

A pattern's classification (`E` / `S` / `P`, or a combined form such as `S/P`) is a **hypothesis until Validated status**. Classification changes are expected and normal as prior-art research proceeds — they are not failures, they are the review process working as intended. Every classification change must be recorded in the pattern's `Revision History` section and, where material, noted in `CHANGELOG.md`.

## Quality bar

Every document created in this repository must be able to answer the eight questions in `framework/principles.md` §6. A document that only defines a term without addressing forces, trade-offs, and applicability boundaries does not meet the bar and should remain in `Proposed` or `Research` status.

## Review cadence

Given the current stage of the framework (v0.x, single-maintainer research phase — see `VERSIONING.md`), formal review cadence has not yet been established. This section will be expanded once the contributor base grows beyond the initial AQEVON research team.

## Content classification for public exposure

Separately from the pattern lifecycle, every piece of content is also classified for exposure purposes:

- **PUBLIC NOW** — accurate, reviewed, safe to publish via `website-content/` or elsewhere.
- **RESEARCH / BETA** — accurate as a statement of current thinking, but explicitly marked as unvalidated research when exposed publicly.
- **INTERNAL AQEVON** — not yet ready for any public exposure (e.g., early-stage lab notes, unreviewed hypotheses).
- **FUTURE COMMERCIAL PRODUCT** — content whose purpose is to seed a future paid AQEVON offering (e.g., the assessment framework, the architecture decision engine) and is not to be given away as open public content without a deliberate decision to do so.

This classification is applied per-document in the Final Validation Report each time a major content pass is completed (see `CHANGELOG.md`).
