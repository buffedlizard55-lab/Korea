#!/usr/bin/env python3
"""Warn/fail when a deal or discovery lead has passed its recheck date.

The recheck date is a maintenance deadline, not necessarily the promotion's
expiry. Active/live-check/future/candidate records must be revisited by then.
"""
from __future__ import annotations

import argparse
import csv
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = [(ROOT / "data" / "deals.csv", "deal_id"), (ROOT / "data" / "deal-discovery-queue.csv", "candidate_deal")]
WATCHED = {"candidate", "active", "live-check", "future"}


def parse_date(raw: str) -> date | None:
    try:
        return date.fromisoformat(raw)
    except ValueError:
        return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Check recheck/expiry dates against a chosen date.")
    parser.add_argument("--as-of", default=date.today().isoformat(), help="YYYY-MM-DD; defaults to today")
    parser.add_argument("--horizon", type=int, default=14, help="days ahead to report as due soon")
    args = parser.parse_args()
    today = parse_date(args.as_of)
    if today is None:
        parser.error("--as-of must be YYYY-MM-DD")
    if args.horizon < 0:
        parser.error("--horizon must be non-negative")

    overdue: list[str] = []
    due_soon: list[str] = []
    checked = 0
    for path, label_field in FILES:
        date_field = "expiry_or_recheck" if path.name == "deals.csv" else "expiry_or_recheck_date"
        with path.open(encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                if row.get(label_field) in {"", "add candidate here"}:
                    continue
                if row.get("status") not in WATCHED:
                    continue
                target = parse_date(row.get(date_field, ""))
                if target is None:
                    overdue.append(f"{path.name}: {row[label_field]} has no valid {date_field}")
                    continue
                checked += 1
                delta = (target - today).days
                item = f"{path.name}: {row[label_field]} — {target.isoformat()} ({row['status']})"
                if delta < 0:
                    overdue.append(item)
                elif delta <= args.horizon:
                    due_soon.append(item)

    for item in overdue:
        print(f"❌ OVERDUE {item}")
    for item in due_soon:
        print(f"⚠️  DUE SOON {item}")
    if not overdue and not due_soon:
        print(f"✅ {checked} active/candidate records are outside the next {args.horizon}-day recheck window.")
    else:
        print(f"\nChecked {checked} active/candidate records: {len(overdue)} overdue, {len(due_soon)} due soon.")
    return 1 if overdue else 0


if __name__ == "__main__":
    sys.exit(main())
