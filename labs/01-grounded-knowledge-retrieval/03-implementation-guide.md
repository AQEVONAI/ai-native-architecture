# 03 — Implementation Guide

Vendor-neutral build steps. This guide describes the shape of each step, not a specific product's configuration syntax — pair with `decision-framework/DF-10`-style build-vs-buy evaluation for actual tool selection.

## Step 1 — Question-type router

Implement a lightweight classification step ahead of everything else that distinguishes structured/exact questions (route to direct lookup) from knowledge questions (route to the fabric). This does not need to be sophisticated — a small set of known structured-answer intents (phone numbers, specific policy numbers) classified with high precision is sufficient; anything not confidently classified as structured routes to knowledge retrieval by default, consistent with `DF-03`'s decision tree.

```
question -> classifier -> { structured_lookup | knowledge_retrieval }
```

## Step 2 — Federation connectors

Build a connector per source (HR document system, IT wiki) that can: (a) retrieve content relevant to a query, and (b) report the access-control metadata (role restrictions, if any) attached to each piece of content natively. Do not build a connector that retrieves content without also retrieving its access metadata — this is the specific gap that produces `AP-04`'s access-control failure mode.

```
connector(source) -> { content, source_id, access_metadata }
```

## Step 3 — Fabric-layer authorization

At the fabric layer, filter candidate content by the requesting employee's actual role against each item's access metadata, before any content reaches the ranking/budgeting step. This ordering matters: authorization must happen before ranking, not as a post-hoc filter on an already-ranked, already-assembled context.

```
authorized_content = [c for c in federated_content if authorize(employee_role, c.access_metadata)]
```

## Step 4 — Context budgeting

Rank `authorized_content` by relevance to the query, and assemble it into the model's context within a defined token budget, per `I-02`. For cross-source questions, ensure the ranking step operates across both sources jointly (not "top 3 from HR plus top 3 from IT regardless of relevance") so the highest-relevance content overall — not per-source — fills the budget.

## Step 5 — Grounded answer generation

Generate the answer with an explicit constraint that every claim must cite one of the assembled, authorized content items — implemented as a structural requirement on the generation step (e.g., requiring inline citation markers resolved against the assembled content set), not merely a prompt instruction asking the model to cite sources.

## Step 6 — Evolution loop

Implement a scheduled job per source that detects content change (via the source's native change-notification if available, or periodic diffing if not) and propagates updates into whatever the fabric's ranking/retrieval step reads from. Tune polling cadence per source based on each source's actual observed change rate — do not use one global interval for both HR (infrequent changes) and IT (more frequent changes).

## Step 7 — Direct-lookup path

For the structured-question branch from Step 1, implement a direct, deterministic lookup (a small key-value store or direct query against the authoritative field) rather than routing these questions through Steps 2–5 at all.

## Verification

After implementation, proceed to `06-validation-checklist.md`.
