# Estate pages: /property-agent/<estate>. Each one has its own unique content.
# TODO(Andik): add real local stories (e.g. a Yishun sale) to "stories" when you have them.
from content import sale_check_form, CHAT, UPDATED, REVIEWS, SOLD

CHOOSE = [
    ("Ask what they've sold nearby, and for how much", "Recent, real transactions near your block tell you more than any slogan. Ask how they priced them and how long they took."),
    ("Check their reviews and CEA registration", "Look for recent Google reviews from real clients, and check the agent's name on the CEA Public Register."),
    ("Ask them to explain your numbers", "Not just the selling price: your CPF refund, cash proceeds and timeline. If they can't explain it simply, keep looking."),
    ("Be careful with the highest valuation", "An exciting number can be a way to win your listing. Ask what it's based on."),
    ("Ask how they'll market your home", "Photos, video, portals, social media, and who will actually be at the viewings."),
    ("Pick someone you can talk to", "You'll be messaging this person for months. Make sure they reply, explain, and don't pressure you."),
]


def estate_body(d):
    name = d["name"]
    hi = "".join('<div class="card"><h3>' + t + "</h3><p>" + x + "</p></div>" for t, x in d["highlights"])
    suits = "".join("<li>" + s + "</li>" for s in d["suits"])
    coming = "".join("<li>" + s + "</li>" for s in d["coming"])
    tips = "".join("<li>" + s + "</li>" for s in d["tips"])
    choose = "".join("<li><b>" + t + ".</b> " + x + "</li>" for t, x in CHOOSE)
    sold = [s for s in SOLD if name in s[2]]
    sold_html = ""
    if sold:
        sold_html = '<h3 style="margin-top:26px">Homes we\'ve sold in ' + name + '</h3><div class="sold" tabindex="0">' + "".join(
            '<figure><div class="pic">{{PIC:' + f + "|Living room of " + a + ", " + dd + '}}</div><figcaption><span class="tag">Sold</span><b>' + a + "</b>" + dd + "</figcaption></figure>"
            for f, a, dd in sold) + "</div>"
    revs = [r for r in REVIEWS if name in r[1]] + d.get("extra_reviews", [])
    rev_html = ""
    if revs:
        rev_html = '<div class="grid g3" style="margin-top:18px">' + "".join(
            '<figure class="card" style="margin:0"><div class="quote-mark">“</div><blockquote style="margin:0 0 14px">' + q + '</blockquote><figcaption><b>' + n + '</b> · <span class="fine">' + w + " · ★★★★★ on Google</span></figcaption></figure>"
            for n, w, q in revs) + "</div>"
    return '''<section class="article-head"><div class="wrap split">
  <div>
    <nav class="crumbs" aria-label="Breadcrumb"><a href="{{L:home}}">Home</a> / <a href="{{L:estates}}">Estates</a> / ''' + name + '''</nav>
    <h1>Looking for a property agent in ''' + name + '''?</h1>
    <p class="lede">''' + d["intro"] + '''</p>
    <div class="btns">
      <a class="btn primary" href="{{WA:Hi Andik! I have a property question about ''' + name + '''.}}">''' + CHAT + '''WhatsApp me</a>
      <a class="btn ghost" href="#check">What's my ''' + name + ''' home worth?</a>
    </div>
    <p class="phone">Call or WhatsApp <a href="tel:+6587368736">+65 8736 8736</a></p>
    <p class="fine" style="margin-top:6px">Prefer Malay? <a href="{{L:malay}}">I'm a Malay-speaking agent</a>, boleh bincang dalam BM.</p>
  </div>
  <div class="card">
    <h3>''' + name + ''' at a glance</h3>
    <ul class="ticks">''' + "".join("<li>" + g + "</li>" for g in d["glance"]) + '''</ul>
    <p class="fine">Last reviewed ''' + UPDATED + '''</p>
  </div>
</div></section>

<section class="band paper"><div class="wrap">
  <div class="section-head"><h2>What makes ''' + name + ''', ''' + name + '''</h2><p class="lede">''' + d["character"] + '''</p></div>
  <div class="grid g3">''' + hi + '''</div>
</div></section>

<section class="band"><div class="wrap split rev">
  <div class="prose">
    <h2 id="suits">Who ''' + name + ''' suits</h2>
    <ul>''' + suits + '''</ul>
    <h2 id="coming">What's coming</h2>
    <ul>''' + coming + '''</ul>
    <p class="fine">Future plans and dates come from public announcements and can change.</p>
    <h2 id="selling">Selling in ''' + name + ''': what buyers look at</h2>
    <ul>''' + tips + '''</ul>
  </div>
  <div class="card" style="align-self:start">
    <h3>Thinking of buying or selling in ''' + name + '''?</h3>
    <p>Tell me your block and what you're thinking. I'll send recent sales nearby and an honest take, no strings attached.</p>
    <a class="btn wa" href="{{WA:Hi Andik! I'm thinking of buying/selling in ''' + name + '''. Can we chat?}}">''' + CHAT + '''Chat on WhatsApp</a>
  </div>
</div></section>

<section class="band paper"><div class="wrap">
  <h2>''' + d["track_title"] + '''</h2>
  <p class="lede">''' + d["track"] + '''</p>
  ''' + sold_html + rev_html + '''
</div></section>

<section class="band"><div class="wrap prose" style="max-width:860px">
  <h2 id="choose">How to choose the best property agent in ''' + name + '''</h2>
  <p>"Best" means different things to different families. Whoever you speak to, me included, here's what I'd check:</p>
  <ul>''' + choose + '''</ul>
  <h2 id="faq">''' + name + ''' questions</h2>
  [[FAQ]]
</div></section>

<section class="band dark" id="check"><div class="wrap split">
  <div><h2>What's your ''' + name + ''' home worth?</h2><p class="lede">Send your postal code. I'll reply on WhatsApp with recent sales in your block and a rough idea of what you'd keep after selling.</p></div>
  <div>''' + sale_check_form() + '''</div>
</div></section>'''


