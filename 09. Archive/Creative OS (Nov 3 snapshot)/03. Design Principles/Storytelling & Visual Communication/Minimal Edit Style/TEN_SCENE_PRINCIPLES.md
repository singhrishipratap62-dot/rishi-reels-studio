# The Ten Scene Principles — v1.1

> v1.1 tags: `[R1.1]` = Rishi's rule from the first Tesseract edit (see `LESSONS_LEARNED.md`); it outranks `[EST]`/`[INF]`.

Tags: `[OBS]` seen · `[TX]` said in tutorial · `[EST]` estimated · `[INF]` my interpretation.
Timestamps "tut mm:ss" = tutorial; "final N s" = seconds into the tutorial's finished 57 s edit (starts tut 17:55.5); "R# m:ss" = reference reel. Stills: `references/stills/`.

---

## 0. A-roll + captions (the base layer)
Not one of the ten, but the most-used scene. `[OBS final: ~45 % of runtime]`
- **When:** hook line, announcing a new item/category, personal asides, jokes, the emotional verdict ("that was *brutal.*").
- **Treatment:** natural grade, bottom gradient to black; alternate framings by digital zoom (wide → medium → tight close-up) to create cuts without B-roll `[OBS final 31 s, 35 s, 39 s, 47 s]`. ~~Optional~~ **Always** a very subtle constant push-in on every A-roll shot: about +1.2 % per second, linear, with zoom cuts stacked on top `[R1.1]`.
- **Split-screen sources:** captions go on the seam band over a gradient scrim (see DESIGN_SYSTEM §6) `[R1.1]`.
- **Captions:** Principle 1 logic, hero word around chest height.

## 1. Cinematic caption design
**Look** `[TX 01:09–01:54, OBS tut 01:38 "blood glucose", R1, R7]`
- Inter for main text; Playfair Italic for special words.
- ≤ 5 words per caption group. 1–2 hero words bold (sans *or* serif), centred; the rest small, tucked above/below in the gaps.
- Asymmetric, balanced: support words often right-aligned over the hero's left half or trailing under its right edge.

**Animation** `[OBS 6 fps strip final 0–1 s, 23–24 s]`, **revised v1.1** `[R1.1]`
- **Support / normal text: word by word**, each word on its *spoken* time (from the word-level transcript). Each word **rises from below** (22 px → 0 over 420 ms) while its opacity eases up (0 → 100 over 380 ms). Ease-out. Never put a whole line on at once.
- **Impact / hero text: character by character, left → right.** Each glyph slides in 28 px from the left, unblurs (10 → 0 px over 300 ms) and fades up (240 ms). The stagger spreads the reveal over the word's spoken length (12–48 ms per glyph). Rishi likes the blur, so keep it.
- The hero reveal must **finish ≥ 350 ms before the group cuts**. If the word sits right before a scene change, move the scene change later rather than leaving a half-revealed word.
- Caption group holds while spoken, cuts out (no exit animation) when next group starts. `[EST]`
- Applies to text inside graphic scenes too: support lines word by word, hero words character by character `[R1.1]`.

**Rules**
- Hero = the word carrying meaning (number, noun, emotion). Serif italic for feelings/abstract ("*psychologically*", "*brutal.*", "*decide it.*"); bold sans for concrete/punchy ("four", "people", "fourth turn").
- Never two hero styles fighting in one group unless it's a deliberate pair ("**four** / *psychologically*").
- **Common mistakes:** centring every word; full-sentence captions; hero on a filler word; placing at the bottom where IG UI covers it; text too wide (> ~85 % width).
- **Mistakes Rishi flagged (v1.1):** a sans hero on A-roll (use serif); support text too small or far from the hero (use 48 px, tucked tight: above inset from the left, below inset from the right); text touching the frame edge (keep the hero ≤ 740 px, inside the safe zone).

