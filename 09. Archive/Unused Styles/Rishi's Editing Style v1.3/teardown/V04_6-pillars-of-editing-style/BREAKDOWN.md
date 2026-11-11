# V04 teardown — "The 6 pillars behind my editing style"
720x1280 @30fps, 1601 frames (#0-#1600, 53.4 s). Coordinates: x%/y% of frame and px in 1080x1920 (= src x1.5). Frame #N = N/30 s. Durations: ms = (end_f − start_f)·1000/30, end_f = first frame at rest (QUALITY_NOTES Q1).
Rules applied: Q3 fit gate (rmse ≤ .05 bezier [MEAS]; .05-.12 named/≈ [MEAS]; > .12 family only [EST]); Q5 sheet timings written "~s [EST]"; Q10 no sound named as fact.

## 1. Overview
- Hook: "This editing style took me more than two years to build. Here are the six pillars behind it." (0-5 s). Topic: six components of the creator's style, each demonstrated by the reel's own graphics. CTA: comment "Style" to get the tutorial (49-53.4 s). [OBS]
- Structure: HOOK #0-149 (0-5 s, footage shrinks to a card carousel + 6-diamond tracker) → PILLARS 1-6 #150-1389 (5-46.3 s, ≈ 7 s each: numbered diamond title → glass panel demonstrating the pillar) → OUTRO #1390-1445 (46.3-48.2 s, plain captions) → CTA card #1446-1600 (48.2-53.4 s). [OBS]
- Runtime share [EST from timeline rows]: full-frame A-roll with only small overlays (title/captions) ≈ 20 s (37%); A-roll + glass UI panel at chest ≈ 27 s (51%); light-grey carousel scene ≈ 5 s (9%); CTA card over A-roll ≈ 5 s (… counted in A-roll+panel). Never a full-frame graphic scene after #150.
- Shots: 1 hard cut (#150, diff 130.2); everything after is continuous footage with overlays. Avg shot length 26.7 s over 2 shots (events.md) — the real edit rate is panel/title swaps ≈ every 3.5 s [EST].
- Distinct animations catalogued: 18 in animations.json (V04-A01…A18) + A19 (glow breathing, [INF] only, not in json); 11 tracks fitted (T1-T11), 9 usable.
- Look: dark blue studio A-roll (plant left, chair, black tee, RØDE boom), one accent: electric-blue glow. Every graphic is a dark translucent "glass" panel with a bright blue border over the chest or a blue diamond number badge. Intro carousel is light grey-blue (#C9D1D6).

## 2. Beat-by-beat timeline
| frames | time | words | screen layers back→front | anim | camera | audio onset (MEAS) | WHY |
|---|---|---|---|---|---|---|---|
| 0-5 | 0.00-0.17 | This editing | A-roll full frame, no graphics | — | static | — | instant face |
| 6-149 | 0.20-4.97 | style took me more than two years to build. Here are the six pillars | footage shrinks (#8-70) into a glowing portrait card with dashed inner frame + purple thumbnail, on a light carousel of dim side cards; caption "more than two years to build" above; row of 6 diamonds appears under | A01,A02,A03,A04 | card centred x50%, y≈55%→50% | 1.83 s (attack 366 ms, centroid 2672 Hz) | video-in-video = "my edit is the thing studied"; 6 diamonds = counted promise |
| 150-204 | 5.00-6.80 | The first pillar is the cinematic | hard cut to A-roll (wider, plant/chair); blue diamond "1" grows at x≈18-20%, y≈59% (#150-172) then title "Cinematic Text" reveals right of it | A05,A06,A07 | cut | — (no onset within 100 ms of cut) | chapter marker introduces pillar |
| 205-403 | 6.83-13.43 | text. We use a modern sans font called Coolvetica… script font called Edwardian script | glass panel (69% W) rises at chest; specimen lines "If you look at your Edits that look…" in white sans + script "Edits"; two leader-line labels "Sans Font Coolvetica" / "Edwardian Script" | A08,A09 | static | 8.27, 10.05 s | the font names are shown as the specimen, not just spoken |
| 404-464 | 13.47-15.47 | The second pillar is the hook animations | panel dissolves (#390-403, ~13 s); diamond "2" + "Hook Animations" | A06,A07 | static | — | pillar 2 title |
| 465-620 | 15.50-20.67 | We create a five-star outline animation using the shape tool, then add a glow to make them pop | new panel: five outlined stars fill gold one by one; checklist bullets "Create 5-stars using shape tool" / "Add a glow to make it pop" | A10 | static | 16.67 s, 18.62, 20.29-20.81 s | demo of the recipe itself |
| 621-668 | 20.70-22.27 | The third pillar is the listicles | panel exits; diamond "3" + "The Listicles" | A06,A07 | static | — | pillar 3 title |
| 669-860 | 22.30-28.67 | three points using a UI made up of a rounded square, white stroke, and a number, animated with a pop | panel: three numbered diamonds (1,2,3) pop in; caption "these three things … animated with a pop"; leader label "Rounded square, white stroke and a number" | A11 | static | 25.57, 26.45, 27.21 s | the thing described is shown being built |
| 861-1062 | 28.70-35.40 | The fourth pillar is chapter animations… reuse the listicle style, stroke title, subheader | badge "4" slides left & settles (#868-895) + "Chapter Animations"; small diamond expands into panel with "2 / design" + bullets "Reuse the Listicles style", "Add subheader for the chapters" | A06,A07,A12 | static | 29.02, 33.13 s | shows chapters re-using listicle diamond |
| 1063-1111 | 35.43-37.03 | The fifth pillar is the UI animations | diamond "5" + "UI Animations" | A06,A07 | static | 35.34, 35.74 s | pillar 5 title |
| 1112-1256 | 37.07-41.87 | We take a UI like Figma and using a 3D camera we walk the viewer through | white tall UI panel rises (#1112-1150) with blue edge glow; content pans/blurs; fades #1236-1256 | A13 | static | 37.55 s, 38.78 s | UI-in-UI demonstration |
| 1257-1311 | 41.90-43.70 | The sixth pillar is the visual animation | diamond "6" + "Visual Animation" | A06,A07 | static | — | pillar 6 title |
| 1312-1389 | 43.73-46.30 | Like this stable animation showcasing different effects | glass panel with effect-list rows (Vignettes, Blur, Chromatics, Noise…), cyan/purple highlight bars; caption "Showcasing different effects" | A14 | static | 43.93 s | live specimen |
| 1390-1445 | 46.33-48.17 | If you wanna learn how I edited this entire | A-roll only; bold white captions one word at a time ("If you want", "how I", "edited", "entire") | A17 | static | 46.65, 48.16 s | no graphics = attention on the ask |
| 1446-1600 | 48.20-53.40 | video, I created a full tutorial… Comment down the word style | YouTube card "Edit Like Me" rises from lower right to centre-low; caption "Style" in quotes | A15,A16,A17 | static | 51.32 s | tutorial card = destination for the comment |

## 3. Animation catalogue
Format: element · trigger · frames/ms · from→to · easing (rmse) · exit · rebuild. Tracks are work/T1-T11.csv (src px). Overshoot = peak/final (Q4).

**V04-A01 Footage→card shrink** — full footage becomes a portrait card (bh 1279→526 px src = 100%→41% H; 1919→789 px @1080). #8-70, 2067 ms; free fit ≈ bezier (0.5,0,0,1) rmse .089 (named easeOutSine rmse .174) → ≈, ease-in-out shape, no overshoot (peak/final 1.00) [MEAS T1]. Trigger: first words (start #8 = word 0 + 8 f; "style" word @#21). Exit: card holds, side cards fade in around it (A02). Rebuild: scale the video wrapper + border + glow `cubic-bezier(.5,0,0,1) 2.07s`.

**A02 Carousel side cards + dashed inner frame** — blue dashed rectangle fades in around chest (#6-8), purple thumbnail of the same footage grows inside it (#7-12, ≈ 5 f) [OBS strip_000]; side cards (dimmer clones of the footage, 3 per side) slide in from both edges #17-36 while the grey-blue ground (#C9D1D6 [MEAS f100]) replaces the footage frame; outer glow ≈ 12 px src (≈ 1.7% W) light blue [EST]. Not tracked (CSV absent) → [OBS] frame numbers from strip, [EST] radii. Rebuild: flex row of 7 cards, centre scale 1, sides scale .85 opacity .5, blue box-shadow.

**A03 Word-by-word grey→dark caption** — "more than two years to build", black-ish sans ≈1.9% cap height, y≈7% H (strip_000 #36-120 → y≈ 70-80 px@720 → in 1080 ≈ 130 px); words appear light-grey then darken; one word every ≈ 6-7 f (more #37, than #43, two #50 [OBS strip]) [OBS]; whole caption slides down ≈ 25 px as scene rises (strips #36-120) [OBS]. Trigger "build" @#78 vs last word at #~110 → caption leads speech late by ≈ 1 s (caption runs on its own timing) [INF]. Rebuild: spans with colour transition 6 f, stagger 6.5 f.

**A04 Six-diamond tracker build** — 6 blue diamond (rounded-square rotated 45°) badges numbered 1-6 in a row under the carousel (#120-135, 1 per ≈ 3 f stagger, the 5th-6th lighter "ghost" until #131) [OBS strip_004]; glow blue. Trigger "pillars" @#113 (+7 f). Position y≈ 42-48% of strip tile ≈ 66% H [EST]. Persists to #149 then hard cut. Rebuild: 6 inline-flex diamonds with pop 6 f stagger 3 f.

**A05 Hard cut carousel→A-roll** — #149→#150, diff 130.2 (hist-chi 1.16) [MEAS events.md]; no transition frames [OBS strip_004]; new footage framing is wider (head ≈ 62% of the carousel's, plant + chair visible). Audio: no onset within ±100 ms of the cut (hit rate 0/1) [MEAS audio.json].

**A06 Diamond number badge enter** — diamond (rounded square rotated 45°, light-blue fill ≈ #65AFD5 [MEAS mean 30 px f200; the saturated centre ≈ #1F8FE0 [EST]], white numeral, blue glow) at x≈18-20% W, y≈58-59% H. Pillar 1: scale small→full #150-168 (diamond grows ≈ 18 f) while luma 37→87 and cx 130→142 px src (x18.0→19.7%; 195→213 px @1080) [MEAS T2 #150-172, 733 ms; ease not fitted: only 3 CSV rows in range, [EST] ease-out]. Pillars 2-6: same pattern (sheets 13.5, 21.0, 29.0, 35.0, 42.0 s ~ [EST]). Trigger "first" @#153 (badge starts at #150, −3 f). Exit: fade with title ≈ 0.5 s [OBS]. Rebuild: scale(.2→1) rotate(45°) + opacity, 0.6 s.

**A07 Pillar title wipe** — white bold sans (≈2.5% H cap) to the right of the badge reveals left→right "Cinematic Text" / "Hook Animations" / "The Listicles" / "Chapter Animations" / "UI Animations" / "Visual Animation"; reveal ≈ 0.4 s, hold ≈ 1 s, fade ≈ 0.4 s (~ [EST], from 2 fps sheets). Trigger: pillar-ordinal word ("first" @#153; "second" @#404; "third" @#626; "fourth" @#874; "fifth" @#1063; "sixth" @#1257): title visible ≈ 3-15 f after the ordinal [EST]. Rebuild: clip-path inset(0 100% 0 0)→0 on text, 12 f.

**A08 Glass specimen panel rise** — dark glass rectangle (blue-violet fill, 1.5 px bright blue border, outer glow) centred on chest: width 499 px src = 69% W (748 px@1080). Track T4 #205-240: cy 876→795 px src (y 68.4%→62.1% H; 1314→1193 px@1080), bh 338→369, 1167 ms; free fit bez (0.4,1.4,0,1.1) rmse .222 → family only: ease-out with a small overshoot (peak/final 0.98 on cy) [EST gate]. Trigger "text" ≈ @#205 (+0). Exit: fades 13.0 s ≈ 0.5 s [OBS]. Contents: white sans + script specimen. Rebuild: translateY(80px→0) + opacity, spring-ish ease, glass = `background: rgba(20,30,90,.55); border:1.5px solid #2F80FF; box-shadow:0 0 14px rgba(47,128,255,.6); border-radius:≈3.5% W`. Radius % W [EST].

**A09 Leader-line callouts** — white 1 px line from label ("Sans Font / Coolvetica", "Edwardian Script") to the relevant text/mic; line draws ≈ 8 f, label fades in; appears each time the specimen line changes (7.3-13.0 s) [OBS sheets ~]. Rebuild: SVG line stroke-dashoffset 8 f, label opacity.

**A10 Five-star panel + checklist** — panel expands: bw 186→299 px (26%→42% W), bh 17→79 px, #496-545 (1633 ms), bez (0,1.4,0,0.9) rmse .039 (bw) / .033 (bh) → bezier [MEAS T5]; cx 423→354 (rmse .171, EST). Five outlined stars fill gold one per ≈ 0.3 s (16.0-17.5 s [EST]), then glow bloom (#585 "glow" +…) 18.5-20.5 s [OBS]; two checklist rows appear below the panel with a blue sparkle bullet (16.5 s and ≈19 s [EST]). Trigger "five-star" @#477 (T5 start #496, +19 f: panel grows after the phrase). Rebuild: scaleX/scaleY ease-out `cubic-bezier(0,1.4,0,.9) 1.6s`; star fill staggered 9 f.

**A11 Listicle diamonds pop** — panel height 130→259 px src (10%→20% H) over #669-715 (1533 ms), bez (0,1.4,0,0.9) rmse .040 → bezier [MEAS T6]; three diamonds (1,2,3) pop inside (≈ 0.3 s stagger [EST]) 22.5-23.5 s; leader label "Rounded square, white stroke and a number" appears #750-ish (25.0 s [EST]). Trigger "UI" @#719 (panel started #669, −50 f: panel leads speech by 1.7 s). Rebuild: same panel + 3 pop(scale .6→1, rotate 45°).

**A12 Chapter badge slide + small-diamond expand** — badge cx 211→154 px src (x29.3%→21.4%; 317→231 px@1080) over #868-895 (900 ms), bez (0.1,0.6,0.4,1.1) rmse .029 → bezier [MEAS T7] (easeOutQuart rmse .036). Trigger "fourth" @#874 (start #868, −6 f). Then 31.0-31.5 s a small glowing diamond expands into a panel containing "2 / design" ≈ [OBS sheet]. Rebuild: translateX with `cubic-bezier(.1,.6,.4,1.1) .9s`.

**A13 Figma-style UI panel** — white portrait UI card with blue edge glow rises: bh 174→545 px src (13.6%→42.6% H) over #1112-1150 (1267 ms), bez (0.1,1.4,0,0.9) rmse .067 → named easeOutExpo ≈ rmse .160 [MEAS T8: gate .05-.12 → named ≈]; cy 735→858 rmse .186 (EST). Content: UI thumbnails; panned/blurred while "3D camera" words play (39.3-41.4 s [EST]); panel dims to white then fades #1236-1256. Trigger "UI" @#1092 / "Figma" @#1149 (start #1112 = −37 f vs "Figma"); onset 37.55 s (#1126). Rebuild: scaleY from bottom, then CSS 3D rotateX/translateZ pan of inner image.

**A14 Effects-list panel** — glass panel with rows (names such as Vignettes / Blur / Chromatics / Noise) and a cyan→purple gradient highlight bar that moves down row by row (44.0-46.0 s [OBS]); panel grows bh 89→319 px (7%→25% H) over #1312-1385 (2433 ms), bez (0.2,1.4,0,0.9) rmse .081 → named ≈ easeOutExpo rmse .144 [MEAS T9]; cy 939→783 rmse .099 named ≈; cx 293→388 rmse .144 (EST). Trigger "visual" @#1286 / "stable" @#1327 (start #1312). Onset 43.93 s = #1318 (+6 f from start). Caption "Showcasing different effects" with sparkle bullet.

**A15 Tutorial card rise** — YouTube card ("Edit Like Me", yellow/white title on blue/orange thumb, view count line) from lower-right: bh 199→371 px (15.5%→29% H) over #1446-1480 (1133 ms), bez (0.2,1.4,0.2,1) rmse .050 → bezier [MEAS T10, peak/final 1.02 on bh]; cx 534→372 (x74%→52%), cy 1004→878 (y78%→69%), both rmse > .13 (EST ease-out w/ small overshoot). Trigger "tutorial" @#1480 (start #1446, −34 f: card enters ≈ 1.1 s before the word). Onset 48.16 s (#1445, ±1 f of start) [MEAS]. Rebuild: translate + scale spring `cubic-bezier(.2,1.4,.2,1) 1.13s`.

**A16 "Style" quote pop** — "Style" in straight quotes, bold white sans (≈2.7% H cap), above the card at y≈51% H: cx 304→363 px src (+59 px; 84 px→ x 42%→50%) over #1539-1555 (533 ms), fit rmse .290 → family only (ease-out with overshoot peak/final 1.12, [EST gate]) [T11]. Trigger "style" @#1561 (start #1539, −22 f: appears before spoken). Burst peak 15.3 at #1539-1541 = word swap [MEAS events]; onset 51.32 s (#1540).

**A17 Plain A-roll bold captions** — "If you want", "how I", "edited", "entire": white bold sans (≈2.6% H), centre-left at y≈66-70% H, one phrase at a time, hard-swap; no script, no glow [OBS sheets 46.5-48.0 s]. They appear only when no panel is on screen.

**A18 Panel dissolve** — panels fade+blur out over ≈ 0.5 s (13.0 s, 19.8-20.7 s, 28.7 s, 35.0 s [EST from sheets], not tracked).

**A19 Persistent glow breathing** — blue border glow of the panels/badges pulses subtly (≈ ±15% brightness, period ≈ 1.2 s) [INF; not measured]. Dropped from signature list.

## 4. Text & typography system
| style | font (conf.) | weight | cap %H | colour | use |
|---|---|---|---|---|---|
| Badge numeral | grotesque (SF/Inter-like, med) | Bold | ≈2.2 | #FFFFFF [OBS] | 1-6 in diamonds |
| Title | same | Bold | ≈2.5 | #FFFFFF | pillar names |
| Specimen sans | Coolvetica-like (as spoken [ASR: Coolvetic]) | Regular | ≈2 | #FFFFFF | demo text in panel |
| Specimen script | Edwardian Script-like (as spoken [ASR: Itwardian]) | Regular | ≈3.5 | #FFFFFF with blue glow | "Edits" |
| Carousel caption | grotesque | Medium | ≈1.9 | dark #2A3340 [EST] on #C9D1D6 | "more than two years to build" |
| Outro captions | grotesque | Bold | ≈2.6 | #FFFFFF | plain words |
| Bullets | grotesque | Regular | ≈1.1 | #D8E6FF [EST] | checklist rows |
Rule [INF]: titles/numerals = bold sans; the pillar's own typography is demonstrated in its true font; script appears only inside the panel as a specimen, not as a spoken-word emphasis device (unlike V01-V03). Captions are mostly absent because panels carry the text.

## 5. Colour, light & material
- Studio wall #323E49 → #102D4B (cool slate/teal, top-left lighter) [MEAS f200]; tee #050205 [MEAS]; carousel ground #C9D1D6 / #CBD4D9 [MEAS f100].
- Accent blue glow ≈ #2F80FF [EST], diamond highlight #65AFD5 [MEAS mean of 30 px]. Gold stars ≈ #F2C14E [EST].
- Glass panel: translucent blue-violet fill (≈ α .55), 1.5 px border blue, glow radius ≈ 14 px src (≈ 2% W) [EST — not measured; Q12 not satisfied for radius].
- A-roll grade: lifted shadows blue, skin warm, bottom crushed; same family as V02/V03.

## 6. Depth & 3D
Carousel: 7 cards, centre upright, sides smaller/dimmer ≈ rotateY ±20° [EST], horizontal row, no orbit (deg/s: n/a). Panels: flat 2D with glow, nothing orbits. Figma panel: inner image has 3D pan/rotation (claimed by speech) [OBS blur only]. Radius: diamond corner ≈ 18% of badge width [EST]; panel ≈ 3.5% W [EST].

## 7. Camera & transitions
| frames | type |
|---|---|
| #8-70 | footage→card shrink |
| #17-36 | carousel build |
| #150 | hard cut |
| #205-240, #496-545, #669-715, #1112-1150, #1312-1385, #1446-1480 | panel/card entrances (spring-ish ease-out, 1.1-2.4 s) |
| #390-403 etc. | panel fade-out ≈ 0.5 s |
No zooms, whips, flashes or punch-ins on the footage after the cut (framing constant per scene).

## 8. Assets used
Built: diamond badges, glass panels, star shapes, checklist bullets, effect-list UI, carousel. Captured: YouTube tutorial card (own thumbnail "Edit Like Me"), Figma-like UI screenshot (third-party UI; study only). Footage clones fill the carousel.

## 9. Sound ↔ picture
| onset s (frame) | attack ms / centroid Hz | visual | Δ f |
|---|---|---|---|
| 1.83 (#55) | 366 / 2672 | carousel mid-build | in A02-A03 |
| 8.27 (#248) | 35 / 2237 | specimen panel, "Coolvetica" #253 | −5 f |
| 16.67 (#500) | 41 / 1877 | A10 start #496 | +4 |
| 20.29/20.53/20.81 (#609/#616/#624) | 499/453/174 | "pop" @#610, stars glow | ≈0, +6, +14 |
| 29.02 (#871) | 215 / 2303 | A12 start #868 (burst #871) | +3 |
| 37.55 (#1126) | 261 / 1635 | A13 start #1112 | +14 |
| 43.93 (#1318) | 192 / 2805 | A14 start #1312 | +6 |
| 48.16 (#1445) | 238 / 1353 | A15 start #1446 | −1 |
| 51.32 (#1540) | 41 / 1519 | A16 start #1539 (burst) | +1 |
Totals: 21 strong onsets in 53.4 s (0.39/s); the only hard cut (#150) has no onset within 100 ms (hit rate 0.0); cue medians 586 ms long, attack 192 ms, centroid 2237 Hz, peak −2.1 dBFS [MEAS]. 9 of 21 onsets fall within ±15 f of a panel entrance — consistent with soft whoosh-like cues under panel entrances [INF]. Music bed: rms p10/p50/p90 −30.4 / −19.6 / −13.2 dB [MEAS] → likely music present [EST].

## 10. Editing psychology
| condition | action | reason [INF] |
|---|---|---|
| a numbered pillar begins | blue diamond + bold title at left, speaker visible | scannable chapter marker; face remains for trust |
| the pillar is about a visual technique | glass panel at chest that performs the technique | "show don't tell"; chest area is empty of captions |
| a font/typography is named | specimen panel with label + leader line | verifies the spoken name visually |
| the CTA is asked | plain bold captions, then tutorial card rising in the lower third | no competing graphics while the ask is spoken |
| intro | footage shrinks into a card carousel | signals "this is the object being analysed" |
Pacing (visual state changes per 10 s, counted from §2 rows): 0-10 s: 6 (card, caption, diamonds, cut, badge, title) · 10-20 s: 5 · 20-30 s: 6 · 30-40 s: 5 · 40-50 s: 6 · 50-53 s: 2. Even ≈ 5-6 per 10 s (steady ≈ 1.8 s per change); no hook spike except the hard cut at 5 s. [EST from rows]

## 11. Signature moves (self-contained recipes)
1. Numbered diamond chapter badge: rotated rounded square, blue ≈ #1F8FE0 with glow ≈ 14 px, white bold numeral; scales/fades in ≈ 0.6-0.73 s at x≈19%, y≈58%; title in white bold 2.5% H wipes in right (0.4 s).
2. Glass panel at chest: 69% W (748 px), blue border 1.5 px, glow ≈ 14 px, fill rgba(20,30,90,.55); rises ≈ 80 px with ease-out/spring over 1.1-1.6 s `cubic-bezier(0,1.4,0,.9)`.
3. Footage-to-card shrink: 100%→41% H in 2.07 s `cubic-bezier(.5,0,0,1)`, with dashed inner frame and side clone cards.
4. Demonstration panels (stars, diamonds, effect list) that perform the pillar being named, entering 1.7 s before / 1-2 s after the word.
5. Leader-line callouts naming fonts/tools in 1.1% H text.
6. Tutorial card rise: `cubic-bezier(.2,1.4,.2,1) 1.13 s`, from lower-right to centre-low.
7. Hard cut only once; everything else is overlay on continuous footage.

## 12. Gaps / uncertain
- Strips viewed: 2/27 (strip_000, strip_004); skipped = panel-hold strips, covered through 5 sheets (2 fps) + T1-T11. Sheet-based times are "~"/[EST]. Panel exits, bullet timing, star-fill timing, leader-line draw timing and glow radius are not frame-measured.
- Work CSV usage: T1-T11 all cited (T3 #168-200 bw/cx rmse .20-.36 → discarded as title-region track polluted by the mic boom; T11 rmse .29 → EST only).
- Fonts unconfirmed (spoken names Coolvetica / Edwardian Script are creator statements, not measurements; ASR wrote "Coolvetic", "Itwardian").
- Carousel angles, glow radii and corner radii not measured. 3D camera inside the Figma panel not analysed.
