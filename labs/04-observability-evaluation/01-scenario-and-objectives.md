# 01 — Scenario and Objectives

## Scenario

`assessment/worked-example.md`'s roadmap identified an Operations-domain gap for the support assistant: the assessor could not reconstruct which specific source document a sampled answer had drawn from, because logging existed only at the request/response level. This lab closes that gap, and extends the same observability backbone to the ticket-update agent from Lab 03, so both capabilities share one instrumentation layer rather than each building its own.

## Why Shared Infrastructure, Not Per-Capability Logging

Building separate tracing for each capability would duplicate effort and, more importantly, prevent the kind of cross-capability signal aggregation `E-02` depends on — a recurring theme in `reference-architectures/RA-04.md` and `RA-05.md`. This lab treats observability as infrastructure built once and consumed by every capability, consistent with `RA-05`'s deployment guidance to build the Operations domain early as shared infrastructure.

## Success Criteria

- For any sampled support-assistant answer, the full execution trace reconstructs: identity, sources retrieved, policy/access decisions applied, and the final answer with citations — satisfying the exact test `assessment-questionnaire.md` Q14 failed on originally.
- For any sampled ticket-agent action, the trace reconstructs: identity, proposed action, policy evaluation outcome, and execution result.
- A proposed change to the support assistant's retrieval configuration is blocked from promotion if it fails a defined evaluation suite — tested with an actual failing change, not just a passing one.
- A simulated IT-wiki source outage (from Lab 01) triggers a defined, explicitly signaled degradation rather than a silent failure or an unsignaled fallback.
- A minimal review cycle runs on a defined schedule and produces at least one recorded decision from aggregated trace/evaluation signal.

## What This Lab Does Not Cover

Full production-scale tooling selection (a `DF-10` build-vs-buy decision) is discussed but not executed — this lab implements the minimal schema and enforcement logic needed to satisfy `O-01`/`O-02`/`O-03`/`E-02`'s requirements, vendor-neutral, as a reference implementation rather than a production deployment guide.
