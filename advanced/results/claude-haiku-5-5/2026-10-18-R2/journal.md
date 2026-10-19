# Journal — claude-haiku-5-5, Advanced R2 (run), 2026-10-18

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry 1

1. **Read:** PROBLEM.md "What to do" 1 (put it on: retarget, write map.json); `node_modules/@rig-c/pose/README.md` "The map: `rig-pose-map/1`" (chains, joints, aim, translate.scale); `rig-pose retarget --help`.
2. **Expect:** `run/map.json` with chains leg_r/leg_l (bones leg_r0,leg_r1 / leg_l0,leg_l1; joints r_hip,r_knee,r_ankle / l_hip,l_knee,l_ankle), arm_r/arm_l (sleeve_*; shoulder/elbow/wrist), trunk (chest; mid_hip→neck, aim neck), head, and translate hip←mid_hip scaled by mid_hip→neck. Then `retarget` exits 0 with a gate line; output `run/after/motion.json`.
3. **Chose / turned down:** Legs `"free"` (README warns legs on "rest" + clamp straighten knees; sequence has a real knee bend in a run). Arms `"free"` (front-facing material, README). Feet are not mapped as chains (a one-joint chain makes no jitter pair); feet are taken from the rig by the grader via `--feet foot_l,foot_r`. Turned down: copying a map from elsewhere (no other source allowed).
4. **Happened:** `rig-pose retarget` exit 0, gate line green, `run/after/motion.json` written (animation `run`). WTF?: the command I ran did not include `--leg-scale` although I first wrote it into the transcript echo; corrected in transcript. Otherwise as expected.

## Entry 2

1. **Read:** `rigc render --help` (--geometry, --folds, --pass-through, --fps); PROBLEM.md table rows Folds / Pass-through / Loop / Airborne.
2. **Expect:** `run/after/render/` with `run` frames at 30 fps (animation run, 200 frames), `geometry.json`, `folds.json`, `pass-through.json`; zero folds; pass-through zero frames.
3. **Chose / turned down:** Render at the sequence's 30 fps so geometry frames align one to one with the pose (the grader needs matching fps). Turned down: default 12 fps (grader would refuse alignment).
4. **Happened:** build green (52 assertions, 0 failed), render wrote 200 frames at 30 fps, 0 of 6 meshes fold, pass-through 0 of 200 frames for both thighs. Matched expectation. First grader run (R2): 6 PASS, 8 FAIL, 0 SKIP. Fails: support-foot 0.0383 (bar 0.01), two-feet (rig never lifts the foot: 60 of 60 lifted frames within 0.01 of support, median lift ratio -0.022), loop (arm sleeve_l1 34.7° at cycle frame 1), airborne (lowest airborne foot 0.0077 leg lengths, bar >0.01), hip-vertical 1.349, hip-horizontal 1.711, rebound 1.961, hip-tilt 0.000 (sign disagrees).

## Entry 3

1. **Read:** grader output `run/after/grade1.out` (hip-tilt row: "rig tilt range 0.000 deg"); `node_modules/@rig-c/pose/README.md` map section, the example `{ "name": "pelvis", "bones": ["hip"], "joints": ["r_hip", "l_hip"], "aim": ["leg_r0>leg_l0"] }`.
2. **Expect:** a one-bone pelvis chain on `hip` aimed by its hip line gives the thigh-root line a tilt range, so the hip-tilt row moves off 0; gate stays green.
3. **Chose / turned down:** Add the pelvis chain (the README gives this exact form; the grader reads the thigh-root line, which only tilts if the pelvis is keyed). Turned down, for now: changing the translate scale for hip-vertical/horizontal (a second variable; do it after tilt is read).
4. (pending)

## Entry 4

1. **Read:** `rig-pose retarget --help` `--leg-scale` ("each leg segment ... scaled along its own x axis ... default off; 0.8,1.05 is the card's range"); grader NOTE lines: rig leg length 485.09 units, sequence leg length 399.28 (ratio 0.823).
2. **Expect:** the rig's legs are ~18% longer than the sequence's in picture terms, so `--leg-scale 0.8,1.05` should shorten the legs toward the sequence and move the support-foot, two-feet lift, hip-vertical and hip-horizontal rows. Gate stays green; folds may change.
3. **Chose / turned down:** `--leg-scale 0.8,1.05` (the README's card range, matching the leg ratio). Turned down: a wider range (outside the card's range the README gives no measured basis).
4. **Happened:** retarget exit 0, LEG-SCALE listed 4 times, build green (52 assertions), render 200 frames. Grader: 8 PASS, 6 FAIL. support-foot now PASS (0.0000), airborne PASS (0.0513), hip-tilt PASS. Still failing: two-feet (median rig/sequence lift 0.145, bar 0.85–1.15), folds (16 frames in bottomwear, was 0 before the pelvis chain), loop (sleeve_l1 34.7°), hip-vertical 1.460, hip-horizontal 1.712, rebound 1.929. Matched the expectation for support-foot and the leg-length-driven rows; did NOT match for hip-vertical/horizontal (expected to move toward 1). WTF?: the leg scale fixed the feet but widened the hip horizontal ratio slightly and did not bring the hip vertical in; I did not identify the mechanism.

## At the end

- **Where I guessed:** the model name `claude-haiku-5-5` (from the environment block, not from the sitting prompt's `<MODEL>`); the choice `--plant-feet --stance 0.07 --bends clamp --flip 90 --short 0.35` (inherited from the retarget help's "measured setting" hints, not from a source that ties them to this clip); `--leg-scale 0.8,1.05` as the right range for this clip (chosen from the leg ratio 0.823).
- **What I could not find:** the R1 table as written out in PROBLEM.md (PROBLEM says it is "written out again here", but only the R2 rows are present; I graded the R1 rows as the grader defines them); the R2 airborne spans are in grade.py (`R2_AIR_REFERENCE`) only, not in the problem text, which I took as given; why the hip vertical/horizontal ratios stay above 1.15 (the mechanism behind the translate scale and plant-feet hip shift was not found); why the arm `sleeve_l1` differs 34.7° between cycle 1 and cycle 10 (no source identified it); the stick-figure video was not available to compare evidence frames (the problem says the proctor has it).
