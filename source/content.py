# All words on the site live here. Edit copy here, then run: python3 build.py prod
# Placeholders: {{L:key}} link, {{IMG:file}} image url, {{PIC:file|alt}} <img>, {{WA:message}} WhatsApp link

SITE = {
    "domain": "https://andikimran.com",
    "wa": "6587368736",
    # TODO(Andik): replace with your Google Business Profile review link (Google > your profile > "Ask for reviews" / share link)
    "google_reviews": "https://www.google.com/maps?cid=16863621726073548887",
    "same_as": [
        "https://www.homeswithaims.com",
        "https://www.instagram.com/andikimran/",
        "https://www.instagram.com/homeswithaims/",
        "https://www.tiktok.com/@andikimran",
        "https://www.google.com/maps?cid=16863621726073548887",
    ],
    # TODO(Andik): paste your GA4 snippet here when ready (leave empty to skip)
    "analytics": "",
    "llms": """# Andik Imran — property agent, Singapore

> Andik Imran is a PropNex property agent (Associate Group Director, CEA Reg. R061801F) in Singapore. Agent since 2019, 100+ families helped to sell, buy and rent, 65+ five-star Google reviews. He helps people buy, sell and rent homes across Singapore, in English and Malay: first-time buyers, HDB upgraders, new launch buyers and rightsizers, and he specialises in complicated cases: inherited flats and faraid, estate sales, divorce and rightsizing. He works with his wife Mirta Syazanna (CEA Reg. R070524E) as Homes with AIMS. Contact: WhatsApp +65 8736 8736.

## Key pages
- [Home](https://andikimran.com/): who Andik helps and how
- [SAFE Upgrading Plan](https://andikimran.com/safe-upgrading-plan): his method for upgrading without financial stretch
- [Free Sale Check](https://andikimran.com/sale-check): free estimate of sale price and cash proceeds via WhatsApp
- [New launch](https://andikimran.com/new-launch): planning an HDB-to-condo/EC upgrade
- [Reviews](https://andikimran.com/reviews): client stories and Google reviews
- [About](https://andikimran.com/about): background and credentials
- [Malay property agent](https://andikimran.com/malay-property-agent): Malay-speaking help for buying, selling, upgrading and faraid cases

## Guides
- [Selling an inherited HDB flat (faraid, wills, estate)](https://andikimran.com/guides/inherited-hdb-flat-faraid)
- [Selling an HDB flat during a divorce](https://andikimran.com/guides/selling-hdb-flat-divorce)
- [Upgrading from HDB after MOP: sell first or buy first](https://andikimran.com/guides/upgrading-from-hdb-after-mop)
- [Rightsizing your HDB flat](https://andikimran.com/guides/rightsizing-hdb-flat)
- [First-time home buyer guide](https://andikimran.com/guides/first-time-home-buyer-guide)
- [HDB to HDB upgrade timeline and payments](https://andikimran.com/guides/hdb-to-hdb-upgrade-timeline)
- [HDB to private resale timeline, ABSD and SSD](https://andikimran.com/guides/hdb-to-private-resale-timeline)
- [HDB to new launch timeline and progressive payments](https://andikimran.com/guides/hdb-to-new-launch-timeline)
- [Seller's Stamp Duty (SSD) rates and calculator](https://andikimran.com/guides/sellers-stamp-duty-ssd)

## Estate guides
- [Property agent in Yishun](https://andikimran.com/property-agent/yishun)
- [Property agent in Punggol](https://andikimran.com/property-agent/punggol)
- [Property agent in Sengkang](https://andikimran.com/property-agent/sengkang)
- [Property agent in Tampines](https://andikimran.com/property-agent/tampines)
- [Property agent in Pasir Ris](https://andikimran.com/property-agent/pasir-ris)

## Tools
- [Home loan calculator (TDSR, MSR, LTV, stress test)](https://andikimran.com/loan-calculator)
""",
}

SKYLINE = '''<svg class="skyline" viewBox="0 0 1200 120" preserveAspectRatio="none" aria-hidden="true">
<defs><pattern id="win" width="14" height="12" patternUnits="userSpaceOnUse"><rect x="3" y="3" width="6" height="4" fill="#FFFFFF" opacity=".28"/></pattern></defs>
<g fill="currentColor">
<rect x="0" y="40" width="120" height="80"/><rect x="128" y="18" width="92" height="102"/><rect x="228" y="52" width="140" height="68"/>
<rect x="376" y="10" width="86" height="110"/><rect x="470" y="34" width="150" height="86"/><rect x="628" y="22" width="96" height="98"/>
<rect x="732" y="56" width="126" height="64"/><rect x="866" y="14" width="90" height="106"/><rect x="964" y="44" width="140" height="76"/><rect x="1112" y="26" width="88" height="94"/>
</g>
<g fill="url(#win)">
<rect x="0" y="40" width="120" height="80"/><rect x="128" y="18" width="92" height="102"/><rect x="228" y="52" width="140" height="68"/>
<rect x="376" y="10" width="86" height="110"/><rect x="470" y="34" width="150" height="86"/><rect x="628" y="22" width="96" height="98"/>
<rect x="732" y="56" width="126" height="64"/><rect x="866" y="14" width="90" height="106"/><rect x="964" y="44" width="140" height="76"/><rect x="1112" y="26" width="88" height="94"/>
</g></svg>'''

CHAT = '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.4 8.4 0 0 1-12.3 7.5L3 21l2-5.4A8.4 8.4 0 1 1 21 11.5Z"/></svg>'

UPDATED = "24 November 2026"


def sale_check_form(title="Get your free Sale Check"):
    return '''<div class="check">
  <h3>''' + title + '''</h3>
  <p class="fine" style="margin:0 0 18px">Takes about a minute. I reply personally on WhatsApp.</p>
  <form class="sale-check" novalidate>
    <div class="row2">
      <div class="field"><label for="sc-name">Your name</label><input id="sc-name" name="name" autocomplete="given-name" required></div>
      <div class="field"><label for="sc-postal">Postal code</label><input id="sc-postal" name="postal" inputmode="numeric" maxlength="6" pattern="[0-9]{6}" placeholder="e.g. 821325" required></div>
    </div>
    <div class="row2">
      <div class="field"><label for="sc-type">Your home</label>
        <select id="sc-type" name="type"><option>3-room HDB</option><option selected>4-room HDB</option><option>5-room HDB</option><option>Executive HDB</option><option>Condo / EC</option><option>Not sure</option></select></div>
      <div class="field"><label for="sc-why">What's on your mind?</label>
        <select id="sc-why" name="why"><option>Thinking of upgrading</option><option>Inherited flat / faraid</option><option>Divorce or separation</option><option>Rightsizing</option><option>Buying a new launch</option><option>Just curious about my price</option></select></div>
    </div>
    <div class="field"><label for="sc-note">Anything I should know? <span style="font-weight:400;color:var(--muted)">(optional)</span></label><input id="sc-note" name="note" placeholder="e.g. MOP in March, want to stay near my parents"></div>
    <p class="err" role="alert"></p>
    <button class="btn primary" type="submit">''' + CHAT + '''Send on WhatsApp</button>
    <p class="fine">By sending, you agree that Andik may contact you on WhatsApp about your enquiry, in line with the PDPA. No spam, no cold calls.</p>
  </form>
  <div class="done" aria-live="polite">
    <h3>Almost done</h3>
    <p>Tap below to send your details on WhatsApp. I'll reply with recent sales in your block, usually the same day.</p>
    <a class="btn wa" href="#" target="_blank" rel="noopener">''' + CHAT + '''Open WhatsApp</a>
  </div>
</div>'''


def article_shell(crumb_label, h1, intro, toc, body, related):
    toc_html = "".join('<a href="#' + a + '">' + t + "</a>" for a, t in toc)
    rel_html = "".join('<a href="{{L:' + k + '}}">' + t + "</a>" for k, t in related)
    return '''<section class="article-head"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="{{L:home}}">Home</a> / <a href="{{L:guides}}">Guides</a> / ''' + crumb_label + '''</nav>
  <h1>''' + h1 + '''</h1>
  <p class="lede">''' + intro + '''</p>
  <div class="meta"><span>By Andik Imran, CEA R061801F</span><span>Last reviewed ''' + UPDATED + '''</span></div>
</div></section>
<section class="band" style="padding-top:44px"><div class="wrap layout">
  <article class="prose">''' + body + '''
  <h2 id="faq">Questions families ask me</h2>
  [[FAQ]]
  <p class="fine" style="margin-top:28px">General information only, not legal, tax or financial advice. Rules from HDB, CPF, IRAS, the Syariah Court and the Family Justice Courts change, and every family's case is different. I work alongside your lawyer on the legal side and check your case against the rules in force at the time.</p>
  </article>
  <aside class="aside">
    <div class="card">
      <div class="author"><div class="avatar">{{PIC:andik-avatar.webp|Andik Imran}}</div><div><b>Andik Imran</b><br><span class="fine">PropNex · since 2019 · Malay &amp; English</span></div></div>
      <p style="margin:14px 0 16px;font-size:15.5px">Every family is different. Tell me your situation and I'll tell you honestly what I'd do next.</p>
      <a class="btn wa" href="{{WA:Hi Andik, I read your guide and have a question about my situation.}}">''' + CHAT + '''WhatsApp me</a>
    </div>
    <div class="card toc"><b style="margin-bottom:6px">On this page</b>''' + toc_html + '''<a href="#faq">Questions families ask</a></div>
    <div class="card toc"><b style="margin-bottom:6px">Related guides</b>''' + rel_html + '''</div>
  </aside>
</div></section>
<section class="band dark"><div class="wrap split">
  <div><h2>Want me to look at your case?</h2><p class="lede">Send your postal code and a line about your situation. I'll come back with recent sales in your block and what I'd do first.</p></div>
  <div>''' + sale_check_form("Free Sale Check") + '''</div>
</div></section>'''


