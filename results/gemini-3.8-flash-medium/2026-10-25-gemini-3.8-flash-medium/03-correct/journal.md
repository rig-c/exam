# Journal

## Entry 1 (opened 2026-10-25T09:16:08Z)

1. **Read:** node_modules/@rig-c/parts/docs/AUTHORING.md §4, step 6
2. **Expect:** assemble --propose-plan exits 0 and writes assemble.plan into config.json for seated character
3. **Chose / turned down:** proposing plan with assemble --propose-plan on seated character layers
4. **Happened** (2026-10-25T09:16:33Z): exit 0; added assemble.plan and extend_below_crop to config.json

## Entry 2 (opened 2026-10-25T09:16:38Z)

1. **Read:** node_modules/@rig-c/parts/docs/AUTHORING.md §4, step 7
2. **Expect:** assemble produces work_03/rig with parts.json and measures recomposite uncovered error px
3. **Chose / turned down:** running assemble on seated figure to produce parts for propose
4. **Happened** (2026-10-25T09:17:14Z): exit 0; recomposite vs source uncovered error px: 1726 well below 3500 threshold

## Entry 3 (opened 2026-10-25T09:17:20Z)

1. **Read:** node_modules/@rig-c/parts/docs/AUTHORING.md §4, step 7
2. **Expect:** propose writes proposal into config.json and prints LINT lines naming what differs from check
3. **Chose / turned down:** proposing rig elements to see tool findings on the seated character
4. **Happened** (2026-10-25T09:17:35Z): exit 0; LINT hairback_r and hairback_l on mesh 'hair_back' squeeze it: swung together, every other bone held, edge 37-117 of triangle 167 closes to 0.064 times its rest length at idle frame 22

## Entry 4 (opened 2026-10-25T09:17:48Z)

1. **Read:** node_modules/@rig-c/parts/docs/AUTHORING.md §4, step 8
2. **Expect:** propose --from-config verifies the amplitude sign correction and reports 0 LINT lines
3. **Chose / turned down:** checking corrected config with propose --from-config before full build
4. **Happened** (2026-10-25T09:18:00Z): exit 0; 0 LINT line(s) over 8 mesh(es) and the hip after correcting hairback_l amplitude sign

## Entry 5 (opened 2026-10-25T09:18:05Z)

1. **Read:** node_modules/@rig-c/parts/docs/AUTHORING.md §4, step 9 and tasks/03-correct/TASK.md
2. **Expect:** rig-parts build exits 0, passes check, and idle renders without folding
3. **Chose / turned down:** running full build with --loop to verify corrected config against all bars
4. **Happened** (2026-10-25T09:18:45Z): exit 0; check: PASS; 11 of 11 bar(s) measured, 0 skipped and build completed successfully

## Entry 6 (opened 2026-10-25T09:18:50Z)

1. **Read:** grade.py and tasks/03-correct/TASK.md
2. **Expect:** grade.py passes all 6 lines for task 03 (built, checked, whole, does_not_fold, kept, still_moves)
3. **Chose / turned down:** running grade.py to officially grade task 03
4. **Happened** (2026-10-25T09:19:24Z): exit 0; 6 of 6 line(s); journal present, 0 entry(ies) whose line 4 begins WTF?:; log .grade/2026-10-25-gemini-3.8-flash-medium-03-correct/grade.log

## At the end (2026-10-25T09:19:28Z)

- **Where I guessed:** none; hairback_l positive amplitude [0.6, 1.4, 2.4] was directly given by the LINT squeeze diagnostic
- **What I could not find:** none; LINT diagnostic gave the exact remedy
