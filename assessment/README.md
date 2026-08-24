# Assessment Framework

A 5-file maturity model for evaluating an organization's AI-native architecture practice against the six domains defined in `framework/meta-model.md`. This assessment is diagnostic, not certifying — its purpose is to produce an honest, evidence-based picture of current state and a concrete improvement roadmap, not a score to be optimized for its own sake.

| File | Purpose |
|---|---|
| [maturity-model.md](maturity-model.md) | The core 5-level maturity model, defined per domain, with explicit anti-pattern and pattern indicators at each level. |
| [assessment-questionnaire.md](assessment-questionnaire.md) | The structured questions used to gather evidence for a maturity rating, per domain. |
| [scoring-guide.md](scoring-guide.md) | How to convert questionnaire answers into a domain-level and overall maturity rating, and how to interpret the result honestly. |
| [roadmap-template.md](roadmap-template.md) | How to turn an assessment result into a prioritized, sequenced improvement roadmap referencing specific patterns and decision guides. |
| [worked-example.md](worked-example.md) | A full illustrative (composite, not a named organization) assessment walkthrough from questionnaire through roadmap. |

## Principles this assessment follows

- **Evidence over self-report.** Per `framework/principles.md`'s evidence-over-assertion principle, the questionnaire asks for specific artifacts (a documented Envelope, an evaluation suite, an execution trace sample) wherever possible, not just a confidence rating.
- **Per-domain, not single-score.** An organization can be highly mature in Knowledge while being immature in Control — collapsing this into one overall number would hide exactly the imbalance that matters most for prioritization (see `AP-06`, which is a common consequence of exactly this kind of imbalance).
- **Diagnostic, not punitive.** A low maturity rating in a domain the organization has not yet needed (e.g., Autonomy, for an organization with no agentic capabilities yet) is not a deficiency — the roadmap should reflect actual priority, not uniform pressure to max every domain.

## How to use this assessment

Run the questionnaire (`assessment-questionnaire.md`) against your current AI-native capability portfolio, score it per domain (`scoring-guide.md`), and use the result to prioritize a roadmap (`roadmap-template.md`) referencing the specific patterns (`patterns/`), decision guides (`decision-framework/`), and reference architectures (`reference-architectures/`) that address the gaps found.
