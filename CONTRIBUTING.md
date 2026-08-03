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
- New top-level pages to maintain: `docs/cheat-sheet.md` (one-page summary), `docs/trip-calendar.md`
  (date-dependent deals), `docs/neighborhood-guide.md` (deals by area), `docs/faq.md` (common questions).
- Put sources into `docs/verification-log.md`.
- Note material changes in `CHANGELOG.md`.

## Nice-to-do later
- Jeju section (and deeper Busan) as the itinerary firms up
- In-trip receipts/photos that confirm a deal actually worked → upgrade 🔴/🟡 to 🟢
- A `deal-manage.csv` with cost per redeemed deal so we can see total savings
