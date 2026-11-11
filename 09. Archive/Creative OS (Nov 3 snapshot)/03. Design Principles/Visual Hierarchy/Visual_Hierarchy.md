# Visual Hierarchy

**Core First Principle:** Attention is serial: the eye fixates on one point at a time, ranked by visual salience (contrast × scale × motion × human faces). Hierarchy is the deliberate ranking of salience so the eye's natural order matches the intended reading order. Clutter means two or more elements competing for rank #1.

## Strategic Frameworks

- **The salience stack (strongest to weakest, roughly):**
  1. Faces and eyes
  2. Motion
  3. Luminance contrast
  4. Text
  5. Scale
  6. Saturation and hue

  To promote an element, raise it on several of these channels at once; to demote one, reduce it on all of them.
- **One #1 per frame, maximum three tiers.** Primary (the thing), secondary (context), tertiary (atmosphere). A fourth tier is clutter and should be removed, not styled down.
- **Faces win by default.** Any text or graphic placed near a face loses unless it's dramatically more salient. Either move the text away from the face or make the text the *intentional* #1 for that moment (and cut the face's salience with blur, a wider shot or reduced exposure).
- **Use depth layers as a hierarchy engine:**
  - **Foreground:** framing elements, out of focus, darker. They create depth but must never carry information.
  - **Midground:** the subject, sharpest, best lit, highest contrast.
  - **Background:** lower contrast, softer focus, cooler and less saturated, with minimal detail or motion.
- **Detail density reads as importance.** The eye goes to the region with the most edges and texture. If the background (bookshelf, busy wall, screens) has more detail than the subject, it wins attention. Reduce it with defocus, darkening or reframing.
- **Ratio rule for scale.** For a clear hierarchy, the primary element should be ≥1.5–2× the scale of the secondary. Below ~1.3×, elements look like equals and compete.
- **Hierarchy over time, not just space.** In video, hierarchy can be sequential: introduce elements one by one so each gets rank #1 for its moment, rather than showing everything at once.

## Tactical Execution & Trade-offs

| Technique | Primary Use Case | Psychological Effect | The "Common Trap" vs. Pro Fix |
|---|---|---|---|
| **Scale dominance (primary ≥2× secondary)** | Text-heavy frames, data callouts, thumbnail-style frames | Instant read order; no decision cost for the viewer | **Trap:** headline, subhead and caption at similar sizes, so the viewer reads nothing. **Fix:** a 3-tier type scale (e.g., 1 : 0.5 : 0.3) and cut tier 3 if possible. |
| **Contrast weighting (luminance isolation)** | Talking heads with busy environments | Subject "pops" without visible effects; the background recedes subconsciously | **Trap:** brightening the whole frame or adding a heavy vignette. **Fix:** relight or grade the subject +0.5 stop over the background; drop background contrast (lift blacks, reduce highlights) rather than darkening alone. |
| **Depth separation (FG / MG / BG)** | Interviews, B-roll, any location shoot | A sense of production value and focus; signals "this person matters" | **Trap:** a flat wall behind the subject, or a sharp detailed background. **Fix:** pull the subject 1.5–3m off the wall, use a wide aperture or a synthetic depth blur in post, and add a blurred foreground element for layering. |
| **Sequential reveal (temporal hierarchy)** | Explainers, lists, frameworks, multi-element graphics | Each element is fully processed; prevents overload and early swipes | **Trap:** a full graphic dropped at once, so the viewer reads ahead and disconnects from the speaker. **Fix:** reveal each element synced to the spoken word that introduces it; dim previous elements to secondary tier. |

### Salience Channel Control Sheet

| Channel | Promote (make #1) | Demote (push back) |
|---|---|---|
| Luminance | Brighter / highest local contrast | Lower contrast, lifted blacks |
| Scale | ≥1.5–2× nearest element | Shrink, or crop out |
| Focus | Sharpest in frame | Defocus, blur |
| Motion | The only moving element | Freeze or lock off |
| Saturation | Most saturated / brand accent | Desaturate 25–45% |
| Position | Optical center, upper-third, eye-line | Edges, corners, UI zones |

### Clutter Audit (run on every frame cluster)

| Check | Pass condition |
|---|---|
| Can you name the #1 element in 0.5s? | Yes, unambiguously |
| How many elements are competing? | ≤3 tiers |
| Does the background have less detail than the subject? | Yes |
| Is text overlapping the face or UI zones? | No |
| Is more than one element moving? | Only if staggered and intentional |

## Retention & Funnel Application

- **Hook frame = one element.** The first frame of a short should have an obvious single #1 (a face with an intense expression, a striking object or a bold claim). Multi-element hook frames are processed too slowly for the scroll decision window.
- **Thumbnail and first-frame hierarchy rule:** a face, ≤3–4 words, and one supporting object. Each extra element dilutes click-through and the first-second hold.
- **Use hierarchy shifts as pattern-breaks.** Switching which element is #1 (face → text card → B-roll object → face) every few seconds re-triggers attention without needing new content.
- **Long-form: hierarchy for scanning viewers.** Many long-form viewers half-watch. Chapter cards, on-screen key terms and lower thirds give them re-entry points so they can catch up instead of leaving.
- **CTA frames: strip to two tiers.** The speaker (secondary) and the action (primary). Remove B-roll, background motion and decorative graphics. The fewer competing elements in the CTA frame, the higher the action rate.
