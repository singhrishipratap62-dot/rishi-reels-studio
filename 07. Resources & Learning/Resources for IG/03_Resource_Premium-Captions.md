# Premium Captions with Claude
### The caption system I use on my reels

*by @rishi.docx*

Captions are the part of an edit people notice most and the part I've corrected most. Here's the system, as principles you can give Claude (or use in any editor).

---

## 1. Two fonts, two jobs
- **Hero word:** a serif italic, bold (I use **Playfair Display Bold Italic**). One meaning word per caption, big.
- **Support words:** a clean sans (I use **Inter Medium**). Smaller, around the hero.

Both are free Google Fonts. Two fonts is the whole system; a third makes it look busy.

**Picking the hero:** the word that carries the meaning: a noun, a verdict, a number, the key term. Never a filler word ("the", "so", "hai"). If a caption has no meaning word, it's support-only.

## 2. Less text, centred
- **Five words or fewer** on screen at once.
- **About 22 characters per line**, max.
- **Everything centred:** hero in the middle, support line just above and/or below it, tight to it.
- Hero is large (roughly 3× the support size), but never wider than about 70% of the screen.

## 3. Words appear when they're spoken
This is what makes captions feel premium instead of "auto-generated":
- **Support words rise in one by one** on the exact time they're spoken (small upward slide + fade, about half a second, soft ease).
- **The hero builds letter by letter**, left to right, sliding in with a light blur that clears. Spread the letters across the time it takes to say the word.
- The hero must **finish appearing before the caption changes**. A half-built word at a cut looks like a glitch.
- Captions **cut** from one group to the next. No exit animation.

To do this Claude needs **word-level timestamps**. Ask for them, or give it an SRT and ask it to estimate per word.

## 4. Placement
- **Below the chin**, over a soft dark gradient at the bottom of the frame (transparent to about 45% black over the bottom 40%). The gradient keeps white text readable on any background.
- **Inside Instagram's safe zone:** on a 1080×1920 frame, roughly x 120–960 and y 250–1600, and keep clear of the right-hand button column in the lower half.
- If you know where the face is, tie the caption position to the chin so it never covers the mouth.

## 5. Captions change with the scene
One style everywhere looks lazy. Mine adapts:
- **On a light graphic:** dark text, at the top of the white area, never touching cards.
- **Split screen:** captions in the graphic half, above the content.
- **Busy screen (many elements):** one word at a time, so the eye has one thing to read.
- **Call to action:** one word at a time, just above the comment box.

## 6. Hinglish (or any mixed language)
- Write Hindi in **Roman script, exactly as spoken**. "aisa kuch nahi hota hai", not a translation, not cleaned-up grammar.
- English words stay English, lowercase.
- Keep spoken pauses as punctuation ("…hai.", "there?").
- Never split a compound verb across captions ("samjha paoge" stays together).
- Transcription tools mishear: one of mine heard "slow" for "slop". Treat the transcript as a draft and check words that change the meaning.

## 7. Small tricks
- **Repeated phrase, one new word:** keep the support line and swap only the hero ("seekhni hai," → "samajhni hai,"). It reads like emphasis.
- **Lowercase heroes** feel calmer and more modern than Title Case.
- **No coloured hero by default.** I tried a blue hero and removed it; white serif on a dark gradient looked more premium.

## 8. Mistakes I've had to fix
- White captions on a white card.
- Captions overlapping a graphic ("move it a little up" = about 30 px).
- Long lines, more than 5 words, left-aligned support text.
- Letters rendering half-cut because a blur effect was clipped. Always check a few frames up close.
- A sans hero on the face (it should be the serif; bold sans is only for inside graphics).

---

## Prompt to set this up
> Use this caption system for my edit: hero word in Playfair Display Bold Italic (lowercase, large, centred), support words in Inter Medium around it, max 5 words and ~22 characters per line. Support words rise in one by one on their spoken time; the hero builds letter by letter with a light blur and finishes before the caption changes. Place captions below my chin over a soft bottom gradient, inside the Instagram safe zone. [Hinglish: Roman script exactly as spoken.] Use the word timestamps attached. Show me 3 sample frames before doing the whole video.

*@rishi.docx*