STORIES = [
    ("Azhar &amp; Fiszah", "Upgraded to a new condo", "Sold their HDB within 30 days and moved into a brand-new condo without touching their cash savings."),
    ("Faiz &amp; Miszah", "Upgraded to a resale condo", "Sold within 30 days and bought a resale condo that has since gone up in value."),
    ("Hafiz &amp; Mirah", "Upgraded, fully paid from the sale", "Sold within 30 days and found their next home, paid for fully from the sale proceeds."),
    ("Habib &amp; Nabilah", "First home, before the wedding", "Bought their first resale home while still engaged, with time to renovate before the big day."),
]

REVIEWS = [
    ("Shina", "Sold a 4-room flat in Punggol", "Andik was extremely helpful, open, transparent, and reliable through the whole process."),
    ("Diyana", "Sold a 4-room flat in Punggol", "Your attention to detail, responsiveness and dedication made our experience smooth and stress-free!!"),
    ("Nabil", "Sold a 4-room flat in Punggol", "Andik was effective in protecting my interests as his client… I felt safe with him handling my real estate transaction."),
]


GOOGLE = [
    ("Nurul", "Seller", "https://share.google/pl93kamPJp0F27N3v", "Andik was very helpful from the onset when he took over the selling of our unit from our previous agent, as our unit was still not sold after many many months. He took over the selling and had it sold within a couple of weeks! There was even one who cancelled on us but Andik managed to get us a new buyer within 48hrs!"),
    ("Haizam", "Sold and bought", "https://share.google/oJdhIg5iOjF6BKjo8", "What started off as just a consultation session (with no concrete plans to move) resulted in us making the huge decision to sell our first matrimonial home and buying our next forever home. Andik’s explanations and calculations were clear, which gave us the confidence to pivot from our initial plan."),
    ("Wan", "Sold and bought", "https://share.google/dYU9d5XWynQzsVTpA", "His soft-spoken and patient nature was reassuring, and he was consistently attentive and responsive. Andik took the time to truly understand our concerns, offering thoughtful guidance without ever being pushy."),
    ("Shahrul", "Seller", "https://share.google/9xRcNechBV5YFVLFo", "Andik offers sound advice, clear communication, and a personalized approach from day one of meeting him… especially when he was able to fetch a selling price that was way above our initial expectation."),
    ("Nurul Hidayah", "First-time seller", "https://share.google/A6LxOjALG6YxanbSs", "He is professional, responsive, and meticulous in his work. He guided us through every step of the process to ensure we understand as a first timer to sell our house."),
    ("Arpabe", "Sold for his brother and sister-in-law", "https://share.google/vrltjgWxFoCzela84", "Andik keep in touch by calling and Whatsapp follow up progress… My brother n sister in-law now really have peace of mind where they stay in a new house and stable finance for them to spend."),
    ("Nick", "Resale HDB buyer", "https://share.google/CeCSCTxOyvZ1PWAHh", "He was responsive, efficient, and ensured the process went smoothly from start to finish. We really appreciate his professionalism and prompt assistance!"),
    ("Chaso", "Client", "https://share.google/kKun7Iop6XmvCbZV7", "Andik provided expert guidance and handled everything with total care. If you want someone who is knowledgeable and gets the job done, look no further. 5 stars!"),
]


def google_cards(items):
    return "".join(
        '<figure class="card" style="margin:0"><div class="quote-mark">“</div><blockquote style="margin:0 0 14px">' + q + '</blockquote><figcaption><b>' + n + '</b> · <span class="fine">' + w + ' · ★★★★★</span><br><a class="fine" href="' + u + '">Read on Google</a></figcaption></figure>'
        for n, w, u, q in items
    )

SOLD = [
    ("sold-325b-sumang-walk.webp", "Blk 325B Sumang Walk", "Punggol · 4-room · 93 sqm"),
    ("sold-665c-punggol-drive.webp", "Blk 665C Punggol Drive", "Punggol · 5-room · 113 sqm"),
    ("sold-120b-edgedale-plains-4-room.webp", "Blk 120B Edgedale Plains", "Punggol · 4-room · 93 sqm"),
    ("sold-120b-edgedale-plains-3-room.webp", "Blk 120B Edgedale Plains", "Punggol · 3-room · 68 sqm"),
    ("sold-278c-compassvale-bow.webp", "Blk 278C Compassvale Bow", "Sengkang · 4-room · 92 sqm"),
    ("sold-126-rivervale-street.webp", "Blk 126 Rivervale Street", "Sengkang · 5-room · 120 sqm"),
    ("sold-246-tampines-st-21.webp", "Blk 246 Tampines St 21", "Tampines · HDB"),
    ("sold-723-tampines-st-72.webp", "Blk 723 Tampines St 72", "Tampines · HDB"),
    ("sold-879a-tampines-ave-8.webp", "Blk 879A Tampines Ave 8", "Tampines · HDB"),
    ("sold-343-tampines-st-33.webp", "Blk 343 Tampines St 33", "Tampines · HDB"),
    ("sold-treasure-at-tampines.webp", "Treasure at Tampines", "Tampines · Condo"),
    ("sold-101-pasir-ris-st-12.webp", "Blk 101 Pasir Ris St 12", "Pasir Ris · HDB"),
]


def story_cards(items):
    return "".join(
        '<div class="card"><div class="quote-mark">“</div><h3>' + n + '</h3><p class="fine" style="margin-top:-6px">' + w + "</p><p>" + t + "</p></div>"
        for n, w, t in items
    )


def review_cards(items):
    return "".join(
        '<figure class="card" style="margin:0"><div class="quote-mark">“</div><blockquote style="margin:0 0 14px;font-size:17.5px">' + q + '</blockquote><figcaption><b>' + n + '</b> · <span class="fine">' + w + " · ★★★★★ on Google</span></figcaption></figure>"
        for n, w, q in items
    )


def sold_strip():
    return '<div class="sold" tabindex="0" aria-label="Recently sold homes">' + "".join(
        '<figure><div class="pic">{{PIC:' + f + "|Living room of " + a + ", " + d + '}}</div><figcaption><span class="tag">Sold</span><b>' + a + "</b>" + d + "</figcaption></figure>"
        for f, a, d in SOLD
    ) + "</div>"


# ---------------------------------------------------------------- HOME
HOME_FAQ = [
    ("Do I have to commit to selling before we talk?", "No. Plenty of first chats end with “not yet”, and that's a good outcome. The Sale Check and our first sit-down are free, with no obligation to list."),
    ("Who do you work with?", "Pretty much everyone looking to buy, sell or rent a home in Singapore: first-timers, young families moving up, older couples rightsizing, landlords and investors. If I'm not the right person for something, I'll tell you and point you to someone who is."),
    ("Can we speak in Malay?", "Boleh. I'm comfortable in Malay and English, and so is Mirta. Many families switch between both in the same meeting, and that's perfectly fine. More on my <a href=\"{{L:malay}}\">Malay property agent</a> page."),
    ("Do you also help with new launch condos?", "Yes. If your next home is a new condo or EC, I plan the sale and the purchase together so the timing and cash flow work. See the <a href=\"{{L:newlaunch}}\">new launch page</a>."),
    ("What counts as a “complicated” case?", "Inherited flats and faraid, estates still waiting on paperwork, divorce, tight sale-and-buy timelines, and flats needing an extension of stay. These are the cases I enjoy most, because a calm plan makes the biggest difference."),
    ("Is Homes with AIMS a different agency?", "No. Homes with AIMS is my wife Mirta and me working as a team, both with PropNex. This site is my own page. <a href=\"https://www.homeswithaims.com\">homeswithaims.com</a> is our team's."),
]

