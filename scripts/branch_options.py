#!/usr/bin/env python3
"""Print hotel/branch-level options entered after booking accommodation."""
from __future__ import annotations
import argparse
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "data" / "branch-options.csv"

def main() -> int:
    p=argparse.ArgumentParser(description="List saved branch-level options by city.")
    p.add_argument('--city', default='all')
    args=p.parse_args()
    with PATH.open(encoding='utf-8', newline='') as f: rows=list(csv.DictReader(f))
    if args.city.lower()!='all': rows=[r for r in rows if r['city'].casefold()==args.city.casefold()]
    if not rows:
        print('No real branch options saved yet. Fill data/branch-options.csv after hotels are booked.')
        return 0
    for r in rows:
        print(f"{r['city']} / {r['neighborhood']} — {r['venue_name']} ({r['status']})")
        print(f"  Map: {r['naver_map_url']}\n  Check: {r['hours_last_checked']}\n  Notes: {r['notes']}")
    return 0
if __name__=='__main__': raise SystemExit(main())
