# V02 teardown — "3 mistakes that make your edits look amateur" (beginner → professional)
720x1280 @30fps, 1491 frames (49.7 s). Coordinates: x%/y% of frame, px in 1080x1920 (= src px x1.5). Frame #N = N/30 s.

## 1. Overview
- Hook: "These three mistakes make your edits look like an amateur" (0-3.2 s). Topic: 3 motion-design rules (1: make elements 25% smaller, 2: use fewer effects, 3: use duller colours). The video itself practises them: small type, restrained motion, cream/dull palette. [INF]
- Structure: HOOK + promise #0-259 (0-8.6 s; 3-badge tracker + Beginner→Professional slider) → MISTAKE 1 #260-~615 (8.7-20.5 s) → MISTAKE 2 #615-~920 (20.5-30.7 s) → MISTAKE 3 #920-1310 (30.7-43.7 s) → CTA recap #1310-1490 (43.7-49.7 s, A-roll + badges). [OBS]
- Runtime share [EST from sheets + events.md cut list]: A-roll full frame ≈ 20.5 s (41%); split screen (cream graphic pane on top, A-roll below) ≈ 13.9 s (28%); full-frame cream graphic scenes ≈ 15.3 s (31%). No saturated colour cards (unlike V01).
- Shots: 4 hard cuts in events.md (#260/261 iris, #404, #920, #1310) plus 6 wipe/pane transitions flagged as motion bursts (#322, #613, #714, #807, #991, #1109). Scene change every ≈3.8 s [EST]; events.md "8.28 s avg" counts hard cuts only and under-states edit density.
- Distinct animations catalogued: 21 (V02-A01…A21); 10 curves measured with track.py/ease_fit.py.
- Look: navy-blue studio A-roll (brown hoodie, RØDE mic) with small white sans + electric-blue script captions; warm off-white (#FFFEFB) "Apple keynote" graphic panes with soft shadowed white cards, one photoreal eye render, brand-logo cards; blue #397FF7-ish script as the only accent.

## 2. Beat-by-beat timeline
| frames | time | words (ASR) | screen layers back→front | anim | camera | SFX onset | WHY |
|---|---|---|---|---|---|---|---|
| 0-95 | 0.00-3.17 | These three mistakes make your edits look like an amateur | A-roll full; caption "These" small left, script "three mistakes" blue, "make your edits look like an amateur" small below; red-outline 1-2-3 badge row under | A01,A02,A20 | static medium shot | 1.28, 1.67, 2.37 s (onsets with attack 0.5 s, swell-like [INF]) | counted promise ("three") = open loop, badge row makes the list tangible |
| 96-125 | 3.20-4.17 | Here's what you should do | badges + caption fade out (burst #99-105) → caption white small | A20 | static | — | reset before the promise |
| 126-197 | 4.17-6.57 | take your animation from beginner to professional | A-roll; dark pill with "Beginner ——— Professional" slider; white thumb travels left→right, bar fills blue | A03 | static | 4.46 s, 5.60 s, 6.04 s | before/after promise visualised as one gesture |
| 198-259 | 6.67-8.63 | Number one, stop over-sizing everything | A-roll; white 1-2-3 badges with "1" filled; "Number 1:" white + script blue "Stop oversizing everything" | A01,A02 | static | 6.83 s (badge change #205) | numbered chapter marker, rule in blue script |
| 260-322 | 8.67-10.73 | The biggest thing that screams beginner editor | centre iris wipe to cream; creator thumbnail card (orange bg) fades in, scales up, drops low; "The biggest thing that" black sans + "screams beginner" blue script | A04,A05,A06 | card settles ~5-7° tilt | — | scene change = new topic; card = "the edit" being judged |
| 323-403 | 10.77-13.43 | editor is huge icons and huge shape layers | card slides up to top-left (#323-335); "Huge icons and" + script "huge shape layers" bottom-right | A05,A06 | — | — | names the error with the creator's own object as the example |
| 404-540 | 13.47-18.0 | As a rule of thumb, the next time you're creating an animation | cream pane slides in from top to half height; large blue app-icon card; A-roll pushed to lower half with captions ("As a", script "rule of thumb", "creating an", script "animation") | A07,A08,A20 | A-roll pane shifted down | 14.54 s | split screen keeps speaker present while the abstract rule is shown |
| 541-606 | 17.87-20.2 | make every element 25% smaller | icon shrinks 225→169 px (−24.9%) inside a dashed ghost outline; blue "-25%" pill; blue/black particle burst; script "25% smaller" | A09,A10 | — | 16.76 s | the rule is literally performed on screen |
| 606-614 | 20.2-20.5 | and just watch how much better it looks | A-roll grows from lower half to full frame (18 f); script "better" | A11 | pane collapses | — | payoff of rule 1 returns to face |
| 615-719 | 20.5-23.97 | Number two, stop overusing effects. Less is more | A-roll; badges 1-2 white; "Number 2" + script "stop overusing effects"; later script "Less is more." | A01,A02 | static | — | chapter 2 marker; maxim in script |
| 720-806 | 23.8-26.9 | The less you use an effect, the more special it is | split: cream pane with "EFFECT USAGE" segmented meter (blue segment travels 1→centre); A-roll below, script "less", "special" | A07,A12 | — | — | meter = visual proof for "less" |
| 807-919 | 26.9-30.63 | Reserve your visual effects for elements that you really need to grab attention | rounded-rect wipe covers A-roll; eye render pops from dot; timeline mini-panel (top-left) and waveform card (bottom-right) fly in; "Reserve your" + script "visual effects", later "for elements that you really need to" + script "grab attention" | A13,A14,A15 | — | — | one eye = "attention"; the two panels = the effects you may spend it on |
| 920-989 | 30.67-32.97 | And number three, use more dull colors | hard cut A-roll; badges 1-2-3 (3 active); "And number 3" + script "use more dull colors" | A01,A02 | cut (#920 diff 212) | 30.77 s (+100 ms after cut) | chapter 3 marker |
| 990-1109 | 33.0-37.0 | Beginner editors always use harsh blacks, harsh whites and bright reds | split: cream pane "Beginner editors" + script "always use"; swatches pop (black → white → red); A-roll below with "harsh / blacks," etc. | A07,A16 | — | 39.36 s later | swatches appear on the spoken word (black @#1034-1040, red @#1084) |
| 1110-1229 | 37.0-41.0 | [ASR: jargiest] → on-screen "Luxurious brands" always use dull colors | full cream pane; brand-logo cards pop in staggered (8 brands) while "Luxurious brands always use" + script "dull colors" sits left | A17,A14 | slow parallax drift [EST] | 39.36, 40.19 s | borrowed authority (luxury) for "dull = high-end" |
| 1230-1309 | 41.0-43.63 | Duller colors always look more high-end | logos fade; centred black "Duller colors always look" + script "more high-end." | A18 | — | 41.15, 42.84 s | the thesis line alone on a clean page |
| 1310-1490 | 43.67-49.7 | So now that you know that, change these three things … go from beginner to professional | hard cut A-roll (tighter, calmer); badges 1-2-3; small white captions, script "know" | A01,A19,A20 | cut #1310 (diff 225) | 46.56, 49.16 s | recap = tracker closes the loop opened at 0 s |

## 3. Animation catalogue
Measured with track.py + ease_fit.py unless tagged. Several fits are on small net changes; confidence is stated.

**V02-A01 Progress badge row (1-2-3 tracker)** — element: three circular badges joined by a thin line, centred ≈ x50%, y≈66% H in A-roll lower third. Hook version: red-outline circles on dark chip; body version: white circles, active one filled white with dark numeral, inactive ones grey outline. Connector line draws 0→275 px src (413 px 1080-wide) in #10-34 (24 f, 800 ms), easeOutCirc-like, bezier (0,0.9,0,0.6) rmse .071 [MEAS a_badges.csv]. Step change at each "Number n" (#201, #615, #924): previous circle stays filled, next fills [OBS]. Fades out with caption at #96-105 in hook; remains through chapters; reappears in CTA. Rebuild: SVG circles + line with stroke-dashoffset animation, fill toggled per chapter. Reusable: "chapter tracker". **Strip check (strip_000, 2026-11-06):** circle 1 fades in #12-15, connector 1 draws #19-21, circle 2 #21-23, connector 2 #25-27, circle 3 #29-31 → row built in ≈ 20 f (0.67 s), ≈ 8-9 f per step [OBS].

**A02 Blue script phrase reveal** — script words ("three mistakes", "Stop oversizing everything", "use more dull colors", "Less is more.") enter left→right with fade (soft mask wipe), ≈8-10 f [EST from sheets, not frame-measured]; colour ≈ #397FF7 [MEAS mean of blue pixels, f450/f840: (53-57,127,247-254)]; faint glow only on dark A-roll [OBS]. Exit: hard clear or fade with next phrase. Rebuild: clip-path inset wipe + opacity, italic serif (Playfair/"Instrument Serif"-style, conf. med). **Strip check (strip_000):** "three" reveals #11-18, "mistakes" #17-26, "make" #36, "your" #45, "edits" #49-52 → ≈ 8-9 f per script word, left→right with fade [OBS, replaces "≈ 8-10 f [EST]"].

**A03 Beginner→Professional slider** — dark pill chip with labels "Beginner" (left) and "Professional" (right), white thumb with soft shadow; thumb centre x 208→504 px src over #125-197 (72 f, 2400 ms) [MEAS a_slider.csv]. Curve is near-linear/slightly accelerating (best fit easeInSine rmse .150; free bezier (1,0.7,1,0.6) rmse .076): it follows the sentence, not an ease [MEAS]. Bar left of thumb fills blue (#2F6BFF-ish [EST]); label "Professional" brightens at the end (#180). Rebuild: width of fill = thumb x; drive with speech timestamps, not an easing curve.

**A04 Centre iris wipe to cream** — #259 last A-roll frame (diff 108.7); #260 white circle ≈ 100% W diameter centred (≈50%,≈50%); #261 circle > frame; #262 full cream [OBS strip 8.0 s]. 3 f / 100 ms, hard-edged circle, no blur [OBS]. Trigger: end of "everything"/start "The biggest". Rebuild: clip-path circle() 0→150% in 3 frames.

**A05 Thumbnail card entrance + slide** — creator video card (orange backdrop, portrait, rounded ≈6% radius, soft drop shadow). #262 appears at ≈40% opacity small near centre; #263-281 height 375→585 px (+56%) and drifts down so bottom reaches frame edge; tilt −20.6° at #263 → +5.6° at #269 → settles 5.4-7.5° [MEAS card2.csv, tilt estimate from edge, ±2°]. #323-335 (12 f, 400 ms) card slides up: top edge 727→0 px, size unchanged (w 385→373) [MEAS], ends top-left of frame. Rebuild: translateY with ease-out; rotate(-20°→6°) 8 f; shadow 0 20px 40px rgba(0,0,0,.18).

**A06 Black-sans + blue-script lockup (cream)** — small black sans ("The biggest thing that", "Huge icons and") reveals word by word left→right (≈4-5 f per word, mask wipe, grey→black), then script blue ("screams beginner", "huge shape layers") reveals per character left→right starting light blue (#9FC0F5-ish) to full blue over ≈8 f [EST/OBS strips 8.0, 12.0 s]. Script starts ≈3 f before word onset ("screams" word #293, script first visible #290) [OBS]. Position: line at lower-centre (y≈71% H) on first scene, lower-right on second.

**A07 Split-screen pane slide-in** — cream pane enters from top edge, height 0→639 px src (50% H) in #405-418 (13 f, 433 ms); A-roll underneath is pushed/cropped to the lower half. Fit: easeInOutCubic rmse .050, free bezier (0.6,0,0.3,1.05) rmse .008 [MEAS splitY.csv]. Same device re-used at #712 (23.73 s) and #990 (33.0 s) [OBS, motion bursts peak 45/44]. Rebuild: two stacked divs; top height animates 0→50% with cubic-bezier(.6,0,.3,1). **Strip check (strip_024):** second use starts ≈ #716 (A-roll top edge already ≈ 12% down at #720) and reaches ≈ 52% H by #731 ≈ 15 f (≈ 0.5 s) [OBS ±2 f]; split_in2.csv / split_in3.csv (bw 19 px constant: edge-column probe, no motion detected) are discarded.

**A08 App-icon pop** — large rounded-square white card with blue gradient play icon, soft shadow, appears from top edge #410-420 scaling up as the pane opens (~10 f) [OBS]; floats centred in the pane through #540. Rebuild: scale .6→1 with the pane slide.

**A09 "-25%" shrink with ghost outline** — icon card bw 225→169 px src (−24.9%) over #536-600 (64 f nominal, 2133 ms; most motion in the first ≈20 f), spring: overshoot 21% of the 56 px change, best bezier (0.3,1.4,0,0.9) rmse .128, easeOutExpo rmse .169 [MEAS icon_shrink_b.csv]. A thin outline of the original size remains as a "ghost" [OBS 18.0-19.5 s]. Trigger: "twenty-five percent" word @#527, shrink starts ≈#536 (+9 f). Rebuild: transform scale(1→.75) with cubic-bezier(.3,1.4,0,.9); ghost = static dashed border.

**A10 "-25%" pill + particle burst** — small blue pill top-right of the ghost outline: width 6→86 px src, first detected at 6 px (not a rest value); fit peak/final ≈ 1.46 but rmse .189 > .12 → family only (spring-like ease-out) [EST pill.csv]; ≈25 blue/black dots radiate from the icon #540-575 and fade [OBS]. Purpose: celebratory "pop" for the key number. Rebuild: spring scale for pill; particle emitter (CSS or Remotion) 36 f.

**A11 Pane collapse back to A-roll** — A-roll region grows from lower half to full frame: height 639→1279 px in #606-624 (18 f, 600 ms); accelerating, easeInSine rmse .161, free bezier (1,0,0.3,0.9) rmse .035 [MEAS split_out1.csv]. Reverse of A07 in intent. Burst #613-626 peak 49.9 [events.md].

**A12 Effect-usage segmented meter** — pale card "EFFECT USAGE" header + 10 grey segments; one blue segment (pill) moves/grows from left to ≈ centre while neighbours stay grey, then narrows to one segment as "special" lands (#24.0-26.5 s) [OBS sheet 24.0-26.5, EST timing]. Plays in the top pane above A-roll. Rebuild: flex of 10 rounded segments; highlighted index animated with spring. **Strip check (strip_024):** grey segments appear one by one from #723 (1 pill) to 10 segments by ≈ #765, i.e. 9 steps in ≈ 42 f ≈ 4.7 f (157 ms) per step; the blue segment appears as a dot at #742, full pill by #745 (≈ 4 f pop), stays in the 5th-6th slot, and a soft halo pulses from #771 [OBS]. The blue segment does not travel; the bar fills around it.

**A13 Rounded-rect wipe + eye reveal** — #807 small white notch at top centre; rect widens to full width 0→719 px in #805-816 (11 f, 367 ms), easeOutQuart rmse .071, free bezier (0.3,0.3,0,1.1) rmse .022 [MEAS irisX.csv], covers A-roll; eye render appears as a dot at #822 and grows to full size by ≈#829 (7 f, 233 ms) with soft ground shadow [EST from strip 26.0 s, not tracked]. Trigger "Reserve" @#807 (0 f). **eye.csv (work/tr/eye.csv, #806-845): bw 519→504 px, rmse 8.9 → discarded (bbox is the white rect, not the eye).**

**A14 Two-line type lockup (cream)** — "Reserve your" black sans (small) above "visual effects" script blue (larger), centred y≈47% H; same pattern for "for elements that you really need to / grab attention", "Luxurious brands always use / dull colors". Words appear left→right; script line follows the black line by ≈10 f [EST]. Dead-centre, text cap height ≈2% H (black) and ≈3.3% (script) [EST].

**A15 Floating UI panels around eye** — timeline mini-panel (blue clips on grey tracks, top-left of eye) flies in #833-838; waveform "Sound FX" card (bottom-right) #836-845; both white cards with soft shadows, tiny labels [OBS]. They represent "effects"; each slides in ≈20-40 px from outside with ease-out [EST].

**A16 Colour swatch pop (black / white / red)** — rounded-square swatches with tiny labels (hex-like captions, unreadable at 720 p [OBS]); black swatch width 96→156 px, tracked width 96→193→156 px (peak ≈ 1.24× final; 96 px is the first detection, not a rest value), nominal 1600 ms (#1044-1092), curve shape family only (rmse .172 > .12) [MEAS peak ratio, EST shape; sw_black.csv]; red swatch 48→148 px in #1093-1104 (367 ms), peak ≈ 1.45× the first-detected width, rmse .196 > .12 → family only [EST shape; sw_red.csv]; strip_036: red appears as a dot at #1092, reaches full size by #1100-1103 (≈ 9 f) with an ≈ +8% larger frame at #1099-1100 [OBS]. Triggers: "harsh" @#1034 (black appears #1040, +6 f), "bright" @#1084 (red +9 f). White swatch appears between (≈#1060 [EST]). Rebuild: spring scale (.4→1, overshoot ≈1.05-1.2).

**A17 Brand-logo card field** — 8 white rounded cards each carrying a luxury-brand wordmark (third-party marks; do not reproduce), different sizes, scattered around a left-centre text block; staggered pop-in (see strip check) from #1115 to ≈#1195, each with scale-up and soft shadow; field drifts slowly left/up (~15-20 px over 3 s [EST]) [OBS sheet 37.0-40.5]. Motion burst peak 63.6 at #1109 = cut into this scene. Rebuild: absolute cards with stagger delay 12-15 f; slow translate of group. **Strip check (strip_036, strip_038):** pop-in frames — Tiffany #1115, Rolex #1124, Chanel #1134, Louis Vuitton #1144, Dior #1152, Cartier #1160, Bottega (faint) #1178, Prada #1193 → ≈ 8-10 f apart for the first six (0.27-0.33 s), then 15-18 f [OBS]; the preceding pane (#1123-1127) is covered by a hard centre circle iris in ≈ 3-4 f [OBS]. Replaces "≈0.4-0.5 s [EST]".

**A18 High-end line reveal** — "Duller colors always look" black; then script blue "more high-end." wipes in: tracked line width 201→572 px src in #1272-1296 (24 f, 800 ms), easeInOutQuart rmse .226, free bezier (0.7,0.1,0.2,1.1) rmse .205 [MEAS w_highend.csv] — noisy, treat as a left→right wipe ≈800 ms. Trigger "high-end" @#1288 (reveal already under way = anticipates by ≈10 f).

**A19 CTA recap tracker** — badge row 1-2-3 (white, all active) returns under centred white captions (2 lines); text is word-appearing sans, script "know" [OBS]. Calm: motion bursts here peak ≤6.8 [events.md].

**A20 A-roll caption stack** — small white sans (cap ≈2% H, medium-bold), 1-4 words per line, left-aligned to centre depending on line; newest word fades in over ≈6 f, older lines stay and push up; max 2-3 lines; sits y≈52-60% H on full A-roll; in split mode sits in the upper part of the lower pane [OBS]. Script words (blue) replace sans for emphasis: three, mistakes, Stop oversizing, rule of thumb, animation, 25% smaller, better, Less is more, special, use more, dull colors, know. Rebuild: per-word opacity .25→1, 6-16 f easeOutCubic (V01 measured 16 f; V02 not re-measured).

**A21 Hard cuts on A-roll** — #920 (diff 212) and #1310 (diff 225): hard cuts, no flash; framing between shots shifts a few %, head scale changes (e.g. tighter at 30.5 s, 43.7 s) [OBS sheets, scale not measured]. Whoosh at 30.77 s (+100 ms after cut).

## 4. Text & typography system
| style | font guess (conf.) | weight | cap height %H | colour | use |
|---|---|---|---|---|---|
| A-roll caption | Inter / SF Pro-like grotesque (med) | Medium | ≈2.0% | #FFFFFF | spoken words under the mic |
| Script emphasis | italic high-contrast serif, Playfair-italic-like (low-med) | Bold italic | ≈3.3-4% | #397FF7 | rule names, key phrases |
| Chapter label | same sans | Regular | ≈1.8% | #FFFFFF | "Number 1:", "And number 3" |
| Cream-pane lead | same sans | Medium | ≈1.8-2.2% | #111111 | "The biggest thing that" |
| Cream-pane script | same serif italic | Bold | ≈3.3% | #397FF7 | "screams beginner", "visual effects" |
| Micro UI label | same sans | Medium | ≈0.7% | #9AA0A8 | "EFFECT USAGE", slider labels |
Rules [INF]: the noun-phrase that carries the rule goes in blue script; connective and framing words stay small sans; caption lines are short (2-4 words) and never cover the face; type is small on purpose (the video preaches "25% smaller"). Captions on A-roll sit at chest/mic height; in split screen they move to the lower pane. No caption during the 3 s eye/logo scenes' wipe moments.

## 5. Colour, light & material
- Cream ground #FFFEFB (flat, with a very faint paper grid visible on logo/eye scenes [OBS]) [MEAS pixel f450/f840].
- A-roll grade: wall #001938-#063B66 deep navy, bottom of frame crushed to #010010, skin neutral-warm, hoodie brown. Vignette: dark bottom third where badges/captions sit [MEAS samples f60].
- Accent: electric blue ≈#397FF7 for script and highlights; red swatch for "bright reds" demo; icon gradient blue (#2F6BFF→#4C8CFF [EST]).
- Cards: white, radius ≈8-12% of card width, soft shadow 0 12px 30px rgba(0,0,0,.10) [EST]; no borders. No glass/holographic panels (unlike V01).
- Particle dots: blue #397FF7 and black.

## 6. Depth & 3D
Mostly flat 2D layout. Depth cues: soft shadows under every card and under the eye; the thumbnail card is tilted ≈5-7° (2D rotate); slow parallax drift in the logo field [EST]; A-roll to split pane relies on cropping, not 3D. Eye is a photoreal still, not a 3D object [OBS].

## 7. Camera & transitions
| frames | type |
|---|---|
| #96-105 | caption/badge fade (A-roll continues) |
| #259-262 | centre iris wipe (circle) A-roll→cream |
| #323-335 | card slide-up within cream scene |
| #404-418 | top pane slide-in → split screen |
| #606-624 | pane collapse → A-roll full |
| #712-728 | pane slide-in (second split) |
| #805-816 | rounded-rect wipe A-roll→cream (eye scene) |
| #920 | hard cut cream→A-roll |
| #990-1004 | pane slide-in (third split) |
| #1109-1115 | cut/wipe into logo scene (peak 63.6) |
| #1310 | hard cut cream→A-roll |
No whips, flashes, shakes, or animated zooms on footage; framing differences between A-roll shots come from jump cuts.

## 8. Assets used
Built in an editor: badge tracker, slider, effect meter, swatches, icon card, pill, logo cards (third-party wordmark captures/recreations), "timeline" and "Sound FX" mini-panels. Captured/stock: creator video thumbnail (orange backdrop), photoreal eye render (stock/3D render), brand logos. Never reproduce brand marks or the thumbnail outside the study folders.

## 9. Sound ↔ picture
| onset s | frame | visual | Δ ms |
|---|---|---|---|
| 1.28 / 1.67 / 2.37 | #38-71 | badge line + "three mistakes" build | during build [INF] |
| 4.46 | #134 | slider travel (start #125) | +300 into move |
| 5.60 / 6.04 | #168/#181 | slider near end / "professional" | ≈0 [INF] |
| 6.83 | #205 | badge "1" change (#200-207 burst) | +0-100 |
| 14.54 | #436 | icon scale-up in split | — |
| 16.76 | #503 | rule/"25%" approach | −800 vs #527 word |
| 30.77 | #923 | hard cut #920 | +100 |
| 39.36 / 40.19 / 41.15 | #1181-1234 | logo pops / text swap | ≈0 [INF] |
| 42.84 | #1285 | "high-end" line | ≈ −100 |
| 46.56 / 49.16 | #1397/#1475 | CTA beats | — |
Only 16 strong onsets in 49.8 s (0.32/s), 1 of 5 cuts has a hit within 100 ms (hit rate 0.2). Cue medians: 578 ms long, 104 ms attack, centroid ≈2.2 kHz, peak −3 dBFS: attack 104 ms median (soft onsets, not sharp impacts); sound type not verified by ear [INF]. Most transitions (iris, pane slides) have no distinct SFX onset [MEAS]. Light music bed likely (rms p10 −29 dB, p50 −19.8, p90 −13.5) [EST]. Sound is sparse by design (consistent with "less is more").

## 10. Editing psychology
- Rule: abstract principle → split screen or cream pane with a literal demonstration (icon shrinking 25%, usage meter, swatches, luxury logos); personal claim / chapter marker / CTA → full A-roll with tracker. [INF]
- Retention: three-item list with a persistent tracker; each chapter gets a different scene vocabulary (card + split → meter + eye → swatches + logos) so rhythm never repeats; payoff line always returns to the face. [INF]
- Pacing: fast hook (promise + slider in 8 s), chapters 10-13 s each, calm CTA. Hard cuts reserved for chapter 3 and CTA entry; elsewhere wipes and pane slides. [OBS]
- The video demonstrates its own rule: small type, one accent colour, sparse SFX, no glows/holograms. [INF]

## 11. Signature moves (ranked)
1. Split screen: cream pane slides in from top (433 ms easeInOutCubic) while the speaker stays in the lower half.
2. Chapter tracker 1-2-3 under the speaker (line draws in 800 ms; active badge fills).
3. Black sans + blue script two-line lockup on cream, script lagging by ≈10 f.
4. Literal demonstration of the number ("25%": 225→169 px, spring, ghost outline, "-25%" pill, particle burst).
5. Spring-pop objects (swatches, pills, eye) with spring-like pop, peak ≈ 1.24× final (sw_black 96→193→156) [MEAS]; curve shape EST (fits rmse .17-.20).
6. Centre circle iris wipe for a topic switch (3 frames).
7. Slider driven by speech (2.4 s linear) for before/after promise.
8. Staggered white brand cards as borrowed authority.
9. Restraint: one accent colour, sparse SFX.

## 12. Gaps / uncertain
- Strips viewed: 7/25 (000, 008, 012, 024, 026, 036, 038); NOT viewed and not static: 002-006, 010, 014-022, 028-034, 040-048 (eye-scene panels ~28 s, CTA ~44 s etc.). Native-frame strips were viewed only for 0, 8, 12, 24, 26, 36, 38 s; the rest was covered with the 2 fps sheets + events.md, so inter-sheet details (exact word-reveal frames, A-roll punch-in amounts, logo stagger times) are [EST].
- Several ease fits are on small net changes (card, eye, icon_in: overshoot % unstable); only the numbers quoted above should be trusted.
- Fonts unconfirmed; swatch/slider micro-labels unreadable at 720 p.
- [ASR: jargiest] = on-screen "Luxurious brands"; transcript otherwise matches captions.
- Eye scale-in and logo card timings not tracked. Music vs SFX not separated.
