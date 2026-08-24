---
title: Stop Averaging Your AI Maturity Score
status: content-prep-only
target_audience: technical and business leaders running or commissioning AI maturity assessments
last_reviewed: 2026-08-24
---

# Stop Averaging Your AI Maturity Score

Most AI maturity assessments end with a number. "You're a 3.2 out of 5." It fits neatly in a slide, it's easy to track quarter over quarter, and it is, we'd argue, actively hiding the thing you most need to know.

## What a single score can't tell you

Picture an organization with excellent knowledge grounding — every AI answer traceable to source, properly access-controlled, kept fresh — and, at the same time, an autonomous agent whose only real constraint is a sentence in a system prompt. Average those two realities across enough dimensions and you might land on a comfortable-looking 3.2. Nothing about that number tells you the second fact exists, let alone that it's the one actually likely to produce an incident.

This isn't a hypothetical construction to make a point. It's a genuinely common profile, because organizations tend to invest first in whichever domain was easiest to demo and got funded first — usually knowledge and retrieval — while autonomy and control get built more reactively, often after the capability they're supposed to govern is already in production.

## Why averaging happens anyway

It's not that assessment designers don't understand the risk of collapsing a profile into one number. It's that a single score is genuinely easier to communicate to an executive audience, easier to compare across a portfolio, easier to put in a quarterly business review. Those are real pressures, and we don't think the answer is to refuse to ever summarize — it's to summarize honestly, in a way that doesn't erase the specific thing an average erases.

## What we do instead

We score six domains independently, and when a single summary is genuinely needed, we report the *minimum* score among domains actually in scope — not the average — and name which domain it is. The minimum is what determines your actual exposure, because a weak control layer isn't offset by a strong knowledge layer any more than a house's weakest foundation corner is offset by its strongest one.

We also build in a specific override for the profile we find most often and consider most dangerous: an autonomy level that's outpaced the control mechanisms meant to enforce it. Even when that's not literally the organization's lowest score, we treat it as the priority — because an under-enforced autonomous capability is the specific precondition for the kind of incident that ends up in a post-mortem, regardless of how strong the rest of the portfolio looks.

## What this looks like in a real roadmap

Instead of "improve your score from 3.2 to 3.8," a profile-based assessment produces something like: "your Knowledge domain is strong, at Level 3. Your Control domain is at Level 0 — the only constraint on your highest-consequence agent is a prompt instruction. That gap gets closed before anything else, including before you invest further in expanding that agent's autonomy." That's a materially more useful sentence, even though it doesn't fit on a single slide as cleanly.

## The question worth asking about any assessment you're handed

Not "what's our score" — ask what would happen to that score if your weakest domain got dramatically worse while everything else stayed the same. If the answer is "not much, because it only weighs one-sixth of an average," you're looking at a number that's optimized for legibility over usefulness. Ask for the profile underneath it instead.
