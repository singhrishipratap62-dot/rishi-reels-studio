# TabLabel

A small boxed name tag with a signal tab on its left edge and a hairline leader to the thing it names.

**Use for:** naming parts of a diagram, objects in an illustration, places on a map, people or devices in a photo (`THE SUN`, `GPU RACK`, `SOUTH POLE`). Also the base for coordinate and date tags.

**Anatomy:** 2px `ink` hairline box on `bg` → 10px `signal` tab flush on the left → text in `label` uppercase Semibold, tracking 0.12em, padding 12×16px → a 2px `ink` leader from the box to the exact point it names. Variants: **coordinate tag** (`signal-marker` fill: `SRIHARIKOTA · 13.72°N 80.23°E`), **date tag** (`30 MAY 2024`), **ink tag** on dark grounds (paper box, ink text).

**Motion:** leader draws from the object (Draw, `dur-quick`) → box scales out from its tab edge (Settle, `dur-quick`) → text is simply there (names don't type). Several labels stagger 120ms. Exit all together, 100ms.

**Rules:** names only — 1–3 words, no opinions (that's a `Callout`). Up to 4 on a frame. Leaders never cross each other or the text. Keep at 32px minimum.

**You provide:** the names and the point each one attaches to.
