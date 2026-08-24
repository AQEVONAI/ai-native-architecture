# 03 — Implementation Guide

This guide is scoped to what's genuinely new or extended, per `02-architecture-walkthrough.md`'s audit table — it does not repeat Labs 01–04's full implementation detail for infrastructure being reused as-is.

## Step 1 — New federated source

Build a connector for the ticket system's own data (ticket counts, assignment, status by team member), following the same connector contract established in Lab 01 Step 2: return content plus access metadata. Access metadata here is manager-scoped: a manager's identity authorizes visibility only into their own team's ticket data.

```
connector(ticket_system) -> { content, access_metadata: {authorized_manager_teams} }
```

## Step 2 — Register the new source with the existing fabric

Add this connector to the same `K-03` federation layer used by Labs 01–02, rather than building a separate retrieval path. If the fabric's authorization logic was built generically in Lab 01 (per that lab's Exercise 1 discussion), this step should require no changes to the fabric's core authorization code — only a new connector registration.

## Step 3 — New Envelope and autonomy assignment

Write a new, distinct Envelope and autonomy-level justification — do not reuse Lab 03's ticket-agent Envelope, since this capability's tools, authority, and action scope are genuinely different (read/analyze ticket data and suggest, versus execute a reassignment directly):

```yaml
purpose: "Analyze team ticket workload and suggest (not execute) rebalancing."
knowledge: ["ticket data scoped to manager's own team"]
tools: ["read_team_tickets(manager_id)"]  # note: NO write/execute tool
authority: "Read-only for manager's own team. No execution authority."
action: "Surfaces a suggestion only. Any actual reassignment requires the
  manager to separately use the Lab 03 ticket agent's own C-01/C-02 path."
autonomy_level: A2
justification: "Preparation only, no proposed decision asserted as correct,
  no execution capability at all — the lowest-risk classification available,
  chosen deliberately since this is a new capability with no evaluation
  history yet, consistent with DF-02's guidance to start at the lowest
  level that still delivers value."
```

## Step 4 — Extend, not duplicate, the trace schema

Add a third `capability` value to Lab 04's shared trace schema (`"team_workload_assistant"`) with its own nested fields, following the same pattern established for the first two capabilities — do not stand up a separate trace store.

## Step 5 — Extend the evaluation suite

Add test cases for the new capability's question types to the same evaluation pipeline from Lab 04, rather than building a separate evaluation harness.

## Step 6 — Confirm E-02 aggregation picks up the new capability automatically

If Lab 04's aggregation job was built generically (querying "all capabilities" rather than hard-coding the two existing ones), this step requires no code change — only confirm it via the next scheduled review cycle. If it requires a code change, this is itself a finding worth recording (see `05-common-pitfalls.md`).

## Verification

Proceed to `06-validation-checklist.md`.
