# Minimal Editorial

A premium, minimal editing system for 9:16 talking-head reels: one cobalt accent, a grotesk + didone-italic type pair, paper and paint textures, and ten scene types chosen by what the speaker is doing in each line. It's reverse-engineered from Joseph's tutorial on the Arthur Brooks minimal animation style and seven reference reels. This is version 1.1: the v1.0 study plus Rishi's corrections from the first full edit (a 34 s podcast clip built in Tesseract). Rules he set directly are tagged **[R1.1]** and outrank estimates. Start with the **Lessons** section before an edit.

Evidence tags in these pages: **[R1.1]** set by Rishi · **[OBS]** seen in frames · **[TX]** said in the tutorial · **[EST]** measured or estimated · **[INF]** our interpretation.

## What stays fixed, what can vary

| Fixed in every video | Allowed to vary per brand or video |
| --- | --- |
| Caption placement logic (≤5 words, one hero, tucked support) | The `accent` hue (alias it to another token) |
| Texture on every graphic; no flat vectors | The serif partner (any high-contrast italic) |
| Ten scene types + A-roll, chosen by the selection rules | Paper tone (warm/cool white) |
| Announce → face, explain → show | Which optional motifs appear (orbs, orbit text, halftone) |
| One accent hue per video | Caption language: English, Hinglish or both |
| Plan approved before build; visuals approved before sound | Music genre within "restrained cinematic" |

## Colour

