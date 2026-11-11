# rishi.docx

Bold, high-contrast, editorial design for explaining AI on Instagram: reels, motion graphics, carousels and covers.

This is the brand book for **@rishi.docx**. Anything made for the account (a motion graphic, a carousel, a cover, a static post) starts here. Read this page first, then **Taste rules** (what Rishi has approved and rejected in review: check every frame against it), then *Motion references* and *Motion references, set 2* (the taste this system is built on), *Pacing and structure*, *Motion*, *Formats and safe zones* and *Pen and grid*, then the components you need.

**Talking head or AI voiceover?** If the brief says the reel is a **talking-head** video of Rishi, also read *Talking-head layout*: it opens in split screen, with graphics on top and a green screen below for his video, and switches between split, full-graphic and full-green frames. AI-voiceover reels (ElevenLabs, faceless), or any brief that doesn't say "talking head", use the normal full-frame layout with **no green screen**.

**The one-line brief for any motion graphic:** explained, not decorated — every spoken idea gets a visual that lands on its word with smooth, eased motion, on a calm paper or ink ground, with one red accent pointing at what matters.

**Language: English only.** Every word that appears on screen — in motion graphics, carousels, covers and any other design — is in English. Hinglish is used only when a specific brief explicitly asks for it.

## Personality

**Bold, punchy, high-contrast, premium, editorial.** It should feel like a well-designed magazine that explains technology, not a tech product and not a hype page.

- **Bold**: big type, few words, one idea per frame.
- **High-contrast**: ink on paper (or paper on ink). No mid-tone mush.
- **Premium**: restraint. Lots of empty space, three colours, nothing decorative that doesn't explain something.
- **Editorial**: structure you can feel (alignment, rules, crop marks, numbered labels), and type that does the work.

- **Explained**: the voice drives the screen. Every idea gets a visual — a diagram, a framed screenshot, a number, a tag — arriving exactly when it's said.

What it is not: neon, glowing brains, blue-purple gradients, robot stock imagery, emoji, drop shadows, "futuristic" UI chrome, giant bouncing captions. Those are what every AI page looks like.

## The core idea: structure and pen

Every visual combines two layers:

1. **Structure** (precision). Rules, aligned columns, numbered labels like `01`, `02`. This is the "explained properly" layer. There is **no drawn background grid**: the frame is plain paper or ink, and the structure comes from alignment, rules and labels. Faint guide lines appear only *inside* charts and diagrams, where they help read values.
2. **The pen** (the human hand). Marks drawn in `signal` red on top: an underline, an arrow, a strike-through, a tick. **No pen circles, ever.** Emphasis on any word (headlines, labels, real text) is a highlight: three levels, from a pale Follow wash to a solid deep-red bar (see *Highlights* in *Pen and grid*); emphasis on an object is a red-tint wash behind it or the marching dotted square (see *Taste rules*). This is "here's what matters": it's you pointing at the screen.

Structure = what's true. Pen = what to notice. Use the pen once or twice per frame at most. Details in the *Pen and grid* section.

## Colour

Three locked colours. Nothing else, ever.

| Token | Hex | Role |
|---|---|---|
| `brand-paper` | `#F4F1EA` | Default ground |
| `brand-ink` | `#141414` | Text, solid shapes; the ground of the ink theme |
| `signal` | `#E2432A` | The one thing to notice |

Everything else is a step of these (`surface`, `ink-muted`, `line`, `line-strong`, `signal-marker`), never a new hue.

**Themes.** `Paper` (paper ground, ink text) is the default. `Ink` (ink ground, paper text) is the same system inverted — use it for heavier moments, for contrast between sections of one video, and so the grid doesn't look monotonous. The semantic tokens (`bg`, `ink`, `ink-muted`, `surface`, `line`) flip automatically; `signal` stays the same.

**Rules for signal red:**
- **One signal moment per frame.** The key phrase, the key number, or one pen mark — not all three.
- **Red text only at 60px and above** (on a 1080-wide canvas). Its contrast against paper is about 3.7:1, which only reads at large sizes. For smaller emphasis, use a `signal-marker` highlight swipe behind ink text instead.
- Red is never a background fill for a whole frame or card. It points; it doesn't sit.
- Red means "look here", not "danger". Don't use it to colour-code good vs bad; use position, labels and the pen marks (tick vs strike) for that.

