# Journal

## Entry 1 (opened 2026-10-25T09:39:52Z)

1. **Read:** tasks/03-correct/TASK.md, tasks/03-correct/inputs/seethrough.json, and AUTHORING.md §4 step 6
2. **Expect:** assemble --propose-plan writes assemble.plan and assemble.extend_below_crop into config.json and prints notes about any unplanned layers
3. **Chose / turned down:** run rig-parts assemble --propose-plan with --write-config runs/2026-10-25-gemini-4-argon-high-03-correct/config.json
4. **Happened** (2026-10-25T09:40:26Z): added assemble.plan and assemble.extend_below_crop; headwear: head run 5 rig px < 0.8 x full run 2146 -> full-run layer, drawn behind the face

## Entry 2 (opened 2026-10-25T09:40:37Z)

1. **Read:** Entry 1 output: 22-row assemble.plan and extend_below_crop; AUTHORING.md §4 step 7
2. **Expect:** assemble writes work/rig and reports recomposite vs source with uncovered_error_px <= 3500
3. **Chose / turned down:** run rig-parts assemble into runs/2026-10-25-gemini-4-argon-high-03-correct/work
4. **Happened** (2026-10-25T09:41:23Z): recomposite vs source: mean |d|=1.09, within 8: 97.9%, error px > 40: 6164, uncovered error px: 1726; drift: bottomwear refuses 21999 px of full:bottomwear

## Entry 3 (opened 2026-10-25T09:41:36Z)

1. **Read:** Entry 2 assemble output: 22 parts in work/rig; TASK.md stating what the tool proposes does not pass its own check as proposed
2. **Expect:** propose --parts writes bones, meshes, regions, motion, and proposed_rig_scale into config.json and emits LINT lines identifying what is wrong with the draft
3. **Chose / turned down:** run rig-parts propose --parts runs/2026-10-25-gemini-4-argon-high-03-correct/work/rig --write-config runs/2026-10-25-gemini-4-argon-high-03-correct/config.json
4. **Happened** (2026-10-25T09:42:07Z): LINT hairback_r and hairback_l on mesh 'hair_back' squeeze it: swung together, every other bone held, edge 37-117 of triangle 167 closes to 0.064 times its rest length at idle frame 22 (max(ratio, 1/ratio) 15.572; <= 1.926544 is required, check's TEXTURE_STRETCH bar)

## Entry 4 (opened 2026-10-25T09:42:50Z)

1. **Read:** Entry 3 LINT line on hairback_r and hairback_l squeezing mesh 'hair_back' (ratio 15.572) and work/render/landmarks.png showing both chains on the same back-hair mass 39.0 px apart
2. **Expect:** propose --from-config prints 0 LINT line(s) after changing hairback_l amps from [-0.6, -1.4, -2.4] to [0.6, 1.4, 2.4] in config.json
3. **Chose / turned down:** run rig-parts propose --from-config runs/2026-10-25-gemini-4-argon-high-03-correct/config.json
4. **Happened** (2026-10-25T09:43:16Z): 0 LINT line(s) over 8 mesh(es) and the hip; coverage: 45 bone(s) — 37 checked and clean, 0 checked with a LINT line, 8 not checked

## Entry 5 (opened 2026-10-25T09:43:27Z)

1. **Read:** Entry 4 output: 0 LINT line(s) over 8 mesh(es) and the hip; TASK.md pass lines for task 03
2. **Expect:** grade.py passes all 6 lines (built, checked, whole <= 3500, does_not_fold [], kept >= 8 meshes, still_moves 45.9 rig px >= 23)
3. **Chose / turned down:** run python3 grade.py runs/2026-10-25-gemini-4-argon-high-03-correct
4. **Happened** (2026-10-25T09:44:36Z): 6 of 6 line(s) passed; PASS still_moves: "the back hair travels 45.881 rig px against the head over the idle, against >= 23"

## At the end (2026-10-25T09:45:16Z)

- **Where I guessed:** nothing — propose's LINT line and work/render/landmarks.png directly named hairback_r [0.6, 1.4, 2.4] and hairback_l [-0.6, -1.4, -2.4] on mesh 'hair_back' squeezing triangle 167 edge 37-117 to 0.064x (ratio 15.572) and stated the fix (give both the same sign, then 1.046)
- **What I could not find:** propose drafts opposed amplitudes for hairback_r and hairback_l even when both chains sit 39.0 px apart on the same back-hair mass and then immediately flags its own draft in the squeeze LINT check; drafting same-sign amplitudes when two back-hair chains share one mass within the squeeze threshold would avoid the manual edit
