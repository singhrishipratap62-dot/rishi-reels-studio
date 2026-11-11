# Typography Principles

**Core First Principle:** On-screen text competes for a fixed reading budget while the eye is also tracking a face and the ear is decoding speech. Readability in video is measured in milliseconds of recognition, not legibility at rest. Every typographic choice should minimize fixation time: fewer saccades, recognizable word shapes, and no searching for where the text is.

## Strategic Frameworks

- **Recognition beats reading.** In fast video, viewers recognize word shapes rather than read letters. Short lines, high x-height and generous letterforms speed recognition. Thin strokes, condensed widths and decorative forms slow it.
- **Serif vs. sans: decide by role and render size, not "retention rate."** There is no reliable evidence that serifs or sans-serifs raise retention by themselves. The real variables are stroke contrast, x-height and render size. The stance:
  - **Captions and fast-read text:** heavy, low-contrast sans. Uniform strokes survive compression, small screens and motion blur.
  - **Statement and quote cards** (held ≥1.5s): a high-contrast serif works and signals editorial authority. It only survives at large sizes and on clean backgrounds.
  - **Never** use a thin-hairline serif for captions; the hairlines vanish under H.264 compression on phones.
- **Words per line are the real pacing control.** 2–4 words per line (house style) keeps each line within one or two fixations. Longer lines force the eye off the face to scan.
- **Kerning and tracking logic for speed:**
  - All-caps: track +2 to +5% to separate letterforms.
  - Mixed-case bold: track 0 to −2% to tighten word shapes.
  - Fix optical kerning on large headlines (AV, To, LT); bad pairs at 120px+ read as errors.
- **Leading for stacked caption lines:** 1.0–1.15× for 2-line captions, so the lines read as one unit. Above 1.25×, lines read as separate items and the eye pauses between them.
- **Contrast survives compression.** Use a solid stroke (6–10% of cap height), a soft drop shadow or a backing plate. Don't rely on footage contrast; backgrounds change every cut, and text must not.
- **Fixed position = zero search time.** Captions should live at one consistent anchor. Moving captions around costs the viewer a search on every line. Move only intentional emphasis text.

## Tactical Execution & Trade-offs

| Technique | Primary Use Case | Psychological Effect | The "Common Trap" vs. Pro Fix |
|---|---|---|---|
| **Heavy sans, 2–4 words/line, fixed lower-third anchor** | Spoken-word captions (Reels, Shorts, sound-off viewing) | Effortless parallel processing of face + text; sound-off viewers stay | **Trap:** full-sentence subtitle blocks, which pull the eye down and away from the face. **Fix:** chunk by phrase boundaries (not word count alone) and keep each chunk on screen ≥0.4s. |
| **Keyword emphasis (color/scale on one word)** | Stressing the payload term per line | Creates a micro-hierarchy; the viewer remembers the emphasized concept | **Trap:** emphasizing every other word, so emphasis becomes noise. **Fix:** at most one emphasized word per line, and not every line. Emphasis frequency ≈ one in three lines. |
| **High-contrast serif statement card** | Thesis lines, quotes, chapter titles, "the one idea" | Gravitas and editorial credibility; slows the viewer to absorb | **Trap:** serif used at caption size over busy footage, where hairlines break up. **Fix:** ≥7% of frame height, clean or blurred background, held for word count ÷ 3 + 0.5s. |
| **Kinetic typography (word-by-word build)** | Hooks, text-only reels, emphasis sequences | Controls reading pace exactly; builds anticipation per word | **Trap:** animating every word with heavy motion, which raises cognitive load and drop-off. **Fix:** short pops (3–5 frames), animate scale/opacity only, never spin or skew body text. |

### Platform Safe Zones (1080×1920 vertical)

| Zone | Instagram Reels | YouTube Shorts | TikTok | Rule |
|---|---|---|---|---|
| Top (avoid) | ~220–250px | ~200–250px | ~150–200px | No key text; header UI and gradient |
| Bottom (avoid) | ~350–420px | ~350–400px | ~400–450px | Captions sit *above* this |
| Right edge (avoid) | ~120–150px | ~120–150px | ~140–160px | Like/comment/share rail |
| Caption sweet spot | ~1250–1500px from top | similar | slightly higher | Lower third, above UI, below chin |

*Values are approximate and platforms change their UI. Verify against a current UI overlay template before locking a style.*

### Desktop vs. Mobile Ecosystem

| Factor | Mobile (vertical feed) | Desktop (YouTube long-form 16:9) |
|---|---|---|
| Minimum caption size | ~55–70px cap height at 1080w | ~4–5% of frame height |
| Words per line | 2–4 | 5–8 acceptable |
| Bottom safe area | Large (UI overlay) | ~10% (progress bar, controls on hover) |
| Thumbnail conflicts | Cover crop to 4:5 / 1:1 in grid | Timestamp badge bottom-right; avoid text there |
| Reading context | Sound often off, glance viewing | Sound on, seated attention |

## Retention & Funnel Application

- **Hook text = a second hook channel.** First-frame text should state a *different* angle than the spoken line (e.g., a spoken setup plus a written stakes line). Two parallel hooks catch both sound-on and sound-off scrollers.
- **First-frame text must be readable in under 1 second:** ≤6 words, heavy weight, top-center or upper-third placement (above the face if possible), never in the bottom UI zone.
- **Typographic consistency = brand recognition at scroll speed.** A locked caption style (font, stroke, emphasis color) lets returning viewers recognize your content before they see your face. This is the compounding asset; don't redesign it per video.
- **Long-form:** use typography for structure (chapter cards, key-term callouts) rather than full captions. Desktop viewers are sound-on, so text should *add* information, not duplicate it.
- **CTA text:** larger and held longer than any caption (≥2s), and placed in the clean, centered safe zone. A CTA that viewers have to search for converts at a fraction of one they can't miss.
