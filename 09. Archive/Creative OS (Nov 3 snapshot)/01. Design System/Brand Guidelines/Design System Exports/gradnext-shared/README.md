gradnext helps people become sharp thinkers who solve problems from first principles, not formulas. The system is calm, structured and consulting-grade: deep Rhino grounds, generous white space, one Periwinkle or Chrome Yellow highlight per view.

> **Vision** — To create a generation of sharp thinkers who solve problems from first principles, not formulas.
>
> **Mission** — We transform how you think by connecting you with experienced problem-solvers who've been there.

## Content fundamentals

**Voice.** Clear, intelligent, grounded in first-principles thinking. Quiet confidence — never over-promising or over-explaining. Direct, structured and insight-led: help people think better rather than follow shortcuts.

**Tone.** Supportive but uncompromising. Challenge assumptions, ask the right question, choose clarity over comfort. Sound like an experienced problem-solver who has been there, guiding with honesty, precision and intent.

- Write practical, real-world language. No jargon, no hype, no motivational fluff.
- Address the reader as *you*; the brand speaks as *we*.
- Sentence case for headings and copy. The brand name is always lowercase — **gradnext** — even at the start of a sentence.
- No emoji in brand copy.
- Values, quoted as written: First-Principles Thinking · Real-World Relevance · Clarity Over Complexity · Ownership of Thinking · Long-Term Impact.

Real copy from the brand: "Crack consulting with clarity, structure, and community." · "How to Ace Fit Interviews in Consulting" · "Let's solve a Case Problem" · "3 signs you're a consultant… but you don't know it yet."

## Logo

The logo is a text-only wordmark in a formal sans-serif, all lowercase for evenness and balance. Use the files in **Logos**; never retype it in a font.

- `gradnext-wordmark-rhino.svg` on `white` or `neutral-100`; `gradnext-wordmark-white.svg` on `rhino`, `rhino-950` or `midnight`. `gradnext-wordmark-midnight.svg` is the small header mark on white pages.
- Clear space: the height of the wordmark's "e" on every side.
- Don't: condense or stretch it, capitalise it ("Gradnext"), rotate it, recolour part of it (e.g. "grad" + yellow "next"), strike or underline it, or italicise it.
- Placement: on 1080×1080 and 1350×1080 social posts, top-right at 1× padding (1350 also bottom); on 1920×1080 presentations and videos, top-left and top-right corners at 1.5× padding.
- Partnerships: gradnext and the partner logo sit at equal optical weight, separated by a thin vertical rule, a "×", or stacked with a horizontal rule — see `PartnerLockup`. Neither logo dominates.

## Colour

