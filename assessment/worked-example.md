# Worked Example

A full illustrative assessment walkthrough, from questionnaire through roadmap. This is an explicitly composite, representative scenario — not a named organization — consistent with the evidence-over-assertion / illustrative-scenario labeling discipline in `framework/principles.md`.

## Scenario

A mid-size enterprise software company has one AI-native capability in production: an internal support assistant that answers employee questions using a mix of HR policy documents and IT knowledge-base articles, launched eight months ago. A second capability — an agent that can update ticket status and reassign tickets automatically — is in active development and expected to launch within the quarter.

## Questionnaire findings (abbreviated)

- **Q1/Q2 (Knowledge):** The assistant does cite source documents in its answers (Q1: evidenced, a specific example was reconstructed). However, access control is enforced only in the application layer after retrieval — the underlying vector index has no per-document classification (Q2: fails).
- **Q5 (Intelligence):** A single fixed model is hard-coded throughout the assistant's codebase; no routing abstraction exists.
- **Q8/Q9 (Autonomy):** The in-development ticket-update agent has no documented autonomy-level assignment or Envelope yet — the team has been iterating on functionality first.
- **Q11 (Control):** The ticket-update agent's only constraint on which tickets it may modify is a system-prompt instruction ("only update tickets assigned to the requesting user's team").
- **Q12 (Control):** Not yet applicable — no human authorization boundary has been designed for the ticket-update agent's actions.
- **Q14 (Operations):** For the support assistant, the assessor could not reconstruct which specific source document a sampled answer had actually drawn from — logging exists but only at the request/response level, not the retrieval-provenance level.
- **Q17 (Evolution):** No recurring review cycle exists for either capability.

## Scoring

| Domain | Score | Basis |
|---|---|---|
| Knowledge | 1 | Q1 met, but Q2's enforcement-location failure caps the score — access control gap is a real, live risk despite citation working correctly. |
| Intelligence | 1 | No routing abstraction at all; single hard-coded model (`AP-07` risk present). |
| Autonomy | Not applicable (support assistant is non-agentic) / Level 0 (ticket-update agent, once launched) | Scored separately per capability, per scoring-guide.md. |
| Control | 0 | The ticket-update agent's only constraint is a prompt instruction — textbook `AP-03` (Prompt-as-Policy), not yet in production but on a near-term launch path. |
| Operations | 1 | Basic logging exists but fails the Q14 live-reconstruction test — provenance is not actually recoverable. |
| Evolution | 0 | No review cycle exists for either capability. |

## Overall interpretation

The minimum in-scope domain score is 0 (Control and Evolution), and Control is the domain with the most urgent, concrete exposure given the ticket-update agent's near-term launch: it will reach production with `AP-03`'s exact failure mode present in the highest-consequence capability the organization has built. This is the clearest case for the roadmap prioritization override in `roadmap-template.md` — Autonomy/Control gaps take precedence over the (real, but lower-urgency) Knowledge access-control gap.

## Resulting roadmap (first three items)

### Roadmap Item: Control — 0 → 3, before ticket-update agent launch

**Gap:** Q11 — the only constraint on the ticket-update agent's actions is a prompt instruction, not an enforced policy.
**Evidence at assessment time:** System prompt text reviewed directly; no enforcement component found in the architecture.

**Recommended actions:**
- Pattern(s): `C-02` (Policy-Bounded Action), `C-03` (Identity-Carrying Agent — required for the policy to evaluate "requesting user's team" correctly)
- Decision guide(s): `DF-06` (Human Authorization vs. Policy-Bounded Execution — ticket volume likely favors `C-02` over `C-01`, but this should be confirmed against actual expected volume before launch)
- Reference architecture: `RA-03` (Bounded Autonomous Agent)

**Sequencing:** Blocks launch — this is treated as a launch-blocking gap, not a post-launch improvement, given the direct `AP-03` exposure.
**Success evidence for re-assessment:** A denied-action test case (an attempt to update a ticket outside the requesting user's team) demonstrably blocked by policy, independent of what the agent's own reasoning concluded.
**Target timeframe:** Before ticket-update agent production launch.

### Roadmap Item: Autonomy — 0 → 2, before ticket-update agent launch

**Gap:** Q8/Q9 — no documented autonomy-level assignment or Envelope for the ticket-update agent.
**Recommended actions:** Pattern `A-01` (autonomy-level assessment), `A-02` (Envelope definition). Decision guide `DF-02`.
**Sequencing:** Should be resolved alongside, and inform, the Control roadmap item above — the Envelope definition (`A-02`) is a direct input to the `C-02` policy definition.
**Success evidence:** A dated, justified autonomy-level assignment on record before launch.
**Target timeframe:** Before ticket-update agent production launch.

### Roadmap Item: Operations — 1 → 3, within the current quarter

**Gap:** Q14 — retrieval provenance is not reconstructable from current logging for the already-live support assistant.
**Recommended actions:** Pattern `O-01` (AI Execution Trace). Decision guide `DF-10` (build vs. buy — given the maturity of existing tracing tooling found in `research/sources.md`, adoption rather than custom build is likely the faster path here).
**Sequencing:** Independent of the Control/Autonomy items above; can proceed in parallel, and should be prioritized to be in place before the ticket-update agent also launches, so both capabilities share one observability backbone from the start (`RA-04`) rather than the second capability requiring its own retrofit later.
**Success evidence:** A live reconstruction (repeating the Q14 test) succeeding for a sampled production answer.
**Target timeframe:** Within the current quarter, ahead of the ticket-update agent's launch.

## What this example illustrates

Note that the Knowledge-domain gap (Q2, access-control enforcement location) — while real — was not roadmapped first, despite Knowledge scoring low too. The prioritization principle in `roadmap-template.md` correctly surfaced the Control gap as more urgent given its direct connection to a near-term, higher-consequence capability launch, illustrating why a per-domain profile with explicit prioritization logic produces a materially different (and better) roadmap than simply addressing whichever domain scored lowest in isolation.

## Revision History

- 0.1.0 (2026-08-24) — Initial worked example.
