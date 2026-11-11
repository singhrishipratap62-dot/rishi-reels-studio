# DESIGN_SYSTEM.md — Prompt-to-Reel v1.0 (source of truth)

Links: [[DESIGN_PHILOSOPHY]] · [[COMPONENT_LIBRARY]] · [[LAYOUT_LIBRARY]] · [[MOTION_LIBRARY]] · [[STYLE_DO_AND_DONT]] · [[QUALITY_CONTROL]]
Confidence tags: **C** confirmed · **S** strong inference · **E** estimated · **U** unknown.
All refs are 720×1280 H.264 @ 30 fps re-encodes (Instagram downloads); author masters were likely 1080×1920. Pixel values below are given at **1080×1920** (×1.5 of measured).

## 1. Canvas
| Token | Value | Conf |
|---|---|---|
| canvas | 1080×1920, 9:16, 30 fps | C (ratio/fps) |
| duration | 17–35 s (median ~23 s) | C |
| IG safe zone | top 220 px, bottom 340 px, right 140 px kept free of key text | S |

## 2. Colour
| Token | HEX | Use | Conf |
|---|---|---|---|
| `bg.app` | `#1A1A16` | Family A app background (warm near-black) | C measured |
| `bg.app-deep` | `#0C0C10` | CTA / end-card backgrounds, card interiors | C measured |
| `surface.input` | `#21211C` | composer, reply bar, autocomplete row | C measured |
| `surface.raised` | `#3C3C40` | keyboard keys, toggle pill active | C measured |
| `surface.accent-tint` | `#2A2018` | autocomplete chip bg (accent at ~12% on bg) | C measured (≈#282014) |
| `text.primary` | `#F2F0EA` | headlines, UI text | E |
| `text.secondary` | `#8A8780` | "Chat", hints, placeholders | E |
| `accent.terracotta` | `#D4704C` | Claude asterisk, slash text, send button, CTA word, CTA pill | C measured |
| `accent.terracotta-deep` | `#CC6834` | CTA pill fill (R06) | C measured |
| `accent.yellow` | `#F4E474` | Family B keyword highlight ("effects?", "scatter") | C measured |
| `accent.red-badge` | `#C06C20`→`#E04A3A` | Family B counter badge "01/24" | E |
| `light.paper` | `#E6E8DC` | light-mode cards/explainer pages (R04) | C measured |
| `selection.blue` | `#4C7DF0` | keyword selection box + handles in captions | E |

Rules: chrome = neutrals + terracotta only (C). Content inside cards may use any palette (green cutting mat, blue map, red sun) (C). Max one accent per UI element.

## 3. Typography
| Role | Family (suggested) | Weight | Size @1080 | Tracking | Case | Conf |
|---|---|---|---|---|---|---|
| Display / CTA | SF Pro Display / **Inter Display** | 700–800 | 120–150 (CTA word) / 60–70 (CTA line) | −2% | Title / UPPER for keyword | S (family E) |
| Headline (B) | Inter / SF Pro Rounded-ish | 800 | 64–80 | −3% | lowercase | S |
| Caption word | Inter | 700 | 50–60 | −1% | lowercase | C style |
| Italic flavour | **Instrument Serif Italic** or Playfair Display Italic (condensed serif italic) | 400 | = sans size ×1.05 | 0 | lowercase | S (family E) |
| UI body | SF Pro Text / Inter | 500 | 30–34 | 0 | Sentence | S |
| UI meta | SF Pro Text | 400 | 22–24 | 0 | sentence | S |
| Mono (tags, receipts, file names) | JetBrains Mono / SF Mono | 500 | 22–28 | 0 | lowercase | S |
| Numbers (views, stats) | Inter tabular | 800 | 60–200 | −2% | — | C style |

Hierarchy pattern (C): **bold sans line** + **italic serif sub-line** stacked, centred, e.g. "laptop battery explainer / *with Claude Code*".
Keyword emphasis (C): (a) A — the active word gets a 2 px blue selection box with corner handles (Figma-selection look); unspoken words at 45% opacity. (b) B — keyword in yellow, ~1.4× size.

## 4. Spacing & shape
| Token | Value | Conf |
|---|---|---|
| base unit | 8 px | S |
| side margin (output card) | 102 px (card = 81% width) | C measured (68/720) |
| app side margin | 48 px | E |
| radius.card | 36 px | E |
| radius.pill | 999 px | C |
| radius.key | 14 px | E |
| radius.chip | 24 px | E |
| card shadow | 0 30 80 rgba(0,0,0,.55) | E |
| glass | bg white 10–14%, blur 24 px, 1 px border white 18% | S (R03, R05) |
| stroke.sticker | 10–12 px white outline around cut-outs | C (R05, R02) |

## 5. Texture
Clean digital — no grain on chrome (C). Content may carry its own texture (paper, ink-wash, dot-matrix). Talking-head footage: warm practical lighting, shallow DOF (C).

## 6. Motion tokens (detail in [[MOTION_LIBRARY]])
| Token | Value | Conf |
|---|---|---|
| beat | ~1.0 s per visual change (B), 4–5 s per demo (A) | C |
| ease.ui | cubic-bezier(.2,.8,.2,1) (iOS spring-like) | E |
| dur.micro | 150–250 ms | E |
| dur.reveal | 400–600 ms | E |
| type speed | ~12–15 chars/s with key-pop | E |
| counter roll | 1.5–2.5 s, odometer blur on digits | C (visible blur) |

## 7. Brand marks
Terracotta 8–12-ray asterisk (Claude-style spark) — used as status bullet, app greeting, CTA crown. C.
