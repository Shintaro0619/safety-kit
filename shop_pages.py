"""Shop sections and Tips pages (posted reels only: Parts 1-5).

Paid-manual-only content (day-bag list, hotel 10-minute check, contact sheet) must not appear here.
"""

SHOP = [
    {
        "slug": "power",
        "menu": "Power",
        "title": "Power for a blackout in Japan",
        "description": "A power bank you can take on a plane and a home power station, with the maker's own figures and Japan's flight rules for power banks.",
        "intro": "Japan's flight rules for power banks (Ministry of Land, Infrastructure, Transport and Tourism, from 24 April 2026): carry-on only, never in checked bags; up to 2 per person, each 160 Wh or less; do not charge the power bank or charge anything from it during the flight. Japanese airlines also ask you to keep it with you, not in the overhead bin. Your airline may have stricter rules.",
        "items": ["buffalo-bmpbsa10000", "jackery-1000-new"],
        "sources": [
            ("Ministry of Land, Infrastructure, Transport and Tourism, press release, 14 April 2026 (Japanese)", "https://www.mlit.go.jp/report/press/kouku10_hh_000310.html"),
            ("Ministry of Land, Infrastructure, Transport and Tourism, press release, 1 July 2025 (Japanese)", "https://www.mlit.go.jp/report/press/kouku10_hh_000284.html"),
        ],
    },
    {
        "slug": "lights",
        "menu": "Lights",
        "title": "Lights for a power cut in Japan",
        "description": "A flashlight, a headlamp and a lantern that all run on AA batteries, with the maker's own figures.",
        "intro": "All three run on AA batteries, which convenience stores in Japan sell. Keep spare batteries with them. Figures are from the maker's own pages.",
        "items": ["gentos-sr-320dt", "gentos-cp-131d", "gentos-ex-236d"],
    },
    {
        "slug": "water-toilet",
        "menu": "Water & toilet",
        "title": "Water and toilets when the water is off",
        "description": "Emergency toilet bags for the toilet you already have, and a 10 L water jug with a tap, with the maker's own figures.",
        "intro": "When the water stops, toilets stop too. These bags go over the toilet you already have. A folding jug helps you carry water from a water station; 10 L of water weighs about 10 kg, so fill only what you can carry.",
        "items": ["bos-15", "bos-50", "captainstag-m-1481"],
    },
    {
        "slug": "cooking",
        "menu": "Cooking",
        "title": "Cooking without gas or power at home",
        "description": "An Iwatani cassette stove and cans for indoor home use, plus outdoor stoves for a garden or balcony, each listed with the gas it takes.",
        "intro": "For people who live in Japan. Each stove is listed with the gas its maker says to use; Iwatani and SOTO both say to use their own cans. Gas cans can't go on a plane, in carry-on or checked bags (ANA), so visitors should buy and use them in Japan only.",
        "items": ["iwatani-cb-ts-5", "iwatani-gas-12", "iwatani-toughmaru-jr", "iwatani-toughmaru", "soto-st-310", "soto-power-gas"],
        "sources": [
            ("Iwatani, how to use cassette stoves (Japanese)", "https://www.iwatani.co.jp/jpn/consumer/products/cg/useful/howto/"),
            ("ANA, restricted items, international flights (Japanese)", "https://www.ana.co.jp/ja/jp/international/prepare/baggage/limit/caution-restriction.html"),
        ],
    },
    {
        "slug": "kit",
        "menu": "Disaster kit",
        "title": "A ready-made disaster kit",
        "description": "A 30-item disaster backpack whose maker publishes the full list of contents.",
        "intro": "For people who live in Japan. The maker publishes the full list of what is inside. It has no food or water, so add your own.",
        "items": ["yamazen-ybg-30"],
    },
    {
        "slug": "whistle",
        "menu": "Whistle",
        "title": "A whistle for when you are trapped",
        "description": "A pealess whistle, and why Japanese guides say to use one instead of shouting if you are trapped.",
        "intro": "Japanese local governments say shouting uses up your strength if you are trapped, and a small whistle needs only a little breath. See Disaster Tips, Part 3.",
        "items": ["fox40-classic"],
    },
]

