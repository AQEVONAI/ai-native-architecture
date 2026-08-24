# Maturity Model

Five maturity levels, defined independently for each of the six domains in `framework/meta-model.md`. An organization's overall profile is the set of six per-domain ratings, not a single collapsed number — see `README.md` for why.

## The five levels

| Level | Name | General Description |
|---|---|---|
| 0 | Ad Hoc | The domain's concerns are addressed inconsistently or not at all; behavior is emergent, undocumented, and varies by whoever built the capability. |
| 1 | Aware | The organization recognizes the domain's concerns and has informal practices, but nothing enforced, consistent, or reviewable. |
| 2 | Managed | Defined practices exist and are applied to new capabilities, but consistency across the existing portfolio is incomplete and enforcement is partial. |
| 3 | Governed | Practices are consistently applied, enforced (not just documented), and reviewable — matching this framework's patterns as described. |
| 4 | Optimizing | Governed practice is continuously measured and deliberately improved via the evolution loop (`E-02`), with evidence of actual revision over time, not just stable compliance. |

## Domain-specific criteria

### Knowledge

| Level | Indicator |
|---|---|
| 0 | No defined grounding requirement; answers may be asserted from model memory. Vector indexes, if present, have no access control layer (`AP-04`). |
| 1 | Some capabilities cite sources informally; no consistent fabric or federation model. |
| 2 | `K-01` grounded retrieval is standard for new capabilities; `K-02` fabric governance exists for at least one source but is not consistently applied. |
| 3 | `K-02`/`K-03` fabric governance is consistently enforced across sources; `E-01` freshness loop is active and monitored. |
| 4 | Freshness and access-control metrics are tracked over time and drive deliberate fabric revisions; staleness incidents trend down measurably. |

### Intelligence

| Level | Indicator |
|---|---|
| 0 | Single hard-coded model integration throughout, no context management discipline (`AP-07`, `AP-05` both likely present). |
| 1 | Awareness that routing/budgeting would help, but no implementation; context assembly is ad hoc. |
| 2 | `I-01` routing or `I-02` budgeting implemented for at least one capability; not yet standard practice. |
| 3 | Routing and context budgeting are standard, evaluated (`O-02`) practice; memory, where present, is governed (`I-03`). |
| 4 | Routing policy and context budget allocation are revised based on measured evaluation data on a recurring cycle. |
| — | Any level's rating should separately note whether `I-03` (Governed Memory) is in scope — an organization with no memory feature is not penalized for it, per `DF-08`. |

### Autonomy

| Level | Indicator |
|---|---|
| 0 | Agents built by default (`AP-01`) with no explicit autonomy-level assignment or documented Envelope. |
| 1 | Autonomy is discussed informally; no formal `A-01` assessment process exists. |
| 2 | `A-01` assessments exist for new agentic capabilities; older capabilities are not yet retrofitted. |
| 3 | Every agentic capability has a current, justified `A-01` assignment and a documented `A-02` Envelope; handoffs (`A-03`) are designed, not incidental. |
| 4 | Autonomy assignments are demonstrably revised based on evolution-loop signal (`E-02`), not static since initial launch. |

### Control

| Level | Indicator |
|---|---|
| 0 | Constraints exist only as prompt instructions (`AP-03`); no enforcement point independent of model reasoning. |
| 1 | Some enforcement exists for the highest-risk capability only; inconsistent elsewhere. |
| 2 | `C-02` policy enforcement or `C-01` authorization boundaries exist for most A3+ capabilities; identity propagation (`C-03`) is partial. |
| 3 | Every A3+ capability has enforced `C-01`/`C-02` controls and full `C-03` identity propagation; approval rates and review quality are monitored (guarding against `AP-08`). |
| 4 | Policy and authorization-boundary placement are demonstrably revised based on measured approval/denial data. |

### Operations

| Level | Indicator |
|---|---|
| 0 | No structured execution tracing; capability changes are promoted without formal evaluation. |
| 1 | Basic application logging exists but lacks AI-specific fields (identity, retrieval provenance, policy outcomes). |
| 2 | `O-01` tracing exists for some capabilities; `O-02` evaluation gates exist but may not consistently block promotion. |
| 3 | `O-01`/`O-02`/`O-03` are standard, enforced practice across the portfolio; degradation events are explicitly signaled. |
| 4 | Trace and evaluation data actively and demonstrably drive the evolution loop (`E-02`); degradation frequency trends down over time. |

### Evolution

| Level | Indicator |
|---|---|
| 0 | No mechanism exists to detect or act on architectural drift; changes are made ad hoc in response to individual incidents only. |
| 1 | The organization recognizes the value of a review cycle but has not implemented one. |
| 2 | An informal or irregular review cycle exists for at least one capability. |
| 3 | `E-01`/`E-02` loops run on a defined, honored cadence across the capability portfolio, producing recorded decisions. |
| 4 | The evolution loop has a demonstrated track record of producing decisions that measurably improved downstream metrics (evaluation scores, degradation frequency, autonomy-level accuracy). |

## Reading a profile

A profile like Knowledge: 3, Intelligence: 2, Autonomy: 1, Control: 1, Operations: 2, Evolution: 0 is a realistic, common early-stage profile — strong on the domain the organization started with (Knowledge), and correctly showing Autonomy/Control immaturity if agentic capabilities are new or nonexistent. The roadmap (`roadmap-template.md`) should prioritize Control catching up to Autonomy if and when Autonomy increases — an Autonomy level rising faster than Control is the specific imbalance `AP-06` describes.

## Revision History

- 0.1.0 (2026-08-24) — Initial maturity model, six domains x five levels.
