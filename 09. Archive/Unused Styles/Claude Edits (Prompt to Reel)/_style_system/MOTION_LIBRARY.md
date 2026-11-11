# Motion Library v1.0
Timing from scene-change detection + 1 fps frames. Exact easing/durations = E unless noted.

| ID | Name | Behaviour | Dur | Conf |
|---|---|---|---|---|
| M01 | type-in | chars appear 12–15/s, keyboard key-pop magnifier, predictive word updates, caret blink 530 ms | 0.8–1.3 s | C (behaviour) |
| M02 | autocomplete-pop | chip fades+rises 8 px above composer when "/" typed | 200 ms | C |
| M03 | send-dismiss | send button press (scale .92), keyboard slides down, composer collapses, user bubble flies to top-right | 300–400 ms | C |
| M04 | status-shimmer | "Animating with /x…" text with moving highlight sweep | while processing | S |
| M05 | blur-reveal | output card appears blurred/dim (R05 frosted, R06 dot-matrix placeholder), sharpens + scales 0.96→1 | 400–700 ms | C |
| M06 | card-breakout | card scales to full-bleed (corner radius → 0) then back | 400 ms each way | C |
| M07 | word-select caption | each word fades in from 45% to 100%; active word gets blue selection box that snaps word-to-word | per word ~250 ms | C |
| M08 | odometer-count | numbers roll up with vertical motion blur, ease-out, settle | 1.5–2.5 s | C |
| M09 | counter-tick | header 1/3→2/3, list item ticks/highlights yellow | 150 ms | C |
| M10 | sticker-freeze | frame freezes, white outline draws around subject, name tag drops with tilt bounce | 500 ms | C (R05) |
| M11 | text-behind | huge word rises behind subject (masked) | 400 ms | C |
| M12 | fan-carousel | thumbnails slide sideways in perspective fan | continuous | C (R01 CTA) |
| M13 | grid-assemble | CTA thumbnails pop in staggered 60–80 ms | 0.6 s total | S |
| M14 | whip / hard cut | B family: hard cuts on the beat between effects; light-leak/flash wipe occasional (R02 3s, 15s) | 1–3 frames | C |
| M15 | pull-back reveal | camera pulls back from content to show it's on a phone/editor timeline (R02 16–17s, R03 21s) | 0.8 s | C |

Rhythm rules: A = one demo per 4–5 s, ≥ 3 sub-events inside (type, reveal, caption/count). B = scene change every 0.9–1.9 s (R06 cuts: 2.8, 4.7, 5.6, 7.5, 8.4, 10.3 …). Never hold a static frame > 2 s except CTA.
Audio (U): refs had audio, not analysed — likely key-click SFX on typing, whoosh on reveal, music bed.
