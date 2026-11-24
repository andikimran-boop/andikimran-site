# /malay-property-agent — one focused page for "Malay property agent" searches.
from content import sale_check_form, CHAT, UPDATED, GOOGLE, google_cards

MALAY_FAQ = [
    ("Do you only work with Malay clients?", "Not at all. I work with families of every background. Many of my clients are Malay families, and I'm glad to explain everything in Malay when that's more comfortable."),
    ("Boleh bincang dalam Bahasa Melayu?", "Boleh. Saya selesa berbincang dalam Bahasa Melayu atau English, dan ramai keluarga guna kedua-duanya dalam satu perjumpaan."),
    ("Can you help with a flat under faraid?", "Yes. I work alongside your lawyer or the Syariah Court process on the property side: valuation, family agreement on price and timeline, and the HDB sale. My <a href=\"{{L:g-faraid}}\">faraid guide</a> explains the steps."),
    ("Can my parents join the meeting?", "Please do. Many families decide together with Mak and Abah, so I'm happy to meet at home and explain the numbers to everyone in the language they're comfortable with."),
    ("Which areas do you cover?", "All of Singapore. I know <a href=\"{{L:e-punggol}}\">Punggol</a>, <a href=\"{{L:e-sengkang}}\">Sengkang</a>, <a href=\"{{L:e-tampines}}\">Tampines</a>, <a href=\"{{L:e-pasirris}}\">Pasir Ris</a> and <a href=\"{{L:e-yishun}}\">Yishun</a> especially well."),
]

MALAY_PAGE = '''<section class="article-head"><div class="wrap split">
  <div>
    <nav class="crumbs" aria-label="Breadcrumb"><a href="{{L:home}}">Home</a> / Malay property agent</nav>
    <h1>Looking for a Malay property agent in Singapore?</h1>
    <p class="lede">Hi, I'm Andik, a PropNex property consultant since 2019. Many of the families I work with are Malay families who'd rather talk about something this big, their home, their CPF, their parents' flat, in Malay. Boleh, no problem at all.</p>
    <div class="btns">
      <a class="btn primary" href="{{WA:Assalamualaikum Andik, saya nak tanya pasal rumah.}}">''' + CHAT + '''WhatsApp saya</a>
      <a class="btn ghost" href="{{L:salecheck}}">Free property report</a>
    </div>
    <p class="phone">Call or WhatsApp <a href="tel:+6587368736">+65 8736 8736</a> · Bahasa Melayu or English</p>
  </div>
  <div class="portrait">{{PIC:andik-imran.webp|Andik Imran, Malay-speaking PropNex property agent in Singapore}}</div>
</div></section>

<section class="band paper"><div class="wrap">
  <div class="section-head"><h2>Why families look for a Malay-speaking agent</h2><p class="lede">It's rarely just about language. It's about being understood: how your family decides, who's involved, and what matters to you.</p></div>
  <div class="grid g3">
    <div class="card"><h3>Mak and Abah can follow along</h3><p>Big decisions often include parents. I explain the numbers, the steps and the risks in Malay so everyone at the table understands, not just the person who speaks the most English.</p></div>
    <div class="card"><h3>Faraid and family flats</h3><p>When a parent passes on, the flat may follow faraid and need a Syariah Court Inheritance Certificate. I handle the property side calmly and keep every sibling in the loop. <a href="{{L:g-faraid}}">Read the guide</a>.</p></div>
    <div class="card"><h3>Staying near family</h3><p>Many families want to live near their parents, or bring them closer. I'll help you find the right estate and check if the Proximity Housing Grant applies.</p></div>
    <div class="card"><h3>Money talk, without pressure</h3><p>CPF refunds, cash proceeds, loan limits. I lay it all out plainly with my <a href="{{L:safe}}">SAFE Upgrading Plan</a>, so you only move when the numbers are comfortable.</p></div>
    <div class="card"><h3>Upgrading, rightsizing, first homes</h3><p>Whether it's your first flat, a bigger home for growing kids, or something smaller after they've moved out, I've walked with families at every stage.</p></div>
    <div class="card"><h3>A dad of four, like many of you</h3><p>Mirta and I started in a 3-room BTO. I know what it's like to juggle school runs, family and a home decision all at once.</p></div>
  </div>
</div></section>

<section class="band" lang="ms"><div class="wrap split rev">
  <div class="prose">
    <h2>Dalam Bahasa Melayu</h2>
    <p>Assalamualaikum dan salam sejahtera. Saya Andik Imran, ejen hartanah PropNex sejak 2019. Ramai keluarga yang saya bantu lebih selesa berbincang dalam Bahasa Melayu, terutamanya bila melibatkan ibu bapa, duit CPF dan keputusan besar untuk keluarga.</p>
    <p>Sama ada nak jual flat HDB, naik taraf ke rumah yang lebih besar, beli rumah pertama, atau uruskan rumah arwah ibu bapa mengikut faraid, saya akan terangkan langkah demi langkah, dengan angka yang jelas, sebelum apa-apa keputusan dibuat.</p>
    <p>Tiada tekanan. Kalau angka belum sesuai untuk keluarga, saya akan beritahu dengan jujur. Lebih baik tunggu setahun daripada menyesal kemudian.</p>
    <p><b>WhatsApp saya di +65 8736 8736.</b> Boleh bincang dalam BM atau English, ikut keselesaan.</p>
  </div>
  <div class="card" style="align-self:start">
    <h3>Nak tahu harga flat anda?</h3>
    <p>Hantar poskod anda. Saya akan balas di WhatsApp dengan harga jualan terkini di blok anda dan anggaran wang tunai selepas jual.</p>
    <a class="btn wa" href="{{WA:Assalamualaikum Andik, saya nak tahu anggaran harga flat saya. Poskod saya: }}">''' + CHAT + '''WhatsApp saya</a>
  </div>
</div></section>

<section class="band paper"><div class="wrap">
  <div class="section-head"><h2>What families say</h2><p class="lede">Real Google reviews, first names only.</p></div>
  <div class="grid g3">''' + google_cards(GOOGLE[:6]) + '''</div>
  <div class="btns"><a class="btn ghost" href="{{GR}}">All reviews on Google</a></div>
</div></section>

<section class="band"><div class="wrap prose" style="max-width:860px">
  <h2>Estates I know well</h2>
  <p>I work across Singapore. These are the towns I'm asked about most: <a href="{{L:e-punggol}}">Punggol</a>, <a href="{{L:e-sengkang}}">Sengkang</a>, <a href="{{L:e-tampines}}">Tampines</a>, <a href="{{L:e-pasirris}}">Pasir Ris</a> and <a href="{{L:e-yishun}}">Yishun</a>.</p>
  <h2 id="faq">Questions</h2>
  [[FAQ]]
</div></section>

<section class="band dark"><div class="wrap split">
  <div><h2>Let's talk, in Malay or English</h2><p class="lede">Get a free property report on WhatsApp in minutes: your indicative price and recent sales in your block. No obligation.</p></div>
  <div>''' + sale_check_form() + '''</div>
</div></section>'''

MALAY_PAGES = [dict(
    key="malay", url="/malay-property-agent", file="malay-property-agent.html", h1_short="Malay property agent in Singapore",
    title="Malay Property Agent in Singapore | Andik Imran, PropNex",
    desc="Looking for a Malay-speaking property agent in Singapore? Andik Imran (PropNex, since 2019) helps families buy, sell and upgrade, including faraid cases. Bahasa Melayu or English. WhatsApp +65 8736 8736.",
    faq=MALAY_FAQ, body=MALAY_PAGE)]
