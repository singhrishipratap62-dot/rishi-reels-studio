# Motion library: Rishi v2

> Smoothness is the brand. When in doubt, make it longer and softer. Values are what Rishi approved; adjust per video. Helpers live in `engine/build_template.py` (`reveal`, `exit_`, `rise`, `blurfx`, `wrapclip`).

## Easing curves
| Name | cubic-bezier | Use |
|---|---|---|
| `E1` soft ease-out | (0.22, 1, 0.36, 1) | entrances, word rises, glides |
| `ES` smooth in-out | (0.45, 0.05, 0.2, 1) | big moves: shrinks, zooms, PiP, pane, line→rect |
| `EX` smooth exit | (0.55, 0, 0.75, 0.4) | exits |
| hold | step | text typing, key states |
Never linear for motion (only for constant drifts and playheads). No overshoot or bounce.

## Motions
| ID | Name | Values | Use | Tag |
|---|---|---|---|---|
| R01 | **Line → rectangle reveal** | scaleY 3 → 100 % and scaleX 96 → 100 % (ES) over 0.6–0.7 s; opacity 0 → 100 in the first 35 %; rise 40 px (ES); blur 18 → 0 over 90 % | **every card** (result, doc, timeline, PiP card) | [R] |
| R02 | Slide-blur exit | translate (left −300…−720 px or up −40…−60 px) + opacity → 0 + blur 0 → 14 px, 0.42–0.6 s, EX | cards and contents leaving | [R] |
| R03 | Word rise | +26 px → 0 + fade, 0.5 s, E1; stagger 0.08–0.15 s | support captions, list rows, doc lines, step labels | [ME][R] |
| R04 | Hero letter build | see CAPTION_SYSTEM §3 | caption heroes | [ME] |
| R05 | Shrink into UI | wrap the clip in a group; scale 100 → 23.5 %, move to the target over 1.28 s (ES); card behind settles 94 → 100 % + fade 0.5 s | hook: face → chat attachment | [R] |
| R06 | Slide-out from behind the head | from (540, 660) at 62 % scale → corner target over 0.6 s (ES), fade in 0.12 s; track matte lumaInverted | opening logo + video card | [R] |
| R07 | Logo slow spin | rotation 6·sin(2πt/3) degrees (±6° over 3 s) | Claude logo while visible | [R] |
| R08 | Pane drop / lift | ice pane y −940 → 0 over 1.0 s (ES); A-roll shifts down 460 px in sync; lift 0.7 s (EX) | split screen | [R] |
| R09 | Card stagger in | each card: rise 34 px + blur 10 → 0 over 0.55 s; next card +0.18 s (only after the pane has landed) | skill-card grid | [R] |
| R10 | Glide from the right | x +820 → 0 over 0.75 s (E1) + fade 0.3 s, +0.2 s stagger | repo cards, pipeline card | [R] |
| R11 | Orbit, fast → slow | θ = phase + 2π(1.1(1 − e^(−t/0.9)) + 0.05t); ellipse 205×150; opacity fades in over 0.5 s then 55–100 % with depth | words around the blob | [R] |
| R12 | Blob paint-in | scale 72 → 100 % (ES 0.68 s) + fade 0.38 s + blur 18 → 0; idle rotation 3·sin(1.2t) | organic figure | [R] |
| R13 | B&W nose-track | saturation −100 + scale 110 % (+0.8 %/s); position follows the nose (0.3× offset, 0.13 s lag) + 4 px sine wiggle; eases back to 100 % over 1 s | reaction / "no" beat | [PS][R] |
| R14 | Cut-hiding zoom | 100 → 112 % over 0.7 s (ES) **across** the jump cut, slow push after, ease back to 100 % before the next scene | hides jump cuts | [R] |
| R15 | Wall zoom-out | camera group scale 360 → 100 % over 1.45 s (ES) with the face tile as anchor, then 100 → 102.5 % drift; starts **exactly on the trigger word** and holds | "all the slop" contrast | [R] |
| R16 | PiP in / out | scale 100 → 32 % + move over 0.9 s (ES); out 32 → 100 % over 0.8 s (ES), only after the line ends | explanation beats | [R] |
| R17 | Contents swap | old contents R02 left (−300 px); new rows R03 word by word, 0.15 s apart; the card itself stays | changing lists inside one card | [R] |
| R18 | Progress fill | scaleX 3 → 100 % over 1.0 s (ES), "100%" fades in after | "samajh gaya" style completion | [R] |
| R19 | Sheet rise | sheet + keyboard y +1000 → 0 over 0.8 s (E1); face y −400 + blur 0 → 24 + dim 45 % over 0.8 s; held to the last frame, slides out in the final 0.35 s | CTA | [R] |
| R20 | Tap + success | soft white dot (96 px, blur 6, 55 %) scale 55 → 125 % + fade over 0.5 s; button blue → green (0.16 s); arrow → tick | send press | [R] |
| R21 | Key press | lit key + pop-up bubble with an enlarged letter for 0.18 s; ≈0.2 s per letter | keyboard typing | [S] |
| R22 | Typing | textContent hold-steps across the spoken window (≈0.45 s for 20 chars) | prompt in the chat | [RES] |
| R23 | Highlighter swipe | scaleX 0 → 100 % over 0.2 s from the left | prompt emphasis | [DP] |
| R24 | Slop tile breathe | white sweep overlay opacity 50 ± 50 % at 0.9 rad/s, phase per tile | "moving gradient" on tiles | [R] |
| R25 | A-roll slow push | +1.2 %/s on plain A-roll shots (punch framings may hold) | all A-roll | [ME] |

