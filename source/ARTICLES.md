# Weekly article routine — andikimran.com

Andik Imran is a PropNex property consultant in Singapore (CEA R061801F, agent since 2019, Malay & English).
Each week he gives ONE real input (a client question, a deal story, a voice note or a TikTok/IG video script).
That input becomes ONE article on andikimran.com. Nothing is published without his explicit approval.

## The weekly steps

1. Ask Andik (short, friendly, one message): "What did a client ask you this week? Send a voice note, a few lines, or the script of a video you made."
   - If he doesn't reply, do nothing. Skipping a week is fine. Never publish anything he didn't provide.
2. Turn his input into a draft article:
   - Pick the real question as the headline. First person, his voice: calm, warm, practical, plain English, a little Malay is fine ("boleh", "Mak and Abah"). No hype, no "best agent" claims, no talk of commission.
   - Open with a 2–3 sentence "Short answer" box, then 3–5 short sections with clear h2 headings, then 2–4 FAQs.
   - Use only details he gave. Never invent clients, prices, results or quotes. Anonymise clients (no names, no block numbers unless he says so).
   - Check every rule, number or deadline (HDB, CPF, IRAS, MAS, CEA) against official sources with web search before stating it. If unsure, leave it out or say "check the latest rules".
   - Link to 2–3 relevant existing pages (see keys below) and end on the free Sale Check / WhatsApp.
   - 600–1,000 words. Commodity summaries of what's already online are worthless; the value is his first-hand experience.
3. Send Andik the draft to read (title, short answer, full text). Ask: "OK to publish, or any changes?"
4. Only after he clearly approves:
   - Add one dict at the TOP of `ARTICLES` in `source/content_articles.py` (format is documented in that file). `body` is HTML using `<h2 id="…">`, `<p>`, `<ul>`, `<div class="answer"><b>Short answer</b>…</div>` and `<div class="note"><b>…</b> …</div>`. `slug` = short, lowercase, hyphenated, keyword-led.
   - `cd source && python3 build.py prod` (regenerates the site at the repo root; never edit generated HTML by hand).
   - Check: no errors, `guides/<slug>.html` exists, sitemap includes it.
   - Commit ("Add article: <title>") and push to `main`. Vercel deploys automatically in ~1 minute.
   - Reply to Andik with the live link: https://andikimran.com/guides/<slug>

## Link keys for `related` and `{{L:key}}` links inside body
home, about, reviews, safe, newlaunch, salecheck, calculator, guides, malay,
g-upgrade, g-faraid, g-divorce, g-rightsize, g-first, g-hdb2hdb, g-hdb2pvt, g-hdb2nl, g-ssd,
e-yishun, e-punggol, e-sengkang, e-tampines, e-pasirris, estates.
In body HTML write links as `<a href="{{L:g-upgrade}}">…</a>`.

## Compliance
- CEA: no misleading claims or superlatives; no unconditional promises.
- Google: one genuine article beats many generic ones; never mass-produce pages.
- General-information disclaimer is added automatically by the article template.
