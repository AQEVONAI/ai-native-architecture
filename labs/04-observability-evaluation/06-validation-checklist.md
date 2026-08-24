# 06 — Validation Checklist

## Trace reconstruction (O-01) — the roadmap-closing test

- [ ] For a sampled support-assistant answer, reconstruct identity, retrieval sources, authorization outcome, and citations entirely from the trace record — repeat the exact test `assessment-questionnaire.md` Q14 originally failed, and confirm it now passes.
- [ ] For a sampled ticket-agent action, reconstruct identity, proposed action, policy outcome, and result entirely from the trace record.

## Evaluation gate (O-02) — the genuine-block test

- [ ] Submit an intentionally failing retrieval-configuration change (e.g., one that would break citation accuracy) through the promotion pipeline. Confirm it is blocked and does not reach production.
- [ ] Submit a passing change and confirm it is promoted, so the gate is confirmed to actually let valid changes through, not just block everything.

## Degradation (O-03)

- [ ] Simulate the IT-wiki source becoming unavailable. Confirm the assistant's response to an IT-related question includes the explicit degradation notice, and confirm HR-only questions continue to work normally, unaffected.
- [ ] Confirm the degradation event is logged with start/end time.

## Evolution loop (E-02)

- [ ] Confirm the scheduled review job has run at least once and produced a recorded decision (even if "no change warranted").
- [ ] Confirm the recorded decision references actual aggregated data (trace volume, evaluation pass rate, degradation frequency) rather than being a generic template with no real numbers filled in.

## Cross-capability consistency

- [ ] Confirm both the support assistant and ticket agent write to the same trace store using the same schema (query both capability types from one interface, not two separate systems).

## Sign-off

The O-02 genuine-block test and the O-01 reconstruction test are the two highest-value checks in this lab — both directly address gaps `assessment/worked-example.md` identified as real, not hypothetical.
