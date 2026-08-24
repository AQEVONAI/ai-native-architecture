---
id: AP-03
name: Prompt-as-Policy
also_known_as: "Policy by Instruction"
severity: critical
last_reviewed: 2026-08-24
---

# AP-03 — Prompt-as-Policy

## Problem Summary

Encoding authorization or behavioral constraints only as natural-language prompt instructions ("only use this tool for read operations," "never discuss pricing with unauthenticated users") rather than as an enforced, machine-evaluable policy the model's own reasoning cannot bypass.

## Also Known As

Policy by Instruction; "the system prompt says not to."

## Symptoms

- Security- or compliance-relevant constraints exist only as sentences in a system prompt, with no corresponding enforcement mechanism outside the model.
- Constraint violations are discovered through user reports or incident review rather than being structurally prevented.
- "How do we know the agent won't do X" is answered with "the prompt tells it not to" rather than a description of an enforcement mechanism.

## Root Cause

Natural-language instructions are the fastest, most immediately available way to influence model behavior, and can appear to work reliably during typical use — creating false confidence that the instruction is functioning as a control, when it is in fact a request the model may or may not honor, especially under adversarial input, prompt injection, or edge-case reasoning paths.

## Why It Happens

Writing a prompt instruction takes minutes; building a genuine enforcement layer takes real engineering effort. Under time pressure, and absent an incident that reveals the gap, prompt instructions are frequently treated as "good enough" security or policy controls.

## Consequences

- Constraints can be bypassed via prompt injection, adversarial input, or simply a model reasoning path the instruction did not anticipate.
- Security and compliance review that treats prompt instructions as controls produces a false sense of assurance not backed by an actual enforcement guarantee.
- This is frequently the specific mechanism behind `AP-06` (Autonomous Privilege Creep) becoming exploitable rather than merely undesirable.

## How to Recognize It

Ask, for any stated behavioral or authorization constraint: what happens, mechanically, if the model does not follow this instruction — is there a component outside the model's own reasoning that would catch and block the violation? If the honest answer is "nothing, we're relying on the model following the prompt," this anti-pattern is present.

## A Worked (Illustrative) Example

*Illustrative scenario:* An internal support agent's system prompt instructs it to "only look up account information for the authenticated user making the request." A crafted request phrased as a hypothetical or role-play scenario leads the model to retrieve a different account's information, because the constraint existed only as a prompt instruction with no enforcement point verifying the requested account matched the authenticated identity. A `C-02` policy enforcement point evaluating every retrieval request against the actual authenticated identity — independent of what the model's reasoning concluded — would have blocked the action regardless of how the request was phrased.

## Corrective Pattern(s)

`C-02` (Policy-Bounded Action — the direct corrective pattern: express constraints as enforced, machine-evaluable policy).

## Related Anti-Patterns

`AP-01` (Agent by Default — agentic capabilities built without a bounded scope are especially exposed to this anti-pattern, since a broad action surface with only prompt-level constraint has more to go wrong), `AP-06` (Autonomous Privilege Creep — prompt-as-policy is frequently the underlying reason an apparent constraint fails to actually hold as access expands).

## Evidence / Prevalence

Well-documented in AI security research and practitioner discussion as a core limitation of relying on prompt instructions for security-relevant behavior; prompt injection and instruction-bypass techniques are an active, ongoing area of security research. This anti-pattern's severity is rated critical because the gap between apparent and actual enforcement is not visible during normal operation — it typically surfaces only via adversarial testing or incident.

## Revision History

- 0.1.0 (2026-08-24) — Initial anti-pattern card.
