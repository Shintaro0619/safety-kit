#!/usr/bin/env python3
"""Build the JDG Gear marketplace and the Disaster Tips pages.

Outputs: shop/index.html, shop/<category>/, shop/item/<key>/, tips/index.html, tips/<slug>/.
Rakuten link HTML is pasted exactly as the Rakuten Affiliate link tool made it (no edits to tags,
attributes, image size or URL; only the words of a text-only link are changed), from
rakuten_links/<key>_image240.html, _image300.html and _text.html.
Amazon links are plain /dp/ASIN?tag= links. No prices, no Amazon images, no ratings.
"""
import html
import os
from pathlib import Path

from build_guide import APP, CSS, SITE, umami_tag
from market_theme import MARKET_CSS, NAV_CSS, PAGE, nav_html
from shop_pages import SHOP, TIPS
from shop_products import PRODUCTS

ROOT = Path(__file__).parent
SITE = os.environ.get("PREVIEW_SITE", SITE)  # local preview only; publish builds must not set it
RK = ROOT / "rakuten_links"
TAG = "jdgkit-22"
MANUAL = "https://soyama6.gumroad.com/l/japan-travel-safety-manual"
DISCLOSURE_JA = "Amazonのアソシエイトとして、Japan Disaster Guideは適格販売により収入を得ています。"
DISCLOSURE_EN = "As an Amazon Associate, Japan Disaster Guide earns from qualifying purchases."


def esc(s):
    return html.escape(s, quote=True)


def rakuten(key, kind):
    f = RK / f"{key}_{kind}.html"
    if not f.exists():
        raise SystemExit(f"missing Rakuten link: {f}")
    return f.read_text(encoding="utf-8").strip()


def amazon(key):
    return f"https://www.amazon.co.jp/dp/{PRODUCTS[key]['asin']}?tag={TAG}"


def prline():
    return (f'<div class="prline"><p><span class="chip">PR</span>This page contains affiliate links to Rakuten Ichiba and Amazon.co.jp.</p>'
            f'<p lang="ja">{esc(DISCLOSURE_JA)}</p><p>{esc(DISCLOSURE_EN)}</p></div>')


def item_url(key):
    return f"{SITE}shop/item/{key}/"


def tile(key, ev):
    p = PRODUCTS[key]
    return (f'<div class="tile"><div class="ph" data-rk="{ev}-{key}">{rakuten(key, "image240")}</div>'
            f'<h3><a href="{item_url(key)}">{esc(p["name"])}</a></h3><p class="sub">{esc(p["kind"])} · {esc(p["for"])}</p></div>')


def tip_card(t):
    return (f'<a class="tip" href="{SITE}tips/{t["slug"]}/"><img src="{SITE}assets/tips/{t["slug"]}.jpg" alt="" width="240" height="240" loading="lazy">'
            f'<h3>{esc(t["short"])}</h3><p class="sub">Disaster Tips, Part {t["part"]}</p></a>')


def manual_tile():
    return (f'<a class="mtile" href="{MANUAL}" data-event="click_manual" data-vendor="gear-home" rel="noopener">'
            '<span>Our own guide</span><b>Japan Travel Safety Manual</b><span>66-page PDF for your phone: what to do in the first 72 hours, the 119 script, 21 pointing cards</span><em>$9.99 PDF</em></a>')


def rail(title, cards, more=None):
    link = f'<a href="{more}">See all ›</a>' if more else ""
    return f'<div class="rowhead"><h2>{esc(title)}</h2>{link}</div><div class="rail">{"".join(cards)}</div>'


def source_block(title, items, checked):
    if not items:
        return ""
    li = "".join(f'<li>{esc(n)}. <a href="{u}" rel="noopener">{esc(u)}</a></li>' for n, u in items)
    return (f'<div class="sources"><b>{esc(title)}</b> ({esc(checked)})<ol>{li}</ol>'
            f'<p>In an emergency, follow the instructions of local officials.</p></div>')


def render(rel, title, description, content, ev, sources="", og=None, nav="gear"):
    text = PAGE.format(title=esc(title), description=esc(description), url=f"{SITE}{rel}/", site=SITE, umami=umami_tag(),
                       css=CSS + MARKET_CSS + NAV_CSS, content=content, manual=MANUAL, app=APP, ev=ev, sources=sources,
                       og_image=og or f"{SITE}assets/og.png", nav=nav_html(SITE, nav),
                       disclosure_ja=esc(DISCLOSURE_JA), disclosure_en=esc(DISCLOSURE_EN))
    d = ROOT / rel
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(text, encoding="utf-8")