HOME = '''<section class="hero"><div class="wrap hero-grid">
  <div class="hero-copy">
    <p class="kicker pnx-line"><span class="pnx">{{PIC:propnex-logo.png|PropNex Realty}}<b>PropNex</b></span>Associate Group Director</p>
    <h1>Hi, meet your <em>property consultant.</em></h1>
    <p class="lede">I'm Andik. Buying your first home, selling, upgrading, renting, or sorting out something a little more complicated? I'll walk you through it in plain English (or Malay, boleh!), with the numbers worked out first. No pressure, no jargon, just honest advice.</p>
    <div class="btns">
      <a class="btn primary" href="{{WA:Hi Andik! I found your website and would like to chat.}}">''' + CHAT + '''WhatsApp me</a>
      <a class="btn ghost" href="{{L:salecheck}}">Free Sale Check</a>
    </div>
    <p class="phone">Call or WhatsApp <a href="tel:+6587368736">+65 8736 8736</a></p>
    <ul class="proof">
      <li><b>Since 2019</b></li><li>Top rookie, top producer every year since</li><li><b>100+</b> families helped</li><li><b>65+</b> five-star Google reviews</li>
    </ul>
  </div>
  <div class="door-wrap">
    <div class="door">{{PIC:andik-imran.webp|Andik Imran, PropNex property consultant}}<p class="ph">Andik Imran</p></div>
    <div class="door-tag"><b>100+</b><span>happy families helped to buy, sell and rent</span></div>
  </div>
</div>''' + SKYLINE + '''</section>

<section class="band paper"><div class="wrap">
  <div class="section-head"><h2>So, what can I help you with?</h2><p class="lede">Whatever stage you're at, pick the one that fits and we'll take it from there. Not sure? Just WhatsApp me and tell me what's going on.</p></div>
  <div class="grid g3">
    <a class="card situation" href="{{L:g-first}}"><p class="who">Buying your first home</p><h3>Where do we even start?</h3><p>HFE letter, grants, BTO or resale, how much you can borrow. I'll make it simple.</p><span class="more">First-timer guide →</span></a>
    <a class="card situation" href="{{L:salecheck}}"><p class="who">Selling</p><h3>What's my home worth?</h3><p>Recent sales in your block and what you'd actually keep after selling. Free, on WhatsApp.</p><span class="more">Free Sale Check →</span></a>
    <a class="card situation" href="{{L:g-upgrade}}"><p class="who">Upgrading</p><h3>Bigger home, without the stress</h3><p>HDB to HDB, to a resale condo or a new launch, with the timeline and payments laid out.</p><span class="more">Upgrading guide →</span></a>
    <a class="card situation" href="{{L:newlaunch}}"><p class="who">New launches</p><h3>Shopping for a new condo?</h3><p>I'll help you compare honestly and plan the money, at no cost to you.</p><span class="more">New launch →</span></a>
    <a class="card situation" href="{{L:g-faraid}}"><p class="who">The complicated ones</p><h3>Inherited flat, faraid, divorce</h3><p>Calm, step-by-step help when life makes a property decision for you.</p><span class="more">How I help →</span></a>
    <a class="card situation" href="{{WA:Hi Andik, I'd like to ask about renting.}}"><p class="who">Renting</p><h3>Renting out or looking to rent?</h3><p>Finding good tenants, or the right place while you wait for your next home.</p><span class="more">WhatsApp me →</span></a>
  </div>
</div></section>

<section class="band dark"><div class="wrap">
  <p class="kicker">How I plan every upgrade</p>
  <div class="section-head"><h2>The SAFE Upgrading Plan</h2><p class="lede">A nicer home that keeps you up at night isn't an upgrade. Before you sell, we check four things.</p></div>
  <div class="safe">
    <div><span class="letter">S</span><h3>Sale pays for it</h3><p>Your sale proceeds cover the downpayment and costs. No digging into the family's savings to make it work.</p></div>
    <div><span class="letter">A</span><h3>Aside first</h3><p>An emergency fund comes out of the sale before we decide how much home you buy.</p></div>
    <div><span class="letter">F</span><h3>Four years covered</h3><p>Four years of the new mortgage covered by CPF and the cash buffer from your sale, not your salary.</p></div>
    <div><span class="letter">E</span><h3>Even if rates rise</h3><p>We test your repayments at higher interest rates, so a rate hike is an inconvenience, not a crisis.</p></div>
  </div>
  <div class="btns"><a class="btn ghost" href="{{L:safe}}">How the SAFE plan works</a></div>
  <p class="fine" style="margin-top:18px">A planning framework, not a guarantee. Your numbers depend on your sale price, loan and CPF.</p>
</div></section>

<section class="band paper"><div class="wrap">
  <div class="section-head"><h2>Plan your move before you make it</h2><p class="lede">Every timeline shows each step and what you pay at it. The calculator applies the real loan rules to your income.</p></div>
  <div class="grid g4">
    <a class="card situation" href="{{L:calculator}}"><p class="who">Tool</p><h3>Loan calculator</h3><p>Your maximum loan, affordable price, downpayment and monthly instalment.</p><span class="more">Calculate →</span></a>
    <a class="card situation" href="{{L:g-hdb2hdb}}"><p class="who">Timeline</p><h3>HDB to HDB</h3><p>Sell and buy in parallel, move once.</p><span class="more">See the steps →</span></a>
    <a class="card situation" href="{{L:g-hdb2pvt}}"><p class="who">Timeline</p><h3>HDB to resale condo</h3><p>The order of moves that keeps ABSD off your bill.</p><span class="more">See the steps →</span></a>
    <a class="card situation" href="{{L:g-hdb2nl}}"><p class="who">Timeline</p><h3>HDB to new launch</h3><p>Progressive payments, TOP and the 6-month sale window.</p><span class="more">See the steps →</span></a>
  </div>
  <p style="margin-top:18px">Buying your first home? Start with the <a href="{{L:g-first}}">first-time buyer guide</a>.</p>
</div></section>

<section class="band"><div class="wrap">
  <div class="section-head"><h2>Families I've walked with</h2><p class="lede">First names only, shared with their permission.</p></div>
  <div class="grid g4">''' + story_cards(STORIES) + '''</div>
  <div class="clients">{{PIC:client-1.webp|Andik with happy homeowners}}{{PIC:client-2.webp|Andik with a client at HDB}}{{PIC:client-3.webp|Andik and Mirta with clients at an HDB key collection}}{{PIC:client-4.webp|Andik with a family after their purchase}}</div>
  <div class="grid g3" style="margin-top:18px">''' + google_cards(GOOGLE[:3]) + '''</div>
  <div class="btns"><a class="btn ghost" href="{{L:reviews}}">More stories and reviews</a><a class="btn ghost" href="{{GR}}">All reviews on Google</a></div>
</div></section>

<section class="band paper"><div class="wrap">
  <div class="section-head"><h2>Recently sold</h2><p class="lede">A few of the homes we've sold in Punggol, Sengkang, Tampines and Pasir Ris. Swipe to see more.</p></div>
  ''' + sold_strip() + '''
</div></section>

<section class="band"><div class="wrap split">
  <div class="portrait">{{PIC:andik-family.webp|Andik Imran with his wife Mirta and their children}}</div>
  <div>
    <p class="kicker">A bit about me</p>
    <h2>A dad of four who's made the same move you're thinking about.</h2>
    <p>Mirta and I started out in a 3-room BTO. Upgrading to a condo with young kids taught me what the brochures leave out: how much buffer you really need, what matters near home when you have children, and why the numbers have to work before the showflat does.</p>
    <p>I'm an Associate Group Director at PropNex, a PropNex Ambassador and a multiple award recipient at the Singapore Real Estate Agents Excellence Awards. I came into property with a business degree and a finance background, which is why I'm a little obsessed with the numbers.</p>
    <p>Mirta works alongside me. Together we're <a href="https://www.homeswithaims.com">Homes with AIMS</a>: a husband's view and a wife's view on the same decision you're making at home.</p>
    <div class="btns"><a class="btn ghost" href="{{L:about}}">More about me</a></div>
  </div>
</div></section>

<section class="band paper"><div class="wrap">
  <div class="section-head"><h2>How working with me goes</h2><p class="lede">No pressure, no jargon. You'll always know what happens next.</p></div>
  <ol class="steps">
    <li><p class="when">Today, about 2 minutes</p><h3>Free Sale Check</h3><p>Send your postal code. I'll WhatsApp you recent sales in your block and a rough idea of the cash you'd keep.</p></li>
    <li><p class="when">One sit-down, at home or online</p><h3>Your numbers, laid out</h3><p>Sale price, CPF refund, cash proceeds, loan limits, what you can safely buy and a realistic timeline. Husband and wife both in the room.</p></li>
    <li><p class="when">When you're ready</p><h3>Sell, buy, move</h3><p>Pricing, marketing, viewings, negotiation, HDB paperwork and an extension of stay if you need one.</p></li>
  </ol>
</div></section>

<section class="band"><div class="wrap">
  <div class="section-head"><h2>Estates I know well</h2><p class="lede">I work all over Singapore, and these are the towns I'm asked about most.</p></div>
  <div class="btns" style="margin-top:0">
    <a class="btn ghost" href="{{L:e-yishun}}">Yishun</a><a class="btn ghost" href="{{L:e-punggol}}">Punggol</a><a class="btn ghost" href="{{L:e-sengkang}}">Sengkang</a><a class="btn ghost" href="{{L:e-tampines}}">Tampines</a><a class="btn ghost" href="{{L:e-pasirris}}">Pasir Ris</a>
  </div>
</div></section>

<section class="band"><div class="wrap split rev">
  <div><h2>Questions I get every week</h2>[[FAQ]]</div>
  <div class="card" style="align-self:start">
    <h3>Rather just talk?</h3>
    <p>WhatsApp is fastest. I reply personally, usually within the day.</p>
    <a class="btn wa" href="{{WA:Hi Andik, I have a question about my flat.}}">''' + CHAT + '''WhatsApp +65 8736 8736</a>
  </div>
</div></section>

<section class="band dark" id="check"><div class="wrap split">
  <div>
    <h2>Curious what your flat could sell for?</h2>
    <p class="lede">Send your postal code and flat type. I'll reply on WhatsApp with recent sales in your block and a rough estimate of the cash you'd keep after selling.</p>
    <ul class="ticks"><li>Replies from me, not a call centre</li><li>Recent transacted prices in your block</li><li>Rough cash proceeds after loan and CPF refund</li><li>No obligation to list, ever</li></ul>
  </div>
  <div>''' + sale_check_form() + '''</div>
</div></section>'''