## 2. B-roll + cinematic text
`[TX 02:15–02:37, OBS tut 02:08–02:26, final 28–30 s, R1 0:28–0:45, R4, R5]`
- **Selection:** split script into small segments; pick footage that literally shows the line (fight → someone fighting; "take their career down to the studs" → figure walking through a bare doorway).
- **Treatment:** light paper texture → darken edges → blur edges, so attention lands on the focal point. Moody, low-key, often desaturated/dark.
- **Text:** Principle-1 caption over the B-roll describing the scene; hero centred on/near focal point.
- **Animation:** gentle push-in (≈ 102 → 108 % over the shot) `[EST]`; text reveals as caption.
- **Use when:** the line is a human action/emotion that stock can show. Prefer over illustration when the viewer should *feel* rather than *understand*. `[TX 15:02 "easy for the viewer to feel it"]`
- **Mistakes:** generic/beautiful-but-unrelated stock; bright, busy, saturated clips; no edge treatment.

## 3. Painting animations
`[TX 02:37–03:01, OBS tut 02:38–02:50, final 10–12 s & 16–18 s, R2 0:02, R7]`
- **Selection:** a classical/public-domain painting that depicts the line (barista → Chardin-style kitchen maid; "fell in love" → Hayez *The Kiss*; "my dad" → old man reading a newspaper; prayer → devotional painting). Paintings carry philosophical, romantic, historical, or timeless ideas. `[INF]`
- **Treatment:** paint texture + rough paper texture over the painting; vignette.
- **Text:** cinematic text placed around the painting's main subject (in negative space beside a head, wall, sky).
- **Animation:** quick camera slide-in reveal `[TX]`; observed as a focus-pull (blurred → sharp in ~0.17 s) with a slow push `[OBS 6 fps final 10.5 s]`; exits with horizontal whip-blur into the next painting `[OBS final 11.5 s]`.
- **Character callout variant:** painting of a person + small label ("My dad") with a thin leader line, then "**Same job** for" + `HighlightBox` "**42 years**" `[OBS final 17–18 s]`.
- **Mistakes:** texture too heavy or not moving with the zooming painting `[TX revision #3: halve strength]`; text over faces; modern/AI-looking paintings.

## 4. Line + text animations
`[TX 03:01–03:25, OBS tut 03:00–03:18, final 50–53 s, R2 0:04–0:12]`
- **Base:** black or white background with paper texture.
- **Line:** accent-blue stroke (thick on white ≈ 22–28 px; thinner on black ≈ 6–10 px with a white marker dot) `[EST]`.
- **Behaviour:** the line leads up to a phrase, is *interrupted* by the text (gap where words sit), then continues to the next related phrase. Camera tracks the line's head so the viewer follows the argument.
- **Use when:** a sequence of linked abstract terms (calling → agility → courage; positive → negative → normal) or a quote unfolding.
- **Animation:** stroke-dashoffset draw ~0.6–1.0 s per segment, ease-in-out; text group appears as the line reaches it; scene exits with a whip-blur along the line direction `[OBS 6 fps final 47.8 s]`.
- **Mistakes:** line crossing through letters; line not ending where the eye needs to go; camera static while line leaves frame.

## 5. Line + illustration animations
`[TX 03:25–04:08, OBS tut 03:24–03:48]`
| Variant | Description | Use |
|---|---|---|
| **A – Horizon + marker** | horizontal/arched blue line, white marker dot locates the object, cinematic text above, illustration below (e.g., glowing blue brain under "what image pops *into your head?*") | introduce one object/idea |
| **B – Zigzag progression** | starts with text, line zig-zags down, camera pans to reveal objects on alternating sides with labels (rock-sculpture sequence) | stages, phases, a process |
| **C – Line to subject** | line travels straight to the main subject (blue line down to a brain, "benefits") | point at the consequence/answer |
- Illustrations: glowing blue on black, or painted/greyscale objects on dark. `[OBS]`
- Camera follows line head; each object reveals as the line passes it. `[TX]`

