# 07 — Exercises

## Exercise 1 — Extend evaluation to the ticket agent

Build an evaluation suite for the ticket-update agent from Lab 03, covering both correctly-permitted and correctly-denied test cases. Run it, and use the results to actually complete Lab 03's Exercise 2 — does the resulting pass rate and failure analysis support moving the "policy-permitted" path to a more confidently-justified A4, per `DF-02`'s evidence-based revisiting guidance?

## Exercise 2 — Model-level degradation

Per `05-common-pitfalls.md`'s AP-07 note, this lab's `O-03` coverage stops at the knowledge-source level. Design (you do not need to fully implement) a fallback for the support assistant's underlying model becoming unavailable, referencing `I-01` and `DF-07`. What would the degradation notice say in this case, and how would it differ from the IT-wiki notice?

## Exercise 3 — E-02 in action

Using this lab's aggregated data (real or simulated), construct a scenario where the monthly review cycle should conclude something needs to change — e.g., a sustained pattern of degradation events for the IT-wiki source suggesting the connector itself needs attention, not just the fallback. Write the resulting decision record in the format `04-decision-points.md` and `E-02`'s own pattern card describe.

## Exercise 4 — Retrofit vs. build-in

This lab retrofitted observability onto Labs 01–03's capabilities after they were already built. Reflect on what would have been different if `O-01` instrumentation had been built into Lab 01/02/03 from the start, per this framework's actual stated baseline requirement (`O-01`'s "When to Use" section: "any AI-native capability, without exception"). Why do you think this framework's own labs sequenced observability last despite that stated requirement — is this a defensible pedagogical sequencing choice, or does it risk implicitly teaching the wrong lesson about when observability should actually be built?

## Exercise 5 — Second-guessing the schema

Step 1's trace schema uses capability-specific nested fields. As a third capability is added (hypothetically, beyond this framework's scenario continuity), propose how the schema should evolve, and identify the point at which capability-specific nesting becomes unwieldy enough to warrant a different schema design (e.g., a more generic key-value event model).
