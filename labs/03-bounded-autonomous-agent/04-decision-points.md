# 04 — Decision Points

## DF-01 — Should This Be Agentic?

**Applied at:** the initial decision to build this as an agent at all.

**Decision:** Yes — this task genuinely requires intermediate reasoning (interpreting the employee's natural-language request, evaluating which ticket and action it refers to) followed by a tool call whose target depends on that reasoning, satisfying `DF-01`'s test for legitimate agentic architecture. This is not `AP-01` (Agent by Default) because the step-dependency is genuine, not assumed.

## DF-02 — Choosing an Autonomy Level

**Applied at:** Step 3 of the implementation guide.

**Decision:** A3, not A4, per the justification recorded in Step 3. `DF-02`'s decision table specifically flags "confidence not yet measured" as a case that should not receive A3+ without strong enforcement, and A4 (no per-action approval) specifically requires evaluated confidence this capability does not yet have. Note: this lab's Envelope-enforced A3 still executes tool calls without human approval on each one in the technical sense described in Step 5 — this is intentional and consistent with `A-01`'s definition: A3 means "ready to execute but requires explicit approval," which in this lab's design is satisfied by the enforced policy boundary standing in for per-action review at the "is this within the requester's authority" level, while genuinely ambiguous or denied cases route to explicit human review (see `05-common-pitfalls.md` for why this distinction matters and isn't a shortcut around A3's actual approval requirement).

**Correction to the above, stated plainly:** on reflection against `A-01`'s definition, an agent that executes automatically whenever the policy check passes, with no human touch at all for permitted actions, is more accurately described as operating at **A4** (policy-bounded autonomous execution) for the "permitted" path, while denied actions escalate toward `C-01`/A3-style review. This lab intentionally implements that split-level design and documents it honestly here rather than mislabeling the whole capability as a single level — see `07-exercises.md` Exercise 2 for a structured exercise on exactly this classification question.

## DF-06 — Human Authorization vs. Policy-Bounded Execution

**Applied at:** deciding how "team boundary" violations are handled.

**Decision:** `C-02` (policy-bounded, automatic denial) for out-of-scope actions — ticket volume is likely high enough that per-instance human review of every reassignment would risk `AP-08`, and "is this ticket assigned to the requester's team" is cleanly encodable as policy, satisfying `DF-06`'s first decision gate.

## What would change this lab's decisions

Once `O-02` evaluation (Lab 04) accumulates production evidence of this agent's reliability, `DF-02` supports revisiting the A3/A4 classification with genuine evidence — see `07-exercises.md`.
