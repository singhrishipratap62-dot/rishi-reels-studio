# Design system: Rishi v2

> Defaults, not rules: tokens approved on roughcut_v3. Per-video brand needs (a product's colours, a guest's logo) can extend them.

## 1. Canvas
| Item | Value | Tag |
|---|---|---|
| Format | 1080×1920, 30 fps, H.264 MP4. **Every export is 1080p** | [R] |
| Safe zone (captions, key text) | x 120–960, y 250–1600; keep the right icon column clear below y 1130 | [ME] |
| Footage | lav-mic talking head, marble wall, natural grade | [S] |

## 2. Colour
| Token | Hex | Use | Tag |
|---|---|---|---|
| `ice` | `#EAF0F8` + grain 0.8 | light graphic grounds (chat scene, split pane) | [RES] |
| `ink` | `#0B1224` | dark grounds (rare), deep text | [RES] |
| `ink.text` | `#0B1730` | text on light grounds, captions in light modes | [RES] |
| `muted.light` / `muted.dark` | `#4A5878` / `#9AA8C7` | support text on light / on dark | [RES] |
| `accent` | `#3E7BFA` | ticks, progress fill, send button, PiP glow tint, caret | [RES] |
| `card.dark` | `#121C38` | dark repo cards / chips | [RES] |
| `card.white` | gradient `#FFFFFF → #E4E6EA` + radial vignette (edges ≈7 % black) | **every white card/screen**. Grey-scale only, never blue-tinted | [R] |
| `board` | gradient `#F4F5F7 → #E2E4E8` + grain 0.6 | PiP-scene background | [S] |
| `wall.bg` | `#0D0E12` | slop wall gaps | [S] |
| `slop.tile` | gradient `#FFFFFF → #C8CCD2` (angle varies) + slowly breathing white sweep | wall tiles | [R] |
| `green` | `#2FD08A` | "sent ✓" state only | [S] |
| `teal` | `#2FB58A` | "● awake" status dot/text | [S] |
| `highlighter` | `#FFD68A` | prompt highlight swipe | [DP] |
| `row.highlight` | `#E3F6EE` | ticked rows | [S] |
| Claude orange | `#D97757` | only via the real Claude logo | [S] |
| Blob | gradient `#5D8BFF → #0839B0` + grain 1.0 + halo `rgba(62,123,250,.22)` blur 55 | painted organic figure | [R] |
- A-roll: natural grade + a bottom caption gradient (transparent → 45 % black over the bottom 40 %).
- B&W beat: saturation −100 via an adjustment layer, eased back over ≈0.45 s.

## 3. Typography
| Role | Face | Size | Tag |
|---|---|---|---|
| Caption hero | Playfair Display **Bold Italic**, lowercase | 132 px (A-roll), 100–110 (light grounds), ≤740 px wide | [ME][R] |
| Caption support | Inter Medium | 48 px (A-roll), 40–44 (light grounds) | [ME][R] |
| Single-line / one-word captions | Playfair Display Bold Italic | 54–78 px (auto-fit) | [R] |
| UI text in mock-ups | Inter Regular/SemiBold | 26–44 px | [S] |
| Card titles | Inter SemiBold | 32–42 px | [S] |
| Wall tile word | Inter Bold | 76 px, grey `#6B7079` + soft white shadow | [R] |
| Big numbers / % | Inter Bold | 34–38 px | [S] |
- Fonts are fontsource **latin** TTFs, so the glyphs ✓ ↑ ● are missing: draw ticks, arrows and dots as shapes.

## 4. Shape and depth
| Item | Value | Tag |
|---|---|---|
| Card radius | 22–36 px (chat card 36, PiP card 28, doc 22, timeline 14) | [R] |
| Tile radius | ≈8 px (wall); your tile's video corner radius 0.035 | [R] |
| PiP | rounded mask radius 100 (frame space) + white border (radius 36) + glow `rgba(140,157,255,.9)` blur 30 | [R] |
| Card shadow | `0 14 30 rgba(11,18,36,.16)` | [S] |
| Logo disc | white circle 176 px + Claude logo 118 px + shadow `0 10 34 rgba(0,0,0,.38)` | [R] |
| Video card | white frame 14 px + live clip + shadow `0 12 34 rgba(0,0,0,.4)` | [R] |
| Grain | Tesseract grain: amount 0.6 (board) / 0.8 (ice) / 1.0 (dark, blob), size 1.6 | [ME] |

## 5. Layout grids (1080×1920)
| Scene | Geometry | Tag |
|---|---|---|
| Chat card | card x 70–1010, y 460–1600; header logo (150, 520); input box y 1080–1580; thumbnail 23.5 % at (250, 1325); result card 270×480 at (815, 830) | [S] |
| Split pane | ice pane height 940 from the top; face shifted down 460 px (full hair line just below the pane); captions hero baseline 330; content starts at y 380 | [R] |
| Behind-head card | x 90–990, y 250–710, behind head via matte | [R] |
| Wall | 3×4 tiles 300×533, gap 30, origin (60, 60); face = row 1, col 1 (2nd from top); caption tile = row 2, col 1 | [R] |
| PiP | PiP scale 32 % at (540, 1270); card x 110–970, y 250–870; single-line caption baseline 922 | [R] |
| Comments sheet | sheet top y 980; field y 1104–1188; keyboard from y 1220 to the bottom; caption baseline 935; face moved up 400 px, blur 24, dim 45 % | [R] |

## 6. v2.1 additions (Style Lab v1, 2026-11-09) `[R]`
### Grounds (all Keep; pick per video)
| Token | Value | Note |
|---|---|---|
| `ice` | as above | still good |
| `paper.warm` | `#F4F1EA` + grain 0.6 | editorial |
| `dots` | `#F1F3F7` + dots `#D6DBE3` (lighter than v1) on a 54 px grid, drift 1.5 %/s, **with the slow mesh light on top** | |
| `mesh` | `#F2F4F8` + two blurred light clouds (`#DCE5F7`, white) drifting on 6 s sines + grain | **his favourite ground** |
| `ink.spot` | `#0B1224` + drifting blue spotlight `rgba(62,123,250,.28)` + grain 1.0; card variants: dark card **or white card on ink** | rare, serious beats |
| ✗ blurred own frame | rejected | |
- **Coarse grain** (from the "zoom through a window" demo, Keep): grain about 3.3× coarser than the default, amount 0.8, behind every card scene. Start at Tesseract grain size ≈ 5.3 and calibrate on a 1080p test still against `<studio root>/03. Projects/Rishi Style v2/style_lab_v2/` tile "Coarse grain" before the first build.

### Accent palette (all Keep; Rishi names one per video)
| Token | Hex | Use |
|---|---|---|
| `accent` | `#3E7BFA` | as before (was the v2.0 default; superseded by D26: default is `accent.duo`) |
| `accent.duo` | `#3E7BFA` UI + `#FFD68A` emphasis only | leaning favourite |
| `accent.clay` | `#D97757` | Claude-topic reels |
| `accent.mono` | `#0B1730` | quiet / premium |
| `accent.jacket` | `#23704F` | matches the green jacket |
If he hasn't named one, use `accent.duo` and list it in the storyboard assumptions.

### Numbers
- Big numbers: **Inter Bold** (or Playfair roman). Never Playfair italic for digits. The word next to the number can be Playfair.
