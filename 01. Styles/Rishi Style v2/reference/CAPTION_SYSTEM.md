# Caption system: Rishi v2

> The most-reviewed part of the edit. Based on Minimal Edit Style `[ME]`, tuned by Rishi `[R]`. Code: the caption block at the end of `engine/build_template.py`.

## 1. Text
- **Romanised Hinglish, exactly as spoken** ("aisa kuch nahi hota hai", "samjhaaya"). No Devanagari, no translation, no cleaning up the grammar. `[R]`
- English words stay English, lowercase ("this doesn't work like that.").
- Keep punctuation as spoken pauses ("…lo,", "…hai.", "there?").
- Words that sit across an edit cut are inferred from timings, so flag them to Rishi to listen. `[S]`
- The SRT is a draft: flag mis-heard words that change the meaning (vid2: "slow" was "slop"). `[R]`
- The SRT's Devanagari uses precomposed nukta letters (e.g. U+095B): match `roman_map.json` keys by NFD. `[S]`

## 2. Grouping
- ≤5 words per caption group; **≤ ~22 characters per line**. Don't overdo the text on screen. `[R]`
- Hero = the meaning word or phrase (noun, verdict, key term: *video, prompt, nahi hota, like that., skills, repos, taste, design skill, ghanta, end-to-end, edited, samjhaaya, did this,*). Groups without a hero are support-only lines.
- Break at punctuation and at cuts. Never split compound verbs ("samjha paoge").
- Repeated phrases with one changed word ("seekhni hai, samajhni hai,"): keep the support line and swap only the hero word. `[R]`
- Note: `engine/tools/roman_captions.py` groups ≤ ~22 chars and ≤4 words (inside the ≤5 rule); `build_template.py` sets the groups per video in `GROUPS`.

## 3. Default mode: A-roll (white serif hero)
| Part | Spec |
|---|---|
| Hero | Playfair Display Bold Italic, lowercase, 132 px, **white**, centred, baseline y 1420, ≤740 px wide (shrink to fit) |
| Support | Inter Medium 48 px, white 85 %, **centred** above (baseline = hero − 0.8×size − 8) and below (~~hero + size + 14~~ superseded v2.1: baseline = hero + 0.55 × support size, see §6) |
| Backing | bottom gradient (transparent → 45 % black, bottom 40 %), always on under A-roll captions. **No blue hero** (removed by Rishi) |
| Support reveal | word by word on the spoken time: rise 26 px → 0 + fade over 0.5 s, ease (0.22, 1, 0.36, 1) |
| Hero reveal | letter by letter, left → right: slide −24 px → 0 (0.42 s) + fade (0.28 s) + blur 8 → 0 (0.32 s); stagger = spoken length ÷ letters, 14–45 ms; finish ≥0.35 s before the group ends |
| Timing | group shows from its first word to the next group's start (or last word + 0.45 s if the gap > 0.6 s); ~~hard cut between groups~~ superseded v2.1: soft exit (MOTION_LIBRARY C-out) |
| Sound | Hi-Tech Click on the first hero letter; flick on each support word |

## 4. Context modes
Caption-mode boundaries must sit a little **before** word starts (vid2: 5.587 vs 5.59 fell into the wrong mode). `[S]`

| Mode | When | Spec | Tag |
|---|---|---|---|
| **Light ground (top)** | chat / ice scenes | same grammar, ink `#0B1730` hero, `#4A5878` support, hero baseline ≈372 so it just clears the card (don't push higher than needed) | [R] |
| **Split pane** | split screen | captions **above** the graphics at the top of the white pane: hero 100 px, baseline 330, support 40 px | [R] |
| **PiP single line** | picture-in-picture layout | one line of Playfair Bold Italic, ink, 54 px (auto-fit to 820 px), between the card and the PiP (baseline 922), word by word | [R] |
| **Wall one-word** | slop-wall zoom-out | **one word at a time**, pure **black** Playfair Bold Italic inside the tile directly below the face, auto-fit to ≈250 px (max 96 px); that tile drops its "slop" label; no other captions on this screen | [R] |
| **CTA one-word** | comments sheet up | one word at a time, white Playfair Bold Italic, up to 78 px, centred just above "Comments" (baseline 935) | [R] |

## 5. Don'ts
- White captions over white tiles or cards; blue captions over light scenes. `[R]`
- Captions overlapping cards or UI ("a little more toward the top"). `[R]`
- Long lines, more than 5 words, left-aligned or inset-tucked support (centred now). `[R]`
- **Blur on text without `layerSize`:** Tesseract clips the glyph to a thin baseline strip ("bottom 3 % appears first"). Every blur effect needs `layerSize: [1080, 1920]`. `[S]`

## 6. v2.1 additions (Style Lab v1, 2026-11-09) `[R]`
- **Default stays A** (serif hero letter build). Fix: a support line *below* the hero sits tight under it: baseline = hero baseline + 0.55 × support size (≈ +26 px at 48 px), not hero + size + 14. Rishi: "hai" was "very far below".
- **New mode: highlighter underline** (Keep). For the one verdict word of a section: after the hero lands, a `#FFD68A` stroke at 70 % sweeps under it left → right, 0.5 s ES, 0.1 s after the last letter; it sits behind the lower third of the letters.
- **Captions leave softly** (default now): see MOTION_LIBRARY C-out.
- Not adopted: karaoke brighten, editorial pair + hairline, mask rise, tracked kicker (left out of his picks; offer again only in option pools).
