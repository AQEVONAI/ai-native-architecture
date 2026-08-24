---
id: DF-05
name: Centralize or Federate Knowledge Sources
decision: Whether to consolidate multiple knowledge sources into one centrally managed store, or to federate — querying sources in place under a shared governance layer.
related_patterns: [K-02, K-03, E-01]
last_reviewed: 2026-08-24
---

# DF-05 — Centralize or Federate Knowledge Sources

## The Decision

Once `DF-04` has concluded a fabric is warranted, decide whether to centralize the organization's knowledge sources into one consolidated store, or to federate (`K-03`) — leaving sources in place, under their own native systems and ownership, and querying/reconciling across them through the fabric layer.

## Why This Is Hard

Centralization looks simpler on paper — one store, one place to secure, one thing to keep fresh — but in practice requires migrating and re-platforming content owned by other teams, which is organizationally expensive and creates a synchronization lag between the source of truth and the centralized copy. Federation avoids that migration cost but requires the fabric layer to reconcile heterogeneous native access-control models, freshness characteristics, and query interfaces across sources that were never designed to be queried together.

## Decision Inputs

- Organizational ownership — are the candidate sources owned by different teams with different update cadences and access-control models?
- Migration feasibility — is centralizing the source content technically and organizationally realistic, or would it require rebuilding systems of record that are actively maintained elsewhere?
- Query pattern — do most real questions require reconciling content across sources in a single answer, or do most questions cleanly map to one source at a time?
- Freshness tolerance — can the capability tolerate the synchronization lag a centralized copy would introduce, or does it require querying the source of truth directly?

## Decision Tool

| Consideration | Favors Centralization | Favors Federation |
|---|---|---|
| Source ownership | Single team, or willing to consolidate ownership | Multiple teams, each retaining ownership of their system |
| Migration cost | Low — content already loosely structured, portable | High — sources are actively maintained systems of record |
| Cross-source questions | Rare — most questions map to one source | Common — most valuable questions span sources |
| Freshness requirement | Tolerant of a defined sync lag | Requires querying the live source of truth |
| Governance model | Organization has (or wants) centralized governance | Organization already practices federated, domain-owned governance (e.g., an existing Data Mesh model) |

## Recommendation Guidance

Default to federation (`K-03`) when sources are actively maintained systems of record owned by different teams — this avoids the organizational cost and freshness lag of migration, and aligns with the federated-computational-governance model already established in Data Mesh practice (see `research/sources.md`). Centralization remains appropriate for genuinely low-maintenance, migratable content where consolidation reduces rather than adds operational burden.

A hybrid approach — federating the sources that are expensive or organizationally sensitive to migrate, while centralizing genuinely low-friction content — is a legitimate and common outcome, not a failure to decide.

## Common Mistakes

- Centralizing a source that is actively maintained elsewhere, creating a second, drifting copy that becomes its own staleness risk independent of `E-01`'s freshness loop for the original.
- Federating a source with no realistic native query interface, forcing the fabric layer to build and maintain a costly custom integration for content that would have been simpler to migrate once.

## Related Patterns

`K-02` (the fabric layer either approach sits beneath), `K-03` (the specific pattern for federation), `E-01` (freshness management differs meaningfully between centralized copies and federated live queries).

## Revisit Triggers

A federated source's native query interface proving too unreliable or limited to sustain federation; organizational ownership changes that make migration newly feasible or newly infeasible.

## Revision History

- 0.1.0 (2026-08-24) — Initial decision guide.
