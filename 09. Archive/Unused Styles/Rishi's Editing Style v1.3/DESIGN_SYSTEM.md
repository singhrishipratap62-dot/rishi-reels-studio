# DESIGN_SYSTEM — Rishi's Editing Style v1.3 (Ink blue + Editorial serif captions, [R1.3])

> **Status: working starting point, not final.** Rishi chose Ink blue + Editorial serif (2026-11-06) and said it is "still not exactly like that": the first real video and his feedback will define the final system. Every value in §3-§4 is a first guess to be corrected through `[R1.x]` notes in LESSONS_LEARNED. Motion, layout, components and scene logic (§2, §5-§8) still come from the 15 reference reels.

Sources: SYNTHESIS.md (15 reference reels) + DECISIONS.md `[R1.0]`. Evidence tags: [MEAS]/[OBS]/[EST]/[INF] refer to the reference measurements; `[R1.0]` = Rishi's decision. Values marked *proposed* are to be confirmed in the pilot.

## 1. Philosophy
- **The speaker persuades; the UI proves.** Every claim is followed (or preceded) by an artifact the viewer could check: a post, a profile, a payout toast, a price, a typed prompt.
- **Show the rule performed, don't just state it.** If the script says "make it 25% smaller", the icon shrinks 25% on screen.
- **Calm, premium surface; busy information.** Flat cards, one accent, small set of moves repeated, with many changes of content.
- **Volume = credibility.** Quantity claims become walls of cards or running counters.

## 2. Canvas & safe zone
| item | value |
|---|---|
| frame | 1080 × 1920, 30 fps `[R1.0]` |
| text safe | y 250-1500, x 64-920 (right icon column clear) `[R1.0]` |
| side margin | ≈ 64px [EST from reference layouts] |
| split seam | y ≈ 922 (48% H) [MEAS V14] |
| A-roll caption block centre | y ≈ 1150-1230 (60-64% H) [EST] |
| graphic-scene caption band | y ≈ 260-420 (reference used 6-14% H; moved below the 250px safe line) [INF] |

## 3. Colour tokens — Ink blue `[R1.3]`
Palette chosen from four options. Hex values are the options Rishi saw; roles marked *proposed* are my additions to be tuned in the first video.
| token | hex | role |
|---|---|---|
| `ground.ink` | `#0B1224` | dark graphic ground; heavy beats (verdict, deadline, drum-roll words) |
| `ground.ice` | `#EAF0F8` | light graphic ground; proof, demo and UI-card scenes |
| `surface.ink` | `#18264A` | raised surface on ink: panels, speaker-silhouette stand-in |
| `card.dark` | `#121C38` | dark cards: Comments sheet, toasts *proposed* |
| `card.white` | `#FFFFFF` | UI cards on ice; soft shadow `rgba(11,18,36,.18)` blur ≈ 28px |
| `text.on-ink` | `#F2F6FC` | all text on ink and on A-roll |
| `text.on-ice` | `#0B1730` | text on ice and on white cards |
| `text.muted.on-ink` / `.on-ice` | `#9AA8C7` / `#4A5878` | support text, UI micro text *proposed* |
| `accent.blue` | `#3E7BFA` | **the one accent**: key word on ice, chapter badge, send button, active states, glows (35% alpha) |
| `hairline` | `#F2F6FC1F` on ink · `#0B17301F` on ice | dividers, card outlines *proposed* |
| `money.green` | `#2FD08A` | money, payouts, final counter value only *proposed* |
| `scarcity.red` | `#E5484D` | hand-drawn ellipse / strike / arrow only *proposed* |
| `claude.orange` | `#D97757` | Claude asterisk on Claude UI cards only (kept from the references) |
Rules: one ground per scene; one accent per frame (blue); green only for money; red only for scarcity or negation; white cards on ice, `card.dark` on ink. The heavy ink ground replaces the reference's blue ground, ice replaces cream. Text never goes below `#F2F6FC` contrast on ink.

