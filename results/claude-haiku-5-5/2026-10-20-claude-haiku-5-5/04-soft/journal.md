# Journal — claude-haiku-5-5, 04-soft, 2026-10-20

## Entry 1

1. **Read:** TASK.md (`hop.json` must be carried exactly; `topwear` must differ from its physics-free build by 3 to 15 rig px at its furthest vertex; at least 8 vertices move over half a rig px, at most 80 %; whole figure at most 700 triangles); AUTHORING §3 *Recipe: a soft region driven by physics* (a config-only bone under the patch, a contour-mode region on the part with `band`, a `physics` constraint); AUTHORING §3 `meshes.<part>.contour` (`budget` and `spacing` set the vertex count, so the triangle cost).
2. **Expect:** my task 02 rig (wave, hair physics) already holds some triangles. The 8 meshes were 590 triangles in task 01 and 722 in task 03 (the corrected build), so I may already be at or above the 700 budget once `topwear` is traced.
3. **Chose / turned down:** start from my own task 02 config (the chain 01 → 02 → 04 → 05 the TASK names) and add `hop` exactly as `hop.json` gives it into the same motion file as `wave`. Before adding anything for the soft chest, build this baseline and read its triangle count, so the cost of the recipe is measured and not guessed. Turned down: a fresh rig from task 01 (it would not carry the wave, and the task 05 rig is to come from this one).
4. **Happened:** `build` exit 0 with the baseline config (wave and hair physics, no soft region): `TEXTURE_STRETCH: PASS — meshes 8; triangles 590`. The rig's `mesh_report.json` lists topwear at 86 triangles (grid 31), so 700 leaves 110 more for a contour-mode topwear. Matches my expectation for the total; I had not expected the whole figure to be as light as 590.

## Entry 2

1. **Read:** AUTHORING §3 *Recipe: a soft region driven by physics* (the config fragment: a config-only bone under the part's bone, a `contour` mesh with a `circle` region on that bone, `band`, and a `physics` constraint with `x: 0.5, y: 1` for a single bone with no length); the recipe's `Limits` (the band caps the displacement); the chest bone in my config (`hip` → `chest` at (446, 325)); the topwear `segments` (chest and hip at x 446).
2. **Expect:** the topwear mesh goes from 86 triangles to about 130 to 190 (the bust patch at spacing 12 over an area of about 6,000 px²), so the total is still under 700. The physics on `chest_jiggle` should move the patch by a few rig px on `hop`.
3. **Chose / turned down:** a circle region of r 26 with band 16 centred on the chest at (446, 320), region `spacing` 12 (not the recipe's 6, which would cost about 4 times the vertices), background `spacing` 31 (the grid's own spacing), and a physics constraint with the recipe's values for a single bone (inertia 0.25, strength 120, damping 0.92). Turned down: copying the example's `r 28` and `band 16` at face value, since her chest is at a different place. The values are my choice (recorded in the `note`).
4. WTF?: `build` exit 0 and `check: PASS`, but `TEXTURE_STRETCH: PASS — meshes 8; triangles 708`. The topwear contour is 138 vertices and 204 triangles (`mesh topwear v= 138 t= 204 … contour … spacing=31 … region bust->chest_jiggle reaches 48 (18 whole)`), up from 86. The whole figure is 708, which is over the 700 budget the task names. I expected 590 + about 130 = about 720 at most, so the estimate was rough; I had not expected to be over.

## Entry 3

1. **Read:** the `triangles 708` figure above; the task's `Budget` line (at most 700 triangles); AUTHORING §3 `meshes.<part>.contour` (`spacing` is the background interior spacing, `regions[].spacing` the region's, and both set the vertex count).
2. **Expect:** a larger background `spacing` (31 → 36) and a larger region `spacing` (12 → 15) take out at least 8 triangles, so the total falls below 700. Both are coarser than the bust's own shape needs, so the outline is kept and the patch still moves.
3. **Chose / turned down:** widen both spacings by a few pixels, rather than drop the band or the region (which would change the patch). Turned down: removing the `physics` constraint's region to save triangles (the patch is the thing being measured).
4. **Happened:** `build` exit 0 and `TEXTURE_STRETCH: PASS`, with `triangles 664` (under 700), `topwear v= 116 t= 160`. I expected spacing 36 and 15 to take out about 8 triangles; they took out 44, and the figure is 664. Matches the outcome I wanted; the drop was bigger than my estimate.

## Entry 4

1. **Read:** the task's `Soft` and `A patch` pass lines (3 to 15 rig px at its furthest vertex; at least 8 of topwear's vertices move over half a rig px, at most 80 %); the grader's method (it builds the rig twice, once without any physics constraint, and reads the furthest-vertex difference on `hop`).
2. **Expect:** with the physics the topwear patch differs from the no-physics build by a few rig px on `hop`. The recipe warns the spring answers a fast key on its parent (`hip` keys up 24 at 0.3 s), so this should be larger than the idle's 0.1.
3. **Chose / turned down:** build the same config minus every constraint into `out_nophys` (under `work/`, in the same way the task describes), then render `hop` with `rigc render --geometry` on both and compare the topwear vertices. Turned down: judging by a picture of the chest alone (the grader's line is numeric, and the picture is a second check after the numbers).
4. WTF?: the no-physics twin first failed: `build: stopped at assemble … CONFIG_FILE_PRESENT: config.motion.animations_from — names …/work/animations.json`. The path is relative to the config's own folder, not to where I ran the command, and I had only put the config in `work/`. Copying `animations.json` beside it fixed that, and the twin built (exit 0). Then I rendered `hop` at 24 fps with `--geometry --folds` on both: `0 of 8 mesh(es) fold` on each. My own measure (`work/measure_soft.py`, comparing topwear's 116 vertices frame by frame): furthest difference 6.305 rig px (frame 11, vertex 70), 20 of 116 vertices differ by more than 0.5 px at some frame (17.2 %). The soft region moves, and it moves a patch, not the garment. I had not expected this: when I measured the travel from rest, all 116 vertices travel over 0.5 px, since the whole top rides the hip. That is why the patch line has to be read as a difference from the no-physics build, not as travel from rest.

## At the end

- **Where I guessed:** the physics values `inertia 0.25`, `strength 120`, `damping 0.92` are the recipe's, not tuned on this hop; the patch centre (446, 320), radius 26 and band 16 are my reading of the chest in the rig. The `spacing` values 36 and 15 were chosen to bring the total under 700, not from a measurement of the patch.
- **What I could not find:** whether the rig should carry the patch's physics only, or a second constraint on the bust's far side; the recipe shows one bone.
