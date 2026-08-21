"""Build the static deal directory from the verified data/deals.csv registry."""
import csv, html, re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "site"
OUT.mkdir(exist_ok=True)
rows = list(csv.DictReader((ROOT / "data/deals.csv").open(encoding="utf-8")))
by = defaultdict(list)
for row in rows:
    by[row["category"]].append(row)
food = [r for key in ("restaurant", "delivery", "market", "coupon", "membership", "birthday") for r in by.get(key, [])]
labels = {"restaurant":"Restaurants", "delivery":"Delivery", "market":"Markets", "coupon":"Coupons", "membership":"Memberships", "birthday":"Birthday", "attraction":"Entrance & Museums", "activity":"Activities", "shopping":"Shopping", "transport":"Transport", "transport+attraction":"Transport + Entrance", "city-pass":"City Passes", "payment":"Payments", "city-tour":"City Tours", "festival":"Festivals", "airport":"Airport", "travel":"Travel", "water":"Water Activities"}

def e(v): return html.escape(str(v or ""), quote=True)
def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
def card(r):
    return f'''<article class="card"><div class="eyebrow">{e(r['city'])} <span class="status {slug(r['status'])}">{e(r['status'])}</span></div><h3>{e(r['title'])}</h3><div class="facts"><span>₩ {e(r['price_or_saving_krw'])}</span><span>Recheck {e(r['expiry_or_recheck'])}</span></div><p>{e(r['notes'])}</p><div class="card-foot"><span>{e(r['source_tier'])} source · {e(r['live_check'])} live check</span><a href="{e(r['source_url'])}" target="_blank" rel="noopener">Verify source ↗</a></div></article>'''
def page(title, intro, cards, current=""):
    nav = '<a href="index.html" class="brand">🇰🇷 Korea deals</a>' + ''.join(f'<a class="{"selected" if current == k else ""}" href="{slug(k)}.html">{e(labels.get(k,k))}<small>{len(by[k])}</small></a>' for k in sorted(by, key=lambda k: (0 if k in {"restaurant","delivery","market","coupon","membership","birthday"} else 1, labels.get(k,k))))
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)} · Korea deals</title><link rel="stylesheet" href="styles.css"></head><body><header><nav>{nav}</nav></header><main><a class="back" href="index.html">← All deals</a><div class="hero"><p class="kicker">Verified deal registry</p><h1>{e(title)}</h1><p>{e(intro)}</p></div><div class="summary">{len(cards)} verified listing{'s' if len(cards)!=1 else ''} · every claim is shown exactly as recorded in <code>data/deals.csv</code></div><section class="grid">{''.join(card(r) for r in cards) or '<p>No deals recorded in this category.</p>'}</section></main><footer>Source links open the original provider. Recheck details before paying or traveling.</footer></body></html>'''

css = '''*{box-sizing:border-box}body{margin:0;background:#f6f7fb;color:#172033;font:15px/1.55 Inter,system-ui,-apple-system,sans-serif}header{background:#fff;border-bottom:1px solid #e5e7ee;position:sticky;top:0;z-index:5}nav{max-width:1180px;margin:auto;padding:14px 24px;display:flex;gap:7px;align-items:center;overflow:auto;white-space:nowrap}.brand{font-weight:800;color:#172033;text-decoration:none;margin-right:12px;font-size:17px}nav a:not(.brand){color:#596277;text-decoration:none;padding:7px 10px;border-radius:8px}nav a.selected,nav a:hover:not(.brand){background:#eef2ff;color:#3848b8}nav small{font-size:11px;margin-left:5px;color:#9299ab}main{max-width:1180px;margin:auto;padding:32px 24px 60px}.back{color:#5664c7;text-decoration:none;font-weight:650}.hero{padding:28px 0 18px;max-width:730px}.kicker{text-transform:uppercase;letter-spacing:.12em;font-size:11px;font-weight:800;color:#6470d8;margin:0 0 8px}.hero h1{font-size:clamp(30px,5vw,48px);line-height:1.08;margin:0 0 12px;letter-spacing:-.04em}.hero p:last-child{color:#687186;font-size:17px;margin:0}.summary{color:#727b8d;margin:12px 0 22px;font-size:13px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:16px}.card{background:#fff;border:1px solid #e4e7ef;border-radius:14px;padding:19px;box-shadow:0 2px 7px #17203308}.card:hover{border-color:#aab3f4;box-shadow:0 7px 22px #17203312}.eyebrow{font-size:12px;text-transform:uppercase;letter-spacing:.07em;color:#737d91;font-weight:750}.status{float:right;padding:3px 7px;border-radius:99px;font-size:10px;background:#eef8f1;color:#237a43}.status.live-check{background:#fff6df;color:#986816}.card h3{font-size:18px;line-height:1.25;margin:12px 0}.facts{display:flex;gap:8px;flex-wrap:wrap}.facts span{background:#f2f4f8;border-radius:6px;padding:4px 8px;font-size:12px;color:#4e596d}.card p{color:#596477;font-size:13px;min-height:60px}.card-foot{border-top:1px solid #edf0f5;padding-top:12px;color:#8a92a2;font-size:11px;display:flex;justify-content:space-between;gap:8px}.card-foot a{color:#5664c7;text-decoration:none;font-weight:700}footer{text-align:center;border-top:1px solid #e5e7ee;padding:24px;color:#8a92a2;font-size:12px}code{font-size:11px}'''
(OUT / "styles.css").write_text(css)
(OUT / "index.html").write_text(page("Korea deals, organized", "Food deals are first. Use the navigation to open a dedicated page for every deal type. Nothing is added beyond the repository's verified deal registry.", food))
for category, items in by.items():
    (OUT / f"{slug(category)}.html").write_text(page(labels.get(category, category.title()), f"{labels.get(category, category.title())} recorded in the deal registry.", items, category))
# Keep root URL as the homepage for simple static hosting.
(ROOT / "index.html").write_text((OUT / "index.html").read_text())
(ROOT / "styles.css").write_text(css)
for p in OUT.glob("*.html"):
    if p.name != "index.html":
        # category pages are intentionally separate root-level subpages
        (ROOT / p.name).write_text(p.read_text())
print(f"Built {len(rows)} deals across {len(by)} category pages; food first page has {len(food)} deals.")
