# 🚦 Deal Status Board — What Can Be Used, Watched, or Ignored

This is the beginner-facing view of the registry’s status system. It prevents a past promotion, a future announcement, or a source with unknown terms from being treated as a usable trip deal.

> **Last verified: 2026-08-04** · Data source: [`data/deals.csv`](../data/deals.csv) · Quick filter: `python3 scripts/deal_registry.py --status active`

## Status meanings

| Status | What it means | What to do |
| --- | --- | --- |
| 🟣 **CANDIDATE** | A newly found lead not yet promoted into the core registry | Verify source, access, city/branch, terms, and expiry before using or promoting it. |
| 🟢 **ACTIVE** | A current program, standing benefit, or specific date-window offer with a source | Still perform its listed live check before spending. |
| 🔄 **LIVE CHECK** | The system/brand is real, but price, partner, stock, barcode, or branch changes frequently | Open the current app/site or ask the desk on the day. Do not budget it in advance. |
| 📅 **FUTURE** | Announced but not active yet | Put a recheck date on the calendar; do not buy/plan around it now. |
| ⛔ **EXPIRED** | The date window has ended | Keep only as historical evidence of a seasonal pattern. |
| 🚫 **REJECTED** | Not tourist-usable, did not meet source standards, or does not fit this trip | Do not spend time trying to claim it. |

## Current core view

### 🟢 Active — worth putting on a draft itinerary

- **Seoul:** Climate Card short-term passes; Seoul Guided Walking Tour; Tiger Bus same-day partner offer.
- **Busan:** free regular museum admissions; Visit Busan Pass and Busan Pay systems *(both require live partner/merchant checks)*.
- **Cheonan:** Tourism Taxi (through Dec. 31, first-come), City Tour, Independence Hall.
- **Daejeon:** City Tour (through Nov. 29), free heritage program (through Nov.), National Science Museum, DMA Collection Highlights (through Dec. 20).
- **Nationwide:** Shuttle `VK2026` ₩6,000 credit (through Dec. 31); immediate tax-refund system at qualifying stores.

### 🔄 Live check — useful only after opening the source

- Discover Seoul Pass attraction/partner list
- Visit Busan Pass pass type, price, attractions and restaurant partners
- Busan Pay merchant/cashback list
- Cheong Wa Dae entry/registration system
- Korea Sale Festa 2026 dates and partners
- KakaoTalk coupons, delivery banners, department-store booklets, and convenience-store monthly products

### 📅 Future / ⛔ expired / 🚫 rejected

| Deal | Status | Why |
| --- | --- | --- |
| Korea Sale Festa 2026 | 📅 Future | Official dates and partners are not published yet. Recheck in late September. |
| Daejeon 2026 summer 50% attraction tickets | ⛔ Expired for the trip | Use-by date is Oct. 31; it cannot cover November dates. |
| Resident app birthday benefits (Starbucks KR, Outback, KFC KR, CJ ONE, etc.) | 🚫 Rejected | Standard US tourists without ARC/`본인인증` cannot reliably claim them. |
| Dead Twosome FAQ benefit claim | 🚫 Rejected | Former source is dead; no current official terms captured. |

---

## Rules for adding or changing status

1. Shared lifecycle: `candidate → active` or `live-check → future / expired / rejected` as evidence and dates change. Candidates live in `data/deal-discovery-queue.csv`; core records live in `data/deals.csv`.
2. Every core deal requires a **stable deal ID**, source URL, source tier, city, access label, and recheck/expiry date in `data/deals.csv`.
3. **ACTIVE never means permanent.** It must retain `live_check=yes` in the registry.
4. When a date ends, change the status to **expired**—do not delete it or quietly leave it in beginner pages.
5. A live coupon stays **live-check** until its current barcode, branch, and expiry are visible.
6. Use **rejected** for resident-only deals and dead/unsupported claims. That is useful information because it stops wasted effort.

Run the validators after edits:

```bash
python3 scripts/check_registry.py
python3 scripts/check_discovery_queue.py
python3 scripts/check_staleness.py
```

`check_staleness.py` fails only when an Active/Live Check/Future/Candidate record has passed its recheck date; it warns when the date is within 14 days.
