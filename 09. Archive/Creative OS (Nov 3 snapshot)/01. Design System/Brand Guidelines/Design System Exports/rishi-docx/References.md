# Motion references

What the rishi.docx motion style is built from: five reference reels Rishi chose (October 2026), studied frame by frame. This page records what they have in common — the taste — so every motion graphic starts from it. Colours and fonts are never taken from references; only motion, pacing, layout and graphic language.

## The core, in one paragraph

**The voice drives everything on screen.** These reels are explained, not decorated: almost every second of narration has a matching visual — a word lighting up as it's said, a tag snapping onto the thing being named, a diagram growing one node per sentence. The face appears at the start, at turning points and at the end; the middle is mostly graphics and real footage. Everything moves fast (100–250ms), cuts hard, and sits on a calm, mostly empty ground with one accent colour. Small, technical details (hairline frames, corner ticks, tiny uppercase labels, numbered chapters) make it feel precise and premium, never flashy.

## What all five share

1. **Split-screen hook.** Every reel opens with the screen split: the topic's most striking visual on top (roughly 60%), the talking head below (roughly 40%), a bold title set over the top half. Within 1–2 seconds the split resolves into full-screen.
2. **Show the payoff first.** The result, the surprising image or the "after" appears inside the first 2 seconds; the explanation follows.
3. **Face → graphics → face.** Talking head is only ~10–25% of runtime: the hook, chapter pivots, and the CTA at the end. The middle is graphics, screen recordings and b-roll.
4. **Something changes every 1–2 seconds.** No graphic holds longer than ~3s without a new element arriving. Scene changes are hard cuts.
5. **Graphics build in sync with the voice.** Elements arrive on the word they illustrate. Diagrams grow node by node, lists tick off item by item, text lights up word by word.
6. **One accent colour per video.** Yellow, green or blue — never several. Everything else is black, white, grey. (Ours is always `signal`.)
7. **Small captions.** 1–3 words at a time, small (about 3% of frame width), in a compact pill or plain bold text, centred at about 72% of frame height. Never giant karaoke captions.
8. **Real things, framed.** Screenshots, tweets, articles, apps, footage and code are shown real but placed inside frames: browser windows, phones, hairline boxes with corner ticks and a small uppercase label.
9. **Annotation everywhere.** Leader lines, tags, highlights, strike-throughs, ticks, circles and magnifier insets point at the exact part that matters.
10. **Calm ground.** Plain off-white paper (with faint grain) or plain black. Lots of empty space; the content is the only thing on screen.

## Reel by reel

**Reference A — paper explainer (the closest match).** Off-white paper with faint grain, ink type, one yellow accent. Ghost-grey text turns black word by word as it's spoken, with a highlighter sweeping across key phrases. Numbered chapter dial ("01 Writing", next numbers fading on an arc). Annotation tags: a hairline leader draws out, a highlight bar extends, text types in, with tiny crop marks at the tag's corners. Recreated UI: a prompt box that types, a slider that drags to "80% — sweet spot", a checklist where tasks get struck through and ticked, a 2×2 grid of numbered cards with one selected, a working calculator with a growing bar chart. Halftone illustrations, isometric icons on yellow plates, small stars and crosshair ornaments.

**Reference B — dark documentary.** Black ground, thin white hairline frames with corner ticks and tiny uppercase labels ("THE COMPANY", "REPORTED"). Serif numbers counting up, serif italic micro-captions, a vertical timeline of framed clips by year, an org chart with a circular portrait, a radial "polymath" burst of skills, line-art isometric hardware, a terminal typing commands, tabbed comparisons ("original / green screen / replaced"). Captions bold uppercase; quotes from the interviewee captioned in a different colour from the narrator.

**Reference C — dark tech explainer.** Black ground, browser windows with traffic-light dots as the main frame for everything, windows multiplying into grids, code typing in an editor, wide-tracked display words with spaced small-caps subtitles, a lowercase serif phrase set against a heavy uppercase sans phrase in one headline, pagination dots stepping through a sequence, loading bars, a magnifier circle on footage connected by a line to an enlarged inset, a scan-line wipe for before/after.

**Reference D — fast CGI/tool walkthrough.** Split hook with a word-by-word title and a flash cut to the reveal. Bright white canvases with heavy uppercase "STEP 2"-style titles, multicolour highlighter on a script, storyboard sheets, image grids, before/after pairs joined by a hand-drawn arrow, behind-the-scenes footage cut against results.

**Reference E — product/tool demo.** Split hook (UI on top, face below), screen recordings cropped tight and zoomed on the action, a cursor selecting and highlighting text, mascots and cards on flat light backgrounds, b-roll of hands typing between UI shots, small dark-pill captions throughout.

## What changed in this design system because of these

- Motion is faster and cut harder (see *Motion*).
- New: *Pacing and structure* section (the face → graphics → face shape, split hook, beat timing).
- New components: SplitHook, Captions, KaraokeText, Callout, ChapterDial, PromptBox, WindowFrame, PostCard, Checklist, SliderControl, BentoGrid, MediaFrame, MagnifyInset, BeforeAfter.
- Paper ground may carry a faint grain; technical ornaments (corner ticks, crop marks, crosshairs, small stars) are now part of the grid language.
- A `ink-ghost` colour for text that hasn't been spoken yet.
- Second pass: IconSet (isometric line icons on signal plates), Halftone illustration style, ProgressSteps, ScanWipe, TabsCompare, OrgChart, RadialMap.
- Small technical labels use General Sans uppercase with wide tracking instead of the monospace the references use (two-font rule kept).
