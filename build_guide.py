#!/usr/bin/env python3
"""Generate the free explainer pages under guide/ (one question per page).

Content = the "first half" of each chapter of the Japan Travel Safety Manual:
definitions and the one key rule, each with its primary source. Full
procedures, pointing cards and worksheets stay in the paid manual.

Run:  python3 build_guide.py   (also run build.py; then commit both)
Every fact below is in ~/disaster-app/marketing/PDF_SOURCES.md with a quote,
URL and read date. Do not add numbers here that are not in that ledger.
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "guide"
SITE = "https://shintaro0619.github.io/safety-kit/"
CFG = json.loads((ROOT / "kit.config.json").read_text(encoding="utf-8"))
APP = CFG["appStore"]["url"]
UMAMI = CFG["analytics"]["websiteId"]
TODAY = "2026-09-09"

PAGES = [
    {
        "slug": "japan-alert-levels",
        "title": "What do Japan's Alert Levels 1 to 5 mean?",
        "description": "Japan's five Alert Levels for heavy rain, flooding, landslides and storm surge, as named by the Japan Meteorological Agency since May 2026, and what each one asks you to do.",
        "answer": "Since 29 May 2026 the Japan Meteorological Agency (JMA) names every heavy-rain, flood, landslide and storm-surge warning with its Alert Level. Level 5 is an Emergency Warning (a disaster is happening), Level 4 is an Urgent Warning (everyone in the at-risk area must leave), Level 3 is a Warning (people who need time should start evacuating), Level 2 is an Advisory, and Level 1 is early information that a warning-level event may come within days.",
        "body": """
<h2>The five levels</h2>
<table><thead><tr><th>Level</th><th>What JMA issues</th><th>What it means for you</th></tr></thead><tbody>
<tr><td>5</td><td><b>Emergency Warning</b></td><td>A disaster is already happening or is certain. Protect your life with whatever is around you: an upper floor, away from windows or slopes.</td></tr>
<tr><td>4</td><td><b>Urgent Warning</b> (shown as "Danger Warning" in some apps and translations)</td><td>Everyone in the at-risk area must leave now. Cities issue an Evacuation Order at this level.</td></tr>
<tr><td>3</td><td><b>Warning</b></td><td>People who need more time (elderly, disabled, families with small children) start evacuating. Everyone else prepares.</td></tr>
<tr><td>2</td><td><b>Advisory</b></td><td>Check where you would go and how.</td></tr>
<tr><td>1</td><td>Early information (<i>sōki chūi jōhō</i>)</td><td>A warning-level event may come within days. Watch the forecasts.</td></tr>
</tbody></table>
<h2>JMA's own words</h2>
<p>An Emergency Warning signals <q>the significant likelihood of catastrophes in association with natural phenomena of extraordinary magnitude</q>, of a scale <q>observed only once every few decades</q>. JMA's instruction: <q>Take all steps possible to protect yourself if an Emergency Warning is issued.</q></p>
<h2>The one rule</h2>
<p><b>At Level 4, leave the at-risk area. Do not wait for Level 5.</b> Level 5 means the disaster has started; by then travel through it is dangerous.</p>
<h2>Which warnings carry a level</h2>
<p>Heavy rain, river flooding, landslides and storm surge. Other warnings (storm, snowstorm, heavy snow, high waves) still use the three tiers Advisory, Warning and Emergency Warning.</p>
""",
        "sources": [
            ("Japan Meteorological Agency, Emergency Warning System (English)", "https://www.jma.go.jp/jma/en/Emergency_Warning/ew_index.html"),
            ("Japan Meteorological Agency, notice of 27 May 2026 on the start of the new disaster weather information (Japanese, PDF)", "https://www.jma.go.jp/jma/press/2605/27a/teikyoukaishi.pdf"),
        ],
        "note": "Level 1 has no official English name on JMA's English pages at the time of writing; the description is a paraphrase.",
    },
    {
        "slug": "shindo-seismic-intensity",
        "title": "What is shindo, and how is it different from magnitude?",
        "description": "Japan reports earthquakes by seismic intensity (shindo 0 to 7), which is how strongly the ground shook where you are. JMA's description of each level, and why one earthquake has many intensities.",
        "answer": "Shindo (seismic intensity) is JMA's 0 to 7 scale for how strongly the ground shook at a given place. Magnitude is the size of the earthquake at its source. The same earthquake has one magnitude and many intensities, one for each observation point. Travelers should read the intensity for where they are, not the magnitude.",
        "body": """
