#!/usr/bin/env python3
"""Builds andikimran.com as plain static HTML.
   python3 build.py prod     -> ../site     (clean URLs, deploy to Vercel)
   python3 build.py preview  -> ../preview  (relative .html links, for previewing anywhere)
"""
import json, os, re, sys, shutil, html
from urllib.parse import quote
from content import PAGES, SITE

MODE = sys.argv[1] if len(sys.argv) > 1 else "prod"
OUT = os.path.join(os.path.dirname(__file__), ".." if MODE == "prod" else "../preview")
DOMAIN = SITE["domain"]

ROUTES = {p["key"]: (p["url"], p["file"]) for p in PAGES}


def rel_prefix(file):
    return "../" * file.count("/")


def link(key, cur_file):
    anchor = ""
    if "#" in key:
        key, anchor = key.split("#", 1)
        anchor = "#" + anchor
    url, file = ROUTES[key]
    if MODE == "prod":
        return url + anchor
    return rel_prefix(cur_file) + file + anchor


def img_src(name, cur_file):
    return ("/img/" + name) if MODE == "prod" else rel_prefix(cur_file) + "img/" + name


def asset(name, cur_file):
    return ("/assets/" + name) if MODE == "prod" else rel_prefix(cur_file) + "assets/" + name


def wa(text):
    return "https://wa.me/" + SITE["wa"] + "?text=" + quote(text)


def fill(s, cur_file):
    s = re.sub(r"\{\{L:([^}]+)\}\}", lambda m: link(m.group(1), cur_file), s)
    s = re.sub(r"\{\{IMG:([^}]+)\}\}", lambda m: img_src(m.group(1), cur_file), s)
    s = re.sub(r"\{\{WA:([^}]*)\}\}", lambda m: html.escape(wa(m.group(1))), s)
    s = re.sub(
        r"\{\{PIC:([^|}]+)\|([^}]+)\}\}",
        lambda m: f'<img src="{img_src(m.group(1), cur_file)}" alt="{html.escape(m.group(2))}" loading="lazy" decoding="async">',
        s,
    )
    return s


NAV = [("guides", "Guides"), ("calculator", "Calculator"), ("safe", "SAFE plan"), ("newlaunch", "New launch"), ("reviews", "Reviews"), ("about", "About")]

CHAT_ICON = '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.4 8.4 0 0 1-12.3 7.5L3 21l2-5.4A8.4 8.4 0 1 1 21 11.5Z"/></svg>'


def header(cur_key, cur_file):
    items = []
    for k, label in NAV:
        cur = ' aria-current="page"' if (k == cur_key or (k == "guides" and (cur_key.startswith("g-") or cur_key.startswith("e-") or cur_key == "estates"))) else ""
        items.append(f'<a href="{link(k, cur_file)}"{cur}>{label}</a>')
    items.append(f'<a class="btn wa" href="{wa("Hi Andik! I found your website and would like to chat.")}">{CHAT_ICON}8736 8736</a>')
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="wrap">
  <a class="brand" href="{link("home", cur_file)}">Andik Imran<small>Property Consultant · PropNex</small></a>
  <a class="brand-pnx" href="{link("about", cur_file)}" aria-label="PropNex Realty"><img src="{img_src("propnex-logo.png", cur_file)}" alt="PropNex Realty" height="28"><span>PropNex</span></a>
  <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav class="nav" id="nav" aria-label="Main">{"".join(items)}</nav>
