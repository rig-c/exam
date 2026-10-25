# Journal

## Entry 1 (opened 2026-10-25T09:09:03Z)

1. **Read:** AUTHORING soft-region recipe and contour weights; task04 <=700 triangles, unchanged hop; task01 landmarks chest patch around427,332
2. **Expect:** Mesh-stats constructs topwear contour patch and coarse grids, hopefully <=700 triangles before costly double build.
3. **Chose / turned down:** Copy corrected task01; grids60 chosen for budget, topwear contour spacing40 patch r28 spacing12 band24 at427,332. Documented physics .25/120/.92. Copy hop exactly; no keys on jiggle.
4. **Happened** (2026-10-25T09:09:19Z): "mesh-stats: total 399 triangles over 8 mesh(es)"; topwear221, leaves301 triangles of headroom. Use some of it for less coarse non-top meshes.

## Entry 2 (opened 2026-10-25T09:09:19Z)

1. **Read:** mesh-stats total399, topwear221 at grid60 leaves301 headroom
2. **Expect:** Grid40 raises non-top count but should remain <=700; topwear stays221.
3. **Chose / turned down:** Change seven grid spacings60 to40 for better silhouette and chain support; measure rather than spend budget blindly.
4. **Happened** (2026-10-25T09:09:30Z): "mesh-stats: total 533 triangles over 8 mesh(es)"; topwear221 unchanged. Budget leaves167 triangles for region attachments or later tuning.

## Entry 3 (opened 2026-10-25T09:09:30Z)

1. **Read:** Soft recipe measured6.702px for hop at physics .25/120/.92; mesh-stats533; task04 pass lines
2. **Expect:** Grader double build passes9 lines; patch displacement3..15 and8..80percent vertices, no hop folds.
3. **Chose / turned down:** Grade grid40 contour patch config with exact supplied hop; keep recipe physics rather than key soft bone.
4. **Happened** (2026-10-25T09:11:41Z): "9 of 9 line(s)" pass:533 triangles, soft6.61px,55of138 vertices >.5px, unchanged hop, no folds.

## At the end (2026-10-25T09:11:41Z)

- **Where I guessed:** Patch centre427,332 read visually from task01 landmarks, radius28 from recipe, band24 chosen wider than recipe16, spacing12/40 and grid40 chosen for triangle budget. Physics .25/120/.92 from recipe.
- **What I could not find:** No blocking missing instruction; mesh-stats answered budget cheaply and accurately.