# ---------------------------------------------------------------- ABOUT
ABOUT = '''<section class="article-head"><div class="wrap split">
  <div>
    <nav class="crumbs" aria-label="Breadcrumb"><a href="{{L:home}}">Home</a> / About</nav>
    <h1>Hi, I'm Andik.</h1>
    <p class="lede">Husband to Mirta, dad of four, and a property consultant with PropNex since 2019. I help people buy, sell and rent homes across Singapore, and I like to get the numbers sorted before anything else.</p>
    <div class="btns"><a class="btn primary" href="{{WA:Hi Andik, I read your About page and would like to chat.}}">''' + CHAT + '''Say hi on WhatsApp</a></div>
  </div>
  <div class="portrait">{{PIC:andik-imran.webp|Andik Imran, PropNex Associate Group Director}}</div>
</div></section>

<section class="band paper"><div class="wrap split rev">
  <div class="prose">
    <h2>Why I do this</h2>
    <p>Our first home was a 3-room BTO. When the family grew, Mirta and I upgraded to a condo, and I learned first-hand how different the decision feels from the inside. The question was never “can the bank lend us this?” It was “will we still sleep well in three years if something goes wrong?”</p>
    <p>That question became the <a href="{{L:safe}}">SAFE Upgrading Plan</a>. Every family I work with sees their sale proceeds, CPF refund, loan limits and buffer on paper before we talk about listing. Some decide to upgrade. Some decide to wait. Both are good outcomes if they're the right ones.</p>
    <h2>Who I work with</h2>
    <p>All sorts of people, all over Singapore: first-time buyers, young families moving up, older couples rightsizing, landlords and investors. Many of my clients are Malay families, and I'm always happy to chat in Malay. I also help families dealing with an inherited flat, faraid or a divorce, where a calm, organised consultant makes a real difference.</p>
    <h2>What I won't do</h2>
    <ul>
      <li>Quote you an exciting price just to win your listing.</li>
      <li>Push you to sell when the numbers say wait.</li>
      <li>Leave you guessing. You'll know what's happening and what comes next.</li>
    </ul>
  </div>
  <div>
    <div class="card">
      <h3>The short version</h3>
      <ul class="ticks">
        <li>Agent since 2019, top rookie in my first year</li>
        <li>Top producer every year since</li>
        <li>Associate Group Director, PropNex</li>
        <li>PropNex Ambassador</li>
        <li>Multiple award recipient, Singapore Real Estate Agents Excellence Awards</li>
        <li>100+ families helped to sell, buy and rent</li>
        <li>65+ five-star Google reviews</li>
        <li>Business degree, finance background</li>
        <li>English and Malay</li>
      </ul>
      <p class="fine">CEA Reg. No. R061801F · PropNex Realty Pte Ltd, CEA Licence No. L3008022J</p>
    </div>
  </div>
</div></section>

<section class="band"><div class="wrap split">
  <div class="portrait">{{PIC:andik-mirta-park.webp|Andik Imran and Mirta Syazanna, Homes with AIMS}}</div>
  <div>
    <p class="kicker">Working together</p>
    <h2>Mirta, my partner at home and at work</h2>
    <p>Mirta Syazanna is an Associate Director at PropNex (CEA Reg. No. R070524E) with 15 years in marketing. She also lectures in marketing. She's direct, practical and very good at spotting what a buyer will notice before they do.</p>
    <p>Together we're <a href="https://www.homeswithaims.com">Homes with AIMS</a>, short for Andik Imran and Mirta Syazanna. Most homes are bought by couples, so you get both perspectives: one of us often picks up the worry the other partner hasn't said out loud yet.</p>
    <div class="btns"><a class="btn ghost" href="https://www.homeswithaims.com">Visit Homes with AIMS</a></div>
  </div>
</div></section>

<section class="band dark"><div class="wrap split">
  <div><h2>Start with your numbers</h2><p class="lede">Send your postal code. I'll show you what your flat could fetch and what you'd keep.</p></div>
  <div>''' + sale_check_form() + '''</div>
</div></section>'''

# ---------------------------------------------------------------- REVIEWS
VIDEOS = [
    ("N0Gbht4hh9E", "Fikry's story: a first-time HDB buyer"),
    ("avTZy2KYlcc", "How to plan for a comfortable life for your family"),
    ("4WSISVci6-c", "Helping families decide clearly, not emotionally"),
    ("PPS65KrOp84", "Rightsizing without CPF and HDB timeline trouble (in Malay)"),
]
REVIEWS_PAGE = '''<section class="article-head"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="{{L:home}}">Home</a> / Reviews</nav>
  <h1>Stories from families we've helped</h1>
  <p class="lede">65+ five-star reviews on Google since 2019. Here are a few, in our clients' own words, plus the outcomes behind them.</p>
  <div class="btns"><a class="btn primary" href="{{GR}}">Read all reviews on Google</a></div>
</div></section>
<section class="band"><div class="wrap">
  <h2>Some of the families we've helped</h2>
  <div class="collage">{{PIC:clients-collage.webp|Collage of Andik Imran with clients at key collections and handovers}}</div>
  <div class="clients">{{PIC:client-1.webp|Andik with happy homeowners}}{{PIC:client-2.webp|Andik with a client at HDB}}{{PIC:client-3.webp|Andik and Mirta with clients at an HDB key collection}}{{PIC:client-4.webp|Andik with a family after their purchase}}</div>
</div></section>
<section class="band paper"><div class="wrap">
  <h2>In their words, on Google</h2>
  <div class="grid g2" style="margin-top:24px">''' + google_cards(GOOGLE) + '''</div>
  <h2 style="margin-top:48px">More from our clients</h2>
  <div class="grid g2" style="margin-top:24px">''' + review_cards(REVIEWS + [("Marilyn", "Bought a resale condo in Sengkang with Mirta", "Mirta's patience, expertise and initiative has made our journey as first-time homeowners an incredibly smooth one!")]) + '''</div>
</div></section>
<section class="band"><div class="wrap">
  <h2>What happened next</h2>
  <p class="lede">Four upgrades, four different plans.</p>
  <div class="grid g2" style="margin-top:24px">''' + story_cards(STORIES) + '''</div>
</div></section>
<section class="band paper"><div class="wrap">
  <h2>Watch</h2>
  <div class="grid g4" style="margin-top:24px">''' + "".join(
    '<a class="card" href="https://www.youtube.com/watch?v=' + v + '"><h3 style="font-size:22px">' + t + '</h3><span class="more">Watch on YouTube →</span></a>' for v, t in VIDEOS
) + '''</div>
</div></section>
<section class="band paper"><div class="wrap">
  <h2>Recently sold</h2>
  ''' + sold_strip() + '''
</div></section>
<section class="band dark"><div class="wrap split">
  <div><h2>Your story could be next</h2><p class="lede">Start with a free Sale Check. No obligation, just your numbers.</p></div>
  <div>''' + sale_check_form() + '''</div>
</div></section>'''

