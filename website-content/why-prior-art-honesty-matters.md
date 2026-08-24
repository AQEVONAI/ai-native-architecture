---
status: content-prep-only
target_audience: enterprise architects, CTOs, technical buyers
last_reviewed: 2026-08-24
---

# Why We Tell You What We Didn't Invent

AI architecture content right now has a novelty problem. Nearly everything is pitched as revolutionary, first-of-its-kind, a category of one — and most of it isn't, and everyone building this stuff for a living quietly knows it isn't. We think that's a bad way to earn trust from people whose job is to be skeptical of exactly this kind of claim.

## What we actually did

Every pattern in our library is tagged with where it actually came from: **Established**, meaning the core idea is already documented, named, and in active use elsewhere — we're not claiming to have invented model routing, or grounded retrieval, or policy-as-code for AI agents, because we didn't. **Synthesis**, meaning we're applying a genuinely established principle — least privilege, federated governance, circuit breakers — specifically to an AI-native problem in a way we didn't find already packaged elsewhere. **Proposed**, meaning we don't yet know of comparable prior art, and we're labeling it as a hypothesis, not a fact.

We went and checked. We didn't just assert these labels — we researched the field and looked for the closest existing practice to every single pattern we publish, and we recorded exactly what we found, including the specific sources.

## We even found we were wrong about one, and said so

Our Autonomy Gradient pattern was originally labeled a AQEVON-original proposal. Then we actually looked, and found several comparable graduated-autonomy frameworks already in circulation — including at least one using the exact same analogy to vehicle-autonomy levels we'd independently landed on. We corrected the label. Publicly, in the same repository, with the reasoning laid out in full.

## Why this should matter to you, not just to us

If a vendor's entire pitch rests on a claim of novelty, and that claim turns out to be inflated, what else in the pitch should you take on faith? We'd rather you trust the roughly two-thirds of our framework that's honestly established-or-synthesized practice — because it's genuinely well-tested — than trust a framework where everything is claimed as new and none of it can actually be checked.

See our [pattern library](pattern-library-overview.md) for the classifications themselves, applied pattern by pattern.
