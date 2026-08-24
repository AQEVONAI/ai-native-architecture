# 05 — Common Pitfalls

## The "just reuse the config" temptation

**How it would appear here:** Copying Lab 03's Envelope and autonomy-level assignment for the new capability because they're topically related (both concern tickets), rather than independently justifying the new capability's own Envelope and level.

**How this lab avoids it:** `04-decision-points.md` names this temptation explicitly and explains why `A-01`'s per-capability discipline requires independent justification even for related capabilities — this is a specific, concrete instance of the general principle that autonomy assignment must track actual risk and action scope, not surface similarity.

## AP-06 — Autonomous Privilege Creep (the "just add write access later" version)

**How it would appear here:** A future request to let the workload assistant "just go ahead and execute the rebalance it suggests, to save the manager a step" — added as a seemingly small UX improvement, without recognizing this would mean adding write/execute authority to a capability explicitly designed and justified as read-only/suggest-only (Step 3's Envelope explicitly excludes execution tools).

**How this lab avoids it:** By making the Envelope's exclusion of execution authority explicit and load-bearing in the design ("No execution authority" is stated directly, not left implicit), any future proposal to add it must explicitly confront and revise that stated constraint, rather than being folded in as an incremental change that erodes it silently.

## Silent infrastructure duplication

**How it would appear here:** Building a new, separate trace store or evaluation pipeline for this third capability because it seemed faster than integrating with the existing shared infrastructure from Lab 04 — quietly reintroducing the siloed-observability problem `RA-05` and Lab 04 were specifically built to avoid.

**How this lab avoids it:** Steps 4-5 explicitly instruct extending the existing schema and pipeline rather than building new ones, and `06-validation-checklist.md` includes a specific check for this.

## Over-trusting the reuse audit table

The `02-architecture-walkthrough.md` reuse audit table is a design intent, not a guarantee — Step 6 explicitly flags that if the `E-02` aggregation job requires code changes to pick up the new capability (rather than working automatically), that is itself a finding worth recording, because it reveals the "generically built" claim from Lab 04 was, in practice, less generic than assumed. Treat every "reused directly" claim in the audit table as a hypothesis to verify, not an assumption to build on unchecked.
