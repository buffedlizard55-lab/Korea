# 🔎 Deal Discovery System — Find More Without Chasing Fake Deals

This is the repeatable research system for finding **new** Korea savings opportunities before and during the trip. It is designed to catch deals that do not appear in English travel blogs, while refusing to call a changing or resident-only offer a tourist deal.

> **Last verified: 2026-08-03** · **Trip: Oct 31 – Nov 22, 2026**  
> **Important:** no one can truthfully guarantee that they have found “every last deal.” Promotions change daily, branch menus change, and some offers appear only inside Korean apps. The goal is stronger: systematically cover every realistic **source channel**, log every candidate, and make a live check before spending money.

**Use with:** [City Deal Checklist](city-deal-checklist.md) · [Verification Log](verification-log.md) · [Field Notes](field-notes.md) · [`data/deal-discovery-queue.csv`](../data/deal-discovery-queue.csv) · [`data/deals.csv`](../data/deals.csv)

---

## The discovery loop

1. **Search one channel** from the coverage map below using both English and Korean words.
2. **Add candidates** to `data/deal-discovery-queue.csv` with status `candidate` — even if they are not yet usable. Once verified, assign it a stable ID and promote it into `data/deals.csv` as `active` or `live-check`.
3. **Verify the actual terms:** official brand/government/platform page first; then two independent recent sources if no primary terms exist.
4. **Run the tourist filter:** no ARC/RRN/`본인인증`, no Korean domestic-card-only requirement, no resident companion, and no hidden mandatory subscription.
5. **Assign a city:** Seoul, Busan, chosen third city, nationwide, airport, or online-only. Confirm a real operating branch with an official locator or Naver Map.
6. **Publish only after proof:** source URL, access date, expiry, branch exclusions, price/minimum spend, redemption steps, and an honest confidence badge.
7. **Recheck before use:** a live coupon barcode, partner list, shelf tag, menu, or checkout screen always beats an old article.

A candidate that fails Step 4 is still useful: add it as **“resident-only — skip”** so nobody wastes time trying it.

---

## Coverage map: 18 places new deals hide

| # | Where to look | Korean searches / actions | Why it finds value | Tourist-safe test |
| --- | --- | --- | --- | --- |
| 1 | Official brand promotion pages | `브랜드명 이벤트`, `브랜드명 프로모션`, `브랜드명 매장찾기` | Launch, lunch, bundle and seasonal offers | Does it show dates, excluded stores, and payment conditions? |
| 2 | Official KakaoTalk channels | Search the brand, select the blue verified badge, open Coupons/Events | Short-term barcode and add-friend offers | Is the barcode visible, unexpired, and accepted at the chosen branch? |
| 3 | Convenience-store monthly catalogs | `CU 11월 행사`, `GS25 11월 1+1`, `세븐일레븐 11월 행사`, `이마트24 11월 행사` | Monthly 1+1/2+1 stock changes | Shelf tag + exact quantity wins; do not rely on a screenshot alone. |
| 4 | Department-store foreign visitor desks | `외국인 쿠폰`, `관광객 쿠폰`, ask `외국인 쿠폰 있나요?` | Visitor books and food-floor offers are often not advertised broadly | Ask about current booklet, passport rule, dates and restaurants. |
| 5 | Official tourist organizations | `visitseoul`, Visit Busan, Visit Korea, city tourism sites | City campaigns, passes, museum/attraction bundles | Check government/tourism organization dates and eligibility. |
| 6 | Travel platforms | Klook, KKday, Creatrip, Trazy; search exact restaurant + city | Foreign-card-friendly fixed-price vouchers | Compare final price, reservation time, branch, cancellation and inclusions. |
| 7 | Hotel and airline partner pages | `탑승권 할인`, hotel dining promotions | Boarding-pass, member and seasonal dining offers | Confirm the airline/hotel’s own partner list; expect name/boarding-pass checks. |
| 8 | Tourist payment products | WOWPASS app/site, card-linked offers | Cashback and partner promotions | Check the live merchant list, rate, cap, and payment method. |
| 9 | Official chain apps / web ordering | `앱 쿠폰`, `첫 주문`, `신규 가입` | App-only first-order and pickup discounts | Mark blocked if signup needs Korean SMS/`본인인증`; guest checkout must actually work. |
| 10 | Naver Map and Kakao Map | Search dish + neighborhood: `국밥 서면`, `백반 홍대`, `점심특선 강남` | Real local menu photos, recent prices, happy-hour/lunch signs | Favor recent reviews, posted menus, Korean-language regulars, and visible prices. |
| 11 | University / office districts | `대학가 맛집`, `직장인 점심`, `가성비` + neighborhood | Cheap daily menus and lunch sets | Treat as a price lead, not a coupon; check the physical menu. |
| 12 | Traditional markets | `전통시장`, `야시장`, market’s official page | Market events, coupons, local specialties | Ask price/portion/service fee first; avoid assuming famous market = cheapest. |
| 13 | Supermarkets and warehouse stores | `롯데마트 행사`, `이마트 행사`, `트레이더스 행사` | Multi-buy food/gift offers and permitted tax refunds | Verify membership requirement and tax-refund threshold; passport required for refund. |
| 14 | Cinema, museum, sport and attraction bundles | `패키지`, `제휴 할인`, `입장권 할인` | Food + entry, weekday, or transit bundles | Confirm foreign-card/payment and actual savings versus buying separately. |
| 15 | Festival / municipal calendars | `서울 행사 11월`, `부산 축제 11월`, third city + `행사` | Pop-ups, neighborhood festivals, free programming | Official date/location only; never count a prior-year event as current. |
| 16 | Local Korean deal communities | `뽐뿌`, `클리앙 알뜰구매`, `더쿠 핫딜`, `다사자` | Early warning for promotions and changed terms | **Lead only:** trace back to official terms before publishing. |
| 17 | Social media and short videos | `브랜드명 할인 2026`, `지역명 가성비`, creator posts | New openings and menu photos | Treat as unverified until date, branch, and terms are independently confirmed. |
| 18 | On-the-ground observation | Poster, kiosk banner, shelf tag, receipt, staff question | Some local deals are never posted online | Photograph/save the terms, expiry and branch; log it in Field Notes. |

