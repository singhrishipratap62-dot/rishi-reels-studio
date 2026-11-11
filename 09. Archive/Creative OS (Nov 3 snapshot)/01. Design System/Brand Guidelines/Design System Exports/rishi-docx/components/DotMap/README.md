# DotMap

A dot-matrix map that pushes into a region, drops a pin, and pins a coordinate tag and a photo or logo card beside it.

**Use for:** any story with a place in it — a launch site, a company's city, where a law applies, where something happened.

**Anatomy:** dot field (10–12px dots on a 20–22px pitch): the land in focus in `ink`, other land in `line-strong`, sea dots in `line` → crop-mark corners and a `kicker` → pin: 28px `signal` dot with a 4px `bg` ring → a coordinate `TabLabel` (`PLACE · LAT°N LONG°E`) → optional photo card (paper card, 14px padding, label under the image, rotated 2–3°) or logo tile.

**Motion:** field fades in (200ms) → camera pushes in to the region (Cinematic, `dur-camera`) → pin drops (Settle, `dur-quick`) with one ring pulse → coordinate tag extends (150ms) → photo/logo card eases in (220ms). For world → country stories, start as a globe and rotate to the region before pushing in.

**Rules:** use accurate map outlines from a trusted source (Natural Earth or official boundary files; for India, use the official boundary). Never hand-draw a country. Coordinates must be real and checked. One pin per frame unless the point is the route between two.

**You provide:** the place, its verified coordinates, the map outline, and the photo or logo.
