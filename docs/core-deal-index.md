# 🗃️ Core Deal Index — Registry IDs for the Main Claims

This page is the bridge while the guide completes its migration from scattered prose to one structured source of truth.

> **Last verified: 2026-08-28** · Coverage mapping: [`data/claim-mapping.csv`](../data/claim-mapping.csv) · Canonical fields (status, source, recheck date, ID requirement, live-check flag, backup): [`data/deals.csv`](../data/deals.csv)

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


## Official Seoul/Busan expansion — 2026-08-21 second sweep

Twenty further records were promoted only after an official Seoul Tourism, Seoul museum, Busan city, or Visit Busan page was opened. Free dates, recurring free-entry rules, and permanent free admission are kept separate in the registry notes; Live Check means a closure, construction notice, current exhibition, or operator schedule must still be checked.

| Registry ID | Deal | Status | Manual verification |
| --- | --- | --- | --- |
| `SEOUL-BAEKJE-CHILDREN` | Seoul Baekje Children's Museum free admission | Live Check | [Official source ↗](https://english.visitseoul.net/attractions/SeoulBaekjeChildrensMuseum/ENPeenv2i) |
| `SEOUL-HORIM-LAST-THU` | Horim Museum last-Thursday free admission | Live Check | [Official source ↗](https://english.visitseoul.net/attractions/Horim-Museum-Sinsa-Main-Building/ENP005546) |
| `SEOUL-GYEOMJAE-FREE` | Gyeomjae Jeong Seon Art Museum free-admission days | Active | [Official source ↗](https://english.visitseoul.net/attractions/Gyeomjae-Jeong-Seon-Art-Museum/ENP001961) |
| `SEOUL-BEAUTIFUL-TEA` | Beautiful Tea Museum free gallery admission | Active | [Official source ↗](https://english.visitseoul.net/attractions/Beautiful-Tea-Museum/ENP004467) |
| `SEOUL-POLICE-MUSEUM` | Korean National Police Heritage Museum admission | Active | [Official source ↗](https://english.visitseoul.net/attractions/Korean-National-Police-Heritage-Museum/ENP020549) |
| `SEOUL-WATERWORKS` | Seoul Waterworks Museum free admission | Live Check | [Official source ↗](https://english.visitseoul.net/partners-en/seoultour-articles/Seouls-Museums-Getting-to-Know-Seoul_/33309) |
| `SEOUL-ELECTRICITY` | Electricity Museum free admission | Live Check | [Official source ↗](https://english.visitseoul.net/attractions/Electricity-Museum/ENP001958) |
| `SEOUL-SEMA-NAM-CHOSUKJIN` | SeMA Nam-Seoul: Cho Sook Jin free exhibition | Active | [Official source ↗](https://sema.seoul.go.kr/kr/whatson/exhibition/detail?exNo=1556711) |
| `SEOUL-SEMA-BUK-KWON` | SeMA Buk-Seoul: Kwon Byungjun free exhibition | Active | [Official source ↗](https://sema.seoul.go.kr/kr/whatson/exhibition/detail?exNo=1538201) |
| `SEOUL-BAEKJE-MUSEUM` | Seoul Baekje Museum free admission | Live Check | [Official source ↗](https://baekjemuseum.seoul.go.kr/eng/) |
| `BUSAN-SAMGWANGSA` | Samgwangsa Temple free admission | Active | [Official source ↗](https://visitbusan.net/en/index.do?menuCd=DOM_000000301001001000&uc_seq=347&lang_cd=en) |
| `BUSAN-GEUMJEONGSAN` | Geumjeongsan Mountain free access | Active | [Official source ↗](https://visitbusan.net/en/index.do?menuCd=DOM_000000301001001000&uc_seq=396&lang_cd=en) |
| `BUSAN-SEONAMSA` | Seonamsa Temple free admission | Active | [Official source ↗](https://www.visitbusan.net/en/index.do?menuCd=DOM_000000301001001000&uc_seq=458&lang_cd=en) |
| `BUSAN-UNSUSA` | Unsusa Temple free admission | Active | [Official source ↗](https://www.visitbusan.net/en/index.do?menuCd=DOM_000000301001001000&uc_seq=459&lang_cd=en) |
| `BUSAN-HWAMYEONG-ARBORETUM` | Hwamyeong Arboretum free admission | Active | [Official source ↗](https://www.visitbusan.net/en/index.do?menuCd=DOM_000000301001001000&uc_seq=457&lang_cd=en) |
| `BUSAN-NORTH-PORT-HALL` | Busan North Port Redevelopment Promotion Hall | Active | [Official source ↗](https://www.visitbusan.net/en/index.do?menuCd=DOM_000000301001001000&uc_seq=2082&lang_cd=en) |
| `BUSAN-BOKBYEONGSAN` | Bokbyeongsan Mountain Small Art Museum | Active | [Official source ↗](https://www.visitbusan.net/en/index.do?menuCd=DOM_000000302002001000&uc_seq=1401&lang_cd=en) |
| `BUSAN-MANGYANG-EXHIBIT` | Mangyang-ro Mountainside Road Exhibition Hall | Active | [Official source ↗](https://www.visitbusan.net/en/index.do?menuCd=DOM_000000302002001000&uc_seq=1401&lang_cd=en) |
| `BUSAN-HYUNDAI-MOTORSTUDIO` | Hyundai Motorstudio Busan free exhibition | Live Check | [Official source ↗](https://www.visitbusan.net/en/index.do?menuCd=DOM_000000301001001000&uc_seq=1322&lang_cd=en) |
| `BUSAN-HUINNYEOL` | Huinnyeoul Culture Village free public access | Active | [Official source ↗](https://visitbusan.net/en/index.do?menuCd=DOM_000000301001001000&uc_seq=255&lang_cd=en) |

The second sweep adds no unverified BOGO SKU or secondary-source claim. Use the source link and the registry note together.

## Seoul/Busan promotions, sign-up offers and free admissions — 2026-08-28 sweep

These 20 records were added after the official or operator page in the last column was opened on 2026-08-28. Free admission, discount percentages, promo codes and expiry dates below are quoted from that page; nothing here is inferred from a blog or an aggregator.

| Registry ID | Deal | Status | Manual verification |
| --- | --- | --- | --- |
| `SEOUL-PAINTERS-VK` | The Painters Gwanghwamun VISITKOREA 30% + welcome gift | Live Check | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?menuSn=607&vcontsId=1589587) |
| `SEOUL-JINYEON-VK` | Jinyeon Gugak performance VISITKOREA 20% + free pouch | Live Check | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?menuSn=607&vcontsId=1589738) |
| `SEOUL-RAKKOJAE-VK` | Rakkojae Bukchon hanok stay VISITKOREA 10% code | Live Check | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?menuSn=607&vcontsId=1589688) |
| `SEOUL-WEHOME-VK` | Wehome VISITKOREA 5% code and free airport welcome | Live Check | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?menuSn=607&vcontsId=1589636) |
| `SEOUL-MOTORSTUDIO-LOUNGE-VK` | Hyundai Motorstudio Seoul VISITKOREA club lounge benefit | Live Check | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?menuSn=607&vcontsId=1590710) |
| `SEOUL-HANBOK-PALACES-OTHER` | Hanbok free admission at Changdeokgung, Deoksugung, Changgyeonggung | Active | [Open source ↗](https://royal.khs.go.kr/ENG/contents/E701000000.do) |
| `SEOUL-PALACE-AGE-FREE` | Palace free admission for foreign visitors 18 and under or 65 and over | Active | [Open source ↗](https://royal.khs.go.kr/ROYAL/contents/R703000000.do) |
| `SEOUL-PALACE-LASTWED-FREE` | Palace free admission on Culture Day (last Wednesday per palace page) | Live Check | [Open source ↗](https://royal.khs.go.kr/ROYAL/contents/R703000000.do) |
| `SEOUL-UNHYEONGUNG-FREE` | Unhyeongung Palace grounds admission | Active | [Open source ↗](https://english.visitseoul.net/attractions/unhyeongungpalace_/478) |
| `SEOUL-NAMSANGOL-FREE` | Namsangol Hanok Village free entry and free permanent guided tours | Active | [Open source ↗](https://english.visitseoul.net/walking-tour/General-Information/ENN015020) |
| `SEOUL-LOTTE-TOURIST-MEMBERSHIP` | Lotte Tourist Membership Card sign-up benefits | Live Check | [Open source ↗](https://global.lotteshopping.com/eng/main) |
| `SEOUL-CITYBUS-SHILLA-DF` | Shilla Duty Free benefit with Seoul City Tour Bus ticket | Live Check | [Open source ↗](https://www.seoulcitybus.com/en/discounts) |
| `SEOUL-CITYBUS-LUGGAGELESS` | Luggage Less storage discount with Seoul City Tour Bus ticket | Live Check | [Open source ↗](https://www.seoulcitybus.com/en/discounts) |
| `SEOUL-CITYBUS-MOMSTOUCH-NAMSAN` | Mom's Touch N Seoul Tower 10% off with bus ticket | Live Check | [Open source ↗](https://www.seoulcitybus.com/en/discounts) |
| `BUSAN-YACHTTALE-VK` | Yacht Tale Busan VISITKOREA booking discount | Live Check | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?menuSn=607&vcontsId=1589743) |
| `BUSAN-VBP-REVISIT` | Visit Busan Pass re-visit reward promotion | Live Check | [Open source ↗](https://www.visitbusanpass.com/reVisitBusanPass) |
| `BUSAN-CITYTOUR-SEALIFE` | SEA LIFE Busan Aquarium discount with Busan City Tour ticket | Live Check | [Open source ↗](https://www.citytourbusan.com/en2/04discount/02.php) |
| `BUSAN-CITYTOUR-XTHESKY` | Busan X-the-Sky observatory 25% off with Busan City Tour ticket | Live Check | [Open source ↗](https://www.citytourbusan.com/en2/04discount/02.php) |
| `BUSAN-CITYTOUR-ARTE-MUSEUM` | Arte Museum Busan discounted admission with Busan City Tour ticket | Live Check | [Open source ↗](https://www.citytourbusan.com/en2/04discount/02.php) |
| `BUSAN-CITYTOUR-BOKSOONDOGA` | Boksoondoga makgeolli 50% off with Busan City Tour ticket | Live Check | [Open source ↗](https://www.citytourbusan.com/en2/04discount/02.php) |

Every record keeps a live check: promo codes are entered at booking, coupon barcodes are downloaded on the day, and the two city-tour partner pages gate their discounts on a same-day boarding ticket.

## Official Seoul/Busan free parks, beaches and venues — 2026-08-28 second sweep

Twenty more records were added only after the official Visit Seoul or Visit Busan page in the last column was opened. Parks and beaches are free-admission deals, not coupons. Cable cars, paid museums inside parks, parking, and out-of-season fountain shows are excluded in the notes.

| Registry ID | Deal | Status | Manual verification |
| --- | --- | --- | --- |
| `SEOUL-LEEUM-M1-FREE` | Leeum Museum of Art M1 permanent collection | Active | [Open source ↗](https://english.visitseoul.net/attractions/Leeum-Samsung-Museum-of-Art/ENP001232) |
| `SEOUL-LEEUM-GUIDE-FREE` | Leeum digital guide free rental with passport | Active | [Open source ↗](https://english.visitseoul.net/attractions/Leeum-Samsung-Museum-of-Art/ENP001232) |
| `SEOUL-SARANGCHAE-FREE` | Cheongwadae Sarangchae | Active | [Open source ↗](https://english.visitseoul.net/attractions/Cheongwadae-Sarangchae/ENP006007) |
| `SEOUL-NFM-CHILD` | National Folk Museum Children's Folk Museum | Live Check | [Open source ↗](https://english.visitseoul.net/attractions/childrens-folk-museum_/5132) |
| `SEOUL-NAKSAN-PARK` | Naksan Park and city-wall trail | Active | [Open source ↗](https://english.visitseoul.net/dongdaemunarea/Naksan-Park_/3702) |
| `SEOUL-GWANGHWAMUN-SQUARE` | Gwanghwamun Square | Active | [Open source ↗](https://english.visitseoul.net/attractions/Gwanghwamun-Square/ENP001899) |
| `SEOUL-OLYMPIC-PARK` | Olympic Park grounds and sculpture park | Active | [Open source ↗](https://english.visitseoul.net/nature/Olympic-Park/ENP002139) |
| `SEOUL-BUKHANSAN` | Bukhansan National Park trail access | Live Check | [Open source ↗](https://english.visitseoul.net/attractions/BukhansanNationalPark_/371) |
| `SEOUL-CHEONGGYE-SOUL-OCEAN` | Cheonggye Soul Ocean free nighttime media art | Active | [Open source ↗](https://english.visitseoul.net/exhibition/CheonggyeSoulOcean/ENP20kefn) |
| `SEOUL-YEOUIDO-HANGANG` | Yeouido Hangang Park | Active | [Open source ↗](https://english.visitseoul.net/nature/Yeouido-Hangang-Park-Girls%E2%80%99-Generation-Forest/ENP012993) |
| `SEOUL-HANGANG-ART` | Hangang Art Park outdoor artworks | Active | [Open source ↗](https://english.visitseoul.net/other/Hangang-Art-Park/ENP035118) |
| `SEOUL-MAEHEON-FOREST` | Maeheon Citizens Forest | Active | [Open source ↗](https://english.visitseoul.net/attractions/yangjaecitizensforest_/2160) |
| `SEOUL-SEOUL-FOREST` | Seoul Forest park | Active | [Open source ↗](https://english.visitseoul.net/nature/Seoul-Forest/ENP001838) |
| `BUSAN-HAEUNDAE-BEACH` | Haeundae Beach | Active | [Open source ↗](https://visitbusan.net/index.do?lang_cd=en&menuCd=DOM_000000301001001000&uc_seq=373) |
| `BUSAN-DADAEP-BEACH` | Dadaepo Beach | Active | [Open source ↗](https://visitbusan.net/index.do?menuCd=DOM_000000301001001000&uc_seq=366&lang_cd=en) |
| `BUSAN-SONGDO-BEACH` | Songdo Beach shoreline | Active | [Open source ↗](https://visitbusan.net/index.do?lang_cd=en&menuCd=DOM_000000301001001000&uc_seq=286) |
| `BUSAN-IGIDAE` | Igidae Coastal Trail | Active | [Open source ↗](https://www.visitbusan.net/en/index.do?menuCd=DOM_000000302002001000&uc_seq=323&lang_cd=en) |
| `BUSAN-AMNAM-PARK` | Amnam Park and Songdo Coast Bollegil Trail | Active | [Open source ↗](https://www.visitbusan.net/en/index.do?menuCd=DOM_000000301001001000&uc_seq=326&lang_cd=en) |
| `BUSAN-HWAMYEONG-ECO` | Hwamyeong Eco Park | Active | [Open source ↗](https://www.visitbusan.net/en/index.do?menuCd=DOM_000000302008001000&uc_seq=1157&lang_cd=en) |
| `BUSAN-DADAEP-PARK` | Dadaepo Beach Park | Active | [Open source ↗](https://www.visitbusan.net/index.do?menuCd=DOM_000000301001001000&uc_seq=1718&lang_cd=en) |

## Seoul/Busan city-tour partner discounts — 2026-08-28 third sweep

Twenty promotional discounts copied from the official Seoul City Tour Bus and Busan City Tour affiliate pages. All require a **same-day boarding ticket** (Seoul) or BUTI bracelet shown **before purchase** (Busan). Night-view Busan tours are excluded. These are not walk-in coupons.

| Registry ID | Deal | Status | Manual verification |
| --- | --- | --- | --- |
| `SEOUL-CITYBUS-BABYSHARK` | Baby Shark The Experience 20 percent off | Live Check | [Open source ↗](https://www.seoulcitybus.com/en/discounts) |
| `SEOUL-CITYBUS-STARFIELD-25` | Starfield Avenue Gran Seoul up to 25 percent off | Live Check | [Open source ↗](https://www.seoulcitybus.com/en/discounts) |
| `SEOUL-CITYBUS-STARFIELD-GIFT` | Starfield free WAKEMAKE cushion at 100000 won | Live Check | [Open source ↗](https://www.seoulcitybus.com/en/discounts) |
| `SEOUL-CITYBUS-8SECONDS` | 8Seconds extra 5 percent off | Live Check | [Open source ↗](https://www.seoulcitybus.com/en/discounts) |
| `SEOUL-CITYBUS-RAINREPORT` | Rainreport 10 percent off menu | Live Check | [Open source ↗](https://www.seoulcitybus.com/en/discounts) |
| `SEOUL-CITYBUS-YESEYESEE` | YESEYESEE extra 10 percent off | Live Check | [Open source ↗](https://www.seoulcitybus.com/en/discounts) |
| `SEOUL-CITYBUS-OFFBEAUTY` | Off-beauty free Bless Moon trial kit | Live Check | [Open source ↗](https://www.seoulcitybus.com/en/discounts) |
| `SEOUL-CITYBUS-MLB` | MLB Hannam Flagship 10 percent off | Live Check | [Open source ↗](https://www.seoulcitybus.com/en/discounts) |
| `SEOUL-CITYBUS-OWLS` | Owl's Cutlet N Seoul Tower 10 percent off | Live Check | [Open source ↗](https://www.seoulcitybus.com/en/discounts) |
| `SEOUL-CITYBUS-GWANHO` | Gwanho lamb 10 percent off | Live Check | [Open source ↗](https://www.seoulcitybus.com/en/discounts) |
| `SEOUL-CITYBUS-GANGA` | Ganga Mugyo 15 percent off | Live Check | [Open source ↗](https://www.seoulcitybus.com/en/discounts) |
| `SEOUL-CITYBUS-ZAMSHH` | ZAMSHH 10 percent off | Live Check | [Open source ↗](https://www.seoulcitybus.com/en/discounts) |
| `SEOUL-CITYBUS-HANSANG` | Gwanghwamun Hansang 10 percent off | Live Check | [Open source ↗](https://www.seoulcitybus.com/en/discounts) |
| `SEOUL-CITYBUS-LUMIERES` | Theatre des Lumieres 20 percent off on-site | Live Check | [Open source ↗](https://www.seoulcitybus.com/en/discounts) |
| `BUSAN-CITYTOUR-RYAN` | Ryan Holiday in Busan 30 percent off | Live Check | [Open source ↗](https://www.citytourbusan.com/en2/04discount/02.php) |
| `BUSAN-CITYTOUR-KIDZANIA` | Kidzania Busan 20-30 percent off | Live Check | [Open source ↗](https://www.citytourbusan.com/en2/04discount/02.php) |
| `BUSAN-CITYTOUR-RYUS` | Ryu's coffee bar 10 percent off | Live Check | [Open source ↗](https://www.citytourbusan.com/en2/04discount/02.php) |
| `BUSAN-CITYTOUR-KPOP` | K-pop World Champion free drink at 20000 won | Live Check | [Open source ↗](https://www.citytourbusan.com/en2/04discount/02.php) |
| `BUSAN-CITYTOUR-COFFEEVOICE` | Coffee Voice 10 percent off drinks | Live Check | [Open source ↗](https://www.citytourbusan.com/en2/04discount/02.php) |
| `BUSAN-CITYTOUR-CASABUSANO` | Casabusano 10 percent drinks / 5 percent bakery | Live Check | [Open source ↗](https://www.citytourbusan.com/en2/04discount/02.php) |

## Seoul/Busan KTO free-admission sites — 2026-08-28 fourth sweep

Twenty public parks, trails, temples, and KTO visitor halls whose official VISITKOREA destination pages list **Fees: Free**. Cable cars, prison museum, Some Sevit, and paid programs are excluded.

| Registry ID | Deal | Status | Manual verification |
| --- | --- | --- | --- |
| `SEOUL-SEOULLO-7017` | Seoullo 7017 sky garden | Active | [Open source ↗](https://english.visitkorea.or.kr/enu/ATR/SI_EN_3_6.jsp?cid=2829579) |
| `SEOUL-WORLD-CUP-PARK` | World Cup Park cluster | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=107540) |
| `SEOUL-NAMSAN-PARK` | Namsan Park grounds | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=110622) |
| `SEOUL-TAPGOL-PARK` | Tapgol Park | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=104563) |
| `SEOUL-TTUKSEOM-HANGANG` | Ttukseom Hangang Park | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=90908) |
| `SEOUL-BANPO-SEORAESEOM` | Banpo Seoraeseom Island | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=81505&menuSn=351) |
| `SEOUL-BUKCHON-CULTURAL` | Bukchon Cultural Center | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=97933) |
| `SEOUL-INDEPENDENCE-PARK` | Seodaemun Independence Park grounds | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=81455) |
| `SEOUL-MONTMARTRE-PARK` | Montmartre Park Seocho | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=69718&menuSn=351) |
| `SEOUL-JINGWANSA` | Jingwansa Temple | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=89135) |
| `SEOUL-HIKR-GROUND` | HiKR Ground | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/sp/hikr) |
| `SEOUL-GUARD-CHANGE` | Royal Guard Changing Ceremony | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=104589) |
| `SEOUL-CHEONGGYE-BOOKS` | Cheonggyecheon Old Books Street | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=186516) |
| `SEOUL-SSAMZIGIL` | Ssamzigil Insadong | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=44678) |
| `BUSAN-GWANGALLI-BEACH` | Gwangalli Beach | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=111074) |
| `BUSAN-MILLAK-PARK` | Millak Waterfront Park | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=84959) |
| `BUSAN-DONGBAEKSEOM` | Dongbaekseom Island trail | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=81541) |
| `BUSAN-NAKONG-ECO` | Nakdong Estuary Eco-Center | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=91004) |
| `BUSAN-GEUMGANG-PARK` | Geumgang Park grounds | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=86363) |
| `BUSAN-DALMAJI` | Dalmaji Road | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=112002) |

## Seoul/Busan KTO free sites — 2026-08-28 fifth sweep (50)

Fifty Hangang parks, temples, plazas, and trails whose official VISITKOREA or Visit Seoul/Visit Busan pages list Fees: Free or Service Fees Free. Paid add-ons (cable, skating, Ahopsan Forest, cinema tickets) are excluded.

| Registry ID | Deal | Status | Manual verification |
| --- | --- | --- | --- |
| `SEOUL-MANGWON-HANGANG` | Mangwon Hangang Park free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?menuSn=351&vcontsId=91202) |
| `SEOUL-JAMWON-HANGANG` | Jamwon Hangang Park free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=91930) |
| `SEOUL-JAMSIL-HANGANG` | Jamsil Hangang Park free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?menuSn=351&vcontsId=91632) |
| `SEOUL-ICHON-HANGANG` | Ichon Hangang Park free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=91800) |
| `SEOUL-YANGHWA-HANGANG` | Yanghwa Hangang Park free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=91221) |
| `SEOUL-GWANGNARU-HANGANG` | Gwangnaru Hangang Park free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=80362&menuSn=351) |
| `SEOUL-BANPO-HANGANG` | Banpo Hangang Park free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=91983) |
| `SEOUL-HANYANG-TRAIL` | Hanyangdoseong city-wall trail free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=136593) |
| `SEOUL-SEONYUDO` | Seonyudo Park free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=175826) |
| `SEOUL-NODEUL` | Nodeul Island free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=34334) |
| `SEOUL-YEOUIDO-PARK` | Yeouido Park inland lawn free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=110577) |
| `SEOUL-JEONGDONG-OBS` | Jeongdong Observatory free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=69685) |
| `SEOUL-NAMSAN-BOTANIC` | Namsan Outdoor Botanical Garden free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=80961) |
| `SEOUL-INWANGSAN` | Inwangsan Mountain trail free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=85681) |
| `SEOUL-BUGAKSAN` | Bugaksan Mountain trail free admission | Live-Check | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=90662) |
| `SEOUL-DOBONGSAN` | Dobongsan Mountain trail free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=80867) |
| `SEOUL-PALGAKJEONG` | Bugak Skyway Palgakjeong Pavilion free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=76679) |
| `SEOUL-DONGDAEMUN-PARK` | Dongdaemun History and Culture Park grounds free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=75906&menuSn=351) |
| `SEOUL-DDP-PLAZA` | Dongdaemun Design Plaza grounds free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=67162) |
| `SEOUL-SCIENCE-PARK` | Seoul Science Park education campus free admission | Live-Check | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=81476&menuSn=351) |
| `SEOUL-HYOCHANG` | Hyochang Park free admission | Active | [Open source ↗](https://english.visitseoul.net/nature/Hyochang-Park_/39738) |
| `SEOUL-INWANG-SHELTER` | Inwangsan Shelter in the Woods free admission | Active | [Open source ↗](https://english.visitseoul.net/area/2024-iwsshelter/ENPqsaooa) |
| `SEOUL-HANGANG-PLAY` | Hangang Play Place Ttukseom free general admission | Active | [Open source ↗](https://english.visitseoul.net/area/HangangPlayPlace/ENPqb6ctu) |
| `SEOUL-SEOSOMUN-PARK` | Seosomun Historical Park grounds free admission | Active | [Open source ↗](https://english.visitseoul.net/attractions/seosomun-historical-park_/30157) |
| `SEOUL-YONGSAN-FAMILY` | Yongsan Family Park free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/enu/ATR/SI_EN_3_6.jsp?cid=2514566) |
| `SEOUL-BUDDHIST-MUSEUM` | Central Buddhist Museum at Jogyesa free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=183557) |
| `SEOUL-PALACE-TOUR-EN` | Royal palace free English guided tours | Live-Check | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=124533) |
| `SEOUL-JOGYESA` | Jogyesa Temple Seoul free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=111552&menuSn=351) |
| `SEOUL-BONGEUNSA` | Bongeunsa Temple Gangnam free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=104722) |
| `SEOUL-SAJIK-LIGHT` | Sajik Forest of Light free admission | Live-Check | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=217718) |
| `SEOUL-DAEHANMUN-HANBOK` | Deoksugung Daehanmun Sunday free hanbok photo | Live-Check | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=129527) |
| `SEOUL-HEUNGINJIMUN` | Heunginjimun Dongdaemun Gate exterior free viewing | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=110658) |
| `BUSAN-BEOMEOSA` | Beomeosa Temple free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=111223) |
| `BUSAN-HWANGNYEONG` | Hwangnyeongsan Mountain trail free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=77390) |
| `BUSAN-GEUMJEONG-FORT` | Geumjeongsanseong Fortress free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=111743) |
| `BUSAN-GWANGALLI-THEME` | Gwangalli Beach Theme Street free walking access | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=189755) |
| `BUSAN-GREEN-RAIL` | Haeundae Green Railway walking trail free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=172690) |
| `BUSAN-TRAVEL-LOUNGE` | Busan Travel Lounge rest and info free admission | Active | [Open source ↗](https://visitbusan.net/index.do?lang_cd=en&menuCd=DOM_000000301001001000&uc_seq=1900) |
| `BUSAN-SONGJEONG-BEACH` | Songjeong Beach free access | Active | [Open source ↗](https://www.visitbusan.net/en/index.do?menuCd=DOM_000000301001001000&uc_seq=280&lang_cd=en) |
| `BUSAN-CITIZENS-PARK` | Busan Citizens Park grounds free admission | Active | [Open source ↗](https://www.visitbusan.net/en/index.do?menuCd=DOM_000000302002001000&uc_seq=1186&lang_cd=en) |
| `BUSAN-SEUNGHAKSAN` | Seunghaksan Mountain trail free admission | Active | [Open source ↗](https://visitbusan.net/index.do?lang_cd=en&menuCd=DOM_000000302002001000&uc_seq=1019) |
| `BUSAN-EULSUKDO-PARK` | Eulsukdo Migratory Bird Park outdoor free access | Active | [Open source ↗](https://visitbusan.net/index.do?lang_cd=en&menuCd=DOM_000000302002001000&uc_seq=1019) |
| `BUSAN-SUYEONG-SAJEOK` | Suyeong Sajeok Park free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=81400) |
| `SEOUL-PLAZA` | Seoul Plaza free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=107522) |
| `BUSAN-MARINE-CITY` | Marine City Haeundae streetscape free access | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=60310) |
| `BUSAN-F1963` | F1963 culture factory grounds free admission | Active | [Open source ↗](https://www.visitbusan.net/en/index.do?menuCd=DOM_000000301001001000&uc_seq=372&lang_cd=en) |
| `BUSAN-CINE-ROAD` | Busan Cine Road free walking access | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=184378) |
| `BUSAN-HOEDONG` | Hoedong Reservoir walking path free admission | Active | [Open source ↗](https://www.visitbusan.net/index.do?menuCd=DOM_000000301001001000&uc_seq=436&lang_cd=en) |
| `BUSAN-CINEMA-CENTER` | Busan Cinema Center outdoor grounds free admission | Active | [Open source ↗](https://english.visitkorea.or.kr/enu/ATR/SI_EN_3_1_1_1.jsp?cid=2503886) |
| `SEOUL-CHEONGGYE-STREAM` | Cheonggyecheon Stream walk public recreation | Active | [Open source ↗](https://english.visitkorea.or.kr/svc/contents/infoHtmlView.do?menuSn=219&vcontsId=136646) |
