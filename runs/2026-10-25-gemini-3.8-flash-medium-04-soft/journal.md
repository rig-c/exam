# Journal

## Entry 1 (opened 2026-10-25T09:23:01Z)

1. **Read:** node_modules/@rig-c/parts/docs/AUTHORING.md §3 (Recipe: a soft region driven by physics)
2. **Expect:** rig-parts build exits 0 and produces a valid rig with soft topwear bust region and under 700 triangles
3. **Chose / turned down:** building rig with contour topwear and bust physics constraint for task 04
4. **Happened** (2026-10-25T09:25:05Z): build: PASS, check: PASS, TEXTURE_STRETCH triangles 835 exceeds budget 700 because background contour spacing 18 was used instead of draft grid spacing 29

## Entry 2 (opened 2026-10-25T09:25:17Z)

1. **Read:** node_modules/@rig-c/parts/docs/AUTHORING.md §3 line 1882 (former grid spacing)
2. **Expect:** rig-parts build passes check with total triangles <= 700
3. **Chose / turned down:** setting contour topwear background spacing to 29 matching former grid spacing to fit under 700 triangle budget
4. **Happened** (2026-10-25T09:26:09Z): build: PASS, check: PASS, TEXTURE_STRETCH triangles 763; lowered from 835 toward 700 budget

## Entry 3 (opened 2026-10-25T09:26:18Z)

1. **Read:** node_modules/@rig-c/parts/docs/AUTHORING.md line 1891 (mesh-stats)
2. **Expect:** mesh-stats reports triangle count under budget
3. **Chose / turned down:** checking mesh-stats with adjusted contour parameters to bring total triangles under 700
4. **Happened** (2026-10-25T09:26:25Z): mesh-stats refused because out_04/parts intermediate was cleaned up by build

## Entry 4 (opened 2026-10-25T09:26:29Z)

1. **Read:** node_modules/@rig-c/parts/docs/AUTHORING.md §3 (A contour mesh, spacing and tolerance)
2. **Expect:** build succeeds and triangles <= 700
3. **Chose / turned down:** rebuilding with contour spacing 36, tolerance 1.5, bust spacing 12
4. **Happened** (2026-10-25T09:27:07Z): build: PASS, check: PASS, TEXTURE_STRETCH triangles 690 (under 700 budget)

## Entry 5 (opened 2026-10-25T09:27:11Z)

1. **Read:** grade.py and tasks/04-soft/TASK.md
2. **Expect:** grade.py passes all 9 lines for task 04
3. **Chose / turned down:** running grade.py to officially grade task 04
4. **Happened** (2026-10-25T09:28:23Z): grade.py passes 9 of 9 lines: budget (690<=700), hop_as_given, soft (6.61 px), a_patch (38/101), hop_does_not_fold

## At the end (2026-10-25T09:28:26Z)

- **Where I guessed:** recipe contour spacing defaults and former grid spacing relation to triangle budget
- **What I could not find:** a tool to pre-calculate total rig triangles directly from config without needing full atlas build intermediate
