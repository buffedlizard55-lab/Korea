# 🧭 Four-City Deal Research Hub — Seoul, Busan, Cheonan & Daejeon

This is the **research reference**, not the first page to plan from. Start with the [City Planning Board](city-planning-board.md), then use this hub only for the city you selected. Check the [Deal Status Board](deal-status-board.md) before treating any lead as usable.

> **Last verified: 2026-08-04** · **Assumption:** “chaenon” means **Cheonan (`천안`)**. If you meant Chuncheon (`춘천`) or another city, say so before using the Cheonan results.

## Use the fast refresh system

The source list lives in [`data/city-source-registry.csv`](../data/city-source-registry.csv). Run one command for a focused, short research board:

```bash
python3 scripts/deal_refresh.py --city Seoul
python3 scripts/deal_refresh.py --city Busan --format markdown
python3 scripts/deal_refresh.py --city Cheonan
python3 scripts/deal_refresh.py --city Daejeon
```

The script does **not** claim a coupon is live. It tells a researcher exactly which official pages to open and which terms to capture. Log the result in [`data/deal-discovery-queue.csv`](../data/deal-discovery-queue.csv), then promote a deal only after the [Discovery System](deal-discovery-system.md) quality gates are met.

---

## 1. Seoul — high-density value, city pass, visitor benefits

### Current confirmed routes

