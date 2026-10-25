# Journal

## Entry 1 (opened 2026-10-25T09:54:44Z)

1. **Read:** AUTHORING Recipe: a soft region driven by physics, especially its mesh-stats cost warning; Task 04 budget <=700
2. **Expect:** mesh-stats accepts the adapted contour patch and totals at most 700 triangles, with topwear adding fewer than 84 triangles over its old 92
3. **Chose / turned down:** use the documented circle r28, band16 and physics values at this rig chest, but spacing 7 and outer spacing 29 to limit cost; turned down spacing 6 before measuring because the source rig already has 616 triangles
4. **Happened** (2026-10-25T09:54:48Z): WTF?: mesh-stats refused PARTS_FILE_PRESENT because I passed work instead of work/rig or the assembled output root expected by --parts; the message named missing work/parts.json.

## Entry 2 (opened 2026-10-25T09:54:51Z)

1. **Read:** mesh-stats refusal PARTS_FILE_PRESENT named the expected root-level parts.json; Task 01 out contains parts.json and parts/
2. **Expect:** mesh-stats runs on Task 01 out and reports a total at most 700 triangles
3. **Chose / turned down:** retry with --parts runs/...01-build/out; turned down work/rig because it has rig/parts.json rather than the root layout named by the refusal
4. **Happened** (2026-10-25T09:54:56Z): WTF?: mesh-stats reported "mesh-stats: total 919 triangles over 8 mesh(es)"; topwear alone was 395 triangles, so spacing 7 costs 219 triangles beyond the 176 available.

## Entry 3 (opened 2026-10-25T09:55:02Z)

1. **Read:** Previous mesh-stats: non-topwear meshes total 524, leaving at most 176 triangles for topwear; recipe says finer region spacing is the added cost
2. **Expect:** raising region spacing from 7 to 12 reduces topwear to at most 176 triangles and total to at most 700
3. **Chose / turned down:** measure spacing 12 while retaining r28 and band16; turned down shrinking the patch before testing the direct cost control
4. **Happened** (2026-10-25T09:55:08Z): WTF?: spacing 12 still reported "mesh-stats: total 727 triangles over 8 mesh(es)"; topwear was 203, 27 triangles over budget.

## Entry 4 (opened 2026-10-25T09:55:12Z)

1. **Read:** Spacing 12 measured topwear 203 triangles, 27 over the available 176; region spacing is the recipe cost control
2. **Expect:** spacing 14 drops at least 27 triangles, bringing total to <=700 while retaining enough regional vertices for the >=8 moved-vertex bar
3. **Chose / turned down:** increase to spacing 14; turned down shrinking radius because that changes the intended patch footprint
4. **Happened** (2026-10-25T09:55:17Z): mesh-stats reported "mesh-stats: total 687 triangles over 8 mesh(es)"; topwear is 109 vertices and 163 triangles, inside the 700 budget.

## Entry 5 (opened 2026-10-25T09:55:19Z)

1. **Read:** Task 04 command and soft-region recipe; mesh-stats measured 687 triangles with hop copied exactly
2. **Expect:** build exits 0, check passes, hop is built, physics is present, and folds remain zero
3. **Chose / turned down:** build the measured spacing-14 contour patch with documented physics; turned down further mesh changes because cost is already under budget
4. **Happened** (2026-10-25T09:56:17Z): build exited 0 with "check: PASS; 11 of 11 bar(s) measured, 0 skipped"; hop and one physics constraint were built and no animation folded.

## Entry 6 (opened 2026-10-25T09:56:19Z)

1. **Read:** Task 04 pass lines; build confirms hop and physics while grade compares against a no-physics rebuild
2. **Expect:** grader prints 9 of 9, soft displacement 3..15 px, at least 8 and at most 80% moved vertices, and 687 triangles
3. **Chose / turned down:** grade the documented physics values with measured budget; turned down tuning before observing the task-specific differential
4. **Happened** (2026-10-25T09:58:47Z): grader printed "9 of 9 line(s); journal present, 3 entry(ies) whose line 4 begins WTF?:"; soft displacement 6.61 px, 23/109 vertices moved, and budget 687.

## At the end (2026-10-25T09:58:50Z)

- **Where I guessed:** The initial adapted patch centre [403,330] came from this rig chest and topwear geometry; spacing 14 was measured before build, and all physics values came from the recipe.
- **What I could not find:** The mesh-stats help/doc example did not make clear that --parts wants the assemble output root rather than its rig subdirectory; the refusal supplied the missing shape.
