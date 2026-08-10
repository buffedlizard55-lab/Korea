#!/usr/bin/env python3
"""Create a D-14 trip-lock report from core deal data.

This is an offline planning report: it identifies exactly what must be checked
in the browser/app before departure; it does not claim to refresh external data.
"""
from __future__ import annotations

import argparse
import csv
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEALS = ROOT / "data" / "deals.csv"


def parse(raw: str) -> date:
    return date.fromisoformat(raw)


def main() -> int:
    parser = argparse.ArgumentParser(description="Print a city-sorted D-14 deal recheck report.")
    parser.add_argument("--as-of", default=date.today().isoformat(), help="report date YYYY-MM-DD")
    parser.add_argument("--trip-start", default="2026-10-31", help="trip start YYYY-MM-DD")
    args = parser.parse_args()
    as_of, trip_start = parse(args.as_of), parse(args.trip_start)
    with DEALS.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    actionable = [r for r in rows if r["status"] in {"active", "live-check", "future"}]
    actionable.sort(key=lambda r: (r["city"], r["expiry_or_recheck"], r["deal_id"]))
    print(f"TRIP LOCK REPORT — {as_of.isoformat()} — trip starts {trip_start.isoformat()} ({(trip_start-as_of).days} days away)")
    print("Only recheck records whose current terms could change the plan. Do not spend time on expired/rejected claims.\n")
    current_city = None
    for row in actionable:
        if row["city"] != current_city:
            current_city = row["city"]
            print(f"[{current_city}]")
        due = parse(row["expiry_or_recheck"])
        flag = "OVERDUE" if due < as_of else "DUE BEFORE TRIP" if due <= trip_start else "AFTER START"
        print(f"  {flag:15} {row['deal_id']} — {row['title']}")
        print(f"    Check: {row['notes']}")
        print(f"    Source: {row['source_url']}")
        print(f"    Backup: {row['local_backup']}")
    print("\nFinal tasks: confirm hotels/neighborhoods, choose Cheonan or Daejeon from live availability, screenshot only current barcodes, and rerun pass math.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