<h2>JMA's description of each level</h2>
<table><thead><tr><th>Shindo</th><th>What people feel (JMA wording)</th></tr></thead><tbody>
<tr><td>0</td><td>Imperceptible to people, but recorded by seismometers.</td></tr>
<tr><td>1</td><td>Felt slightly by some people keeping quiet in buildings.</td></tr>
<tr><td>2</td><td>Felt by many people keeping quiet in buildings. Some people may be awoken.</td></tr>
<tr><td>3</td><td>Felt by most people in buildings. Felt by some people walking. Many people are awoken.</td></tr>
<tr><td>4</td><td>Most people are startled. Felt by most people walking.</td></tr>
<tr><td>5 Lower</td><td>Many people are frightened and feel the need to hold onto something stable.</td></tr>
<tr><td>5 Upper</td><td>Walking is difficult without holding onto something stable.</td></tr>
<tr><td>6 Lower</td><td>It is difficult to remain standing.</td></tr>
<tr><td>6 Upper</td><td>It is impossible to remain standing or move without crawling.</td></tr>
<tr><td>7</td><td>People may be thrown through the air.</td></tr>
</tbody></table>
<h2>Why it varies</h2>
<p>Intensities are measured by instruments at fixed points and <q>vary with underground conditions and topography</q>. A report of shindo 5 Lower for a prefecture does not mean your street shook that hard, or that it did not shake harder.</p>
<h2>The one rule</h2>
<p><b>While it shakes: drop, get under a sturdy table, cover your head, and do not run outside.</b> Falling glass, tiles and signboards injure people who run.</p>
<h2>In the app</h2>
<p>Japan Disaster Guide lets you choose the intensity at which you are notified (3, 4 or 5 Lower). During an aftershock sequence, raising it cuts the noise while the important alerts still get through.</p>
""",
        "sources": [
            ("Japan Meteorological Agency, Seismic Intensity Scale (English)", "https://www.jma.go.jp/jma/en/Activities/inttable.html"),
            ("Tokyo Metropolitan Government, Disaster Preparedness Tokyo (2023, English)", "https://www.bousai.metro.tokyo.lg.jp/_res/projects/default_project/_page_/001/029/136/tb2023_e_00.pdf"),
        ],
    },
    {
        "slug": "tsunami-warnings",
        "title": "What are Japan's three tsunami warnings, and what should I do?",
        "description": "Major Tsunami Warning, Tsunami Warning and Tsunami Advisory: the expected heights, the words 'Huge' and 'High', and the action JMA gives for each.",
        "answer": "JMA issues three categories about three minutes after a large earthquake: a Major Tsunami Warning (expected height over 10 m, 10 m or 5 m, or the word 'Huge'), a Tsunami Warning (3 m, or 'High') and a Tsunami Advisory (1 m). For both warnings the instruction is to evacuate from coastal or river areas immediately to high ground; for an advisory, get out of the water and leave the coast. If you are near the sea when the ground shakes hard, move to high ground without waiting for the warning.",
        "body": """
