# 01 — Scenario and Objectives

## Scenario

*Illustrative composite scenario, consistent with `assessment/worked-example.md`.*

A mid-size enterprise software company wants an internal support assistant that employees can ask questions like "how many vacation days do I accrue in my second year" (HR policy) and "how do I request a new laptop" (IT knowledge-base). The two source sets are owned by different teams: HR policy documents live in an HR-owned document management system, and IT knowledge-base articles live in a separate IT-owned wiki. Some IT articles are restricted to specific roles (e.g., administrative access procedures visible only to IT staff); HR documents are visible to all employees except a small number of confidential HR-only policy documents.

## Question types the capability must handle

- Single-source factual questions ("how many sick days do I get") — answerable from one source.
- Single-source but access-restricted questions ("how do I reset an administrator password") — must respect the requesting employee's role.
- Cross-source questions ("if I'm on leave, does my equipment request get paused") — requires reconciling HR and IT content in one answer.
- A small number of exactly-answerable structured questions ("what is the current help desk phone number") — better served by direct lookup than retrieval.

## Success Criteria

- Every generated answer to a knowledge question cites its specific source document.
- An employee never receives content from a document their role does not authorize.
- HR and IT content are federated (queried in their owning systems) rather than migrated into one centralized store, since both are actively maintained systems of record (see `04-decision-points.md` for why).
- A change to a source document (e.g., an updated PTO policy) is reflected in the capability's answers within a defined, bounded time window, not indefinitely stale.
- The one identified exactly-answerable structured question type (help desk phone number) is answered via direct lookup, not retrieval-and-generation.

## What This Lab Does Not Cover

Memory/personalization (Lab 02), autonomous action (Lab 03), and full observability instrumentation (Lab 04) are out of scope here — this lab isolates the Knowledge domain. Lab 05 shows how this capability's fabric becomes shared infrastructure for a second capability.