TIPS = [
    {
        "slug": "no-power-no-water",
        "short": 'No power or water? 3 small tricks',
        "posted": "2026-11-03",
        "part": 1,
        "title": "Disaster Tips, Part 1: no power or no water",
        "description": "Three small tricks from official Japanese guides for a power cut or a water outage: a flashlight lantern, wrap on plates, and cleaning teeth without a toothbrush.",
        "answer": "A how-to, not a current alert. Three small tricks from official Japanese guides for when the power or the water is off: turn a flashlight into a lantern, keep plates clean without water, and clean your teeth without a toothbrush.",
        "body": """
<h2>1. No lantern?</h2>
<ul>
<li>Put a white plastic bag over a flashlight and tie the handles to it. The light spreads through the whole bag (Okayama learning site; Tokyo Metropolitan Government, 2015 guide).</li>
<li>If the flashlight gets warm, take the bag off. This is our own suggestion; the guides we read do not cover it.</li>
</ul>
<h2>2. No water for dishes?</h2>
<ul>
<li>Line the plate with plastic wrap (Tokyo Metropolitan Government; Japan's farm ministry).</li>
<li>After the meal, throw away only the wrap. The plate is ready for the next meal (Yamanashi Prefecture).</li>
<li>For hot food, the ministry suggests aluminum foil as a plate.</li>
</ul>
<h2>3. No toothbrush?</h2>
<ul>
<li>After a meal, rinse with a little water or tea.</li>
<li>Wipe your teeth with a tissue or handkerchief. It still helps (Chiba Prefecture, from Japan's health ministry).</li>
<li>Tokyo's guide: wrap gauze or tissue around a finger, wipe your gums and tongue too, then rinse.</li>
</ul>
""",
        "gear_intro": "The lantern trick needs a flashlight. If you live in Japan, a lantern and a water jug help for a longer outage.",
        "items": ["gentos-sr-320dt", "gentos-ex-236d", "captainstag-m-1481"],
        "shops": ["lights", "water-toilet"],
        "sources": [
            ("Okayama Prefecture, Manabi-to Search, OKAYAMA Ouchi Lab sheet (Japanese, PDF)", "https://www.okayama-c.ed.jp/manabi-to-search/wp-content/uploads/2021/10/005081.pdf"),
            ("Tokyo Metropolitan Government, Disaster Preparedness Tokyo (2015), Survival Tips (English, PDF)", "https://www.bousai.metro.tokyo.lg.jp/book/pdf/en/04_Survival_Tips.pdf"),
            ("Tokyo Metropolitan Government, Tokyo Bosai (2023), pp.106-147 (Japanese, PDF)", "https://www.bousai.metro.tokyo.lg.jp/_res/common/2023_bk/tb/tb2023_106_147.pdf"),
            ("Ministry of Agriculture, Forestry and Fisheries, home food stock guide, chapter 8 (Japanese)", "https://www.maff.go.jp/j/zyukyu/foodstock/chapter08.html"),
            ("Yamanashi Prefecture, disaster food material (Japanese, PDF)", "https://www.pref.yamanashi.jp/documents/6568/siryou2_saigai.pdf"),
            ("Chiba Prefecture, oral care in a disaster, from the Ministry of Health, Labour and Welfare e-Health Net (Japanese, PDF)", "https://www.pref.chiba.lg.jp/kenzu/documents/saigaikoukuukea_1.pdf"),
        ],
    },
    {
        "slug": "free-wifi-00000japan",
        "short": 'Free disaster Wi-Fi: 00000JAPAN',
        "posted": "2026-11-04",
        "part": 2,
        "title": "Disaster Tips, Part 2: free disaster Wi-Fi 00000JAPAN",
        "description": "After a big disaster in Japan, look for the free Wi-Fi called 00000JAPAN. What it is, when it is switched on, and how to stay safe on it.",
        "answer": "A how-to, not a current alert. After a big disaster in Japan, mobile phones can be hard to use. Look for the free disaster Wi-Fi called 00000JAPAN.",
        "body": """
<h2>What it is</h2>
<ul>
<li>Wi-Fi name: 00000JAPAN (five zeros, then JAPAN).</li>
<li>Free for anyone. No password, no sign-up.</li>
<li>Wi-Fi owners switch it on in big disasters. Since 2023 it can also be switched on during major phone network outages.</li>
<li>It isn't meant for normal days, and each owner decides when and where to turn it on.</li>
<li>Recent examples: the July 2026 Kumamoto earthquake (all of Kumamoto Prefecture) and the August 2026 heavy rain in Uozu, Toyama.</li>
</ul>
<h2>Stay safe on it</h2>
<ul>
<li>It is not encrypted. Use it to check news and contact family.</li>
<li>Avoid entering IDs, passwords or card details, and avoid bank apps. If you must, use a secure app, HTTPS or a VPN.</li>
<li>You may see 00000JAPAN and still not connect. Speed is not guaranteed.</li>
<li>Some Wi-Fi spots open their usual network instead, without the sign-up ("disaster mode").</li>
</ul>
<p>Japan's Ministry of Internal Affairs and Communications describes 00000JAPAN as a private-sector program run under the guidelines of the Wireless LAN Business Promotion Council (Wi-Biz).</p>
""",
        "gear_intro": "Wi-Fi only helps if your phone still has power. A power bank you can take on the plane:",
        "items": ["buffalo-bmpbsa10000"],
        "shops": ["power"],
        "sources": [
            ("Wireless LAN Business Promotion Council (Wi-Biz), 00000JAPAN", "https://www.wlan-business.org/00000japan"),
            ("Wi-Biz, 00000JAPAN for users", "https://www.wlan-business.org/00000japan/for_users"),
            ("Wi-Biz, 00000JAPAN activation news", "https://www.wlan-business.org/archives/category/00000japan"),
            ("Ministry of Internal Affairs and Communications, free Wi-Fi 00000JAPAN (Japanese)", "https://www.soumu.go.jp/menu_seisaku/ictseisaku/public_wi-fi/freewifi_00000japan.html"),
        ],
    },
    {
        "slug": "trapped-sos",
        "short": "Trapped after a quake? Don't keep shouting",
        "posted": "2026-11-06",
        "part": 3,
        "title": "Disaster Tips, Part 3: trapped after an earthquake",
        "description": "If you are trapped after a big earthquake in Japan, don't keep shouting. What Japanese local governments say to do instead.",
        "answer": "A how-to, not a current alert. If you are trapped after a big earthquake in Japan, don't keep shouting.",
        "body": """
<h2>Why not shout?</h2>
<ul>
<li>Shouting non-stop uses up your strength and can put your life at risk (Tokyo Metropolitan Government).</li>
<li>Hit a door or wall with something hard, or make another loud noise, so people know you're inside.</li>
</ul>
<h2>Pinned under something?</h2>
<ul>
<li>With your chest pressed, it's hard to shout loudly (Shimane Prefecture).</li>
<li>A small disaster whistle lets you tell people you're there with only a little breath (Shimane Prefecture, Niiza City).</li>
</ul>
<h2>Keep it close</h2>
<ul>
<li>Put a whistle by your pillow (Nagakute City).</li>
<li>Tokyo also suggests practicing finger whistling.</li>
</ul>
<h2>Stuck on a high floor?</h2>
<ul>
<li>Reflect light with a mirror.</li>
<li>Write SOS and where you are on paper, and drop it to the ground.</li>
<li>Make noise (Tokyo Metropolitan Government).</li>
</ul>
""",
        "gear_intro": "A whistle to keep by your pillow, and a kit that has one inside:",
        "items": ["fox40-classic", "yamazen-ybg-30"],
        "shops": ["whistle", "kit"],
        "sources": [
            ("Tokyo Metropolitan Government, Tokyo Bosai (2023), pp.208-275 (Japanese, PDF)", "https://www.bousai.metro.tokyo.lg.jp/_res/common/2023_bk/tb/tb2023_208_275n.pdf"),
            ("Shimane Prefecture, earthquake basics (Japanese)", "https://www.pref.shimane.lg.jp/bousai_info/bousai/kenchiku/quake/yobichishiki.html"),
            ("Niiza City, home stockpile (Japanese)", "https://www.city.niiza.lg.jp/site/bousai/bitiku.html"),
            ("Nagakute City, disaster preparation (Japanese)", "https://www.city.nagakute.lg.jp/soshiki/kurashibunkabu/anshinanzenka/1/2/bosai_category/saigai/4816.html"),
        ],
    },
    {
        "slug": "disaster-message-171",
        "short": '171: leave a voice message when calls jam',
        "posted": "2026-11-14",
        "part": 4,
        "title": "Disaster Tips, Part 4: the 171 disaster message line",
        "description": "How to record and listen to a voice message on 171, Japan's disaster message line, and web171 in English. Try days every month.",
        "answer": "A how-to, not a current alert. After a big quake, calls to the area can jam. 171, Japan's disaster message line, keeps voice messages instead.",
        "body": """
<h2>What it is (NTT East, NTT West)</h2>
<ul>
<li>A voice message line for big disasters. Each message is up to 30 seconds.</li>
</ul>
<h2>To record</h2>
<ul>
<li>Dial 171, then 1.</li>
<li>Enter the phone number from the area code: your home number, or the number of the person in the area.</li>
<li>On a push-button phone, press 1, then speak after the beep.</li>
</ul>
<h2>To listen</h2>
<ul>
<li>Dial 171, then 2, then the same number, then 1.</li>
</ul>
<h2>Good to know</h2>
<ul>
<li>The voice guide is in Japanese only.</li>
<li>You can't call 171 from abroad.</li>
<li>It works from mobile phones too. Call charges depend on your phone company.</li>
<li>web171 (web171.jp) lets you post and read messages online, in English, Korean or Chinese, and it works from abroad.</li>
</ul>
<h2>Try it</h2>
<p>Anyone in Japan can try 171 on the 1st and 15th of every month, on 1-3 January, and during two disaster-prep weeks. Try days may not run while a real disaster is going on.</p>
""",
        "gear_intro": "171 and web171 need a phone with battery left:",
        "items": ["buffalo-bmpbsa10000", "jackery-1000-new"],
        "shops": ["power"],
        "sources": [
            ("NTT East, disaster message dial 171 (Japanese)", "https://www.ntt-east.co.jp/saigai/voice171/"),
            ("NTT East, 171 Q&A (Japanese)", "https://www.ntt-east.co.jp/saigai/qa_voice171/v_09.html"),
            ("NTT East, web171 Q&A (Japanese)", "https://www.ntt-east.co.jp/saigai/qa_web171/w_04.html"),
            ("NTT West, how to record (Japanese)", "https://www.ntt-west.co.jp/dengon/way/rec.html"),
            ("web171", "https://www.web171.jp/"),
        ],
    },
    {
        "slug": "call-119",
        "short": 'How to call 119 in Japan',
        "posted": "2026-11-12",
        "part": 5,
        "title": "Disaster Tips, Part 5: how to call 119 in Japan",
        "description": "119 for fire and ambulance, 110 for police: what the operator asks, phone interpreters, and calling from a mobile without an address.",
        "answer": "A how-to, not a current alert. In Japan, 119 is fire and ambulance, and 110 is police (JNTO).",
        "body": """
<h2>What they ask, in order (Tokyo Fire Department)</h2>
<ul>
<li>"Fire or ambulance?" Answer "Kaji desu" (fire) or "Kyukyu desu" (ambulance).</li>
<li>The address the fire truck or ambulance should go to. In a hotel: its name, address and room number.</li>
<li>For a fire: what is burning. For an ambulance: what happened and the person's age.</li>
<li>Your name, and sometimes your phone number.</li>
<li>If it is very urgent, the ambulance may be sent before all the questions are done.</li>
</ul>
<h2>No Japanese?</h2>
<ul>
<li>Most fire departments can add a phone interpreter to the call, 24 hours, in main languages. 673 of Japan's 720 fire departments had this as of 1 January 2025 (FDMA).</li>
<li>In Tokyo the languages are English, Chinese, Korean, Portuguese and Spanish.</li>
</ul>
<h2>Calling from a mobile</h2>
<ul>
<li>No address? Name a building, a shop, a crossing, or a station and platform.</li>
<li>Keep your phone on until help arrives. The ambulance crew may call you back.</li>
</ul>
<p>Not an emergency? JNTO's Japan Visitor Hotline: 050-3816-2787, 24 hours, in English, Chinese and Korean, for accidents, illness, disasters and travel information.</p>
""",
        "gear_intro": "The crew may call you back, so keep your phone charged:",
        "items": ["buffalo-bmpbsa10000"],
        "shops": ["power"],
        "sources": [
            ("Fire and Disaster Management Agency (FDMA), three-way phone interpreting (Japanese)", "https://www.fdma.go.jp/mission/enrichment/gaikokujin_syougaisya_torikumi/sanshakan-douji-tsuuyaku.html"),
            ("Tokyo Fire Department, how to call 119 (Japanese)", "https://www.tfd.metro.tokyo.lg.jp/lfe/119/119.html"),
            ("Tokyo Metropolitan Government, emergency calls (English)", "https://www.hokeniryo.metro.tokyo.lg.jp/iryo/iryo_hoken/medical_info_eng/emergency_call"),
            ("JNTO, Japan Visitor Hotline", "https://www.japan.travel/en/plan/hotline/"),
        ],
    },
]
