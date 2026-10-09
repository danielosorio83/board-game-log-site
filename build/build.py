#!/usr/bin/env python3
"""Builds every page of the site, in each language, from the content files next to this script.

    python3 build/build.py

English lives at the root (/, /how-to/ ...), Spanish under /es/ and French under /fr/. Edit the text in content_*.py, never the
generated pages: the next build overwrites them.
"""
import importlib
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
BASE = "https://boardgamelog.app"
LANGS = ["en", "es", "fr"]
PAGES = ["home", "how-to", "support", "privacy", "terms"]
META_KEY = {"home": "home", "how-to": "howto", "support": "support", "privacy": "privacy", "terms": "terms"}
SHOT_W, SHOT_H = 540, 1174


def content(lang):
    return importlib.import_module(f"content_{lang}")


def prefix(lang):
    return "" if lang == "en" else f"/{lang}"


def path(lang, page):
    tail = {"home": "/", "how-to": "/how-to/", "support": "/support/", "privacy": "/privacy/", "terms": "/terms/"}[page]
    return (prefix(lang) + tail) if page != "home" else (prefix(lang) + "/")


def esc(text):
    return text.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")


def shot(name, alt, caption=None):
    cap = f"<figcaption>{caption}</figcaption>" if caption else ""
    img = lambda theme: (f'<img class="{theme}" src="/assets/img/app/{theme}/{name}.webp" width="{SHOT_W}" height="{SHOT_H}" '
                         f'alt="{esc(alt)}" loading="lazy" decoding="async">')
    return f'<figure class="shot">{img("light")}{img("dark")}{cap}</figure>'


SUN = '<svg class="icon-sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
MOON = '<svg class="icon-moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>'
EARLY_THEME = '<script>try{var t=localStorage.getItem("theme");if(t==="light"||t==="dark")document.documentElement.setAttribute("data-theme",t)}catch(e){}</script>'


def head(lang, page, title, desc, noindex=False):
    T = content(lang).T
    url = BASE + path(lang, page)
    alternates = "".join(f'<link rel="alternate" hreflang="{l}" href="{BASE + path(l, page)}">\n' for l in LANGS)
    alternates += f'<link rel="alternate" hreflang="x-default" href="{BASE + path("en", page)}">\n'
    other = "".join(f'<meta property="og:locale:alternate" content="{content(l).T["locale"]}">\n' for l in LANGS if l != lang)
    robots = '<meta name="robots" content="noindex">\n' if noindex else ""
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{robots}<link rel="canonical" href="{url}">
{alternates}<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#faf3e3" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#1f0f0c" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Board Game Log">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="{T["locale"]}">
{other}<meta property="og:image" content="{BASE}/assets/img/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/assets/img/favicon-192.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/bricolage-grotesque.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/figtree.woff2" as="font" type="font/woff2" crossorigin>
{EARLY_THEME}
<link rel="stylesheet" href="/assets/css/tokens.css">
<link rel="stylesheet" href="/assets/css/base.css">
<link rel="stylesheet" href="/assets/css/layout.css">
<link rel="stylesheet" href="/assets/css/components.css">
<link rel="stylesheet" href="/assets/css/pages/{"home" if page == "home" else "content"}.css">
<script src="/assets/js/site.js" defer></script>
</head>
'''


def header(lang, page):
    T = content(lang).T
    ui = T["ui"]
    cur = lambda p: ' aria-current="page"' if page == p else ""
    langs = "".join(
        f'<li><a href="{path(l, page if page in PAGES else "home")}" lang="{l}" hreflang="{l}"'
        f'{" aria-current=\"true\"" if l == lang else ""}>{content(l).T["code"]}</a></li>' for l in LANGS)
    return f'''<body>
<a class="skip-link" href="#content">{ui["skip"]}</a>
<header class="site-header">
<div class="container">
<a class="brand" href="{path(lang, "home")}"><img src="/assets/img/logo-96.png" width="40" height="40" alt="">Board Game Log</a>
<div class="header-tools">
<nav class="main-nav" aria-label="{ui["menu"]}"><ul class="nav">
<li><a href="{path(lang, "how-to")}"{cur("how-to")}>{ui["nav_howto"]}</a></li>
<li><a href="{path(lang, "support")}"{cur("support")}>{ui["nav_support"]}</a></li>
</ul></nav>
<nav class="lang-nav" aria-label="{ui["language"]}"><ul class="lang">{langs}</ul></nav>
<button class="theme-toggle" type="button" data-to-dark="{esc(ui["to_dark"])}" data-to-light="{esc(ui["to_light"])}" aria-label="{esc(ui["to_dark"])}">{MOON}{SUN}</button>
</div>
</div>
</header>
'''


def footer(lang):
    ui = content(lang).T["ui"]
    return f'''<footer class="site-footer">
