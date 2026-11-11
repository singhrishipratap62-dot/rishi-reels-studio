# SCENE_PRINCIPLES — Rishi's Editing Style v1.0

One section per scene type found in the 15 reference reels, then the scene-selection table and genre recipes. Runtime shares are reference medians from SYNTHESIS §3 [EST]. Motion names refer to MOTION_LIBRARY.md.

## Target mix per reel (reference medians, adjust per script)
| scene | share | range seen |
|---|---|---|
| A-roll (± small overlay) | ≈ 45% | 26-60% |
| Full graphic (incl. walls, type beats) | ≈ 45% | 25-73% |
| Split | ≈ 10% (when used 7-28%) | 0-28% |
- A new visual state every ≈ 1.6-2.3 s; a hard cut every ≈ 4-8 s (reference median 6.7 s [MEAS]).
- **Never three graphic scenes in a row without returning to the face** [INF from all reels].

---

## S1 — A-roll
**Job:** trust, opinion, chapter openings, the payoff line, the CTA ask.
**Layout:** speaker full frame; caption block at y ≈ 1190, 1-2 lines, one italic word.
**Allowed overlays (one at a time):**
- chapter badge + title (lower-left; captions are hidden for that 1.5-3 s)
- counter or toast above shoulder height (proof that lands while he talks)
- reel-card strip behind the head (quantity without leaving the face)
- defocus bridge: A-roll blurred 8-12 px [EST] under a floating card or a single word
**Motion:** jump cuts on retakes/breaths; hold > 3 s gets a push 1.0 → 1.04 over the hold.
**Don't:** cover the face; put two overlays at once.

## S2 — Split pane
**Job:** a definition, rule or piece of evidence shown *while the speaker keeps talking*.
**Layout:** pane y 0-922 on the blue ground (or cream in cream reels), A-roll pushed into y 922-1920 with the face kept visible. White cards inside the pane; a single-line small caption (white sans + one white italic word) at the top of the pane (V14). The A-roll defocuses when the pane expands to full.
**Motion:** `pane-drop` (1.0 s) in, content `card-snap`/`hero-settle` starting as the pane lands, `pane-expand` (0.85 s) if the next beat needs the full frame, `pane-lift` (0.97 s) out.
**Hold:** 3-10 s. Re-use the same device several times in a reel (V07 used it 4×, V14 3×) [OBS].

## S3 — Full graphic: demonstration
**Job:** the rule is *performed*: shrink by 25%, split a colour 60/30/10, re-typeset a line in three fonts, before → after.
**Layout:** blue ground (or cream in cream reels), top caption band (headline lockup with one italic word), the demo object centred (y 500-1300) on white cards.
**Motion:** objects pop/settle with the ease-out grammar; labels with leader lines; a cursor may drive the UI.
**Rule:** the change on screen must equal the spoken number/claim (25% = 25%).

## S4 — Full graphic: proof / UI step
**Job:** evidence (post, profile, payout toast, DM, job post, tweet) or one step of a workflow (typed prompt, file chips, result card).
**Layout:** one hero card 60-90% W; supporting cards at the sides or stacked; caption at top.
**Motion:** hero `hero-settle` (1.0-1.5 s) or `card-snap` from the left edge (0.37-0.43 s); typed text ≈ 20 chars/s [EST] in sync with the spoken line; optional `proof-zoom` (1.8-3.5×) onto the one number that matters, highlighted in green or red.

## S5 — Wall / field
**Job:** quantity: "hundreds of tutorials", "12 brands", "60 edits", "$282,000 earned by editors".
**Layout:** 12-60 cards in a grid or loose field, outer ones blurred 6-8 px, one focus card sharp; may zoom out (scale 1 → 0.4) to reveal more.
**Motion:** diagonal-wave build (delay ≈ 0.04 s × (row + col)) [EST V05], slow drift, focus card swaps every ≈ 1.3 s.

## S6 — Counter over speaker / on ground
**Job:** money or result number before the claim is finished.
**Layout:** numerals 120-140px, white Inter Bold, centred upper-middle on A-roll or on the blue/cream ground; final money value turns green `≈#2FD26B` with a soft glow.
**Motion:** `counter-run` 1.0-2.0 s ease-out; may already be ~40% done at frame 0 in a hook [OBS V09]; price steps ≈ 0.5 s each.

## S7 — Type beat
**Job:** a provocative question, a verdict, the deadline.
**Layout:** full blue ground with light streaks (V14) or cream (deadline in cream reels, V13/V15); 1-3 white words centred, or a giant verdict word (cap 12% H); the deadline line with a red hand-drawn ellipse.
**Motion:** `drum-roll words` (hard swaps ≈ 0.5 s/word, last word italic), or a slow 1.8 s open on the giant word.
**Rule:** at most 2 type beats per reel; they are emphasis, not structure.

## S8 — CTA
**Job:** one clear action, decided per reel `[R1.0]`.
**Options:** (a) dark Comments sheet rising from the bottom, keyword typing into the dark input pill, blue send button (reference default, 12/15; captions hidden while the sheet is up, as in V15); (b) tutorial/product card rising + caption ask; (c) follow/save ask on A-roll. Always end on the face or on the action UI, calm (4-6 changes per 10 s).

---

## Scene selection table (condition → scene → why)
| condition in the script | scene | why [INF] |
|---|---|---|
| personal claim, opinion, chapter intro | S1 (+ badge at chapter start) | face carries persuasion; badge = scannable structure |
| abstract rule/definition while still talking | S2 | speaker stays present while the idea is shown |
| a principle that can be shown | S3 | show, don't tell |
| evidence, a person, a workflow step | S4 | verifiable, specific |
| a quantity | S5 or S6 | volume = credibility |
| money/result | S6 or toast in S4, green | checkable number |
| an objection ("is it AI?", "too expensive?") | the doubt as UI (comment toasts) → answer card | the viewer sees their own thought |
| a question / verdict | S7 | gives the beat its own frame |
| deadline / old price | red pen mark; S7 deadline line near the end | the only red = urgency |
| the hidden thing | blurred/pixelated card, revealed later or never (drives comments) | curiosity gap |
| the ask | S8 | one action |

## Genre recipes (all optional patterns, not limits `[R1.0]`)
| genre | beat order |
|---|---|
| **Teach a rule / tips** | hook (counted promise, "3 mistakes…") + tracker → per chapter: S1 + badge → S2 or S3 demo (7-13 s) → payoff on face → recap tracker → S8 |
| **Story / case study** | hook: person + number (avatar + counter/post card) → contrast fact (italic line) → steps with diamonds, one artifact per step, escalating card count → climax proof with zoom → lesson on face → S8 |
| **Offer / launch** | counter at frame 0 → secret/hidden item → "what's inside" by ordinals (one card each) → result card → price drawn down (strike + green) → deadline (red ellipse, ink type beat) → S8 |
| **AI / tool workflow** | hook question → each step as real UI (typed prompt word-synced, chips, result card) → verdict word → reaction on face → S8 |
| **Consulting case** (fits Story) | the case question as S7 → structure/frame as S3 demo → numbers as S6 → the answer on face |
