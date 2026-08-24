# 02 — Architecture Walkthrough

```mermaid
flowchart TD
    REQ[Employee Request<br/>"reassign ticket #4471 to me"] --> ID[C-03: bind requesting employee identity]
    ID --> AGENT[Agent Reasoning Loop]
    AL["A-01: assigned level A3<br/>(see 04-decision-points.md)"] -.governs.-> AGENT
    ENV["A-02 Envelope:<br/>tools=[update_status, reassign]<br/>knowledge=[ticket metadata]<br/>authority=requester's team only"] --> PEP
    AGENT -->|proposes: reassign #4471 to requester| PEP["C-02 Policy Enforcement Point<br/>independent process"]
    PEP -->|checks: is #4471.team == requester.team?| DECIDE{Policy Check}
    DECIDE -->|yes| ACT[Ticket System Executes Reassignment]
    DECIDE -->|no| DENY[Denied + Logged]
    ACT --> TRACE[O-01 stub: action + identity logged]
    DENY --> TRACE
```

## Mapping table

| RA-03 Component | This Lab's Concrete Instance |
|---|---|
| `A-01` | The ticket-update agent is assigned autonomy level A3 (execution ready, human approval required) initially, per `04-decision-points.md`'s `DF-02` analysis — not A4, despite the organization's preference for full automation. |
| `A-02` | The Envelope explicitly lists two tools (`update_status`, `reassign`), the specific ticket metadata the agent may read to evaluate a request, and an explicit authority boundary (the requester's own team only). |
| `C-02` | A policy enforcement point, implemented as a component separate from the agent's own process, evaluates every proposed action against the Envelope's authority boundary before it reaches the ticket system. |
| `C-03` | Every request is bound to the actual requesting employee's identity at Step 1, and that identity — not a shared "ticket-bot" service account — is what the policy check and the ticket system's own audit log both see. |
| `O-01` (stub) | This lab implements minimal logging of action + identity + policy outcome, sufficient for the validation checklist; full tracing is Lab 04's scope. |

## Why A3, not A4, at launch

Per `DF-02`'s decision table, this capability has no yet-measured confidence data (`O-02` evaluation has not run against production traffic) and moderate-but-real consequence (misrouted tickets cause real workflow disruption) — `DF-02` recommends A1–A2 or A3 with strong enforcement when confidence is unmeasured, not A4. See `04-decision-points.md` for the full reasoning and the path toward reconsidering A4 later.
