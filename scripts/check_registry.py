#!/usr/bin/env python3
"""Validate the normalized deal registry's status and required fields."""
from __future__ import annotations

import csv
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "data" / "deals.csv"
ALLOWED_STATUSES = {"candidate", "active", "live-check", "future", "expired", "rejected"}
ALLOWED_TYPES = {"walk-in-value", "standing-benefit", "live-coupon", "city-pass", "transit-pass", "payment-layer", "free-attraction", "future-event", "expired-event", "rejected-claim"}
REQUIRED = {"deal_id", "city", "category", "deal_type", "title", "status", "expiry_or_recheck", "access", "source_tier", "source_url", "live_check", "local_backup"}


def main() -> int:
    with PATH.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    issues: list[str] = []
    ids: set[str] = set()
    for number, row in enumerate(rows, start=2):
        missing = [field for field in REQUIRED if not row.get(field, "").strip()]
        if missing:
            issues.append(f"line {number}: missing {', '.join(sorted(missing))}")
        deal_id = row.get("deal_id", "")
        if deal_id in ids:
            issues.append(f"line {number}: duplicate deal_id {deal_id}")
        ids.add(deal_id)
        if row.get("deal_type") not in ALLOWED_TYPES:
            issues.append(f"line {number}: invalid deal_type '{row.get('deal_type')}'")
        if row.get("status") not in ALLOWED_STATUSES:
            issues.append(f"line {number}: invalid status '{row.get('status')}'")
        try:
            date.fromisoformat(row.get("expiry_or_recheck", ""))
        except ValueError:
            issues.append(f"line {number}: expiry_or_recheck must be YYYY-MM-DD")
        if row.get("status") == "active" and row.get("live_check") != "yes":
            issues.append(f"line {number}: active deals must retain a live_check=yes safeguard")
    if issues:
        print("Registry issues:")
        for issue in issues:
            print(f"  ❌ {issue}")
        return 1
    counts = {status: sum(row["status"] == status for row in rows) for status in sorted(ALLOWED_STATUSES)}
    print(f"✅ {len(rows)} deals validated — " + ", ".join(f"{k}: {v}" for k, v in counts.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
