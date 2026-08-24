---
title: Why We Corrected Our Own Framework in Public
status: content-prep-only
target_audience: technical and business leaders evaluating AI architecture frameworks and vendors
last_reviewed: 2026-08-24
---

# Why We Corrected Our Own Framework in Public

We built an autonomy scale for AI agents — six levels, A0 through A5, running from full human decision-making to full autonomous execution. We were reasonably proud of it. And when we sat down to check our own claim that it was original, we found out it wasn't, not entirely, and we changed the label. This is the story of that correction, and why we think publishing it matters more than the correction itself.

## The claim we started with

Our Autonomy Gradient pattern originally carried a classification we call "Proposed" — meaning, in our own internal system, that we hadn't found comparable prior art and were presenting it as a genuine, AQEVON-originated hypothesis rather than an established technique. We'd drawn an analogy to the automotive industry's well-known scale for self-driving vehicle autonomy, and built out a six-level structure adapted specifically for enterprise AI agents.

## What we found when we actually looked

We run a research pass against every pattern in our catalog before publishing it, specifically to check whether comparable work already exists — not because we assume the worst about our own ideas, but because we think publishing an inflated novelty claim is a worse outcome than publishing an honest one. When we ran that check against the Autonomy Gradient, we found several existing frameworks doing something close enough that "AQEVON-original proposal" wasn't a defensible label anymore — including at least one independently published only months before our own research, using the exact same analogy to vehicle-autonomy levels we'd arrived at separately.

That's not a minor overlap. That's the same core idea, converged on independently by more than one team.

## What we did about it

We changed the classification from "Proposed" to "Synthesis" — our label for patterns that combine established ideas into a treatment specific to AI-native architecture, rather than inventing something new outright. We rewrote the pattern's evidence section to name the specific frameworks we found, updated its version number, and logged the whole correction — reasoning included — in a differentiation document that sits in the same public repository as everything else. We didn't quietly edit the file and move on. We wrote down why we were wrong.

## Why we think this is the right call, not just the honest one

Most vendor and framework content in this space leans hard on novelty. "Revolutionary," "unprecedented," "first-of-its-kind" — read enough of it and the words stop meaning anything, because they're applied indiscriminately regardless of whether the underlying claim holds up. We think that pattern is actively bad for the people trying to evaluate this stuff, because it makes genuine novelty indistinguishable from marketing.

The alternative isn't false modesty. It's actually checking, and actually saying what you find — including when what you find is inconvenient. We'd rather be the framework where two-thirds of our patterns are honestly labeled as established-or-synthesized existing practice, and trusted for it, than the framework where everything is claimed as new and none of it holds up to a determined fact-check.

## What this should tell you, if you're evaluating any framework in this space

Ask whoever's pitching you a "revolutionary" approach one question: did you actually check? Not "do you believe it's novel" — did you run the search, and can you show your work? If the answer is a shrug, that's worth knowing before you build anything real on top of the claim.
