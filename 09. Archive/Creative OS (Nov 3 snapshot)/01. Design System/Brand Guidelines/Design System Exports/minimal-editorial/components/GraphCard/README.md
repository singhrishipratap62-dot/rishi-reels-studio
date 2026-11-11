Graph and statistics scene: dark textured ground, thin glowing grid, white series line, blue ball on the line head, camera following the ball.

- Ground `graph-ground` + noise; grid `grid-line` at `grid` stroke; ball `blue-400` with glow.
- Sync every movement to a trigger word (one step per "up"; a flat line for "slow and steady").
- Labels `label-caps` with dashed reference lines; one key word may get a `highlight` box, which must visibly grow from zero (scaleX 0 → 1 over 480 ms, ease-in-out, starting ~120 ms before the word) before its words arrive one by one (M25) [R1.1].
- Keep the whole graph, end point and ball included, inside x 160–840 so it clears the Reels icon column [R1.1]. Every line extension gets a highlighter sound.
- Hold the finished graph ≥ 15 frames before cutting (revision #2). No ticks, legends or real chart clutter.