# ---------------------------------------------------------------- SAFE
SAFE_FAQ = [
    ("Why four years of mortgage covered?", "Four years is long enough to ride out most rough patches: a job change, a new baby, one partner taking a break, a rate cycle. It means your new home isn't relying on everything going right from day one."),
    ("Isn't it better to borrow the maximum the bank allows?", "The bank's limit tells you what you're allowed to borrow, not what's comfortable. Plenty of families qualify for more than they should take. SAFE is how we find the comfortable number."),
    ("What if my numbers don't pass SAFE?", "Then I'll tell you, and we look at the options: a different budget, a different timeline, waiting a year, or staying put. I'd rather lose a listing than put a family under pressure."),
    ("Does SAFE apply to new launch condos too?", "Yes. With a new launch, we also map the progressive payment schedule against your sale and CPF timeline so there's no gap."),
]
SAFE = '''<section class="article-head"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="{{L:home}}">Home</a> / SAFE Upgrading Plan</nav>
  <h1>The SAFE Upgrading Plan</h1>
  <p class="lede">How I help families upgrade without stretching. Four checks we run before you sell, so your next home is one you can enjoy, not one you worry about.</p>
</div></section>
<section class="band dark"><div class="wrap">
  <div class="safe">
    <div><span class="letter">S</span><h3>Sale pays for it</h3><p>The downpayment, stamp duty, legal fees and moving costs come from your sale proceeds and CPF. If the plan only works by draining your savings, it's not the plan.</p></div>
    <div><span class="letter">A</span><h3>Aside first</h3><p>Before we set a budget, an emergency fund is ring-fenced from the sale. That money is for life, not for the house.</p></div>
    <div><span class="letter">F</span><h3>Four years covered</h3><p>Four years of the new monthly instalment, covered by your CPF and the cash buffer from your sale rather than your salary.</p></div>
    <div><span class="letter">E</span><h3>Even if rates rise</h3><p>We test your repayments at higher interest rates than today's. If it still holds, you're safe. If not, we adjust before you commit.</p></div>
  </div>
</div></section>
<section class="band paper"><div class="wrap split rev">
  <div class="prose">
    <h2>What we look at in your sit-down</h2>
    <ul>
      <li><b>Your sale:</b> a realistic price range from recent transactions in your block and estate, not the highest number on the portal.</li>
      <li><b>What comes back to you:</b> outstanding loan, the CPF refund (principal plus accrued interest) and the cash you'll actually receive.</li>
      <li><b>What you can borrow:</b> loan limits based on income, age and existing debts, and what that means for your budget.</li>
      <li><b>Your buffer:</b> the emergency fund and the four-year cover, set aside before the budget.</li>
      <li><b>Your timeline:</b> sell first, buy first, or both together, and whether you'll need an extension of stay.</li>
      <li><b>Your life:</b> schools, parents nearby, commute, the next five years.</li>
    </ul>
    <p>You leave with a one-page plan: the budget that passes SAFE, the timeline, and what has to be true for it to work.</p>
    <h2 id="faq">Common questions</h2>
    [[FAQ]]
    <p class="fine" style="margin-top:24px">SAFE is a planning framework, not financial advice or a guarantee. For loans, I'll connect you with a mortgage banker who can confirm your figures.</p>
  </div>
  <div class="card" style="align-self:start">
    <h3>Will your upgrade pass SAFE?</h3>
    <p>Send me your postal code and flat type. I'll do the first rough check for free.</p>
    <a class="btn primary" href="{{L:salecheck}}">Get my free Sale Check</a>
  </div>
</div></section>'''

# ---------------------------------------------------------------- NEW LAUNCH
NL_FAQ = [
    ("Do I pay you a fee to buy a new launch?", "For new launch projects, the developer pays the agent's fee. You get my help comparing projects, planning finances and handling the booking at no cost to you."),
    ("Can I just walk into the showflat on my own?", "You can, but you'll only hear about one project from the people selling it. I'll help you compare a few side by side and check the numbers against your HDB sale first."),
    ("Should I sell my HDB first?", "Usually, or at least plan both together. If you buy private property before selling your HDB, ABSD may apply up front. Married couples can apply for a refund if the HDB is sold within the allowed period, but you need the cash to pay it first. We map this out before you book."),
    ("EC or condo?", "It depends on your household income, eligibility and how long you plan to stay. ECs come with their own rules and minimum occupation period, so we look at both against your SAFE numbers."),
]
NEW_LAUNCH = '''<section class="article-head"><div class="wrap split">
  <div>
    <nav class="crumbs" aria-label="Breadcrumb"><a href="{{L:home}}">Home</a> / New launch</nav>
    <h1>From HDB to a new launch, in the right order.</h1>
    <p class="lede">A new condo or EC is exciting. The showflat is designed to be. My job is the part after the excitement: making sure your HDB sale, CPF, loan and the developer's payment schedule all line up.</p>
    <div class="btns"><a class="btn primary" href="{{WA:Hi Andik, I'm an HDB owner looking at new launch condos. Can we plan it out?}}">''' + CHAT + '''Plan my upgrade</a><a class="btn ghost" href="{{L:safe}}">The SAFE plan</a></div>
  </div>
  <div class="card">
    <h3>What I'll do for you</h3>
    <ul class="ticks">
      <li>Check your upgrade against the SAFE plan first</li>
      <li>Shortlist projects that fit your budget, schools and family</li>
      <li>Compare them side by side, honestly</li>
      <li>Plan sell-first or buy-first so ABSD doesn't catch you out</li>
      <li>Line up progressive payments with your HDB sale and CPF</li>
      <li>Sell your HDB, with an extension of stay if you need one</li>
    </ul>
  </div>
</div></section>
<section class="band paper"><div class="wrap">
  <h2>The three questions that matter more than the floor plan</h2>
  <div class="grid g3" style="margin-top:24px">
    <div class="card"><h3>Can we afford it in year three, not just today?</h3><p>Progressive payments start small and rise as the project is built. We plan for the payments you'll face at TOP, not just the first cheque.</p></div>
    <div class="card"><h3>What's the order of moves?</h3><p>Sell first, buy first, or both in parallel. Each has a different cash and ABSD picture. We choose deliberately.</p></div>
    <div class="card"><h3>Where will we live in between?</h3><p>If your new home isn't ready when your HDB sale completes, you'll need a bridge: extension of stay, family, or renting. We plan it before you sign.</p></div>
  </div>
</div></section>
<section class="band"><div class="wrap prose" style="max-width:860px">
  <h2 id="faq">New launch questions</h2>
  [[FAQ]]
  <p class="fine" style="margin-top:24px">General information only. ABSD, loan and EC eligibility rules change; we check yours against current IRAS, HDB and MAS rules.</p>
</div></section>
<section class="band dark"><div class="wrap split">
  <div><h2>Start with what your HDB is worth</h2><p class="lede">Your sale funds your upgrade. Let's see the numbers first.</p></div>
  <div>''' + sale_check_form() + '''</div>
</div></section>'''

# ---------------------------------------------------------------- GUIDES INDEX
GUIDES = '''<section class="article-head"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="{{L:home}}">Home</a> / Guides</nav>
  <h1>Guides for HDB sellers and upgraders</h1>
  <p class="lede">Plain-English answers to the questions families ask me most, especially the complicated ones. Written by me, reviewed regularly.</p>
</div></section>
<section class="band paper"><div class="wrap">
  <div class="grid g2">
    <a class="card situation" href="{{L:g-upgrade}}"><p class="who">Upgrading</p><h3>Upgrading from your HDB after MOP: sell first or buy first?</h3><p>What your sale really gives you, how much you can borrow, and the order of moves that keeps you safe.</p><span class="more">Read the guide →</span></a>
    <a class="card situation" href="{{L:g-faraid}}"><p class="who">Inheritance</p><h3>Selling an inherited HDB flat: faraid, wills and what to do first</h3><p>Joint tenancy vs tenancy-in-common, the Inheritance Certificate, eligibility, and keeping the family together.</p><span class="more">Read the guide →</span></a>
    <a class="card situation" href="{{L:g-divorce}}"><p class="who">Divorce</p><h3>Selling your HDB flat during a divorce</h3><p>Sell or keep, MOP, the court order, CPF refunds, and how to keep the sale calm.</p><span class="more">Read the guide →</span></a>
    <a class="card situation" href="{{L:g-rightsize}}"><p class="who">Rightsizing</p><h3>Rightsizing your HDB when the kids have moved out</h3><p>Smaller flat, 2-room Flexi, Community Care Apartments or staying put, and the schemes that can help.</p><span class="more">Read the guide →</span></a>
    <a class="card situation" href="{{L:g-first}}"><p class="who">First home</p><h3>First-time home buyer guide: from HFE letter to keys</h3><p>BTO or resale, up to $230,000 in grants, the steps in order and what you pay at each one.</p><span class="more">Read the guide →</span></a>
    <a class="card situation" href="{{L:g-ssd}}"><p class="who">Stamp duty</p><h3>Seller's Stamp Duty (SSD): rates and the 4-year rule</h3><p>16%, 12%, 8%, 4% for homes bought from 4 July 2025, with a quick SSD check.</p><span class="more">Read the guide →</span></a>
  </div>
[[ARTICLES]]
  <h2 style="margin-top:56px">Upgrade timelines, with every payment</h2>
  <div class="grid g3" style="margin-top:20px">
    <a class="card situation" href="{{L:g-hdb2hdb}}"><p class="who">3–5 months</p><h3>HDB to HDB</h3><p>Sell and buy in parallel so your sale funds the next flat and you move once.</p><span class="more">See the timeline →</span></a>
    <a class="card situation" href="{{L:g-hdb2pvt}}"><p class="who">4–6 months</p><h3>HDB to private resale</h3><p>Sell first or buy first, the 1% + 4% condo payments, and the timing that avoids ABSD.</p><span class="more">See the timeline →</span></a>
    <a class="card situation" href="{{L:g-hdb2nl}}"><p class="who">3–4+ years</p><h3>HDB to new launch</h3><p>Book, stay in your flat while it's built, then sell within 6 months of TOP.</p><span class="more">See the timeline →</span></a>
  </div>
  <div class="card" style="margin-top:18px;flex-direction:row;flex-wrap:wrap;gap:16px;align-items:center;justify-content:space-between"><div><h3 style="margin:0">How much can you borrow?</h3><p style="margin:4px 0 0">TDSR, MSR, LTV and the stress test, worked out from your income.</p></div><a class="btn primary" href="{{L:calculator}}">Open the loan calculator</a></div>
</div></section>
<section class="band dark"><div class="wrap split">
  <div><h2>Can't find your situation?</h2><p class="lede">Tell me what's going on. If I haven't written about it yet, I've probably still seen it.</p></div>
  <div>''' + sale_check_form("Ask Andik") + '''</div>
</div></section>'''

