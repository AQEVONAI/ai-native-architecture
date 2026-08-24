---
id: DF-04
name: When to Build an Enterprise Knowledge Fabric
decision: Whether an organization's current stage warrants investing in the full K-02 Enterprise Knowledge Fabric, versus simpler single-source retrieval.
related_patterns: [K-01, K-02, K-03, E-01]
last_reviewed: 2026-08-24
---

# DF-04 — When to Build an Enterprise Knowledge Fabric

## The Decision

Decide whether to invest in the full governed, federated Enterprise Knowledge Fabric (`K-02`) now, or to build simpler single-source grounded retrieval (`K-01`) and defer fabric-level investment until it is actually warranted.

## Why This Is Hard

`K-02` is a flagship concept of this framework and can read as the "correct" target architecture for any knowledge-grounded capability — but a fabric's governance, federation, and freshness-loop apparatus (`K-03`, `E-01`) is real, ongoing organizational and engineering investment that is only worth paying once the underlying need (multiple sources, meaningful access-control complexity, sustained freshness requirements) is actually present. Building it prematurely is itself a form of over-engineering this framework's other principles (see `framework/principles.md`'s complexity-justified-by-capability principle) argue against.

## Decision Inputs

- Number of distinct, independently governed knowledge sources the capability (or capability portfolio) actually needs to draw on.
- Access-control complexity — does content require per-user or per-role filtering beyond a single source's native access control?
- Freshness requirements — how volatile is the underlying knowledge, and how costly is staleness if unaddressed?
- Number of capabilities expected to share this knowledge investment — a fabric's cost amortizes across multiple capabilities far better than a single one.

## Decision Tool

```
Does more than one capability need to draw on overlapping
knowledge sources, or is a second capability with similar
knowledge needs expected within a reasonably near-term horizon?
│
├── NO (a single, standalone capability, no near-term second
│    use case) → Single-source K-01 grounded retrieval.
│    Building K-02 now is premature investment.
│
└── YES → Does the knowledge span more than one independently
          governed source (different owning teams, different
          native access control, different systems)?
          │
          ├── NO (one source, shared across capabilities) →
          │    A shared K-01 retrieval layer with basic
          │    governance may suffice; K-03 federation is not
          │    yet needed.
          │
          └── YES → Build K-02 with K-03 federation. Also
              confirm E-01 (freshness loop) is resourced —
              a fabric without a freshness loop degrades into
              AP-04 (Vector Database as Knowledge Architecture)
              over time.
```

## Recommendation Guidance

Start with the narrowest retrieval implementation that serves the first real capability, and let the fabric emerge as a second and third capability reveal genuine shared, cross-source knowledge needs — rather than building the fabric speculatively ahead of demonstrated need. This is consistent with `RA-01`'s framing of the fabric as infrastructure that amortizes across capabilities, not a per-capability cost.

## Common Mistakes

- Building the full fabric for a single capability's launch, before a second capability exists to justify the shared investment.
- Conversely, continuing to bolt single-source retrieval onto capability after capability well past the point where the organization clearly has multiple independently governed sources that need reconciling — this is the mirror-image mistake, usually caused by treating the fabric decision as a one-time choice rather than revisiting it as the capability portfolio grows.

## Related Patterns

`K-01` (the recommended starting point), `K-02` (the target once warranted), `K-03` (federation, once multiple sources are genuinely in play), `E-01` (required once the fabric exists, not optional).

## Revisit Triggers

A second or third capability emerging with overlapping knowledge needs; access-control requirements outgrowing a single source's native capability; staleness incidents indicating an ad hoc re-sync process is no longer sufficient.

## Revision History

- 0.1.0 (2026-08-24) — Initial decision guide.
