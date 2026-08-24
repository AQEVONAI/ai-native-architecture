---
id: AP-05
name: Context Dumping
also_known_as: "Fill the Window"
severity: moderate
last_reviewed: 2026-08-24
---

# AP-05 — Context Dumping

## Problem Summary

Appending as much retrieved content, conversation history, and instruction text as fits into a model's context window, in whatever order it happens to be assembled, instead of deliberately curating and ranking what enters context.

## Also Known As

Fill the Window; "just retrieve more chunks."

## Symptoms

- Retrieval returns a large, unranked set of passages, all appended to context regardless of relevance strength.
- Conversation history is included in full up to a token limit, with no relevance- or recency-aware pruning.
- Answer quality degrades or becomes inconsistent as context length grows, particularly for information positioned in the middle of a long context.

## Root Cause

Increasing retrieval count or context inclusion is often the first, easiest lever engineers reach for when an answer seems to be missing information — "the answer's wrong, let's retrieve more" — without addressing whether the right information was ranked and positioned effectively within the context that was already available.

## Why It Happens

Larger context windows in modern models make it technically possible to include much more content than before, which can be mistaken for a reason to stop curating what's included — even though model attention to buried information does not scale as cleanly as raw window size does.

## Consequences

- Diluted model attention: relevant information present in context but buried among lower-relevance content is used less reliably than the same information would be if prioritized and well-positioned.
- Increased cost: every included token has a direct cost, and unranked over-inclusion inflates cost without a corresponding quality benefit.
- Harder debugging: a wrong answer with 40 unranked retrieved passages in context is much harder to diagnose than one with 5 deliberately selected, ranked passages.

## How to Recognize It

Ask: is there a defined ranking and token-budget policy governing what enters this capability's context, or does context assembly simply continue until a token limit is hit? If the latter, this anti-pattern is present.

## A Worked (Illustrative) Example

*Illustrative scenario:* A support assistant's retrieval step returns the top 25 similarity-matched passages for every query and appends all of them to context, alongside full unpruned conversation history. For a specific question with a clear, high-relevance answer present in the second-ranked passage, the assistant's answer is occasionally incomplete or references a lower-relevance passage instead — a known effect of information placement within long, unranked context. Introducing explicit `I-02` context budgeting — ranking passages by relevance, allocating a fixed budget per category, and positioning the highest-relevance content deliberately — resolves the inconsistency without requiring any change to the underlying retrieval or model.

## Corrective Pattern(s)

`I-02` (Context Budgeting — the direct corrective pattern), `K-01` (Grounded Retrieval — pairs with ranked, budgeted inclusion rather than unranked dumping), `I-03` (Governed Memory — the equivalent discipline applied to persisted conversational context specifically).

## Related Anti-Patterns

None directly overlapping, though `AP-02` (RAG Everything) can compound this anti-pattern when retrieval volume is increased as a fix for answer quality issues that were actually a ranking/budgeting problem.

## Evidence / Prevalence

The underlying phenomenon (positional attention effects in long context, "lost in the middle") is documented in model-evaluation research; the practitioner tendency to respond to quality issues by increasing retrieval/context volume rather than curating it is widely discussed informally in applied LLM engineering practice.

## Revision History

- 0.1.0 (2026-08-24) — Initial anti-pattern card.
