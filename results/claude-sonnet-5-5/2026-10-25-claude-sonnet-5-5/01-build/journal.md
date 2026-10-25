# Journal

## Entry 1 (opened 2026-10-25T11:29:17Z)

1. **Read:** README.md 'The loop, for an agent'; AUTHORING §4 steps 3,6
2. **Expect:** layers prints a table of the full run's layers, exit 0, maybe WARN PLAN_LAYER lines
3. **Chose / turned down:** run rig-parts layers on layers/full (read-only); not editing config yet. config.json (key, seethrough from inputs/seethrough.json, rig_scale 0.5) written by hand, used from the next step
4. **Happened** (2026-10-25T11:29:29Z): exit 0; "29 layer(s): 29 with opaque pixels, 0 with none" and "0 WARN line(s)" as expected.

## Entry 2 (opened 2026-10-25T11:29:30Z)

1. **Read:** README 'The loop' step assemble --propose-plan; AUTHORING §4 step 6
2. **Expect:** prints plan JSON plus notes and, with --write-config, saves assemble.plan and extend_below_crop into config.json; exit 0
3. **Chose / turned down:** assemble --propose-plan --write-config config.json using given head layers; head_box taken from inputs/seethrough.json, so no propose --head-box step (turned down: would just reproduce it)
4. **Happened** (2026-10-25T11:30:04Z): exit 0; config: added assemble.plan and added assemble.extend_below_crop; 22 plan rows, no notes naming a body no part covers.

## Entry 3 (opened 2026-10-25T11:30:04Z)

1. **Read:** AUTHORING §4 step 7; README loop 'assemble ... --out work'
2. **Expect:** writes work/rig parts and prints uncovered hole lines; exit 0; maybe a few holes
3. **Chose / turned down:** assemble into runs/.../work (not handed in). Not adding the nose row (only needed for head pitch read)
4. **Happened** (2026-10-25T11:30:47Z): exit 0; "recomposite vs source: mean |d|=1.09, within 8: 97.6%, error px > 40: 7465, uncovered error px: 1812" — under the 3,700 bar; largest hole 94 px, no patches needed.

## Entry 4 (opened 2026-10-25T11:30:47Z)

1. **Read:** AUTHORING §4 step 7: propose --parts ... --write-config
2. **Expect:** writes bones, meshes, regions, motion, proposed_rig_scale into config.json (no limbs without --keypoints, no turn without --full/--head); LINT lines possible; exit 0 or 1
3. **Chose / turned down:** propose --parts with --full/--head (turn needs both) and --write-config; not passing --keypoints (no keypoints file given) and not --cloth (task 01 only needs build pass)
4. **Happened** (2026-10-25T11:31:01Z): exit 0 but one LINT: "LINT hairback_r and hairback_l on mesh 'hair_back' squeeze it" — amplitudes opposed; message says give both the same sign. Expected possible LINT, so no WTF.

## Entry 5 (opened 2026-10-25T11:31:11Z)

1. **Read:** propose output LINT line: 'give both the same sign (then 1.051), or drop one chain'; AUTHORING §4 step 8 (--from-config until no LINT)
2. **Expect:** after flipping hairback_l amps to positive in config.json motion, propose --from-config prints no LINT line and exits 0
3. **Chose / turned down:** flip sign of hairback_l amps (edited config.json by hand); turned down dropping a chain (loses hair sway)
4. **Happened** (2026-10-25T11:31:18Z): WTF?: I added --full/--head to --from-config, which the tool refuses ("FAIL  USAGE: --full and --head draft the turn control while proposing; --from-config proposes nothing"); my own misuse (and my grep pipe masked the exit code as 0). Nothing was linted.

## Entry 6 (opened 2026-10-25T11:31:18Z)

1. **Read:** README loop: 'propose --parts work/rig --source painting.png --out work --from-config config.json' (no --full/--head)
2. **Expect:** no LINT line after the sign flip, exit 0
3. **Chose / turned down:** rerun from-config without --full/--head, no grep pipe so the exit code is the tool's
4. **Happened** (2026-10-25T11:31:30Z): 0 LINT line(s) over 8 mesh(es) and the hip; exit 0 as expected.

## Entry 7 (opened 2026-10-25T11:31:30Z)

1. **Read:** TASK.md build command; README loop last step; AUTHORING §4 step 9
2. **Expect:** build exits 0 with 'build: PASS', check PASS, uncovered_error_px 1812; takes about a minute
3. **Chose / turned down:** build with the task's exact command shape, plus --loop (not needed; turned down to save time)
4. **Happened** (2026-10-25T11:32:14Z): build: PASS — the packed atlas is the artifact; check: PASS; 11 of 12 bar(s) measured, 1 skipped (FEET_STAY_LEVEL); uncovered_error_px 1812. As expected.

## Entry 8 (opened 2026-10-25T11:32:14Z)

1. **Read:** README 'You may run python3 grade.py runs/<run>'; TASK.md pass lines
2. **Expect:** grader prints Built/Checked/Whole/Does-not-fold all PASS plus journal chain intact; writes result.json
3. **Chose / turned down:** run grade.py once on the run dir now; the folds line needs rigc render --folds which the grader runs itself
4. **Happened** (2026-10-25T11:33:06Z): exit 0; "4 of 4 line(s)"; "journal: chain intact, 8 entries, 1 WTF"; the clock line only lacks finished: which comes next.

## At the end (2026-10-25T11:33:13Z)

- **Where I guessed:** rig_scale 0.5 (copied from the examples' doc, not computed from the figure height); the hairback_l sign flip was taken from the LINT message
- **What I could not find:** Nothing blocking; no doc said that --from-config cannot be combined with --full/--head.