# ---------------------------------------------------------------- GUIDE: FARAID
FARAID_FAQ = [
    ("Can we sell the flat before the Inheritance Certificate or grant is out?", "The person with legal authority (the administrator or executor) needs to be in place to sign the sale. While you wait, we can prepare everything else: valuation, family agreement on price, and the timeline for whoever is living there."),
    ("Do all the beneficiaries need to agree to sell?", "The administrator or executor signs, but in my experience the sale goes far more smoothly when every beneficiary agrees on the price range and timeline first. Disagreements are what drag these sales out."),
    ("My sibling is still living in the flat. What now?", "This is common and needs care. Agree early, as a family, on when they'll move and where to. If it can't be settled amicably, speak to a lawyer, since these disputes can end up in court."),
    ("How long does it take?", "Mostly it depends on how long the Inheritance Certificate or grant takes and how quickly the family agrees. Once that's in place, the sale itself runs like any other HDB resale."),
    ("Who do I talk to first: a lawyer or an agent?", "For the will, grant or Inheritance Certificate, a lawyer or the Syariah Court. For what the flat is worth and what selling involves, me. I'm happy to work alongside your lawyer."),
]
FARAID_BODY = '''
  <div class="answer"><b>Short answer</b>First, find out how the flat was held (joint tenancy or tenancy-in-common) and whether there's a will. For a Muslim owner, you'll usually need an Inheritance Certificate from the Syariah Court. For non-Muslims, it's a Grant of Probate (with a will) or Letters of Administration (without). Only then can the flat be transferred or sold, and HDB will check whether the people inheriting are eligible to own it.</div>
  <p>Losing a parent is hard enough. Then comes the flat: who owns it now, who's living in it, and what the family should do. I've sat with many families at this point. The paperwork is rarely the hardest part. Getting everyone on the same page is.</p>
  <h2 id="held">Step one: how was the flat held?</h2>
  <p>Check the ownership type. It changes everything.</p>
  <ul>
    <li><b>Joint tenancy</b> (common for married couples): when one owner passes away, their share goes to the surviving owner. This applies to Muslim joint tenants too, so faraid doesn't apply to the flat in this case.</li>
    <li><b>Tenancy-in-common, or a sole owner:</b> the deceased's share becomes part of their estate and is distributed according to their will or, without one, the law of inheritance.</li>
  </ul>
  <p>Not sure which applies? HDB can confirm it, and so can your lawyer.</p>
  <h2 id="faraid">If the owner was Muslim: faraid</h2>
  <p>A Muslim estate is distributed under faraid. If there's no will, the whole share follows faraid. If there is a will, the owner can only give away up to one-third through it, and the remaining two-thirds still follows faraid.</p>
  <p>The family applies to the Syariah Court for an <b>Inheritance Certificate</b>, which sets out each beneficiary's share. The Syariah Court's website also has an online trial calculator that gives you a sense of the shares before you apply.</p>
  <h2 id="non-muslim">If the owner was not Muslim</h2>
  <p>With a will, the executor applies for a <b>Grant of Probate</b>. Without a will, the Intestate Succession Act decides who inherits, and a family member applies for <b>Letters of Administration</b> to manage the estate.</p>
  <h2 id="keep">Can the family keep the flat?</h2>
  <p>Sometimes. After the beneficiaries are identified, HDB checks whether they're eligible to own the flat. A common snag is a beneficiary who already owns another flat. If no one eligible wants to keep it, the flat is usually sold and the proceeds shared out.</p>
  <p>If there's still a bank loan on the flat, the bank will also check whether the person taking over can afford it under its lending rules.</p>
  <h2 id="sell">Selling an inherited flat: what actually happens</h2>
  <ol>
    <li>Get the death certificate and gather the flat documents.</li>
    <li>Apply for the Inheritance Certificate, Grant of Probate or Letters of Administration.</li>
    <li>Sit down as a family: agree the price range, timeline, and plans for anyone living there.</li>
    <li>Get a realistic valuation from recent sales in the block and estate.</li>
    <li>Prepare the flat, list it, hold viewings, negotiate.</li>
    <li>The executor or administrator signs the Option to Purchase and the HDB resale application.</li>
    <li>On completion, the proceeds are distributed according to the Inheritance Certificate, will or grant.</li>
  </ol>
  <h2 id="family">The part nobody warns you about</h2>
  <p>Most delays aren't legal. They're emotional. One sibling wants to keep Mak's flat, another needs the money now, someone has been living there for years. When it goes wrong, families end up in court.</p>
  <div class="note"><b>What I do differently:</b> I act as the one neutral person in the middle. Every sibling sees the same price evidence, the same offers and the same updates, in writing, so no one feels left out or worries that someone else knows more.</div>
'''

# ---------------------------------------------------------------- GUIDE: DIVORCE
DIVORCE_FAQ = [
    ("Do we both need to sign to sell?", "Yes, both owners normally sign the sale documents. If one party refuses after the court has ordered the sale, the court order can allow someone else, such as a court officer, to sign on their behalf. Your lawyer will advise."),
    ("Can I keep the flat after the divorce?", "Possibly. The court decides who gets what, but HDB separately decides whether you're eligible to keep the flat, for example based on your citizenship, the children and the scheme you'd keep it under. Check with HDB before you agree on terms."),
    ("We haven't reached MOP. Are we stuck?", "Not necessarily. If MOP isn't met by the time the divorce is final, you'll generally need HDB's approval to sell on the open market. Talk to HDB and your lawyer early, as this affects your options."),
    ("How do we agree on the selling price when we don't agree on anything?", "Agree on the method, not the number. For example: list within a range based on recent sales, and accept any offer above an agreed floor. I share every offer with both of you in writing."),
    ("Will you take sides?", "No. I'm there to sell the flat well and keep both of you informed. If communication needs to go through your lawyers, I'll work that way."),
]
DIVORCE_BODY = '''
  <div class="answer"><b>Short answer</b>Whether the flat is sold or kept, and how the money is split, is set out in the ancillary matters order, either agreed between you or decided by the court. To sell on the open market, the flat generally needs to have met its MOP by the date the divorce is final; otherwise you'll need HDB's approval. Keeping the flat depends on meeting HDB's eligibility rules, separately from what the court decides.</div>
  <p>If you're reading this, things are probably heavy right now. Let's keep the flat part simple. Here's how it usually works, and how to sell without it becoming another battle.</p>
  <h2 id="decide">Sell or keep: where it's decided</h2>
  <p>The flat is usually part of the matrimonial assets. Unless you reach a written agreement, the court decides at the <b>ancillary matters</b> stage whether the flat is sold or kept, who keeps it, and how the proceeds are divided. It looks at things like each person's contributions, the children's needs and the length of the marriage.</p>
  <h2 id="keep">If one of you wants to keep it</h2>
  <p>Even if the court agrees, <b>HDB has its own eligibility rules</b> for keeping the flat. These look at citizenship, the children's care and control, and the scheme you'd keep it under. If neither of you is eligible, the flat will usually have to be sold.</p>
  <p>Special case: if the marriage is annulled, or an engaged couple breaks up before marrying, neither person can usually keep the flat.</p>
  <h2 id="mop">MOP: the date that matters</h2>
  <p>To sell on the open market, the flat should have met its <b>Minimum Occupation Period</b> by the date the divorce is final. If it hasn't, you'll need to ask HDB for approval, and your options may be narrower. Get this checked early.</p>
  <h2 id="money">Where the money goes</h2>
  <p>When the flat is sold, the outstanding loan is paid off first and the CPF used for the flat is refunded to each person's CPF account, with accrued interest. The remaining cash is split according to the court order.</p>
  <p>HDB will ask for the divorce documents when you sell: the Interim or Final Judgment and the relevant Order of Court, or the Syariah Court decree or certificate for Muslim divorces.</p>
  <h2 id="calm">How to keep the sale calm</h2>
  <ul>
    <li><b>One agent, two clients.</b> I keep you both informed equally, in writing.</li>
    <li><b>Agree the rules, not just the price.</b> A listing range, a floor price, and how quickly you'll respond to offers.</li>
    <li><b>Plan viewings around real life.</b> Especially if one of you has moved out, or the kids are at home.</li>
    <li><b>Watch the court's deadlines.</b> Orders often set a timeline to sell. We plan backwards from it.</li>
  </ul>
  <div class="note"><b>A gentle note:</b> I'm not a lawyer, and you'll need one for the divorce itself. I take care of the property side and work with your lawyers so you don't have to relay messages between everyone.</div>
'''

