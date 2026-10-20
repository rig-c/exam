# Journal — claude-sonnet-5-5, 04-soft, 2026-10-20

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry 1

1. **Read:** AUTHORING §3 'Recipe: a soft region driven by physics' (bone chest_jiggle under chest, topwear moved from grid to contour with a circle region and band, a physics constraint with x 0.5 y 1, inertia 0.25 strength 120 damping 0.92); 'Which mode comes out smaller' and 'A contour mesh' (When not to use it: contour uses more vertices than the lattice at the same spacing); recipe's Limits (band caps the displacement, TEXTURE_STRETCH).
2. **Expect:** build exit 0; hop carried from hop.json by motion.animations_from; topwear triangles rise from 86 to maybe 150-250, so the total goes from 590 to somewhere near or over 700 (risk to the Budget line); the soft displacement on hop around 4-7 rig px as on reference-sample; check PASS if the band holds.
3. **Chose / turned down:** Start from task 01's config (no hair physics, no wave: fewer unknowns) with topwear as contour tolerance 1.5 margin 1 spacing 30 stray 4 and a bust circle at (446,322) r 24 spacing 10 band 16. Turned down: copying the recipe's spacing 6 (cost: about 4x the vertices in the circle, I expect it to blow the 700 budget) and the wave config from task 02 (physics on hair adds nothing to triangles but a second thing to debug).
4. **Happened:** build exit 0, check PASS 10 of 10, but 'TEXTURE_STRETCH ... triangles 719': over the 700 budget; topwear went from 86 to 215 triangles (130 vertices, mode contour); hop carried, 1 physics constraint, folds 0. Expectation was 150-250 for topwear: right, and 'near or over 700': over by 19. No WTF.

## Entry 2

1. **Read:** Task 04 pass lines (Soft 3..15 px, A patch 8 vertices to 80%, Budget 700).
2. **Expect:** Grader: built/checked/whole/does_not_fold pass, hop-as-given pass, soft some value 3-15 (reference-sample read 6.7), patch plausible, hop no folds PASS, budget FAIL at 719.
3. **Chose / turned down:** Run the grader now to learn soft/patch before changing the triangle count, so the next edit changes only what has to change.
4. **Happened:** 8 of 9: only 'FAIL budget: 719 triangles against <= 700'; soft 6.61 rig px at hop frame 14 (3 to 15), a_patch 46 of 130 vertices, hop_as_given, hop_does_not_fold PASS. As expected; soft was in the range I guessed.

## Entry 3

1. **Read:** Recipe Limits: 'The region's band caps the displacement'; contour mode table (spacing governs triangle count); my topwear mesh_report: 130 vertices, 215 triangles.
2. **Expect:** Region spacing 10 -> 12 and background spacing 30 -> 36 cut topwear to about 150-185 triangles, total about 655-690 (<= 700); soft stays around 6 px (displacement comes from the spring, not the mesh density); patch vertices drop to about 30.
3. **Chose / turned down:** Coarsen the topwear mesh only. Turned down: coarsening other parts (handwear, hair), since they carry the idle motion checks and hair_front/bottomwear are not what the task asks me to touch; and shrinking the circle (it would change the displacement and patch share).
4. **Happened:** build PASS, check 10 of 10, 'triangles 667', topwear 163 triangles. Predicted 655-690: yes. No WTF.

## Entry 4

1. **Read:** Task 04 pass lines.
2. **Expect:** 9 of 9 PASS; soft around 6 px, patch about 30 of ~90 vertices.
3. **Chose / turned down:** Run grader.
4. **Happened:** 9 of 9 PASS: soft 6.61 (unchanged, so the displacement indeed did not depend on mesh density), patch 32 of 104, budget 667. No WTF.

## At the end

- **Where I guessed:** Bust circle position (446,322), radius 24 and band 16 were my guesses from the chest bone (446,325) and the recipe's r 28; I never looked at where the bust is on the topwear picture. Physics numbers are the recipe's (inertia 0.25, strength 120, damping 0.92). Spacings 36 and 12 were guessed to meet the budget. I would have needed the topwear part picture with a ruler, or a printed triangle count per part before building.
- **What I could not find:** How many triangles a contour region would cost before building (only mesh_report.json after a build says it); I did not view the chest with and without physics.
