---
status: content-prep-only
target_audience: enterprise architects, CTOs, technical buyers
last_reviewed: 2026-08-24
---

# 8 Ways AI-Native Architecture Goes Wrong

We catalog what works. We also catalog what doesn't — because most of the AI incidents that make organizations gun-shy about AI adoption trace back to one of a fairly small set of recurring mistakes.

**Agent by Default.** Building an autonomous, tool-using agent because that's what everyone's building, when the task actually needed one grounded lookup and nothing more. More moving parts, more risk, more cost, for no real gain.

**RAG Everything.** Routing an exactly-answerable question (a price, a policy number) through retrieval-and-generation instead of a direct database query — introducing avoidable, unnecessary variance into what should be a deterministic answer.

**Prompt-as-Policy.** Telling the model, in the system prompt, what it's not allowed to do — and calling that a security control. It isn't. It's a request the model may or may not honor, especially when someone's actively trying to talk it out of following the rules.

**Vector Database as Knowledge Architecture.** Standing up a vector index and calling it "our knowledge base" — without access control enforced at retrieval, without a plan for keeping it current, without anything a governance team could actually review.

**Context Dumping.** Cramming everything retrievable into the model's context window instead of ranking and budgeting it. Models pay less attention to information buried in the middle of a long context — a well-documented effect that context dumping runs straight into.

**Autonomous Privilege Creep.** An agent's access growing, tool by "just one more" tool, until nobody can say with confidence what it can actually do — each addition reasonable on its own, the sum quietly dangerous.

**Single-Model Dependency.** Hard-coding one model provider throughout an application, with no fallback — turning a routine provider outage into a full incident.

**Human-in-the-Loop Theater.** A human approval step that exists on paper but, in practice, gets rubber-stamped because there's too much volume and too little time to actually review each one. The appearance of a safety control, without the substance.

## Why we publish our own failure modes

Most vendors lead with what their approach gets right. We think what an approach explicitly refuses to do — and names clearly as a mistake — is at least as informative, and a lot harder to fake. Full detail on each, including how to recognize it early, is in our [full pattern library](pattern-library-overview.md).

*[Placeholder note for whoever integrates this content: link to the public architecture repository here once its URL and public-access status are finalized — no repository URL has been confirmed as of this content's preparation, so none is included above.]*
