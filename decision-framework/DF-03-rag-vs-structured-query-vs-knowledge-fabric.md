---
id: DF-03
name: RAG vs. Structured Query vs. Knowledge Fabric
decision: Which retrieval mechanism — direct structured query, single-source grounded retrieval, or the full Enterprise Knowledge Fabric — fits a given question type.
related_patterns: [K-01, K-02, K-03]
last_reviewed: 2026-08-24
---

# DF-03 — RAG vs. Structured Query vs. Knowledge Fabric

## The Decision

For a given question type an AI capability needs to answer, choose the appropriate retrieval mechanism: a direct structured query against a database or API, single-source grounded retrieval (`K-01`), or a full governed, federated Enterprise Knowledge Fabric (`K-02`/`K-03`).

## Why This Is Hard

Retrieval-augmented generation has become the reflexive default answer to "how do we make AI know about our data" (see `AP-02`, RAG Everything), which obscures that many questions are better and more reliably answered by a direct structured query with no generative step at all, while others genuinely require the governance and federation apparatus of a full knowledge fabric. The three options have real cost and reliability differences that are easy to overlook when one pipeline (typically RAG) is already built and available.

## Decision Inputs

- Does the question have a single, structurally retrievable correct value (a database field, a specific record)?
- Does the question require synthesizing information from unstructured content (documents, policies, free-text descriptions)?
- Does answering the question require drawing on more than one independently governed source?
- How volatile is the underlying data, and does the current pipeline have a defined freshness mechanism (`E-01`) for it?

## Decision Tool

```
Is the answer a single, exactly-retrievable structured value
(a database field, an API response)?
│
├── YES → Direct structured query. No generative/retrieval step
│         needed. (Avoids AP-02, RAG Everything.)
│
└── NO → Does answering require synthesizing unstructured content
          from a SINGLE governed source?
          │
          ├── YES → Single-source grounded retrieval (K-01) is
          │         sufficient. Building a full K-02 fabric here
          │         is likely premature investment.
          │
          └── NO (requires reconciling MULTIPLE independently
              governed sources) → Enterprise Knowledge Fabric
              (K-02) with Knowledge Federation (K-03). See DF-04
              and DF-05 for whether and how to build it.
```

## Recommendation Guidance

Route by question type, not by defaulting the whole capability to one retrieval mechanism — most real capabilities need a mix: structured queries for exact facts, grounded retrieval for unstructured synthesis, and federation only where the organization's knowledge is genuinely spread across independently governed sources. Building the full fabric before confirming the question mix actually requires it is a common form of premature architecture investment.

## Common Mistakes

- Embedding structured data into a vector store and answering it via retrieval-and-generation, introducing avoidable variance into what should be a deterministic answer (`AP-02`).
- Building single-source `K-01` retrieval when the actual question set requires reconciling multiple sources, producing incomplete answers that only surface the one indexed source.
- Jumping straight to a full `K-02`/`K-03` fabric for an initial capability with genuinely simple, single-source retrieval needs — see `DF-04`.

## Related Patterns

`K-01` (single-source grounded retrieval), `K-02` (the governed fabric layer), `K-03` (federation across sources), `AP-02` (the anti-pattern this guide directly prevents).

## Revisit Triggers

A capability's question mix shifting over time (more cross-source questions emerging than originally anticipated), or evaluation data (`O-02`) showing retrieval-and-generation answers for exact-value questions underperforming a direct query equivalent.

## Revision History

- 0.1.0 (2026-08-24) — Initial decision guide.
