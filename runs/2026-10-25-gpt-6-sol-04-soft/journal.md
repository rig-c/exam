# Journal

## Entry 1 (opened 2026-10-25T08:52:04Z)

1. **Read:** AUTHORING soft region recipe: contour adds vertices; mesh-stats before build; task 04 700 triangle budget
2. **Expect:** mesh-stats total at most 700 triangles, or a number indicating need coarser spacing
3. **Chose / turned down:** Copy task01 config, add chest_jiggle circle at left breast 379,335 with documented spring and exact hop; count triangles first
4. **Happened** (2026-10-25T08:52:10Z): mesh-stats: total 787 triangles over 8 mesh(es); above 700, so coarsen contour and region spacing

## Entry 2 (opened 2026-10-25T08:52:15Z)

1. **Read:** mesh-stats 787 triangles, target <=700; AUTHORING contour spacing controls density
2. **Expect:** coarser contour reduces at least 87 triangles, total <=700
3. **Chose / turned down:** Set contour spacing 42, tolerance 2, region spacing 14; retain region radius and band
4. **Happened** (2026-10-25T08:52:21Z): WTF?: CONTOUR_COVERAGE says tolerance 2 margin 1 clips 8 art pixels; increase margin to 2 before counting.

## Entry 3 (opened 2026-10-25T08:52:25Z)

1. **Read:** CONTOUR_COVERAGE refusal: 8 pixels outside at tolerance2 margin1
2. **Expect:** mesh stats now cover art and total <=700 triangles
3. **Chose / turned down:** Increase margin to 2 while preserving coarser contour spacing
4. **Happened** (2026-10-25T08:52:29Z): mesh-stats: total 646 triangles over 8 mesh(es), within 700

## Entry 4 (opened 2026-10-25T08:52:32Z)

1. **Read:** mesh-stats 646 triangles; AUTHORING soft region physics recipe; task04 hop exact
2. **Expect:** build exits 0, check PASS, 646 triangles and hop has no folds
3. **Chose / turned down:** Build counted config with chest_jiggle contour region and documented spring values
4. **Happened** (2026-10-25T08:53:08Z): check: PASS; 11 of 11 bar(s) measured; TEXTURE_STRETCH reports 646 triangles and hop has 0 folding meshes

## Entry 5 (opened 2026-10-25T08:53:12Z)

1. **Read:** Task04 soft 3..15 rig px and patch 8..80%; build PASS 646 triangles
2. **Expect:** grader prints nine PASS if spring displacement and patch coverage fall in bounds
3. **Chose / turned down:** Run official grader; adjust region or spring only on measured failure
4. **Happened** (2026-10-25T08:54:12Z): 9 of 9 line(s); topwear physics difference 6.61 rig px; 32 of 77 vertices move; 646 triangles

## At the end (2026-10-25T08:54:14Z)

- **Where I guessed:** chest patch center 379,335 and radius30 were chosen from painting; contour spacing42 region spacing14 margin2 tuned by mesh-stats and coverage refusal; spring fields from AUTHORING reference-sample recipe
- **What I could not find:** CONTOUR_COVERAGE runtime refusal identified tolerance2 margin1 clipping 8 art pixels; margin2 fixed it
