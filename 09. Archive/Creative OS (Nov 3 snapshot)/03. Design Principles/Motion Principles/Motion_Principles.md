# Motion Principles

**Core First Principle:** The brain models motion using real-world physics: mass, friction, acceleration. Motion that obeys an implied physics feels intentional and is processed effortlessly. Motion that breaks it, through linear speed or acceleration with no cause, registers as artificial, and the viewer notices the edit instead of the message.

## Strategic Frameworks

- **Linear motion is a tell.** Nothing physical moves at constant velocity from start to stop. Every keyframed move needs easing. The only exceptions are intentionally mechanical motion (tickers, scrolls, glitch).
- **Easing encodes mass.**
  - Heavy objects take longer to accelerate and decelerate (gentle curves, longer duration).
  - Light objects snap (aggressive curves, short duration).
  - Choose the curve by what the element *is*: a headline is heavy, a sticker or emoji is light.
- **Ease-out dominates entrances.** Elements entering should arrive fast and settle slowly (strong deceleration). The eye catches the fast part and then reads during the settle. Exits do the opposite: they accelerate away (ease-in) and get out of the eye's way.
- **Anticipation sets up attention.** A small counter-move before the main move (a 2–4 frame pull-back before a push) primes the viewer where to look. Use it on elements whose entrance must not be missed.
- **Momentum carries across cuts.** If motion is moving in a direction when the cut happens, the next shot should continue that direction or vector. Matching motion vectors hides the cut; opposing vectors emphasize it. Choose deliberately.
- **Motion speed sets pacing more than cut rate.** A slow cut rate with energetic motion feels fast; a fast cut rate with sluggish motion feels choppy, not fast. Match motion energy to the intended pace before adjusting cut length.
- **One primary motion at a time.** The eye tracks one moving object reliably. Two simultaneous primary motions split attention. Stagger entrances by 3–6 frames so they read as a sequence.

## Tactical Execution & Trade-offs

| Technique | Primary Use Case | Psychological Effect | The "Common Trap" vs. Pro Fix |
|---|---|---|---|
| **Strong ease-out (e.g., cubic-bezier 0.16, 1, 0.3, 1)** | Text, captions and graphics entering | Feels responsive and confident; content "lands" | **Trap:** a default "easy ease" (symmetric), which feels floaty. **Fix:** asymmetric curve: steep start, long tail. Entrance ≈ 6–12 frames at 30fps for text. |
| **Overshoot / spring (back-out, elastic)** | Light elements: stickers, emoji, icons, pop-ups | Playful, alive, high energy; signals informality | **Trap:** springs on serious content (data, quotes, founder statements), which undercuts authority. **Fix:** reserve overshoot for light-tone elements; keep overshoot ≤10% of travel distance, and settle within 1 oscillation. |
| **Slow push-in (digital zoom 100%→108–115% over a line)** | Talking-head emphasis, emotional beats | Increasing intimacy and intensity; viewer leans in | **Trap:** a constant zoom across the whole video, which loses meaning and stops registering. **Fix:** trigger push-ins only on build-up lines, then cut or reset at the payoff. The reset is the punctuation. |
| **Motion-matched cut (cut on action / vector continuation)** | Transitions between B-roll, whip pans, gesture-driven cuts | The cut becomes invisible; feels like one continuous flow | **Trap:** whip transitions everywhere, which tire the viewer and look template-like. **Fix:** cut on *real* subject motion (head turn, hand gesture) first; use synthetic whips only for scene or chapter changes. |

### Duration Reference (30fps)

| Element / Move | Duration | Curve character |
|---|---|---|
| Caption word pop | 3–5 frames | Sharp ease-out, slight scale (90→100%) |
| Headline / title entrance | 8–14 frames | Strong ease-out, no overshoot |
| Sticker / emoji | 6–10 frames | Back-out overshoot |
| Lower third / info card | 10–15 frames | Ease-out in, ease-in out |
| Emphasis push-in | Length of the line (1–4s) | Near-linear with eased ends |
| Exit of any element | 60–70% of its entrance duration | Ease-in (accelerate away) |

### Kinetic Weight → Edit Matching

| Cut energy | Motion pairing | Avoid |
|---|---|---|
| Hard cut on beat | Snap entrances, short durations | Slow floaty fades |
| Soft / J-cut (emotional) | Slow push, gentle ease, opacity drifts | Bouncy overshoot |
| Pattern-break cut | Abrupt scale jump, shake (2–4 frames), flash | Matched continuous motion (hides the break) |

## Retention & Funnel Application

- **Motion in the first 0.5s.** A completely static opening frame is the most skippable state in the feed. Have something already moving on frame 1: a subject mid-gesture, a push-in already underway, or text animating in. Don't start from rest.
- **Use motion to signal "new information."** An element should animate in only when it carries new meaning. Constant animation teaches the viewer that motion means nothing, which kills your ability to direct attention with it.
- **Rhythmic motion against the speech cadence.** Sync caption pops to syllable stress or keywords, not uniformly to every word. Stress-synced motion reads as "the edit understands what's being said."
- **Pacing curve across the video:**
  - **Hook:** highest motion energy.
  - **Body:** moderate, with spikes at each new point.
  - **Payoff:** a brief *stillness* before the key line (contrast makes the payoff land).
  - **CTA:** clean, low motion, so clarity beats energy.
- **Funnel stance:**
  - **Short-form TOFU:** fast, light, spring-heavy motion.
  - **Long-form / BOFU:** restrained, heavy easing. Over-animated sales or proof content reads as hype and erodes trust.
