# 07 — Exercises

## Exercise 1 — Add a bulk-reassignment tool

A team lead wants the agent to support reassigning multiple tickets at once ("move all of Alex's open tickets to Sam"). Update the Envelope, the policy enforcement logic, and the autonomy-level justification for this new capability. Does bulk action change the risk profile enough to warrant a different autonomy level than the single-ticket case?

## Exercise 2 — Resolve the A3/A4 classification honestly

`04-decision-points.md` notes the lab's actual implementation is more accurately a split-level design (A4-like automatic execution for policy-permitted actions, A3-like escalation for denied ones) rather than a clean single A3 rating. Propose a way to record this in the autonomy-level justification artifact so it's honestly represented rather than rounded to a single label — should this framework's `A-01` pattern support recording a split-level assignment, or should this scenario instead be modeled as two separate action types with two separate autonomy levels?

## Exercise 3 — Cross-team ticket edge case

A legitimate cross-team scenario exists: a manager who oversees two teams should be able to reassign tickets across both. The current policy (`ticket.assigned_team == identity.team`) would incorrectly deny this. Redesign the Envelope's authority definition and the enforcement logic to handle this without simply removing the team-boundary check (which would reopen the original vulnerability for everyone else).

## Exercise 4 — Adversarial phrasing test suite

Design 5 additional adversarial phrasings beyond the one in `06-validation-checklist.md`, intended to probe whether the agent's reasoning could be talked into proposing an out-of-scope action (even though enforcement should deny it regardless). Why is it still valuable to test these, given that enforcement is supposed to be independent of the agent's reasoning?