## 6. Text-centric scenes
`[TX 04:08–04:30, OBS tut 04:02–04:08, final 48–49 s, R2 0:19–0:20, R5 0:55, R6 1:12]`
- White or blue background, very rough paper texture.
- Two quotation marks bracket the text block near centre; text writes on in the middle (support line small, key phrase large bold sans, emotion word serif italic: "that's what it means to live an **entrepreneurial** *life*").
- **Use when:** a quote, a thesis, or the conclusion — the words *are* the visual. Also a reset/breath between busy scenes. `[INF]`
- **Animation:** word-by-word fade/blur-in synced to speech; quote marks appear first `[OBS]`.
- **Mistake:** forgetting the quote marks `[TX revision #6]`; too many words (> ~12).
- **Quote marks must bracket the text** `[R1.1]`. The opening mark hugs the first line top-left, and the closing mark sits after the last line, bottom-right. Keep the block slightly above centre. Marks placed far from the text read as separate elements.

## 7. Center illustration scenes
`[TX 04:30–04:54, OBS tut 04:20–04:50, final 19–27 s & 43–46 s, R4 0:00, 0:17, R6 0:58]`
- One illustration of the core idea dominates the centre; on white paper bg; rough painted noisy texture; occupies lower half and bleeds into upper-middle; abstract ragged edges/fade at the bottom.
- Variants: painted figure (blue), top-down object (brain scan), thin-line circular pattern, side-profile head with rough cloth texture + diagonal light, hand-drawn spiral, portrait with halo + orbiting words (`OrbitText`).
- **Text:** fills remaining space (usually above); can stack progressively ("Because it was **secure** / and because it was **low stress,**").
- **Animation:** subject paints/fades in from texture; slow zoom-out; words cycle or orbit. Keep on screen long enough `[TX revision #5]`.
- **Multi-part builds never pause** `[R1.1]`. When several pieces arrive in sequence (stacked blocks, bars, steps), overlap them: each rises over about 900 ms with ease-in-out, and the next starts about 520 ms later. A gap between pieces reads as a stutter.
- Consistency comes from shared texture, edges, colours — not identical drawings. `[TX 04:54]`

## 8. Side illustration + text scenes
`[TX 05:18–05:41, OBS tut 05:04–05:16, R6 0:51]`
- Same textured bg and abstract characters, but the figure sits left or right; text on the other side so the frame feels complete.
- Variant: half-circle (rough cloth texture) on one edge with clean text rotating around it (`OrbitText` on an arc), e.g., "No.4 GET INTERESTED".
- **Use when:** two elements must be shown together (person + fact; thing + label; before/after) — prefer over center when the text is substantial. `[TX]`

## 9. Object + text callouts
`[TX 05:41–05:52, OBS tut 05:24–05:34, final 32–38 s, R4 1:02, R6 1:01–1:05]`
- One element (photo, object, document) on paper background, cinematic text around it, rough reveal.
- Personal/biographical moments: real photos of the speaker, tilted slightly, soft shadow, stacked when the story advances ("leaving the *French horn*" → second photo "becoming a *scientist,*").
- **Use when:** a concrete, specific thing from the story — one object is enough. `[TX]`
- **Animation:** rough/torn or masked reveal, photo drops in with small rotation, stack offset `[EST]`.

## 10. Graphs & statistics
`[TX 05:52–06:05, OBS tut 05:40–05:46, final 1–5 s & 14–15 s, R1 0:00–0:08, 1:17–1:20]`
- Flat dark bg + noise; grid of thin white glowing lines; axes in white; series line white/blue; a **blue ball** marks the line head; camera follows the ball.
- Labels small sans with dashed reference lines ("MAX OUT at some point", "70's", "EARLY 50's"); key word in a blue `HighlightBox` ("*decline*").
- Patterns seen: rising staircase (one step per spoken "up"), flat line ("slow and steady"), rise-and-fall curve, bar comparison, 3 glowing orbs for "three components".
- **Animation:** axes draw (~0.3 s), line draws synced to words, ball eases; camera tracks with slight lag. Hold final text until the graph has read (~0.5 s) before cutting `[TX revision #2]`.
- **Highlight box (v1.1)** `[R1.1]`: it must visibly **grow from nothing**. scaleX 0 → 100 over about 480 ms with ease-in-out, starting about 120 ms before the word. Its text then arrives word by word. A 220 ms ease-out grow looked like it "started midway".
- Keep the whole graph (end point and ball included) inside x 160–840 so it clears the Reels icon column `[R1.1]`.
- **Mistakes:** real chart clutter (ticks, legends); data not synced to speech.
