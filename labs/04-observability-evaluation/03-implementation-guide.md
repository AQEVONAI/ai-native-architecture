# 03 — Implementation Guide

## Step 1 — Shared trace schema

Define one trace schema used by both capabilities, with capability-specific fields nested rather than forking the schema entirely:

```yaml
execution_id: uuid
capability: "support_assistant" | "ticket_agent"
identity: employee_id
timestamp: iso8601
support_assistant_fields:  # present only when capability == support_assistant
  retrieval_sources: [{source_id, doc_id, authorized: bool}]
  citations: [doc_id]
ticket_agent_fields:  # present only when capability == ticket_agent
  proposed_action: {tool, ticket_id, target}
  policy_outcome: "permitted" | "denied"
  policy_reason: string
result: "success" | "denied" | "error" | "degraded"
```

## Step 2 — Instrument both capabilities

Modify Lab 01/02's retrieval and citation steps, and Lab 03's enforcement step, to emit a trace record matching Step 1's schema at the end of every execution — not just on error, and not just a sample.

## Step 3 — Build the evaluation suite

For the support assistant, assemble a representative set of test questions covering: single-source HR, single-source IT, cross-source, and structured-lookup question types from Lab 01's scenario, each with an expected correct answer or expected citation set. Define a pass threshold (e.g., 95% of test cases must produce a correctly cited, correct answer).

```
eval_suite = [
  {question: "...", expected_sources: [...], expected_answer_contains: "..."},
  ...
]
```

## Step 4 — Wire the evaluation gate into promotion

Implement a promotion step for any change to retrieval configuration, prompts, or policy that runs Step 3's suite and blocks the change from taking effect in production if the pass threshold is not met — this must be a genuine block (the change cannot be deployed by any path that skips the gate), not merely a report generated after deployment.

```
def promote(change):
    result = run_eval_suite(change)
    if result.pass_rate < THRESHOLD:
        return Blocked(result)
    deploy(change)
    return Promoted(result)
```

## Step 5 — Implement O-03 for the IT-wiki dependency

Add a health check for the IT-wiki connector from Lab 01. On detected unavailability, route IT-related questions to a defined fallback response that explicitly states IT information may be incomplete, rather than either failing hard or silently answering without IT content while looking normal.

```
if not it_wiki.healthy():
    response.degradation_notice = "IT knowledge source temporarily unavailable; answer may be incomplete for IT-related questions."
    proceed_with_available_sources_only()
```

## Step 6 — Minimal E-02 review cycle

Implement a scheduled (e.g., monthly) job that aggregates: trace volume and error rate per capability, evaluation pass-rate history, and degradation event frequency and duration. Produce a short, dated decision record — even if the decision is "no change warranted this cycle," record that explicitly rather than skipping the cycle when there's nothing dramatic to report.

## Verification

Proceed to `06-validation-checklist.md`.