| Lead | Why it is worth checking | Current safe action |
| --- | --- | --- |
| **VISITKOREA Exclusive** | Official international-visitor partner feed: department stores, activities, shows, stays, dining/delivery | Filter to Seoul and open each live partner term; headline discounts are not universal. |
| **Discover Seoul Pass** | Free-entry, coupon and transport/eSIM bundle | Do pass math only with attractions you will actually use inside its activation window. [Official overview](https://english.visitseoul.net/tour-pass) |
| **Climate Card Short-Term Pass** | Unlimited eligible Seoul transit for short stays; foreign credit/debit cards are accepted at new vending machines | Current official short passes: 1/2/3/5/7 days = ₩5k/8k/10k/15k/20k. It activates when loaded; excludes airport/intercity buses and some rail. International-card purchases carry ~3.7% fee. [Official terms](https://english.seoul.go.kr/climate-cards-and-single-journey-transit-tickets-now-accepting-international-credit-cards-no-cash-needed/) |
| **Seoul City Tour Tiger Bus partner offers** | Same-day bus ticket can unlock partner discounts | 🟡 Operator site currently advertises same-day boarding-pass partner discounts, including **20% off Baby Shark The Experience through Dec. 19, 2026**. Check the live partner list before buying the bus ticket—the bus itself is only value if you will use its route. [Operator’s English site](https://en.seoulcitybus.com/) |
| **Seoul Guided Walking Tour** | Multilingual city volunteer guide at no guide charge | ✅ Reserve online **at least 3 days ahead**; palace/experience admission is separate and volunteer availability can limit slots. [Official current guide](https://english.visitseoul.net/walking-tour/General-Information/ENN015020) |
| **Cheong Wa Dae** | Free major Seoul attraction if it fits the route | 🔄 Admission is free, but **online reservation requires a Korean resident registration/ARC number and a Korean mobile number**, so ARC-less US tourists cannot pre-book. Foreigners can register **on-site** at the Main Gate or Chunchu Gate information desk (walk-up quota approx 2,000/day shared with 65+, disabled and veteran visitors) — **bring your passport**. **Closed Tuesdays** (open if Tuesday is a public holiday, closed the next day). [VISITKOREA](https://english.visitkorea.or.kr/svc/contents/infoHtmlView.do?vcontsId=136571) |
| **2026 Seoul Autumn Festival** | A live calendar for the exact trip window, Sept. 19–Nov. 29 | 🔄 204 performances/events are scheduled citywide; use the official calendar to pick free events and confirm ticketing rather than assuming all are free. [Official festival overview](https://english.seoul.go.kr/fun-seoul-a-365-day-festival-destination-elevating-seoul-as-a-global-cultural-hub/) |
| **Hangang Drone Light Show** | Free night-event option when a second-half date lines up | 🔄 Official city policy says it is free and runs first/second halves annually; check the actual date/location on the official show site. [Seoul official overview](https://english.seoul.go.kr/seoul-policy-archive/hangang-drone-light-show/) |
| **The Hyundai Seoul / department-store visitor desks** | Potential visitor booklet, food or shopping benefits | Ask the desk on arrival; use passport only if the current booklet requires it. |
| **Local-value search** | Student districts and lunch specials often beat coupon hunting | Naver Map: `점심특선 홍대`, `가성비 식당 성수`, `백반 종로`; use current menu photos and reviews. |

### Seoul search order
1. Compare Climate Card Short-Term Pass against your expected eligible rides; buy/load only on the first travel day.
2. Official VISITKOREA partners and DSP list.
3. Hotel-neighborhood Naver Map menus.
4. KakaoTalk brand coupons for a branch already on the day’s route.
5. Department-store desk only if already shopping nearby.

---

## 2. Busan — pass math, coast logistics, local-price meals

### Current confirmed routes

| Lead | Why it is worth checking | Current safe action |
| --- | --- | --- |
| **Visit Busan Pass** | Official scope: 40+ paid facilities and 150+ discount partners | Compare the live attractions/food partners and the exact selected pass price to your actual day. [Official guide](https://www.visitbusan.net/en/index.do?menuCd=DOM_000000303012007000) |
| **VISITKOREA Exclusive** | Includes Busan-specific experience partners such as Yacht Tale, plus nationwide partners | Open individual live terms before booking. |
| **Busan Pay** | Official foreign-visitor payment/local-currency route | ✅ Busan’s Jan. 2026 city guide says participating merchants offer 5–7% cashback, some QR payments add 3%, and affiliated businesses may add 3–10% pre-discounts; Visit Busan Pass purchases via it earn 5% cashback. 🔄 Merchant/rate/cap are live in app; malls/duty-free have no cashback. [Official terms](https://www.busan.go.kr/bige/daily-busan/view?dataNo=69959&curPage=2&bbsNo=10&srchCl=Daily+Busan) |
| **Free Busan museum cluster** | Indoor, no-entry-fee alternative to paid attractions | ✅ Busan Museum of Art (regular exhibitions), Bokcheon Museum, Busan Marine Natural History Museum, and National Maritime Museum permanent exhibitions are listed free. Check closures and special/4D paid exhibits. [Verified details below](#busan-free-culture-cluster) |
| **Local-value search** | Dwaeji gukbap, milmyeon, student lunch and market choices are more dependable than a short coupon | Naver Map: `돼지국밥 서면`, `밀면 부산역`, `점심특선 해운대`; compare menus and service charges. |

### Busan free-culture cluster

| Place | Area | Confirmed saving / caveat |
| --- | --- | --- |
| **Busan Museum of Art** | Haeundae / APEC-ro | Regular admission free; special exhibitions may charge. [VISITKOREA](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=91156) |
| **National Maritime Museum of Korea** | Yeongdo | Free admission; 4D theater and paid special exhibitions excluded. [Visit Busan](https://www.visitbusan.net/en/index.do?menuCd=DOM_000000301001001000&uc_seq=257&lang_cd=en) |
| **Bokcheon Museum** | Dongnae | Free; closed Mondays/New Year’s Day. [VISITKOREA](http://english.visitkorea.or.kr/enu/ATR/SI_EN_3_1_1_1.jsp?cid=1635387) |
| **Busan Marine Natural History Museum** | Dongnae | Free; closed Mondays/New Year’s Day (Tuesday closure if Monday is public holiday). [VISITKOREA](http://english.visitkorea.or.kr/enu/SI/SI_EN_3_1_1_1.jsp?cid=1251680) |

### Busan search order
1. Pass math for the day you want Haeundae/Songdo/attractions.
2. Check VBP partner list for nearby food—not the other way around.
3. Use neighborhood menu comparison for meals.
4. Check delivery only after entering the actual hotel address.

---

## 3. Cheonan (`천안`) — unusually strong official local transport value

### Current confirmed routes

| Lead | Terms found | Current safe action |
| --- | --- | --- |
| **2026 Cheonan Tourism Taxi** | Cheonan’s official tourism home advertises **50% off**; new details make it a real group-value option | 🟡 Secondary reports corroborate: non-Cheonan residents, first-come through **Dec. 31**; 4h costs **₩40,000** after subsidy (normal ₩80,000), 8h **₩80,000** (normal ₩160,000), plus ₩20,000/h. Reserve through the city platform and confirm the live eligibility/availability. [Official tourism home](https://www.cheonan.go.kr/tour.do) · [Yonhap reporting](https://www.yna.co.kr/view/AKR20260224042200063) |
| **Cheonan City Tour** | City-operated, explicitly for domestic and international visitors; adult fare **₩4,000**, youth/military ₩3,000, child/senior ₩2,000; 20+ group gets 50% off | Check the exact November route/date first. Attraction admission, meals and experiences are separate costs. [Official terms](https://cheonan.go.kr/tour/sub02_01_01.do) |
| **Independence Hall of Korea** | Major Cheonan history stop with no general admission charge | ✅ The official institution records free admission; budget only for transport and, if driving, parking (small car ₩2,000/day). [Official visitor information](https://i815.or.kr/2018/tour/info.do) |
| **November Culture-Heritage City Tour** | Cheonan’s official 2026 city-tour calendar includes a November heritage route | ✅ City-tour fare is ₩4,000 adult; official weekend-course page also lists free safety-experience and walnut-snack-making activities on relevant routes. Confirm the exact November route/date and capacity. [Official route page](http://www.cheonan.go.kr/tour/sub02_01_02_02.do) |
| **Local-value search** | City tour stops and station/terminal areas can be paired with low-cost meals | Naver Map: `천안 가성비 맛집`, `천안 점심특선`, `천안 빵집`; verify current menu/operating hours. |

### Cheonan search order
1. Verify the tourism-taxi 50% offer before setting the itinerary.
2. Check whether a city-tour date matches the group, then price direct transit versus the ₩4,000 tour.
3. Build food stops around the route rather than paying for separate cross-city taxis.

---

## 4. Daejeon — city tours and seasonal ticket releases

### Current confirmed routes

| Lead | Terms found | Current safe action |
| --- | --- | --- |
| **2026 Daejeon City Tour** | City source says it operates through **Nov. 29, 2026** and includes a bread-focused (`빵시투어`) route; booking is required | Check the November timetable, fare, seats and included/excluded costs. This can reduce repeated taxi rides between bakeries/attractions. [City notice](https://daejeon.go.kr/its/ItsdjNormalboardView.do?menuSeq=5931&boardSeq=3747&boardGubun=itsdj01&pageIndex=1) |
| **2026 Daejeon National-Heritage Program** | City-supported guided heritage walks/experiences that fit the trip window | ✅ **Free**; city says 15 sessions run through November. Check the session date, language and reservation before relying on it. [Official city notice](https://www.daejeon.go.kr/its/ItsdjNormalboardView.do?menuSeq=5929&boardSeq=3756&boardGubun=itsdj01&pageIndex=1) |
| **Daejeon Citizen Marathon Class** | Free, no-registration early-morning local fitness option through November | ✅ Official city notice says anyone can join by showing up; sessions run March–November at several parks/venues. It is practical only if the schedule/location suits the group. [Official notice](https://www.daejeon.go.kr/its/ItsdjNormalboardView.do?menuSeq=&boardSeq=3722&boardGubun=itsdj01&searchCondition=BAL_MAIN) |
| **Daejeon government tourism releases** | The city has run limited, first-come ticket discounts (including 50% attraction/experience offers) | Treat those as a monitored seasonal source—not a current November promise. The 2026 50% summer tickets expire Oct. 31 and should not be budgeted for later trip days. Check the official city tourism-news lane weekly. |
| **National Science Museum** | Big free base attraction near Expo/Yuseong; useful before paying for any add-on | ✅ Permanent halls, botanical garden, outdoor exhibits and children’s museum are free; planetarium/other listed exhibits are paid and Culture Day (last Wednesday) gives 50% off paid admissions. [Official visitor terms](https://www.science.go.kr/eps/cntnts/671/moveCntnts.do) |
| **Daejeon Museum of Art: `DMA Collection Highlights 2026`** | Current city exhibition, valid through Dec. 20 | ✅ Free admission for this specific 2026 collection exhibition; confirm hours/any special-exhibition fee separately. [Official city listing](https://daejeon.go.kr/dma/DmaExhibView.do?exType=01&menuSeq=6082&exSeq=106423&pageIndex=1) |
| **Currency Museum of Korea** | Free culture stop in the same Yuseong/science area | ✅ VISITKOREA says the nonprofit museum is free; closed Mondays and major holidays, so check day/hours. [VISITKOREA](https://english.visitkorea.or.kr/enu/ATR/SI_EN_3_1_1_1.jsp?cid=1664932) |
| **Local-value search** | Daejeon’s bakery routes and university/office areas reward route planning | Naver Map: `대전 빵시투어`, `대전 점심특선`, `대전 가성비 맛집`; compare walk-in menu price with packaged experiences. |

### Daejeon search order
1. Reserve city-tour/bread-route only after confirming the operating date.
2. Check Tour Pass Mall / city tourism news for a current event release.
3. Set a bakery route by geography; avoid taxi hopping across the city for one item at a time.

---

## Shared rule: how to keep each city manageable

For each city, use only this five-row daily card:

- [ ] One official city/tourism source
- [ ] One city pass or transport calculation (if applicable)
- [ ] One neighborhood menu search in Korean
- [ ] One live coupon/payment check
- [ ] One backup walk-in option with posted prices

That gives deep coverage without turning every day into coupon work. Add a new candidate only if it has a city, source, current date, terms and a realistic tourist redemption path.
