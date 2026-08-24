# 01 — Scenario and Objectives

## Scenario

The same organization from `assessment/worked-example.md` is building an agent that can update IT support ticket status and reassign tickets between team members, reducing manual triage overhead. As found in that assessment, the initial implementation constrained the agent's behavior with a single system-prompt instruction: "only update tickets assigned to the requesting user's team." This lab rebuilds the agent to close that gap before launch.

## Why the Original Design Fails

The prompt instruction is not an enforcement mechanism — it is a request the model may or may not honor, especially for edge-case phrasings or adversarial input (see `AP-03`, Prompt-as-Policy). Nothing in the original design would actually prevent the agent from updating a ticket outside the requesting user's team if the model's reasoning concluded, for any reason, that doing so was appropriate.

## Success Criteria

- The agent has a documented, dated autonomy-level assignment (`A-01`) with explicit justification.
- The agent has a documented Envelope (`A-02`): specific tools (ticket status update, ticket reassignment), specific knowledge access (ticket metadata needed to evaluate a request), explicit authority boundaries, and explicit action scope.
- Every proposed ticket action is evaluated against an enforced policy (`C-02`) by a component independent of the agent's own reasoning — verified by an actual denial test, not just code review.
- Every action is attributed to a specific, carried identity (`C-03`) — the requesting employee, not a shared service credential.
- A test case attempting to update a ticket outside the requesting employee's team is reliably blocked, regardless of how the request is phrased.

## What This Lab Does Not Cover

Full execution tracing and evaluation gating (Lab 04) are referenced but not built out in depth here — this lab focuses on the Autonomy and Control domains specifically, per `RA-03`'s scope.
