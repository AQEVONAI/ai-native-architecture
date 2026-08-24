---
id: AP-02
name: RAG Everything
also_known_as: "Retrieval as Universal Solvent"
severity: moderate
last_reviewed: 2026-08-24
---

# AP-02 — RAG Everything

## Problem Summary

Applying retrieval-augmented generation to problems that are better solved by deterministic lookup, structured database queries, or rule-based logic — because RAG has become the reflexive default answer to "how do we make the AI know about our data."

## Also Known As

Retrieval as Universal Solvent; "just RAG it."

## Symptoms

- Structured, precisely-answerable data (exact prices, exact policy numbers, exact dates) is embedded into a vector store and answered via retrieval-and-generation, rather than queried directly and returned deterministically.
- Answers to questions with a single objectively correct value show variance across repeated queries, because retrieval-and-generation introduces probabilistic behavior into what should be a deterministic lookup.
- Engineering effort goes into retrieval tuning (chunking, embedding, re-ranking) for data that a simple structured query would answer more reliably and cheaply.

## Root Cause

RAG's genuine strength — grounding AI-generated answers in unstructured source content — gets over-generalized into "the way we make AI answer questions about our data," including cases where the data is structured and does not need a generative step at all.

## Why It Happens

RAG pipelines are a well-known, widely tooled pattern that can be reused across many question types with the same infrastructure, making it operationally tempting to route everything through one retrieval pipeline rather than maintaining both a retrieval path and a structured-query path.

## Consequences

- Reduced answer reliability for exactly-answerable facts, since a generative step introduces variance a direct query would not have.
- Unnecessary latency and cost for questions a structured query could answer in a fraction of the time.
- Harder debugging: a wrong exact-value answer requires investigating retrieval and generation behavior, when a structured-query bug would have been immediately visible.

## How to Recognize It

Ask, for any RAG-answered question type: does this question have a single, structurally retrievable correct value (a field in a database, a specific record)? If so, and the current implementation still routes it through embedding-based retrieval and generation, this anti-pattern is present.

## A Worked (Illustrative) Example

*Illustrative scenario:* A team builds a RAG pipeline over a product catalog PDF export to answer "what is the current price of product X." The price is a single structured field, updated in a source database. The RAG-based answer is occasionally stale (the PDF export lags the database) and occasionally imprecise (the model paraphrases a price range instead of returning the exact figure). A direct structured query against the source database would have returned the exact, current price every time, with lower latency, and the RAG pipeline should have been reserved for genuinely unstructured questions (e.g., "what makes product X different from product Y" against product description content).

## Corrective Pattern(s)

`K-01` (Grounded Retrieval — reserved for genuinely unstructured or synthesis-requiring questions), `K-02` (Enterprise Knowledge Fabric — a properly designed fabric routes structured queries to structured sources rather than forcing everything through one retrieval pipeline).

## Related Anti-Patterns

`AP-04` (Vector Database as Knowledge Architecture — often the underlying infrastructure choice that makes this anti-pattern easy to fall into, since a vector-only architecture has no natural structured-query path to route to instead).

## Evidence / Prevalence

Widely discussed in practitioner communities as retrieval pipelines have become the default AI-data-integration reflex; the underlying principle (use the right query mechanism for the data's actual structure) is a long-established data-architecture concern predating RAG specifically. AQEVON names this as a specific, recurring instance of that general principle being overlooked in AI-native system design.

## Revision History

- 0.1.0 (2026-08-24) — Initial anti-pattern card.
