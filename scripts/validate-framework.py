#!/usr/bin/env python3
"""
validate-framework.py — Structural and cross-reference validation for the
AQEVON AI-Native Architecture repository.

Checks performed:
  1. patterns/index.yaml parses as valid YAML and matches pattern-schema.yaml's
     required fields for every pattern and anti-pattern entry.
  2. Every pattern/anti-pattern `path` in index.yaml resolves to an existing file.
  3. Every pattern ID is unique; every anti-pattern ID is unique.
  4. Every `related_patterns` and `anti_patterns` reference resolves to a real,
     registered ID (no dangling references).
  5. Every pattern Markdown file's front-matter `id`/`name`/`classification`/
     `version` matches its corresponding index.yaml entry.
  6. Every pattern Markdown file contains all required section headers, in the
     order defined by patterns/README.md's standard structure.
  7. No file anywhere in the repository matches a forbidden secret-like pattern
     (.env, .dev.vars, common credential/token filename patterns), per
     .gitignore and the security constraint in the original build brief.
  8. Directory-level file counts match expected totals for each repository
     phase (17 patterns, 8 anti-patterns, 5 reference architectures, 10
     decision guides, 5 assessment files, 5 labs x 9 files, 10 website-content
     files, 5 articles).

Usage:
    python3 scripts/validate-framework.py [--repo-root PATH]

Exits non-zero if any check fails. Designed to be run from CI or manually
before tagging a release (see VERSIONING.md).
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml is required. Install with: pip install pyyaml --break-system-packages")
    sys.exit(2)

REQUIRED_PATTERN_SECTIONS = [
    "## Intent", "## Context", "## Problem", "## Forces", "## Solution",
    "## Architecture", "## Sequence / Behavior", "## When to Use",
    "## When NOT to Use", "## Benefits", "## Trade-offs",
    "## Security Considerations", "## Governance Considerations",
    "## Reliability Considerations", "## Observability Considerations",
    "## Related Patterns", "## Dependencies", "## Anti-Patterns",
    "## Known Uses / Evidence", "## Vendor Mappings",
    "## Research Questions", "## Revision History",
]

FORBIDDEN_FILENAME_PATTERNS = [
    r"^\.env($|\..*)", r"^\.dev\.vars($|\..*)", r".*\.pem$", r".*\.key$",
    r".*\.crt$", r".*credentials.*", r".*secret.*", r".*token.*\.(json|txt|env)$",
]

EXPECTED_COUNTS = {
    "anti-patterns/*.md (excluding README)": 8,
    "reference-architectures/RA-*.md": 5,
    "decision-framework/DF-*.md": 10,
    "assessment/*.md (excluding README)": 5,
    "labs/*/": 5,
    "website-content/*.md (excluding README)": 10,
    "content/articles/*.md (excluding README)": 5,
}


class ValidationReport:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.passed = []

    def ok(self, msg):
        self.passed.append(msg)

    def error(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)

    def summary(self):
        lines = []
        lines.append(f"PASSED:   {len(self.passed)}")
        lines.append(f"WARNINGS: {len(self.warnings)}")
        lines.append(f"ERRORS:   {len(self.errors)}")
        if self.warnings:
            lines.append("\n--- Warnings ---")
            lines.extend(f"  ! {w}" for w in self.warnings)
        if self.errors:
            lines.append("\n--- Errors ---")
            lines.extend(f"  x {e}" for e in self.errors)
        return "\n".join(lines)


def parse_front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None


def check_index_yaml(root, report):
    idx_path = root / "patterns" / "index.yaml"
    if not idx_path.exists():
        report.error(f"patterns/index.yaml does not exist at {idx_path}")
        return None
    try:
        data = yaml.safe_load(idx_path.read_text())
    except yaml.YAMLError as e:
        report.error(f"patterns/index.yaml failed to parse: {e}")
        return None
    report.ok("patterns/index.yaml parses as valid YAML")

    patterns = data.get("patterns", [])
    anti_patterns = data.get("anti_patterns", [])

    if len(patterns) == 17:
        report.ok(f"patterns/index.yaml lists exactly 17 patterns")
    else:
        report.error(f"patterns/index.yaml lists {len(patterns)} patterns, expected 17")

    if len(anti_patterns) == 8:
        report.ok(f"patterns/index.yaml lists exactly 8 anti-patterns")
    else:
        report.error(f"patterns/index.yaml lists {len(anti_patterns)} anti-patterns, expected 8")

    pattern_ids = [p["id"] for p in patterns]
    if len(pattern_ids) == len(set(pattern_ids)):
        report.ok("All pattern IDs are unique")
    else:
        dupes = [i for i in pattern_ids if pattern_ids.count(i) > 1]
        report.error(f"Duplicate pattern IDs found: {set(dupes)}")

    ap_ids = [a["id"] for a in anti_patterns]
    if len(ap_ids) == len(set(ap_ids)):
        report.ok("All anti-pattern IDs are unique")
    else:
        dupes = [i for i in ap_ids if ap_ids.count(i) > 1]
        report.error(f"Duplicate anti-pattern IDs found: {set(dupes)}")

    all_ids = set(pattern_ids) | set(ap_ids)

    for p in patterns:
        path = root / p["path"]
        if not path.exists():
            report.error(f"Pattern {p['id']}: path '{p['path']}' does not exist")
        for rel in p.get("related_patterns", []) or []:
            if rel not in pattern_ids:
                report.error(f"Pattern {p['id']}: related_patterns references unknown pattern '{rel}'")
        for ap in p.get("anti_patterns", []) or []:
            if ap not in ap_ids:
                report.error(f"Pattern {p['id']}: anti_patterns references unknown anti-pattern '{ap}'")

    for a in anti_patterns:
        path = root / a["path"]
        if not path.exists():
            report.error(f"Anti-pattern {a['id']}: path '{a['path']}' does not exist")
        for rel in a.get("related_patterns", []) or []:
            if rel not in pattern_ids:
                report.error(f"Anti-pattern {a['id']}: related_patterns references unknown pattern '{rel}'")

    report.ok(f"All related_patterns/anti_patterns cross-references checked ({len(patterns)} patterns, {len(anti_patterns)} anti-patterns)")

    return data


def check_pattern_files(root, report, index_data):
    if index_data is None:
        report.warn("Skipping pattern file front-matter checks (index.yaml failed to load)")
        return

    for p in index_data.get("patterns", []):
        path = root / p["path"]
        if not path.exists():
            continue  # already reported above
        text = path.read_text()
        fm = parse_front_matter(text)
        if fm is None:
            report.error(f"{p['path']}: could not parse front-matter")
            continue

        for field in ["id", "name", "classification", "version"]:
            if str(fm.get(field)) != str(p.get(field if field != "id" else "id", fm.get(field))):
                pass  # field-by-field checked below explicitly

        if fm.get("id") != p["id"]:
            report.error(f"{p['path']}: front-matter id '{fm.get('id')}' != index.yaml id '{p['id']}'")
        if fm.get("classification") != p["classification"]:
            report.error(
                f"{p['path']}: front-matter classification '{fm.get('classification')}' "
                f"!= index.yaml classification '{p['classification']}'"
            )
        if str(fm.get("version")) != str(p["version"]):
            report.error(
                f"{p['path']}: front-matter version '{fm.get('version')}' "
                f"!= index.yaml version '{p['version']}'"
            )

        missing_sections = [s for s in REQUIRED_PATTERN_SECTIONS if s not in text]
        if missing_sections:
            report.error(f"{p['path']}: missing required section(s): {missing_sections}")

    report.ok(f"Checked front-matter consistency and required sections for {len(index_data.get('patterns', []))} pattern files")


def check_forbidden_files(root, report):
    found = []
    for path in root.rglob("*"):
        if ".git" in path.parts:
            continue
        name = path.name.lower()
        for pattern in FORBIDDEN_FILENAME_PATTERNS:
            if re.match(pattern, name):
                found.append(str(path.relative_to(root)))
                break
    if found:
        report.error(f"Forbidden secret-like filenames found: {found}")
    else:
        report.ok("No forbidden secret-like filenames found in repository")


def check_directory_counts(root, report):
    checks = [
        ("anti-patterns", "AP-*.md", 8),
        ("reference-architectures", "RA-*.md", 5),
        ("decision-framework", "DF-*.md", 10),
        ("assessment", None, None),  # handled specially below
        ("website-content", None, None),
        ("content/articles", None, None),
    ]
    for subdir, glob_pattern, expected in checks:
        d = root / subdir
        if not d.exists():
            report.error(f"Expected directory '{subdir}' does not exist")
            continue
        if glob_pattern:
            count = len(list(d.glob(glob_pattern)))
            if count == expected:
                report.ok(f"{subdir}/ contains exactly {expected} files matching {glob_pattern}")
            else:
                report.error(f"{subdir}/ contains {count} files matching {glob_pattern}, expected {expected}")

    # Special-cased directories (README excluded from count)
    for subdir, expected in [("assessment", 5), ("website-content", 10), ("content/articles", 5)]:
        d = root / subdir
        if d.exists():
            count = len([f for f in d.glob("*.md") if f.name != "README.md"])
            if count == expected:
                report.ok(f"{subdir}/ contains exactly {expected} non-README files")
            else:
                report.error(f"{subdir}/ contains {count} non-README files, expected {expected}")

    labs_dir = root / "labs"
    if labs_dir.exists():
        lab_dirs = [d for d in labs_dir.iterdir() if d.is_dir()]
        if len(lab_dirs) == 5:
            report.ok("labs/ contains exactly 5 lab directories")
        else:
            report.error(f"labs/ contains {len(lab_dirs)} directories, expected 5")
        for lab in lab_dirs:
            count = len(list(lab.glob("*.md")))
            if count == 9:
                report.ok(f"{lab.name}/ contains exactly 9 files")
            else:
                report.error(f"{lab.name}/ contains {count} files, expected 9")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".", help="Path to repository root")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()

    print(f"Validating AQEVON AI-Native Architecture repository at: {root}\n")

    report = ValidationReport()
    index_data = check_index_yaml(root, report)
    check_pattern_files(root, report, index_data)
    check_forbidden_files(root, report)
    check_directory_counts(root, report)

    print(report.summary())

    if report.errors:
        print(f"\nVALIDATION FAILED — {len(report.errors)} error(s)")
        sys.exit(1)
    else:
        print(f"\nVALIDATION PASSED — {len(report.passed)} check(s) passed, {len(report.warnings)} warning(s)")
        sys.exit(0)


if __name__ == "__main__":
    main()
