# Journal

## Entry 1 (opened 2026-10-25T09:00:56Z)

1. **Read:** node_modules/@rig-c/parts/docs/AUTHORING.md §4, step 6
2. **Expect:** assemble --propose-plan exits 0 and writes assemble.plan and extend_below_crop into config.json
3. **Chose / turned down:** proposing plan with assemble --propose-plan; turned down writing plan by hand to let the tool inspect layer plausibility and order
4. **Happened** (2026-10-25T09:01:22Z): exit 0; added assemble.plan and extend_below_crop to config.json

## Entry 2 (opened 2026-10-25T09:01:26Z)

1. **Read:** node_modules/@rig-c/parts/docs/AUTHORING.md §4, step 7
2. **Expect:** assemble produces work/rig with parts.json and reports uncovered holes
3. **Chose / turned down:** running assemble to produce parts for propose; turned down manual part splitting
4. **Happened** (2026-10-25T09:02:05Z): exit 0; recomposite vs source uncovered error px: 1812 well below 3700 threshold

## Entry 3 (opened 2026-10-25T09:02:11Z)

1. **Read:** node_modules/@rig-c/parts/docs/AUTHORING.md §4, step 7
2. **Expect:** propose drafts bones, meshes, regions, motion and writes them into config.json via --write-config
3. **Chose / turned down:** running propose --parts with --write-config to draft rig elements; turned down authoring skeleton from scratch
4. **Happened** (2026-10-25T09:02:26Z): exit 0; wrote proposal.json (23 bone entries, 8 meshes) and render/landmarks.png (+_head) under work

## Entry 4 (opened 2026-10-25T09:02:40Z)

1. **Read:** node_modules/@rig-c/parts/docs/AUTHORING.md §4, step 8
2. **Expect:** propose --from-config runs cleanly with 0 LINT lines after giving hairback_l positive amplitudes
3. **Chose / turned down:** checking corrected config with propose --from-config; turned down running full build directly to verify lint first
4. **Happened** (2026-10-25T09:02:56Z): exit 0; 0 LINT line(s) over 8 mesh(es) and the hip after correcting hairback_l amplitude

## Entry 5 (opened 2026-10-25T09:03:02Z)

1. **Read:** node_modules/@rig-c/parts/docs/AUTHORING.md §4, step 9 and tasks/01-build/TASK.md
2. **Expect:** rig-parts build exits 0, check passes all bars, and idle renders without folding
3. **Chose / turned down:** running full build with --loop to verify assembled rig against all check bars
4. **Happened** (2026-10-25T09:04:36Z): exit 0; check: PASS; 11 of 11 bar(s) measured, 0 skipped and build completed successfully

## Entry 6 (opened 2026-10-25T09:04:42Z)

1. **Read:** README.md, grade.py, and tasks/01-build/TASK.md
2. **Expect:** grade.py passes all 4 lines (built, checked, whole, does_not_fold)
3. **Chose / turned down:** running grade.py to officially grade the task 01 run
4. **Happened** (2026-10-25T09:05:49Z): exit 0; 4 of 4 line(s); journal present, 0 entry(ies) whose line 4 begins WTF?:; log .grade/2026-10-25-gemini-3.8-flash-medium-01-build/grade.log

## At the end (2026-10-25T09:05:54Z)

- **Where I guessed:** none; rig_scale 0.5 and head_box from seethrough.json, bones/meshes from propose, and hairback_l positive sign from LINT recommendation
- **What I could not find:** none; standard workflow documented in AUTHORING.md §4 was followed