<h2>The three categories</h2>
<table><thead><tr><th>Category</th><th>Expected height</th><th>What JMA expects</th><th>What JMA tells you to do</th></tr></thead><tbody>
<tr><td><b>Major Tsunami Warning</b></td><td>over 10 m / 10 m / 5 m, or <b>"Huge"</b></td><td>Wooden structures are expected to be completely destroyed and/or washed away</td><td>Evacuate from coastal or river areas immediately to safer places such as high ground</td></tr>
<tr><td><b>Tsunami Warning</b></td><td>3 m, or <b>"High"</b></td><td>Tsunami waves will hit, causing damage to low-lying areas. Buildings will be flooded</td><td>Evacuate from coastal or river areas immediately to safer places</td></tr>
<tr><td><b>Tsunami Advisory</b></td><td>1 m</td><td>Anybody exposed will be caught in strong tsunami currents in the sea</td><td>Get out of the water and leave coastal areas immediately</td></tr>
</tbody></table>
<p>"Huge" and "High" appear when the earthquake is so large that JMA cannot yet give a number. Treat them as the top of the scale.</p>
<h2>The one rule</h2>
<p><b>Near the coast, strong or long shaking means go to high ground now, on foot.</b> Japan's tourism organization: <q>If you are by the coast when a large earthquake strikes, head for higher ground in case of a tsunami.</q></p>
<h2>Waves come in sets</h2>
<p>JMA: <q>Tsunami waves are expected to hit repeatedly. Do not leave the tsunami evacuation location until Tsunami Warnings are cleared.</q> Rivers count too: a tsunami runs up rivers far inland.</p>
""",
        "sources": [
            ("Japan Meteorological Agency, Tsunami Warnings/Advisories and Tsunami Information (English)", "https://www.data.jma.go.jp/eqev/data/en/guide/tsunamiinfo.html"),
            ("JNTO, Staying Safe in Japan", "https://www.japan.travel/en/plan/emergencies/"),
        ],
    },
    {
        "slug": "typhoon-strength",
        "title": "What do 'strong', 'very strong' and 'violent' typhoon mean in Japan?",
        "description": "JMA's typhoon classes by maximum sustained wind (33, 44 and 54 m/s), the size classes, and what the 25 m/s storm area on the map means for a traveler.",
        "answer": "JMA grades a typhoon by its maximum sustained wind: strong (33 m/s or more, under 44), very strong (44 or more, under 54) and violent (54 m/s or more). On JMA's maps the storm area is where winds of 25 m/s or more are blowing or may blow, and the strong-wind area is 15 m/s or more. If your city is inside the storm circle on the forecast, plan to be indoors for that window; trains and flights stop before it arrives.",
        "body": """
<h2>Strength</h2>
<table><thead><tr><th>JMA grade</th><th>Maximum sustained wind</th></tr></thead><tbody>
<tr><td><b>Strong</b> (<i>tsuyoi</i>)</td><td>33 m/s or more, under 44 m/s (64 to under 85 knots)</td></tr>
<tr><td><b>Very strong</b> (<i>hijō ni tsuyoi</i>)</td><td>44 m/s or more, under 54 m/s (85 to under 105 knots)</td></tr>
<tr><td><b>Violent</b> (<i>mōretsu na</i>)</td><td>54 m/s or more (105 knots or more)</td></tr>
</tbody></table>
<h2>Size</h2>
<table><thead><tr><th>JMA size</th><th>Radius of winds of 15 m/s or more</th></tr></thead><tbody>
<tr><td><b>Large</b></td><td>500 km or more, under 800 km</td></tr>
<tr><td><b>Very large</b></td><td>800 km or more</td></tr>
</tbody></table>
<h2>The two circles on the map</h2>
<p><b>Storm area</b> (<i>bōfū-iki</i>): winds of <b>25 m/s or more</b> are blowing or may blow. <b>Strong-wind area</b> (<i>kyōfū-iki</i>): 15 m/s or more.</p>
<h2>The one rule</h2>
<p><b>Inside the storm circle, be indoors for that window.</b> Japanese railways announce planned suspensions ahead of a typhoon and airlines cancel in the same window; check the evening before and book the extra night early.</p>
""",
        "sources": [
            ("Japan Meteorological Agency, 台風の強さと大きさ (Japanese)", "https://www.jma.go.jp/jma/kishou/know/typhoon/1-3.html"),
        ],
    },
    {
        "slug": "heat-stroke-alert",
        "title": "What is Japan's Heat Stroke Alert, and what counts as an 'intense heat day'?",
        "description": "The Heat Stroke Alert is issued when the WBGT index is 33 or higher, announced at 5 pm the day before and 5 am the same day. JMA's definitions of summer day, mid-summer day, intense heat day and tropical night.",
        "answer": "Japan's Heat Stroke Alert is issued by the Ministry of the Environment and JMA when the WBGT heat-stress index is forecast to reach 33 or higher, announced at 5:00 pm the previous day and again at 5:00 am, for each of 58 regions. JMA calls a day with a maximum of 35 °C or more an intense heat day (mōshobi); 30 °C or more is a mid-summer day, 25 °C or more a summer day, and a night that stays at 25 °C or more is a tropical night.",
        "body": """
