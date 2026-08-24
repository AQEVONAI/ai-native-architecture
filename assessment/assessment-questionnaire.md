# Assessment Questionnaire

Structured questions for gathering evidence toward a maturity rating in each domain, per `maturity-model.md`. Each question requests a specific artifact or observable evidence, not a self-reported confidence level, consistent with this framework's evidence-over-assertion principle. Answer for the organization's current AI-native capability portfolio as a whole, noting where answers vary meaningfully by capability.

## Knowledge

1. For your highest-risk AI capability, can you produce the specific source(s) a recent generated answer traces back to? (Evidence: a specific traced example, not "yes we do grounding.")
2. Is retrieval access control enforced at the retrieval/fabric layer, or only checked afterward in the application? (Evidence: point to the enforcement code/config.)
3. For each knowledge source in use, is there a defined change-detection mechanism, and can you state its current staleness (time since last verified sync)?
4. If knowledge spans multiple independently governed sources, is access control preserved consistently across all of them, or does it vary by source?

## Intelligence

5. Is model selection hard-coded per capability, or handled by a routing layer? If routing exists, what inputs does it use (cost, latency, task complexity)?
6. Is there a defined, documented context budget/allocation policy, or is context assembled until a token limit is hit?
7. If any capability persists cross-session memory, can you produce its classification, ownership, and retention policy for a specific stored item?

## Autonomy

8. For each agentic capability, is there a documented, dated autonomy-level (A0–A5) assignment with a stated justification?
9. For each agentic capability at A2+, is there a documented Envelope (Purpose, Knowledge, Reasoning, Tools, Authority, Action)?
10. When an agent reaches an autonomy or confidence boundary, is there a defined handoff process, or does it fail silently / require manual investigation to notice?

## Control

11. For each capability at A3+, what specifically prevents an out-of-scope action from executing — is it a prompt instruction, or an independent enforcement component? (Evidence: describe the enforcement mechanism concretely.)
12. For each human-authorization step in place, what is its current approval rate and median time-to-decision? (Evidence: pull the actual numbers if available — this is the single most diagnostic question in this questionnaire for detecting `AP-08`.)
13. Are agent actions attributed to a specific, carried identity, or a shared service credential? (Evidence: check what identity appears in a sampled action log.)

## Operations

14. For a specific recent AI-generated output, can you reconstruct what was retrieved, what model was used, what policy was evaluated, and who/what the acting identity was? (Evidence: attempt this reconstruction live during the assessment.)
15. Does a proposed change to a model, prompt, or retrieval configuration require passing an evaluation suite before reaching production, and does a failing result actually block promotion?
16. For each external dependency (model provider, knowledge source, tool), is there a defined fallback behavior, and is degraded operation explicitly signaled to users/downstream systems?

## Evolution

17. Is there a scheduled, recurring architecture review cycle distinct from ad hoc incident response? When did it last run, and what decision did it produce?
18. Can you point to a specific instance where accumulated operational or evaluation signal led to a deliberate architectural change (an autonomy-level revision, a pattern substitution)?
19. For knowledge sources specifically, is there a recurring freshness review distinct from the automated `E-01` sync mechanism itself?

## Portfolio-level questions

20. How many distinct AI-native capabilities are currently in production, and does shared infrastructure (fabric, observability backbone) exist across them, or is each capability built independently?
21. Which domain's gaps, if any, has the organization already identified as a priority — and does that priority match what this questionnaire's answers suggest?

## Recording answers

For each question, record: the answer, the specific evidence or artifact examined (or "no evidence available" if the answer is asserted but not demonstrated), and the capability(ies) the answer applies to if it varies across the portfolio. Unevidenced answers should be scored conservatively per `scoring-guide.md`, not taken at face value.

## Revision History

- 0.1.0 (2026-08-24) — Initial questionnaire, 21 questions across six domains plus portfolio-level context.
