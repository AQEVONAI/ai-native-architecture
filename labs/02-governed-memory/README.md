---
lab_id: LAB-02
name: Governed Memory
target_reference_architecture: RA-02
last_reviewed: 2026-08-24
---

# Lab 02 — Governed Memory

## Objectives

By the end of this lab, you should be able to: decide whether a capability actually needs cross-session memory (`DF-08`); implement write-time classification, ownership, and retention (`I-03`); scope memory retrieval to a carried identity (`C-03`); and route a memory-informed high-consequence action through a human authorization boundary (`C-01`).

## Prerequisites

- Read `patterns/intelligence/I-03-governed-memory.md`, `patterns/control/C-01-human-authorization-boundary.md`, and `patterns/control/C-03-identity-carrying-agent.md`.
- Read `reference-architectures/RA-02-governed-ai-memory-personalization.md`.
- This lab extends Lab 01's support assistant — read Lab 01 first, or at minimum its `01-scenario-and-objectives.md`.

## Target Reference Architecture

`RA-02` — Governed AI Memory & Personalization, composing `I-03`, `C-01`, `C-03`, `K-02`.

## What You'll Build

An extension to Lab 01's support assistant that remembers an employee's stated preferences (e.g., "I prefer detailed answers with policy citations") and relevant prior context (e.g., a previously reported IT issue) across sessions — governed by classification, ownership, and retention from the moment each memory is written, and scoped strictly to the employee who produced it.

## Lab Files

1. `01-scenario-and-objectives.md`
2. `02-architecture-walkthrough.md`
3. `03-implementation-guide.md`
4. `04-decision-points.md`
5. `05-common-pitfalls.md`
6. `06-validation-checklist.md`
7. `07-exercises.md`
8. `08-solutions-and-discussion.md`