<h2>The terms</h2>
<table><thead><tr><th>Term</th><th>JMA definition</th></tr></thead><tbody>
<tr><td><b>Summer day</b> (<i>natsubi</i>)</td><td>Daily maximum of 25 °C or more</td></tr>
<tr><td><b>Mid-summer day</b> (<i>manatsubi</i>)</td><td>Daily maximum of 30 °C or more</td></tr>
<tr><td><b>Intense heat day</b> (<i>mōshobi</i>)</td><td>Daily maximum of 35 °C or more</td></tr>
<tr><td><b>Tropical night</b> (<i>nettaiya</i>)</td><td>Night-time minimum of 25 °C or more</td></tr>
</tbody></table>
<h2>The alert</h2>
<p><q>The Heat Stroke Alert will be announced when the WBGT index is 33 or higher.</q> It is announced <q>at 5:00 pm the previous day, and again at 5:00 am the following day</q>, by region (58 regions).</p>
<h2>The one rule</h2>
<p><b>On an alert day, move sightseeing to morning and evening, drink before you are thirsty, and use air-conditioned spaces (stations, department stores, convenience stores).</b> Watch children and older travelers.</p>
""",
        "sources": [
            ("Ministry of the Environment, Heat Stroke Alert (English)", "https://www.wbgt.env.go.jp/en/sp/alert.php"),
            ("Ministry of the Environment, press release: Heat Stroke Alert starts throughout Japan", "https://www.env.go.jp/en/headline/2512.html"),
            ("Japan Meteorological Agency, 予報用語 気温 (Japanese)", "https://www.jma.go.jp/jma/kishou/know/yougo_hp/kion.html"),
        ],
    },
    {
        "slug": "emergency-numbers-japan",
        "title": "What are the emergency numbers in Japan for tourists?",
        "description": "119 for ambulance and fire, 110 for police, 118 for the coast guard, and the 24-hour Japan Visitor Hotline in English, Chinese and Korean.",
        "answer": "In Japan, call 119 for an ambulance or fire, 110 for the police, and 118 for the Japan Coast Guard (emergencies at sea). All three are free from any phone. The Japan Visitor Hotline, 050-3816-2787 (+81-50-3816-2787 from abroad), answers 24 hours a day, 365 days a year in English, Chinese and Korean, for accidents, illness, natural disasters and general help.",
        "body": """
<h2>The numbers</h2>
<table><thead><tr><th>Number</th><th>Who answers</th><th>Use it for</th></tr></thead><tbody>
<tr><td><b>119</b></td><td>Fire and Disaster Management (fire service)</td><td>Ambulance, fire, rescue</td></tr>
<tr><td><b>110</b></td><td>Police</td><td>Crime, traffic accidents, a person in danger</td></tr>
<tr><td><b>118</b></td><td>Japan Coast Guard</td><td>Emergencies at sea</td></tr>
<tr><td><b>050-3816-2787</b><br>(+81-50-3816-2787 from abroad)</td><td>Japan Visitor Hotline (JNTO)</td><td>24 hours, 365 days. English, Chinese, Korean. Accidents, illness, natural disasters, general help</td></tr>
<tr><td><b>03-3501-0110</b></td><td>Tokyo Metropolitan Police English helpline</td><td>Police matters in Tokyo</td></tr>
</tbody></table>
<h2>If you cannot make yourself understood</h2>
<p>The Fire and Disaster Management Agency's guide: <q>Please ask them to help you call if there are people who speak Japanese around you.</q> Hotel, station and shop staff will do this. The ambulance service is <q>available for anyone in Japan</q>.</p>
<h2>The one rule</h2>
<p><b>Say "Kyūkyū desu" (medical emergency) or "Kaji desu" (fire), then where you are.</b> If you do not know the address, <q>describe a nearby building or intersection as a landmark</q>. The full five-step 119 script and the list of symptoms that need an ambulance are in the manual.</p>
""",
        "sources": [
            ("Fire and Disaster Management Agency, Guide for Ambulance Services (English, PDF)", "https://www.fdma.go.jp/publication/portal/items/portal001_pamphiet_english.pdf"),
            ("JNTO, Japan Visitor Hotline", "https://www.japan.travel/en/plan/hotline/"),
            ("JNTO, Staying Safe in Japan", "https://www.japan.travel/en/plan/emergencies/"),
            ("Japan Coast Guard, 海の「事件・事故」は118番 (Japanese)", "https://www.kaiho.mlit.go.jp/info/kouhou/post-1274.html"),
        ],
    },
    {
        "slug": "evacuation-sites-and-shelters",
        "title": "What is the difference between an evacuation site and an evacuation shelter in Japan?",
        "description": "Designated emergency evacuation sites are where you go right now to survive a hazard; designated evacuation shelters are where you stay afterwards. Visitors can use both. What the national policy says about pets.",
        "answer": "Japan designates two kinds of place. A designated emergency evacuation site is where you go immediately to protect your life from an imminent hazard, designated per hazard (earthquake, tsunami, flood, storm surge, landslide), often open ground, high ground or a tall building. A designated evacuation shelter is an indoor facility, typically a school or gymnasium, where you stay for a period after a disaster. Visitors can use both. Evacuating with a pet is national policy, but whether the animal can come inside is decided by each shelter.",
        "body": """
