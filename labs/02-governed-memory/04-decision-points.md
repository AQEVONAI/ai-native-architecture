# 04 — Decision Points

## DF-08 — When to Introduce Governed Memory

**Applied at:** the initial decision to build this lab at all, in response to the employee feedback described in `01-scenario-and-objectives.md`.

**Decision:** Memory is justified here — the capability's value proposition (not needing to re-explain context each session) is genuinely degraded without it, per `DF-08`'s first decision gate. Reliable per-employee identity (`C-03`) is already available from Lab 01's authentication. Organizational capacity to own retention/deletion enforcement was confirmed before proceeding (Step 6/7 of the implementation guide are treated as required, not optional, deliverables) — per `DF-08`'s capacity gate, this lab would not have proceeded without that confirmation.

## DF-06 — Human Authorization vs. Policy-Bounded Execution

**Applied at:** deciding how the assistant should act on `reported_issue` memory that suggests a high-consequence outcome.

**Decision:** `C-01` (human authorization, i.e., requiring the employee's own confirmation) rather than `C-02` (policy-bounded automatic execution). Per `DF-06`'s decision tree: the volume of this specific action (expedited-replacement recommendations) is low, and the consequence (an expedited replacement being created based on possibly-stale memory) is not so easily reversible that automatic action is clearly safe. This is a deliberately conservative choice appropriate to memory-informed actions specifically, where staleness (per `I-03`'s own Trade-offs section) is a known, unresolved risk — acting automatically on memory that might be stale is a materially different risk profile than acting on freshly retrieved knowledge.

## What would change this lab's decisions

If evaluation data (`O-02`, covered in Lab 04) later showed `reported_issue` memory is reliably fresh and the expedited-replacement recommendation is consistently correct when surfaced, `DF-06`'s tree would support reconsidering a move toward `C-02` for this specific action — but that reconsideration should be evidence-driven (per this framework's `E-02` evolution-loop discipline), not a default loosening over time.
