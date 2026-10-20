# Journal — gemini-4-argon-high, 04-soft, 2026-10-20

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry 1

1. **Read:** `tasks/04-soft/TASK.md`, `tasks/04-soft/hop.json`, and `node_modules/@rig-c/parts/docs/AUTHORING.md` §3 (*Recipe: a soft region driven by physics*, lines 1236–1311).
2. **Expect:** Copying `tasks/04-soft/hop.json` into the run directory, writing `config.json` from task 01's config with bone `chest_jiggle` at `[446, 325]` under `chest`, `meshes.topwear` switched to `contour` (`tolerance: 1, margin: 1, spacing: 31, stray: 4`, region `bust` circle `cx: 446, cy: 325, r: 28, bone: "chest_jiggle", spacing: 12, band: 16`), `motion.animations_from: "hop.json"`, and `bust_phys` constraint (`x: 0.5, y: 1, inertia: 0.25, strength: 120, damping: 0.92, mass: 1, mix: 1`), then running `npx rig-parts build` will exit 0 with `check: PASS; 10 of 10 bar(s) measured` and total triangles `<= 700`.
3. **Chose / turned down:** Chose background `spacing: 31` (matching `topwear`'s proposed `grid: 31`) and region `spacing: 12` to stay within the 700-triangle budget (the other 7 meshes already take 504 triangles); turned down copying the recipe's `spacing: 18` and region `spacing: 6` verbatim because that would push total triangles above 700.
4. **Happened:** WTF?: Exited 0 and passed all 10 check bars (`ANIMATIONS_DO_NOT_FOLD: PASS` over `idle` and `hop`), but total triangles was 718 (18 over the 700 budget) because `topwear` at `tolerance: 1` and region `spacing: 12` produced 70 hull vertices and 143 total vertices (214 triangles, `region bust->chest_jiggle reaches 46 (21 whole)`), whereas I expected `spacing: 12` to stay under 196 triangles.

## Entry 2

1. **Read:** The `[rig] mesh topwear v= 143 t= 214 hull= 70 ... region bust->chest_jiggle reaches 46 (21 whole)` output line from `rig-parts build` and `tasks/04-soft/TASK.md` (Budget <= 700 triangles, A patch >= 8 vertices).
2. **Expect:** Increasing `meshes.topwear.contour.regions[0].spacing` from `12` to `18` in `config.json` and running `npx rig-parts build` will exit 0 with `check: PASS`, reduce `topwear` to ~165 triangles and total triangles to ~670 (`<= 700`), and still reach >= 20 vertices on `bust->chest_jiggle`.
3. **Chose / turned down:** Chose raising the `bust` region's `spacing` from `12` to `18` since 46 reached vertices at spacing 12 is far above the 8-vertex minimum; turned down raising `contour.tolerance` above 1 because `AUTHORING.md` §3 warns that larger tolerances can leave art uncovered at margin 1.
4. **Happened:** Exited 0 with `check: PASS; 10 of 10 bar(s) measured, 0 skipped`, `slot topwear, triangles 150`, and total `triangles 654` (`<= 700`).

## Entry 3

1. **Read:** `tasks/04-soft/TASK.md` (Pass lines: Built, Checked, Whole, Does not fold, Hop as given, Soft, A patch, Hop does not fold, Budget) and `grade.py`.
2. **Expect:** Running `python3 grade.py runs/2026-10-20-gemini-4-argon-high-04-soft` will exit 0, print `9 of 9 line(s)` (`budget: "654 triangles against <= 700"`, `hop_as_given`, `soft` ~6.7 rig px between 3.0 and 15.0, `a_patch` between >= 8 and <= 80%, `hop_does_not_fold: []`), and write `result.json`.
3. **Chose / turned down:** Chose to run `grade.py` directly on the 654-triangle build; turned down tuning `bust_phys` parameters further before seeing the measured hop displacement.
4. **Happened:** Exited 0 with `9 of 9 line(s)` passed (`budget: "654 triangles against <= 700"`, `hop_as_given`, `soft: "topwear differs from the same build without its physics by 6.61 rig px at hop frame 14, against 3.0 to 15.0"`, `a_patch: "14 of 111 topwear vertices move over 0.5 rig px, against >= 8 and <= 80 %"`, `hop_does_not_fold: []`), writing `result.json`.

## At the end

1. **Where time went:** One extra build to raise the `bust` region `spacing` from `12` to `18` after `tolerance: 1` on `topwear` produced 214 triangles (718 total) instead of staying under 700.
2. **What in `@rig-c/parts` or `rig-c` got in the way:** `rig-parts propose` does not offer a dry-run triangle count estimate for `contour` meshes with `regions` before running the full build, so finding the exact triangle count of a contour + region override requires running `rig-parts build`.



