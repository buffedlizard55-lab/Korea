#!/usr/bin/env python3
"""Validate the deal-discovery queue uses the shared lifecycle vocabulary."""
from __future__ import annotations

import csv
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "data" / "deal-discovery-queue.csv"
STATUSES = {"candidate", "active", "live-check", "future", "expired", "rejected"}
REQUIRED = {"date_found", "city", "candidate_deal", "source_url", "status", "notes"}


def is_date_or_placeholder(value: str) -> bool:
    if value == "YYYY-MM-DD":
        return True
    try:
        date.fromisoformat(value)
        return True
    except ValueError:
        return False


def main() -> int:
    with QUEUE.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    issues: list[str] = []
    for line, row in enumerate(rows, start=2):
        if row.get("candidate_deal") == "add candidate here":
            continue  # format row is intentionally a placeholder
        missing = [field for field in REQUIRED if not row.get(field, "").strip()]
        if missing:
            issues.append(f"line {line}: missing {', '.join(sorted(missing))}")
        if row.get("status") not in STATUSES:
            issues.append(f"line {line}: invalid lifecycle status '{row.get('status')}'")
        if not is_date_or_placeholder(row.get("date_found", "")):
            issues.append(f"line {line}: invalid date_found")
        if not is_date_or_placeholder(row.get("expiry_or_recheck_date", "")):
            issues.append(f"line {line}: invalid expiry_or_recheck_date")
    if issues:
        print("Discovery-queue issues:")
        for issue in issues:
            print(f"  ❌ {issue}")
        return 1
    counts = {status: sum(r.get("status") == status for r in rows) for status in sorted(STATUSES)}
    print(f"✅ {len(rows) - 1} queue records validated — " + ", ".join(f"{k}: {v}" for k, v in counts.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
