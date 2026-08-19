#!/usr/bin/env python3
"""Structural guards for defects the content checks cannot see.

Added after the 2026-08-18 external audit, which found three classes of problem
that every existing validator passed straight over:

  1. Recursively nested `.github/workflows/.github/workflows/...` directories
     (identical copies of a workflow, created by a bad copy operation).
  2. Source URLs containing UUID-shaped IDs with non-hex characters — the
     signature of a hallucinated link. NOTE: IKEA KR genuinely uses an
     obfuscated scheme with letters beyond f, so ikea.com is allowlisted after
     manual live verification.
  3. (advisory) Source-confidence badges with no accompanying URL. Reported as
     warnings only, because 🟢 is overloaded in this repo — it marks both source
     confidence and tourist-accessibility, and legend rows legitimately have no link.

Usage:  python3 scripts/check_structure.py
Exit code 0 = clean, 1 = issues found.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Hosts known to use non-hex characters in article IDs, verified by fetching the
# live page. Do not add to this without actually opening the URL.
OBFUSCATED_ID_HOSTS = {"ikea.com", "www.ikea.com"}

UUIDISH = re.compile(r"\b[0-9a-zA-Z]{8}-[0-9a-zA-Z]{4}-[0-9a-zA-Z]{4}-[0-9a-zA-Z]{4}-[0-9a-zA-Z]{12}\b")
URL_RE = re.compile(r"https?://[^\s)>\"'\]}]+")
# A green/official badge on a table cell that contains no link at all.
BADGE_NO_LINK = re.compile(r"\|\s*🟢\s*([^|]*)\|")


def check_nested_dotgithub() -> list[str]:
    issues = []
    gh = ROOT / ".github"
    if not gh.exists():
        return issues
    for path in gh.rglob(".github"):
        issues.append(f"nested .github directory inside .github: {path.relative_to(ROOT)}")
    for path in gh.rglob("*"):
        rel = path.relative_to(ROOT).as_posix()
        if rel.count("workflows/") > 1:
            issues.append(f"recursively nested workflows path: {rel}")
    return issues


def check_fabricated_ids() -> list[str]:
    issues = []
    for f in list(ROOT.glob("*.md")) + list((ROOT / "docs").glob("*.md")) + list((ROOT / "data").glob("*.csv")):
        text = f.read_text(encoding="utf-8")
        for url in URL_RE.finditer(text):
            u = url.group(0)
            host = u.split("/")[2].lower() if "://" in u else ""
            if host in OBFUSCATED_ID_HOSTS:
                continue
            for m in UUIDISH.finditer(u):
                if not re.fullmatch(r"[0-9a-f-]+", m.group(0)):
                    issues.append(f"{f.name} — UUID with non-hex characters (possible fabricated link): {m.group(0)}")
    return issues


def check_badge_without_source() -> list[str]:
    issues = []
    for f in sorted((ROOT / "docs").glob("*.md")):
        for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if "🟢" not in line:
                continue
            for cell in BADGE_NO_LINK.finditer(line):
                body = cell.group(1)
                if "http" not in body and "](" not in body:
                    issues.append(
                        f"{f.name}:{i} — 🟢 official badge with no source link: {body.strip()[:60]}"
                    )
    return issues


def main() -> int:
    issues = check_nested_dotgithub() + check_fabricated_ids()
    warnings = check_badge_without_source()

    if issues:
        print("Structural issues found:")
        for issue in issues:
            print(f"  ❌ {issue}")
    for warning in warnings:
        print(f"  ⚠️  {warning}")

    if issues:
        return 1
    print(
        f"✅ Structure clean — no nested workflow dirs, no fabricated-looking IDs "
        f"({len(warnings)} badge advisory warning(s))."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
