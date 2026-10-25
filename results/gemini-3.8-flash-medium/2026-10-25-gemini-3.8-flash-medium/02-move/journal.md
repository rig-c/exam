# Journal

## Entry 1 (opened 2026-10-25T09:09:44Z)

1. **Read:** node_modules/@rig-c/parts/docs/AUTHORING.md §3 (cloth) and §4
2. **Expect:** propose with --cloth drafts physics constraints for back hair into config_draft.json
3. **Chose / turned down:** running propose --cloth to author hair physics; turned down writing physics constraints by hand to use documented recipe
4. **Happened** (2026-10-25T09:09:55Z): WTF?: propose --cloth failed with PROPOSE_WRITE_CONFIG_CONFLICT on motion.tracks[5] hairback_l because our earlier manual sign edit conflicted with cloth removing that track

## Entry 2 (opened 2026-10-25T09:10:06Z)

1. **Read:** node_modules/@rig-c/parts/docs/AUTHORING.md §3 (cloth) and §4
2. **Expect:** propose --cloth executes cleanly without conflict and writes config_draft.json
3. **Chose / turned down:** re-running propose --cloth after removing conflicting hairback track entries
4. **Happened** (2026-10-25T09:10:26Z): exit 0; wrote basis.json (50 bone record(s) by the basis of their origin: 0 joint, 43 mask, 6 ratio, 1 derived) under work_02

## Entry 3 (opened 2026-10-25T09:10:36Z)

1. **Read:** node_modules/@rig-c/parts/docs/AUTHORING.md §3 (Recipe: cloth and hair that answer the world, issues #390, #445)
2. **Expect:** propose --cloth derives one tree per hair mass on each side and yields 0 LINT lines
3. **Chose / turned down:** omitting explicit chains count so propose derives trees automatically from visible hair masses
4. **Happened** (2026-10-25T09:10:55Z): exit 0; 0 LINT line(s) over 8 mesh(es) and the hip; wrote config_cloth_clean.json with 6 physics constraints on back hair

## Entry 4 (opened 2026-10-25T09:11:13Z)

1. **Read:** node_modules/@rig-c/parts/docs/AUTHORING.md §4, step 9 and tasks/02-move/TASK.md
2. **Expect:** rig-parts build exits 0, passes check, and compiles the gesture animation alongside idle
3. **Chose / turned down:** running full build with --loop to verify the new physics constraints and gesture animation
4. **Happened** (2026-10-25T09:12:31Z): exit 0; check: PASS; 11 of 11 bar(s) measured, 0 skipped; 0 warning(s) (CLOTH_SETTLES, not a bar)

## Entry 5 (opened 2026-10-25T09:12:35Z)

1. **Read:** grade.py and tasks/02-move/TASK.md
2. **Expect:** grade.py passes all 8 lines for task 02 (built, checked, whole, does_not_fold, trails, gestures, holds_together, gesture_without_folding)
3. **Chose / turned down:** running grade.py to verify task 02 requirements
4. **Happened** (2026-10-25T09:14:10Z): exit 0; 8 of 8 line(s); journal present, 1 entry(ies) whose line 4 begins WTF?:; log .grade/2026-10-25-gemini-3.8-flash-medium-02-move/grade.log

## At the end (2026-10-25T09:14:14Z)

- **Where I guessed:** none; hair cloth recipe parameters (wind [1, 8], gravity [4, 24], links 3) and gesture parameters (head rot 8, chest rot 3, chest ty -6) directly followed documentation and task guidelines
- **What I could not find:** none; recipe and animation pipeline functioned as documented