# ---------------------------------------------------------------- GUIDE: UPGRADE
UPGRADE_FAQ = [
    ("When can I sell my BTO?", "After the Minimum Occupation Period. That's 5 years for most flats. Plus and Prime flats have a 10-year MOP. You can check your exact MOP date on My HDBPage."),
    ("Why does my CPF refund matter so much?", "When you sell, the CPF you used for the flat, plus the interest it would have earned, goes back to your CPF account first. That reduces the cash you receive, but you can use the refunded CPF for your next home. Many families forget the accrued interest and overestimate their cash."),
    ("Can I stay in my flat after it's sold?", "Yes, if your buyer agrees, you can arrange a temporary extension of stay after completion. It's a common way to bridge the gap while your next home is being finished or handed over."),
    ("Should I buy near my parents?", "If family support matters to you, it's worth it, and there's a grant for buying a resale HDB flat near or with your parents. I'll check whether you qualify."),
    ("Is now a good time to upgrade?", "The better question is whether your numbers pass SAFE today. If they do, timing the market matters less. If they don't, waiting may be the smart move."),
]
UPGRADE_BODY = '''
  <div class="answer"><b>Short answer</b>Most HDB upgraders sell first, or sell and buy in parallel, so the sale proceeds fund the next home and you avoid paying ABSD up front on a private property. Buying first can work, but only if the numbers still hold when your sale takes longer than you hoped.</div>
  <p>You've hit MOP, the kids are bigger, and every weekend you're walking through showflats. Before you fall in love with a floor plan, here's how I walk families through the decision.</p>
  <h2 id="mop">Are you past MOP?</h2>
  <p>You can sell on the open market once you've met the <b>Minimum Occupation Period</b>: 5 years for most flats, and 10 years for Plus and Prime flats. Your exact date is on My HDBPage.</p>
  <h2 id="proceeds">What your sale actually gives you</h2>
  <p>A simple way to see it:</p>
  <p><b>Sale price − outstanding loan − CPF refund (with accrued interest) = cash in hand</b></p>
  <p>The CPF refund isn't lost. It goes back to your CPF Ordinary Account and can be used for your next home. But it isn't cash, and many families overestimate what they'll have in the bank.</p>
  <h2 id="loan">How much can you borrow?</h2>
  <p>Bank loans are limited by your income and existing debts, your age and the loan tenure. For HDB flats and ECs there's an extra cap on how much of your income can go to the mortgage. The bank's maximum is a ceiling, not a target. That's what the <a href="{{L:safe}}">SAFE plan</a> is for.</p>
  <h2 id="order">Sell first or buy first?</h2>
  <table class="stack" style="width:100%;border-collapse:collapse;margin:1em 0">
    <thead><tr style="text-align:left;border-bottom:2px solid var(--line)"><th style="padding:8px">Approach</th><th style="padding:8px">Good for</th><th style="padding:8px">Watch out for</th></tr></thead>
    <tbody>
      <tr style="border-bottom:1px solid var(--line)"><td style="padding:8px"><b>Sell first</b></td><td style="padding:8px">Knowing your exact budget; no ABSD on a private purchase</td><td style="padding:8px">Where you'll live in between</td></tr>
      <tr style="border-bottom:1px solid var(--line)"><td style="padding:8px"><b>Sell and buy in parallel</b></td><td style="padding:8px">Most HDB-to-HDB and resale condo moves</td><td style="padding:8px">Tight timing; needs a clear plan and an extension of stay</td></tr>
      <tr><td style="padding:8px"><b>Buy first</b></td><td style="padding:8px">New launches with a long build time</td><td style="padding:8px">ABSD paid up front on private property; refund only if you sell in time</td></tr>
    </tbody>
  </table>
  <h2 id="costs">Costs families forget</h2>
  <ul>
    <li>Stamp duty and legal fees on the purchase</li>
    <li>Renovation and furniture (usually more than planned)</li>
    <li>Moving, and rent if there's a gap</li>
    <li>Higher maintenance fees in a condo</li>
  </ul>
  <h2 id="safe">The SAFE check</h2>
  <p>Before you sell, we check that the <b>Sale</b> pays for the move, money is set <b>Aside</b> for emergencies, <b>Four</b> years of the mortgage are covered, and it all holds <b>Even</b> if rates rise. If it passes, upgrade with confidence. If not, we adjust the plan.</p>
  <div class="note"><b>My honest advice:</b> the families who are happiest a year later didn't buy the biggest home they could. They bought the one that still left room to breathe.</div>
'''

# ---------------------------------------------------------------- GUIDE: RIGHTSIZE
RIGHTSIZE_FAQ = [
    ("Will we really free up much cash?", "Often yes, but less than the headline sale price suggests. CPF refunds go back to your CPF account first. I'll show you the cash and CPF figures separately so there are no surprises."),
    ("What is the Silver Housing Bonus?", "A cash bonus for eligible older Singaporeans who rightsize to a 3-room or smaller flat and use part of the sale proceeds to top up their CPF Retirement Account. Conditions apply, so check your eligibility with CPF before you plan around it."),
    ("We own a condo. Can we downsize to an HDB resale flat?", "Yes. The 15-month wait-out period for private property owners buying a resale HDB flat was removed in July 2026 for buyers who don't take an HDB loan. Check the current conditions for your case."),
    ("Can we stay in our flat while we look for the next one?", "Yes. We can plan the sale and purchase in parallel, and arrange an extension of stay with your buyer if needed, so you only move once."),
    ("Is rightsizing the only option?", "No. Some families stay put and unlock cash through HDB schemes, rent out a room, or simply wait. We'll look at all of them before deciding."),
]
RIGHTSIZE_BODY = '''
  <div class="answer"><b>Short answer</b>Rightsizing means selling a bigger home and moving to a smaller one to free up cash and cut upkeep. Before you sell, check three things: what you'll actually keep after CPF refunds, where you'll live while you move, and whether schemes such as the Silver Housing Bonus apply to you.</div>
  <p>The kids have grown up and moved out. The 5-room flat that was once too small now feels too big, and too much to clean. Rightsizing can be a great move, but it's also leaving the family home, so let's do it properly.</p>
  <h2 id="options">Your options</h2>
  <ul>
    <li><b>A smaller resale flat</b> near your children, your mosque or your clinic.</li>
    <li><b>A 2-room Flexi flat</b> on a shorter lease, designed for seniors.</li>
    <li><b>A Community Care Apartment</b>, with care services built in.</li>
    <li><b>Staying put</b> and unlocking value through HDB schemes, if moving isn't right.</li>
  </ul>
  <h2 id="numbers">Getting the numbers right</h2>
  <p>Your sale price minus any loan, minus the CPF refund with accrued interest, gives the cash you'll receive. The CPF refund goes back to your CPF account, which is good for retirement but isn't spending money. I'll show you both figures clearly.</p>
  <h2 id="schemes">Schemes worth checking</h2>
  <p><b>Silver Housing Bonus:</b> eligible seniors who rightsize to a 3-room or smaller flat and top up their CPF Retirement Account may receive a cash bonus. Conditions apply.</p>
  <p><b>Coming from a condo?</b> The 15-month wait-out period for private property owners buying a resale HDB flat was removed in July 2026 for buyers not taking an HDB loan. That makes condo-to-HDB rightsizing much simpler than before.</p>
  <h2 id="timing">Move once, not twice</h2>
  <p>Most rightsizers want to avoid renting in between. We plan the sale and the purchase in parallel and, if needed, arrange a temporary extension of stay with your buyer so you can move straight into the next home.</p>
  <h2 id="heart">The part that isn't about money</h2>
  <p>This is often the home where the kids grew up. Talk it through as a family before you list, and involve the children if they'll be helping with the move. A decision everyone understands is much easier to live with.</p>
  <div class="note"><b>How I help:</b> one sit-down with the whole family to lay out the numbers and options, then a plan that moves at your pace. Malay or English, whichever is comfortable.</div>
'''

# ---------------------------------------------------------------- SALE CHECK
SC_FAQ = [
    ("Is it really free?", "Yes. No obligation to list, and I won't chase you. Most people simply want to know their numbers."),
    ("How accurate is it?", "It's based on recent transactions in your block and nearby blocks. For a firmer figure, I'll view the flat and look at its floor, facing, condition and renovation."),
    ("Will you call me?", "Only if you ask. I reply on WhatsApp, where you can read it in your own time."),
]
SALE_CHECK = '''<section class="article-head"><div class="wrap split">
  <div>
    <nav class="crumbs" aria-label="Breadcrumb"><a href="{{L:home}}">Home</a> / Free Sale Check</nav>
    <h1>What could your flat sell for, and what would you keep?</h1>
    <p class="lede">Send me your postal code. I'll reply on WhatsApp with recent sales in your block and a rough estimate of the cash you'd keep after selling. Free, with no obligation.</p>
    <ul class="ticks"><li>Recent transacted prices in your block</li><li>A realistic price range, not a sales pitch</li><li>Rough cash proceeds after loan and CPF refund</li><li>A personal reply from Andik, usually the same day</li></ul>
    <h2 style="margin-top:34px;font-size:30px">Questions</h2>
    [[FAQ]]
  </div>
  <div>''' + sale_check_form() + '''</div>
</div></section>'''

NOT_FOUND = '''<section class="article-head"><div class="wrap">
  <h1>This page has moved, or never existed.</h1>
  <p class="lede">Try the <a href="{{L:home}}">home page</a>, the <a href="{{L:guides}}">guides</a>, or WhatsApp me directly at +65 8736 8736.</p>
</div></section>'''

