# boardgamelog.app

The website of Board Game Log: a static site served by GitHub Pages from `master`, with the domain in `CNAME`. English is at the root, Spanish under `/es/` and French under `/fr/`.

## Editing

The pages are generated. Change the text in `build/content_en.py` (the source), then the same keys in `content_es.py` and `content_fr.py`, and run:

```
python3 build/build.py
```

It rewrites every page (`index.html`, `how-to/`, `support/`, `privacy/`, `terms/` in each language), `404.html` and `sitemap.xml`. Do not edit the generated HTML by hand. The layout (header, footer, language links, theme button, hreflang tags) lives in `build/build.py`.

## Layout

- `assets/css/` tokens (colors and type, light and dark), base, layout, components, and one file per kind of page (`pages/home.css`, `pages/content.css`).
- `assets/js/site.js` the theme button and the guides that open from a link. The site works without it.
- `assets/img/app/{light,dark}/` screenshots of the app, one per theme (webp, 540 px wide). They use made-up games and players and no game from the catalog.
- `assets/fonts/` self-hosted Bricolage Grotesque and Figtree (SIL Open Font License).

## Theme

The site follows the phone's light or dark setting. The button in the header lets the visitor choose, and the choice is kept in the browser (`localStorage`, key `theme`). `data-theme="light|dark"` on `<html>` overrides the system setting.

## Screenshots

They come from the app's UI test `HowToScreenshotsTests` (in the app repository), run once in light and once in dark (`xcrun simctl ui booted appearance light|dark`) on an iPhone 17 simulator with a clean status bar (`xcrun simctl status_bar booted override --time 9:41 ...`). Convert with `cwebp -q 82 -resize 540 0 in.png -o out.webp`.

## Checks before publishing

No game names anywhere (not the catalog's, not the built-in one), links and anchors that resolve, no horizontal overflow at 320 and 390 px, tap targets of at least 44 px.
