---
lab_id: LAB-04
name: AI Observability & Evaluation
target_reference_architecture: RA-04
last_reviewed: 2026-08-24
---

# Lab 04 — AI Observability & Evaluation

## Objectives

By the end of this lab, you should be able to: instrument full execution tracing across identity, retrieval, policy, and action (`O-01`); build an evaluation gate that genuinely blocks promotion, not just reports scores (`O-02`); implement explicit, signaled degradation for a dependency failure (`O-03`); and stand up a minimal recurring review cycle (`E-02`).

## Prerequisites

- Read `patterns/operations/O-01-ai-execution-trace.md`, `O-02-ai-evaluation-gate.md`, `O-03-graceful-ai-degradation.md`, and `patterns/evolution/E-02-ai-architecture-evolution-loop.md`.
- Read `reference-architectures/RA-04-ai-observability-evaluation.md`.
- This lab retrofits full observability onto Labs 01–03's capabilities, which used only stub logging. Completing Labs 01–03 first is recommended but not required — this lab is self-contained if you start here.

## Target Reference Architecture

`RA-04` — AI Observability & Evaluation, composing `O-01`, `O-02`, `O-03`, `E-02`.

## What You'll Build

A shared observability backbone instrumented across the support assistant (Lab 01/02) and the ticket-update agent (Lab 03): unified execution tracing, an evaluation gate blocking unsafe prompt/retrieval/policy changes from reaching production, explicit degradation handling for a knowledge-source outage, and a minimal scheduled review cycle that closes the loop identified in `assessment/worked-example.md`'s roadmap.

## Lab Files

1. `01-scenario-and-objectives.md`
2. `02-architecture-walkthrough.md`
3. `03-implementation-guide.md`
4. `04-decision-points.md`
5. `05-common-pitfalls.md`
6. `06-validation-checklist.md`
7. `07-exercises.md`
8. `08-solutions-and-discussion.md`
