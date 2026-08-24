---
title: The Six Domains Every AI-Native Architecture Needs
status: content-prep-only
target_audience: technical and business leaders scoping enterprise AI architecture work
last_reviewed: 2026-08-24
---

# The Six Domains Every AI-Native Architecture Needs

Ask five different teams what "AI architecture" means and you'll get five different scopes — for one team it's a retrieval pipeline, for another it's agent orchestration, for a third it's model selection and cost management. All of them are right, and all of them are incomplete, because "AI architecture" isn't one concern. It's at least six, and treating them as one undifferentiated blob is a big part of why so many AI initiatives end up with strong capability in one area and dangerous gaps in another nobody was watching.

## Knowledge: is it actually true, and is it allowed to be shown to you

The first domain asks whether what an AI system says is grounded in something real, current, and access-controlled — not asserted from the model's own memory, not sourced from a document that went stale eight months ago, not surfaced to someone who shouldn't be able to see it. This is where most organizations start, and for good reason: it's the most visible failure mode when it's missing, and the most immediately valuable to get right.

## Intelligence: is the right reasoning happening, on the right information

The second domain covers which model handles a given request, what information that model actually sees, and what it remembers across interactions. It's less visible than Knowledge because it's mostly an efficiency and quality concern rather than a dramatic failure mode — a poorly budgeted context window doesn't crash, it just quietly produces worse answers than the same system would with better-curated input.

## Autonomy: how much is it allowed to do on its own

The third domain asks how independently an AI capability is allowed to act — and, critically, whether that independence was assigned deliberately or just accumulated by default. This is where things start to get genuinely risky if skipped, because unlike a knowledge gap (which produces a wrong answer) an autonomy gap produces a wrong *action*.

## Control: what actually stops it if it tries to do the wrong thing

The fourth domain is the enforcement layer underneath Autonomy — the mechanisms that make a given level of independence actually defensible rather than merely declared. A system prompt telling an agent what not to do is not a control. An enforcement point that evaluates every proposed action against policy, independent of the model's own reasoning, is. This distinction is not academic; see our companion piece on autonomy theater for what happens when it's skipped.

## Operations: can you see what happened, and catch a bad change before it ships

The fifth domain is the observability and evaluation backbone — full execution tracing so you can reconstruct what a system actually did, and evaluation gates so an unproven change can't reach production and quietly degrade quality. Every other domain's failures are far harder to detect, diagnose, and fix without this one in place.

## Evolution: is it getting better, on purpose

The sixth and final domain closes the loop: turning the signal the Operations domain produces into deliberate architectural change, on a recurring cadence, rather than letting the system drift through a thousand individually reasonable point fixes until nobody can explain why anything is configured the way it is.

## Why the six-way split matters more than any single domain

The organizations we've seen struggle most aren't the ones weak across the board — they're the ones strong in one or two domains and quietly, invisibly weak in the others, usually because whichever domain got attention first was the one that was easiest to demo. A retrieval system with excellent grounding and zero enforced autonomy boundaries isn't a partial success. It's a specific, predictable kind of exposure, and it's one a single collapsed "how mature is our AI" score would likely never surface.

Six domains isn't an arbitrary number for its own sake. It's the minimum split that keeps these very different failure modes from hiding behind each other.