## 4. Typography and captions — Editorial serif `[R1.3]`
Fonts: **Playfair Display Bold Italic** (hero) + **Inter** (everything else). Both are variable fonts in `assets/fonts/` (`PlayfairDisplay-Italic-Variable.ttf`, `Inter-Variable.ttf`, copied from Creative OS → Asset Library; the weight axis gives Bold Italic, Medium, Bold). No download needed.
| style | font | size @1080w | colour | use |
|---|---|---|---|---|
| caption hero | Playfair Display Bold Italic, lowercase | 132px, width ≤ 740px (shrink to fit) | `text.on-ink` (on A-roll); `accent.blue` for the key word on ice | the meaning word of each group, centred |
| caption support | Inter Medium | 48px (≈ 36% of hero) | `text.on-ink`, 80% opacity | 1-4 small words around the hero |
| verdict hero | Playfair Display Bold Italic | 180-220px | `text.on-ink` | single word / phrase on ink ("nahi", "like that") |
| big number | Inter Bold | 120-160px, tabular | `text.on-ink` (`money.green` for money) | counters, prices |
| UI micro text | Inter Regular/Medium | 18-30px | `text.muted.*` | inside recreated cards |
| ghost word | Inter Bold | ≈ 120px, 15% opacity | `text.on-ink` | "Step one" behind a badge |
**Caption build** (Minimal Editorial rules Rishi approved on an earlier edit, `Minimal Edit Style/LESSONS_LEARNED.md` §2-§4; a starting point here):
- ≤ 5 words per group; the hero is the meaning word, lowercase serif italic, centred; **never a whole line at once**.
- Support above the hero, inset ≈ 7% of the hero width from its **left** edge; support below, inset from its **right** edge, ≈ 58px under the baseline (74px if the hero ends in g, j, p, q, y or a comma).
- Support words reveal **word by word** on their spoken times: rise 22px → 0 over 420 ms, opacity over 380 ms, `cubic-bezier(.22,1,.36,1)`.
- The hero reveals **character by character, left → right**: each glyph slides 28px over 380 ms, blur 10 → 0 over 300 ms, opacity over 240 ms; stagger = spoken length ÷ glyph count, clamped 12-48 ms. Finish ≥ 350 ms before the group cuts.
- Position: **below the face**, hero baseline roughly y 1250-1500 inside the safe zone; the analyse gate measures the face and sets the exact line. Graphic scenes: top band (y 260-420), same type.
- Hinglish: Roman script only; the hero may be a Hindi word; helper verbs and particles stay in the small support; never split compound verbs; numbers stay digits.

## 3b. Reference colour values (superseded by §3; kept for lookup)
Copied from the reference reels (SYNTHESIS §6 + re-viewed sheets V14/V10/V15). No rishi.docx token is used.
| token | hex | role |
|---|---|---|
| `ground.blue` | `#4279BB` (top) → `#205AA4` (bottom), soft vertical light streaks, very faint grid | default graphic ground for AI/tool, offer and teach reels (V05-V07, V12, V14) [MEAS] |
| `ground.cream` | `#EBE7E1`, corner `#E6E2DD`, faint grid, soft radial vignette | story/case and design reels (V08-V11, V13, V15) [MEAS] |
| `ui.claude.cream` | `#F4F2EC` | Claude chat UI screens only (V03/V05) [MEAS] |
| `card.white` | `#FFFFFF`, soft shadow, radius ≈ 4% of card width | every UI card |
| `card.dark` | `≈#1E1E1E` at ~90% (glass-dark) | Comments sheet, toasts, product/repo cards [EST] |
| `caption.white` / `caption.unspoken` | `#FFFFFF` / `≈#8E8E8E` | A-roll and blue-ground captions; words grey until spoken [OBS V10/V14] |
| `text.dark` / `text.navy` | `≈#1B1B1F` / `#103D7B` · `#193452` | text on cream [MEAS V08/V11] |
| `script.navy-blue` | `≈#2A5FA0` | italic serif word on cream [EST] |
| `badge.blue` | `≈#2F80FF` (gradient to lighter top), highlight `#65AFD5` | diamond badge, send button, glyphs in icon tiles [EST / MEAS V04] |
| `claude.orange` | `≈#D97757` | Claude asterisk on Claude UI cards and tiles [EST] |
| `scarcity.red` | `≈#E83A3A` | hand-drawn ellipse / strike only [EST] |
| `money.green` | `≈#2FD26B` | prices, payouts, counters' final value [EST] |
| `shadow.card` | soft, ≈ 20-30 px src blur, low opacity, no border | under white cards [EST] |
Rules: one ground per scene; white UI cards on either ground; red only for scarcity/negation; green only for money; no glows/glass in the default style (Family A = experimental).

## 4b. Reference typography and caption build (superseded by §4)
Fonts in the references are unconfirmed; stand-ins: **Inter** (grotesque) and **Playfair Display Italic** (high-contrast italic serif).
| style | font | size @1080w | colour | use |
|---|---|---|---|---|
| caption connector | Inter Medium | ≈ 30-34px | white (grey until spoken) | small words: "My last", "have been", "they took" |
| caption key word | Inter Bold | ≈ 44-50px | white | content words, numbers, money |
| caption italic | Playfair Display Italic | ≈ 54-60px | white on dark/blue; navy-blue on cream | one emotional/key word per group |
| cream-scene caption | Inter Medium + Playfair Italic | ≈ 34 / 44px | `#1B1B1F` + `#2A5FA0` | top band on cream |
| pane caption | Inter Medium + Playfair Italic | ≈ 30 / 38px | white | top of the blue pane ("Editing a video is like *building* software") |
| drum-roll word | Inter SemiBold / Playfair Italic | ≈ 64 / 80px | white | single words on full blue |
| big number | Inter Bold | ≈ 120-160px | white (green for money) | "458", "$3,000" |
| ghost word | Inter Bold | ≈ 120px, ~15% opacity | white | "Step One" behind the diamond |
| UI micro text | Inter Regular/Medium | 18-30px | grey/dark | inside recreated UI |
Caption build: words appear grey and turn white on the spoken word; lines stack (new line under the last), mixed sizes on one line, 2-4 lines per group, then clear.