## Typography

Three families, each with one job:

- **Bricolage Grotesque** (`--font-display`) — the headline voice: hooks, titles, headlines, chapter numbers and big stats. Characterful and confident, so it carries the brand on its own. ExtraBold 800 for hooks and numbers, Bold 700 for headlines and titles. Open-source (Google Fonts, OFL).
- **General Sans** (`--font-sans`) — the workhorse for everything read at small sizes: body lines, labels, kickers, captions, axis labels, source lines. Regular 400, Medium 500, Semibold 600.
- **Gambetta** (`--font-serif`) — two uses only:
  1. **Quotes**: what a person, company or court actually said, in Gambetta regular.
  2. **Concept titles**: the title of an explainer plate, `concept-title` style — Gambetta regular, with an optional italic second line ("Schlep / *Blindness*"), plus serif units next to a big number ("65 *billion*"). Only on explainer plates, never as the reel's hook.

**The signature phrase:** one key phrase inside a headline goes in `signal` red, in the **same Bricolage face, upright** — no font switch, no italic. Example: "Did AI **really** take the job?" with *really* in red. One phrase, never a whole line, and only at 60px and above.

**Scale (at the native 1080px-wide canvas):** `display-xl` 132 · `display` 104 · `headline` 80 · `title` 60 · `body` 44 · `label` 32 · `caption` 32. Nothing smaller than 32px, ever: reels are watched on phones, often fast.

**Rules:**
- Headlines in Bricolage Grotesque, ExtraBold or Bold, tight tracking (-3% to -3.5%), tight leading (0.95–1.0).
- Never set body copy, labels or captions in Bricolage; never set headlines in General Sans.
- **Kickers**: a tiny spaced uppercase line above a title, between two short hairlines (`— THE PHENOMENON —`), `kicker` style in General Sans. One per plate.
- **Tiered titles** for cinematic hooks: light small line → heavy big line → light small line, right-aligned ("one of the / **Worst Cyberattacks** / in history"). Bricolage Regular 400 for the light lines, ExtraBold for the heavy one.
- Sentence case. No all-caps headlines; `label` style may be uppercase for short tags (`01 · INPUT`).
- Max ~6 words per line in a hook; max 3 lines on screen at once.
- **All on-screen text is in English** — titles, labels, captions, diagrams, carousels, covers. Never Hinglish, even when the voiceover is in Hinglish, unless a specific brief explicitly asks for it.

> **Font files are installed**: Bricolage Grotesque (variable, 200–800, with optical size), General Sans and Gambetta (full families).

## Layout

- **Formats:** reel 1080×1920, carousel 1080×1350, cover 1080×1920 (cropped to 3:4 on the profile grid). Full details in *Formats and safe zones*.
- **Margins:** `space-5` (64px) on the sides of every frame.
- **Grid:** 6 columns inside the margins, `space-3` (24px) gutters. Everything aligns to it: text, diagram nodes, chart bars. It is an **invisible** alignment grid; it is never drawn on the frame.
- **Alignment:** left-aligned by default. Centre only a single hook or single number standing alone.
- **Spacing scale:** 8 · 16 · 24 · 40 · 64 · 96 · 144. Use only these.
- **Corners:** square (`radius-0`) for all brand shapes. Rounded only for things that are literally UI (chat bubbles, app screenshots, `radius-lg`) and small tags (`radius-sm`).
- **No gradients, no glow.** Depth comes from `surface` vs `bg` and from hairlines. Two exceptions: a very soft, short shadow under floating UI cards (prompt box, post card) so they read as objects on paper; and the `scrim` — a short ink fade (0 → `scrim`) behind text that sits directly on footage (`TitleOverFace`, `BeatWord`).
- **Crop-mark corners**: rare. Use them on the end card or one framed plate at most, never on every frame, and nothing may touch them. (Changed October 2026.)
- **Text never overlaps graphics.** Headline band at the top, caption band at the bottom (y 1395–1490), graphics between. See *Taste rules*.
- **A touch of red in every frame**: a highlight bar, a tint wash or a red-tint ring, never pure ink on paper.
- **Texture:** the paper ground may carry a faint grain (2–4% opacity noise). Illustrations may use halftone dots for shading. Nothing else.
- **Empty space is the default.** One graphic, centred in the safe area, with room around it. If the frame feels full, split it into two beats.

