#!/usr/bin/env python3
"""Pre-render the Kit cards and JSON-LD into index.html so crawlers and AI
search engines see the content without running JavaScript.

Run after every change to kit.config.json:  python3 build.py
The browser still re-renders from kit.config.json at load time, so the two
never drift: this file only fills the space between the prerender markers.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
CFG = json.loads((ROOT / "kit.config.json").read_text(encoding="utf-8"))
INDEX = ROOT / "index.html"

EVENT = {"alerts": "click_appstore", "esim": "click_esim", "power": "click_power", "insurance": "click_insurance"}


def esc(s):
    return html.escape(str(s or ""), quote=True)


def app_store_url():
    a = CFG["appStore"]
    base = a["url"]
    c = a.get("campaign") or {}
    if c.get("pt"):
        return f"{base}?pt={c['pt']}&ct={c.get('ct', 'safety_kit')}&mt={c.get('mt', '8')}"
    return base


def facts(items, muted=False):
    if not items:
        return ""
    lis = "".join(f"<li>{esc(t)}</li>" for t in items)
    return f'<ul class="facts">{lis}</ul>'


def render_cards():
    out = []
    shown = 0
    for card in CFG["cards"]:
        opts = [o for o in card.get("options", []) if o.get("enabled") and o.get("url")]
        if not opts:
            continue
        shown += 1
        own = card.get("kind") == "own"
        parts = [f'<section class="card" id="card-{esc(card["id"])}">']
        parts.append('<div class="card-head"><div class="num"><b>Essential %02d</b>  %s</div>%s</div>' % (
            shown, esc(card.get("kicker", "")),
            f'<span class="badge{" free" if own else ""}">{esc(card["badge"])}</span>' if card.get("badge") else ""))
        parts.append(f'<h2>{esc(card.get("title", ""))}</h2>')
        if card.get("why"):
            parts.append(f'<p class="why">{esc(card["why"])}</p>')
        parts.append(facts(card.get("facts")))
        for i, o in enumerate(opts):
            boxed = len(opts) > 1 or not own
            url = app_store_url() if o["url"] == "APP_STORE" else o["url"]
            rel = "sponsored noopener" if card.get("kind") == "affiliate" else "noopener"
            parts.append(f'<div class="{"option" if boxed else ""}">')
            if boxed:
                parts.append(f'<h3>{esc(o.get("name", ""))}</h3>')
            parts.append(facts(o.get("facts")))
            parts.append(f'<a class="btn{"" if own else " secondary"}" href="{esc(url)}" target="_blank" rel="{rel}" '
                         f'data-event="{EVENT.get(card["id"], "click_other")}" data-vendor="{esc(o.get("id", i))}">{esc(o.get("cta") or o.get("name") or "Open")}</a>')
            if o.get("note"):
                parts.append(f'<p class="note">{esc(o["note"])}</p>')
            if card.get("kind") == "affiliate" and CFG.get("disclosure", {}).get("short"):
                parts.append(f'<p class="disc">{esc(CFG["disclosure"]["short"])}</p>')
            parts.append("</div>")
        parts.append("</section>")
        out.append("".join(parts))
    return "\n".join(out)


def render_jsonld():
    site = CFG["site"]["url"]
    app = {
        "@type": "SoftwareApplication",
        "name": "Japan Disaster Guide",
        "operatingSystem": "iOS",
        "applicationCategory": "TravelApplication",
        "description": "Free iPhone app that delivers Japan Meteorological Agency warnings for earthquakes, tsunami, typhoons and heavy rain in 7 languages, after JMA confirms them, with 115,000+ designated evacuation sites on a map.",
        "url": CFG["appStore"]["url"],
        "installUrl": CFG["appStore"]["url"],
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "inLanguage": ["en", "ja", "ko", "th", "vi", "zh-Hans", "zh-Hant"],
        "publisher": {"@type": "Organization", "name": "Japan Disaster Guide", "url": site,
                      "sameAs": [CFG["site"]["instagram"], CFG["appStore"]["url"]]},
    }
    page = {
        "@type": "WebPage",
        "@id": site,
        "url": site,
        "name": "Japan Travel Safety Kit",
        "description": "A before-you-fly checklist for travelers to Japan: an app for official disaster warnings in English, a travel eSIM so the warnings reach you, a power bank, and travel insurance.",
        "inLanguage": "en",
        "isPartOf": {"@type": "WebSite", "name": "Japan Disaster Guide", "url": site},
        "about": [{"@type": "Thing", "name": t} for t in ["Japan disaster preparedness for travelers", "Japan Meteorological Agency warnings", "earthquake", "tsunami", "typhoon", "heavy rain"]],
        "mainEntity": app,
    }
    data = {"@context": "https://schema.org", "@graph": [page, app]}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def fill(text, marker, body):
    pat = re.compile(rf"(<!-- prerender:{marker} -->).*?(<!-- /prerender:{marker} -->)", re.S)
    if not pat.search(text):
        raise SystemExit(f"marker {marker} not found in index.html")
    return pat.sub(lambda m: m.group(1) + "\n" + body + "\n" + m.group(2), text)


def main():
    text = INDEX.read_text(encoding="utf-8")
    text = fill(text, "cards", render_cards())
    text = fill(text, "jsonld", render_jsonld())
    INDEX.write_text(text, encoding="utf-8")
    n = text.count('<section class="card"')
    print(f"prerendered {n} cards + JSON-LD into index.html")


if __name__ == "__main__":
    main()
