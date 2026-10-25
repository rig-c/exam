# Journal

## Entry 1 (opened 2026-10-25T12:00:51Z)

1. **Read:** TASK.md 04 (soft chest: patch of topwear lagging on physics, hop exactly as hop.json, <= 700 triangles). AUTHORING 'Recipe: a soft region driven by physics' (bone + contour region + physics constraint; a region adds vertices; count them with rig-parts mesh-stats before the first build). Config: runs/…-04-soft/config.json = copy of task 01's config, then hand edits: bone chest_jiggle under chest at [403,325]; topwear mesh from grid 29 to contour (tolerance 1, margin 1, spacing 18, stray 4) with region bust (circle at 403,325 r 30, bone chest_jiggle, spacing 8, band 16); constraint bust_phys (physics, strength 120, damping 0.92, inertia 0.25); motion.animations_from 'animations.json' = a byte copy of tasks/04-soft/hop.json.
2. **Expect:** exit 0; 22 parts; uncovered_error_px 1812 (unchanged plan and painting)
3. **Chose / turned down:** Run assemble into runs/…-04-soft/work so mesh-stats can count triangles. Turned down: running mesh-stats on task 01's work/rig, since it has no contour mesh yet and the step must read this config's parts.
4. **Happened** (2026-10-25T12:01:30Z): exit 0; "22 part(s) on a 832x1216 rig" and "uncovered error px: 1812". Matched the expected 22 parts and 1812.

## Entry 2 (opened 2026-10-25T12:01:43Z)