## 5. Textures & materials
- **v1.3 default**: flat ink / ice grounds, grain 0.8 on light and 1.0 on dark (size 1.6) plus a soft vignette (Minimal Editorial values, `[INF]` here); no grid or light streaks unless Rishi asks.
- Reference grounds (superseded) carried a faint square grid (2px lines at ~5% opacity, ≈ 64px pitch [EST]) and a very soft radial vignette (corners ≈ 3% darker [MEAS ref: #EBE7E1 → #E6E2DD]).
- Cards are flat with a soft shadow. Corner radius: cards ≈ 4% of card width; UI recreations (phones, chats, Comments sheet) ≈ 28-34px; pills fully rounded [EST]. Cards enter blurred (≈ 8-10px → 0) and A-roll defocuses under floating cards [OBS V05/V10/V14].
- A-roll: real footage, dark and low-key wall behind the subject, bottom third dark enough for white captions (add a 0→40% black gradient over the bottom 35% if needed [INF]).

## 6. Layout system
| frame type | layout |
|---|---|
| **A-roll** | speaker full frame; caption block centred at y ≈ 1190; optional overlays: chapter badge + title (lower-left, replaces captions for that beat), counter/toast above the shoulder line, reel-card strip behind the head |
| **Split** | graphic pane y 0-922 (blue or cream ground), A-roll y 922-1920 (pushed down, face kept in frame); captions in the upper part of the lower pane or at the top of the pane |
| **Full graphic** | ground + 1 hero card (60-90% W, centred, y 500-1300) + top caption band; supporting cards at the sides |
| **Type beat** | ground only; 1-3 words centred, or giant word |
| **Wall** | 12-60 cards in a grid/field, outer ones blurred 6-8px [EST], one focus card |

## 7. Components
| component | spec |
|---|---|
| **Chapter diamond badge** | rotated rounded square, ≈ 120px (11% W) lower-left at x ≈ 170, y ≈ 1150; or 178px (16.5% W) centred at (540, 1095) for story reels [MEAS V10]. Fill `badge.blue` gradient with soft glow, white Inter Bold numeral [OBS V10]. Title right of it (lower-left) or below it (centred). Optional ghost word ("Step 2") behind at 8% opacity [OBS V08/V10]. |
| **1-2-3 tracker** | 3 circles joined by a line, under the captions (y ≈ 1270); active one filled; line draws 0.8 s [MEAS V02] |
| **Post / profile card** | white, radius 28px, avatar + name + text in UI micro type; real content from Rishi's or the subject's account (recreated) |
| **Toast** | dark `card.dark` pill-card, icon left, amount in green; slides in from the left |
| **Comments sheet** | dark glass sheet `card.dark` rising from the bottom: "Comments" title, dark input pill with avatar, keyword types in, blue round send button press [OBS V13/V15] |
| **Counter** | Inter Bold numerals, tabular figures, white; turns green on the final value (money) |
| **Pen marks** | `scarcity.red`, hand-drawn ellipse / strike / arrow, only for scarcity or negation |
| **Leader-line label** | `line.strong` 4px line + 32px label |
| **Price pill** | rounded pill, price in green, rises ahead of the spoken number |
| **Tutorial / product card** | landscape thumbnail card, radius 4% W, rises from bottom |
| **Reel-card strip** | row of 9:16 thumbnails behind the speaker's head, scrolling 1 card / 1-1.5 s |

## 8. Scene list
A-roll · Split · Full graphic (demo / proof / UI step) · Type beat (drum-roll, verdict, deadline) · Wall/field · Counter-over-speaker. Details and genre recipes: SCENE_PRINCIPLES.md.

## 9. Core vs optional (from SYNTHESIS)
- **CORE**: A-roll ↔ graphic alternation; one ground per scene; UI cards as proof; caption system; quantity → wall; rule → literal demo; numbered chapters; split pane; ease-out card grammar; mostly-dry cuts; front-loaded pacing; proof on/before the word; accent discipline.
- **OPTIONAL**: footage→card opener, counter, red ellipse/strike, carousel, defocus bridge, proof zoom, tutorial card, typed prompt, spring pop, reel strip, drum-roll words, giant word, pixelated hidden item, confetti, leader lines, cursor.
- **SIGNATURE** (Rishi-requested `[R1.2]`, rationed, specced in `DEPTH_AND_ORBIT.md`): orbit ring, cylinder carousel, hologram icons, graphics behind the subject (needs a person matte), 3D post push.
- **EXPERIMENTAL** (off by default): glass/glow panels, font-cycle word, flicker title, gradient type-on, countdown ring, percentage ring, particles, iris wipe.
