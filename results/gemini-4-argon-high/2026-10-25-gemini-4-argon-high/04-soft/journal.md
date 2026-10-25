# Journal

## Entry 1 (opened 2026-10-25T09:48:36Z)

1. **Read:** tasks/04-soft/TASK.md, tasks/04-soft/hop.json, and AUTHORING.md §3 Recipe: a soft region driven by physics and §4 Counting the triangles before a build
2. **Expect:** mesh-stats reports the contour topwear mesh and a total triangle count across all 8 meshes of at most 700
3. **Chose / turned down:** run rig-parts mesh-stats --config runs/2026-10-25-gemini-4-argon-high-04-soft/config.json --parts runs/2026-10-25-gemini-4-argon-high-01-build/out
4. **Happened** (2026-10-25T09:48:54Z): WTF?: mesh-stats: topwear — contour 112 vertices, 188 triangles; mesh-stats: total 712 triangles over 8 mesh(es), 12 over the <= 700 budget

## Entry 2 (opened 2026-10-25T09:49:32Z)

1. **Read:** Entry 1 mesh-stats output: total 712 triangles (topwear 188)
2. **Expect:** mesh-stats reports total triangles <= 700 after raising lattice grids to 32 and topwear contour spacing to 32 with bust region spacing 14
3. **Chose / turned down:** run rig-parts mesh-stats --config runs/2026-10-25-gemini-4-argon-high-04-soft/config.json --parts runs/2026-10-25-gemini-4-argon-high-01-build/out
4. **Happened** (2026-10-25T09:49:53Z): mesh-stats: topwear — contour 83 vertices, 130 triangles; mesh-stats: total 588 triangles over 8 mesh(es)

## Entry 3 (opened 2026-10-25T09:50:04Z)

1. **Read:** Entry 2 mesh-stats output: total 588 triangles over 8 mesh(es) (topwear contour 83 vertices, 130 triangles); TASK.md pass lines for task 04
2. **Expect:** grade.py passes all 9 lines (built, checked, whole, does_not_fold, budget <= 700, hop_as_given, soft 3..15 rig px, a_patch >= 8 and <= 80%, hop_does_not_fold)
3. **Chose / turned down:** run python3 grade.py runs/2026-10-25-gemini-4-argon-high-04-soft
4. **Happened** (2026-10-25T09:52:30Z): 9 of 9 line(s); PASS budget: "588 triangles against <= 700"; PASS soft: "`topwear` differs from the same build without its physics by 6.61 rig px at hop frame 14, against 3.0 to 15.0"; PASS a_patch: "21 of 83 `topwear` vertices move over 0.5 rig px, against >= 8 and <= 80 %"

## At the end (2026-10-25T09:52:41Z)

- **Where I guessed:** the initial bust region spacing (12 at grid 29), which came out to 712 triangles in mesh-stats before raising spacing to 32 / region spacing 14 (588 triangles)
- **What I could not find:** mesh-stats prints vertex and triangle counts per mesh and in total, but for contour meshes with regions it does not print the count or share of vertices reached by each region (g > 0 and g = 1, which mesh_report.json only writes after rig/build)
