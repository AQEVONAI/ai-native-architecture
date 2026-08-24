# Versioning

## Framework version

The repository as a whole carries a framework version, tracked in `CHANGELOG.md`:

- **v0.x** — Research. The framework, meta-model, and pattern catalog are under active development and may change materially between minor versions. Not recommended as a stable integration target.
- **v1.0** — First stable public edition. The six-domain meta-model, the core pattern catalog, and the flagship concepts are considered stable; breaking conceptual changes require a major version bump from this point forward.
- **v1.x** — Additive changes. New patterns, reference architectures, labs, and content may be added; existing published/mature patterns are not redefined in breaking ways.
- **v2.0** — Major conceptual changes (e.g., a change to the six-domain meta-model itself, or a breaking redefinition of a flagship concept).

## Pattern-level versioning

Every individual pattern, anti-pattern, and reference architecture carries its own `version` field in front-matter, independent of the overall framework version. A pattern's version increments according to standard semantic conventions applied to conceptual content:

- **Patch** (0.1 → 0.1.1) — wording clarification, typo fix, added example, no change to the pattern's Solution or Architecture.
- **Minor** (0.1 → 0.2) — additive change: new section content, expanded trade-offs, added related-pattern links, classification refinement following prior-art review.
- **Major** (0.x → 1.0, or 1.x → 2.0) — a change to the pattern's core Solution, Architecture, or Intent that would require an architect who used the previous version to re-evaluate their design.

## Git and release model

`main` is the active research/development branch. It is expected to change frequently and is not the recommended integration target for any downstream consumer, including the AQEVON website.

Stable snapshots are published as tagged releases:

```
v0.1.0
v0.2.0
v1.0.0
```

**The AQEVON website should consume a tagged release, not `main` directly**, once website integration is implemented (see `website-content/integration.md` — not yet built, per this repository's current scope). This avoids the website silently breaking or displaying half-finished research content whenever this repository's `main` branch is updated. A release is cut only when:

1. All patterns referenced by the release are at least at `Research` status (see `GOVERNANCE.md`) — no broken or empty pattern cards.
2. `scripts/validate-framework.py` passes with no errors.
3. `CHANGELOG.md` has been updated for the release.

## Change tracking

All framework-level and pattern-level version changes are recorded in `CHANGELOG.md`. Classification changes resulting from prior-art review (see `GOVERNANCE.md`) are recorded in both `CHANGELOG.md` and the individual pattern's `Revision History` section.