## v2.1 additions: Style Lab v1 picks (2026-11-09) `[R]`
> Demos: `<studio root>/03. Projects/Rishi Style v2/style_lab_v1/index.html` (picked) and `<studio root>/03. Projects/Rishi Style v2/style_lab_v2/index.html` (revised per notes). "Keep" = approved default or option; "Maybe" = option pool only.

### Upgrades to existing motions (Keep, now the default)
| ID | Change | Values |
|---|---|---|
| R01+ | **Shadow grows with the card** | shadow 0 → `0 14 30 rgba(11,18,36,.16)` (up to `0 28 60 /.30` on hero cards) over the same 0.65 s ES. Blur only on entry (18 → 0) and on the R02 exit, never while held |
| R02+ | **Directional continuity** | the next element enters from the side the old one left toward: old exits left −720 px; new enters x +720 → 0, 0.75 s E1 + blur 10 → 0, starting 0.1 s into the exit |
| R03+ | **Eased stagger** | list gaps shrink as the list goes: 0.20, 0.15, 0.12, 0.10, 0.08 s (then 0.08) |
| R05+/R16+ | **Motion blur on big moves** | blur 0 → 6 px → 0, peak at 50 % of the move (shrinks, PiP in/out) |
| C-out | **Captions leave softly** | old group opacity → 0 + blur 6 px + up 10 px in 0.18 s EX, overlapping the next group's R03 (replaces the hard cut) |
| (Maybe) | Soft landing | after a big move: extra 4 px / 101 → 100 % over 0.4 s E1. Try sometimes, not default |

### New card entrances (all Keep; A–C are his favourites)
| ID | Name | Values | Note |
|---|---|---|---|
| R26 | Feathered wipe down | gradient mask (black 40 % → clear 60 %, 250 % tall) travels top → bottom 0.85 s ES + rise 15 px | top-3 |
| R27 | Pill grows into the card | pill (logo + name) blur-in 0.4 s E1 → width 0.5 s ES → height 0.6 s ES (overlap 0.2 s), corner 4.5 → 3 cqw; pill = card header | top-3 |
| R28 | Frosted glass condenses | glass (blurred A-roll copy + 12 % white) → solid white 0.9 s ES, text blur 10 → 0. **Place it low: bottom half, over the hand and the bottom gradient** | |
| R29 | Deck settles (fan in) | 3 cards, **anchor = centre of the bottom edge**; start fanned wide (−22°, 0°, +22°), rotate inward to a still-visible fan (−7°, 0°, +7°) over 0.9 s ES, fade + blur 10 → 0, 0.12 s stagger. Never collapse fully | |
| R30 | Tilt up into place | rotateX 28° → 0 from the bottom edge + rise 8 % + blur 14 → 0, 0.85 s ES (fake: scaleY + skew if no 3D) | as is |