<h2>Two kinds of place</h2>
<ul>
<li><b>Designated emergency evacuation site</b> (<i>shitei kinkyū hinan basho</i>): go <b>right now</b>. Designated per hazard, because a good place in an earthquake can be a bad one in a tsunami.</li>
<li><b>Designated evacuation shelter</b> (<i>shitei hinanjo</i>): a place to <b>stay</b> after a disaster. Schools, gymnasiums, community centers.</li>
</ul>
<p>Japan Disaster Guide maps 115,000+ designated sites from the national dataset, sorted by distance, with walking directions. Check which hazard a site is designated for before you head there.</p>
<h2>Visitors</h2>
<p>Shelters are opened by the municipality for anyone in the area who needs them. Tokyo also runs temporary shelters for stranded persons, facilities that <q>can accept stranded persons who have nowhere to go, usually for a period of three days</q>, <q>equipped with enough drinking water and food to last for three days, portable toilets, and other supplies</q>.</p>
<h2>Pets</h2>
<p>The Ministry of the Environment's policy is <i>dōkō hinan</i>, evacuating together with your pet, and it asks owners to get the animal used to a carrier and to bring enough water, food and regular medicine. Whether the animal can come inside the building is decided by each municipality and shelter; the ministry's advice is to check in advance. Ask at reception, and keep the animal in its carrier.</p>
<h2>The one rule</h2>
<p><b>Imminent danger: evacuation site for that hazard. Nowhere to stay: evacuation shelter.</b></p>
""",
        "sources": [
            ("Tokyo Metropolitan Government, Disaster Preparedness Tokyo (2023, English)", "https://www.bousai.metro.tokyo.lg.jp/_res/projects/default_project/_page_/001/029/136/tb2023_e_00.pdf"),
            ("Ministry of the Environment, ペットの災害対策 (Japanese)", "https://www.env.go.jp/nature/dobutsu/aigo/1_law/disaster.html"),
            ("Geospatial Information Authority of Japan, designated emergency evacuation sites data", "https://www.gsi.go.jp/bousaichiri/hinanbasho.html"),
        ],
    },
    {
        "slug": "reach-family-after-disaster",
        "title": "How do I reach my family after an earthquake in Japan?",
        "description": "Phone networks jam after a big earthquake. Japan's Disaster Emergency Message Dial 171, the free disaster Wi-Fi 00000JAPAN, and a one-message plan.",
        "answer": "After a large earthquake, calls fail first; text and data usually recover sooner. Send one short message to one person at home who relays it. Japan has a voice message board, Disaster Emergency Message Dial 171, switched on during disasters and keyed to a phone number in the affected area, and carriers open a free public Wi-Fi network called 00000JAPAN during major disasters. It is not encrypted, so keep it to safety messages.",
        "body": """
