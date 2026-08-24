# Contributing

This repository is the canonical source of truth for AQEVON's AI-Native Architecture Pattern Language. Contributions are held to the standard of a professional enterprise-architecture research body of knowledge — see `framework/principles.md` and the quality bar in `GOVERNANCE.md`.

## Before proposing a new pattern

A new pattern must address a **recurring** architectural problem — one an architect will encounter across multiple, unrelated engagements — not a one-off implementation detail. Before opening a contribution, confirm:

- The problem is not already covered by an existing pattern (check `patterns/index.yaml`).
- The problem is not better addressed by an anti-pattern (i.e., is this a problem with a good solution, or a recurring mistake to warn against?).
- The problem fits within one of the six domains in `framework/meta-model.md`, or represents a genuine gap in the meta-model itself (rare — raise this as a framework-level discussion, not a pattern proposal).

## What a pattern contribution must include

Every new pattern must use the standard pattern card structure defined in `patterns/README.md`, and the contributor must, at minimum:

1. **Explain the recurring problem** the pattern solves, in concrete architectural terms.
2. **Provide evidence** — real-world usage, documented precedent, or a clearly labeled AQEVON hypothesis if evidence does not yet exist.
3. **Identify prior art** — what existing frameworks, vendor guidance, or academic research already address this problem, even partially. If prior art is unclear after reasonable investigation, state "Prior art requires further validation" rather than omitting the section or implying novelty.
4. **Describe the forces** in tension that make this problem non-trivial (see the pattern card's `Forces` section).
5. **Describe the trade-offs** of the proposed solution — every pattern has costs; a pattern with no stated trade-offs has not been thought through completely.
6. **Provide an architecture** — a Solution and Architecture section concrete enough that two different architects would implement recognizably similar systems from it.
7. **Identify related patterns and anti-patterns** — the pattern must be positioned within the existing catalog, not left as an island.
8. **Avoid unsupported novelty claims** — propose classification honestly (`E`/`S`/`P`) per `framework/terminology.md`; do not claim `E` (Established) without citing the established source, and do not claim AQEVON "invented" anything without evidence per `framework/principles.md` §4.
9. **Avoid vendor lock-in** — the conceptual Solution and Architecture must be vendor-neutral; vendor-specific guidance belongs only in the pattern's `Vendor Mappings` section.

## Contribution workflow

1. Draft the pattern using the standard card template (`patterns/README.md`).
2. Add the pattern's stable ID, name, and metadata to `patterns/index.yaml`.
3. Run `scripts/validate-framework.py` locally to check structural completeness, unique IDs, and valid cross-references.
4. Submit for review. New patterns enter the repository at `Proposed` or `Research` status (see `GOVERNANCE.md`) — never `Validated` or above on first contribution.
5. Prior-art review happens against `research/prior-art-differentiation-matrix.md`; the contributor's proposed classification may change as a result. This is expected, not a rejection.

## Style and tone

- Follow `framework/terminology.md` exactly for controlled vocabulary — do not introduce synonyms for established AQEVON terms.
- Write for a working enterprise architect, not a general audience — assume architectural literacy, avoid re-explaining fundamentals covered elsewhere.
- No emoji-heavy formatting, no marketing language, no unqualified superlatives ("revolutionary," "groundbreaking").
- Prefer Mermaid diagrams for conceptual architecture over prose-only descriptions or external image files.
- Every claim that could be mistaken for a verified fact must be sourced or explicitly hedged ("AQEVON's hypothesis is...", "Evidence required.").

## Anti-pattern, reference architecture, decision guide, and lab contributions

Follow the same evidentiary and structural discipline as pattern contributions, using the respective templates in `anti-patterns/README.md`, `reference-architectures/`, `decision-framework/`, and `labs/`. All cross-references (related patterns, anti-patterns) must resolve to real IDs — this is checked by `scripts/validate-framework.py`.

## What will not be accepted

- Patterns, articles, or reference architectures that fabricate case studies, statistics, or citations.
- Content that presents vendor-specific architecture as universally applicable.
- Content claiming AQEVON originality without a supporting prior-art review.
- Duplicate documents covering the same recurring problem as an existing pattern without a clear, stated reason for the duplication (e.g., superseding an existing pattern, which should instead be a revision with a recorded classification/version change).
