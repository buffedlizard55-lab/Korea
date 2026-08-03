#!/usr/bin/env python3
"""Health checks for the repo's markdown docs (no network needed).

Checks:
  1. Every markdown table has consistent column counts.
  2. Every internal link (../README.md, sibling .md, docs/...) resolves.
  3. Every doc has a "Last verified: YYYY-MM-DD" line.

Usage:  python3 scripts/check_docs.py
Exit code 0 = clean, 1 = issues found.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
MD_FILES = sorted((ROOT / "README.md").glob("*"))[:0] or []
MD_FILES = [ROOT / "README.md"] + sorted(DOCS.glob("*.md")) + sorted(ROOT.glob("*.md"))
MD_FILES = sorted(set(MD_FILES))

DATE_RE = re.compile(r"(?:Last verified|Last full verification sweep): \d{4}-\d{2}-\d{2}")
LINK_RE = re.compile(r"\]\(([^)#\s]+\.md)\)")

# Meta-docs don't carry deal date stamps (they're changelog/contribution docs).
DATE_STAMP_EXEMPT = {ROOT / "CHANGELOG.md", ROOT / "CONTRIBUTING.md"}


def check_tables(path: Path) -> list[str]:
    issues = []
    lines = path.read_text(encoding="utf-8").splitlines()
    current_cols = None
    for i, line in enumerate(lines, 1):
        if not line.lstrip().startswith("|"):
            current_cols = None
            continue
        cols = len([c for c in line.split("|")])
        if line.replace("|", "").replace("-", "").strip() == "":
            continue  # separator row
        if current_cols is None:
            current_cols = cols
        elif cols != current_cols:
            issues.append(f"{path.name}:{i} — table column mismatch ({cols} vs {current_cols}): {line[:60]}")
    return issues


def resolve_internal(target: str, origin: Path) -> bool:
    if target.startswith("http") or target.startswith("#"):
        return True
    if target.startswith("mailto:"):
        return True
    return (origin.parent / target).resolve().exists()


def check_links(path: Path) -> list[str]:
    issues = []
    text = path.read_text(encoding="utf-8")
    for m in LINK_RE.finditer(text):
        target = m.group(1)
        if not resolve_internal(target, path):
            issues.append(f"{path.name} — broken internal link: {target}")
    return issues


def check_date(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [] if DATE_RE.search(text) else [f"{path.name} — missing 'Last verified: YYYY-MM-DD'"]


def main() -> int:
    all_issues = []
    for f in MD_FILES:
        all_issues += check_tables(f)
        all_issues += check_links(f)
        if f not in DATE_STAMP_EXEMPT:
            all_issues += check_date(f)

    if all_issues:
        print("Issues found:")
        for issue in all_issues:
            print(f"  ❌ {issue}")
        return 1
    print(f"✅ {len(MD_FILES)} markdown files: tables, internal links, and date stamps all clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