<h2>The one-message plan</h2>
<ol>
<li>One short message, not many calls, to one person who tells everyone else.</li>
<li>Agree the wording before you fly: "Safe, at hotel, will update at 20:00 JST".</li>
<li>Keep the phone alive: a power bank in your day bag.</li>
</ol>
<h2>171</h2>
<p>NTT's 171 is <q>a voice message board that is provided when a disaster such as an earthquake or volcanic eruption occurs</q>. Dial 171, press 1 to record or 2 to play back, then the phone number of the person in the affected area starting with the area code. As a traveler, use the number of the phone you carry in Japan and give it to your family in advance. The step-by-step sequence is in the manual.</p>
<h2>00000JAPAN</h2>
<p>When a large disaster hits, Japanese carriers open their public Wi-Fi under one network name, <b>00000JAPAN</b> (five zeros), for anyone. The council that runs it states it is not encrypted (<q>通信の暗号化等セキュリティへの対応は行っていません</q>) and asks users to keep it to emergency safety confirmation and information gathering.</p>
<h2>In the app</h2>
<p>Japan Disaster Guide can send one link that lets family see your status and location in a browser, no app or account needed on their side. This live safety link is part of the app's one-time Traveler Unlock (¥300 / $1.99); alerts, shelters and guides are free.</p>
""",
        "sources": [
            ("NTT East, Disaster Emergency Message Dial (171) (English)", "https://www.ntt-east.co.jp/en/saigai/voice171/"),
            ("Wireless LAN Business Promotion Council, 災害用統一SSID 00000JAPAN (Japanese)", "https://www.wlan-business.org/00000japan"),
        ],
    },
]

CSS = """
:root{--bg:#0F1420;--bg-2:#1A2130;--bg-3:#232C3D;--line:#2E3950;--text:#F5F7FA;--muted:#9AA6BB;--accent:#2F6FED;--accent-2:#3B9EF5;--ok:#33B27B}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
a{color:var(--accent-2)}.wrap{max-width:640px;margin:0 auto;padding:0 20px 48px}
.top{display:flex;align-items:center;gap:10px;padding:22px 0 6px;font-size:13px;letter-spacing:.04em;text-transform:uppercase;color:var(--muted)}.top img{width:26px;height:26px;border-radius:6px}.top a{color:var(--muted);text-decoration:none}
h1{font-size:28px;line-height:1.2;margin:10px 0 12px;letter-spacing:-.01em}
.answer{overflow-wrap:anywhere;background:var(--bg-2);border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:12px;padding:16px 18px;margin:0 0 22px;font-size:17px}
h2{font-size:18px;margin:26px 0 8px}p{margin:0 0 12px}q{quotes:"\\201C" "\\201D";color:var(--text)}
table{width:100%;border-collapse:collapse;margin:8px 0 14px;font-size:15px}th,td{text-align:left;vertical-align:top;padding:9px 10px;border-bottom:1px solid var(--line);overflow-wrap:anywhere}th{color:var(--muted);font-weight:600;font-size:13px;letter-spacing:.04em;text-transform:uppercase}
ul,ol{padding-left:20px}li{margin:6px 0}.tablewrap{overflow-x:auto}
.cta{border:1px solid var(--line);border-radius:14px;padding:18px;margin:28px 0 18px;background:var(--bg-2)}.cta h2{margin:0 0 6px;font-size:16px}.cta p{color:var(--muted);font-size:14px}
.btn{display:flex;align-items:center;justify-content:center;min-height:48px;padding:12px 16px;border-radius:12px;border:1px solid transparent;font-weight:600;text-decoration:none;color:#fff;background:var(--accent);margin:10px 0 0}.btn.secondary{background:var(--bg-3);border-color:var(--line);color:var(--text)}
.sources{font-size:13px;color:var(--muted);border-top:1px solid var(--line);padding-top:14px;margin-top:26px}.sources li{margin:4px 0}.sources a{color:var(--muted);word-break:break-all}
.more{margin-top:22px}.more ul{list-style:none;padding:0}.more li{margin:6px 0}.more a{text-decoration:none}
footer{margin-top:28px;color:var(--muted);font-size:12px}footer a{color:var(--muted)}
"""

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Japan Disaster Guide</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0F1420">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Japan Disaster Guide">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{site}assets/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" sizes="64x64" href="{site}assets/jdg-logo-64.png">
<script type="application/ld+json">{jsonld}</script>
{umami}
<style>{css}</style>
</head>
<body>
<div class="wrap">
<div class="top"><img src="{site}assets/jdg-logo-64.png" alt="" width="26" height="26"><a href="{site}">Japan Travel Safety Kit</a> · <a href="{site}guide/">Guides</a></div>
<h1>{title}</h1>
<p class="answer">{answer}</p>
<div class="tablewrap">{body}</div>
{note}
<div class="cta">
<h2>The live warnings, in your language</h2>
<p>Japan Disaster Guide is a free iPhone app that delivers JMA warnings for the places you save, after JMA confirms them, in 7 languages, with 115,000+ evacuation sites on a map.</p>
<a class="btn" href="{app}" data-event="click_appstore" data-vendor="guide-{slug}" rel="noopener">Free on the App Store</a>
<a class="btn secondary" href="{site}" data-event="click_index" data-vendor="guide-{slug}">See the Japan Travel Safety Kit</a>
<p style="margin-top:10px">The full procedures, the 119 script, shelter life, the 171 steps, 20 pointing cards and the worksheets are in the <b>Japan Travel Safety Manual</b> (PDF, coming September 2026).</p>
</div>
<div class="sources"><b>Sources</b> (read {today}; quotations are verbatim)<ol>{sources}</ol>
<p>Japan Disaster Guide is an independent app. It is not affiliated with the Japan Meteorological Agency or any government body. In an emergency, follow the instructions of local officials.</p></div>
<div class="more"><b>More guides</b><ul>{more}</ul></div>
<footer><a href="{site}">Japan Travel Safety Kit</a> · <a href="https://www.instagram.com/japandisasterchannel/" rel="noopener">@japandisasterchannel</a> · <a href="https://shintaro0619.github.io/jdg-web/privacy.html" rel="noopener">Privacy</a></footer>
</div>
<script>
(function(){{var p=new URLSearchParams(location.search),u={{}};['utm_source','utm_medium','utm_campaign'].forEach(function(k){{var v=p.get(k);if(v)u[k]=v.slice(0,64)}});
document.addEventListener('click',function(e){{var a=e.target.closest&&e.target.closest('a[data-event]');if(!a)return;var d=Object.assign({{vendor:a.getAttribute('data-vendor')||''}},u);if(window.umami&&umami.track){{try{{umami.track(a.getAttribute('data-event'),d)}}catch(x){{}}}}}});}})();
</script>
</body>
</html>
"""

INDEX_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Japan disaster warnings explained for travelers | Japan Disaster Guide</title>
<meta name="description" content="Short, sourced answers to the questions travelers ask about Japan's disaster warnings: alert levels, shindo, tsunami warnings, typhoon classes, heat alerts, emergency numbers, shelters and reaching family.">
<link rel="canonical" href="{site}guide/">
<meta name="theme-color" content="#0F1420">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Japan Disaster Guide">
<meta property="og:title" content="Japan disaster warnings explained for travelers">
<meta property="og:description" content="Sourced answers about Japan's alert levels, shindo, tsunami warnings, typhoons, heat alerts, emergency numbers, shelters and 171.">
<meta property="og:url" content="{site}guide/">
<meta property="og:image" content="{site}assets/og.png">
<link rel="icon" type="image/png" sizes="64x64" href="{site}assets/jdg-logo-64.png">
<script type="application/ld+json">{jsonld}</script>
{umami}
<style>{css}</style>
</head>
<body>
<div class="wrap">
<div class="top"><img src="{site}assets/jdg-logo-64.png" alt="" width="26" height="26"><a href="{site}">Japan Travel Safety Kit</a></div>
<h1>Japan's disaster warnings, explained for travelers</h1>
<p class="answer">Each page answers one question with the official definition, quoted as written from the Japanese source, and the one rule that follows from it.</p>
<div class="more"><ul>{list}</ul></div>
<div class="cta">
<h2>The live warnings, in your language</h2>
<p>Japan Disaster Guide is a free iPhone app that delivers JMA warnings for the places you save, after JMA confirms them, in 7 languages.</p>
<a class="btn" href="{app}" data-event="click_appstore" data-vendor="guide-index" rel="noopener">Free on the App Store</a>
<a class="btn secondary" href="{site}" data-event="click_index" data-vendor="guide-index">See the Japan Travel Safety Kit</a>
</div>
<footer><a href="{site}">Japan Travel Safety Kit</a> · <a href="https://www.instagram.com/japandisasterchannel/" rel="noopener">@japandisasterchannel</a> · <a href="https://shintaro0619.github.io/jdg-web/privacy.html" rel="noopener">Privacy</a></footer>
</div>
</body>
</html>
"""


def umami_tag():
    if not UMAMI:
        return ""
    return f'<script defer src="{CFG["analytics"].get("scriptUrl", "https://cloud.umami.is/script.js")}" data-website-id="{UMAMI}"></script>'


def jsonld_for(page, url):
    org = {"@type": "Organization", "name": "Japan Disaster Guide", "url": SITE,
           "sameAs": [CFG["site"]["instagram"], APP]}
    article = {
        "@type": "Article",
        "@id": url,
        "headline": page["title"],
        "description": page["description"],
        "inLanguage": "en",
        "datePublished": TODAY,
        "dateModified": TODAY,
        "author": org,
        "publisher": org,
        "mainEntityOfPage": url,
        "isPartOf": {"@type": "WebSite", "name": "Japan Disaster Guide", "url": SITE},
        "citation": [{"@type": "CreativeWork", "name": n, "url": u} for n, u in page["sources"]],
    }
    faq = {
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": page["title"],
                        "acceptedAnswer": {"@type": "Answer", "text": page["answer"]}}],
    }
    crumbs = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Japan Travel Safety Kit", "item": SITE},
        {"@type": "ListItem", "position": 2, "name": "Guides", "item": SITE + "guide/"},
        {"@type": "ListItem", "position": 3, "name": page["title"], "item": url},
    ]}
    return json.dumps({"@context": "https://schema.org", "@graph": [article, faq, crumbs]}, ensure_ascii=False)


def main():
    OUT.mkdir(exist_ok=True)
    urls = []
    for page in PAGES:
        url = f"{SITE}guide/{page['slug']}/"
        urls.append(url)
        more = "".join(f'<li><a href="{SITE}guide/{p["slug"]}/">{html.escape(p["title"])}</a></li>' for p in PAGES if p is not page)
        sources = "".join(f'<li>{html.escape(n)}. <a href="{u}" rel="noopener">{html.escape(u)}</a></li>' for n, u in page["sources"])
        note = f'<p style="color:var(--muted);font-size:13px">{html.escape(page["note"])}</p>' if page.get("note") else ""
        out = TEMPLATE.format(
            title=html.escape(page["title"]), description=html.escape(page["description"]), url=url, site=SITE,
            jsonld=jsonld_for(page, url), umami=umami_tag(), css=CSS, answer=html.escape(page["answer"]),
            body=page["body"], note=note, app=APP, slug=page["slug"], sources=sources, more=more, today=TODAY)
        d = OUT / page["slug"]
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(out, encoding="utf-8")
    lst = "".join(f'<li><a href="{p["slug"]}/">{html.escape(p["title"])}</a></li>' for p in PAGES)
    idx_ld = json.dumps({"@context": "https://schema.org", "@type": "CollectionPage", "name": "Japan's disaster warnings, explained for travelers",
                         "url": SITE + "guide/", "inLanguage": "en", "isPartOf": {"@type": "WebSite", "name": "Japan Disaster Guide", "url": SITE},
                         "hasPart": [{"@type": "Article", "headline": p["title"], "url": f"{SITE}guide/{p['slug']}/"} for p in PAGES]}, ensure_ascii=False)
    (OUT / "index.html").write_text(INDEX_TEMPLATE.format(site=SITE, jsonld=idx_ld, umami=umami_tag(), css=CSS, list=lst, app=APP), encoding="utf-8")
    # sitemap
    items = [(SITE, "1.0"), (SITE + "guide/", "0.8")] + [(u, "0.8") for u in urls]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, pr in items:
        sm.append(f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod><changefreq>weekly</changefreq><priority>{pr}</priority></url>")
    sm.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")
    print(f"wrote {len(PAGES)} guide pages + index; sitemap has {len(items)} urls")


if __name__ == "__main__":
    main()