</div></header>'''


def footer(cur_file):
    L = lambda k: link(k, cur_file)
    return f'''<footer><div class="wrap">
  <div class="foot">
    <div>
      <div class="brand" style="color:#fff">Andik Imran</div>
      <img class="foot-logo" src="{img_src("propnex-logo-white.png", cur_file)}" alt="PropNex Realty" loading="lazy">
      <p style="margin-top:14px;max-width:34ch">Friendly property consultant with PropNex. Buying, selling, upgrading or renting, in English or Malay.</p>
      <p><a href="tel:+6587368736">Call +65 8736 8736</a><br><a href="{wa("Hi Andik, I found you through your website.")}">WhatsApp +65 8736 8736</a></p>
    </div>
    <div><h4>Explore</h4><ul>
      <li><a href="{L("salecheck")}">Free Sale Check</a></li>
      <li><a href="{L("calculator")}">Loan calculator</a></li>
      <li><a href="{L("safe")}">SAFE Upgrading Plan</a></li>
      <li><a href="{L("newlaunch")}">New launch</a></li>
      <li><a href="{L("reviews")}">Reviews</a></li>
      <li><a href="{L("about")}">About Andik</a></li>
      <li style="margin-top:14px"><b style="color:#fff">Estates</b></li>
      <li><a href="{L("e-yishun")}">Yishun</a> · <a href="{L("e-punggol")}">Punggol</a> · <a href="{L("e-sengkang")}">Sengkang</a></li>
      <li><a href="{L("e-tampines")}">Tampines</a> · <a href="{L("e-pasirris")}">Pasir Ris</a></li>
    </ul></div>
    <div><h4>Guides</h4><ul>
      <li><a href="{L("g-upgrade")}">Upgrading after MOP</a></li>
      <li><a href="{L("g-faraid")}">Inherited flat &amp; faraid</a></li>
      <li><a href="{L("g-divorce")}">Selling during a divorce</a></li>
      <li><a href="{L("g-rightsize")}">Rightsizing</a></li>
      <li><a href="{L("g-first")}">First-time buyers</a></li>
      <li><a href="{L("g-hdb2hdb")}">HDB to HDB timeline</a></li>
      <li><a href="{L("g-hdb2pvt")}">HDB to private resale timeline</a></li>
      <li><a href="{L("g-hdb2nl")}">HDB to new launch timeline</a></li>
      <li><a href="{L("g-ssd")}">Seller's Stamp Duty (SSD)</a></li>
    </ul></div>
    <div><h4>Elsewhere</h4><ul>
      <li><a href="https://www.homeswithaims.com">Homes with AIMS</a></li>
      <li><a href="https://www.instagram.com/homeswithaims/">Instagram @homeswithaims</a></li>
      <li><a href="https://www.instagram.com/andikimran/">Instagram @andikimran</a></li>
      <li><a href="https://www.tiktok.com/@andikimran">TikTok @andikimran</a></li>
      <li><a href="{SITE["google_reviews"]}">Google reviews</a></li>
    </ul></div>
  </div>
  <div class="legal">
    Andik Imran, Associate Group Director · CEA Reg. No. R061801F &nbsp;|&nbsp; Mirta Syazanna, Associate Director · CEA Reg. No. R070524E<br>
    PropNex Realty Pte Ltd · CEA Licence No. L3008022J<br>
    General information only, not legal, tax or financial advice. HDB, CPF and bank rules change, so we check every case against the rules in force at the time. © 2026 Andik Imran.
  </div>
</div></footer>
<a class="wa-float" href="{wa("Hi Andik, I found you through your website.")}" aria-label="WhatsApp Andik">{CHAT_ICON.replace('class="ico"', '')}</a>'''


def person_graph():
    url = DOMAIN + "/"
    return [
        {
            "@type": "Person",
            "@id": url + "#andik",
            "name": "Andik Imran",
            "jobTitle": "Associate Group Director",
            "url": url,
            "image": DOMAIN + "/img/andik-imran.webp",
            "worksFor": {"@type": "RealEstateAgent", "name": "PropNex Realty Pte Ltd"},
            "knowsLanguage": ["English", "Malay"],
            "spouse": {"@type": "Person", "name": "Mirta Syazanna"},
            "sameAs": SITE["same_as"],
        },
        {
            "@type": "RealEstateAgent",
            "@id": url + "#agent",
            "name": "Andik Imran – PropNex",
            "url": url,
            "image": DOMAIN + "/img/andik-mirta-hero.webp",
            "telephone": "+65 8736 8736",
            "priceRange": "$$",
            "founder": {"@id": url + "#andik"},
            "address": {"@type": "PostalAddress", "addressLocality": "Singapore", "addressCountry": "SG"},
            "areaServed": {"@type": "Country", "name": "Singapore"},
            "knowsLanguage": ["English", "Malay"],
            "sameAs": SITE["same_as"],
        },
        {"@type": "WebSite", "@id": url + "#site", "url": url, "name": "Andik Imran", "inLanguage": "en-SG"},
    ]


def page_schema(p):
    url = DOMAIN + (p["url"] if p["url"] != "/" else "/")
    graph = person_graph()
    crumbs = [{"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN + "/"}]
    for i, (k, name) in enumerate(p.get("crumbs", []), start=2):
        crumbs.append({"@type": "ListItem", "position": i, "name": name, "item": DOMAIN + ROUTES[k][0]})
    if p["key"] != "home":
        crumbs.append({"@type": "ListItem", "position": len(crumbs) + 1, "name": p["h1_short"], "item": url})
        graph.append({"@type": "BreadcrumbList", "itemListElement": crumbs})
    if p.get("area"):
        graph.append({
            "@type": "Service",
            "name": "Property agent services in " + p["area"],
            "serviceType": "Real estate agent",
            "provider": {"@id": DOMAIN + "/#agent"},
            "areaServed": {"@type": "Place", "name": p["area"] + ", Singapore"},
            "url": url,
        })
    if p.get("article"):
        graph.append({
            "@type": "Article",
            "headline": p["h1_short"],
            "description": p["desc"],
            "author": {"@id": DOMAIN + "/#andik"},
            "publisher": {"@id": DOMAIN + "/#andik"},
            "datePublished": p["article"]["published"],
            "dateModified": p["article"]["modified"],
            "mainEntityOfPage": url,
            "image": DOMAIN + "/img/og-andik-imran.jpg",
            "inLanguage": "en-SG",
        })
    if p.get("faq"):
        graph.append({
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
                for q, a in p["faq"]
            ],
        })
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)


def faq_html(faq):
    out = ['<div class="faq">']
    for q, a in faq:
        out.append(f"<details><summary>{html.escape(q)}</summary><div><p>{a}</p></div></details>")
    out.append("</div>")
    return "".join(out)


def render(p):
    f = p["file"]
    url = DOMAIN + p["url"]
    body = p["body"]
    if p.get("faq"):
        body = body.replace("[[FAQ]]", faq_html(p["faq"]))
    body = fill(body, f)
    robots = '<meta name="robots" content="noindex">' if p.get("noindex") else '<meta name="robots" content="index,follow,max-image-preview:large">'
    analytics = SITE["analytics"] if MODE == "prod" else ""
    extra = "".join(f'<script src="{asset(x, f)}" defer></script>' for x in p.get("scripts", []))
    return f'''<!DOCTYPE html>
