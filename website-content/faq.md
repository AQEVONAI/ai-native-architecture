---
status: content-prep-only
target_audience: enterprise architects, CTOs, technical buyers
last_reviewed: 2026-08-24
---

# Frequently Asked Questions

**Is this a product?**
No. This is an architecture framework and pattern language — a way of thinking about and structuring AI-native systems, vendor-neutral by design. It informs how AQEVON approaches client engagements; it isn't something you install.

**Do I need to adopt all 17 patterns at once?**
No, and we'd actively discourage it. Start with whichever reference architecture matches your first real capability's actual need — our [reference architecture overview](reference-architectures-overview.md) explains how to choose. The full composite is something organizations grow into as their AI portfolio grows, not a day-one requirement.

**How is this different from [NIST AI RMF / ISO frameworks / other AI governance frameworks]?**
Those are risk-management and governance frameworks — they tell you what outcomes to manage for. Ours is an architecture pattern language — it tells you specifically how to build systems that satisfy those outcomes, at the level of concrete design decisions and enforced mechanisms. They're complementary, not competing.

**Are you claiming to have invented all of this?**
No — see [why prior-art honesty matters to us](why-prior-art-honesty-matters.md). Most of the individual techniques are established practice elsewhere; our contribution is largely in how they're organized, connected, and made specific to AI-native concerns.

**What does "vendor-neutral" actually mean here?**
The patterns describe architectural roles and requirements — an enforcement point, a routing layer, a trace store — not specific products. You can implement any of them with a range of existing tools, commercial or open-source, or build custom where needed. We don't require a specific vendor's platform.

**Is this only for organizations already building AI agents?**
No — several patterns and one full reference architecture (Grounded Enterprise Knowledge Retrieval) apply to non-agentic capabilities: straightforward Q&A and retrieval systems with no autonomous action involved. Autonomy-domain patterns only become relevant once you actually need agentic behavior.

**How do I know if my organization is ready for this?**
That's what our maturity assessment is for — see the [assessment overview](maturity-assessment-overview.md).
