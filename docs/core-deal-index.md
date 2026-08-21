# 🗃️ Core Deal Index — Registry IDs for the Main Claims

This page is the bridge while the guide completes its migration from scattered prose to one structured source of truth.

> **Last verified: 2026-08-21** · Coverage mapping: [`data/claim-mapping.csv`](../data/claim-mapping.csv) · Canonical fields (status, source, recheck date, ID requirement, live-check flag, backup): [`data/deals.csv`](../data/deals.csv)

## How to use it

- Read the city/food guides for explanation and Korean context.
- Use this index and `data/deals.csv` for the current **status**, source, recheck date, and fallback.
- If prose and registry ever disagree, treat the registry as controlling until the prose is corrected.

## Everyday food & shopping

| Registry ID | Deal | Status | Read with |
| --- | --- | --- | --- |
| `NATIONWIDE-DOOKKI` | Dookki unlimited tteokbokki | Active | [Everyday Savings](everyday-savings.md) |
| `NATIONWIDE-MYEONGRYUN` | Myeongryun Jinsa Galbi buffet | Live Check | [Everyday Savings](everyday-savings.md) |
| `NATIONWIDE-NOBRAND` | No Brand Burger Amazing Bulgogi | Live Check | [Everyday Savings](everyday-savings.md) |
| `NATIONWIDE-MOMSTOUCH` | Mom’s Touch value set | Live Check | [Everyday Savings](everyday-savings.md) |
| `NATIONWIDE-CONVENIENCE` | Monthly convenience-store 1+1 / 2+1 | Live Check | [Everyday Savings](everyday-savings.md) |
| `SEOUL-TONGIN` | Tongin Market coin lunchbox | Active | [Everyday Savings](everyday-savings.md) |
| `NATIONWIDE-TAXREFUND` | Immediate tax refund | Active | [Money Guide](money-guide.md) |

## Sign-up, delivery & payment

| Registry ID | Deal | Status | Read with |
| --- | --- | --- | --- |
| `NATIONWIDE-IKEA` | IKEA Family weekday drink/member price | Active | [Birthday Freebies](birthday-freebies.md) |
| `NATIONWIDE-KAKAO` | Official KakaoTalk brand-channel coupons | Live Check | [Welcome Deals](signup-welcome-deals.md) |
| `NATIONWIDE-SHUTTLE` | Shuttle `VK2026` credit | Active | [Delivery Apps](delivery-apps.md) |
| `NATIONWIDE-BAEMIN` | Baemin Guest Checkout | Live Check | [Delivery Apps](delivery-apps.md) |
| `NATIONWIDE-WOWPASS` | WOWPASS partner cashback | Live Check | [Money Guide](money-guide.md) |

## City-specific anchors

| City | Registry IDs | Read with |
| --- | --- | --- |
| Seoul | `SEOUL-TRANSIT-CLIMATE`, `SEOUL-PASS-DSP`, `SEOUL-TOUR-WALK`, `SEOUL-TOUR-CHEONGWADAE`, `SEOUL-TONGIN`, `SEOUL-MUSEUM-NMK`, `SEOUL-WARMEMO`, `SEOUL-FOLK` | [City Planning Board](city-planning-board.md) |
| Busan | `BUSAN-PAY`, `BUSAN-PASS-VBP`, `BUSAN-MUSEUM-ART`, `BUSAN-MUSEUM-MARITIME`, `BUSAN-MUSEUM-BOKCHEON`, `BUSAN-MUSEUM`, `BUSAN-MARINE-NHM`, `BUSAN-UNMCK` | [Busan Guide](busan-guide.md) |
| Cheonan | `CHEONAN-TAXI`, `CHEONAN-CITYTOUR`, `CHEONAN-INDEPENDENCE` | [City Research Hub](city-research-hub.md) |
| Daejeon | `DAEJEON-CITYTOUR`, `DAEJEON-HERITAGE`, `DAEJEON-SCIENCE`, `DAEJEON-DMA` | [City Research Hub](city-research-hub.md) |

## Maintenance rule

When adding a core deal, create its registry record first. Then add its ID to the relevant explanatory page and this index, plus `data/claim-mapping.csv`. Run `python3 scripts/check_claim_coverage.py`; it fails if a core record is orphaned, an ID is invalid, or a mapped page no longer visibly names the ID. This keeps prices/statuses/source confidence from drifting across the repo.

