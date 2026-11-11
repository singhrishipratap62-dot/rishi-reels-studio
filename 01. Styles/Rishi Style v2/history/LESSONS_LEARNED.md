# Lessons learned: Rishi v2 (append after every round)

> **History (v2.2, 2026-11-11):** fully compiled into `../SKILL.md` and `../reference/`; where each item now lives is in `RULE_AUDIT.md`. Kept for the why, not as a mandatory read.

Format: `- YYYY-MM-DD · <edit> · <round> · what Rishi changed → rule for next time`

## roughcut_v3 (Claude edits video only once you teach it your taste)
- 2026-11-08 · roughcut_v3 · draft 1 (Paper Stage) · "not as good as I aimed": the Paper Stage look was too generic → start from an options board mixing several style books, not one style.
- 2026-11-08 · roughcut_v3 · process · Claude created a Motion artifact; Rishi deleted it: "We never create an artifact" → local HTML only; build in Tesseract.
- 2026-11-08 · roughcut_v3 · process · Asked for storyboards and questions as HTML he can open, not text → REVIEW_FORMATS.md.
- 2026-11-08 · roughcut_v3 · options board · Picked mixes per frame (e.g. "B baseline + some of A and C") → always 5 options per frame type; build the exact mix.
- 2026-11-08 · roughcut_v3 · captions · Romanised Hinglish exactly as spoken; serif hero + gradient, no blue → CAPTION_SYSTEM.md.
- 2026-11-08 · roughcut_v3 · assets · Download real logos and keep them in assets/logos for reuse; use his face sticker as the avatar.
- 2026-11-08 · roughcut_v3 · draft 2 → 3 (28 points) · "not smooth" everywhere; pops disliked; Playfair glyph glitch; wanted the line → rectangle reveal; B&W tracking from the cut; split captions in the white area; white slop tiles; PiP with the headspace cropped; green tick on send; longer swooshes → MOTION_LIBRARY R01–R25.
- 2026-11-09 · roughcut_v3 · storyboard 3 notes · The face pushed too low in the split → middle ground (hair line just below the pane); circle → organic blob + more orbit words; drawn oval gap read as real → label mock-ups as sketches.
- 2026-11-09 · roughcut_v3 · draft 3 → 4 · Opening: logo + video slide out from behind the head (lower, white disc, shadow); slow logo spin; captions only slightly higher; wall one-word black Playfair in the tile below; rounded PiP video; same card, contents swap; return after "intervention"; one-word CTA captions; keyboard held to the end.
- 2026-11-09 · roughcut_v3 · "a little" → move ≈30 px, not 120 px (over-correction was flagged).
- 2026-11-09 · roughcut_v3 · deliverables · Asked for SFX-only + voice-only MP3s → fx_check.py --mp3.
- 2026-11-09 · roughcut_v3 · export · "Final video at all times 1080p" → never 720p, even for check renders.
- 2026-11-09 · process · Feasibility of a GUI editor: approve phase by phase; drop anything that takes more than 2–3 minutes to decide.

## vid2 (very short reel: "maine ye poori video claude se edit ki hai")
- 2026-11-09 · vid2 · options board · Head/tail trim marked "No" to both options with "use auto edit and remove this, very basic" → don't ask about silence/unclear-sound trims; just cut them (silencedetect + cut on a quiet frame) and report it.
- 2026-11-09 · vid2 · options board · SRT had a mis-heard word ("slow" was "slop") → treat the SRT as a draft; flag words that change the meaning.
- 2026-11-09 · vid2 · options board · New approved element: a reel timer (subtle 12 px corners, from behind the head → corner, ring + countdown held for the whole reel, label words rise + fade on the move).
- 2026-11-09 · vid2 · options board · Real past drafts as proof of effort ("hafte ya mahine") + real skill-file cards with a small GitHub mark → reuse "show the real work" for effort beats.
- 2026-11-09 · vid2 · captions · Repeated phrases with one changed word ("seekhni hai, samajhni hai,") → keep the support line and swap only the hero word.
- 2026-11-09 · vid2 · CTA · DM "resource" card enters on the green tick, middle of the screen, left → right, just above the one-word caption.
- 2026-11-09 · vid2 · build · The SRT's Devanagari uses precomposed nukta letters (U+095B); match roman_map keys by NFD. Caption-mode boundaries must sit a little before word starts (5.587 vs 5.59 fell into the wrong mode).

## Style Lab v1 (pack upgrade, no video)
- 2026-11-09 · style lab · Animated looping tiles worked for reviewing motion; he kept most options → future boards re-offer every liked option, even past 5 (D24).
- 2026-11-09 · style lab · Support word under the hero sat too far below → keep the lower support line tight (+0.55 × size).
- 2026-11-09 · style lab · Graphics on the A-roll go **low** (bottom half, over the hand/gradient), and blur only the bottom half; the face stays sharp and the hair line visible.
- 2026-11-09 · style lab · Labels must never sit on lines or dots (v4 on the graph, v1–v4 on the arc) → put them above.
- 2026-11-09 · style lab · Deck: anchor rotation on the bottom-centre, fan in from wide to a still-visible fan; fan-out screens appear together, then split.
- 2026-11-09 · style lab · A transition's outro should be a calm move (parallax), not the intro reversed (blob shrink).
- 2026-11-09 · style lab · Liked a by-product: the coarse grain of a scaled-up scene → watch for accidental textures he likes and name them.
- 2026-11-09 · style lab · Voice notes mis-transcribe: "Enter" = Inter, "sea" = C, "deep" = D, "ice + green" = ice + grain, "wallpaper" = warm paper.

## vid5 ("at this point aap claude se kisi bhi tarah ke editing style banwa sakte ho")
- 2026-11-10 · vid5 · intake · Rishi: "I would suggest you not remove it" (0.7 s pause before "wow!") → a pause that carries a joke or a beat is not dead air; only cut silence that does nothing, and say which pauses you kept.
- 2026-11-10 · vid5 · options board · Behind-the-head fan "getting a lot out of the frame … bring it down a little notch" → fan screens' tops ≈ y 180 (not ≈70), spread ±255 px / ±12°, rise 0.7 s + split 1.1 s.
- 2026-11-10 · vid5 · options board · Mixes again: arc + a smaller timeline card inside it; split pane + macOS dock / liquid glass with big real icons; PiP card + 2–3 GitHub doc cards under it; progress bar *below* the card, after the rows → build the exact mix and list it as an F-list.
- 2026-11-10 · vid5 · options board · CTA: wanted the DM to read as a message notification ("rishi sent you a file") sliding in left → right on the tick; typed keyword in CAPITALS.
- 2026-11-10 · vid5 · build · A second `setFxPropertyKeyframes` call on the same property replaces the first (rise then exit_ lost the fade-in) → one call per property (`rise_exit`, `reveal_exit`). JS times must be wrapped: `t-(-0.05)`, never `t--0.05` (apply fails). Mask ids must be unique across the document.
- 2026-11-10 · vid5 · build · Giant word behind the head needs the baseline ≈ y 445 at 360 px and a ≤0.7 s rise, or the head hides the middle letter and the word never lands before the next scene.
