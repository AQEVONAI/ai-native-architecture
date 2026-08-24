---
status: content-prep-only
last_reviewed: 2026-08-24
---

# Integration Boundary and Future Model

## Current status

None of the content in `website-content/` is currently published on the AQEVON website. This repository (`aqevon-ai-native-architecture`) is separate from the website repository (`aqevon-website`), and this repository's scope explicitly does not include making any change to the website's code, content, or deployment. This file exists to state that boundary plainly for whoever integrates this content later, and to sketch — without building — how integration should eventually work.

## Why the boundary exists

This repository's architecture content is still at `v0.x` (Research status — see `VERSIONING.md`) and under active revision, including classification corrections like the one documented in `research/differentiation.md`. Publishing directly from an actively changing research repository risks the website presenting claims that are revised, superseded, or corrected shortly after publication. Separating content preparation (here) from publication (the website) allows this repository to keep iterating honestly without that iteration being visible mid-revision to website visitors.

## The intended future integration model

When AQEVON is ready to publish this content:

1. **Publish from tagged releases, not `main`.** Per `VERSIONING.md`, the website should consume a specific tagged version (e.g., `v1.0.0`) of this repository's content, not the actively changing `main` branch — this ensures published content is stable and matches a specific, citable version of the framework.
2. **Content, not raw pattern cards.** The files in `website-content/` are the intended publication source, not the internal pattern cards in `patterns/` — the internal cards are written for architects; `website-content/` is written for the website's actual visitor.
3. **A defined update cadence.** Website content should be re-synced against a new tagged release on a defined schedule (aligned with `VERSIONING.md`'s release cadence), not continuously auto-published from an evolving research repository.
4. **Classification claims stay accurate.** Any specific novelty or differentiation claim published on the website must remain consistent with the classification recorded in `patterns/index.yaml` and `research/prior-art-differentiation-matrix.md` at the time of the tagged release being published — if a future research cycle changes a classification (as happened with `A-01` in this repository's initial research pass), previously published website content referencing the old classification should be flagged for review, not left uncorrected.

## What this repository does not do

This repository does not implement a CMS integration, a build pipeline into the website, or any website-facing API. That implementation work belongs to whoever owns `aqevon-website`, informed by this document, once AQEVON decides to publish.