def main():
    shops = {s["slug"]: s for s in SHOP}
    cat_of = {k: s["slug"] for s in SHOP for k in s["items"]}
    tips_by_date = sorted(TIPS, key=lambda t: t["posted"], reverse=True)

    # marketplace home
    intro = ('<span class="kicker">Gear</span><h1>Gear for a disaster in Japan</h1>'
             '<p class="answer">For power cuts, water outages and being trapped. Each item is listed with the maker\'s own figures. Rakuten Ichiba and Amazon.co.jp deliver within Japan.</p>')
    rows = [rail(s["menu"], [tile(k, "home") for k in s["items"]], f"{SITE}shop/{s['slug']}/") for s in SHOP]
    rows.append(rail("From Japan Disaster Guide", [manual_tile()]))
    render("shop", "Gear for a disaster in Japan", "Disaster gear for power cuts, water outages and being trapped in Japan, with the maker's own figures.",
           prline() + intro + "".join(rows), "shop-home")

    # category pages
    for s in SHOP:
        ev = f"shop-{s['slug']}"
        related = [t for t in tips_by_date if s["slug"] in t["shops"]]
        body = (prline() + f'<span class="kicker">Gear</span><h1>{esc(s["title"])}</h1><p class="answer">{esc(s["intro"])}</p>'
                f'<div class="grid">{"".join(tile(k, ev) for k in s["items"])}</div>')
        if related:
            body += rail("Related tips", [tip_card(t) for t in related])
        render(f"shop/{s['slug']}", s["title"], s["description"], body, ev,
               source_block("Sources for the rules above", s.get("sources", []), "checked 23 Nov 2026"))

    # product pages
    for key, p in PRODUCTS.items():
        ev = f"item-{key}"
        cat = shops[cat_of[key]]
        src_list = p["source"] if isinstance(p["source"], list) else [p["source"]]
        facts = "".join(f"<li>{esc(x)}</li>" for x in p["facts"])
        srcs = " ".join(f'<a href="{u}" rel="noopener">{esc(u)}</a>' for u in src_list)
        ship = (esc(p["note"]) + " " if p.get("note") else "") + "Rakuten Ichiba and Amazon.co.jp deliver within Japan."
        related = [t for t in tips_by_date if key in t["items"]]
        more = [k for k in cat["items"] if k != key]
        body = (prline() + f'<div class="prod"><div class="big" data-rk="{ev}">{rakuten(key, "image300")}</div><div>'
                f'<span class="kicker">{esc(p["kind"])}</span><h1>{esc(p["name"])}</h1><p class="sub">For: {esc(p["for"])}</p>'
                f'<div class="buy"><span class="rk" data-rk="{ev}">{rakuten(key, "text")}</span>'
                f'<a class="amz" href="{amazon(key)}" data-event="click_gear" data-vendor="{ev}" rel="sponsored noopener">View on Amazon.co.jp</a>'
                f'<span class="prmark">PR</span></div><p class="ship">{ship}</p></div></div>'
                f'<div class="facts"><h2>From the maker</h2><ul>{facts}</ul><p class="src">Source: {srcs}</p></div>')
        if related:
            body += rail("Tips that use this", [tip_card(t) for t in related])
        if more:
            body += rail(f"More in {cat['menu']}", [tile(k, ev) for k in more], f"{SITE}shop/{cat['slug']}/")
        render(f"shop/item/{key}", p["name"], f"{p['name']}: {p['kind'].lower()} for {p['for'].lower()}. The maker's own figures, with links to Rakuten Ichiba and Amazon.co.jp.",
               body, ev)

    # tips pages
    for t in TIPS:
        ev = f"tips-{t['part']}"
        body = (prline() + f'<span class="kicker">Disaster Tips, Part {t["part"]}</span><h1>{esc(t["short"])}</h1>'
                f'<div class="tiphero"><img src="{SITE}assets/tips/{t["slug"]}.jpg" alt="" width="720" height="720"></div>'
                f'<p class="answer">{esc(t["answer"])}</p>{t["body"]}'
                f'<div class="rowhead"><h2>Gear for this tip</h2></div><p>{esc(t["gear_intro"])}</p>'
                f'<div class="rail">{"".join(tile(k, ev) for k in t["items"])}</div>'
                + "".join(f'<p><a href="{SITE}shop/{x}/">{esc(shops[x]["title"])} ›</a></p>' for x in t["shops"])
                + rail("More Disaster Tips", [tip_card(o) for o in tips_by_date if o is not t], f"{SITE}guide/"))
        render(f"tips/{t['slug']}", t["title"], t["description"], body, ev,
               source_block("Sources for the tips", t["sources"], "checked when the reel was made, November 2026"),
               og=f"{SITE}assets/tips/{t['slug']}.jpg", nav="guides")

    print(f"wrote shop home, {len(SHOP)} categories, {len(PRODUCTS)} products and {len(TIPS)} tips")


if __name__ == "__main__":
    main()
