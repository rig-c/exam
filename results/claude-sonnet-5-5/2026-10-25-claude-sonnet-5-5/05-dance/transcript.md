started: 2026-10-25T11:48:49Z

## Step 1 (entry 1)

- argv: ["sh", "-c", "node_modules/.bin/rig-parts build --config runs/2026-10-25-claude-sonnet-5-5-05-dance/config.json --source fixtures/mannequin/inputs/painting.png --full fixtures/mannequin/inputs/layers/full --head fixtures/mannequin/inputs/layers/head --out runs/2026-10-25-claude-sonnet-5-5-05-dance/out > runs/2026-10-25-claude-sonnet-5-5-05-dance/build.log 2>&1; echo exit=$?; command grep -E 'FAIL|check:|build:|ANIMATIONS|FEET_STAY|SEAM|animations beside' runs/2026-10-25-claude-sonnet-5-5-05-dance/build.log | cut -c1-500"]
- start: 2026-10-25T11:49:44Z
- end: 2026-10-25T11:50:43Z
- exit: 0
- output: .journal/step-1.out, 2175 bytes, sha256 7e2d0189903c8de6f42c92bfc2f6523ee21931ce9519bcff1d1ffb5a0b1c1023
- last lines:

    exit=0
    rig-parts build: runs/2026-10-25-claude-sonnet-5-5-05-dance/config.json -> runs/2026-10-25-claude-sonnet-5-5-05-dance/out, seam rule near-white, projection rule core, page edges free, pack shape polygon
    [rig]   animations beside the idle, from /Users/firejune/Workspace/Firejune/exam-sittings/2026-10-25-claude-sonnet-5-5/exam-claude-sonnet-5-5/runs/2026-10-25-claude-sonnet-5-5-05-dance/animations.json as written: dance
    [check] rig-parts check: runs/2026-10-25-claude-sonnet-5-5-05-dance/out/rig -> runs/2026-10-25-claude-sonnet-5-5-05-dance/out/check
    [check]   beside the idle: 1 animation(s), dance — built and gated by rigc with the rig; ANIMATIONS_DO_NOT_FOLD reads each for folds and FEET_STAY_LEVEL for how far the feet turn, every other bar here reads the idle
    [check]   ANIMATIONS_DO_NOT_FOLD: PASS — 2 animation(s) read by rigc render --folds at 12 fps (idle, dance): 0 folding mesh(es), 0 not declared in may_fold (<= 0)
    [check]   FEET_STAY_LEVEL: PASS — 2 animation(s) read by rigc render --folds --geometry at 12 fps (idle, dance): each foot's drawing within ±10 degrees of its setup pose while a bone above it is turned, HQ's line (rig-c/parts#347 ruling 4), not a figure measured here
    [check]   SEAM_OVER_RANGE: PASS — 9 joint(s) bent to their declared range's ends and middle; at each, the pose against the same pose with the joint's own art drawn under the limb, on the rest-pose seam's bar (mean |d| <= 1.0, <= 50 rig px over 40) at frame scale 1.023141
    [check]   SEAM_OVER_MOTION: WARN — 9 declared pair(s) in 2 animation(s) (idle, dance), read by rigc render --seam at 12 fps on the build as played: 2 warning(s), never a bar; a frame opens when its gap or its ghost holds more cells than its box is long (rig-c's cell, its box's longer side) — thicker than one cell; a crack one cell deep is the half-opacity cut moving by less than a cell, and is not reported
    [check] check: PASS; 10 of 14 bar(s) measured, 4 skipped (BLINK_NO_HOLE, TIP_OVER_ROOT, TEXTURE_STRETCH, STRESS_OFF_CHAIN); 2 warning(s) (SEAM_OVER_MOTION, not a bar)
    build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from

## Step 2 (entry 2)

- argv: ["python3", "grade.py", "runs/2026-10-25-claude-sonnet-5-5-05-dance"]
- start: 2026-10-25T11:50:49Z
- end: 2026-10-25T11:53:22Z
- exit: 0
- output: .journal/step-2.out, 2136 bytes, sha256 8c2254fc422bf2ec0c614e8a1b55af64ccebeaf88cb2e8dcd87b1d8746f6390b
- last lines:

    PASS  closes: "the last frame is 0.0 rig px from the first at its furthest vertex, against <= 0.5 (keys only, physics out)"
    PASS  both_hands: "`hand_l` travels 542.7 rig px and `hand_r` 550.2 at their furthest vertex, measured from the middle of `topwear`, each against >= 100.0"
    PASS  whole_body: "the vertex of `topwear` that travels least travels 25.4 rig px, measured from the middle of `foot_l` and `foot_r`, against >= 15.0"
    SKIP  arms_bend_at_the_joints: "not measured: every arm part (`upperarm_l`, `forearm_l`, `upperarm_r`, `forearm_r`) is rigid on one bone and turns only at a joint that declares its range (elbow [-45, 45], wrist [-45, 45]); a rigid part cannot bend along its own length, so the line has nothing on this rig to tell apart"
    FAIL  on_her_feet: "the end of a leg (`shin_l`, `shin_r`) gets 8.32 rig px from where it meets `foot_l`, `foot_r`, against <= 6.0"
    PASS  keeps_time: "1.0 of the variation in how fast she moves repeats every two beats, against >= 0.5"
    SKIP  soft_in_the_dance: "not read on this fixture: the rig is given and has no physics (tasks/05-dance/TASK.md)"
    PASS  dance_does_not_fold: []
    journal: chain intact, 2 entries, 0 WTF
    note: no animation handed in has the shape of the guide's scripts
    clock: no started:/finished: lines in transcript.md
    10 of 11 line(s), 3 skipped (budget, arms_bend_at_the_joints, soft_in_the_dance); journal present, 0 entry(ies) whose line 4 begins WTF?:; log .grade/2026-10-25-claude-sonnet-5-5-05-dance/grade.log

## Step 3 (entry 3)

- argv: ["python3", "grade.py", "runs/2026-10-25-claude-sonnet-5-5-05-dance"]
- start: 2026-10-25T11:53:35Z
- end: 2026-10-25T11:56:52Z
- exit: 0
- output: .journal/step-3.out, 2135 bytes, sha256 c688dc7cf0e08720259e1d58684ba7b02bee7500aeb41bd946b65ba3cb68d155
- last lines:

    PASS  closes: "the last frame is 0.0 rig px from the first at its furthest vertex, against <= 0.5 (keys only, physics out)"
    PASS  both_hands: "`hand_l` travels 542.7 rig px and `hand_r` 550.2 at their furthest vertex, measured from the middle of `topwear`, each against >= 100.0"
    PASS  whole_body: "the vertex of `topwear` that travels least travels 26.5 rig px, measured from the middle of `foot_l` and `foot_r`, against >= 15.0"
    SKIP  arms_bend_at_the_joints: "not measured: every arm part (`upperarm_l`, `forearm_l`, `upperarm_r`, `forearm_r`) is rigid on one bone and turns only at a joint that declares its range (elbow [-45, 45], wrist [-45, 45]); a rigid part cannot bend along its own length, so the line has nothing on this rig to tell apart"
    PASS  on_her_feet: "the end of a leg (`shin_l`, `shin_r`) gets 5.1 rig px from where it meets `foot_l`, `foot_r`, against <= 6.0"
    PASS  keeps_time: "1.0 of the variation in how fast she moves repeats every two beats, against >= 0.5"
    SKIP  soft_in_the_dance: "not read on this fixture: the rig is given and has no physics (tasks/05-dance/TASK.md)"
    PASS  dance_does_not_fold: []
    journal: chain intact, 3 entries, 1 WTF
    note: no animation handed in has the shape of the guide's scripts
    clock: no started:/finished: lines in transcript.md
    11 of 11 line(s), 3 skipped (budget, arms_bend_at_the_joints, soft_in_the_dance); journal present, 1 entry(ies) whose line 4 begins WTF?:; log .grade/2026-10-25-claude-sonnet-5-5-05-dance/grade.log

finished: 2026-10-25T11:56:59Z
