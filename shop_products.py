"""Product cards for the shop and tips pages.

Facts come only from the maker's own page (the "source" URL). No prices, no ratings, no superlatives.
Rakuten link HTML for each key lives in rakuten_links/<key>_image.html and _text.html.
"""

PRODUCTS = {
    # --- power ---
    "buffalo-bmpbsa10000": {
        "name": "BUFFALO BMPBSA10000 power bank (semi-solid battery)",
        "asin": "B0GQSW1DSL",
        "kind": "Power bank",
        "for": "Travelers and residents",
        "facts": [
            "37 Wh (10,000 mAh at 3.7 V), so it is under the 160 Wh limit for carry-on",
            "Built-in USB-C cable (about 23 cm) plus a USB-C port; up to 30 W from one port",
            "About 210 g",
            "The maker marks it PSE compliant (Japan's electrical safety law)",
        ],
        "source": "https://www.buffalo.jp/product/detail/bmpbsa10000whx.html",
    },
    "jackery-1000-new": {
        "name": "Jackery Portable Power Station 1000 New (JE-1000D)",
        "asin": "B0D3HJM175",
        "kind": "Portable power station",
        "for": "Residents",
        "facts": [
            "1,070 Wh, 1,500 W rated output",
            "Lithium iron phosphate battery; the maker rates it for about 4,000 charge cycles",
            "About 10.8 kg, 327 x 224 x 247 mm",
        ],
        "source": "https://www.jackery.jp/products/explorer-1000-new",
    },
    # --- lights ---
    "gentos-sr-320dt": {
        "name": "GENTOS SR-320DT flashlight",
        "asin": "B0C32X7312",
        "kind": "Flashlight",
        "for": "Travelers and residents",
        "facts": ["300 lumens, about 8 hours", "4 AA alkaline batteries", "Dust-tight and waterproof to 25 m (IP68 rating), 1 m drop tested", "About 195 g with batteries"],
        "source": "https://www.gentos.jp/products/series/sr_flashlight/sr-320dt/",
    },
    "gentos-cp-131d": {
        "name": "GENTOS CP-131D headlamp",
        "asin": "B0D3TDHHGM",
        "kind": "Headlamp",
        "for": "Travelers and residents",
        "facts": ["200 lumens for about 7.5 hours, or 70 lumens for about 15 hours", "1 AA alkaline battery", "Dust-tight and water-resistant (IP66 rating), 2 m drop tested", "About 85 g with the battery"],
        "source": "https://www.gentos.jp/products/series/compact_headlight/cp-131d/",
    },
    "gentos-ex-236d": {
        "name": "GENTOS Explorer EX-236D lantern",
        "asin": "B08TQ87BWD",
        "kind": "Lantern",
        "for": "Residents",
        "facts": ["430 lumens for about 10 hours, or 20 lumens for about 142 hours", "6 AA alkaline batteries", "Waterproof to 1 m (IP68 rating), floats, 2 m drop tested", "About 355 g with batteries"],
        "source": "https://www.gentos.jp/products/series/explorer/ex-236d/",
    },
    # --- water and toilet ---
    "bos-15": {
        "name": "BOS emergency toilet set, 15 uses",
        "asin": "B088813DMP",
        "kind": "Emergency toilet",
        "for": "Travelers and small households",
        "facts": [
            "Bags that go over the toilet you already have, with no water or power",
            "Comes with BOS odor-proof bags for the used bags",
            "The bag opening is 140 cm around; the maker says some large or special toilets may not fit",
            "The maker suggests replacing it after 15 years",
        ],
        "source": "https://www.kurilon.co.jp/product/toilet/",
    },
    "bos-50": {
        "name": "BOS emergency toilet set, 50 uses",
        "asin": "B088BKW851",
        "kind": "Emergency toilet",
        "for": "Residents",
        "facts": [
            "Bags that go over the toilet you already have, with no water or power",
            "Comes with BOS odor-proof bags, so used bags can wait at home if rubbish collection stops",
            "The bag opening is 140 cm around; the maker says some large or special toilets may not fit",
            "The maker suggests replacing it after 15 years",
        ],
        "source": "https://www.kurilon.co.jp/product/toilet/",
        "note": "On Amazon.co.jp this is sold by the maker's own shop and can take 2-3 weeks to ship.",
    },
    "captainstag-m-1481": {
        "name": "Captain Stag M-1481 water jug, 10 L",
        "asin": "B000AR4SLK",
        "kind": "Water container",
        "for": "Residents",
        "facts": ["Folding jug with a built-in tap", "Antibacterial polyethylene (inorganic agent)", "In use 240 x 240 x 240 mm; folded 70 mm thick"],
        "source": "https://www.captainstag.net/products/M-1481.html",
    },
    # --- cooking ---
    "iwatani-cb-ts-5": {
        "name": "Iwatani Cassette-Fu Tatsujin Slim V cassette stove, with case (CB-TS-5-A)",
        "asin": "B0FFT6J4HJ",
        "kind": "Cassette stove for indoor home use",
        "for": "Residents",
        "facts": [
            "3.4 kW; one can lasts about 68 minutes on high (maker's test at 20-25 C)",
            "Uses Iwatani cassette gas",
            "Pressure-sensing and can-fitting safety devices",
            "About 1.3 kg, made in Japan. The maker says never to use it in a tent or a car",
        ],
        "source": "https://www.iwatani.co.jp/jpn/consumer/products/cg/stove/cb-ts-5/",
    },
    "iwatani-gas-12": {
        "name": "Iwatani cassette gas (orange, CB-250-OR), 12 cans",
        "asin": "B0757DQQ74",
        "kind": "Cassette gas",
        "for": "Residents",
        "facts": [
            "250 g of butane per can, for Iwatani Cassette-Fu stoves",
            "Iwatani says to use within about 7 years of the date printed on the base of the can",
            "Iwatani's own guide: use and replace them as you go (rolling stock)",
        ],
        "source": ["https://www.iwatani.co.jp/jpn/consumer/products/cg/cb/cb-250-or/", "https://www.iwatani.co.jp/jpn/consumer/products/cg/useful/bombe/"],
    },
    "iwatani-toughmaru-jr": {
        "name": "Iwatani Toughmaru Jr. outdoor stove (CB-ODX-JR)",
        "asin": "B09HGDZPNG",
        "kind": "Outdoor cassette stove",
        "for": "Residents with a garden or balcony",
        "facts": [
            "2.3 kW; about 102 minutes per can of Iwatani cassette gas",
            "Takes the same orange Iwatani cassette gas as the home stove above",
            "About 1.6 kg. The maker says never to use it in a tent or a car",
        ],
        "source": "https://www.iwatani.co.jp/jpn/consumer/products/cg/outdoor/cb-odx-jr/",
    },
    "iwatani-toughmaru": {
        "name": "Iwatani Toughmaru outdoor stove (CB-ODX-1)",
        "asin": "B09N8M294G",
        "kind": "Outdoor cassette stove",
        "for": "Residents with a garden or balcony",
        "facts": [
            "3.3 kW; about 75 minutes per can",
            "Takes Iwatani cassette gas",
            "About 2.4 kg. The maker says never to use it in a tent or a car",
        ],
        "source": "https://www.iwatani.co.jp/jpn/consumer/products/cg/outdoor/cb-odx-1/",
    },
    "soto-st-310": {
        "name": "SOTO Regulator Stove ST-310",
        "asin": "B077Q99XBS",
        "kind": "Outdoor stove",
        "for": "Residents with a garden or balcony",
        "facts": [
            "Outdoor use only (the maker says so)",
            "2.9 kW; about 1.5 hours per can of SOTO gas (maker's figure)",
            "330 g, made in Japan",
            "Uses SOTO's own cassette gas only",
        ],
        "source": "https://soto.shinfuji.co.jp/products/st-310/",
        "note": "On Rakuten Ichiba this link is a set: the stove plus SOTO gas.",
    },
    "soto-power-gas": {
        "name": "SOTO Power Gas (cassette gas for SOTO stoves)",
        "asin": "B001GCIYKY",
        "kind": "Cassette gas",
        "for": "Residents who have a SOTO stove",
        "facts": [
            "240 g per can, butane and propane",
            "For SOTO stoves that take cassette gas",
        ],
        "source": "https://soto.shinfuji.co.jp/products/st-7601/",
        "note": "Pack sizes differ: the Rakuten Ichiba link is three 3-can packs.",
    },
    # --- kit and whistle ---
    "yamazen-ybg-30": {
        "name": "YAMAZEN disaster bag, 30 items (YBG-30)",
        "asin": "B07RMWHK7J",
        "kind": "Disaster kit in a backpack",
        "for": "Residents",
        "facts": [
            "No food or water inside; keep those separately",
            "Includes a whistle, a 2-way flashlight, 3 portable toilets, a rain poncho, an aluminum blanket, a water bag and plastic wrap",
            "The maker says the contents may change",
        ],
        "source": "https://book.yamazen.co.jp/product/detail/I00005070",
        "note": "Same 30-item set in two colors: black on Amazon.co.jp, red on Rakuten Ichiba.",
    },
    "fox40-classic": {
        "name": "Fox 40 Classic whistle",
        "asin": "B000RNQQH6",
        "kind": "Whistle",
        "for": "Travelers and residents",
        "facts": [
            "115 dB (maker's figure)",
            "No ball inside (pealess), which the maker says resists jamming and freezing; it clears itself of water",
        ],
        "source": "https://www.fox40world.com/classic",
    },
}
