# Contributing

This repo is our shared trip playbook. Rules to keep it trustworthy:

## Adding or changing a deal
1. **Source it or mark it.** Every deal needs either:
   - 🟢 a link to the brand/government's own page with the deal's terms, or
   - 🟡 two+ independent secondary sources with publication dates, or
   - 🔴 a clearly marked "unverified" badge (community rumor we still want to test).
2. **Date it.** Every entry owes a "last verified YYYY-MM-DD" line at the top of its doc.
3. **Terms over hype.** Quote the actual conditions (minimum spend, issue date, expiry,
   tier, marketing-consent gates). "Free burger" without conditions isn't a deal.
4. **Tourist-access badge.** Note whether a deal needs a Korean phone number (📱),
   resident status (🪪), or is plain tourist-friendly (✅).

## Removing deals
Don't delete directly — strike them through, add the reason and date, and move to the
end of the doc under "Retired". Losing track of *what died* is how we get fooled by stale
blog lists at the airport.

## Structure
- One markdown doc per category in `docs/` — keep tables readable, columns: Brand | Deal |
  Conditions | Validity | Trust | Access.
- Cross-link docs with the shared navigation bar (README · Cheat Sheet · Calendar · Neighborhoods · FAQ).
- New top-level pages to maintain: `docs/start-here.md` (beginner), `docs/checklist.md` (to-dos),
  `docs/arrival-guide.md`, `docs/money-guide.md`, `docs/phrasebook.md`, `docs/busan-guide.md`,
  `docs/cheat-sheet.md` (one-page summary), `docs/trip-calendar.md` (date-dependent deals),
  `docs/neighborhood-guide.md` (deals by area), `docs/field-notes.md` (in-trip log), `docs/faq.md`.
- Every chain deal should include a **Naver Map search link** (`https://map.naver.com/p/search/<Korean>`)
  so it's tap-to-navigate on the ground. Google Maps is unreliable in Korea.
- Put sources into `docs/verification-log.md`.
- Note material changes in `CHANGELOG.md`.

## Tooling
- Before pushing, run:
  - `python3 scripts/check_docs.py` — tables, internal links, "Last verified" stamps.
  - `python3 scripts/check_links.py` — external URLs (also runs weekly in CI via GitHub Actions).
  - `python3 scripts/check_registry.py` — core deal IDs, status, dates, and live-check safeguards.
  - `python3 scripts/check_source_confidence.py` — rejects aggregators/community sources mislabeled as official.
- New deals/broken links: use the GitHub issue templates (`.github/ISSUE_TEMPLATE/`).
- Track in-trip savings in `data/deal-tracker.csv` and upgrade badges via `docs/field-notes.md`.

## Nice-to-do later
- Jeju section (and deeper Busan) as the itinerary firms up
- In-trip receipts/photos that confirm a deal actually worked → upgrade 🔴/🟡 to 🟢
- A `deal-manage.csv` with cost per redeemed deal so we can see total savings → **started: `data/deal-tracker.csv`**
