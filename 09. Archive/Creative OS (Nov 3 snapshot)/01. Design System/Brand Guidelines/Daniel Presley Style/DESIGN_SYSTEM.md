# DESIGN SYSTEM — Daniel Priestley Editing Style (v1.0)

Evidence tags: `[OBS]` seen (video mm:ss) · `[EST]` measured/estimated by Claude · `[INF]` interpretation · `[R#.#]` Rishi rule (outranks all).

## 1. Philosophy
- **"The teacher's notebook, produced like a documentary."** [INF] A calm desk-side talking head is the spine; every idea he names gets *made visible* on paper-like cream cards, a real whiteboard, or a framed piece of evidence (clip, screenshot, photo).
- **Editorial, not hype.** Cream paper, a high-contrast serif, one blue, one crimson, soft shadows. No running captions, no emoji, no shaking zooms. [OBS all 28]
- **Proof over decoration.** Graphics either *structure* the idea (numbered chapters, lists, diagrams) or *prove* it (name-tagged people, headlines, screenshots, stats). [INF from scene census]
- **Two-colour logic.** Blue = the idea/answer/positive; crimson = the number/label/warning/problem. [OBS R01 00:01 "Price Taker/Maker", R24 01:33, R16 05:33; INF]

## 2. Canvas
| Format | Size | Safe area | Notes |
|---|---|---|---|
| 16:9 YouTube | 1920×1080, 25 fps (his) — use 30 fps per workspace default | 5% margin (x 96–1824, y 54–1026) | All 28 refs 1920×1080; 25 fps except R01/R27/R28 at 29.97 [OBS ffprobe] |
| 9:16 Reels | 1080×1920, 30 fps | x 120–960, y 250–1600; right icon column clear `[R1.0]` | Adaptation rules in §8 [INF] |

## 3. Colour tokens
### 3a. Live palette — gradnext mapping (use these) `[R1.0]`
Source: Rishi's gradnext Design System artifact (https://claude.ai/artifact/K1E2SSh8kvivtni26rYTQ2, `tokens.json`), found after Stage 0. Each Priestley **role** (3b) is carried by the gradnext colour that plays the same job. Mapping is `[INF]` — Rishi to approve.

| Style token | gradnext token | Hex | Replaces Priestley role |
|---|---|---|---|
| `--paper` | `white` / `background-03` (white → periwinkle-100 foot) | `#FFFFFF` → `#DEE3FF` | Cream paper cards (chapter, quote, name card) |
| `--paper-tint` | `periwinkle-100` | `#DEE3FF` | Ghost quote marks, card tints, `--mist` scenes |
| `--ink` | `rhino` | `#2E3558` | Serif headlines, sans headers, name card ink |
| `--ink-body` | `rangoon-black` | `#1A1A1A` | Long body text |
| `--ink-soft` | `neutral-500` | `#808080` | Grey role lines (24px+ only) |
| `--blue` (idea / answer) | `rhino-600` (text, fills) · `rhino-500` (bold keywords) | `#363EA7` · `#5961ED` | Quote text + mark, chips, bullets, "Priestley" |
| `--crimson` (number / label / problem) | `chrome-yellow` as **fill** with `rhino` text (never yellow text on white) | `#FFA601` | Chapter numeral tile, pills, "Principle N", problem side |
| `--highlighter` | `chrome-yellow-200` | `#FFD68A` | Highlighter swipe |
| `--glow` | `periwinkle` (`glow-periwinkle`) | `#8C9DFF` | PiP outer glow, whiteboard glow trace |
| `--charcoal` | `midnight` / `rhino-950` | `#0D1028` / `#1B1F38` | Name-sting band, iris background |
| `--neon` | `chrome-yellow` glow on `midnight` | `#FFA601` | Neon stat text |

Notes: gradnext's own README forbids drop shadows except the periwinkle under-glow. Priestley's soft shadows are part of the copied style ("core fixed"), so they're kept **subtle**, and Rishi should confirm this conflict. Wordmark/logo rules from gradnext apply whenever the gradnext logo appears.

### 3b. Priestley reference palette (measured; reference only)
Measured by PIL pixel medians [EST] unless noted. Kept so roles can be re-mapped later.

