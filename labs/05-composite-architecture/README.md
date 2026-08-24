---
lab_id: LAB-05
name: Composite AI-Native Architecture
target_reference_architecture: RA-05
last_reviewed: 2026-08-24
---

# Lab 05 — Composite AI-Native Architecture

## Objectives

By the end of this lab, you should be able to: extend an established shared infrastructure (Knowledge fabric, Operations backbone) to a genuinely new, third capability without duplicating it; apply the full `RA-05` composite view to reason about cross-domain interdependencies; and run a complete assessment-to-roadmap cycle (`assessment/`) against the resulting multi-capability portfolio.

## Prerequisites

- Complete Labs 01–04, or at minimum read all four labs' `README.md` and `02-architecture-walkthrough.md` files — this lab assumes the support assistant, its memory extension, the ticket agent, and the shared observability backbone all exist.
- Read `reference-architectures/RA-05-composite-ai-native-enterprise-architecture.md`.
- Read `assessment/` in full — this lab ends with a real assessment cycle.

## Target Reference Architecture

`RA-05` — Composite AI-Native Enterprise Architecture, composing all 17 patterns.

## What You'll Build

A third capability — a manager-facing "team workload" assistant that answers questions about ticket load across a manager's team (reusing the Knowledge and Operations infrastructure from Labs 01–04) and can, with appropriate autonomy and control, suggest rebalancing ticket assignments (reusing and extending the Autonomy/Control patterns from Lab 03). The focus of this lab is not building this capability from scratch, but demonstrating how much of Labs 01–04's infrastructure it reuses versus what is genuinely new.

## Lab Files

1. `01-scenario-and-objectives.md`
2. `02-architecture-walkthrough.md`
3. `03-implementation-guide.md`
4. `04-decision-points.md`
5. `05-common-pitfalls.md`
6. `06-validation-checklist.md`
7. `07-exercises.md`
8. `08-solutions-and-discussion.md`
