# Changelog

## 2026-08-03 — v3.3.0 City Deal Checklist & Current-Offer Guardrails
- **NEW `docs/city-deal-checklist.md`:** a markable, city-first checklist for Seoul and Busan, plus a safe fill-in workflow for the still-unnamed third city. Every row has Plan / Confirmed / Used boxes and distinguishes city-specific passes from nationwide systems.
- **Location audit:** added current official Dookki and Mom’s Touch store-finder sources and IKEA routing; confirmed that the guide should route users to a live branch finder rather than promise a specific branch or its hours months in advance.
- **Current-offer guardrails:** rotating KakaoTalk, travel-platform, delivery, WOWPASS, department-store and festival offers are now labeled live-only. The guide no longer treats a general channel, past promo, or future event as a guaranteed coupon; users must confirm barcode expiry, branch eligibility, price and terms on the day.
- **Workflow:** the master checklist and README now point to the city checklist; the verification log records the audit and exact safe-use rules.

## 2026-08-03 — v3.2.0 Field Trip Kit, Automation & Content Expansion
- **Field trip kit:**
  - **NEW `docs/checklist.md`** — master to-do checklist with pre-trip deadlines (D-30/D-15/D-1), in-trip daily routine, arrival/departure day tasks, and a fill-in **birthday schedule** table (IKEA D-7 coupon due dates).
  - **NEW `docs/arrival-guide.md`** — K-ETA status (**US citizens exempt through Dec 31, 2026**), ICN arrival steps (WOWPASS/T-money/eSIM, AREX, exchange), **self-service tax-refund kiosks at ICN T1/T2** (customs stamp first), first-meal options.
  - **NEW `docs/money-guide.md`** — payment methods (WOWPASS vs T-money vs cards), best exchange spots, price index, daily budgets, "never do" list.
  - **NEW `docs/phrasebook.md`** — 40 Korean phrases (kiosk, restaurant, market, delivery, tax refund, politeness) + deal-term glossary.
  - **NEW `docs/busan-guide.md`** — Busan cheap eats by area (Seomyeon, Haeundae/Gwangalli, Jagalchi/Gukje, student districts), dwaeji gukbap/milmyeon, chain branches, VBP food discounts recap.
  - **Naver Map tap-links** for every chain deal (new §11 in everyday-savings + links added to neighborhood guide rows) — Google Maps is unreliable in Korea.
  - **NEW `docs/field-notes.md`** + **`data/deal-tracker.csv`** — in-trip logging template & cost tracker (per CONTRIBUTING nice-to-dos).
