# Journal — gpt-6-luna-medium, 04-soft, 2026-10-20

## Entry 1

1. **Read:** `tasks/04-soft/TASK.md` and `hop.json`; `node_modules/@rig-c/parts/docs/AUTHORING.md` §3 mesh contour row and §4 “Recipe: a soft region driven by physics” and “Limits”.
2. **Expect:** an authored chest region on `topwear`, a child jiggle bone under `hip`, and the given hop clip will produce a localized 3–15 px spring displacement while staying within the 700-triangle budget.
3. **Chose / turned down:** switch only `topwear` from grid to contour; use a 24 px circle at the chest with 10 px region spacing and a 16 px band to limit displacement under the documented cost; parent the spring to `hip` because hop moves `hip`.
4. **Happened:** WTF?: grader found 816 triangles, over the 700 budget; the other 8 lines passed, with 6.61 px soft motion and 44/192 vertices moving.

## Entry 2

1. **Read:** `tasks/04-soft/TASK.md` pass lines; `hop.json` and the run config.
2. **Expect:** grader will report task 01's 4 bars, the exact hop clip, 3–15 px soft motion, a localized patch, no hop folds, and at most 700 triangles.
3. **Chose / turned down:** run the official grader; adjust the region or spring only if the measurements say the candidate misses a line.
4. **Happened:** WTF?: grader found 816 triangles, over the 700 budget; the other 8 lines passed, with 6.61 px soft motion and 44/192 vertices moving.


## Entry 3

1. **Read:** first grader output (`816 triangles against <= 700`); `node_modules/@rig-c/parts/docs/AUTHORING.md` §3 “A contour mesh,” which says coarser region spacing reduces vertices.
2. **Expect:** changing only `topwear.contour.regions[0].spacing` from 10 to 16 px will reduce the rig below 700 triangles while keeping at least 8 patch vertices moving and 3–15 px displacement.
3. **Chose / turned down:** coarsen the local region grid; keep the radius and band, which set the affected patch and its displacement cap.
4. **Happened:** WTF?: 16 px spacing reduced the rig from 816 to 762 triangles, still 62 over budget; patch readings remained within range.


## Entry 4

1. **Read:** second grader output (`762 triangles against <= 700`; 19 patch vertices move); `AUTHORING.md` contour recipe on region spacing.
2. **Expect:** changing the region spacing to 26 px will remove enough local vertices to pass the triangle budget while leaving at least 8 patch vertices active.
3. **Chose / turned down:** coarsen only the region interior and band grid again; keep physics parameters and band fixed to preserve the measured 6.61 px displacement.
4. **Happened:** WTF?: region spacing 26 px reduced the total to 732 triangles, still 32 above budget; soft motion remained 6.61 px with 14 patch vertices.


## Entry 5

1. **Read:** third grader output (`732 triangles against <= 700`; 14 of 150 patch vertices move); contour mesh documentation distinguishing background spacing from region spacing.
2. **Expect:** increasing only the background spacing from 18 to 24 px will cut enough non-patch vertices to reach 700 triangles while preserving the 14 moving patch vertices.
3. **Chose / turned down:** coarsen the mesh outside the region, preserving its spacing, radius, band, and physics values.
4. **Happened:** WTF?: the rig fell to 662 triangles, but only 7 vertices moved over 0.5 px, one short of the patch minimum; soft displacement stayed 6.61 px.


## Entry 6

1. **Read:** fourth grader output (`662 triangles`; `7 of 115` patch vertices move); contour mesh region-spacing guidance.
2. **Expect:** changing only region spacing from 26 to 24 px will add enough active patch vertices while remaining below 700 triangles.
3. **Chose / turned down:** slightly refine the local region grid; preserve background spacing 24 px and all physics parameters.
4. **Happened:** grader passed all 9 lines; 662 triangles, 6.61 px patch displacement, and 8 of 115 vertices moved over 0.5 px.