---

## Search in a way local residents do

Use the **brand or neighborhood in Korean** and pair it with one intent word. These are discovery phrases, not guarantees:

| Goal | Useful Korean terms |
| --- | --- |
| Discount / coupon | `할인`, `쿠폰`, `행사`, `프로모션`, `혜택` |
| Buy-one-get-one / bundle | `1+1`, `2+1`, `세트`, `묶음`, `특가` |
| Value-for-money | `가성비`, `착한가격`, `저렴한`, `가성비 맛집` |
| Lunch / weekday | `점심특선`, `평일`, `런치`, `직장인 점심` |
| Refill / unlimited | `무한리필`, `리필`, `샐러드바` |
| Opening / temporary event | `오픈 이벤트`, `팝업`, `기간 한정` |
| Local food | `백반`, `국밥`, `분식`, `한식부페`, `시장` |
| Foreign visitor | `외국인`, `관광객`, `여권`, `면세` |

Example: search **`점심특선 서면`**, then open current Naver Map results, inspect menu photos and recent reviews, and add only a clearly priced candidate to the queue.

---

## Calendar: keep looking at the right time

| When | What to run | Output |
| --- | --- | --- |
| **Now / monthly** | Official chains, apps, platform listings, tourism organizations | Update or close candidates with an expiry/date. |
| **Sep 1 (D-60)** | Third-city selection, city tourism sites, hotels/airlines, city-pass math | A city-specific short list. |
| **Oct 1 (D-30)** | November convenience promos when published, autumn festival announcement, birthday setup | Planned deal list with sources. |
| **Oct 17 (D-14)** | Exact hotel neighborhoods, operating branches, delivery zones, platform reservations | Final Plan boxes in City Checklist. |
| **Oct 31–Nov 22 (daily)** | Kakao coupons, shelf tags, live menu, WOWPASS partners, weather/festival changes | Confirmed/Used marks and field notes. |
| **After the trip** | Receipts and field notes | Upgrade/reject leads so future travelers do not repeat mistakes. |

---

## Quality gates: do not add hype to the guide

A deal is **publishable** only when all applicable questions have an answer:

- [ ] What exactly is discounted or free, and what is the regular price?
- [ ] What is the start/end date, time window, quantity limit, and minimum spend?
- [ ] Which city and exact branch(es) participate?
- [ ] Is there an official source, or at least two recent independent sources?
- [ ] Can a US visitor pay/redeem without `본인인증`, an ARC, or a Korean card?
- [ ] Does it need a passport, a physical boarding pass, an app, or advance booking?
- [ ] Are there excluded branches, weekdays, menu items, or stacking restrictions?
- [ ] Is the claimed saving still better than the nearby normal local option?

If any answer is unknown, label it 🔴 **lead—verify in person/in app**, not a confirmed deal.

---

## The practical “never overpay” fallback

A coupon hunt should take **two minutes**, not an hour. If the deal fails its live check:

1. Search the dish in Naver Map in Korean.
2. Walk one block away from the major tourist corridor.
3. Choose a busy restaurant with a posted Korean menu and recent local reviews.
4. Compare the menu to one nearby alternative.
5. Use the normal walk-in price and move on.

That is often the same value strategy residents use: reliable local prices first, coupons only when they are genuinely available.