Core colours carry the brand; accents guide attention. Base colours — `rhino` (#2E3558), `white` and `rhino-950` (#1B1F38) — make up about **80%** of any layout. `periwinkle` is a supporting highlight, used sparingly. `chrome-yellow` marks the one key action or idea. Avoid arbitrary combinations; white space plays an active role.

- Text: `ink` on `surface`/`surface-raised`. Highlighted words in `ink-accent`. On `rhino` grounds, highlight in `chrome-yellow` or `periwinkle`.
- Never set `periwinkle` (2.5:1) or `chrome-yellow` (2.0:1) as text on white. Put `on-highlight` text on `highlight` fills, `on-accent` on `accent` fills.
- `ink-muted` in light mode is the source's #808080 — 3.95:1 on white; keep it to 24px+ or legal lines.
- Semitones (`rhino-500…950`, `periwinkle-100…600`, `chrome-yellow-100…400`, `neutral-100…800`) add depth and hierarchy to backgrounds and secondary elements; they never replace the core colour in a logo.

**Backgrounds.** Only these: `background-01` (dusk fade to rhino-950), solid `white` (Background 02), `background-03` (white with a periwinkle foot), `background-04` (midnight to rhino).

**Gradients.** `gradient-01` Rhino→Periwinkle, `gradient-02` Rhino with a Midnight core, `gradient-03` Chrome Yellow→Periwinkle, `gradient-04` White→Periwinkle, and `gradient-amalgamation`. Use as grounds for heroes, covers and key visuals, never behind long-form text. The CSS values approximate the guideline artwork.

**Overlays.** Approved fill-on-ground pairings (see `OverlayTile`): chrome-yellow or white on `background-01`; chrome-yellow or periwinkle on white; midnight on the periwinkle-cornered white; chrome-yellow or periwinkle on the glowing rhino-950 ground.

## Typography

**Primary — Avenir LT Pro** (`--font-sans`): geometric with humanist proportions, clean yet warm. Used for nearly everything.

| Style | Weight | Size |
| --- | --- | --- |
| `h1` Heading H1 | Bold | 96px |
| `h2` Heading H2 | Semi Bold | 64px |
| `sh1` Sub Headline SH1 | Medium | 64px |
| `sh2` Sub Headline SH2 | Medium | 48px |
| `body` Paragraph Body | Book | 48px |

Sizes are set on the 1920px canvas; scale proportionally for smaller canvases.

**Spacing by context**

- Social media (short-form, carousels, statics): letter spacing −4 to −6%, line spacing 95–120% (`social-headline`). Compact and confident.
- Print & high-detail collateral (brochures, PPTs, PDFs): letter spacing 0 to −2%, line spacing 100–120% (`print-headline`).
- UI & digital interfaces (web, dashboards, apps): letter spacing 0%, default line spacing (`ui-headline`).

**Secondary supportive** — only where they add clarity or emphasis:

- **Besley** Italic (`--font-serif`, `explainer-italic`) for explainer titles and one emphasised phrase.
- **Futura Bold** (`--font-display`, `display-futura`) for short uppercase labels, optionally gradient-filled.
- **Figma Hand** (`--font-hand`, `hand-note`) for a brief handwritten aside.

Do: use approved faces consistently, build hierarchy with size and weight, give text air, align deliberately. Don't: mix more than two faces in one lockup, pair Avenir with Figma Hand in a headline, add irregular gradients, squeeze or loosen letter or line spacing irregularly, stretch type, or add shadows and outlines.

Avenir LT Pro and Futura are licensed fonts and aren't bundled here; the stacks fall back to Avenir Next / Nunito Sans and Century Gothic. Besley is on Google Fonts.

## Shape, motif & imagery

- **Stripe motif** — 45° parallel bars in `chrome-yellow` (or `periwinkle` on business cards), bleeding off a corner: top-left and bottom-right on covers. Files in **Motifs**.
- **Outlined "g"** — the wordmark's g as a thin periwinkle outline at ~20% opacity, oversized and cropped behind dark title slides.
- Corners: `radius-md` on tiles, `radius-lg` on value cards, `radius-sm` on buttons. Value cards carry `glow-periwinkle` — an under-glow, not a drop shadow. No drop shadows elsewhere.
- Imagery: real-world brand applications — signage, stationery, cohort brochures — photographed in moody, directional light. See **Imagery**.

## Components

`Wordmark`, `Button`, `ValueCard`, `OverlayTile`, `PartnerLockup` — each has its own guidelines. `Button` and the spacing scale are intentional additions for digital use; the guidelines don't define them.


---

## Consuming this system (generated — do not edit)

Every path named below is under `project/` in this design system: read `project/api/tokens.md`, not `api/tokens.md`.

`components/bundle.js` defines `window.Gradnext` (5 components); `components/bundle.css` is its stylesheet; `tokens.css` is every token as a CSS variable plus `@font-face` for the fonts. `components/bundle.css` reads its variables from `tokens.css`. The bundle needs react 18 (not packed in this system: bring your own copy) (`window.React`), react-dom 18 (not packed in this system: bring your own copy) (`window.ReactDOM`), loaded before it. Build any UI by mounting these components; never hand-build a control or draw an icon the system provides.

- **Standalone page:** inline `tokens.css` and `components/bundle.css` in a `<style>`, then the library files and `components/bundle.js` as classic scripts (a file containing `</style`, `</script` or `<!--` breaks an inline element: write the sequence `<\/style`, `<\/script` or `\x3C!--` in your copy, or load that file by URL).
- **Design canvas:** bring `components/bundle.css`, `components/bundle.js` and `components/index.d.ts` (for the editor’s props panel) onto the canvas in full, as the canvas type’s design-system components reference says (a server-side copy first where it offers one); load the stylesheet before the script; skip the library files (the artboard supplies React); mount with `<x-import component-from-global-scope="Gradnext.<Comp>" …>`.
- **Slides deck, or any surface that cannot run the bundle:** tokens and fonts — the values are on `api/tokens.md`; the deck takes `tokens.json` by file path for its colour pickers, and fonts as “Fonts” below says.

Fonts: `tokens.css` loads each font from its file, by path.

- **Design canvas:** copy `tokens.css`, `fonts/AvenirLTProBlack.otf`, `fonts/AvenirLTProBlackOblique.otf`, `fonts/AvenirLTProBook.otf`, `fonts/AvenirLTProBookOblique.otf`, `fonts/AvenirLTProHeavy.otf`, `fonts/AvenirLTProHeavyOblique.otf`, `fonts/AvenirLTProLight.otf`, `fonts/AvenirLTProLightOblique.otf`, `fonts/AvenirLTProMedium.otf`, `fonts/AvenirLTProMediumOblique.otf`, `fonts/AvenirLTProOblique.otf`, `fonts/AvenirLTProRoman.otf`, `fonts/Futura Bold.ttf`, `fonts/Futura Book.ttf`, `fonts/Futura Round.ttf`, `fonts/Futura Std Book.ttf`, `fonts/Futura Std Heavy.ttf` and `fonts/Futura Thin.ttf` to the same paths under the canvas’s `project/ds/<folder>/` (`<folder>` is the folder you install this system under; `fonts/AvenirLTProBlack.otf` lands on `project/ds/<folder>/fonts/AvenirLTProBlack.otf`), in the same call that installs this system. Link that copy of `tokens.css` in the artboard’s `<head>` as `ds/<folder>/tokens.css`, or as Design’s instructions say for an artboard in a folder. If the install’s reply leaves a font out, bring that font in as for any other page.
- **Slides deck:** for each family you use in the deck (`faces` holds at most the number of typefaces Slides’ `deck-files.md` gives), install its file with the system and name the path it lands on as that family’s `src` in `project/deck.json` `faces`, under the key in the Slides column. A deck takes a font as a file only under the rule in Slides’ `fonts.md` (no space or leading underscore in its path, for two): any other font, or one kept by id, is uploaded as `fonts.md` says.
- **Any other page:** one file per family is enough (below: the upright face nearest regular weight; bold and italic synthesize). Fetch it as the fetch column says (Artifact tool `read`, that id or path as `path`), upload it as an asset (`publish`, `file_path`, `asset:true`) and declare it with an `@font-face { font-family: "<family>"; src: url(<uploaded>) }` rule.

| family | file | fetch | CSS | Slides `faces` key |
| --- | --- | --- | --- | --- |
| Avenir LTPro Black | `fonts/AvenirLTProBlack.otf` (weight 900) | `read` the file with `project/` in front |  | `avenir-ltpro-black` |
| Avenir LTPro Black Oblique | `fonts/AvenirLTProBlackOblique.otf` (weight 900, oblique) | `read` the file with `project/` in front |  | `avenir-ltpro-black-oblique` |
| Avenir LTPro Book | `fonts/AvenirLTProBook.otf` (weight 400) | `read` the file with `project/` in front |  | `avenir-ltpro-book` |
| Avenir LTPro Book Oblique | `fonts/AvenirLTProBookOblique.otf` (weight 400, oblique) | `read` the file with `project/` in front |  | `avenir-ltpro-book-oblique` |
| Avenir LTPro Heavy | `fonts/AvenirLTProHeavy.otf` (weight 800) | `read` the file with `project/` in front |  | `avenir-ltpro-heavy` |
| Avenir LTPro Heavy Oblique | `fonts/AvenirLTProHeavyOblique.otf` (weight 800, oblique) | `read` the file with `project/` in front |  | `avenir-ltpro-heavy-oblique` |
| Avenir LTPro Light | `fonts/AvenirLTProLight.otf` (weight 300) | `read` the file with `project/` in front |  | `avenir-ltpro-light` |
| Avenir LTPro Light Oblique | `fonts/AvenirLTProLightOblique.otf` (weight 300, oblique) | `read` the file with `project/` in front |  | `avenir-ltpro-light-oblique` |
| Avenir LTPro Medium | `fonts/AvenirLTProMedium.otf` (weight 500) | `read` the file with `project/` in front |  | `avenir-ltpro-medium` |
| Avenir LTPro Medium Oblique | `fonts/AvenirLTProMediumOblique.otf` (weight 500, oblique) | `read` the file with `project/` in front |  | `avenir-ltpro-medium-oblique` |
| Avenir LTPro Oblique | `fonts/AvenirLTProOblique.otf` (weight 400, oblique) | `read` the file with `project/` in front |  | `avenir-ltpro-oblique` |
| Avenir LTPro Roman | `fonts/AvenirLTProRoman.otf` (weight 400) | `read` the file with `project/` in front |  | `avenir-ltpro-roman` |
| Futura | `fonts/Futura Book.ttf` (weight 400) | `read` the file with `project/` in front | `var(--font-display)` | `futura` |
| Futura Round | `fonts/Futura Round.ttf` (weight 400) | `read` the file with `project/` in front |  | `futura-round` |
| Futura Std | `fonts/Futura Std Book.ttf` (weight 400) | `read` the file with `project/` in front |  | `futura-std` |

**Read, per thing:** a component’s props, parts and examples: `api/components/<Comp>.md`; token values: `api/tokens.md`; stored assets and their paths: `api/assets/<Group>.md`. After this README, fetch the cards and fonts you need in ONE message as parallel calls — none depends on another.

**Two rules.** Before you use a thing — a component, a token group, an icon, an asset — read its card from the index below; a value you did not read from a card is a guess. `tokens.json`, `manifest.json`, `components/index.d.ts` and `design-system.json` are sources for tools: hand them over. `components/<Comp>/README.md` and `assets/<Group>/README.md` are the long-form second read a card links to; `SKILL.md` and `artifact-type/` beside them are authoring guidance, not needed to consume the system.

## Index (generated — do not edit)

**Tokens**

- `api/tokens.md` — Every token: surface, text, fill, border, palette, type, spacing, radius, shadow, gradient. (15.3k)

**Icons and assets**

- `api/assets/Logos.md` — 3 files, by asset id. (1.3k)
- `api/assets/Motifs.md` — 3 files, by asset id. (1.3k)
- `api/assets/Imagery.md` — 4 files, by asset id. (1.2k)
- `api/assets/Logos_Original.md` — 7 files, by asset id. (1.3k)
- `api/assets/Industry-Primers.md` — 21 files, by asset id. (2.6k)
- `api/assets/Company-and-College-Logos.md` — 48 files, by asset id. (5.7k)
- `api/assets/Thumbnail-Mock-Case-Interview.md` — 1 file, by asset id. (0.8k)
- `api/assets/Thumbnails.md` — 1 file, by asset id. (0.7k)

**Components** (`api/components/<Comp>.md`, 5)

- **Brand**: `Wordmark` — The gradnext logo — a lowercase text-only wordmark — rendered from the guideline artwork as inline SVG · `ValueCard` — A rounded dark-glass card with a periwinkle under-glow that presents one brand value or pillar · `PartnerLockup` — gradnext set beside a partner brand with equal respect — neither logo dominates
- **Actions**: `Button` — A text button for digital surfaces — an intentional addition, since the guidelines define colour pairings but no button
- **Color**: `OverlayTile` — One approved colour-overlay pairing: a rounded square fill centred on a rounded square ground
