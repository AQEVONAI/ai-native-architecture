# 03 — Implementation Guide

## Step 1 — Identity binding

Bind every incoming request to the requesting employee's authenticated identity before it reaches the agent's reasoning loop, consistent with `C-03`. This identity must be carried through every subsequent step — do not let the agent's tool calls execute under a separate, broader service credential.

```
request -> identity = authenticate(request) -> agent_context.identity = identity
```

## Step 2 — Envelope definition

Write down the Envelope explicitly, as a reviewable artifact, before implementation:

```yaml
purpose: "Update ticket status and reassign tickets within the requester's own team."
knowledge: ["ticket metadata: id, status, assigned_team, assigned_user"]
reasoning: "May recommend a status change or reassignment based on ticket content and requester's stated intent."
tools: ["update_status(ticket_id, new_status)", "reassign(ticket_id, new_assignee)"]
authority: "Requester's own team only. Cannot act on tickets outside requester.team."
action: "Executes only after C-02 policy check passes."
```

## Step 3 — Autonomy-level assignment

Record the `A-01` assignment as a dated, justified artifact (not just a config value):

```
autonomy_level: A3
justification: "No production evaluation data yet (O-02 not yet run against
  this capability); moderate consequence (misrouted tickets disrupt team
  workflow); reversible but with real cost. Per DF-02, A3 with strong
  enforcement, not A4, is warranted until evaluation data accumulates."
assigned_by: [role/team]
date: 2026-08-24
```

## Step 4 — Policy enforcement point

Implement the policy check as a component the agent's reasoning process calls but cannot bypass or modify — critically, this should run in a separate process/service, not as a function the agent's own code path could skip:

```
def enforce(proposed_action, identity, envelope):
    ticket = fetch_ticket(proposed_action.ticket_id)
    if ticket.assigned_team != identity.team:
        return Denied(reason="ticket outside requester's team")
    if proposed_action.tool not in envelope.tools:
        return Denied(reason="tool not in envelope")
    return Permitted()
```

## Step 5 — Wire enforcement before execution

Ensure the agent's tool-calling mechanism routes every call through Step 4's enforcement before the actual ticket-system API is invoked — not after, and not as an optional check the agent's reasoning decides whether to request.

```
agent_proposes(action) -> enforce(action, identity, envelope) -> {permitted: execute() | denied: log_and_respond()}
```

## Step 6 — Minimal action + identity logging

Log every enforcement decision (permitted or denied) along with the acting identity and the specific policy clause evaluated — this is a stub toward full `O-01` tracing (Lab 04), sufficient for this lab's validation.

## Verification

Proceed to `06-validation-checklist.md`.