- **Automation:**
  - **NEW `scripts/check_links.py`** — checks every external URL in the repo (bot-blocked hosts handled as warnings).
  - **NEW `scripts/check_docs.py`** — table integrity, internal links, "Last verified" date stamps (run locally: clean ✅).
  - **NEW `.github/workflows/link-check.yml`** — weekly Monday run + manual dispatch; opens/updates an issue on broken links. *(File is ready but pending the GitHub app's `workflows` permission to be pushed/activated.)*
  - **NEW GitHub issue templates** (broken link/deal changed, new deal) + **PR template** baking in CONTRIBUTING rules.
- **Content updates:** full KakaoTalk channel table (added Kyochon, Gong cha, Mega/Compose/Paik's with honest 🟡 "verify in-app" notes) in signup-welcome-deals; FAQ gained K-ETA, Naver Map, and tax-refund-kiosk Q&As; README index + How-to-Use expanded; verification log updated with new sources (K-ETA guides, ICN tax kiosks, Busan HapsKorea).

## 2026-08-03 — v3.1.0 Link Audit, TOS Verification & Beginner UX
- **Full link & TOS audit (all 60+ links re-checked 2026-08-03):**
  - **Fixed dead/hijacked links:** `koreasalefesta.co.kr` (hijacked → official `koreasalefesta.kr` + korea.kr gov source, noted offline between editions); IKEA's cited "TOS" article (wrong article → official birthday-coupon FAQ); dead Twosome FAQ (HTTP 500 → dasaja); dead Lotte English portal (`/en/main` → main site); "official" Discover Seoul Pass link was a coupon-aggregator → official `discoverseoulpass.com`.
  - **Sources read in full (TOS):** IKEA Family birthday FAQ (apple tart since 2025-10-17, emailed exactly D-7, marketing consent required), Dookki official (₩11,900, 90-min limit, ₩3,000 environmental fee, maratang), Starbucks KR rewards (welcome Americano next-day, Green-tier birthday drink), KFC KR membership (tier birthday coupons, 30-day validity, store-visit only, 본인인증 for level-up coupons), Outback membership (anniversary ₩10,000 premium-steak coupon = tomahawk/porterhouse only), Baemin App Store (₩10,000 first-order coupon) + DigitalToday (OS-language UI, foreign cards), WOWPASS (partner cashback list), Straits Times (Lotte Mart tax refund ≥₩15,000), iVisitKorea (Tongin hours).
- **Honesty corrections:**
  - **IKEA birthday apple tart may require ID** at the restaurant (per Korean guides) → re-ranked in README Quick Wins; free weekday hot drink + member prices highlighted as the zero-ID IKEA perks.
  - **Baemin:** English UI follows the phone OS language (no in-app toggle); full signup may need a Korean number → use Guest (`비회원`) ordering.
  - **Tongin Market:** dosirak hours differ by source → recommend 11:00–14:00.
  - **Outback:** Boomerang details updated to current official terms (anniversary coupon limited to tomahawk/porterhouse).
  - **Myeongryun Jinsa Galbi:** added solo-dining restrictions; **Ashley Queens:** added weekend price ₩27,900.
- **Beginner UX:**
  - **NEW `docs/start-here.md`** — 5-minute beginner's guide: the 2 rules (skip `본인인증`, passport stays in pocket), 3 deal types (🚶 walk-in / 📲 sign-up / 🎟️ platform), app setup, 6-word Korean glossary, first-48-hours plan, and "don't waste time" list.
  - **README:** Start Here added to How-to-Use + Guide Index; Quick Wins reordered (zero-ID deals first); WOWPASS cashback added to Quick Win #7.
  - **FAQ:** new Q&As (IKEA ID question, Baemin language setting, WOWPASS value, festival site status).
  - **Cheat sheet:** corrected IKEA row, Baemin OS-language note, Tongin hours note, WOWPASS step.
  - **Verification log:** new "Link Audit — 2026-08-03" section with ✅/🔧 status tables + expanded re-verification checklist.

## 2026-08-03 — v3.0.0 More Deals + User-Friendliness Overhaul
- **New Deals Added (all verified & sourced):**
  - **No Brand Burger (`노브랜드버거`):** Amazing Bulgogi burger **₩2,500** (launched Feb 2026; 70k sold week one — Shinsegae Food newsroom), grilled bulgogi ₩3,900, sets from ₩6,400; ~169 locations.
  - **Mom's Touch (`맘스터치`):** Full set (burger + Cajun fries + cola) **~₩7,600**; tourist-friendly branches (Myeongdong flagship, DDP, Gangnam Station, Hongdae).
  - **Gimbap Cheonguk (`김밥천국`)** rolls ₩2,500–4,000 + **Hong Kong Banjum (`홍콩반점0410`)** jjajangmyeon ₩7,000 (Myeongdong branch) — new "Budget Burger & Meal Chains" section.
  - **More KakaoTalk channels:** `@네네치킨` (Nene Chicken), `@BBQ치킨`, `@맘스터치` added across action plan, birthday, and welcome-deal docs.
  - **Myeongryun Jinsa Galbi:** upgraded to **600+ locations** + cheaper lunch specials (곤드레정식 + salad bar ₩7,000–8,000; galbi set ₩13,900); Dookki confirmed **₩11,900 on official site** with maratang/huoguo.
  - **Discover Seoul Pass:** July 1, 2026 expansion (79 free + 140 coupon partners incl. No Brand & Traders; SPAREX/Aquafield/Seoul Cruise free entry; Pick 3 rule change; eSIM on card pass).
  - **Visit Busan Pass:** concrete verified food discounts (Sulbing −10% Gwangbok, Mipochip −10% Haeundae, P.ARK Café ice cream).
  - **Free water:** Arisu refill stations in Seoul subway stations (year-round) — bring a refillable bottle.
  - **Calendar catches:** Tongin Market closed **Mon & 3rd Sunday → Sun Nov 15, 2026**; Nov 11 = Pepero Day (1+1 snack promos); Korea Sale Festa 2026 dates marked provisional (pattern: 2025 ran Oct 29 – Nov 16).
- **User-Friendliness Overhaul:**
  - **NEW `docs/cheat-sheet.md`** — one-page printable/screenshot summary of every deal + pre-flight 10-minute setup.
  - **NEW `docs/trip-calendar.md`** — day-by-day Oct 31 – Nov 22 calendar with promo resets, closures, and daily windows.
  - **NEW `docs/neighborhood-guide.md`** — deals mapped to Myeongdong, Jongno, Hongdae, Gangnam, Yeouido, Incheon, Busan.
  - **NEW `docs/faq.md`** — ID checks, phones/eSIMs, payment, tipping, water, tax refunds, timing.
  - **README overhaul:** "How to Use This Guide" 3-step path, expanded Guide Index, **Top 7 → Top 10 Quick Wins**, "What's New" section.
  - **Navigation bar added to every doc** (README · Cheat Sheet · Calendar · Neighborhoods · FAQ).
  - **Verification log expanded** with 13 new corroborated/official sources + 3 new unverified items + re-verification checklist additions.

## 2026-08-03 — v2.1.0 Exhaustive 12-Avenue Expansion for US Citizen Itinerary
- **12-Avenue Master Checklist:** Expanded `docs/us-tourist-action-plan.md` to include an exhaustive 12-avenue master checklist covering every possible tourist-accessible F&B savings channel in South Korea.
- **New Everyday Savings & Buffets Added:**
  - **All-You-Can-Eat (`무한리필`):** Added verified 2026 pricing and details for **Myeongryun Jinsa Galbi** (₩21,900 unlimited Korean BBQ), **Dookki** (₩11,900 unlimited tteokbokki/hot pot), and **Ashley Queens** (₩19,900 weekday lunch).
  - **Traditional Markets (`전통시장`):** Added full guide to **Tongin Market Brass Coin Lunchbox (`통인시장 엽전도시락`)** (₩10,000 for 20 coins + lunch tray) and documented why tourists should choose Mangwon Market over Gwangjang Market to avoid inflated prices.
  - **Hypermarket Immediate Tax Exemption (`즉시환급`):** Added rules for claiming instant ~6%–7% tax deduction at the register when spending ≥₩15,000 on edible gifts, snacks, tea, and packaged food at Lotte Mart (Seoul Station / Zettaplex) and E-Mart. (Noted as the only grocery/food avenue requiring physical passport at checkout).
  - **University District (`대학가`) Cheap Eats:** Added coverage of Hongdae, Sinchon, Hyehwa, and Anam student districts for 20%–30% lower meal prices and standing free rice/noodle refills (`밥/면 무한리필`).
- **New Tourist & Airport Promotions Added:**
  - **Airline Boarding Pass Discounts (`탑승권 할인`):** Documented Asiana Magic Boarding Pass and Korean Air Boarding Pass dining partner discounts (10%–20% off within 7 days to 1 month of arrival).
  - **Airport Buffet Lounges:** Documented free full-scale Korean buffet feasts at Incheon Airport **Matina Lounge (`마티나 라운지`)** and **Sky Hub Lounge (`스카이허브 라운지`)** via Priority Pass / DragonPass from US travel credit cards.
  - **Discover Seoul Pass / Visit Busan Pass:** Added F&B partner discount details (10%–20% off or free drinks at participating cafes and restaurants).
- **README Hub Enhancement:** Promoted the guide to feature the **Top 7 Quick Wins** across all 12 avenues.
- **Verification Log Updated:** Added primary/corroborated citations for Myeongryun Jinsa Galbi, Dookki, Tongin Market, Asiana Boarding Pass, Lotte Mart Tax Refund, and Priority Pass airport lounges.

## 2026-08-03 — v2.0.0 Customization for Oct 31 – Nov 22 US Citizen Itinerary
- **New Master Playbook:** Created `docs/us-tourist-action-plan.md` tailored for US citizens with multiple birthdays between Oct 31 and Nov 22, no Korean resident companion, and zero physical ID checks required.
- **`본인인증` (Identity Verification) Distinction:** Split birthday and welcome deals across `README.md`, `birthday-freebies.md`, and `signup-welcome-deals.md` into explicit tables: **US-Tourist Accessible (`✅`)** vs. **Resident-Only (`📱 본인인증` required)** so US citizens don't waste time on blocked native apps (Starbucks KR, Outback, CJ ONE, Happy Point).
- **Zero Physical ID Check Guarantee:** Documented that Korean cafes, restaurants, food halls, and kiosks (`키오스크`) never check passports or ID cards when scanning barcodes, email coupons, or e-vouchers. (ID is only checked for alcohol and tax refunds).
- **Customized D-30 Pre-Trip Timeline:**
  - September 30 (D-30): IKEA Family Korea email-only registration (auto-issues birthday dessert coupon D-7) & KakaoTalk installation.
  - October 15–20 (D-15): Adding official brand channels on KakaoTalk (`@버거킹`, `@KFC코리아`, `@롯데리아`, `@배스킨라빈스`, `@던킨`, `@파리바게뜨`) for instant combo coupons.
  - October 31 (Arrival) & November 1st: Documented that convenience store 1+1 / 2+1 promotions reset on the 1st of the month, giving travelers October's deals on arrival night and a brand-new November slate the next morning.
- **Autumn Seasonality Focus:** Highlighted **Korea Sale Festa 2026** (late Oct – mid Nov 2026) as the #1 autumn shopping/dining festival overlapping the trip dates; clarified that *Korea Grand Sale* is winter-only and ended in Feb 2026.
- **Delivery App Usability:** Focused `delivery-apps.md` on **Shuttle Delivery** (English, US cards, discounted Klook e-gift vouchers) and **Baemin Guest Checkout (`비회원 주문`)** (multi-language UI launched Feb 2026, foreign cards/Apple Pay).

## 2026-08-03 — Initial research sweep (v1.0.0)
- Built full guide structure (`docs/` with 5 category docs + verification log)
- Verified against official pages: Starbucks KR rewards, Outback Boomerang membership, KFC membership, Twosome FAQ, Klook Shuttle voucher, Korea Grand Sale (gov), Baemin App Store listing, Baemin multilingual launch news
- Corroborated secondaries: Banksalad (VIPS), 다사자 June/April 2026 guides, ARTART 2026 birthday roundup, Coupang Eats coupon aggregators, tourist delivery-app guides
- Key findings:
  - Outback retired its birthday coupon; Feb 2026 "My Anniversary" premium-steak coupon is the replacement
  - CGV free birthday combo downgraded to 50% off (2025)
  - Baemin became genuinely usable for tourists (EN UI Feb 2026, foreign cards, guest checkout)
  - Korea Grand Sale 2026 ran Dec 17 '25 – Feb 22 '26 (winter visitors only)