| Token | Value (placeholder) | Role | Evidence |
|---|---|---|---|
| `--paper` | `#F4F1E4` | Cream card / chapter / quote / name-card background | #F6F2E5 (R22 00:50), #F5F3E6 (R24 00:48), #F3F1E2 (R24 00:46) [EST] |
| `--paper-ghost` | `#E6E1D3` | Giant ghost quote-mark watermark on paper | agent estimate R08–R15 [EST] |
| `--mist` | `#F5FAFB` | Cool white for chip / pill-stack / UI scenes | R24 01:40, R16 05:59 [EST] |
| `--mist-2` | `#DCE6F0` | Pale blue-grey behind framed clips & screenshots | R03 08:25, R04 00:15 [EST, agent] |
| `--white` | `#FFFFFF` | Whiteboard surround, tiles, pills | R22 00:53 [EST] |
| `--ink` | `#111111` (titles) / `#2F2F2D` (name card) | Serif headlines, sans headers | R24 01:40 #020305; R24 00:46 #2F2F2D [EST] |
| `--ink-soft` | `#8A8A8A` | Grey role lines, book body text | [EST, agent] |
| `--blue` | `#2155A9` | Primary accent: quote text & mark, chips, bullets, "Priestley" | #2155A9 (R22 00:50), #2553A4 text, #2C5CA9 chips (R24) [EST] |
| `--blue-deep` | `#1F4A99` | Blue letters in name card | R24 00:46 [EST] |
| `--crimson` | `#A52D40` | Chapter numerals, "Principle N", name-card red | #A52D40 (R24 00:48), #982133 (R24 00:46) [EST] |
| `--red` | `#C71338` | Filled pills / boxes (brighter red) | R16 05:59 [EST] |
| `--neon-red` | `#FF2A3A` + bloom | Loss/negative stat glow text on black | R24 02:24 (#C72436 core, glow brighter) [EST] |
| `--glow` | `#A9C2F5` @ ~40% | PiP outer glow | [EST, 3 agents: #8FB0F0–#BFD3FF] |
| `--highlighter` | `#F2C200` | Yellow highlighter swipe on diagrams/screens | R18 01:17, R14 00:06 [EST] |
| `--gold` | `#C9A54E` | Rare third data colour (bars/dots) | R01 05:36 [EST] — optional |
| `--charcoal` | `#1E1E1E` | Name-sting black band, iris background | R01 01:00 [OBS] |

Contrast rules [OBS]: text on `--paper`/`--mist` is `--ink` or `--blue`; text on `--blue`/`--red` fills is white; text over footage is white with soft dark glow.

## 4. Typography
Fonts `[R1.0]`: **Playfair Display** (serif) + **Inter** (sans). Handwriting accent: **Caveat** [INF — Rishi to confirm; refs use a marker-style hand].

His originals (reference only): high-contrast display serif, Canela/Tiempos/Didone-like; neutral grotesk sans (Inter/SF/Söhne-like, tight tracking); casual marker hand (Caveat/Kalam-like). Names not confirmed. [EST]

| Role | Font | Weight | 16:9 size (px, ≈% of H) | 9:16 size (px) | Case | Evidence |
|---|---|---|---|---|---|---|
| Name card (signature) | Playfair Display | 600 | 2 lines, cap ~150 px (≈20–22% H per line) | 150 | Title | R01 01:01, R24 00:46 [EST] |
| Giant single word | Playfair Display | 600 | ~200 px (≈20%) | 180 | Title | R28 03:55 "CAOS" [EST] |
| Kinetic title over A-roll | Playfair Display | 500 | 90–160 px (8–15%) | 110–130 | Title Case, 1–5 words | R22 00:06, R18 00:02, R14 00:58 [OBS] |
| Chapter title | Playfair Display | 500 | ~100 px (≈9–10%) | 96 | Title, 1–8 words | R16 00:47, R24 00:48 [EST] |
| Card heading (beside PiP) | Playfair Display | 500 | ~65 px (≈6–7%) | 64 | Title | R05 09:01, R22 00:21 [EST] |
| Sans header (chip/pill scenes) | Inter | 700, tracking −2% | ~55 px (≈5%) | 56 | Sentence | R24 01:40 [EST] |
| Quote body | Inter | 400 + **700 keywords** | ~45 px (≈4–4.5%) | 52 | Sentence, 10–25 words | R22 00:50, R05 09:05 [EST] |
| Bullets | Inter | 400, blue, "- " lead | ~38 px (≈3.5%) | 44 | Sentence, 3–8 words | R05 09:01 [EST] |
| Pill / chip label | Playfair Display | 500, white | ~40 px | 44 | Title, 1–3 words | R24 01:40, R16 05:59 [OBS] |
| Name-tag name / role | Inter | 700 / 400 grey | 26 / 18 px | 32 / 22 | Name / "Role, Company" | R18 00:03 [EST] |
| Lower-third name super (no box) | Playfair 500 + Inter 400 | ~95 px / 30 px | 90 / 32 | Name / role | R26 00:46, R01 26:43 [EST] |
| Chapter numeral | Inter | 700, `--crimson` | ~70 px in 120 px tile | 80 | Digit | R24 00:48 [EST] |
| Attribution | Playfair Display Italic | 400 | ~30 px | 34 | "– Name, Role" | R17 03:47, R28 03:14 [OBS] |
| Annotation | Caveat | 600 | 30–50 px | 40–56 | Sentence, 2–6 words | R20 01:15, R03 00:06 [OBS] |

Emphasis toolkit (pick one per element) [OBS]: bold weight in same colour (quotes) · crimson single letter/word · hand-drawn crimson ellipse · yellow highlighter swipe · blue underline · hand-drawn arrow.

## 5. Shape, depth, texture
- **Radii** [EST]: rounded cards ~3–4% of frame width (≈60–70 px at 1920); PiP ~6% of PiP width (≈30 px); number tile ~22% of tile (≈26 px on 120 px); chips ~25% of height; white name pill fully round.
- **Shadows** [OBS]: soft, low, warm-neutral. Name-card text has a long soft drop shadow down-right (~12 px offset, ~18 px blur, 30% black). Tiles/pills: 0 6px 18px rgba(0,0,0,.12).
- **PiP glow** [OBS]: thin 2 px white/light-blue stroke + `--glow` outer glow ~24–30 px blur.
- **Paper texture** [OBS]: faint grain/speckle on `--paper`; ghost quote marks as watermark; faint large grey rectangles behind quote text (R22 00:50).
- **Footage treatment behind titles** [OBS R22 00:06]: background desaturated + cooled, faint drifting particles, title has soft white glow.

## 6. Layout grid (16:9)
- **PiP layout** [EST from R05 09:01, R22 00:53, R18 01:29]: content card x 3–74%, y 5–95%; PiP x 76–97%, y 10–90% (≈25–27% W × 75–85% H).
- **Chapter card** [EST R24 00:48]: tile centred at y≈20%; title centred at y≈45–55%.
- **Quote card** [EST R22 00:50]: mark top-left at x≈9%, y≈45–65%; text block x 9–90%, y 70–97% when panel wipes up; full-screen variant text y 30–60%.
- **Name pill** [EST R18 00:03]: bottom-left x≈3%, y≈88% centre; ~17–30% W × 8–9% H.
- **Kinetic title** [OBS]: either huge across the top, behind the subject (R22) or lower third, centred/left with dark bottom gradient (R02, R18).
- **Chips** [EST R24 01:40]: header y≈15%; chip row y≈27%, left-aligned from x≈4%, gap ~1% W.

## 7. Components (build list)
`NameSting` · `NameCard` · `ChapterWipe` (arc + tile) · `ChapterCard` · `KineticTitle` (over A-roll; behind-subject variant) · `NamePill` (person/brand/product/"Example N") · `LowerThirdSuper` (no box) · `QuoteCard` (full / panel-up / centred) · `ListPiP` · `WhiteboardPiP` · `BrollCardPiP` · `ChipRow` (blue) · `PillStack` (red) · `IconTitleCard` · `PrincipleCard` · `DiagramCard` (handwritten + icons) · `FramedScreen` (screenshot/UI/clip on `--mist-2`) · `PhoneMockup` · `IrisSpotlight` (+ neon stat) · `HeadlineOverBroll` · `DataViz` (bars/pie/progress/grid) · `PhotoCollage` · `LightLeak` transition.

## 8. 9:16 adaptation rules [INF — not in refs; Rishi to approve]
1. A-roll: centre-crop to 9:16 on the face; kinetic titles go **above the head** (y 300–600) instead of lower third.
2. PiP layouts become **stacked**: content card top (y 250–1050, x 120–960 safe), PiP bottom (y 1100–1600, rounded, same glow).
3. Full-screen cards (chapter, quote, name card, chips) re-flow vertically; text widths max 840 px (x 120–960).
4. Name pills move to y≈1450, left-aligned at x 120.
5. Nothing important right of x 960 or below y 1600.

## 9. Core / optional / experimental
- **Core** (seen in most of 28 or structural): talking-head spine; name sting → name card in intro (≥24/28 [OBS]); curved cream arc wipe + numbered tile chapters (≥25/28); quote card with ghost marks + blue mark (≥22/28); PiP with blue glow (whiteboard / list / B-roll) (all 28); white name pills (≥20/28); fast proof montage in first 30 s (all); no running captions (27/28); calm ending (all).
- **Optional**: kinetic serif title over A-roll; red pill stack / blue chips; icon title cards; framed screenshots/UI; phone mockups; iris spotlight + neon stat; lower-third super; diagram cards; data viz; principle (book-page) cards; film/TV clips.
- **Experimental** (1–3 videos): light leak & glitch (R22 only), red-blotted face collage (R03), 3D clay props (R01, R03, R04), winding-road timeline (R02), AI corkboard / scrapbook (R08, R10), tinted shape masks (R20), stutter AI stills (R10).
