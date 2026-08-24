# 05 — Common Pitfalls

## AP-05 — Context Dumping (applied to persisted memory)

**How it would appear here:** Retrieving all of an employee's stored memory items and appending them all to context on every session, regardless of relevance to the current question — the memory-specific version of unranked context inclusion.

**How this lab avoids it:** Step 4's retrieval should still be relevance-filtered against the current question, not a blanket dump of everything owned by the employee — `I-03`'s Related Patterns section explicitly connects it to `I-02` (Context Budgeting) for exactly this reason, even though this lab does not implement full `I-02` budgeting in depth (that's part of Lab 01's scope for the knowledge side; memory retrieval here should follow the same relevance-filtering discipline).

## A near-miss: treating memory as implicitly trusted

Not a named anti-pattern directly, but a real risk flagged in `I-03`'s Security Considerations: treating retrieved memory as "the system's own data" and therefore exempt from the same scoped-retrieval discipline applied to Lab 01's HR/IT knowledge sources. This lab's Step 4 explicitly requires memory retrieval to be scoped by `C-03` identity with the same rigor as any other `K-02`-governed retrieval — memory is not a shortcut around that discipline.

## AP-06 — Autonomous Privilege Creep (in miniature)

**How it would appear here:** The high-consequence recommendation path (Step 5) quietly evolving, over incremental changes, from "surface a recommendation requiring confirmation" to "auto-create the expedited ticket, and just notify the employee" — each incremental change (e.g., "let's also auto-create it if the employee doesn't respond within a day, to save them time") individually reasonable, cumulatively eroding the `C-01` boundary this lab deliberately established in `04-decision-points.md`.

**How this lab avoids it:** By recording the `DF-06` decision explicitly, with its reasoning (memory staleness risk), so any future proposal to loosen this boundary has to explicitly address why that risk no longer applies, rather than being approved as a small, isolated UX improvement.