### Transitions face ↔ graphic
| ID | Name | Values | Status |
|---|---|---|---|
| R08+ | Pane drop | as R08, but the face shift must keep the **full hair line visible** below the pane | Keep |
| R31 | Parallax lift | face y 0 → −70 % 1.0 s ES; ground y 100 → 0 % 1.2 s ES, +0.1 s; content R03 after | Keep (as is) |
| R32 | Blob wipe from the head | blob scale 5 → 900 % from behind the head, 1.1 s ES. **Outro = R31 parallax lift (ground slides down/away), not the blob shrinking back** | Keep |
| R33 | Soft light sweep | soft white band (70 % wide, 18°, blur) x −150 → 250 %, 0.9 s ES; scene swaps under the peak with a 0.12 s cross | Keep |
| R34 | Rack focus (bottom) | card in the **bottom half**; only the bottom half blurs (12 px) + darkens with the gradient; the face stays sharp | Maybe |
| — | Zoom through a window | animation rejected; its **coarse grain texture** went into DESIGN_SYSTEM | Maybe (texture: Keep) |

### Emphasis
| ID | Name | Values | Status |
|---|---|---|---|
| R35 | Number roll-up | odometer strips 1.4 s ES (ones roll further). **Number in Inter Bold, the word ("drafts tak") in Playfair** | Keep |
| R36 | Hand-drawn circle | loose ring path trim 0.7 s ES, starts as the hero finishes, white 2.2 px on A-roll | Keep |
| R37 | Echo stack | hero + 2 copies above at 40 / 15 %, R03 rise 0.7 s, 0.18 s apart (bottom copy first) | Keep |
| R38 | Spotlight one card | veil 0 → 55 % 0.6 s ES, chosen card scale 107 % + blue glow shadow. **Variant R38b:** side cards slide in from the left/right edges, centre card rises from below, they align, then the spotlight | Keep |
| — | Strike then replace | rejected | No |

### Behind the head (needs the matte)
| ID | Name | Values | Status |
|---|---|---|---|
| R39 | Screens fan out | 3 screens appear **together** behind the head, then split. **Current values (vid5, 2026-11-10, supersede v2.1's rise 0.5 s / ±16° / split 0.8 s):** screen tops ≈ y 180 (not ≈70), spread ±255 px / ±12°, rise 0.7 s + split 1.1 s (ES). Optional blur on the screens only when a later reveal is pending | Keep |
| R40 | Horizon arc | arc rises behind the head, **its top just above the hair**; dots light 0.25 s apart; **labels above the dots** | Keep (only with headroom) |
| R41 | Giant word behind | Playfair 3× hero size, drift 1.2 %/s. **vid5 (2026-11-10):** at 360 px the baseline must be ≈ y 445 and the rise ≤0.7 s, or the head hides the middle letter and the word never lands before the next scene | Maybe: only if the frame has room to read the word |
| R11+ | Words orbit through | orbit **fast → slow** (R11 curve), behind = smaller + 55 % | Maybe: only with room |

### Proof, chrome and ambient life
| ID | Name | Values | Status |
|---|---|---|---|
| R42 | Line graph draws | path trim 1.2 s ES, end dot, label **above the line end**, never on it | Keep |
| R43 | Before / after wipe | divider 10 → 90 %, 1.6 s ES (speed approved) | Keep |
| R44 | Counting stats | count 1.2 s ES; numbers **Inter** (or Playfair roman, never italic), labels Playfair roman or Inter | Keep |
| R45 | Comments rise | bubbles rise 30 px + blur → 0, 0.6 s E1, 0.35 s apart; real avatars when Rishi supplies them; variant inside a phone mock-up | Keep |
| R46 | Cursor guide | cursor glide 1.0 s ES → click: R20 tap ring, button → green | Keep |
| R47 | Gentle float | y ±8 px, 4 s sine, phase per card | Keep |
| R48 | Light sheen | band x −100 → 200 %, 1.1 s ES every 3 s, 35–80 % white | Keep |
| R49 | Breathing shadow | shadow 30 ↔ 54 px blur, 14 ↔ 24 px y, 5 s sine. **Combo R48 + R49 allowed** | Keep |
| R50 | Living grain | re-seed 12 fps + exposure ±2 %, 4 s sine | Keep |
| — | Chapter marker | rejected | No |