## Visual explanations, not just text

The aim is that motion graphics *show* the idea, not just put the script on screen. Before writing text on a frame, ask which of these fits:

| The idea is… | Show it as |
|---|---|
| A process or how something works | `FlowDiagram` — numbered nodes, connectors drawing in |
| A number that matters | `StatReveal` — counts up, with unit and source |
| A comparison of amounts | `BarChart` — bars growing against faint guide lines |
| Something that happened over time | `Timeline` — a rule drawing across, dated stops |
| Before vs after, claim vs reality | `SplitCompare` — two columns, tick and strike pen marks |
| What an AI actually said | `ChatFrame` |
| What a person or org said | `quote` style + `SourceCard` |
| The one phrase to remember | `HookTitle` + `PenMarks` |
| Ending with a follow CTA | `FollowCard` |
| The opening 2 seconds | `SplitHook` |
| A sentence being said | `KaraokeText` |
| Pointing at a specific part | `Callout`, `MagnifyInset` |
| Starting a new section | `ChapterDial` |
| What someone typed into an AI | `PromptBox` |
| A website, app, code or terminal | `WindowFrame` |
| A tweet, post or news article | `PostCard` |
| Tasks done, steps completed | `Checklist` |
| "How much" / a setting / a trade-off | `SliderControl` |
| Several options, one chosen | `BentoGrid` |
| Real footage or a photo as evidence | `MediaFrame` |
| Before vs after | `BeforeAfter`, `ScanWipe` |
| Several versions of one thing | `TabsCompare` |
| Waiting, processing, steps of a sequence | `ProgressSteps` |
| Who's behind something | `OrgChart` |
| One person or thing, many areas | `RadialMap` |
| Labelling nodes and cards | `IconSet` |
| An object or scene to explain | `Halftone` illustration |
| A real post, article or doc being quoted | `ReadAlong` — the highlight walks the spoken words |
| A product UI that would float on empty ground | `EchoBackdrop` |
| Naming parts of a diagram, photo or map | `TabLabel` |
| A span of years, or "1 in N" | `UnitDots` |
| A place | `DotMap` — dot map, pin, coordinate tag |
| A person in the story | `PortraitCard` |
| A person's photo arriving, or one photo turning into another | `ImageGenerate`: pixel mosaic resolves into the photo; one red cell |
| The AI is working, searching or waiting | `ThinkingOrb`: one of nine dotted states, ink, red only as the frame's one moment |
| The name of an idea or phenomenon | `ConceptTitle` |
| Something running, scanning, being monitored | `RadarSweep` |
| A pricing, benchmark or comparison table | `DataTable` — focus row, the rest dims |
| A cinematic story beat, one word at a time | `BeatWord` |
| The hook in a face-led reel | `TitleOverFace` |

## Credibility on screen

Every reel carries `Captions` throughout. Every factual claim shown on screen gets a `SourceCard` or a `caption` source line (e.g. "Source: company blog, Oct 2026"). This makes accuracy part of the visual identity. Never show a number without where it came from.

## Iconography and illustration

`ThinkingOrb` is the one animated mark: dotted spheres in the same ink-and-dots language as `Halftone`, only for "the AI is thinking" beats.

Icons are isometric line drawings (4px ink, rounded joins) on a flat `signal-marker` plate — see `IconSet` and the `Icons` asset group. Illustrations use the same isometric line with halftone-dot shading and one signal-dotted detail — see `Halftone`. No stock icons, emoji, 3D renders or robot clip-art.

## Logo and wordmark

No logo yet. Until one exists, the brand mark is your **profile photo** (see the `Profile` assets) together with the wordmark: **rishi.docx** in Bricolage Grotesque Bold, `ink`, lowercase, at `label` size or larger in a corner of carousels and covers. Don't invent a mark.

The photo appears in the `FollowCard` at the end of reels with a follow CTA, and anywhere the account itself is shown (a mock post or comment).

## Do and don't

**Do:** one idea per frame · big type, few words · structure on everything (alignment, rules) · one signal moment · show the idea as a diagram/number/chart · source on every claim · leave space.

**Don't:** a drawn background grid · new colours · gradients, glow, shadows · more than one red thing per frame · red small text · text in the safe-zone edges · robot/brain stock imagery · emoji · centred paragraphs · full lines in italic.
