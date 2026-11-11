# ScanWipe

A signal scan line sweeping across a frame, revealing the "after" state behind it.

**Use for:** before/after on the same image — blurry → sharp, original → edited, low-res → upscaled.

**Anatomy:** framed image (hairline border) with the before state underneath and the after state clipped from the left → 6px `signal` vertical line at the clip edge → small ink label chips (BEFORE / AFTER) in the corners.

**Motion:** line travels left to right with Cinematic easing (`dur-slow` to `dur-camera`), then fades. Hold on the after.

**You provide:** the two versions of the image.
