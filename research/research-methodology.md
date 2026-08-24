# Research Methodology

How prior-art research for this framework was conducted, and what standard a claim must meet to be classified Established (`E`), Synthesis (`S`), or Proposed (`P`) in `patterns/index.yaml` and each pattern card's front-matter. See `framework/terminology.md` for the formal definitions this methodology operationalizes.

## Why this document exists

`framework/principles.md` states prior-art-before-originality as a governing principle: no pattern in this catalog may claim to be more novel than it actually is. That principle is only credible if it is backed by an actual, repeatable research process — not asserted once at launch and left unverified as the field moves. This document is that process.

## Research process

For each pattern and anti-pattern, research consisted of:

1. **Web search for directly comparable concepts.** Search queries targeted the pattern's core mechanism (e.g., "AI agent autonomy levels framework," "policy as code AI agent authorization," "LLM model routing framework") rather than AQEVON's own terminology, specifically to avoid confirmation bias toward finding only sources that already use AQEVON's language.
2. **Identification of the closest existing named practice, framework, or product category**, if any, and an honest assessment of how closely it matches the pattern's actual claim (intent + solution), not just its general subject area.
3. **Classification against the E/S/P standard** (below), defaulting to the more conservative (less novel) classification when evidence is ambiguous, consistent with the evidence-over-assertion principle.
4. **Recording of specific, checkable sources** in `sources.md`, rather than general statements like "this is well known in the industry."

## Classification standard

- **Established (`E`)** — the pattern's core mechanism is already named, documented, and in active use as described, by multiple independent sources, prior to and independent of this framework. AQEVON's contribution for an `E`-classified pattern is, at most, organizing it within this framework's structure — not inventing the underlying mechanism.
- **Synthesis (`S`)** — the pattern combines established mechanisms or principles from adjacent, previously separate domains (e.g., applying least-privilege access control, a security principle with decades of prior art, specifically to AI agent tool scoping) into a treatment specific to AI-native architecture that was not, at the time of research, found packaged this way elsewhere.
- **Proposed (`P`)** — AQEVON has not found directly comparable prior art for the pattern's core claim at the time of research. This is an explicit flag that the pattern is a hypothesis requiring further validation, not a claim of confirmed originality — absence of found evidence is not evidence of absence, and `P` classifications are reviewed and re-searched on the same cadence as the rest of this research.

A pattern may carry a combined classification (e.g., `S/P`, `E/S`) when different aspects of the same pattern warrant different classifications — this is recorded explicitly in the pattern's Known Uses / Evidence section rather than resolved to a single label that would obscure the distinction.

## Limitations and honesty about this research's scope

- This research was conducted via web search over a bounded set of queries in August 2026, not a systematic literature review or a formal patent/prior-art search. It is sufficient to avoid overclaiming novelty in good faith, not sufficient to serve as legal prior-art clearance.
- Search results are dated to the time of research and reflect the field's state as of August 2026 — a fast-moving field, where an item classified `P` today may have comparable prior art emerge within months. This is precisely why `E-02` (AI Architecture Evolution Loop) applies to this framework's own patterns, not only to the systems it describes.
- Absence of a found source is reported honestly as "not found at time of research," never as "does not exist" — see `differentiation.md` for cases where this distinction materially affected a classification decision.

## Review cadence

This research should be re-run, at minimum, at each minor version increment of the overall framework (see `VERSIONING.md`), and immediately upon any external report that comparable prior art exists for a pattern currently classified `P` or `S/P`.

## Revision History

- 0.1.0 (2026-08-24) — Initial methodology document, applied retroactively to the initial 17-pattern, 8-anti-pattern catalog.
