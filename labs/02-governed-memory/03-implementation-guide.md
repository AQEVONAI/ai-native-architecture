# 03 — Implementation Guide

## Step 1 — Identity binding

Ensure every interaction with the assistant is bound to the employee's authenticated identity (`C-03`), consistent with however identity is already established for the Lab 01 capability (e.g., SSO session). Do not introduce a separate, weaker identity mechanism for memory specifically.

```
interaction -> require(authenticated_employee_identity) -> proceed
```

## Step 2 — Candidate memory extraction

After each interaction, run a lightweight extraction step that identifies candidate memory items: explicit statements matching a "preference" pattern (e.g., "please keep answers short") and issue-report content matching a "reported issue" pattern (e.g., "my laptop won't connect to wifi"). Keep extraction conservative — under-extraction is a minor UX cost; over-extraction creates unnecessary governance burden and noisy memory.

## Step 3 — Classification and write-time governance

For each candidate item, assign: owner (the employee identity from Step 1), classification (`preference` or `reported_issue`), and retention policy (per classification, per `02-architecture-walkthrough.md`'s table). Persist only after this assignment — never persist first and classify later.

```
memory_item = {
  owner: employee_identity,
  classification: "preference" | "reported_issue",
  content: extracted_content,
  retention_policy: lookup(classification),
  created_at: timestamp,
  source_interaction_id: interaction_id
}
```

## Step 4 — Scoped retrieval

At the start of a new session, retrieve memory items where `owner == requesting_employee_identity` only. Do not implement retrieval that could, even accidentally, return another employee's memory — test this explicitly (see `06-validation-checklist.md`).

## Step 5 — Authorization boundary for high-consequence recommendations

When retrieved `reported_issue` memory would inform a recommendation with real consequence (expedited equipment replacement), generate the recommendation but require explicit employee confirmation before any downstream action (e.g., before actually creating an expedited ticket) — implement this as a genuine pause requiring input, not a notification the employee can passively ignore while the action proceeds anyway.

## Step 6 — Deletion handling

Implement an employee-facing deletion request path that removes all memory items owned by the requesting employee within a defined SLA (e.g., 30 days, or immediately if technically feasible). Log the deletion request and its fulfillment for audit purposes — the deletion event itself should be recorded even though the deleted content is gone.

## Step 7 — Retention enforcement

Implement a scheduled job that purges memory items past their retention window, per classification. Confirm this runs independently of any specific user interaction — retention enforcement should not depend on the employee ever returning to trigger cleanup.

## Verification

Proceed to `06-validation-checklist.md`.