The accent is the brand. `accent` aliases `blue-600` (#0b52f9, measured from the reels), and every accent use points at `accent`, so a variant changes one line. Grounds are `paper`, `accent`, `ink` and `graph-ground`, always textured. Captions are `caption-white` on footage, blue and dark grounds, and `caption-ink` on paper, where serif emphasis words switch to `accent`. Glows and the graph ball use `blue-400`; halos on paper use `blue-200`. White on `accent` is 6:1 and `accent` on `paper` is 6.3:1. Never put accent text on an accent ground.

## Type

Inter does the work and Playfair Display Italic carries the feeling [TX]. Both are Google-hosted. Sizes in the Typography view are at 1080×1920.

- On A-roll, caption heroes are **always** `hero-serif` (110px bold italic), even plain words like *not* [R1.1]. `hero-sans` 120px/800 is for full-screen graphic scenes, where it gives contrast.
- `support` **48px**/500 (≈36 % of the hero), tucked tight against a hero corner: the line above inset ~7 % from the hero's left, the line below inset ~7 % from its right [R1.1]. 26–36px read as too small and floating.
- `quote`, `scene-title`, `label`, `label-caps` for scenes and graphs.

### Caption rules (English and Hinglish)

1. Chunk the line into groups of 5 words or fewer.
2. Pick the 1–2 words that carry the meaning: they become the hero.
3. Put the rest small in the gaps above-left or below-right of the hero. A lone trailing word goes above, on the right.
4. Hero centre sits at `caption-y` (55–70 % down), at most `hero-max-width` wide, inside the Instagram Reels safe zone: x 120–960, y 250–1600, clear of the icon column (x > 845 below y 1130) [R1.1]. Check after push-ins. On split-screen sources, captions go on the seam band between the two faces over a gradient scrim.
5. Hinglish is Roman script only. The hero can be Hindi (*kaam*, *dhoka*) or English (*growth*). Helper verbs and particles (*kar diya*, *hai*, *na*) stay support size. Never split a compound verb across groups. Numbers stay digits.

## Texture

Light grain on footage and paintings (`grain-light`), rough paper on text and illustration scenes (`grain-rough`), paint on paintings (`paint`, which moves with the image), noise on dark grounds (`noise-dark`), edge darkening and edge blur on footage (`vignette`). Painted figures use a rough, noisy dry-brush fill; character profiles and half-circles use rough cloth. A texture belongs to its layer: when the layer zooms, the texture zooms with it [TX revision #3]. Grain must actually show on a phone: in Tesseract that took an effect amount of 0.8 on light grounds and 1.0 on dark [R1.1].

## Layout

One focal point per frame and at least half the frame empty on graphic scenes [EST]. Center illustrations fill the lower ~55 % and bleed upward, with text above. Side layouts split figure and text. Text-centric scenes centre a block between quote marks. Graphs put labels in the top third. Radii are square except photos (`radius-photo`) and round markers (`radius-round`).

## The scene types

| # | Scene | Pick it when the line… |
| --- | --- | --- |
| 0 | A-roll + captions | is a hook, announces a new item, is an emotional verdict, a joke setup, or the close |
| 2 | B-roll + text | describes an action or feeling stock footage can show |
| 3 | Painting + text | is a story vignette, a romantic, historical or philosophical image, or a specific person (character callout) |
| 4 | Line + text | chains abstract terms (calling → agility → courage) or unfolds a quote |
| 5 | Line + illustration | introduces one object (A), walks through stages (B zigzag), or points at a consequence (C) |
| 6 | Text-centric | is a quote, thesis or conclusion |
| 7 | Center illustration | is one abstract concept or shape |
| 8 | Side illustration | needs two things shown together |
| 9 | Object callout | names one real artefact from the story |
| 10 | Graph | is about a number, trend, rate or comparison |

Principle 1 (cinematic captions) applies on top of all of them. The core rule: **announce → face, explain → show** [TX 14:15]. Aim for an average shot of 1.5–3 s (measured on the reels: 1.5–3.1 s), a first visual within ~2 s, and alternating grounds between consecutive graphics. Full detail: the Scenes, Editing psychology and Motion sections.

## Motion in one paragraph

Support words arrive word by word on their spoken time, each rising 22px from below as it fades up (M01). Hero words reveal character by character, left to right, each glyph sliding and unblurring (M02), and finish at least 350 ms before the cut. Caption groups hard-cut out. A-roll always carries a subtle push (+1.2 %/s) and changes framing with zoom cuts [R1.1]. Multi-part builds overlap with no dead time (M28); a highlight box grows visibly from zero over 480 ms (M25). Paintings and B-roll arrive with a focus pull and drift (Ken Burns). Lines draw at 18–30 frames per segment while the camera follows the head. Graph balls step on trigger words. Consecutive graphics are joined by a 4–6 frame whip blur, and A-roll is joined by hard cuts. Easing is ease-out for entrances and ease-in-out for camera moves, never linear.

## Sound

Sound comes after visual approval. **Lots of sound, each one quiet** [R1.1]: every text entry gets a sound, a distinct hi-tech click on hero words, a soft flick under each support word, a highlighter every time a line draws or extends, whooshes on graphic cuts. The denser the layer, the quieter it is. Use the user's SFX library first, lift the first 5 s by 3 dB, and measure the final program at about −15 LUFS, true peak ≤ −1 dBTP. Full trigger map and levels: the Sound section.

## Workflow gates

0. Ask up front: style, framing (keep a split screen or reframe), safe-zone template, SFX library, music [R1.1].
1. Transcribe word by word and cut silences (30 ms padding as the tutorial's reference value).
2. Edit plan: per beat, the script, its function, three design options, motion IDs, assets and notes. **Stop for approval.**
3. Asset list with sources and licences. Never substitute something unrelated.
4. Build scenes from these components, assemble and render. Expect the first draft to be 60–70 % there.
5. Run a numbered revision table, then ask: ready for sound, or more revisions?
6. Sound design, QC checklist, export at 1080×1920 30 fps.

## Building

Two build targets: the Motion artifact (below) or Tesseract, where a generator script writes every layer and audits the safe zone on each build (see Workflow and Lessons).

### In the Motion artifact

Scenes are timed HTML/CSS/JS from the SRT word timings. Load Inter and Playfair Display from Google Fonts. Build textures as SVG `feTurbulence` overlays (see `components/bundle.css`) or uploaded paper PNGs, placed inside the camera transform group. Draw lines with `pathLength` + `stroke-dashoffset`, and hero reveals with `filter: blur()` + opacity. Each scene type is one reusable function that takes words, timings and props. Export the SFX cue sheet with the same timeline.

## Known gaps in v1.1

Sound levels are set by measurement and Rishi's notes, but haven't yet been checked by ear on a phone. Motion durations outside M01, M02, M06, M25 and M28 still come from 1 fps and 6 fps samples. Principles 5B, 8 and 9 have only a few examples. No reference shows exact caption kerning or line-height specs. Add references to tighten these.
