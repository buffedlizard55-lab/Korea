#!/usr/bin/env python3
"""Run the reliable local verification suite in one command.

By default it checks documentation, registry integrity and source confidence.
Use --links only in an environment with outbound HTTPS; this sandbox's TLS
network limitation makes link results unavailable here, not necessarily broken.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKS = [
    ("Documentation", [sys.executable, "scripts/check_docs.py"]),
    ("Structure", [sys.executable, "scripts/check_structure.py"]),
    ("Deal registry", [sys.executable, "scripts/check_registry.py"]),
    ("Discovery queue", [sys.executable, "scripts/check_discovery_queue.py"]),
    ("Staleness", [sys.executable, "scripts/check_staleness.py"]),
    ("Claim coverage", [sys.executable, "scripts/check_claim_coverage.py"]),
    ("Source confidence", [sys.executable, "scripts/check_source_confidence.py"]),
]


def run(label: str, command: list[str]) -> bool:
    print(f"\n=== {label} ===")
    completed = subprocess.run(command, cwd=ROOT, check=False)
    return completed.returncode == 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Korea guide verification checks.")
    parser.add_argument("--links", action="store_true", help="also probe external URLs (requires working outbound HTTPS)")
    args = parser.parse_args()

    passed = all(run(label, command) for label, command in CHECKS)
    if args.links:
        passed = run("External links", [sys.executable, "scripts/check_links.py"]) and passed
    else:
        print("\n=== External links ===")
        print("SKIPPED. Run with --links only where outbound HTTPS works, or use the web verification workflow.")

    print("\n" + ("✅ Verification suite passed." if passed else "❌ Verification suite found an issue."))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
