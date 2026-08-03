#!/usr/bin/env python3
"""Check every external URL in the repo's markdown files.

Usage:
    python3 scripts/check_links.py [--timeout SECONDS] [--parallel N]

Exit code 0 = all good (warnings allowed), 1 = at least one broken link.

Notes:
- Some sites block bots (403/429) — those hosts are in FLAKY_HOSTS and are
  reported as WARN instead of FAIL.
- GitHub Actions runs this weekly; see .github/workflows/link-check.yml.
"""

import argparse
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
URL_RE = re.compile(r"https?://[^\s)>\"'\]}]+")

# Hosts that return 403/429 to bots but are fine in a browser.
FLAKY_HOSTS = {
    "www.reddit.com", "reddit.com", "old.reddit.com",
    "www.tiktok.com", "namu.wiki", "en.namu.wiki",
    "apps.apple.com", "play.google.com",
    "www.7-eleven.co.kr", "gs25.gsretail.com",
    "www.diningcode.com", "mo.twosome.co.kr",
}


def extract_urls(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    urls = []
    for m in URL_RE.finditer(text):
        url = m.group(0).rstrip(".,;:!?")
        # strip trailing markdown/HTML punctuation handled above; also trim ) if unbalanced
        if url.endswith(")") and url.count(")") > url.count("("):
            url = url[:-1]
        urls.append(url)
    return urls


def check(url: str, timeout: int) -> tuple[str, str, str]:
    """Return (url, status, detail)."""
    host = urllib.parse.urlsplit(url).netloc.lower()
    host = host[4:] if host.startswith("www.") else host
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; KoreaDealsLinkCheck/1.0; +https://github.com/buffedlizard55-lab/Korea)",
            "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return url, "OK", str(resp.status)
    except urllib.error.HTTPError as e:
        if e.code in (403, 429) and host in FLAKY_HOSTS:
            return url, "WARN", f"{e.code} (bot-blocked host, verify manually)"
        return url, "FAIL", f"HTTP {e.code}"
    except urllib.error.URLError as e:
        reason = getattr(e, "reason", e)
        return url, "FAIL", f"network error: {reason}"
    except Exception as e:  # noqa: BLE001
        return url, "FAIL", f"error: {e}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--timeout", type=int, default=20)
    ap.add_argument("--parallel", type=int, default=8)
    args = ap.parse_args()

    md_files = sorted((ROOT / "docs").glob("*.md")) + sorted(ROOT.glob("*.md"))
    urls: dict[str, Path] = {}
    for f in md_files:
        for u in extract_urls(f):
            urls.setdefault(u, f)

    print(f"Checking {len(urls)} unique URLs from {len(md_files)} files...\n")
    results: dict[str, tuple[str, str]] = {}
    with ThreadPoolExecutor(max_workers=args.parallel) as ex:
        futs = {ex.submit(check, u, args.timeout): u for u in urls}
        for fut in as_completed(futs):
            u = futs[fut]
            results[u] = fut.result()[1:]

    failed = 0
    for u, (status, detail) in sorted(results.items()):
        src = urls[u]
        flag = {"OK": "✅", "WARN": "⚠️", "FAIL": "❌"}[status]
        print(f"{flag} [{status:4}] {detail:>12}  {u}  ({src.name})")
        if status == "FAIL":
            failed += 1

    print(f"\n{sum(1 for s, _ in results.values() if s == 'OK')} OK, "
          f"{sum(1 for s, _ in results.values() if s == 'WARN')} warnings, "
          f"{failed} broken.")
    return 1 if failed else 0


if __name__ == "__main__":
    import urllib.parse  # noqa: PLC0415
    sys.exit(main())
