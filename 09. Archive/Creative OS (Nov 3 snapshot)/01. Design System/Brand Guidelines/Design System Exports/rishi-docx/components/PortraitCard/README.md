# PortraitCard

A person in the story: their photo in a paper card over a halftone circle, their name in Gambetta, their role in a tab tag.

**Use for:** introducing founders, researchers, executives, victims, whistleblowers — anyone the story turns on. Two cards side by side for "he and his co-founder".

**Anatomy:** paper card, 20px padding, 2px `line` border, `shadow-float`, rotated −2° → photo, greyscale, multiplied over a 360px halftone circle (`signal` dots at 14px pitch, ~55% opacity) → optional year tag on the corner (`signal-marker`, ink border) → name below the card in Gambetta `headline` size → role in a `TabLabel` (`FOUNDER · AGNIKUL`).

**Motion:** card rises in (Smooth, `dur-normal`) → name fades in (200ms) → role tag extends (Settle, `dur-quick`). A second card follows 300ms later, mirrored rotation (+2°).

**Rules:** real, licensed photos only, credited in the source line if not public domain. No portraits of private individuals without consent. Role is a fact (title and organisation), never a description.

**You provide:** the photo, the name, the role and (optionally) the year.
