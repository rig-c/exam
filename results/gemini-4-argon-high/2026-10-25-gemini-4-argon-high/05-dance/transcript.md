started: 2026-10-25T09:52:50Z

## Step 1 (entry 1)

- argv: ["python3", "grade.py", "runs/2026-10-25-gemini-4-argon-high-05-dance"]
- start: 2026-10-25T09:56:48Z
- end: 2026-10-25T10:00:45Z
- exit: 0
- output: .journal/step-1.out, 2138 bytes, sha256 2b9dbab02c2886672cb2300bf1e9a923dc550f6f5fae8b49fc34146a38e612eb
- last lines:

    PASS  closes: "the last frame is 0.0 rig px from the first at its furthest vertex, against <= 0.5 (keys only, physics out)"
    PASS  both_hands: "`hand_l` travels 585.0 rig px and `hand_r` 593.8 at their furthest vertex, measured from the middle of `topwear`, each against >= 100.0"
    PASS  whole_body: "the vertex of `topwear` that travels least travels 47.6 rig px, measured from the middle of `foot_l` and `foot_r`, against >= 15.0"
    SKIP  arms_bend_at_the_joints: "not measured: every arm part (`upperarm_l`, `forearm_l`, `upperarm_r`, `forearm_r`) is rigid on one bone and turns only at a joint that declares its range (elbow [-45, 45], wrist [-45, 45]); a rigid part cannot bend along its own length, so the line has nothing on this rig to tell apart"
    PASS  on_her_feet: "the end of a leg (`shin_l`, `shin_r`) gets 5.83 rig px from where it meets `foot_l`, `foot_r`, against <= 6.0"
    PASS  keeps_time: "1.0 of the variation in how fast she moves repeats every two beats, against >= 0.5"
    SKIP  soft_in_the_dance: "not read on this fixture: the rig is given and has no physics (tasks/05-dance/TASK.md)"
    PASS  dance_does_not_fold: []
    journal: chain intact, 1 entries, 0 WTF
    note: no animation handed in has the shape of the guide's scripts
    clock: no started:/finished: lines in transcript.md
    11 of 11 line(s), 3 skipped (budget, arms_bend_at_the_joints, soft_in_the_dance); journal present, 0 entry(ies) whose line 4 begins WTF?:; log .grade/2026-10-25-gemini-4-argon-high-05-dance/grade.log

finished: 2026-10-25T10:01:14Z
