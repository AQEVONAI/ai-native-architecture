# Roadmap Template

How to turn a scored assessment profile (`scoring-guide.md`) into a prioritized, sequenced improvement roadmap referencing specific patterns, decision guides, and reference architectures.

## Prioritization principle

Prioritize the domain with the lowest score **among domains genuinely in scope**, with one override: if Control (`C-01`/`C-02`/`C-03`) scores meaningfully lower than Autonomy, treat closing that specific gap as the top priority regardless of other domains' scores — an Autonomy level unsupported by matching Control maturity is the direct precondition for `AP-06` (Autonomous Privilege Creep), the highest-severity anti-pattern in this framework's catalog.

## Roadmap structure

For each prioritized domain, the roadmap entry should specify:

1. **Current level and target level** — do not default to targeting Level 4 for every domain; target the level that matches the domain's actual importance to the organization's risk profile (see `maturity-model.md`'s reading-a-profile guidance).
2. **Specific gap** — which questionnaire question(s) revealed the gap, and what evidence (or lack of it) was found.
3. **Recommended pattern(s)** — the specific pattern(s) in `patterns/` that close this gap.
4. **Recommended decision guide(s)** — if the gap stems from an undecided architectural question (not just unimplemented practice), the relevant `decision-framework/` guide.
5. **Recommended reference architecture** — if the gap is best closed as part of a broader composition rather than a single pattern, the relevant `reference-architectures/` entry (see `DF-09`).
6. **Sequencing dependency** — does this gap need to close before another roadmap item can proceed? (Most commonly: Control-domain gaps should close before Autonomy-domain advancement, per the prioritization principle above.)
7. **Success evidence** — what specific artifact or observable would demonstrate this gap is closed, phrased so a future re-assessment can verify it directly (mirroring the same evidence-over-assertion discipline the original assessment used).

## Template

```markdown
### Roadmap Item: [Domain] — [Current Level] → [Target Level]

**Gap:** [specific finding from questionnaire, with question reference]
**Evidence at assessment time:** [what was or wasn't demonstrated]

**Recommended actions:**
- Pattern(s): [e.g., C-02 Policy-Bounded Action]
- Decision guide(s): [e.g., DF-06]
- Reference architecture: [e.g., RA-03]

**Sequencing:** [blocks / blocked by other roadmap items]
**Success evidence for re-assessment:** [specific, checkable artifact]
**Target timeframe:** [organization-specific]
```

## Sequencing guidance across domains

A typical, defensible sequencing for an organization early in AI-native maturity:

1. **Operations first, generally** — `O-01` execution tracing is a prerequisite for evidencing progress in every other domain during a future re-assessment; building it early makes every subsequent roadmap item's success evidence achievable.
2. **Control before further Autonomy investment** — per the prioritization principle, do not advance Autonomy maturity (more agentic capabilities, higher autonomy levels) faster than Control can support it.
3. **Knowledge fabric investment paced to actual portfolio growth** — per `DF-04`, do not roadmap a full `K-02`/`K-03` build before a second capability justifies it; a single-capability organization's Knowledge roadmap item should target Level 2–3 via `K-01`, not premature fabric investment.
4. **Evolution loop (`E-02`) formalization once the other domains have enough operational history to produce meaningful aggregate signal** — an Evolution-domain roadmap item scheduled before Operations tracing exists has nothing to act on yet.

## Revisiting the roadmap

Per this framework's own `E-02` principle applied reflexively: the roadmap itself should be reviewed against a fresh assessment on a recurring cadence, not treated as a one-time plan executed to completion and retired. A roadmap that has not changed across two consecutive assessment cycles is itself worth investigating — either the organization's AI-native architecture has genuinely stabilized, or the assessment process has stopped surfacing real signal.

## Revision History

- 0.1.0 (2026-08-24) — Initial roadmap template.
