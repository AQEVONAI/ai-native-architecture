# 04 — Decision Points

The specific decision-framework guides applied in this lab, and the choice made for this scenario.

## DF-03 — RAG vs. Structured Query vs. Knowledge Fabric

**Applied at:** the question-type router (Step 1 of the implementation guide).

**Decision:** The help desk phone number question is a single, structurally retrievable value — routed to direct lookup, not retrieval. All other question types require either single-source or cross-source unstructured synthesis — routed to grounded retrieval / the fabric. This is `DF-03`'s decision tree applied directly: exactly-answerable structured questions bypass the generative path entirely.

## DF-04 — When to Build an Enterprise Knowledge Fabric

**Applied at:** the initial architecture decision, before any implementation.

**Decision:** A full `K-02` fabric was judged warranted immediately, rather than starting from single-source `K-01` retrieval, because the scenario's own requirements (cross-source questions spanning HR and IT) make single-source retrieval insufficient from day one — this is not the more common incremental path `DF-04` describes (start narrow, add federation once multiple capabilities emerge), but a case where the first capability's own requirements already justify federation. `DF-04`'s guidance to avoid premature fabric investment does not apply when the first capability's own question set already spans multiple sources — the fabric is not being built ahead of need here, it is being built to meet a need that exists at launch.

## DF-05 — Centralize or Federate Knowledge Sources

**Applied at:** deciding how to structure the connectors in Step 2.

**Decision:** Federate. Both HR and IT source systems are actively maintained systems of record owned by different teams, favoring federation per `DF-05`'s decision matrix. Centralizing either would require either duplicating each team's maintenance workflow into a new store or accepting a synchronization lag this scenario's freshness requirements don't tolerate well (PTO policy changes should be reflected promptly).

## What would change this lab's decisions

If the organization later determined the IT wiki was being retired in favor of a new, more portable format, that would be a trigger (per `DF-05`'s revisit triggers) to reconsider centralizing IT content specifically — while HR content, still actively maintained in its existing system, would likely remain federated.
