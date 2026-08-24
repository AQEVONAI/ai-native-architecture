---
lab_id: LAB-01
name: Grounded Knowledge Retrieval
target_reference_architecture: RA-01
last_reviewed: 2026-08-24
---

# Lab 01 — Grounded Knowledge Retrieval

## Objectives

By the end of this lab, you should be able to: explain why a single retrieval mechanism is wrong for this scenario's mixed question set (`DF-03`); implement grounded retrieval (`K-01`) with source citation; federate two independently owned knowledge sources under one governed fabric (`K-02`/`K-03`); and stand up a basic freshness loop (`E-01`).

## Prerequisites

- Read `patterns/knowledge/K-01-grounded-retrieval.md`, `K-02-enterprise-knowledge-fabric.md`, `K-03-knowledge-federation.md`, and `E-01-knowledge-evolution-loop.md` before starting.
- Read `reference-architectures/RA-01-grounded-enterprise-knowledge-retrieval.md` — this lab builds a concrete instance of that architecture.
- Familiarity with `decision-framework/DF-03` and `DF-04` is assumed; this lab shows the decisions those guides describe, applied.

## Target Reference Architecture

`RA-01` — Grounded Enterprise Knowledge Retrieval, composing `K-01`, `K-02`, `K-03`, `E-01`, and `I-02`.

## What You'll Build

A grounded Q&A capability answering employee questions from two independently owned sources — an HR policy document set and an IT knowledge-base — with every answer traceable to a specific source, access-controlled by employee role, and kept current as source content changes.

## Lab Files

1. `01-scenario-and-objectives.md` — the specific scenario and success criteria.
2. `02-architecture-walkthrough.md` — how RA-01's components map onto this scenario.
3. `03-implementation-guide.md` — build steps.
4. `04-decision-points.md` — the DF-03/DF-04/DF-05 decisions made and why.
5. `05-common-pitfalls.md` — AP-02 and AP-04 as they concretely appear here.
6. `06-validation-checklist.md` — how to confirm the result actually satisfies RA-01.
7. `07-exercises.md` — extensions to attempt.
8. `08-solutions-and-discussion.md` — discussion of the exercises.