<div class="container">
<div class="footer-top">
<a class="brand" href="{path(lang, "home")}"><img src="/assets/img/logo-96.png" width="40" height="40" alt="">Board Game Log</a>
<nav aria-label="{ui["footer_menu"]}"><ul class="footer-nav">
<li><a href="{path(lang, "how-to")}">{ui["nav_howto"]}</a></li>
<li><a href="{path(lang, "support")}">{ui["nav_support"]}</a></li>
<li><a href="{path(lang, "privacy")}">{ui["nav_privacy"]}</a></li>
<li><a href="{path(lang, "terms")}">{ui["nav_terms"]}</a></li>
<li><a href="mailto:support@boardgamelog.app">support@boardgamelog.app</a></li>
</ul></nav>
</div>
<div class="footer-legal">
<p>{ui["rights"]}</p>
<p>{ui["legal"]} <a href="{path(lang, "terms")}#game-names">{ui["read_more"]}</a>.</p>
</div>
</div>
</footer>
</body>
</html>
'''


def page_head(h1, lead=None, extra=""):
    lead_html = f'<p class="lead">{lead}</p>\n' if lead else ""
    return f'<div class="page-head">\n<div class="container">\n<h1>{h1}</h1>\n{lead_html}{extra}</div>\n</div>\n'


def home(lang):
    T = content(lang).T
    h = T["home"]
    feats = "\n".join(f'<li class="feature"><h3>{a}</h3><p>{b}</p></li>' for a, b in h["features"])
    screens = "\n".join(f'<li>{shot(n, alt, cap)}</li>' for n, alt, cap in h["see"])
    return f'''<main id="content">
<section class="hero" aria-labelledby="hero-title">
<div class="container">
<div class="hero__text">
<h1 id="hero-title">{h["h1"]}</h1>
<p class="hero__lead">{h["lead"]}</p>
<div class="hero__actions">
<span class="status">{h["status"]}</span>
<a class="button button--plain" href="{path(lang, "how-to")}">{h["cta"]}</a>
</div>
</div>
<img class="hero__logo" src="/assets/img/logo-512.webp" srcset="/assets/img/logo-256.webp 256w, /assets/img/logo-512.webp 512w" sizes="(max-width: 700px) 192px, 304px" width="512" height="512" fetchpriority="high" decoding="async" alt="{esc(h["logo_alt"])}">
</div>
</section>

<section class="section" aria-labelledby="does">
<div class="container">
<div class="section__head">
<h2 id="does">{h["does_h"]}</h2>
<p>{h["does_p"]}</p>
</div>
<ul class="features">
{feats}
</ul>
</div>
</section>

<section class="section" aria-labelledby="see">
<div class="container">
<div class="section__head"><h2 id="see">{h["see_h"]}</h2></div>
<ul class="screens">
{screens}
</ul>
</div>
</section>

<section class="section" aria-labelledby="keep">
<div class="container">
<div class="callout keep">
<h2 id="keep">{h["keep_h"]}</h2>
<p>{h["keep_p"]}</p>
<p><a href="{path(lang, "privacy")}">{h["keep_link"]}</a></p>
</div>
</div>
</section>

<section class="section" aria-labelledby="names">
<div class="container">
<div class="names">
<h2 id="names">{h["names_h"]}</h2>
<p>{h["names_p1"]}</p>
<p>{h["names_p2"]}</p>
<p><a href="{path(lang, "terms")}#game-names">{h["names_link"]}</a></p>
</div>
</div>
</section>
</main>
'''


def howto(lang):
    T = content(lang).T
    h = T["howto"]
    out = [f'<main id="content">\n' + page_head(h["h1"], h["lead"]) + '<div class="container">\n']
    if h.get("note"):
        out.append(f'<p class="how-note">{h["note"]}</p>\n')
    out.append('<div class="guides">\n')
    for g in h["guides"]:
        steps = "\n".join(f'<li><span>{s}</span></li>' for s in g["steps"])
        shots = ""
        if g["shots"]:
            shots = '<ul class="shots">\n' + "\n".join(f'<li>{shot(n, alt, cap)}</li>' for n, alt, cap in g["shots"]) + '\n</ul>\n'
        tip = f'<p class="tip"><strong>{h.get("good", "")}</strong> {g["tip"]}</p>\n' if g.get("tip") else ""
        out.append(f'''<details class="guide" id="{g["id"]}">