def common_faq(name):
    return [
        ("How much is my " + name + " flat worth?", "It depends on your block, floor, facing, remaining lease and condition. The quickest way: send me your postal code through the <a href=\"{{L:salecheck}}\">free Sale Check</a> and I'll reply with recent transactions in your block."),
        ("Do you only work in " + name + "?", "No, I help clients all over Singapore. But I know " + name + " well, and I'm happy to share what I've seen buyers there care about."),
    ]


ESTATES = [
    dict(key="e-yishun", slug="yishun", name="Yishun",
         intro="Hi, I'm Andik, a PropNex property consultant. Whether you're selling your Yishun flat, buying in the north, or just curious what your home is worth, I'll give you honest, numbers-first advice. In English or Malay.",
         glance=["Two MRT stations on the North-South Line: Yishun and Khatib", "Northpoint City, the largest mall in the north, with the bus interchange built in", "Khoo Teck Puat Hospital and Yishun Community Hospital in town", "Lower Seletar Reservoir, Yishun Park and Yishun Pond Park", "Newest neighbourhood: Chencharu, near Khatib"],
         character="Yishun is one of the north's original new towns, with development starting in 1981. It's big, established and still growing, mixing older blocks with brand-new neighbourhoods.",
         highlights=[
             ("Everything at Northpoint City", "Mall, bus interchange, library and community club in one air-conditioned complex next to Yishun MRT. A lot of daily life happens without leaving it."),
             ("A straight line to town", "Yishun and Khatib are both on the North-South Line, so you get a direct ride to Orchard and the city without changing trains."),
             ("Healthcare on your doorstep", "Khoo Teck Puat Hospital and Yishun Community Hospital sit in the town, and more healthcare facilities are planned nearby."),
             ("Water and green", "Lower Seletar Reservoir, Yishun Park and Yishun Pond Park give you proper space for walks, cycling and weekend fishing."),
             ("Old and new side by side", "Established 1980s blocks near the town centre, and new estates like Chencharu near Khatib. There's a wide spread of prices and flat ages."),
             ("Still evolving", "The Draft Master Plan 2025 adds new homes around Yishun MRT, including the former temporary bus interchange site."),
         ],
         suits=["Families who want more space for their budget than towns nearer the city", "People working in the north: Woodlands, Sembawang, Seletar", "Couples who want to stay near parents already living in the north", "Buyers who value a big mall and hospital within easy reach"],
         coming=["New residential plots around Yishun MRT under URA's Draft Master Plan 2025", "Two more healthcare facilities planned near Khoo Teck Puat Hospital", "New BTO neighbourhoods such as Chencharu, near Khatib"],
         tips=["Distance to Yishun or Khatib MRT and to Northpoint City is the first question buyers ask.", "With many 1980s blocks, remaining lease matters: it affects how much CPF and loan buyers can use, so we price with that in mind.", "Older flats sell better when buyers can picture a renovation: clear photos, a sensible price and renovation ideas help.", "Newer flats near Khatib compete with BTO supply, so condition and floor level carry more weight."],
         track_title="Working with Yishun families",
         track="I'm Andik, a PropNex Associate Group Director since 2019, with 100+ families helped across Singapore and 65+ five-star Google reviews. Ask me for recent Yishun transactions and I'll walk you through them.",
         faq=common_faq("Yishun") + [("Are older Yishun flats harder to sell?", "Not if they're priced and presented well. Buyers for older flats usually want space and location. The remaining lease affects their financing, so it shapes who your buyer is and how we price. I'll explain this clearly before we list.")]),
    dict(key="e-punggol", slug="punggol", name="Punggol",
         intro="Hi, I'm Andik. Mirta and I live near Punggol, and we've sold a good number of homes here. If you're selling, upgrading or buying in Punggol, I'd love to help, with the numbers worked out first.",
         glance=["North East Line (Punggol, Punggol Coast) plus the Punggol LRT loops", "Punggol Waterway Park, Coney Island and the coast", "Punggol Digital District and the SIT campus", "Cross Island Line Punggol Extension targeted for 2032", "A young town full of young families"],
         character="Punggol is Singapore's waterfront town: young, family-heavy and changing fast, with a growing digital business district.",
         highlights=[
             ("Life by the water", "Punggol Waterway runs through the town, with Coney Island and Punggol Point close by. Evening walks and weekend cycling are part of everyday life."),
             ("A business district next door", "Punggol Digital District, with the Singapore Institute of Technology campus, brings jobs and amenities right into the town."),
             ("New MRT at Punggol Coast", "Punggol Coast station opened in December 2024 on the North East Line, serving the digital district and the northern part of town."),
             ("East in 15 minutes, eventually", "The Cross Island Line Punggol Extension is targeted for 2032 and is expected to cut the Punggol to Pasir Ris trip to about 15 minutes."),
             ("LRT loops everywhere", "The East and West LRT loops link most blocks to Punggol MRT, so which station you're near really matters."),
             ("Built for young families", "Plenty of newer flats, playgrounds and childcare. Many owners are now reaching MOP and thinking about their next move."),
         ],
         suits=["Young families who want a newer flat and lots of outdoor space", "People working in the Punggol Digital District, Seletar or the north-east", "Upgraders moving from a smaller Punggol flat to a bigger one nearby", "Families who love cycling, water and parks"],
         coming=["Cross Island Line Punggol Extension, targeted for 2032, linking Punggol to Pasir Ris and the east", "More of the Punggol Digital District opening up, including its first hotel", "Continued MOP waves as newer BTO estates reach five years"],
         tips=["With many similar flats reaching MOP, standing out matters: floor, view, condition and LRT distance decide who wins the buyer.", "Waterway or open views are worth highlighting. Photos and video do a lot of the selling here.", "Most buyers are young families, so they look at the layout, storage, nearby childcare and primary schools.", "Pricing is competitive, so we anchor to recent sales in your block, not the town average."],
         track_title="Homes we've sold in Punggol",
         track="Punggol is home turf for us. Here are some of the Punggol homes we've sold, and what a few of the owners said.",
         faq=common_faq("Punggol") + [("So many flats are reaching MOP. How do I stand out?", "Price right from day one, present the flat well (good photos, decluttering, video), and highlight what's unique: view, floor, a renovated kitchen, distance to the LRT. A flat that stands out in its first two weeks usually sells best.")]),
    dict(key="e-sengkang", slug="sengkang", name="Sengkang",
         intro="Hi, I'm Andik. We live in the north-east and know Sengkang well. Selling in Rivervale, buying in Fernvale, or wondering what your Compassvale flat is worth? Let's talk it through.",
         glance=["North East Line at Sengkang and Buangkok, plus the Sengkang LRT loops", "Sengkang General Hospital and Sengkang Community Hospital", "Sengkang Riverside Park (21 hectares, with mangroves)", "Compass One, Rivervale Mall, Anchorvale Village, The Seletar Mall", "Neighbourhoods: Rivervale, Compassvale, Anchorvale, Fernvale"],
         character="Sengkang is a well-planned family town where homes, LRT and amenities were built together. Each of its 'vale' neighbourhoods has its own feel.",
         highlights=[
             ("Planned from day one", "Sengkang was one of the first new towns built together with its transport links. The LRT loops reach almost every precinct."),
             ("A hospital in town", "Sengkang General Hospital and Sengkang Community Hospital are right here, a real comfort for families with young kids or elderly parents."),
             ("Riverside green", "Sengkang Riverside Park covers 21 hectares, with mangrove and civic areas, and connects to Punggol and the Round Island Route park connectors."),
             ("Four 'vales', four characters", "Rivervale and Compassvale near the town centre, Anchorvale by the river, and Fernvale on the west side near The Seletar Mall."),
             ("Easy to the airport", "Bus service 110 links Compassvale and Anchorvale to all Changi Airport terminals, handy for aviation and airport workers."),
             ("Better links east", "The Cross Island Line Punggol Extension, targeted for 2032, will give the north-east a direct rail link to Pasir Ris and Tampines North."),
         ],
         suits=["Families who want a mature-feeling town with a hospital close by", "People working at Seletar, the airport or in the north-east", "Upgraders who want to stay near family already in Sengkang or Punggol", "Buyers who like a quieter, park-connected neighbourhood"],
         coming=["Cross Island Line Punggol Extension (targeted 2032), improving links to Pasir Ris and Tampines North", "Continued upgrades to park connectors and riverside spaces", "More flats reaching MOP, giving buyers more choice"],
         tips=["Which LRT station you're near, and whether it's on the East or West loop, matters a lot to buyers.", "Distance to Sengkang or Buangkok MRT and to the malls is the next thing they compare.", "Buyers often compare Sengkang with Punggol, so we price against both, not just your street.", "Families check primary schools nearby. We highlight them in the listing."],
         track_title="Homes we've sold in Sengkang",
         track="A few of the Sengkang homes we've sold, plus what one of Mirta's buyers said.",
         extra_reviews=[("Marilyn", "Bought a resale condo in Sengkang with Mirta", "Mirta's patience, expertise and initiative has made our journey as first-time homeowners an incredibly smooth one!")],
         faq=common_faq("Sengkang") + [("Is it better to be near the MRT or just an LRT station?", "Being near Sengkang or Buangkok MRT usually draws more buyers, but a flat right beside a convenient LRT stop with a good view or layout can do just as well. It's about your specific block, so let's look at recent sales near you.")]),
    dict(key="e-tampines", slug="tampines", name="Tampines",
         intro="Hi, I'm Andik. I've helped families sell homes in Tampines, and I know how much the exact part of town matters here. Buying, selling or upgrading in Tampines? Let's get your numbers clear.",
         glance=["East-West Line and Downtown Line stations across town", "Cross Island Line at Tampines North targeted for 2030", "Our Tampines Hub: sports, library, hawker centre and more", "Tampines Mall, Century Square and Tampines 1", "Close to Changi Business Park and the airport"],
         character="Tampines is the east's big, self-contained town. It's Singapore's first regional centre, so you rarely need to leave it for anything.",
         highlights=[
             ("A regional centre", "Tampines was planned as Singapore's first regional centre, with offices, three malls and services clustered around the MRT."),
             ("Our Tampines Hub", "A huge community and lifestyle hub with a stadium, pools, library, hawker centre and government services under one roof."),
             ("Two train lines, a third coming", "East-West Line and Downtown Line stations today, with the Cross Island Line at Tampines North targeted for 2030."),
             ("Work nearby", "Changi Business Park, the airport and the east's industrial estates are close, so many residents have short commutes."),
             ("Tampines North is growing", "A newer neighbourhood with its own upcoming MRT station and integrated transport hub."),
             ("Green corners", "Tampines Eco Green and the park connectors offer quieter spaces inside a busy town."),
         ],
         suits=["Families who want everything in one town: malls, sports, schools, transport", "People working in Changi Business Park, the airport or the east", "Upgraders staying in the east to keep kids in the same schools", "Buyers who like a lively town centre"],
         coming=["Cross Island Line Phase 1, including Tampines North station, targeted for 2030", "An integrated transport hub planned with Tampines North MRT", "Continued growth of the Tampines North neighbourhood"],
         tips=["Tampines is big, so micro-location decides price: which MRT line, which mall, which school.", "Downtown Line access (Tampines West, Tampines East) is a selling point for buyers working in town.", "Families focus on primary schools within reach. We put that front and centre.", "Older blocks near the town centre compete on location; newer Tampines North flats compete on condition."],
         track_title="Homes we've sold in Tampines",
         track="Here are some of the homes we've sold in Tampines, and I'm happy to share recent transactions near your block when we chat.",
         faq=common_faq("Tampines") + [("Which part of Tampines is best?", "It depends on what you need. Near Tampines MRT and the malls is the most convenient; Downtown Line stations suit people working in town; Tampines North gives newer flats and a future MRT. Tell me your priorities and I'll suggest where to look.")]),
    dict(key="e-pasirris", slug="pasir-ris", name="Pasir Ris",
         intro="Hi, I'm Andik. I've sold homes in Pasir Ris, and I love how this town mixes beach life with big, comfortable flats. Thinking of selling, buying or upgrading here? Let's talk.",
         glance=["Pasir Ris MRT on the East-West Line", "Pasir Ris Park and the coast, plus Downtown East", "New Pasir Ris Integrated Transport Hub and Pasir Ris Mall", "Cross Island Line interchange targeted for 2030", "Known for larger, older flats"],
         character="Pasir Ris, 'white sands' in Malay, is the east's seaside town: relaxed, green, and home to some of the roomiest flats around.",
         highlights=[
             ("A beach in your backyard", "Pasir Ris Park stretches along the coast, with cycling paths, mangroves and weekend barbecues. Downtown East is next door for the kids."),
             ("A refreshed town centre", "The Pasir Ris Integrated Transport Hub has opened, with Pasir Ris Mall, a polyclinic, childcare and an air-conditioned bus interchange."),
             ("Space for big families", "Pasir Ris is known for larger, older flats, popular with multi-generation families and anyone who needs room."),
             ("A future interchange", "Pasir Ris station is set to become an interchange with the Cross Island Line, targeted for 2030, plus a new Pasir Ris East station."),
             ("Punggol, one line away", "The Cross Island Line Punggol Extension, targeted for 2032, will link Pasir Ris to Punggol in about 15 minutes."),
             ("Quiet, mature, green", "A mature town being rejuvenated under HDB's Remaking Our Heartland programme, without losing its calm."),
         ],
         suits=["Multi-generation families who need a bigger flat", "Families who love the outdoors and the sea", "People working at Changi, Loyang or the eastern industrial areas", "Upgraders who want more space rather than a condo"],
         coming=["Cross Island Line Phase 1: Pasir Ris interchange and Pasir Ris East station, targeted for 2030", "Cross Island Line Punggol Extension, targeted for 2032", "Continued Remaking Our Heartland upgrades and Friendly Streets"],
         tips=["For bigger, older flats, buyers weigh space against remaining lease. The lease affects their CPF and loan, so we price with that in mind.", "Many buyers plan to renovate. Good photos of the space and a realistic price matter more than staging.", "Distance to Pasir Ris MRT and the new mall is a strong selling point.", "Multi-generation buyers care about layouts with separate living spaces, so we highlight that clearly."],
         track_title="Homes we've sold in Pasir Ris",
         track="One of the Pasir Ris homes we've sold. I'll gladly walk you through recent transactions near your block.",
         faq=common_faq("Pasir Ris") + [("Will the Cross Island Line push Pasir Ris prices up?", "Nobody can promise that. New MRT lines often make an area more attractive, but prices depend on the whole market. I'd plan your move around your family's needs and your numbers, and treat the new line as a bonus.")]),
]

