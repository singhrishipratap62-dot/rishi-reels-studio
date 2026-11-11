# Stickers

Rishi's face, cut out as paper stickers, used as the personal touch in motion graphics, carousels and covers. Eight head stickers live in the `Stickers` asset group (`assets/Stickers/`). A sticker is a **reaction**: it shows how Rishi feels about the idea on screen, at the moment the voice says it. It never carries information and never decorates.

Read *Taste rules* first. Everything there applies to stickers too.

## The set

| File | Expression | Use it for |
|---|---|---|
| `head-neutral.webp` | Calm smile | Opening beat after the hook, calm explaining, the follow end card |
| `head-skeptical.webp` | One brow raised, lips pressed | A claim that doesn't add up, a company's official line, "they say..." |
| `head-thinking.webp` | Hand on chin, eyes up | The "why did this happen?" backstory beat |
| `head-confused.webp` | Frowning, mouth slightly open | A twist, a "wait, what?" moment |
| `head-smirk.webp` | Half smile, knowing look | "And here's the catch", an irony, a payoff |
| `head-shocked.webp` | Wide eyes, open mouth | AI crossing a line, the biggest reveal of the reel |
| `head-concerned.webp` | Serious, soft frown | A real person harmed or helped, who is responsible |
| `head-laughing.webp` | Open laugh | A rare absurd or light detail. Use sparingly: most stories here are serious |

Choose the sticker by the **feeling of the sentence being spoken**, not by the topic. If no expression honestly fits the line, use no sticker.

## How often

- **Claude decides the count for each script**, from the script's real emotional beats. Mark the beats that honestly call for a reaction (a twist, a reveal, a person at stake, a claim that doesn't add up) and use a sticker on those, and only those. As a guide that is roughly one per 20 to 25 seconds, never more than four per reel. A script with no honest beat gets none.
- When handing over a reel, say in one line which beats got a sticker and which expression, so Rishi can veto or swap.
- **The hook, by video type.**
  - **AI voiceover videos (no one on camera): a sticker may open the video**, in the first 3 seconds. With no face on screen, the sticker is Rishi's presence, so use the expression that matches the hook's feeling (`head-shocked`, `head-skeptical` or `head-concerned` most often). It sits in its own clear area beside the hook drawing and never touches the headline or the drawing. The hook still needs its headline and its strong visual: the sticker adds to them, it doesn't replace either. It begins arriving at frame 0. It counts toward the video's total.
  - **Talking-head reels: never in the first 3 seconds.** Rishi's real face is already the hook.
- **One sticker on screen at a time.** Never the same expression twice in a row.
- Spread them out: at least 10 seconds between two stickers.
- Place the strongest one (usually `head-shocked` or `head-concerned`) on the single biggest beat of the reel, and keep the rest quieter.

## Size and place

- Visible sticker width **300 to 420 px** on the 1080 canvas (the artwork sits inside a transparent square, so size by the visible head, not the file). Never below 240 px.
- It sits in a **clear area of its own**, beside the graphic. It never overlaps a graphic, a headline, a number or a caption, not even for a moment (*Text over graphics* in *Taste rules*).
- Keep it above y 1390 (the caption band is reserved) and inside the side margin of at least 64 px. Check *Formats and safe zones* for the Instagram UI.
- Build the scene so a sticker fits: if the graphic leaves no room, shrink or move the graphic, or skip the sticker.
- Left or right, whichever side the graphic leaves free. Don't mirror the file.

## Motion

Same two moves every time, so the stickers feel like a set.

- **Arrive: a cinematic ease-in.** It rises about 40 px from below while fading in and growing from 94% to 100% size, on `ease-cinematic` at `dur-slow` (900 ms): a slow start, a long smooth glide, then it comes to rest with no overshoot. Because it is a long move, start it about 0.5 s before the word so it is settling as the word is spoken.
- **Hold.** Completely still for 1.5 to 2.5 seconds, long enough to read the face. No wobble, float, tilt or looping animation.
- **Leave.** Lift-and-fade: rises 60 to 100 px straight up and fades (`ease-smooth`, about 0.6 s). Never a diagonal, spinning or shaky exit.
- Any scale or push on a sticker is anchored to its own centre.
- Swapping expression: the first sticker leaves before the next arrives. Never cross-fade two faces.

## Carousels and covers

Stickers work the same way in static designs, with these changes.

- **Cover.** One sticker, the expression that matches the hook's feeling (`head-shocked` for "AI crossed a line", `head-concerned` for a person at stake). Here it may sit next to the hook text, never touching it. Keep the whole sticker and the hook text inside the middle of the cover (y 300 to 1600) so the 3:4 profile-grid crop doesn't cut either. The cover is the one place a sticker is welcome in a reel's first second.
- **Carousel.** At most one sticker per slide and on no more than one slide in three. A sticker is a reaction, so it goes on the slide where the story turns, not on slides that only list facts. The last slide may use `head-neutral` beside the follow call.
- **No motion** on static designs, so the arrive and leave moves above don't apply. Same size range, same clear-area rule, same *Never* list.
- On a carousel slide the sticker keeps the side margin (64 px or more) and its own area, away from all text and graphics.

## Never

- Never recolour, tint, filter, add a shadow, outline or glow, or crop the sticker. The paper border is part of the artwork.
- Never put text, a speech bubble or an emoji on or around it.
- Never rotate it or tilt it. In a comparison, stickers never appear in pairs.
- Never use the stickers as the **only** visual of a hook, as a full-bleed background, or as a repeated pattern.
- A sticker never counts as a frame's touch of red: the frame still needs its own highlight, wash or ring.
- Don't use one on a heavy moment where Rishi's face would feel flippant (a death, an injury, a victim's own words). Use `head-concerned` at most, or nothing.

## Checklist

1. Is each sticker on a real emotional beat, the only sticker on screen, and, in a talking-head reel, outside the first 3 seconds?
2. Does the expression match the spoken sentence, and differ from the previous sticker?
3. Is it clear of every graphic, text and the caption band?
4. Does it arrive and leave with the two moves above, and nothing else?
5. Is the frame's red touch coming from something other than the sticker?
