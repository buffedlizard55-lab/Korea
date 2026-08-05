#!/usr/bin/env python3
"""Print the normalized core deal registry by city or status.

Examples:
  python3 scripts/deal_registry.py --city Cheonan
  python3 scripts/deal_registry.py --city Busan --backups
  python3 scripts/deal_registry.py --status active
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "deals.csv"


def main() -> int:
    parser = argparse.ArgumentParser(description="Filter the core Korea-deal registry.")
    parser.add_argument("--city", default="all", help="city name, Nationwide, or all")
    parser.add_argument("--status", default="all", help="candidate, active, live-check, future, expired, rejected, or all")
    parser.add_argument("--backups", action="store_true", help="also print the normal local backup for each deal")
    args = parser.parse_args()
    with REGISTRY.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

    if args.city.lower() != "all":
        wanted = args.city.casefold()
        rows = [r for r in rows if r["city"].casefold() in {wanted, "nationwide"}]
    if args.status.lower() != "all":
        rows = [r for r in rows if r["status"].casefold() == args.status.casefold()]

    if not rows:
        print("No registry entries matched. Check city/status spelling.")
        return 1
    print("CITY        STATUS      TYPE             DEAL                                      SAVING / PRICE       RECHECK")
    print("----------- ----------- ---------------- ----------------------------------------- -------------------- ----------")
    for row in rows:
        print(f"{row['city'][:11]:11} {row['status'][:11]:11} {row['deal_type'][:16]:16} {row['title'][:41]:41} {row['price_or_saving_krw'][:20]:20} {row['expiry_or_recheck']}")
        if args.backups:
            print(f"  backup → {row['local_backup']}")
    print(f"\n{len(rows)} deal(s). Open the linked source and perform every live check before spending.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
