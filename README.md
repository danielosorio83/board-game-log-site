# Board Game Log: website

The site of the Board Game Log app, <https://boardgamelog.app>. Plain HTML and CSS, no build step, no tracking, no third-party requests (the fonts are served from here). GitHub Pages publishes the `master` branch.

## Layout

```
index.html              Home
how-to/index.html       How-to videos
support/index.html      Support and common questions
privacy/index.html      Privacy policy
terms/index.html        Terms of use, with the note on game names and trademarks
404.html                Page not found
privacy.html, support.html, terms.html
                        Old addresses: they send the visitor to the new page (the app and
                        the App Store listing of version 1 point to them). Do not delete.
CNAME                   The custom domain
robots.txt, sitemap.xml Search engines
assets/
  css/                  tokens.css (colors, type, space) → base.css → layout.css → components.css
    pages/              home.css, content.css (one per kind of page)
  fonts/                Bricolage Grotesque and Figtree, woff2 subsets, and their licenses
  img/                  Logo, favicons, touch icon, social preview, hexagon pattern
  video/                How-to videos (self-hosted ones; the page can embed YouTube instead)
```

Every address is absolute from the root (`/assets/...`), so the site is meant to be served at the root of its domain.

## Working on it

Preview: `python3 -m http.server 8000` in this folder, then open <http://localhost:8000>.

- **Colors and type** live in `assets/css/tokens.css`, the same palette as the app ("Brick and cream" by day, "Night table" by night, chosen by the visitor's system).
- **Header and footer** are repeated in each page (no templating): change them in every `index.html`.
- **A new page**: copy `support/index.html` to `<name>/index.html`, change the `<title>`, description, canonical and Open Graph tags, and add it to `sitemap.xml` and to the footer.
- **A video**: replace the `.soon` block of its card in `how-to/index.html` with the YouTube `<iframe>` (the comment above it has the line to paste).
- **The copyright line** is in each footer (`© 2026 Board Game Log`); the trademark note is in the footers, on the home and in `terms/`.
- **Images**: `assets/img/og-image.png` is 1200×630; the logo is the app icon without its margin.

## Names

Game names shown in the app belong to their owners; the site and the app say so (see `terms/#game-names`). Contact: <support@boardgamelog.app>.
