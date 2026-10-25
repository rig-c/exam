# Journal

## Entry 1 (opened 2026-10-25T11:45:48Z)

1. **Read:** AUTHORING §3 'Recipe: a soft region driven by physics' (bone chest_jiggle, contour mesh with a circle region, physics constraint; mesh-stats before the first build)
2. **Expect:** mesh-stats prints a topwear contour line and a total; I expect the total to be under 700 (task 01 had 616 triangles, topwear 92 on a grid)
3. **Chose / turned down:** mesh-stats on a config copied from task 01 plus chest_jiggle bone at (427,340), topwear contour spacing 24 with one circle region r 40 spacing 10 band 16 on the bust centre read off topwear.png by eye, and bust_phys from the recipe; hop.json copied verbatim as animations.json. Turned down two side circles (more vertices against the 700 budget). Using task 01's work/rig parts
4. **Happened** (2026-10-25T11:45:55Z): WTF?: "mesh-stats: topwear — contour 192 vertices, 329 triangles" and "mesh-stats: total 853 triangles over 8 mesh(es)" — I expected the total under 700; the recipe warned a region adds vertices but the topwear contour alone is 329 vs 92 as grid. Over budget by 153.

## Entry 2 (opened 2026-10-25T11:45:55Z)

1. **Read:** previous mesh-stats: topwear 329 triangles, total 853; AUTHORING recipe 'A region adds vertices: its spacing is finer than the mesh's'
2. **Expect:** topwear falls to about 150-170 triangles and the total to about 680-700
3. **Chose / turned down:** coarser topwear contour (spacing 36, tolerance 2, maxEdge 40) and a smaller bust circle (r 30, spacing 16, band 14), hand-edited; turned down coarsening other parts (the 'Kept' line wants the eight meshes still deforming, but their triangles count)
4. **Happened** (2026-10-25T11:46:01Z): exit 1: "FAIL  CONTOUR_COVERAGE: contour mesh "topwear" — 8 of 27280 art pixel(s) (alpha above 8) lie outside the mesh at tolerance 2 px and margin 1 px" — expected a count; the refusal says raise margin or lower tolerance. No WTF: a refusal I had not predicted but its message is complete.

## Entry 3 (opened 2026-10-25T11:46:02Z)

1. **Read:** CONTOUR_COVERAGE refusal: 'raise the margin or lower the tolerance'
2. **Expect:** margin 2 at tolerance 2 covers the art; mesh-stats prints topwear near 150-180 triangles, total near 700
3. **Chose / turned down:** raise margin 1 to 2 (hand edit); turned down lowering tolerance (more edge vertices, more triangles)
4. **Happened** (2026-10-25T11:46:08Z): exit 0; "mesh-stats: topwear — contour 73 vertices, 114 triangles" and "mesh-stats: total 638 triangles over 8 mesh(es)" — under the 700 budget.

## Entry 4 (opened 2026-10-25T11:46:08Z)

1. **Read:** TASK.md 04; AUTHORING recipe 'Limits' (TEXTURE_STRETCH is read on the idle alone, not hop)
2. **Expect:** build exit 0, check PASS, hop built beside idle, ANIMATIONS_DO_NOT_FOLD PASS (maybe a stretch FAIL on topwear band from the spring)
3. **Chose / turned down:** build, then grade; no tuning of physics values before seeing grader's soft number
4. **Happened** (2026-10-25T11:47:10Z): exit=0; "build: PASS"; "check: PASS; 11 of 12 bar(s) measured"; "ANIMATIONS_DO_NOT_FOLD: PASS — 2 animation(s) ... with its 1 physics constraint(s) on and off (idle, hop)"; "TEXTURE_STRETCH: PASS — meshes 8; triangles 638".

## Entry 5 (opened 2026-10-25T11:47:10Z)

1. **Read:** TASK.md 04 pass lines
2. **Expect:** grader: soft number unknown; recipe values moved the bust 6.7 px on its own hop, so I expect 3-15 px and a patch share under 80%; hop as given PASS
3. **Chose / turned down:** grade as is
4. **Happened** (2026-10-25T11:48:48Z): exit 0; "9 of 9 line(s)"; soft: "`topwear` differs from the same build without its physics by 6.61 rig px at hop frame 14, against 3.0 to 15.0"; a_patch 20 of 73.

## At the end (2026-10-25T11:48:48Z)

- **Where I guessed:** bust centre (427,340) and radius 30 read by eye off topwear.png; mesh spacing 36, tolerance 2, margin 2, maxEdge 40 were chosen by trial against the triangle count; physics values copied from the recipe (inertia 0.25, strength 120, damping 0.92)
- **What I could not find:** Nothing said the contour mesh's triangle cost before mesh-stats; the recipe's own spacing (18/6) from reference-sample overshot the 700 budget by 153 triangles.
