---
status: content-prep-only
target_audience: enterprise architects, CTOs, technical buyers
last_reviewed: 2026-08-24
---

# The Pattern Library: 17 Ways to Get AI-Native Architecture Right

Principles are useful, but architects build with patterns — specific, reusable solutions to recurring problems. Our catalog has 17, organized across the six domains of AI-native architecture, each with the same structure: the problem it solves, the forces in tension, the solution, and — critically — when *not* to use it.

## Knowledge

**Grounded Retrieval** ensures every AI-generated claim traces to a specific source. **Enterprise Knowledge Fabric** provides the governed layer that makes that grounding trustworthy at scale. **Knowledge Federation** lets that fabric span multiple independently owned sources without forcing a costly, risky migration.

## Intelligence

**Model Routing** sends each request to the model actually suited to it — by cost, latency, and complexity. **Context Budgeting** deliberately ranks and allocates what a model actually sees, instead of stuffing the context window until it's full. **Governed Memory** lets an AI capability remember things across sessions without becoming an ungoverned, undeleteable liability.

## Autonomy

**Autonomy Gradient** assigns every capability an explicit, justified level of independence. **Bounded Agent** scopes exactly what an agent can access and do, enforced — not just instructed. **Agent Handoff** ensures a task moving between an agent and a human, or between two agents, carries full context and accountability with it.

## Control

**Human Authorization Boundary** defines exactly where a human needs to approve an action before it happens — and makes sure that approval is a real check, not a rubber stamp. **Policy-Bounded Action** enforces what an AI capability may do with machine-evaluable policy, not a prompt instruction a determined adversary can talk around. **Identity-Carrying Agent** makes every action attributable to a specific, accountable identity, not a shared, anonymous credential.

## Operations

**AI Execution Trace** captures a complete, queryable record of what happened for every single execution — the foundation everything else in this list depends on being able to answer "why did it do that." **AI Evaluation Gate** stops an unproven change from reaching production. **Graceful AI Degradation** defines what happens, honestly and visibly, when a dependency fails.

## Evolution

**Knowledge Evolution Loop** keeps the Fabric's knowledge from silently going stale. **AI Architecture Evolution Loop** turns everything the other 16 patterns observe into deliberate, evidence-based architectural change over time.

## We're honest about what's genuinely new here

Most of these patterns synthesize established engineering principles — least privilege, policy-as-code, circuit breakers — applied specifically to AI-native concerns, not invented from nothing. A few are genuine open proposals we label as exactly that. See [why prior-art honesty matters to us](why-prior-art-honesty-matters.md) for why we think that distinction is worth making loudly rather than quietly.
