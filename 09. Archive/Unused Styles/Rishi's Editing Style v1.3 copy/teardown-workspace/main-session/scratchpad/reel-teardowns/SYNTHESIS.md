# SYNTHESIS — cross-reel style model from 15 reference reels (Phase 2)
Opus, 2026-11-06. Sources: 15 × animations.json (288 entries) + §1/§4/§5/§9/§10/§11/§12 of each BREAKDOWN.md, PROGRESS.md, QUALITY_NOTES.md. No videos were re-viewed.
Evidence tags as in BRIEF: [MEAS] tool-measured · [OBS] seen in frames · [EST] estimated · [INF] interpretation. "n/15" = number of reels showing the feature.
**⚠EST** marks a CORE rule whose numbers rest only on estimates. Phase 4 should treat those numbers as starting defaults, not as facts.

---

## 0. How to read this (key judgements)
1. **There are two style families.** *Family A* (V01-V04) uses a navy/slate studio, glow/glass/holographic panels and larger captions (2-3.4% H). *Family B* (V05-V15, 11 reels) uses flat white UI cards on one of two fixed grounds (saturated blue or warm cream), white sans captions at 1.5% H with one italic-serif word, diamond chapter badges and a comment-keyword CTA. Family B is the majority and is internally consistent (same cream hex #EBE7E1 in 6 reels, same blue ground in 3 reels [MEAS]). **CORE = Family B unless a feature also appears in Family A.** Family A-only features are OPTIONAL or EXPERIMENTAL. That is why no single reel (V01 especially, the most measured) rewrites the identity.
2. **Measurement quality differs between reels.** Best-measured: V01, V10, V14, V15, then V04, V12, V13. Weakest: V05-V09, V11 (noisy tracks, 3-6 usable curve sets). Native strips were mostly not viewed for V03-V15, so sheet-based timings there carry ±0.5 s. When reels conflict, the better-measured reel wins unless it is a lone outlier against 5+ reels.
3. **Reel genres.** The scene vocabulary depends on genre, so Phase 4 should select scenes by genre:
   - *Teach-a-rule*: V01, V02, V04, V06, V08, V11, V14
   - *AI-workflow demo*: V03, V05, V14
   - *Student story*: V10, V13
   - *Offer/closing*: V07, V09, V12, V15

---

## 1. CORE / OPTIONAL / EXPERIMENTAL

### 1a. CORE (appears in most reels; part of the identity)
| # | rule | n/15 | where | evidence |
|---|---|---|---|---|
| C1 | Talking-head A-roll alternates with graphic scenes. The speaker returns between graphic beats and the payoff line is said on the face. | 15 | all | [OBS] all reels |
| C2 | One graphic ground per reel: **saturated blue** (#4279BB top → #205AA4 bottom, light rays + faint grid) **or warm cream** (#EBE7E1, corner #E6E2DD, faint grid + soft radial vignette). Mixing both grounds is rare (V03/V05, where cream = the Claude app UI, not a style ground). | blue 6 (V03,V05,V06,V07,V12,V14) · cream 6 (V08-V11,V13,V15) · other 3 (V01 ice, V02 #FFFEFB, V04 grey) | §5 | hexes [MEAS] in V06/V12/V14 (blue) and V08-V11/V13/V15 (cream) |
| C3 | Flat white UI recreations are the proof layer: post/profile cards, tweets, toasts, search/comment bars, product cards, with soft shadow and no border. | 14 (not V04: glass) | §8 | [OBS]; white #FDFDFD [MEAS V06], #ECECEE [MEAS V07] |
| C4 | Caption system: white grotesque sans (Inter/SF-like) for the spoken line + **one italic high-contrast serif word** per group on the key noun/qualifier + **bold on numbers/money/keyword**. Never over the face. | italic-serif 13 (not V01 = true script, not V04 = specimen only) | §4 | [OBS]; fonts unconfirmed everywhere |
| C5 | Caption size: sans cap ≈ 1.5% H, script ≈ 2.0% H (≈ 1.3×). Family A is larger (2-3.4%). | 10 (V06-V15) | §4 | ⚠EST (cap heights eyeballed) |
| C6 | Caption position: on A-roll at chest/mic height, y ≈ 55-66% H. On graphic scenes it moves to the top, y ≈ 6-14% H, and the object sits mid-frame. | 12 | §4 | ⚠EST |
| C7 | **Quantity claim → wall/field of cards** (grid, mosaic, tweet wall, phone-card field, card strip). "Volume = credibility." | 11 (V01,V03,V05,V06,V07,V10,V12,V13,V14,V15,V09) | §10 | [OBS] |
| C8 | **Rule/claim → literal demonstration**: the graphic *performs* what is said (icon shrinks 25%, colours split 60/30/10, price is struck through, a prompt is typed). | 13 | §10 | [OBS]/[INF] |
| C9 | **Numbered chapter structure** (3-6 items) with a visible marker per chapter. The default marker is a blue rotated-square **diamond badge** with a white bold numeral and a bold title. Variants: 1-2-3 circle tracker (V02, V11 recap), script ordinals (V15). | numbered 11 · diamond 7 (V04,V06,V08,V09,V10,V11,V13) | §3 | entrance measured only on V10's centred variant: 433 ms `cubic-bezier(0,.6,.2,.6)` rmse .019 [MEAS]; others ⚠EST 0.5-0.73 s |
| C10 | **Split screen**: graphic pane slides down from the top to ≈ 48-50% H, and the A-roll is pushed into the lower half. Used for definitions/evidence while the speaker stays visible. | 9 (V02,V03,V06,V07,V08,V10,V11,V12,V14) | §7 | [MEAS] V02, V14 (×6), V03 — timing reconciled in §2 |
| C11 | **CTA = "comment KEYWORD"**: a comment bar or comments sheet appears and the keyword types in (≈ 0.25-0.3 s/char, cursor/click at the end). | 12 (V03,V05-V15) | §2 last rows | [OBS]; typing speed ⚠EST |
| C12 | Card entrance easing = **fast-start ease-out with ≤ 3% overshoot**, ≈ `cubic-bezier(0.1, 0.9, 0, 1)` / `(0, 1.4, 0, 0.9)` family. Two duration tiers: secondary elements 0.33-0.47 s, hero cards 1.0-1.5 s. | bezier-grade in 8 reels | §2 below | [MEAS] ≥ 14 fits rmse ≤ .04 (list in §2) |
| C13 | Hard cuts are mostly **silent**: median cut↔onset hit rate ≈ 0.18 (range 0-0.33). Sound cues attach to element motion (panes, cards, typing), not to cuts. | 15 | §9 | [MEAS] audio.json all reels |
| C14 | **Front-loaded pacing**: 10-14 visual state changes in the first 10 s, 7-9 per 10 s in the body, 4-6 in the CTA tail. A new visual state every ≈ 1.6-2.3 s; a hard cut every ≈ 6.7 s (median). | 13 | §10 | cut lengths [MEAS events.md]; state counts ⚠EST (counted from rows) |
| C15 | **Proof before claim**: the number/artifact appears on or before the word, never after. Graphics land −10…+10 f around the trigger word; money counters/prices lead the spoken number by 0.7-2.4 s. | 11 | trigger offsets | [MEAS] words.json offsets (V01 A01 −10 f; V09 pill −2.4 s; V15 counter −0.7 s); per-entry offsets partly ⚠EST |
| C16 | **Accent colour discipline**: one blue accent family on the chosen ground; **green only for money/good outcome**, **red only for scarcity/negation** (hand-drawn ellipse, strikethrough). | 12 | §5 | ⚠EST — every green/red/accent-blue hex is [EST]; only #1E6CD9, #193452 (V08) and #103D7B (V11) are [MEAS] |
| C17 | Cards enter with **blur → sharp + small rise** (blur ≈ 8-10 px → 0, translateY ≈ 40-60 px → 0, opacity 0 → 1). | 9 (V05-V07,V09,V11-V14,V15) | animations.json | ⚠EST (no blur radius measured anywhere) |
| C18 | Constant mix: a music bed is likely under everything (rms p50 ≈ −19.6 dB, p10 ≈ −30 dB in every reel) with soft, long-attack cues (median length ≈ 590 ms, attack ≈ 170-450 ms, centroid ≈ 2.2-2.7 kHz). | 15 | §9 | [MEAS] stats; "music" itself is [EST] (not separated) |

### 1b. OPTIONAL (recurring, conditional, or genre-specific)
| # | move | n/15 | use when | evidence |
|---|---|---|---|---|
| O1 | Footage-to-card shrink as the opener (A-roll becomes a rounded card on the ground) | 4 (V01,V04,V05,V06) | hook needs "this edit is the object" | [MEAS] V01 1.87 s to 48% W `(.2,.4,0,1)`; V04 2.07 s to 41% H `(.5,0,0,1)` rmse .089; V05 0.93 s to 63% H [OBS] |
| O2 | Money counter count-up (ease-out, often already running at frame 0, then glow/confetti) | 6 (V07,V09,V10,V11,V13,V15) | offer/story reels with an income claim | values from 2 fps tiles [OBS]; V15 counter cx [MEAS ≈] |
| O3 | Hand-drawn red ellipse / strikethrough (0.35-0.5 s linear draw) | 5 (V07,V09,V10,V12,V15) | scarcity, deadline, old price — **mandatory when the script states a deadline** [INF] | [OBS] draw times ⚠EST |
| O4 | Category carousel (sample reel + title card, step every 1.5-1.8 s, blur dissolve 0.4 s) | 4 (V07,V09,V12,V15) | "what's inside" lists | V12 A11 bh [MEAS ≈] |
| O5 | Defocus of A-roll as a bridge behind UI / under a caption | 6 (V03,V05,V07,V10,V11,V12) | an abstract word or UI floats over the speaker | ⚠EST blur 8-12 px |
| O6 | 2D zoom/push into a proof detail (1.8-3.5×) | 6 (V01 2.0× zoom-cut, V06 3×, V11 1.8×, V13 3.5×, V15 2.2×, V10 3D push) | the one number that matters on a document/UI | V01 2.00× [MEAS frame pair]; V11 bw [MEAS ≈]; others ⚠EST |
| O7 | Tutorial/YouTube card rising at the CTA | 6 (V03,V04,V05,V06,V14,V11 banner) | CTA promises a free tutorial | V04 1.13 s `(.2,1.4,.2,1)` [MEAS] |
| O8 | Typed prompt in a chat UI, word-synced to speech, with file chips | 2 (V03,V05) | AI-workflow reels only | ⚠EST typing ~20 cps |
| O9 | Spring pop with visible overshoot (peak ≈ 1.08-1.25× final) | 6 (V01 A24, V02 swatches, V03 A01/A04, V06 A20, V13 A01) | small objects only: icons, pills, swatches, avatars — never hero cards | V01 18.9% [MEAS]; V02 peak 1.24× [MEAS sw_black]; V03 28-35% [MEAS]; V13 8% [MEAS ≈] |
| O10 | Reel-card strip scrolling behind the speaker's head (≈ 1 card / 1-1.5 s) | 3 (V13,V14,V15) | "thousands of creators/content" without leaving the face | [OBS] |
| O11 | Single-word drum-roll on the full ground (hard swaps ≈ 0.5 s/word, last word script) | 4 (V01 A20, V14 A04, V12 deadline text, V13 deadline) | provocative question, verdict, deadline | [OBS] |
| O12 | Giant verdict word (cap ≈ 12% H, heavy navy) | 1-2 (V11 "GOOD", V01 "1") | one-word judgement | V11 bw `(.2,.9,.6,.6)` rmse .042 [MEAS] |
| O13 | Pixelated/locked hidden item → comment CTA | 2 (V07,V12) | price or product kept secret | [OBS] |
| O14 | Money confetti (bills/dots, ≈ 1 s) | 2 (V09,V15) | price reveal or income climax | [OBS] |
| O15 | Leader-line labels on parts of a demo (0.5-0.7 s stroke draw) | 3 (V04,V08,V11) | naming parts of a design/font/tool | ⚠EST |
| O16 | Cursor-driven UI (arrow visible, click → zoom) | 4 (V08,V11,V15,V05) | "here is the button/action" | [OBS] |

### 1c. EXPERIMENTAL (one-off; keep out of defaults)
| move | reel | note |
|---|---|---|
| Font-cycle word (typeface swaps every 2 f, lands bold) | V01 | [OBS] 367 ms |
| Cylinder carousel / face-circle orbit ring | V01 | orbit 163°/s → 14°/s [MEAS] |
| Hand-held hologram icons, glass/holographic glow panels | V01, V04 (V05 brain icon) | Family A identity; contradicts C3 (flat white UI) |
| Flicker-on title on saturated #074C90 card | V01 | [MEAS] 300 ms |
| Gradient type-on line with drift | V01 | [MEAS] 9.7 px src/f |
| Slow 3D push on a hero post (rotateY ≈ −8°) | V10 | ⚠EST angle |
| Real-time 60-s countdown ring docked bottom-left | V06 (V08 stopwatch) | ring pop 900 ms `(0,1.4,0,.9)` rmse .023 [MEAS] |
| Percentage ring gauge | V11 | [OBS] |
| Particle burst | V02 | [OBS] |
| Centre iris wipe (3 f circle) | V02 | [OBS] |

---

## 2. Conflicts reconciled
| conflict | values seen | decision | why |
|---|---|---|---|
| **Split-pane enter duration/easing** | V02 433 ms `(.6,0,.3,1.05)` rmse .008 · V03 1.0 s · V07 1.3-1.5 s (cx track, not boundary) · V14 0.97-1.13 s ×3 `(.7,.1,.4,.9)` / `(.5,.2,.3,.9)` / `(.8,0,.5,.8)` rmse ≤ .012 · V15 1.17 s | **Default: 1.0 s, `cubic-bezier(.7,.1,.4,.9)` (ease-in-out), boundary 0 → 48% H. Allowed range 0.45-1.3 s.** Expand to ≈ 93% H: 0.85 s `(.7,0,.7,.8)` (ease-in). Exit: 0.97 s `(.6,.1,.4,.9)`. | V14 measures the boundary directly with 6 clean fits; V03/V15 agree (~1.0-1.2 s). V02 is Family A and the only short value. V07's 1.3-1.5 s comes from a cx track, a weaker proxy. |
| **Card entrance: overshoot spring vs fast ease-out** | springs 19-62% (V01, V02, V03) vs ≤ 3% fast ease-outs in V04, V06, V09, V10, V12, V13, V14, V15 | **Default = fast ease-out ≤ 3% overshoot** (C12). Spring = O9 for small objects only, peak ≤ 1.25×. | 14+ bezier-grade fits (rmse ≤ .04) favour the ease-out; V02 springs failed the rmse gate (.17-.20); V03's springs are early-family. |
| **Card entrance duration** | 0.33-0.47 s (V10 post card/toast/avatar/diamond, V15 product cards) vs 1.0-2.0 s (V04 panels, V06 ring, V12 hero, V13 post card 1.17 s / SaaS 2.0 s, V14 morph 1.17 s, V09 pill 1.23 s) | **Two tiers, same curve family**: secondary/supporting element 0.35-0.45 s; hero card or the reel's key artifact 1.0-1.5 s (2.0 s max for a card growing across the frame). | Both tiers are measured in several reels. The same post-card move is 0.37 s in V10 and 1.17 s in V13, so the duration encodes importance, not a different style [INF]. |
| **Caption height on A-roll** | V01 47-58%, V02 52-60%, V03 62-70%, V05/V06 55-63%, V07/V12 ≈ 62-70%, V14 62-66%, V15 chest-mid ≈ 49% | **Default y ≈ 60-64% H** (centre of caption block). Top band y 6-14% H on graphic scenes and for one oversized "contrast" line (V13). | Majority of Family B. Just below the face, above IG UI. ⚠EST |
| **Caption size** | Family A 2-3.4% cap · Family B 1.5% (+ script 2%) | **Family B: 1.5% / 2.0%.** Rishi may want larger for Hinglish readability (Phase 3 question). | 10 reels agree; small type is deliberate (V02 preaches "25% smaller") [INF]. |
| **Script word colour** | white on A-roll (11 reels); blue #397FF7 on A-roll (V02 only); navy-blue ≈ #2A5FA0 on cream [EST] | **White on dark grounds/A-roll; blue on cream.** | Majority; V02 is a lone outlier. |
| **Diamond badge position** | lower-left x ≈ 14-19%, y ≈ 58-63% H (V04, V09, V11 sometimes) vs centred (V10 50%/57%, V11 sometimes) | **Default lower-left** (x ≈ 16%, y ≈ 60% H); centred variant for story reels (V10). | More reels use lower-left; but centred is the only measured one, so position is ⚠EST. |
| **A-roll grade / wall colour** | navy/slate (#10519A, #001938-#063B66, #293C53, #323E49: V01-V04) · near-black (V05-V07) · teal-lit dark (V08-V10, V15) · lit grey/purple (V11-V13) · darkest (V14) | **Not an identity marker.** It follows the set/period. CORE is only: low-key, dark cool wall (L* < ~25), subject lit, crushed bottom third so white captions read. | 5 different grades across 15 reels [MEAS]; Rishi's own set decides (Phase 3). |
| **Grounds: ice/cream/grey (V01, V02, V04) vs #EBE7E1** | #E8F3F7, #FFFEFB, #C9D1D6 vs #EBE7E1 ×6 | **#EBE7E1 is the cream token**; the others are Family A variants. | 6 identical [MEAS] samples. |
| **Blue ground variants** | V05 #3062A8/#1E519B, V07 #204F98 (darker), V06/V12/V14 #427ABB→#205AA4 | **Token: #4279BB → #205AA4** | 3 reels match within a few levels [MEAS]. |
| **Sound on cuts vs on motion** | V15 0.33 hit rate, V04/V08/V14 0.0 | **Cuts dry by default; put cues on pane/card/typing events.** Optional cue on a chapter-opening cut (V15 pattern). | Median 0.18 [MEAS]; V14 3/6 pane moves have an onset within 3 f. |

---

## 3. Scene taxonomy & runtime shares
Shares are from each reel's §1 (mostly [EST] from cut lists + sheets).
| scene type | description | median share | range | present in |
|---|---|---|---|---|
| S1 A-roll (± small overlay) | speaker full frame; captions; may carry badge, counter, toast, strip behind head | **45%** | 26-60% (V04 88% incl. panels) | 15 |
| S2 Full-frame graphic scene | blue or cream ground + UI card(s)/text | **47%** | 9-73% | 15 |
| S3 Split screen | pane top ≈ 48%, A-roll bottom | **9%** (when used: 7-28%) | 0-28% | 9 |
| S4 Type-only beat | single word(s) on ground, no object | < 5% | — | V01, V12, V13, V14 |
| S5 Card wall / field | many cards, one in focus | inside S2 | — | 11 |

Scene-selection rules (condition → action → reason), merged from the 15 §10 tables [INF, recurring ≥ 3 reels]:
| condition in the script | scene | why |
|---|---|---|
| personal claim, opinion, chapter intro, CTA ask | S1 A-roll (+ diamond badge for chapters) | trust; face carries persuasion |
| abstract rule / definition while the speaker keeps talking | S3 split | speaker stays present while the idea is shown |
| a principle that can be shown | S2 demonstration (UI performs the rule) | show, don't tell |
| quantity ("hundreds", "12 brands", "$282,000 earned") | S2/S5 wall or counter | volume = credibility |
| a person/case | S2 their real post/profile card | verifiable identity |
| money/result | counter or toast, green | specific, checkable |
| deadline/scarcity | red ellipse on the word; text-only S4 near the end | the only red = urgency |
| question / verdict | S4 drum-roll or giant word | gives the beat its own frame |
| price | strikethrough → green new price (+ confetti); or hide it (pixelate) to drive comments | the subtraction is drawn |
| CTA | S1 + comment bar typing the keyword (+ tutorial card) | one literal action |

Structure templates by genre [OBS]:
- **Teach-a-rule**: hook (counted promise) → chapters 1..N (S1 + badge → S3/S2 demo, 7-13 s each) → recap → CTA.
- **Story**: hook (person + number) → steps on a timeline/diamonds, each with one artifact, escalating card count → climax proof (zoom) → deadline → CTA.
- **Offer**: proof counter at frame 0 → hidden/secret item → "what's inside" by ordinals → price drop drawn → deadline (red) → CTA.
- **AI-workflow**: hook question → each workflow step as real UI (typed prompt, chips) → result card → verdict word → CTA.

---

## 4. Merged animation library (named, with measured ranges)
Ranges list measured values first. Bezier only where rmse ≤ .05 (Q3 gate), otherwise "≈".
| name | what | duration | easing | key values | evidence / sources |
|---|---|---|---|---|---|
| **pane-drop** | split pane enters from top | 0.97-1.13 s (default 1.0) | `(.7,.1,.4,.9)` | boundary 0 → 48% H | [MEAS] V14 ×3 rmse ≤ .012; V02 433 ms `(.6,0,.3,1.05)` (Family A) |
| **pane-expand** | pane grows to near-full | 0.8-0.9 s | `(.7,0,.7,.8)` ease-in | 50 → 93% H | [MEAS] V14 ×2 |
| **pane-lift** (exit) | pane leaves upward / collapses | 0.6-0.97 s | `(.6,.1,.4,.9)`; V02 collapse ease-in `(1,0,.3,.9)` | 48 → 1% H | [MEAS] V14, V02 |
| **card-snap** | secondary card/toast/avatar wipes or slides in | 0.33-0.47 s | `(0,.9,0,1)` · `(.1,.9,.2,1.1)` · `(.5,.9,.4,1)` | width 5% → 76-90% W from left edge | [MEAS] V10 A01/A05/A11 rmse .017-.035, V15 A09/A14/A16 rmse .013-.014 |
| **hero-settle** | hero card rises/scales and settles | 1.0-1.53 s (2.0 s for cross-frame growth) | `(.1,1.4,0,.9)` · `(0,1.4,0,.9)` · `(.1,.9,0,1.1)` | scale 0.86 → 1, rise 40-60 px | [MEAS] V12 A12/A15 rmse .019-.021, V13 A07 .015-.037, V13 A12, V04 A10/A11 .03-.04 |
| **ring/badge pop** | circular or diamond marker pops | 0.43-0.9 s | `(0,.6,.2,.6)` (V10) · `(0,1.4,0,.9)` (V06) | 13 → 119 px src; ring to 22% W | [MEAS] V10 A07 .019, V06 A02 .023 |
| **price-pill rise** | price pill rises ahead of the word | 1.23 s | `(.1,.9,0,1)` | +59 px src rise | [MEAS] V09 A16 rmse .01 |
| **card→doc morph** | card reshapes into a document/UI | 1.17 s | `(.2,1.4,.6,.9)` | W +23%, H −32% | [MEAS] V14 A07 rmse .007-.01; V01 search-bar morph 467 ms `(.4,0,0,1.05)` |
| **footage→card** | A-roll shrinks into a card | 0.93-2.07 s | `(.2,.4,0,1)` / `(.5,0,0,1)` | to 41-63% H / 48% W | [MEAS] V01, V04 (≈ .089) |
| **counter-run** | numerals count up/down (ease-out), green at end | 1.0-2.0 s; price steps ≈ 0.5 s | easeOutExpo-like | starts ≤ 0 s before word; may be 41% done at frame 0 | [OBS] 2 fps values; ⚠EST curve |
| **red-ellipse** | hand-drawn loop around a word | 0.35-0.5 s | linear stroke | single red | [OBS] ⚠EST |
| **strike-arrow** | strikethrough + arrow to the new price | 0.25 s + 0.35 s → pop 0.47 s | pop `(.7,0,.2,1.1)` ≈ | ≈ 3% overshoot | V15 [OBS]; pop [MEAS ≈ rmse .101] |
| **blur-rise** | generic card entrance | 0.5-1.5 s | ease-out | blur 8-10 → 0 px, y +40-60 → 0 | ⚠EST (9 reels [OBS]) |
| **caption-word fade** | newest caption word fades in | 6-16 f | `(.2,0,0,.9)` | opacity .25 → 1 | [MEAS] V01 only; elsewhere ⚠EST "fade" |
| **script-wipe** | italic word reveals left→right | ≈ 0.3-0.8 s | ease-out | clip 0 → 100% | V13 A06 0.83 s [MEAS ≈]; V02 ⚠EST |
| **keyword-type** | comment bar grows + types keyword | bar 1.17-2.17 s; ≈ 0.25-0.3 s/char | bar `(.2,1.4,0,1)` ≈ | grows from right edge to centre | V06 A20 [MEAS ≈ .089], V12 A17 [≈] |
| **comment-sheet rise** | comments sheet rises | 0.37 s | ease-out ≈ `(.7,.6,.6,1)` | cy 65 → 73% H | V15 A21 [MEAS cy .048] |
| **card-wall** | field of 12-60 cards, slow drift, one focused | 1-4 s build | ease-out / linear drift | outer cards blurred | [OBS] |
| **carousel-step** | category card swap | step 1.5-1.8 s, dissolve 0.4 s | ease-in-out | 22% W cards | V12 [MEAS ≈] |
| **proof-zoom** | zoom into a detail | 0.87-2.7 s | ease-in-out / linear | 1.8-3.5× | V01 2.0× [MEAS]; V11 1.8× [MEAS ≈]; others ⚠EST |
| **spring-pop** (O9) | small object pops with overshoot | 0.47-0.67 s | `(.2,1.4,.2,1.1)` ≈ | peak 1.08-1.25× | V01 A24 [MEAS], V02 [MEAS peak ratio] |
| **drum-roll words** | single words hard-swapped on ground | ≈ 0.5 s/word | cut | last word script | [OBS] |

---

## 5. Caption & type rules (for the pack)
1. Two faces only: grotesque sans (Inter / SF Pro class) + italic high-contrast serif (Playfair-italic class). Fonts are unconfirmed in all 15 reels, so the pack must pick licensed equivalents [INF].
2. Per caption group: 1-4 words per line, max 2-3 lines; exactly **one** script word (the key noun, qualifier or emotional word). Numbers, money, keyword → **bold** sans.
3. Sizes (Family B): sans cap ≈ 1.5% H (≈ 29 px @1920), script ≈ 2.0% H (≈ 38 px). Exceptions: hook numeral 4.5-5% H; one oversized contrast line ≈ 4% H; giant verdict 12% H. ⚠EST
4. Positions: A-roll block centred at y ≈ 60-64% H; graphic scenes top band y ≈ 6-14% H; split screen → top of the pane or upper part of the lower pane. Never over the face. ⚠EST
5. Colours: white on dark/blue; on cream, navy body (#103D7B / #193452 [MEAS]) with blue script (≈ #2A5FA0 [EST]).
6. Captions disappear when the UI text *is* the content (chat, documents) and during wipe moments.
7. Entrance: per-word fade (6-16 f) or blur-fade; groups clear hard on the next phrase.
8. On-screen text follows speech exactly (typed prompts mirror the spoken line); on-screen spelling beats ASR.

## 6. Colour tokens
| token | hex | evidence |
|---|---|---|
| ground.blue.top | #4279BB (#427ABB/#4179BA/#4279BD) | [MEAS] V06, V12, V14 |
| ground.blue.bottom | #205AA4 | [MEAS] V06, V12, V14 |
| ground.blue.overlay | diagonal light rays + faint square grid | [OBS] 6 reels |
| ground.cream | #EBE7E1 | [MEAS] V08-V11, V13, V15 |
| ground.cream.corner | #E6E2DD | [MEAS] |
| card.white | #FDFDFD (V06) / #FFFFFF | [MEAS] |
| text.navy | #103D7B (V11) · #193452 (V08) | [MEAS] |
| accent.blue | #1E6CD9 (V08) · #397FF7 (V02) | [MEAS] |
| badge.blue | ≈ #2F80FF, highlight #65AFD5 (V04) | [EST] / [MEAS] |
| script.blue.on-cream | ≈ #2A5FA0 | [EST] |
| money.green | ≈ #2FD26B / #4CE38B / #1FA463 | [EST] — Phase 4 should pick one |
| scarcity.red | ≈ #E83A3A | [EST] |
| shadow | soft, ≈ 20-30 px src blur, low opacity, no border | [EST] |
| A-roll | dark cool wall, crushed bottom third | [MEAS] per reel; varies (see §2) |
Rules: one accent blue per scene; green = money/good only; red = scarcity/negation only; no glows in Family B (glow = Family A).

## 7. Sound-cue patterns (measured statistics only; no sound is named)
| metric | median | range | source |
|---|---|---|---|
| strong onsets per second | ≈ 0.42 | 0.29 (V10) – 0.58 (V06) | [MEAS] audio.json |
| cut↔onset hit rate (≤ 100 ms) | ≈ 0.18 | 0.0 (V04, V08, V14) – 0.33 (V15) | [MEAS] |
| cue length | ≈ 590 ms | 571-604 ms (V02 578) | [MEAS] |
| cue attack | ≈ 226 ms | 104 (V02) – 447 ms (V13) | [MEAS] |
| spectral centroid | ≈ 2.4 kHz | 2.2-2.7 kHz | [MEAS] |
| peak | ≈ −3 dBFS | −2.1 to −4.1 | [MEAS] |
| bed rms p10 / p50 / p90 | −30.4 / −19.6 / −13.2 dB | ±1.5 dB across reels | [MEAS]; "music" [EST] |
Patterns: onsets coincide with in-scene events (pane move ±3 f in V14 3/6; panel entrances ±15 f in V04 9/21; counter start ±4 f in V07/V09/V15); CTA typing gets a cluster of onsets (V13: 5 in the last 2.5 s) [MEAS]. Long-attack onsets often begin before a move (swell-like [INF]). What the sounds are (whoosh, click, pop) is **unverified** in every reel.

---

## 8. CORE rules resting only on [EST] (verify in the pilot)
C5 caption sizes · C6 caption positions · C9 diamond position/entrance (except V10) · C11 typing speed · C14 visual-change counts · C16 green/red hexes · C17 blur-rise values · caption-word fade outside V01 · counter curve shape · red-ellipse draw time. Cheap fixes if needed later: measure cap height and y on 3 Family-B frames per reel (frame.sh + numpy), sample green/red pixels on V15 f-frames, and run track.py on one blur-rise card with the sharpness column.

## 9. Gaps
- Native strips not viewed for V03-V15 (0-2 per reel) → any timing below ~0.5 s outside the measured CSVs is approximate.
- Fonts unconfirmed in all reels (creator-named fonts in V04/V08 are statements, not measurements).
- No glow, blur, shadow or corner radius is measured anywhere (Q12 unmet series-wide).
- Music vs SFX not separated; no sound type verified.
- Caption word-entrance timing is measured only in V01 (Family A).
- Weak reels (V05-V09, V11) contribute mostly [OBS]/[EST]; they support *which* moves exist and how often, not their exact curves.
- Family A vs B: assumed to be an earlier vs later period of the same creator [INF]; Rishi should confirm which to follow.

## 10. Questions this raises for Phase 3 (Stage 0)
1. Follow Family B (flat white UI, blue/cream grounds) only, or allow Family A glow/glass as an occasional accent?
2. Caption size: keep 1.5% H or go larger for Hinglish readability?
3. Ground: one per reel (blue or cream), or a fixed gradnext choice?
4. Which reel genres will Rishi make (teach / story / offer / AI-workflow)? This sets the scene vocabulary.
5. CTA: always "comment KEYWORD"?
