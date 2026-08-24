---
title: AQEVON Architecture Principles
version: 0.1
status: research
last_reviewed: 2026-08-24
---

# AQEVON Architecture Principles

These principles govern how every pattern, reference architecture, decision guide, and assessment in this repository is written and how the AQEVON framework itself is evolved. They are the standard against which contributions (see `CONTRIBUTING.md`) are reviewed.

## 1. Complexity must be justified by capability

The default architecture is the simplest one that solves the problem. Agentic architecture, multi-model routing, and autonomous execution are not adopted because they are available — they are adopted because a specific business capability requires them and the architecture to control them safely exists. The preferred progression, used throughout the decision framework, is:

```
Deterministic workflow → Direct AI interaction → AI-assisted workflow → Single bounded agent → Multi-agent orchestration
```

An architect should be able to justify, in one sentence, why the chosen point on this progression was necessary rather than the one before it.

## 2. Vendor-neutral by default

Conceptual architecture — the pattern's Solution, Architecture, and Sequence sections, and every reference architecture's core diagram — must stand independent of any specific cloud provider, model vendor, or framework. Vendor mappings (Azure, AWS, GCP, open-source) are provided as implementation guidance, clearly separated from the conceptual model, never embedded in it.

## 3. Authority and capability are architected together

An AI capability's ability to know, reason, and act (Knowledge, Intelligence, Autonomy) is never designed without designing, in the same pass, what it is authorized to do and how that authorization is enforced and observed (Control, Operations). A pattern, reference architecture, or lab that describes a capability without describing its authority boundary is incomplete.

## 4. Prior art before originality claims

No pattern, article, or public-facing document may claim AQEVON originated a concept unless the prior-art review in `research/prior-art-differentiation-matrix.md` supports that claim. The default posture is "AQEVON synthesizes" or "AQEVON proposes," not "AQEVON invented." Where prior art has not yet been reviewed, the document must say so explicitly rather than imply novelty by omission.

## 5. Canonical content lives in Markdown and YAML

This repository — its Markdown pattern cards, YAML metadata, and Mermaid diagrams — is the single source of truth for AQEVON's architecture IP. Website pages, PDFs, whitepapers, and any future AI knowledge layer are derived artifacts, generated from this content, never the other way around. Content is never authored first in a derived format and back-ported here.

## 6. Every architectural claim answers eight questions

Consistent with the quality bar in `GOVERNANCE.md`, a pattern, reference architecture, or lab is not complete until it can answer:

1. Why does this matter?
2. What recurring problem does it solve?
3. What are the forces in tension?
4. What architectural decision does it enable?
5. What are the trade-offs?
6. When should an architect use it?
7. When should an architect *not* use it?
8. What prior art exists, and what is AQEVON's actual contribution?

## 7. Evidence over assertion

Claims about maturity, adoption, or effectiveness are sourced (see `research/sources.md`) or explicitly marked as an AQEVON hypothesis requiring validation. Fabricated statistics, invented case studies, and unverifiable claims are prohibited — this repository uses "Illustrative Scenario" and "Reference Architecture" labeling for non-customer examples, consistent with AQEVON's broader content-honesty discipline.

## 8. Machine readability is a design constraint, not an afterthought

Every pattern and anti-pattern has a stable ID, structured YAML metadata, and a predictable Markdown structure specifically so that `patterns/index.yaml` can drive a future pattern explorer, assessment engine, and architecture decision engine (see `future/architecture-decision-engine.md`) without restructuring the underlying content.
