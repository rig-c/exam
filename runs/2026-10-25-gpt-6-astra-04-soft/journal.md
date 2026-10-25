# Journal

## Entry 1 (opened 2026-10-25T11:41:17Z)

1. **Read:** AUTHORING soft region recipe and mesh-stats; TASK04 budget; task01 landmarks
2. **Expect:** Coarser lattices plus one contour patch should approach 700 triangle budget; mesh-stats gives exact count before expensive build.
3. **Chose / turned down:** Copy task01, grids 50, topwear contour spacing40 with circle [425,335] r28 band22 spacing14; new chest_jiggle physics uses recipe .25/120/.92. Copy hop exactly. Do not add dense spacing6 recipe unexamined.
4. **Happened** (2026-10-25T11:41:31Z): WTF?: Only 397 triangles over 8 meshes, substantially below the 700 budget I was approaching; grid50 is unnecessarily coarse, so I can spend some budget on grid40.

## Entry 2 (opened 2026-10-25T11:41:32Z)

1. **Read:** mesh-stats total397 at grid50; contour171 unchanged
2. **Expect:** Grid40 should improve deformation sampling while keeping total including rigid regions below 700.
3. **Chose / turned down:** Refine seven lattice meshes to grid40, keep contour patch unchanged; count again before build.
4. **Happened** (2026-10-25T11:41:38Z): mesh-stats: total 483 triangles over 8 mesh(es); ample room below 700 for rigid attachments.

## Entry 3 (opened 2026-10-25T11:41:39Z)

1. **Read:** mesh-stats483; soft-region recipe physics example; TASK04 hop comparisons
2. **Expect:** Full grader should pass budget and hop integrity; recipe physics should produce 3-15px displacement limited to patch, no folds.
3. **Chose / turned down:** Grade this grid40 contour configuration and exact supplied hop before changing spring or band further.
4. **Happened** (2026-10-25T11:43:44Z): 9 of 9 line(s); budget483, soft6.61 at frame14, patch35 of113 vertices, exact hop and no folds.

## At the end (2026-10-25T11:43:44Z)

- **Where I guessed:** Patch center425,335 read visually from task01 overlay; r28 from recipe, band22 and spacing14/40 chosen to balance deformation and triangle budget. Initial grid50 then grid40 chosen empirically with mesh-stats. Spring values copied from documented recipe.
- **What I could not find:** No blocking package gaps. Mesh-stats made budget tuning cheap before the two-build physics comparison.
