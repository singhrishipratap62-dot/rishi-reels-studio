# Color Theory

**Core First Principle:** The visual system notices contrast before it identifies objects. Luminance differences register first, then saturation, then hue. A grade controls attention by deciding where the strongest contrast sits in the frame, and the subject should hold the highest combined contrast on all three channels.

## Strategic Frameworks

- **Contrast budget, not palette.** Treat every frame as a fixed budget of luminance, saturation and hue contrast. Spend it on the subject; the background gets what's left. A frame where everything is saturated has no focal point.
- **Luminance outranks hue.** Hue separation can't rescue a subject that sits at the same luminance as the background. Check the grade in monochrome first: if the subject doesn't separate in grayscale, adding color won't fix it.
- **Skin tone is the anchor.** Viewers detect skin errors instantly and forgive almost every other error. Lock skin to the vectorscope skin-tone line (~123°, the I-line) before any creative grading, and build the palette around it rather than the other way round.
- **Complementary separation = an axis.** Orange skin against a teal-shifted background works because the two sit at opposite ends of one axis on the vectorscope. Use the axis, not the look: push the background toward the complement of whatever the subject's dominant hue is.
- **Saturation follows focus.** Desaturate the periphery by 15–30% relative to the subject. Peripheral vision is weak at resolving color, so the eye unconsciously treats the saturated region as the area of interest.
- **Color as narrative state, not decoration.** Assign one color shift to a story state (problem = cooler/desaturated, solution = warmer/fuller). Changing state through the grade tells viewers the story has moved before the dialogue says so.
- **False color is structural, not corrective.** Use false color to decide the exposure hierarchy on purpose: subject skin in the target band (~55–70 IRE for lighter skin, ~40–55 for deeper), background 1–2 stops under, and nothing important clipping.

## Tactical Execution & Trade-offs

| Technique | Primary Use Case | Psychological Effect | The "Common Trap" vs. Pro Fix |
|---|---|---|---|
| **Complementary split (subject hue vs. background complement)** | Talking-head founder content shot in plain rooms | Subject reads as foreground without any compositing; the frame feels "graded" and premium | **Trap:** global orange/teal LUT that turns skin orange and walls cyan. **Fix:** key or isolate skin, hold it on the I-line, and apply the complement only to the background through a qualifier or luminance mask. |
| **Luminance-led isolation (vignette + subject lift)** | Low-budget footage, poor lighting, mixed color temperatures | Creates a pull toward center; implies intimacy and directness | **Trap:** a visible oval vignette darkening everything. **Fix:** shape a soft power window that follows the face, lift the subject +0.3–0.5 stop, and drop the background −0.5 to −1 stop. Viewers shouldn't be able to see where the window is. |
| **False color exposure mapping** | Multi-cam or multi-day shoots that need to match | Consistency reads as authority; mismatched exposure across cuts reads as amateur | **Trap:** matching shots by eye on an uncalibrated laptop screen. **Fix:** set a skin IRE target per speaker, conform every angle to it on false color, then match hue on the vectorscope. |
| **State-shift grading (narrative color arc)** | Before/after, problem/solution, transformation stories | Primes an emotional shift before it's verbalized; makes the "turn" feel earned | **Trap:** shifts so heavy they read as a filter switch. **Fix:** move temperature by ~300–600K and saturation by ~10–15%. It should be felt, not noticed. |

### Saturation Allocation by Region

| Frame region | Relative saturation | Rationale |
|---|---|---|
| Subject skin | 100% (reference) | Anchor; any deviation reads as wrong |
| Subject wardrobe / key prop | 90–110% | Can carry a brand accent if it's the focal object |
| Midground | 70–85% | Supports depth without competing |
| Background | 55–75% | Recedes; the cool shift helps |
| Graphics / captions | Can exceed 100% | Deliberate attention spikes; use sparingly |

## Retention & Funnel Application

- **Hook frame (0–1s):** the first frame should carry the highest contrast of the whole video. Feed scrolling is a luminance-contrast competition: a flat, low-contrast opening frame loses the scroll before the hook line is heard.
- **One brand accent, rationed.** Give the brand a single saturated accent (e.g., one highlight color in captions and graphics) and keep it out of the footage. Scarcity makes it a cue: whenever it appears, the eye goes to it.
- **Caption keyword color = second focal point.** Color only the payload word in each caption line. Coloring more than one word per line cancels the signal.
- **Grade by funnel stage.**
  - **Top of funnel** (reels/shorts): punchier contrast and saturation, because the content competes with the feed.
  - **Mid/bottom of funnel** (long-form, case studies, sales VSLs): gentler, natural grades, because they read as trustworthy and match a "proof" mindset. Over-graded bottom-funnel content looks like an ad and triggers skepticism.
- **Use color to mark sections in long-form.** A subtle grade shift per chapter gives the viewer an unconscious sense of progress, which reduces drop-off in the middle of the video.
- **Thumbnail–video continuity.** The first frame's dominant hue should match the thumbnail. If it doesn't, the viewer registers a "wrong video" mismatch, and the first 3 seconds bleed viewers.
