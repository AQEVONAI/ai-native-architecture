# 06 — Validation Checklist

## Write-time governance (I-03)

- [ ] For 5 sampled stored memory items, each has a recorded owner, classification, retention policy, and creation timestamp — confirmed by inspecting the actual stored records, not the code that should produce them.
- [ ] No memory item exists in the store without all four fields populated (test by attempting to write an incomplete item and confirming it is rejected).

## Identity scoping (C-03)

- [ ] Log in as Employee A, generate a memory item (a stated preference). Log in as Employee B and confirm Employee A's memory is not retrieved or referenced in any way during Employee B's session. This is the single most important test in this lab.

## Retention and deletion

- [ ] A `reported_issue` memory item created before the retention window's start is confirmed purged by the scheduled retention job (test with an artificially backdated item).
- [ ] A deletion request from an employee results in all of that employee's memory items being removed within the defined SLA, and the deletion event itself is logged.

## Authorization boundary (C-01)

- [ ] Trigger the high-consequence recommendation path with test data. Confirm the assistant presents a recommendation requiring explicit confirmation, and confirm no downstream action (e.g., ticket creation) occurs without that confirmation.
- [ ] Confirm the recommendation, once made, is not silently auto-approved after a timeout or any other implicit mechanism.

## Relevance filtering

- [ ] For a session where the employee has multiple stored memory items but only one is relevant to the current question, confirm only the relevant item materially influences the response (not all items dumped into context regardless of relevance).

## Sign-off

All items must be verified against the running implementation before this lab is considered complete.