## Status-only / watch records

These records are intentionally kept in the registry so future/expired/rejected claims cannot drift back into ordinary recommendations.

| Registry ID | Current status | Where to read the rule |
| --- | --- | --- |
| `SEOUL-TOUR-TIGERBUS` | Active / live partner check | [City Research Hub](city-research-hub.md) |
| `SEOUL-SALEFESTA` | Future | [Deal Status Board](deal-status-board.md) |
| `DAEJEON-SUMMER50` | Expired for November trip dates | [Deal Status Board](deal-status-board.md) |
| `NATIONWIDE-TWOSOME` | Rejected | [Deal Status Board](deal-status-board.md) |

## Expanded food, payment & airport records

| Registry ID | Deal | Status | Read with |
| --- | --- | --- | --- |
| `NATIONWIDE-ASHLEY` | Ashley Queens weekday buffet | Live Check | [Everyday Savings](everyday-savings.md) |
| `NATIONWIDE-HKB` | Hong Kong Banjum jjajangmyeon | Live Check | [Everyday Savings](everyday-savings.md) |
| `NATIONWIDE-GIMBAP` | Gimbap Cheonguk budget meal | Live Check | [Everyday Savings](everyday-savings.md) |
| `NATIONWIDE-BUDGETCOFFEE` | Budget coffee chains | Live Check | [Everyday Savings](everyday-savings.md) |
| `SEOUL-HYUNDAI-DESK` | The Hyundai Seoul visitor desk | Live Check | [Tourist Promotions](tourist-promotions.md) |
| `INCHEON-LOUNGE` | Priority Pass lounge access | Live Check | [Arrival Guide](arrival-guide.md) |
| `SEOUL-ASIANA-BOARDING` | Asiana Magic Boarding Pass partners | Live Check | [Tourist Promotions](tourist-promotions.md) |
| `SEOUL-ARISU` | Arisu refill/water savings | Live Check | [Money Guide](money-guide.md) |

## Quality/quantity migration — newly structured records

| Registry ID | Deal | Status | Read with |
| --- | --- | --- | --- |
| `NATIONWIDE-ASHLEY` | Ashley Queens weekday buffet | Live Check | [Everyday Savings](everyday-savings.md) |
| `NATIONWIDE-HKB` | Hong Kong Banjum jjajangmyeon | Live Check | [Everyday Savings](everyday-savings.md) |
| `NATIONWIDE-GIMBAP` | Gimbap Cheonguk budget meal | Live Check | [Everyday Savings](everyday-savings.md) |
| `NATIONWIDE-BUDGETCOFFEE` | Budget coffee chains | Live Check | [Everyday Savings](everyday-savings.md) |
| `SEOUL-HYUNDAI-DESK` | The Hyundai Seoul visitor desk | Live Check | [Tourist Promotions](tourist-promotions.md) |
| `INCHEON-LOUNGE` | Priority Pass airport lounge access | Live Check | [Arrival Guide](arrival-guide.md) |
| `SEOUL-ASIANA-BOARDING` | Asiana Magic Boarding Pass partners | Live Check | [Tourist Promotions](tourist-promotions.md) |
| `SEOUL-ARISU` | Arisu refill/water savings | Live Check | [Money Guide](money-guide.md) |

## Final narrative-migration & value-score records

| Registry ID | Deal | Status | Read with |
| --- | --- | --- | --- |
| `SEOUL-DEPT-CLEARANCE` | Department-store evening clearance | Live Check | [Everyday Savings](everyday-savings.md) |
| `SEOUL-STUDENT-FOOD` | University-district local meals | Live Check | [Everyday Savings](everyday-savings.md) |
| `SEOUL-MANGWON` | Mangwon Market value food | Live Check | [Everyday Savings](everyday-savings.md) |
| `BUSAN-LOCAL-FOOD` | Busan local meal categories | Live Check | [Busan Guide](busan-guide.md) |
| `INCHEON-AIRPORT-MEAL` | Airport meal voucher/platform listing | Live Check | [Arrival Guide](arrival-guide.md) |
| `NATIONWIDE-PEPERO` | Pepero Day convenience offers | Future | [Trip Calendar](trip-calendar.md) |

## Final city-value expansion records

