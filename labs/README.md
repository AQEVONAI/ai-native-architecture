# Architecture Labs

5 hands-on labs, each building toward one reference architecture in `reference-architectures/`. Where a reference architecture describes a composition of patterns conceptually, a lab walks through building it for a specific, illustrative scenario — with decision points, common pitfalls, a validation checklist, and exercises.

| Lab | Reference Architecture | Scenario |
|---|---|---|
| [01-grounded-knowledge-retrieval/](01-grounded-knowledge-retrieval/) | `RA-01` | Building a grounded Q&A capability over federated HR and IT knowledge sources |
| [02-governed-memory/](02-governed-memory/) | `RA-02` | Adding governed, cross-session memory to a support assistant |
| [03-bounded-autonomous-agent/](03-bounded-autonomous-agent/) | `RA-03` | Building a policy-bounded agent that can take real action (ticket reassignment) |
| [04-observability-evaluation/](04-observability-evaluation/) | `RA-04` | Instrumenting execution tracing and evaluation gating for a production capability |
| [05-composite-architecture/](05-composite-architecture/) | `RA-05` | Extending shared infrastructure to a second capability, composing all six domains |

## Scenario continuity

Labs 01–04 build on the same illustrative composite organization and capability set introduced in `assessment/worked-example.md` (a mid-size enterprise software company, an HR/IT support assistant, and an in-development ticket-update agent) — explicitly a representative composite scenario, not a named organization, consistent with `framework/principles.md`'s evidence-over-assertion discipline. Lab 05 extends the same scenario to a second capability to illustrate the composite architecture's shared-infrastructure value directly.

## Standard lab structure

Each lab directory contains 9 files:

```
README.md                        — objectives, prerequisites, target reference architecture
01-scenario-and-objectives.md    — the specific scenario this lab builds toward
02-architecture-walkthrough.md   — how the reference architecture's components apply here
03-implementation-guide.md       — practical build steps, in implementation-neutral pseudocode/config
04-decision-points.md            — where decision-framework guides apply within this lab, and what was chosen
05-common-pitfalls.md            — the anti-patterns most likely to appear in this scenario, and how this lab avoids them
06-validation-checklist.md       — how to verify the lab's result actually satisfies the target reference architecture
07-exercises.md                  — hands-on exercises extending the lab
08-solutions-and-discussion.md   — discussion of the exercises, including legitimate alternative approaches
```

## What these labs are not

These labs are architecture walkthroughs, not a specific vendor's tutorial — implementation guides describe steps and configuration shape in vendor-neutral terms, consistent with this framework's vendor-neutral-by-default principle. They are also not a substitute for `decision-framework/`'s guides — each lab references the specific decision guides relevant to its scenario rather than re-deriving that guidance.
