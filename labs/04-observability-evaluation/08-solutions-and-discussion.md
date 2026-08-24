# 08 — Solutions and Discussion

## Exercise 1 — Extend evaluation to the ticket agent

A reasonable suite includes: permitted-action test cases (requester acting within their own team, expected outcome: execute), denied-action test cases (requester attempting cross-team action, expected outcome: deny), and the adversarial-phrasing cases from Lab 03's `06-validation-checklist.md`. If the resulting pass rate is high (e.g., >98%) with failures concentrated in denial-handling UX rather than actual policy-boundary violations (which should be at 0% failure, since enforcement is independent of the agent's reasoning and should not fail probabilistically at all), this supports treating the "policy-permitted, enforced" path as legitimately at A4 confidence — reinforcing the split-level resolution proposed in Lab 03 Exercise 2's solution, now backed by actual evaluation evidence rather than architectural argument alone.

## Exercise 2 — Model-level degradation

A model-level fallback would route to an alternate model (`I-01`) rather than degrading to reduced knowledge coverage — the degradation notice here should communicate something different from the IT-wiki case: not "information may be incomplete" (a knowledge-coverage statement) but something like "responses may be slower or less detailed than usual" (a capability-quality statement), since a fallback model is likely to differ in capability rather than in knowledge access. This distinction matters: conflating the two notice types would give employees inaccurate expectations about what's actually degraded.

## Exercise 3 — E-02 in action

A defensible decision record: "Aggregated data shows IT-wiki degradation events occurring 4 times in the past 30 days, averaging 45 minutes each, compared to 0 events for HR sources in the same period. Decision: investigate IT-wiki connector reliability directly (a `K-03` federation connector issue) rather than continuing to rely solely on `O-03`'s fallback — the fallback is functioning as designed, but its recurring use is itself a signal the underlying dependency needs attention, not just tolerance." This illustrates `E-02`'s core value: the fallback alone (Lab 04's Step 5) treats each incident individually; the review cycle is what notices the pattern across incidents and escalates it to an actual fix.

## Exercise 4 — Retrofit vs. build-in

This is a fair tension to name directly: this framework's own labs sequence observability last (Lab 04) despite `O-01`'s stated baseline requirement that every capability should have it from the start. The pedagogical justification is that teaching each domain's concerns in relative isolation (Knowledge, then Memory, then Autonomy/Control, then Operations) makes each lab's specific additions clearer — but this sequencing does risk implicitly modeling "build first, observe later" as an acceptable practice, which contradicts the framework's own stated position. A more faithful-to-the-framework lab sequence would build a minimal `O-01` trace stub starting in Lab 01 (as Lab 03 in fact did, calling it a "stub" explicitly) and treat Lab 04 as "graduating" that stub to full maturity, rather than introducing tracing from nothing at Lab 04 — which is in fact what Lab 03's design already partially did. This is a legitimate critique of this lab sequence's own pedagogy, surfaced honestly rather than glossed over.

## Exercise 5 — Second-guessing the schema

Capability-specific nesting remains manageable for roughly 3-5 capability types with genuinely distinct field sets; beyond that, the growing number of largely-empty nested-field blocks per record (since only one capability's fields are populated per record) becomes wasteful and harder to query generically. The natural evolution point is toward a generic `event_type` + `payload` (schema-less or loosely-typed) model once a third or fourth distinct capability type is added, trading some type safety for schema flexibility — a real trade-off, not a strict improvement, and one that should be revisited with the same evidence-based discipline `E-02` applies to every other architectural decision in this framework, not decided reflexively.
