# Journal

## Entry 1 (opened 2026-10-25T11:44:30Z)

1. **Read:** AUTHORING 'Recipe: a soft region driven by physics' (chest_jiggle bone under chest, topwear moved from grid to contour with a circle region on it, physics x 0.5 y 1 inertia 0.25 strength 120 damping 0.92) and its cost paragraph: 'count them: rig-parts mesh-stats --config config.json --parts work/rig'; task 01's build: 616 triangles, topwear 92 of them; TASK budget 700
2. **Expect:** exit 0; topwear contour well over its lattice's 92 triangles — maybe 200-300 (a tolerance-1 outline on a 178x190 part plus the region's 12 px grid), total over 700, so I will have to coarsen
3. **Chose / turned down:** config.json = task 01's (no hair physics, lighter) plus hop.json copied byte-for-byte as animations_from, chest_jiggle at [425,335] (centre of the chest on topwear.png, part px ~87,89 at @338,246), circle r 28 band 16 region spacing 12; mesh-stats over task 01's work/rig (same plan, same scale) before any build; turned down two side circles: one patch is what the recipe measured
4. **Happened** (2026-10-25T11:44:40Z): less than I feared: 'topwear — contour 125 vertices, 195 triangles' (+103 on the lattice's 92), 'total 719 triangles over 8 mesh(es)' — 19 over the 700 budget

## Entry 2 (opened 2026-10-25T11:44:40Z)

1. **Read:** mesh-stats: topwear contour 195 triangles, total 719; AUTHORING *A contour mesh*: 'at tolerance 1 the contour outline is dense'; the #106 window: tolerance 1.5 still covers at margin 1
2. **Expect:** topwear drops to ~170 triangles, total ~695, under 700; no CONTOUR_COVERAGE refusal
3. **Chose / turned down:** raise the outline's tolerance 1 -> 1.5, keeping the region spacing 12 so the patch stays finely weighted; turned down coarsening the region (it is what the soft line reads) or the hair lattices (they deform in the idle)
4. **Happened** (2026-10-25T11:44:51Z): as expected but with no slack at all: 'topwear — contour 106 vertices, 176 triangles', 'total 700 triangles over 8 mesh(es)' — exactly at the bar

## Entry 3 (opened 2026-10-25T11:44:51Z)

1. **Read:** TASK 04 build (task 01's command on this config); recipe's hop figures on reference-sample: bust moved at most 6.702 rig px at 30 fps with these physics values; check counts triangles (Budget line)
2. **Expect:** exit 0, check PASS 11 of 11, physicsConstraints=1, hop built beside the idle, ANIMATIONS_DO_NOT_FOLD reads idle and hop with 0 folding; triangles 700
3. **Chose / turned down:** build as is at 700 and read check's own count; turned down shaving more triangles before seeing whether the build passes at all
4. **Happened** (2026-10-25T11:45:57Z): as expected: 'check: PASS; 11 of 11 bar(s) measured', 'triangles 700', '(idle, hop): 0 folding mesh(es)'; topwear 'region bust->chest_jiggle reaches 44 (24 whole)' of 106 vertices (41.5 %, under the 80 % patch ceiling)

## Entry 4 (opened 2026-10-25T11:45:57Z)

1. **Read:** TASK 04 lines: Soft (topwear vs the no-physics build on hop, 3-15 rig px at its furthest vertex), A patch (8 to 80 % of vertices over 0.5 px), Budget <= 700; recipe: the bust moved at most 6.702 rig px on reference-sample's identical hop at 30 fps
2. **Expect:** all 9 lines PASS; soft somewhere 4-8 rig px (grader at 12 fps may sample below the 30 fps peak); patch ~30-44 of 106 vertices; budget 700
3. **Chose / turned down:** let the grader do the with/without-physics comparison (it builds both); turned down writing my own no-physics build first: the grader is allowed any number of times and is the same reading
4. **Happened** (2026-10-25T11:47:57Z): as expected: '9 of 9 line(s)', soft '6.61 rig px at hop frame 14, against 3.0 to 15.0', '36 of 106 topwear vertices move over 0.5 rig px', '700 triangles against <= 700'

## At the end (2026-10-25T11:47:57Z)

- **Where I guessed:** chest_jiggle at [425,335] and the circle r 28, band 16, region spacing 12 were read off topwear.png by eye; tolerance 1.5 chosen to fit the 700 budget from the #106 survey's window, not from this part. Physics values are the recipe's as tracked.
- **What I could not find:** Nothing said how check counts triangles against a budget it does not hold; mesh-stats and check agreed (700).
