# Journal — claude-opus-5-5, 04-soft, 2026-10-20

## Entry 1

1. **Read:** AUTHORING §3 *Recipe: a soft region driven by physics* (a bone the config authors under `chest`, a `contour` mesh region handing the patch to it, a `physics` constraint `x: 0.5, y: 1, inertia 0.25, strength 120, damping 0.92, mass 1, mix 1`; on reference-sample's `hop` — the same keys as this task's `hop.json` — the bust moved at most 6.702 rig px; "The region's `band` caps the displacement"); *A contour mesh* (outline at tolerance 1 is dense; "on the examples' 13 parts the contour mesh used more vertices than the lattice at the same spacing"); *Which mode comes out smaller*. My task-01 build: 590 triangles in all, `topwear` a grid-31 lattice of 58 v / 86 t, box 350,210 171x218; on `work`'s `parts/topwear.png` the bust sits around image (85,110), i.e. rig (435,320).
2. **Expect:** `build` exits 0, `check: PASS; 10 of 10`, the `[rig] mesh topwear` line now `contour` with somewhere around 150–200 triangles, total under 700 (so the topwear may grow by at most 110 triangles over 86).
3. **Chose / turned down:** start from task 02's config (wave, lock physics) and put `wave` and `hop` (copied byte for byte from `hop.json`) in one `animations.json`; add bone `chest_jiggle` under `chest` at [436,318]; `topwear` → `contour {tolerance 1.5, margin 1, spacing 31, stray 4, regions: [bust circle cx 436 cy 318 r 28, bone chest_jiggle, spacing 12, band 16]}` keeping its `r` and `segments`; physics `bust_phys` with the recipe's values. Turned down the recipe's own `tolerance 1` and region spacing 6 because of what the docs say they cost in vertices against a 700-triangle budget; turned down `auto` (more knobs, and the section says it is not always smaller).
4. **Happened:** exit 0, `check: PASS; 10 of 10`; `mesh topwear v= 112 t= 179 … contour tol=1.5 … region bust->chest_jiggle reaches 42 (23 whole)`; TEXTURE_STRETCH counts `triangles 683` — under 700 by 17, the topwear grew 86 → 179 (my guess was 150–200). The fold reading again left all 9 physics constraints out, so it does not tell me whether the bust folds on `hop` with physics on.

## Entry 2

1. **Read:** `rigc render --help` (`--folds`, `--geometry`); TASK.md *Soft* (3–15 rig px at the furthest vertex, physics against no physics), *A patch* (≥ 8 vertices over 0.5 px, ≤ 80 %).
2. **Expect:** `hop` rendered with physics on: 0 folding meshes. The recipe's 6.702 rig px on reference-sample suggests a furthest-vertex difference of roughly 5–8 px here, with about 42 of 112 vertices (the region's reach) moving — about 37 %.
3. **Chose / turned down:** render hop myself with physics on for folds, then let the grader measure the with/without difference rather than build a second rig by hand.
4. **Happened:** 31 frames at 30 fps, `0 of 8 mesh(es) fold` with physics on.

## Entry 3

1. **Read:** the prompt (grade.py); TASK.md pass lines.
2. **Expect:** 9 of 9 lines; soft 5–8 px; patch about 37 % of topwear's vertices; budget 683.
3. **Chose / turned down:** grade as built.
4. **Happened:** `9 of 9 line(s)`: budget 683 ≤ 700, hop as given, soft 6.61 rig px at hop frame 14 (the recipe's 6.702 on reference-sample, near enough), patch 34 of 112 vertices (30 %), no folds. As expected.

## At the end

- **Where I guessed:** the bust's centre [436,318] and radius 28 — read by eye off `out/parts/topwear.png` (the docs give reference-sample's numbers, not a way to find a bust); tolerance 1.5 and region spacing 12 — chosen to save triangles, no document gives a triangle count for a contour setting before you build it. Physics values copied from the recipe.
- **What I could not find:** a way to see a contour mesh's triangle count without running the whole build (one minute per try); I got under budget on the first try, with 17 to spare, by luck as much as by reading.