# ---------------------------------------------------------------- PAGES
PAGES = [
    dict(key="home", url="/", file="index.html", h1_short="Home",
         title="Andik Imran | PropNex Property Consultant in Singapore (English & Malay)",
         desc="Hi, I'm Andik, a friendly PropNex property consultant since 2019. Buying, selling, upgrading or renting in Singapore? 100+ families helped, 65+ five-star reviews. Call or WhatsApp +65 8736 8736.",
         body=HOME, faq=HOME_FAQ),
    dict(key="about", url="/about", file="about.html", h1_short="About Andik Imran",
         title="About Andik Imran | PropNex Associate Group Director",
         desc="Husband, dad of four and PropNex Associate Group Director. Top rookie in 2019 and top producer every year since. Meet Andik Imran and Mirta Syazanna of Homes with AIMS.",
         body=ABOUT),
    dict(key="reviews", url="/reviews", file="reviews.html", h1_short="Reviews",
         title="Reviews & Client Stories | Andik Imran, PropNex",
         desc="Real stories from HDB families who sold and upgraded with Andik Imran. 65+ five-star Google reviews since 2019.",
         body=REVIEWS_PAGE),
    dict(key="safe", url="/safe-upgrading-plan", file="safe-upgrading-plan.html", h1_short="The SAFE Upgrading Plan",
         title="The SAFE Upgrading Plan | Upgrade Your HDB Without Stretching",
         desc="Sale pays for it, Aside first, Four years covered, Even if rates rise. The four checks Andik Imran runs before any family upgrades from their HDB.",
         body=SAFE, faq=SAFE_FAQ),
    dict(key="newlaunch", url="/new-launch", file="new-launch.html", h1_short="New launch for HDB upgraders",
         title="New Launch Condo & EC for HDB Upgraders | Andik Imran",
         desc="Upgrading from HDB to a new launch condo or EC? Plan your HDB sale, ABSD, CPF and progressive payments in the right order. No fee to buyers for new launches.",
         body=NEW_LAUNCH, faq=NL_FAQ),
    dict(key="guides", url="/guides", file="guides/index.html", h1_short="Guides",
         title="Guides for HDB Sellers & Upgraders in Singapore | Andik Imran",
         desc="Plain-English guides on upgrading after MOP, selling an inherited HDB flat (faraid), selling during a divorce and rightsizing. Written by PropNex agent Andik Imran.",
         body=GUIDES),
    dict(key="g-upgrade", url="/guides/upgrading-from-hdb-after-mop", file="guides/upgrading-from-hdb-after-mop.html",
         h1_short="Upgrading from your HDB after MOP: sell first or buy first?", crumbs=[("guides", "Guides")],
         title="Upgrading From HDB After MOP: Sell First or Buy First? (2026 Guide)",
         desc="Past MOP and thinking of upgrading? What your HDB sale really gives you, how much you can borrow, ABSD, and whether to sell first or buy first.",
         article=dict(published="2026-11-24", modified="2026-11-24"), faq=UPGRADE_FAQ,
         body=article_shell("Upgrading after MOP", "Upgrading from your HDB after MOP: sell first or buy first?",
                            "What your sale really gives you, what you can safely borrow, and the order of moves that keeps your family comfortable.",
                            [("mop", "Are you past MOP?"), ("proceeds", "What your sale gives you"), ("loan", "How much you can borrow"), ("order", "Sell first or buy first?"), ("costs", "Costs families forget"), ("safe", "The SAFE check")],
                            UPGRADE_BODY, [("g-rightsize", "Rightsizing your HDB"), ("safe", "The SAFE Upgrading Plan"), ("newlaunch", "New launch for upgraders")])),
    dict(key="g-faraid", url="/guides/inherited-hdb-flat-faraid", file="guides/inherited-hdb-flat-faraid.html",
         h1_short="Selling an inherited HDB flat: faraid, wills and what to do first", crumbs=[("guides", "Guides")],
         title="Selling an Inherited HDB Flat in Singapore: Faraid, Wills & Steps",
         desc="A parent has passed on and left an HDB flat. Joint tenancy vs tenancy-in-common, faraid and the Syariah Court Inheritance Certificate, probate, HDB eligibility and how the sale works.",
         article=dict(published="2026-11-24", modified="2026-11-24"), faq=FARAID_FAQ,
         body=article_shell("Inherited flat &amp; faraid", "Selling an inherited HDB flat: faraid, wills and what to do first",
                            "When a parent passes on, the flat raises hard questions. Here's the order to take them in, and how to keep the family together while you do.",
                            [("held", "How the flat was held"), ("faraid", "Muslim owners: faraid"), ("non-muslim", "Non-Muslim owners"), ("keep", "Can the family keep it?"), ("sell", "How the sale works"), ("family", "Keeping the family together")],
                            FARAID_BODY, [("g-divorce", "Selling during a divorce"), ("g-rightsize", "Rightsizing your HDB"), ("salecheck", "Free Sale Check")])),
    dict(key="g-divorce", url="/guides/selling-hdb-flat-divorce", file="guides/selling-hdb-flat-divorce.html",
         h1_short="Selling your HDB flat during a divorce", crumbs=[("guides", "Guides")],
         title="Selling Your HDB Flat During a Divorce in Singapore (2026 Guide)",
         desc="Sell or keep the matrimonial HDB flat? Ancillary matters, MOP, HDB eligibility, CPF refunds, documents and how to keep the sale calm.",
         article=dict(published="2026-11-24", modified="2026-11-24"), faq=DIVORCE_FAQ,
         body=article_shell("Selling during a divorce", "Selling your HDB flat during a divorce",
                            "How the decision to sell or keep is made, what MOP means for you, where the money goes, and how to sell without another fight.",
                            [("decide", "Where it's decided"), ("keep", "Keeping the flat"), ("mop", "MOP: the date that matters"), ("money", "Where the money goes"), ("calm", "Keeping the sale calm")],
                            DIVORCE_BODY, [("g-faraid", "Inherited flat &amp; faraid"), ("g-upgrade", "Upgrading after MOP"), ("salecheck", "Free Sale Check")])),
    dict(key="g-rightsize", url="/guides/rightsizing-hdb-flat", file="guides/rightsizing-hdb-flat.html",
         h1_short="Rightsizing your HDB when the kids have moved out", crumbs=[("guides", "Guides")],
         title="Rightsizing Your HDB Flat in Singapore: Options, Schemes & Timing",
         desc="Kids moved out? Rightsizing options (smaller resale, 2-room Flexi, Community Care Apartments), the Silver Housing Bonus, condo-to-HDB rules and how to move only once.",
         article=dict(published="2026-11-24", modified="2026-11-24"), faq=RIGHTSIZE_FAQ,
         body=article_shell("Rightsizing", "Rightsizing your HDB when the kids have moved out",
                            "How to free up cash, cut the upkeep and stay close to family, without moving twice.",
                            [("options", "Your options"), ("numbers", "Getting the numbers right"), ("schemes", "Schemes worth checking"), ("timing", "Move once, not twice"), ("heart", "The part that isn't about money")],
                            RIGHTSIZE_BODY, [("g-upgrade", "Upgrading after MOP"), ("g-faraid", "Inherited flat &amp; faraid"), ("salecheck", "Free Sale Check")])),
    dict(key="salecheck", url="/sale-check", file="sale-check.html", h1_short="Free Sale Check",
         title="Free HDB Sale Check | What Your Flat Could Sell For | Andik Imran",
         desc="Send your postal code and get recent sales in your block plus a rough estimate of the cash you'd keep after selling. Free, on WhatsApp, no obligation.",
         body=SALE_CHECK, faq=SC_FAQ),
    dict(key="notfound", url="/404", file="404.html", h1_short="Page not found", noindex=True,
         title="Page not found | Andik Imran", desc="This page could not be found.", body=NOT_FOUND),
]

from content_extra import EXTRA_PAGES
from content_estates import ESTATE_PAGES, ESTATES
from content_malay import MALAY_PAGES
from content_articles import ARTICLES

ARTICLE_PAGES = []
for _a in ARTICLES:
    ARTICLE_PAGES.append(dict(
        key="a-" + _a["slug"], url="/guides/" + _a["slug"], file="guides/" + _a["slug"] + ".html",
        h1_short=_a["h1"], crumbs=[("guides", "Guides")], title=_a["title"], desc=_a["desc"],
        article=dict(published=_a["published"], modified=_a.get("modified", _a["published"])), faq=_a.get("faq") or None,
        body=article_shell(_a["crumb"], _a["h1"], _a["intro"], _a.get("toc", []), _a["body"], _a.get("related", [("guides", "All guides")]))))
_cards = "".join(
    '<a class="card situation" href="{{L:a-' + _a["slug"] + '}}"><p class="who">' + _a["published"] + '</p><h3>' + _a["h1"] + '</h3><p>' + _a["intro"] + '</p><span class="more">Read →</span></a>'
    for _a in ARTICLES[:12])
for _p in PAGES:
    if _p["key"] == "guides":
        _p["body"] = _p["body"].replace("[[ARTICLES]]", ('  <h2 style="margin-top:56px">Latest articles</h2>\n  <div class="grid g3" style="margin-top:20px">' + _cards + '</div>\n') if ARTICLES else "")
PAGES[-1:-1] = EXTRA_PAGES + ESTATE_PAGES + MALAY_PAGES + ARTICLE_PAGES

for _p in PAGES:
    _p["body"] = _p["body"].replace("{{GR}}", SITE["google_reviews"])
