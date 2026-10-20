# Journal — gemini-3.8-flash-medium, 04-soft, 2026-10-20

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry 1

1. **Read:** `tasks/04-soft/TASK.md` and `tasks/04-soft/hop.json`.
2. **Expect:** `hop.json` created in the run directory matching `tasks/04-soft/hop.json` byte for byte.
3. **Chose / turned down:** Copied given `hop.json`; turned down modifying any hop keyframe or property as `hop_as_given` requires exact values.
4. **Happened:** Copied `tasks/04-soft/hop.json` into run directory.

## Entry 2

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §3 ("Recipe: a soft region driven by physics") and `tasks/04-soft/TASK.md` (triangle budget <= 700, soft displacement 3..15 px).
2. **Expect:** `config.json` authored with `chest_jiggle` bone, contour `topwear` mesh containing circular `bust` region, and `bust_phys` constraint, aiming for < 700 total triangles.
3. **Chose / turned down:** Set contour `spacing: 24` and region `spacing: 12` to keep mesh triangle count well within 700 budget; turned down the recipe's `spacing: 6` which grade.py notes produces ~920 triangles.
4. **Happened:** Created `config.json` with `chest_jiggle` bone, contour `topwear` (spacing 24, bust circle cx=446 cy=325 r=28 band=16 spacing=12), `bust_phys` constraint, and `hop.json` linked.

## Entry 3

1. **Read:** `grade.py` lines 245-263 and `tasks/04-soft/TASK.md` Pass lines.
2. **Expect:** `python3 grade.py runs/2026-10-20-gemini-3.8-flash-medium-04-soft` passes all 9 lines: built, checked, whole, does_not_fold, hop_as_given, soft, a_patch, hop_does_not_fold, budget (<= 700 triangles).
3. **Chose / turned down:** Running `grade.py` to test the soft chest rig against all task requirements.
4. **Happened:** WTF?: Expected all 9 lines to pass with under 700 triangles, but budget failed with 742 triangles (42 triangles over the 700 limit), though soft (6.61 px) and a_patch (38 of 155 vertices) passed cleanly.

## Entry 4

1. **Read:** `grade.py` output (742 triangles vs <= 700) and `node_modules/@rig-c/parts/docs/AUTHORING.md` §3 mesh contour parameters.
2. **Expect:** Coarser `topwear` contour spacing (30), bust region spacing (18), and `bottomwear` grid (34) will bring total triangle count below 700 without losing the soft patch effect.
3. **Chose / turned down:** Increased contour spacing to 30 and region spacing to 18 on `topwear`, plus `bottomwear` grid to 34; turned down making parts rigid or removing bust circle.
4. **Happened:** Updated `config.json` with `topwear.contour.spacing: 30`, `bust.spacing: 18`, and `bottomwear.grid: 34`.

## Entry 5

1. **Read:** `tasks/04-soft/TASK.md` Pass lines and `grade.py` lines 245-263.
2. **Expect:** `python3 grade.py runs/2026-10-20-gemini-3.8-flash-medium-04-soft` passes all 9 lines including budget (<= 700).
3. **Chose / turned down:** Re-running grader after spacing adjustments to confirm budget pass.
4. **Happened:** python3 grade.py passed all 9 of 9 lines (budget: 636 triangles <= 700; soft: 6.61 px; a_patch: 14 of 114 vertices).

## At the end

- **Where I guessed:** Coarsening contour spacing (30) and region spacing (18) to hit triangle budget without losing soft patch movement.
- **What I could not find:** Direct formula predicting total triangles from contour spacing and region spacing combinations prior to build.
