# Japan Travel Safety Kit

Static page for the second Instagram bio link of @japandisasterchannel.
Live: https://shintaro0619.github.io/safety-kit/

The spec is `~/disaster-app/marketing/SAFETY_KIT_BRIEF.md`. Decisions go to
`~/disaster-app/marketing/STATUS.md`.

## Files

| File | What |
|---|---|
| `index.html` | Page shell, styles, and the small renderer. No build step. |
| `kit.config.json` | **Every link, card, and piece of copy.** Edit this, not the HTML. |
| `assets/` | Logo sizes and the OG image (`og.png`, 1200x630). |

## Change a link or add a vendor (no code)

1. Open `kit.config.json`.
2. Find the card (`cards[].id` = `alerts`, `esim`, `power`, `insurance`) and the vendor under `options[]`.
3. Paste the affiliate URL into `url` and set `enabled` to `true`.
4. Commit and push to `main`. GitHub Pages rebuilds in about a minute.

A vendor with `enabled: false` or an empty `url` is not rendered. A card with
no enabled vendor is hidden entirely, so the page never shows a dead button.

Fields marked `_source` and `_program` are notes for us. The page ignores any
key that starts with `_`.

## In-app browsers

Instagram, Facebook, LINE and TikTok open links in an in-app browser without
tabs. There a `target="_blank"` link opens in a fresh context and the back
button cannot return to the Kit. The page detects those user agents (or
`?inapp=1` for testing) and navigates in the same view after a 150 ms delay so
the click event is sent first. Vendor pages that rewrite their own URL on load
(SafetyWing adds `selectedPlan=...`) trap the back button; give them the final
URL directly.

## Analytics

`analytics.websiteId` empty = no tracking script is loaded.
Paste an Umami Cloud website ID to enable it. Umami is cookieless, so no
consent banner is needed.

Events sent (all carry `utm_source`, `utm_medium`, `utm_campaign` from the
landing URL):

| Event | Fired by |
|---|---|
| `click_appstore` | App card button (and the hero CTA when `hero.showAppButton` is true) |
| `click_index` | The "What's in the kit" index under the hero (`vendor` = card id) |
| `click_esim` | Any eSIM vendor button (`vendor` = option id) |
| `click_power` | Any power bank vendor button (`vendor` = option id) |
| `click_insurance` | Any insurance vendor button (`vendor` = option id) |
| `click_coffee` | Buy Me a Coffee button |
| `click_other` | Footer links (`target` = link id) |

Page views are counted by Umami automatically.

## Links to put in Instagram

| Where | URL |
|---|---|
| Bio link 2 | `https://shintaro0619.github.io/safety-kit/?utm_source=instagram&utm_medium=bio` |
| Story link sticker | `https://shintaro0619.github.io/safety-kit/?utm_source=instagram&utm_medium=story` |

Bio link 1 stays the App Store URL. Do not replace it.

## App Store campaign link (optional)

If `appStore.campaign.pt` is set, every App Store link becomes
`...?pt=<pt>&ct=safety_kit&mt=8`, and App Store Connect reports installs from
this page separately under App Analytics > Campaigns.

## Guardrails (from the brief)

- No superlatives or unsourced comparisons ("cheapest", "fastest", "must-have").
- Vendor facts come from the vendor's own page. Record the URL and date in `_source`.
- Do not show prices. They change and go stale.
- Affiliate disclosure stays next to every partner button and at the bottom.
- Four cards only: alerts, eSIM, power bank, insurance. Physical goods link to the buyer's home-country store (Amazon OneLink or a brand store with country sites); never assume shipping from Japan.