1. **Read:** AUTHORING 'Recipe: a soft region driven by physics': 'A region adds vertices ... Before the first build, count them: rig-parts mesh-stats --config config.json --parts work/rig' (prints per-mesh triangles and the total). TASK.md 04 Budget: at most 700 triangles in the whole figure. Config: runs/…-04-soft/config.json (contour topwear with bust region spacing 8).
2. **Expect:** a per-mesh triangle line and a total; total over 700 if the bust region at spacing 8 is as dense as the recipe says (the recipe's own spacing 6 is finer than mine)
3. **Chose / turned down:** Run mesh-stats before any build. Turned down: building first, since the doc says to count before the first build.
4. **Happened** (2026-10-25T12:02:24Z): exit 0; "mesh-stats: topwear — contour 232 vertices, 409 triangles" and "mesh-stats: total 933 triangles over 8 mesh(es)". My expectation was a total over 700; 933 is over the 700 budget by 233, and topwear's contour is 409 of it.

## Entry 3 (opened 2026-10-25T12:02:40Z)

1. **Read:** Entry 2: total 933 over 700 with topwear contour 409. Next, the recipe's region spacing (its example uses 6) is what adds vertices; I hand-edited runs/…-04-soft/config.json region bust spacing 8 -> 10 to cut the count, the only change. Counting with mesh-stats again before any build.
2. **Expect:** topwear contour triangle count lower than 409; total at or under 700 if the cut is enough, otherwise still over
3. **Chose / turned down:** Re-count with mesh-stats at region spacing 10. Turned down: lowering the topwear contour spacing 18 instead, since the region is where the motion is and its spacing sets how the patch bends.
4. **Happened** (2026-10-25T12:02:52Z): exit 0; "mesh-stats: topwear — contour 190 vertices, 325 triangles" and "mesh-stats: total 849 triangles over 8 mesh(es)". The cut from spacing 8 to 10 took 84 triangles off, so 849 is still 149 over the 700 budget. My expectation was a count at or under 700 if the cut was enough; it was not enough, as the count is still above.

## Entry 4 (opened 2026-10-25T12:02:58Z)

1. **Read:** Entry 3: total 849, still 149 over the 700 budget (TASK.md 04 'keep the rig light: at most 700 triangles'). AUTHORING's recipe: the region's spacing adds vertices, and the mesh's own contour spacing sets the outline's lattice. I hand-edited runs/…-04-soft/config.json topwear contour spacing 18 -> 26 (keeping the bust region at spacing 10, the one motion-bearing spacing). Re-count with mesh-stats.
2. **Expect:** topwear contour triangles well below 325; total at or under 700; if not, I will cut the region spacing further
3. **Chose / turned down:** Lower the outline's spacing rather than the bust region's, to keep the physics patch fine. Turned down: removing the bust's band to save vertices, since band is what carries the patch's edge.
4. **Happened** (2026-10-25T12:03:06Z): exit 0; "mesh-stats: topwear — contour 158 vertices, 261 triangles" and "mesh-stats: total 785 triangles over 8 mesh(es)". The spacing 18 -> 26 cut 64 triangles, but 785 is still 85 over the 700 budget. My expectation was a count at or under 700, which was not reached; the outline lattice was cheaper than I guessed but not enough.

## Entry 5 (opened 2026-10-25T12:03:10Z)

1. **Read:** Entry 4: 785 over 700. Hand-edited runs/…-04-soft/config.json topwear contour spacing 26 -> 34 (the outline, not the bust region). Re-count with mesh-stats.
2. **Expect:** topwear contour under 261 triangles; total at or under 700 if the outline's share is about 150 less
3. **Chose / turned down:** Raise the outline spacing again before touching the region. Turned down: shrinking the bust circle's radius, since the bust is the physics patch and its radius is what the grader's A-patch line counts against.
4. **Happened** (2026-10-25T12:03:21Z): exit 0; "mesh-stats: topwear — contour 151 vertices, 247 triangles" and "mesh-stats: total 771 triangles over 8 mesh(es)". Spacing 26 -> 34 cut 14 triangles, so the outline is near its floor. 771 is still 71 over the 700 budget, and the other seven meshes already hold 524 of it, so topwear must come under 176. My expectation was under 261 and a total at or under 700; the total is under 785 but still over 700.

## Entry 6 (opened 2026-10-25T12:03:26Z)

1. **Read:** Entry 5: 771, still 71 over. The seven non-topwear meshes hold 524 triangles, so topwear must reach 176. Hand-edited runs/…-04-soft/config.json region bust spacing 10 -> 16 (fewer vertices in the patch; its band still 16). Re-count with mesh-stats.
2. **Expect:** topwear under 247; total near 700, possibly under if the patch's share falls by about 70
3. **Chose / turned down:** Coarsen the region spacing one step (10 -> 16), leaving the outline at 34. Turned down: the outline at 40, because the outline's last gain (26 -> 34) was only 14 triangles.
4. **Happened** (2026-10-25T12:03:33Z): exit 0; "mesh-stats: topwear — contour 101 vertices, 147 triangles" and "mesh-stats: total 671 triangles over 8 mesh(es)". Under the 700 budget. Expected under 700 with the region spacing at 16: matched.

## Entry 7 (opened 2026-10-25T12:03:34Z)

1. **Read:** TASK.md 04 pass lines: Budget <= 700 triangles (now 671 by mesh-stats); Soft: on hop, topwear differs from the no-physics build by 3-15 rig px at its furthest vertex; A patch: >= 8 of topwear's vertices move > 0.5 px, <= 80%; Hop does not fold; Built and checked. AUTHORING step 9: build. Config: runs/…-04-soft/config.json (contour topwear, chest_jiggle bone, bust_phys constraint); animations.json = hop.json byte copy.
2. **Expect:** exit 0 with check PASS, or a named FAIL (for example the constraint's strength or damping failing a stretch bar)
3. **Chose / turned down:** Run the exact task command (no --loop) into runs/…-04-soft/out. Turned down: --loop, as before.
4. **Happened** (2026-10-25T12:04:08Z): exit 0; "[check] check: PASS; 11 of 11 bar(s) measured, 0 skipped; 0 warning(s)" and "build: PASS — the packed atlas is the artifact". Expected PASS with one physics constraint; the rig reports "physicsConstraints=1" and "animations=2" (idle and hop). TEXTURE_STRETCH PASS at severity 1.119; ANIMATIONS_DO_NOT_FOLD PASS with 1 physics constraint on and off. The soft and patch amounts are not in this output; the grader measures them.

## Entry 8 (opened 2026-10-25T12:04:10Z)

1. **Read:** TASK.md 04 pass lines (Soft: topwear differs 3-15 rig px at its furthest vertex on hop vs no-physics; A patch: >= 8 vertices move > 0.5 px, <= 80%; Budget <= 700; Hop as given). The grader builds my config twice (with and without physics) and poses hop; grade.py's own constants are the proctor's.
2. **Expect:** PASS built, checked, whole, does_not_fold; soft line: the bust constraint's displacement likely below 3 px at strength 120 (the reference's hop moved the bust 6.7), so I expect FAIL on soft or patch
3. **Chose / turned down:** Run grade.py on the 04 run. Turned down: tuning strength before the first grader reading, since the reading tells me which direction to move.
4. **Happened** (2026-10-25T12:05:29Z): exit 0; grader printed "9 of 9 line(s)", PASS soft "6.61 rig px at hop frame 14, against 3.0 to 15.0", PASS a_patch "22 of 101 topwear vertices move over 0.5 rig px", PASS budget "671 triangles against <= 700", PASS hop_as_given. My expectation was FAIL on soft (below 3 px); it was not: the bust constraint moved topwear 6.61 px, close to the AUTHORING reference's 6.7 for its hop. Nothing failed on the first grader run.

## At the end (2026-10-25T12:05:29Z)

- **Where I guessed:** The physics values (inertia 0.25, strength 120, damping 0.92, mass 1, mix 1, x 0.5, y 1) are the AUTHORING reference's constraint for a bust, copied, not tuned to hop; the bust position (403,325) and circle radius 30 are my reading of the landmarks picture, not a measure. The contour's tolerance 1 and margin 1 are the reference's values.
- **What I could not find:** Whether the topwear's outline spacing 34 and the bust spacing 16 are the best trade of triangles and motion (I only read the mesh-stats totals and the grader's soft figure); and whether the patch reads as soft to a person, which the grader does not judge.