<summary>{g["title"]}</summary>
<div class="guide__body">
<p class="intro">{g["intro"]}</p>
<ol class="steps">
{steps}
</ol>
{shots}{tip}</div>
</details>
''')
    out.append('</div>\n</div>\n</main>\n')
    return "".join(out)


def support(lang):
    T = content(lang).T
    s = T["support"]
    fmt = dict(privacy=path(lang, "privacy"), howto=path(lang, "how-to"))
    faq = "\n".join(f'<h3>{q}</h3>\n<p>{a.format(**fmt) if "{" in a else a}</p>' for q, a in s["faq"])
    see = s["see_also"].format(**fmt)
    return f'''<main id="content">
{page_head(s["h1"], s["lead"])}<div class="container">
<div class="prose">
<h2>{s["h2"]}</h2>
{faq}
<p>{see}</p>
</div>
</div>
</main>
'''


def legal(lang, page):
    m = content(lang)
    T = m.T
    ui = T["ui"]
    h1, lead, body = (m.PRIVACY_H1, m.PRIVACY_LEAD, m.PRIVACY) if page == "privacy" else (m.TERMS_H1, m.TERMS_LEAD, m.TERMS)
    body = body.replace("{privacy}", path(lang, "privacy"))
    note = f'<p class="updated">{ui["translation_note"]}</p>\n' if ui["translation_note"] else ""
    return f'''<main id="content">
{page_head(h1, lead, f'<p class="updated">{ui["updated"]}</p>\n' + note)}<div class="container">
<div class="prose">
{body}
</div>
</div>
</main>
'''


def write(rel, text):
    full = os.path.join(ROOT, rel.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)


def build():
    for lang in LANGS:
        T = content(lang).T
        for page in PAGES:
            title, desc = T["meta"][META_KEY[page]]
            body = {"home": home, "how-to": howto, "support": support}.get(page, lambda l, p=page: legal(l, p))(lang)
            rel = path(lang, page) + ("index.html")
            write(rel, head(lang, page, title, desc) + header(lang, page) + body + footer(lang))
    # 404: one file for the whole site, in English with a way to the other languages.
    T = content("en").T
    nf = T["notfound"]
    others = " · ".join(f'<a href="{path(l, "home")}" lang="{l}">{content(l).T["name"]}</a>' for l in LANGS if l != "en")
    body = f'''<main id="content">
{page_head(nf["h1"], nf["lead"])}<div class="container">
<p><a class="button" href="/">{nf["home"]}</a> <a class="button button--plain" href="/how-to/">{nf["howto"]}</a></p>
<p class="how-note">{others}</p>
</div>
</main>
'''
    h = head("en", "home", T["meta"]["notfound"][0], "", noindex=True)
    h = h.replace(f'<link rel="canonical" href="{BASE}/">\n', "")
    import re
    h = re.sub(r'<link rel="alternate"[^\n]*\n', "", h)
    h = re.sub(r'<meta property="og:[^\n]*\n', "", h)
    h = h.replace('<meta name="description" content="">\n', "").replace('<meta name="twitter:card" content="summary_large_image">\n', "")
    write("/404.html", h + header("en", "404") + body + footer("en"))
    # Sitemap with the language alternates.
    urls = []
    for page in PAGES:
        for lang in LANGS:
            alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{BASE + path(l, page)}"/>' for l in LANGS)
            alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{BASE + path("en", page)}"/>'
            urls.append(f"  <url><loc>{BASE + path(lang, page)}</loc><lastmod>2026-10-09</lastmod>{alts}</url>")
    write("/sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n")
    print("built", len(PAGES) * len(LANGS), "pages and the 404")


if __name__ == "__main__":
    build()
