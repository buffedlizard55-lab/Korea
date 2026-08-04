#!/usr/bin/env python3
"""Ensure every normalized core deal has a documented registry bridge.

This guards the migration boundary: a core data record cannot become orphaned,
and no mapping can point to a removed/incorrect registry ID or document.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEALS = ROOT / "data" / "deals.csv"
MAPPING = ROOT / "data" / "claim-mapping.csv"


def main() -> int:
    with DEALS.open(encoding="utf-8", newline="") as f:
        deal_ids = {row["deal_id"] for row in csv.DictReader(f)}
    with MAPPING.open(encoding="utf-8", newline="") as f:
        mappings = list(csv.DictReader(f))

    mapped = {row.get("deal_id", "") for row in mappings}
    issues: list[str] = []
    for deal_id in sorted(deal_ids - mapped):
        issues.append(f"{deal_id}: no document mapping")
    for row in mappings:
        deal_id = row.get("deal_id", "")
        document = row.get("document", "")
        if deal_id not in deal_ids:
            issues.append(f"{deal_id}: mapping references unknown registry ID")
            continue
        path = ROOT / document
        if not path.exists():
            issues.append(f"{deal_id}: mapped document missing: {document}")
        elif deal_id not in path.read_text(encoding="utf-8"):
            issues.append(f"{deal_id}: mapped document does not visibly reference its ID: {document}")
    if issues:
        print("Claim-coverage issues:")
        for issue in issues:
            print(f"  ❌ {issue}")
        return 1
    print(f"✅ Claim coverage passed — {len(deal_ids)} core registry IDs mapped across {len(mappings)} document references.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
