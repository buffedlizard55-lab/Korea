#!/usr/bin/env python3
"""Prevent source-confidence drift in the normalized deal registry.

Checks data/deals.csv against data/source-policy.csv. It does not prove a page
is live; use check_links.py/web verification for that. It catches a different
failure: calling an aggregator, community page, or unknown source 'official'.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DEALS = ROOT / "data" / "deals.csv"
POLICY = ROOT / "data" / "source-policy.csv"
OFFICIAL_TIERS = {"official", "operator"}
ALLOWED_TIERS = {"official", "operator", "corroborated", "secondary", "community"}


def host_matches(host: str, suffix: str) -> bool:
    suffix = suffix.lower().lstrip(".").removeprefix("www.")
    return host == suffix or host.endswith("." + suffix)


def main() -> int:
    with POLICY.open(encoding="utf-8", newline="") as f:
        policy = list(csv.DictReader(f))
    with DEALS.open(encoding="utf-8", newline="") as f:
        deals = list(csv.DictReader(f))

    errors: list[str] = []
    warnings: list[str] = []
    official_count = 0
    for row in deals:
        deal_id = row["deal_id"]
        tier = row["source_tier"].strip().lower()
        host = urlsplit(row["source_url"]).netloc.lower().removeprefix("www.")
        matches = [p for p in policy if host_matches(host, p["domain_suffix"])]
        classifications = {p["classification"] for p in matches}
        if tier not in ALLOWED_TIERS:
            errors.append(f"{deal_id}: unsupported source_tier '{tier}'")
            continue
        if "aggregator" in classifications and tier in OFFICIAL_TIERS:
            errors.append(f"{deal_id}: {host} is an aggregator but tier is {tier}")
        if "secondary" in classifications and tier in OFFICIAL_TIERS:
            errors.append(f"{deal_id}: {host} is community/secondary but tier is {tier}")
        if tier == "official":
            official_count += 1
            if not ("official" in classifications):
                warnings.append(f"{deal_id}: official tier on unlisted domain {host}; add it to source-policy.csv after identity review")
        if tier == "operator" and not ("official" in classifications or "operator" in classifications):
            warnings.append(f"{deal_id}: operator tier on unlisted domain {host}; review operator ownership")
        if row["status"] == "active" and tier in {"secondary", "community"}:
            errors.append(f"{deal_id}: active deal cannot rely only on {tier} source")

    if errors:
        print("Source-confidence errors:")
        for error in errors:
            print(f"  ❌ {error}")
    for warning in warnings:
        print(f"  ⚠️  {warning}")
    if errors:
        return 1
    print(f"✅ Source-confidence check passed — {len(deals)} deals, {official_count} official-tier records, {len(warnings)} review warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
