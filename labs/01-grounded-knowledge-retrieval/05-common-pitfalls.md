# 05 — Common Pitfalls

The anti-patterns most likely to appear in this specific scenario, and how this lab's design avoids them.

## AP-02 — RAG Everything

**How it would appear here:** Routing the help desk phone number question through the same retrieval-and-generation pipeline as unstructured questions, producing an answer that occasionally paraphrases or slightly varies the phone number instead of returning it exactly.

**How this lab avoids it:** Step 1's question-type router explicitly separates structured, exactly-answerable questions into a direct-lookup path (Step 7), bypassing generation entirely for that question type.

**Warning sign if it creeps back in:** If a new structured question type is added to the capability's scope later (e.g., "what is my manager's name") without being routed to direct lookup, this anti-pattern will silently reappear for that new question type. Revisit the router's classification set whenever new question types are added.

## AP-04 — Vector Database as Knowledge Architecture

**How it would appear here:** Building the HR and IT connectors to retrieve content without also retrieving each item's access-control metadata, then attempting to filter by role only in the application layer after retrieval — or worse, not filtering at all and relying on a prompt instruction telling the model not to share restricted content.

**How this lab avoids it:** Step 3 explicitly requires access metadata to be part of what each connector returns, and requires authorization filtering to happen before ranking/budgeting, at the fabric layer — not as an application-layer afterthought and not as a prompt instruction.

**Warning sign if it creeps back in:** If a new source is federated later without a connector that returns access metadata, that source's content will be retrievable by any employee regardless of restriction — this is exactly the access-control gap `AP-04` describes, reintroduced source by source if the connector discipline isn't maintained.

## A near-miss worth naming: E-01 without tuned cadence

Not a named anti-pattern in this framework's catalog, but a real risk in this specific scenario: using one global polling interval for both HR (infrequent changes, could tolerate a slower poll) and IT (more frequent changes, needs a faster poll) either wastes polling resources on HR or under-serves freshness for IT. `03-implementation-guide.md` Step 6 explicitly calls for per-source cadence tuning to avoid this.
