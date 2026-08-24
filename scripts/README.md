# Scripts

Validation tooling for this repository's structural and cross-reference integrity.

| Script | Purpose |
|---|---|
| [validate-framework.py](validate-framework.py) | Core validator: index.yaml schema/parsing, cross-reference integrity, pattern front-matter consistency, required section presence, forbidden-filename/secret-pattern scan, expected file-count checks per directory. |
| [validate-framework.ps1](validate-framework.ps1) | Windows PowerShell wrapper for `validate-framework.py`. |

## Running validation

```bash
# macOS/Linux
python3 scripts/validate-framework.py --repo-root .

# Windows
.\scripts\validate-framework.ps1
```

Requires Python 3 and `pyyaml` (`pip install pyyaml`).

## When to run this

- Before tagging any release (see `VERSIONING.md`).
- After any change to `patterns/index.yaml` or any pattern/anti-pattern Markdown file.
- As a CI check on every pull request, once CI is configured (not yet implemented — see `CONTRIBUTING.md`).

## What this does not check

This validator checks structural integrity (do the files exist, do the cross-references resolve, is the schema followed) — it does not check content quality, prose accuracy, or classification correctness. Classification accuracy is the responsibility of the research process described in `research/research-methodology.md`, not this script.
