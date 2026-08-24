# 05 — Common Pitfalls

## AP-03 — Prompt-as-Policy

**How it would appear here:** This is the exact failure this lab was built to correct — the original design's only constraint was a system-prompt instruction. It's included here as the primary reference case, not a hypothetical.

**How this lab avoids it:** Step 4/5 of the implementation guide implement enforcement in a component genuinely independent of the agent's reasoning — critically, this must be a real architectural separation (a different process/service), not merely a function called from within the same agent codebase that could be bypassed by a future change to the agent's own logic.

**Warning sign if it creeps back in:** If a future change adds a new tool to the agent's capability set without also adding a corresponding policy check in the enforcement point, that new tool is effectively back to prompt-only constraint — every new tool addition must be paired with an enforcement update, not assumed to inherit protection from the existing checks.

## AP-01 — Agent by Default

**How it would appear here:** If this task had been simpler than assumed — e.g., if in practice every reassignment request maps to one of three fixed, predictable actions with no real intermediate reasoning — building it as a full autonomous agent rather than a fixed, deterministic workflow would be over-engineering relative to actual need.

**How this lab avoids it:** `04-decision-points.md`'s `DF-01` analysis explicitly confirmed genuine step-dependency (interpreting the request before determining the action) before proceeding with agentic architecture.

## AP-06 — Autonomous Privilege Creep

**How it would appear here:** A future request to add a third tool (e.g., "also let the agent close resolved tickets") added directly to the agent's tool-calling code without updating the documented Envelope (Step 2) or re-justifying the autonomy level (Step 3) — each such addition individually reasonable, cumulatively expanding the agent's actual authority beyond what was ever reviewed as a whole.

**How this lab avoids it:** By treating the Envelope and autonomy-level justification as versioned, reviewable artifacts (per `06-validation-checklist.md`'s requirement to confirm they're current, not just present), any addition should trigger an explicit update to both, not a silent code change.

## AP-08 — Human-in-the-Loop Theater (a risk to watch, not yet present)

If this lab's design were later changed to route every reassignment through human approval regardless of volume (reverting the `DF-06` decision above), and that volume turned out to be high, this anti-pattern would become a live risk — noted here as a reason not to walk back the `C-02` decision without re-running `DF-06`'s analysis.
