# Feedback log: video production

Newest first. Each round lists what the user said and what changed. Durable rules are folded into `MOTION_PRODUCTION.md`. Add a round here whenever the user reviews a render.

## 2026-11-03 · R003 McKinsey hourly rates · round 2 (on v2)
User: "I like the current version", with three changes:
- Highlighter: good, but make it **bolder**. Alpha went from 0.6 to about 0.9 and height from 30% to about 34% of the glyphs.
- Background: drop my drifting-glow and dots build and use the supplied `gradnext-background-loop-9-16.mp4`. This is now the standard background, copied to `assets/`.
- Sound: take the sound design from **Minimal Edit Style** (its SOUND_DESIGN.md and SFX library). Swapped the procedural accents for that library with peak-aligned target levels.
- Also asked for this skill to record the feedback so future videos start right (this file and MOTION_PRODUCTION.md).

## 2026-11-03 · R003 · round 1 (on v1, the first static-feeling build)
- The hook number was "very bland": it should drop top to bottom with a gaussian blur and count up from slightly below to $1,000+.
- "an hour, for one partner" should arrive word by word, sliding bottom to top with a slight blur.
- Replace the underline with a **highlighter** on the bottom ~30% of the number, from "$" to the last 0, fading out towards the "+".
- Scene transitions were not smooth: make them continuous.
- Headlines should come line by line. Chart labels should reveal word by word from the bottom.
- Bars: ease in-out (fast start, slow settle) and a **gradient** fill. Applies to every bar chart in every video.
- Chips ("Contract maximum", "Derived", "Reported") were too rounded: make them rectangular with a very subtle radius. Applies to every chip and plate.
- Bar colour changes (for example at 33 s) should be a subtle gradient wipe, right to left, with ease in-out.
- The "$3.5 million a year" callout looked cheap: the card should slide in with opacity and blur, then the figure word by word, then the working line word by word.
- Takeaway typography: letter spacing and line spacing looked poor. Tighten both a little for a premium feel.
- Closing card: word by word, with a half-height highlighter under "consulting insights" that fades at its end.
- Captions: word by word, sliding bottom to top with a little blur.
- The background was bland: it should move, with subtle brand-blue dots.
- Remove the top-left "CONSULTING FEES" tag; it looks AI-made.
- Sound: every on-screen event needs a sound effect, except plain captions.

## 2026-11-03 · R003 · setup decisions
- Pilot one reel, review it, then roll the notes out to the rest.
- Light ground; firm names typeset (no logo files were available).
- Use only the gradnext design system and this skill; no other editing style. Minimal Edit Style was later allowed for sound only.
