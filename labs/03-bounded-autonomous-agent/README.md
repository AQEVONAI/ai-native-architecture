---
lab_id: LAB-03
name: Bounded Autonomous Agent
target_reference_architecture: RA-03
last_reviewed: 2026-08-24
---

# Lab 03 — Bounded Autonomous Agent

## Objectives

By the end of this lab, you should be able to: assign and justify an autonomy level (`A-01`, via `DF-02`); define an explicit agent Envelope (`A-02`); implement policy-bounded action enforcement independent of the agent's own reasoning (`C-02`); and propagate a carried identity through multi-step agent execution (`C-03`).

## Prerequisites

- Read `patterns/autonomy/A-01-autonomy-gradient.md`, `A-02-bounded-agent.md`, `patterns/control/C-02-policy-bounded-action.md`, and `C-03-identity-carrying-agent.md`.
- Read `reference-architectures/RA-03-bounded-autonomous-agent.md`.
- Read `assessment/worked-example.md` — this lab builds the ticket-update agent that worked example's roadmap identified as launch-blocked on Control-domain gaps.

## Target Reference Architecture

`RA-03` — Bounded Autonomous Agent, composing `A-01`, `A-02`, `C-02`, `C-03`, `O-01`.

## What You'll Build

The ticket-update agent from `assessment/worked-example.md`: an agent that can update ticket status and reassign tickets, replacing its original prompt-instruction-only constraint ("only update tickets assigned to the requesting user's team") with an enforced policy boundary, an explicit autonomy-level assignment, and identity-carrying execution.

## Lab Files

1. `01-scenario-and-objectives.md`
2. `02-architecture-walkthrough.md`
3. `03-implementation-guide.md`
4. `04-decision-points.md`
5. `05-common-pitfalls.md`
6. `06-validation-checklist.md`
7. `07-exercises.md`
8. `08-solutions-and-discussion.md`
