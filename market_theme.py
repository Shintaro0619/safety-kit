"""Marketplace look for the gear and tips pages (Tekks Space style: hero, rails of photo tiles)."""

MARKET_CSS = """
.wrap{max-width:1040px}
.bar{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:16px 0 10px}
.brand{display:flex;align-items:center;gap:10px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--text);text-decoration:none;font-size:15px}
.brand img{width:28px;height:28px;border-radius:7px}.brand span{color:#F26B3A}

.prline{font-size:12px;color:var(--muted);border:1px solid var(--line);border-radius:10px;padding:8px 12px;margin:0 0 16px}.prline p{margin:0 0 2px}
.chip{display:inline-block;font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;background:#E5483B;color:#fff;border-radius:6px;padding:3px 8px;margin-right:8px}
.kicker{font-size:13px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.hero{position:relative;border-radius:18px;overflow:hidden;margin:4px 0 26px;background:var(--bg-2);display:grid;grid-template-columns:1fr 1fr;align-items:center}
.hero img{width:100%;height:auto;display:block}
.hero .txt{padding:22px 26px}.hero h1{font-size:34px;margin:10px 0 10px}.hero p{color:var(--muted)}
.btnrow{display:flex;flex-wrap:wrap;gap:10px;margin-top:14px}
.b1{display:inline-block;background:#fff;color:#0F1420;font-weight:800;border-radius:10px;padding:12px 18px;text-decoration:none}
.b2{display:inline-block;background:var(--bg-3);color:var(--text);font-weight:700;border-radius:10px;padding:12px 18px;text-decoration:none;border:1px solid var(--line)}
.rowhead{display:flex;align-items:baseline;gap:12px;margin:26px 0 10px}.rowhead h2{margin:0;font-size:21px}.rowhead a{font-size:14px;color:var(--muted);text-decoration:none;font-weight:600}
.rail{display:flex;gap:14px;overflow-x:auto;padding-bottom:8px;scroll-snap-type:x mandatory}.rail>*{scroll-snap-align:start}
.grid{display:flex;flex-wrap:wrap;gap:16px}
.tile{flex:0 0 240px;width:240px}
.tile .ph{width:240px;height:240px;background:#fff;border-radius:12px;display:flex;align-items:center;justify-content:center;overflow:hidden}
.tile .ph a{display:block;line-height:0}
.tile h3{font-size:16px;line-height:1.3;margin:10px 0 2px}.tile h3 a{color:var(--text);text-decoration:none}
.tile .sub{font-size:13px;color:var(--muted);margin:0}
.mtile{flex:0 0 240px;width:240px;height:240px;border-radius:12px;background:linear-gradient(160deg,#2F6FED,#1A2130);color:#fff;text-decoration:none;display:flex;flex-direction:column;justify-content:space-between;padding:18px}.mtile b{font-size:22px;line-height:1.15}.mtile span{font-size:13px;opacity:.9}.mtile em{font-style:normal;font-weight:800;background:#fff;color:#0F1420;border-radius:8px;padding:8px 12px;align-self:flex-start}
.tip{flex:0 0 240px;width:240px;text-decoration:none;color:var(--text)}
.tip img{width:240px;height:240px;border-radius:12px;display:block;object-fit:cover}
.tip h3{font-size:16px;line-height:1.3;margin:10px 0 2px}.tip .sub{font-size:13px;color:var(--muted)}
.prod{display:grid;grid-template-columns:320px 1fr;gap:26px;align-items:start;margin:6px 0 10px}
.prod .big{width:320px;min-height:320px;background:#fff;border-radius:16px;display:flex;align-items:center;justify-content:center}
.prod .big a{display:block;line-height:0}
.prod h1{font-size:30px;margin:8px 0 6px}
.buy{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin:16px 0 6px}
.rk a{display:inline-block;background:#BF0000;color:#fff;font-weight:800;border-radius:10px;padding:12px 18px;text-decoration:none}
.amz{display:inline-block;background:#FF9900;color:#0F1420;font-weight:800;border-radius:10px;padding:12px 18px;text-decoration:none}
.prmark{font-size:11px;font-weight:700;color:var(--muted);letter-spacing:.08em}
.ship{font-size:13px;color:var(--muted);margin:6px 0 0}
.facts{background:var(--bg-2);border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin:18px 0}.facts h2{margin:0 0 6px;font-size:17px}
.facts .src{font-size:12px;color:var(--muted);overflow-wrap:anywhere}.facts .src a{color:var(--muted)}
.tiphero{border-radius:16px;overflow:hidden;max-width:420px;margin:6px 0 14px}.tiphero img{width:100%;height:auto;display:block}
@media (max-width:720px){
 .hero{grid-template-columns:1fr}.hero .txt{padding:18px 18px 22px}.hero h1{font-size:28px}
 .prod{grid-template-columns:1fr}.prod .big{width:100%;min-height:300px}
 .prod h1{font-size:26px}
}
"""

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Japan Disaster Guide</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0F1420">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Japan Disaster Guide">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og_image}">
<link rel="icon" type="image/png" sizes="64x64" href="{site}assets/jdg-logo-64.png">
{umami}
<style>{css}</style>
</head>
<body>
<div class="wrap">
<div class="bar"><a class="brand" href="{site}"><img src="{site}assets/jdg-logo-64.png" alt="" width="28" height="28">Japan Disaster <span>Guide</span></a></div>
{nav}
{content}
{sources}
<footer><a href="{site}">Japan Travel Safety Kit</a> · <a href="https://www.instagram.com/japandisasterchannel/" rel="noopener">@japandisasterchannel</a> · <a href="https://shintaro0619.github.io/jdg-web/privacy.html" rel="noopener">Privacy</a><br>{disclosure_ja} {disclosure_en}</footer>
</div>
<script>
(function(){{var p=new URLSearchParams(location.search),u={{}};['utm_source','utm_medium','utm_campaign'].forEach(function(k){{var v=p.get(k);if(v)u[k]=v.slice(0,64)}});
document.addEventListener('click',function(e){{if(!e.target.closest)return;var a=e.target.closest('a[data-event]'),ev,vd;if(a){{ev=a.getAttribute('data-event');vd=a.getAttribute('data-vendor')}}else{{var r=e.target.closest('[data-rk] a');if(!r)return;ev='click_gear_rakuten';vd=r.closest('[data-rk]').getAttribute('data-rk')}}var d=Object.assign({{vendor:vd||''}},u);if(window.umami&&umami.track){{try{{umami.track(ev,d)}}catch(x){{}}}}}});}})();
</script>
</body>
</html>
"""


NAV_CSS = (".nav{display:flex;width:fit-content;max-width:100%;overflow-x:auto;gap:4px;padding:4px;margin:0 0 16px;background:var(--bg-2);border:1px solid var(--line);border-radius:999px}"
           ".nav a{color:var(--muted);text-decoration:none;white-space:nowrap;font-size:15px;font-weight:700;padding:8px 16px;border-radius:999px}.nav a.on{background:var(--text);color:#0F1420}")


def nav_html(site, on):
    tabs = [("kit", site, "Before you fly"), ("guides", site + "guide/", "Guides"), ("gear", site + "shop/", "Gear")]
    out = []
    for k, u, t in tabs:
        cls = ' class="on"' if k == on else ""
        out.append(f'<a href="{u}"{cls}>{t}</a>')
    return '<nav class="nav">' + "".join(out) + "</nav>"