| Registry ID | Deal | Status | Read with |
| --- | --- | --- | --- |
| `SEOUL-DEPT-CLEARANCE` | Department-store evening clearance | Live Check | [Everyday Savings](everyday-savings.md) |
| `SEOUL-STUDENT-FOOD` | University-district local meals | Live Check | [Everyday Savings](everyday-savings.md) |
| `SEOUL-MANGWON` | Mangwon Market value food | Live Check | [Everyday Savings](everyday-savings.md) |
| `BUSAN-LOCAL-FOOD` | Busan local meal categories | Live Check | [Busan Guide](busan-guide.md) |
| `INCHEON-AIRPORT-MEAL` | Airport meal voucher/platform listing | Live Check | [Arrival Guide](arrival-guide.md) |
| `NATIONWIDE-PEPERO` | Pepero Day convenience offers | Future | [Trip Calendar](trip-calendar.md) |

## 2026-08-19 official Seoul/Busan expansion

Twenty new core records were promoted only after an official government, museum, or Korea Tourism Organization page was opened. Manual verification links are in [Verification Log](verification-log.md#official-seoulbusan-expansion--2026-08-19).

| Registry ID | Deal | Status | Read with |
| --- | --- | --- | --- |
| `SEOUL-MUSEUM-NMK` | National Museum of Korea permanent halls | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-WARMEMO` | War Memorial of Korea | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-FOLK` | National Folk Museum of Korea | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-PALACE-MUSEUM` | National Palace Museum of Korea | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-MUCH` | National Museum of Korean Contemporary History | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-GYEONGGYOJANG` | Gyeonggyojang historic house | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-CHEONGGYECHEON-MUSEUM` | Cheonggyecheon Museum | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-URI-SORI` | Seoul Museum of Korean Folk Music | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-MMCA-LATE` | MMCA Seoul late-hour free admission | Live Check | [City Research Hub](city-research-hub.md) |
| `BUSAN-MUSEUM` | Busan Museum | Active | [Busan Guide](busan-guide.md) |
| `BUSAN-MARINE-NHM` | Busan Marine Natural History Museum | Active | [Busan Guide](busan-guide.md) |
| `BUSAN-UNMCK` | UN Memorial Cemetery in Korea | Active | [Busan Guide](busan-guide.md) |
| `NATIONWIDE-VISITKOREA-EXCLUSIVE` | VISITKOREA Exclusive partner hub | Live Check | [Tourist Promotions](tourist-promotions.md) |
| `NATIONWIDE-SHINSEGAE-VK` | Shinsegae x VISITKOREA vouchers | Live Check | [Tourist Promotions](tourist-promotions.md) |
| `SEOUL-HYUNDAI-VK` | Hyundai x VISITKOREA visitor benefits | Live Check | [Tourist Promotions](tourist-promotions.md) |
| `NATIONWIDE-LOTTE-VK` | Lotte x VISITKOREA gift voucher | Live Check | [Tourist Promotions](tourist-promotions.md) |
| `SEOUL-GOLDENBLUE` | Golden Blue Marina VISITKOREA yacht offers | Live Check | [Tourist Promotions](tourist-promotions.md) |
| `NATIONWIDE-CATCHTABLE` | CATCHTABLE VISITKOREA restaurant offers | Live Check | [Tourist Promotions](tourist-promotions.md) |
| `NATIONWIDE-CULTUREDAY` | Culture Day every Wednesday | Live Check | [Tourist Promotions](tourist-promotions.md) |
| `SEOUL-AUTUMN-FEST` | 2026 Seoul Autumn Festival calendar | Future | [Deal Status Board](deal-status-board.md) |

## 2026-08-19 second official Seoul/Busan expansion

Twenty more records were promoted only after official city, museum, Visit Busan, or Korea Tourism Organization pages were opened. Manual links are in [Verification Log](verification-log.md#second-official-seoulbusan-expansion--2026-08-19).

| Registry ID | Deal | Status | Read with |
| --- | --- | --- | --- |
| `SEOUL-HANYANG-WALL` | Hanyangdoseong Museum | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-LIVING-HISTORY` | Seoul Living History Museum | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-DONGDAEMUN-HIST` | Dongdaemun History Museum and Sports Memorial | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-SEMA` | SeMA Seosomun regular admission | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-SEMA-BUK` | SeMA Buk-Seoul regular admission | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-SEMA-NAM` | SeMA Nam-Seoul admission | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-BAEKINJE` | Baek In-je House outdoor visit | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-DILKUSHA` | Dilkusha historic house | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-GONGPYEONG` | Gongpyeong Historic Site Museum | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-GUNGISI` | Gungisi Relics Exhibition Room | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-DONUIMUN` | Donuimun History Museum | Expired through 2026-12-31 | [Deal Status Board](deal-status-board.md) |
| `BUSAN-MODERN-HIST` | Busan Modern History Museum | Active | [Busan Guide](busan-guide.md) |
| `BUSAN-TEMP-CAPITAL` | Temporary Capital Memorial Hall | Active | [Busan Guide](busan-guide.md) |
| `BUSAN-FORCED-LABOR` | National Forced Mobilization Memorial | Live Check | [Busan Guide](busan-guide.md) |
| `BUSAN-NURIMARU` | Nurimaru APEC House | Active | [Busan Guide](busan-guide.md) |
| `BUSAN-ORYUKDO` | Oryukdo Skywalk | Active | [Busan Guide](busan-guide.md) |
| `BUSAN-SONGDO-WALK` | Songdo Cloud Walk | Active | [Busan Guide](busan-guide.md) |
| `BUSAN-CHEONGSAPO` | Cheongsapo Daritdol Observatory | Active | [Busan Guide](busan-guide.md) |
| `SEOUL-SHINSEGAE-DF` | Shinsegae Duty Free VISITKOREA offers | Live Check | [Tourist Promotions](tourist-promotions.md) |
| `SEOUL-COCORY` | COCORY COLOR 10% analysis | Live Check | [Tourist Promotions](tourist-promotions.md) |

## 2026-08-19 third official Seoul/Busan expansion

Twenty more records were promoted only after official city, museum, district, or operator visitor pages were opened. Manual links are in [Verification Log](verification-log.md#third-official-seoulbusan-expansion--2026-08-19).

| Registry ID | Deal | Status | Read with |
| --- | --- | --- | --- |
| `SEOUL-SEMA-PHOTO` | SeMA Museum of Photography | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-SEMA-NJP` | SeMA Nam June Paik House | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-SEMA-WEST` | SeMA Seoseoul Museum of Art | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-SEMA-ARCHIVE` | SeMA Art Archive regular admission | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-HISTORY` | Seoul Museum of History main building | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-URBAN-ARCH` | Seoul Hall of Urbanism and Architecture | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-CRAFT` | Seoul Museum of Craft Art | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-GYEONGHUIGUNG` | Gyeonghuigung Palace grounds | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-SEOSOMUN-SHRINE` | Seosomun Shrine History Museum | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-GUGAK` | National Gugak Center Gugak Museum | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-STARFIELD-LIB` | Starfield Library COEX | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-AVIATION` | National Aviation Museum exhibitions | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-BOK` | Bank of Korea Money Museum | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-SCIENCE` | Seoul Metropolitan Science Museum | Active | [City Research Hub](city-research-hub.md) |
| `SEOUL-LIBRARY` | Seoul Metropolitan Library on-site reading | Active | [City Research Hub](city-research-hub.md) |
| `BUSAN-UNPM` | UN Peace Memorial Hall | Active | [Busan Guide](busan-guide.md) |
| `BUSAN-FSM` | National Fisheries Science Museum | Active | [Busan Guide](busan-guide.md) |
| `BUSAN-CITIZEN-HIST` | Busan Citizens Park History Hall | Active | [Busan Guide](busan-guide.md) |
| `BUSAN-DONGNAE-HALL` | Dongnae Eupseong History Hall | Active | [Busan Guide](busan-guide.md) |
| `BUSAN-IMJIN` | Dongnae Eupseong Imjin War History Hall | Active | [Busan Guide](busan-guide.md) |


## Official Seoul/Busan expansion — 2026-08-21

Twenty additional records were promoted only after an official Seoul, national-museum, Busan, or Visit Busan page was opened. Each card links to the same manual-verification source recorded in `data/deals.csv`; Live Check means the official page confirms the mechanism but a session, renovation, or current notice still needs checking.

| Registry ID | Deal | Status | Manual verification |
| --- | --- | --- | --- |
| `SEOUL-CHILD-PARK` | Seoul Children's Grand Park free park and zoo admission | Active | [Official source ↗](https://parks.seoul.go.kr/parks/detailView.do?pIdx=26) |
| `SEOUL-BOTANIC-OUTDOOR` | Seoul Botanic Park outdoor zones | Active | [Official source ↗](https://culture.seoul.go.kr/night/sub/viewSpot/view.do?viewId=52&pageIndex=4&listType=list) |
| `SEOUL-PUREUN` | Pureun Arboretum free entry | Active | [Official source ↗](https://parks.seoul.go.kr/template/sub/pureun.do) |
| `SEOUL-ENERGY-DREAM` | Seoul Energy Dream Center free exhibitions | Active | [Official source ↗](https://energyinfo.seoul.go.kr/board/content?menu-id=Z110100&boardType=0001&boardNo=378) |
| `SEOUL-UPCYCLING` | Seoul Upcycling Plaza free self-guided visit | Active | [Official source ↗](https://mediahub.seoul.go.kr/archives/2016935) |
| `SEOUL-WATER-REUSE` | Seoul Water Recycling Experience Center | Live Check | [Official source ↗](https://mediahub.seoul.go.kr/archives/2018243) |
| `SEOUL-NMK-CHILD` | National Museum of Korea Children's Museum | Live Check | [Official source ↗](https://www.museum.go.kr/ENG/contents/E0103000000.do) |
| `SEOUL-HANBOK-GYEONGBOK` | Gyeongbokgung Palace hanbok free-admission rule | Active | [Official source ↗](https://royal.khs.go.kr/ENG/contents/E701000000.do) |
| `SEOUL-FUTURE-LAB` | Seoul Future Lab free technology experiences | Live Check | [Official source ↗](https://mediahub.seoul.go.kr/archives/2017699) |
| `SEOUL-GARDEN-SHOW-2026` | Seoul International Garden Show 2026 free admission | Active | [Official source ↗](https://mediahub.seoul.go.kr/archives/2018049) |
| `BUSAN-MOCA` | Museum of Contemporary Art Busan permanent admission | Active | [Official source ↗](https://www.visitbusan.net/en/index.do?menuCd=DOM_000000301001001000&uc_seq=1671&lang_cd=en) |
| `BUSAN-JEONGGWAN` | Jeonggwan Museum admission | Active | [Official source ↗](https://museum.busan.go.kr/jeonggwan/index) |
| `BUSAN-TONGSINSA` | History Museum of Joseon Tongsinsa admission | Active | [Official source ↗](https://www.visitbusan.net/en/index.do?menuCd=DOM_000000301001001000&uc_seq=269&lang_cd=en) |
| `BUSAN-SEOKDANG` | Seokdang Museum of Dong-A University admission | Active | [Official source ↗](https://www.visitbusan.net/en/index.do?menuCd=DOM_000000301001001000&uc_seq=274&lang_cd=en) |
| `BUSAN-TAEJOON` | Park Tae-joon Museum admission | Live Check | [Official source ↗](https://www.visitbusan.net/en/index.do?menuCd=DOM_000000301001001000&uc_seq=1709&lang_cd=en) |
| `BUSAN-MMCH-ANNEX` | Busan Modern and Contemporary History Museum Annex | Live Check | [Official source ↗](https://www.visitbusan.net/en/index.do?menuCd=DOM_000000301001001000&uc_seq=1444&lang_cd=en) |
| `BUSAN-GAMCHEON` | Gamcheon Culture Village free entry | Active | [Official source ↗](https://www.visitbusan.net/en/index.do?menuCd=DOM_000000303011001000&uc_seq=365&lang_cd=en) |
| `BUSAN-YONGDUSAN` | Yongdusan Park free grounds | Active | [Official source ↗](https://www.visitbusan.net/en/index.do?menuCd=DOM_000000301001001000&uc_seq=368&lang_cd=en) |
| `BUSAN-YONGGUNGSA` | Haedong Yonggungsa Temple free admission | Active | [Official source ↗](https://visitbusan.net/en/index.do?menuCd=DOM_000000303011001000&uc_seq=261&lang_cd=en) |
| `BUSAN-TAEJONGDAE` | Taejongdae Recreation Area free walking access | Active | [Official source ↗](https://www.visitbusan.net/en/index.do?menuCd=DOM_000000302002001000&uc_seq=1155&lang_cd=en) |

Use the source link and the registry note together: the note explains the exact free-entry rule, reservation step, paid exclusion, or closure risk that was actually found.