HUB = '''<section class="article-head"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="{{L:home}}">Home</a> / Estates</nav>
  <h1>Estate guides: what makes each town special</h1>
  <p class="lede">I help clients all over Singapore. Here's what I've learned about some of the estates I'm asked about most: who they suit, what's coming, and what buyers look for.</p>
</div></section>
<section class="band paper"><div class="wrap">
  <div class="grid g3">''' + "".join(
    '<a class="card situation" href="{{L:' + e["key"] + '}}"><p class="who">Estate guide</p><h3>' + e["name"] + "</h3><p>" + e["character"] + '</p><span class="more">Read about ' + e["name"] + " →</span></a>"
    for e in ESTATES) + '''</div>
</div></section>
<section class="band dark"><div class="wrap split">
  <div><h2>Don't see your estate?</h2><p class="lede">I work across Singapore. Send me your postal code and I'll come back with recent sales near you.</p></div>
  <div>''' + sale_check_form() + '''</div>
</div></section>'''

ESTATE_PAGES = [dict(key="estates", url="/property-agent", file="property-agent/index.html", h1_short="Estate guides",
                     title="Property Agent by Estate: Yishun, Punggol, Sengkang, Tampines, Pasir Ris | Andik Imran",
                     desc="Estate guides from PropNex consultant Andik Imran: what makes Yishun, Punggol, Sengkang, Tampines and Pasir Ris unique, who each suits, and what buyers look for.",
                     body=HUB)]
for e in ESTATES:
    n = e["name"]
    ESTATE_PAGES.append(dict(
        key=e["key"], url="/property-agent/" + e["slug"], file="property-agent/" + e["slug"] + ".html",
        h1_short="Property agent in " + n, crumbs=[("estates", "Estates")], area=n,
        title="Property Agent in " + n + " | Andik Imran, PropNex",
        desc="Looking for the best property agent in " + n + "? Andik Imran (PropNex, since 2019, 65+ five-star reviews) shares what makes " + n + " unique, what buyers look for, and a free Sale Check. Call or WhatsApp +65 8736 8736.",
        faq=e["faq"], body=estate_body(e)))