<html lang="en-SG">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(p["title"])}</title>
<meta name="description" content="{html.escape(p["desc"])}">
<link rel="canonical" href="{url}">
{robots}
<meta property="og:type" content="{"article" if p.get("article") else "website"}">
<meta property="og:site_name" content="Andik Imran">
<meta property="og:title" content="{html.escape(p["title"])}">
<meta property="og:description" content="{html.escape(p["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/img/og-andik-imran.jpg">
<meta property="og:locale" content="en_SG">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0B2545">
<link rel="icon" href="{asset("favicon.svg", f)}" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="{asset("site.css", f)}">
<script type="application/ld+json">
{page_schema(p)}
</script>
{analytics}
</head>
<body>
{header(p["key"], f)}
<main id="main">
{body}
</main>
{footer(f)}
<script src="{asset("site.js", f)}" defer></script>{extra}
</body>
</html>
'''


def main():
    if os.path.exists(OUT):
        for name in os.listdir(OUT):
            if name == "img":
                continue
            path = os.path.join(OUT, name)
            shutil.rmtree(path) if os.path.isdir(path) else os.remove(path)
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    os.makedirs(os.path.join(OUT, "img"), exist_ok=True)
    here = os.path.dirname(__file__)
    for name in os.listdir(os.path.join(here, "img")):
        shutil.copy(os.path.join(here, "img", name), os.path.join(OUT, "img", name))
    for a in ["site.css", "site.js", "calc.js", "favicon.svg"]:
        shutil.copy(os.path.join(here, a), os.path.join(OUT, "assets", a))
    for p in PAGES:
        dest = os.path.join(OUT, p["file"])
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w") as fh:
            fh.write(render(p))
    if MODE == "prod":
        today = "2026-11-24"
        urls = "".join(
            f"<url><loc>{DOMAIN}{p['url']}</loc><lastmod>{p.get('article', {}).get('modified', today)}</lastmod></url>\n"
            for p in PAGES if not p.get("noindex")
        )
        open(os.path.join(OUT, "sitemap.xml"), "w").write(
            f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
        open(os.path.join(OUT, "robots.txt"), "w").write(
            f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
        open(os.path.join(OUT, "llms.txt"), "w").write(SITE["llms"])
        open(os.path.join(OUT, "vercel.json"), "w").write(json.dumps({
            "cleanUrls": True,
            "trailingSlash": False,
            "redirects": [
                {"source": "/blog", "destination": "/guides", "permanent": True},
                {"source": "/blog/:path*", "destination": "/guides", "permanent": True},
                {"source": "/editorial", "destination": "/guides", "permanent": True},
                {"source": "/home", "destination": "/", "permanent": True},
            ],
            "headers": [
                {"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=86400"}]},
                {"source": "/img/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=2592000"}]},
            ],
        }, indent=2))
    print("built", len(PAGES), "pages ->", os.path.abspath(OUT))


if __name__ == "__main__":
    main()
