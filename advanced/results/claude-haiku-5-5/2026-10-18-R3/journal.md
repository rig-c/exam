# Journal — claude-haiku-5-5, dance (Advanced R3), 2026-10-19

## Entry 1
1. **Read:** PROBLEM.md "Tools" and "What to do" §1; `rig-pose retarget --help` (map chains, translate, aim, --bends).
2. **Expect:** `rig-pose retarget` runs on inputs/rig/rig.json with a first map (arms, legs, trunk, head, hip translate) and writes motion.json, camera.json and the gated build.
3. **Chose / turned down:** first map from the rig's leg_r0/leg_r1, sleeve_*, chest, head bones and the hip translate; face block turned down until the body gates.
4. **Happened:** WTF?: rig.json alone was refused (gate red with no motion spec; "applies animation turn ... declares none"). Pointing `--rig` at the directory inputs/rig worked. Then 566 POSE_BEND_ONE_WAY on leg_l l_knee (inner angle about -0.1 to -6.4 deg, rest 1.4 deg). I had not expected the bend guard to fire this often. Second run with `--bends clamp` (listed per frame) wrote motion.json and camera.json and the gate went green (52 assertions, 24 measured).

## Entry 2
1. **Read:** PROBLEM.md "Hand in" (camera.json); grade.py header (--build = stdout of the last `rigc build`; --report from retarget).
2. **Expect:** `rigc build --profile spine` exits 0, writes skeleton.json/atlas/model.json to run/after/build; stdout kept.
3. **Chose / turned down:** build from inputs/rig/rig.json + motion.json with the default spine profile; --pack not used.
4. **Happened:** exit 0, skeleton.atlas and skeleton.model.json written, stdout saved as run/after/build.stdout.txt. Matched.

## Entry 3
1. **Read:** PROBLEM.md "Hip tilt" row (thigh-root line tilt ≥ 85% of the pelvis line, signs agree); map.py header (a chain bone's aim `bone name` = direction from its origin to that descendant).
2. **Expect:** the baseline grade (run/evidence/grade_before.txt) fails hip-tilt (rig range 0 deg). A one-bone `pelvis` chain on `hip` (joints l_hip→r_hip, aim leg_r0) keys the hip rotation and moves the tilt.
3. **Chose / turned down:** `pelvis` chain as run/map_v2.json. Turned down editing the rig spec (rotation can be keyed through the map).
4. **Happened:** matched. Hip tilt 0.000 → 1.000 (54.770 deg vs 54.769, sign agrees). Support-foot went 0.0240 → 0.0015 and hip-vertical PASS (1.052). Left failing: two-feet (median lift ratio 0.015) and slide (0.00872 on foot_r, frame 83→84). Note: this retarget overwrote run/after/report.json; from here each variant writes its own report via run/pipe.sh.

## Entry 4
1. **Read:** grade.py two-feet row (lift ratio over lifted frames); retarget help for `--stance` ("a free ankle within this many leg lengths of the supporting one … is planted too").
2. **Expect:** the lift ratio is low (0.015) because `--stance 0.07` plants the free foot on lifted frames. Dropping `--stance` should lift it and keep support green.
3. **Chose / turned down:** run/v3 without --stance. Turned down raising --stance tolerance as the first move.
4. **Happened:** WTF?: yes. Without --stance, support-foot failed (0.0409) and the lifted-foot rows failed too, so the stance planting is what holds the support foot. Sweep of `--stance`: 0.02 failed like 0.0 (0.0412); 0.035 gave 12 pass / 1 fail (slide 0.00872). I had expected lift and support to separate; they did not.

## Entry 5
1. **Read:** grade.py slide row (support-foot move per frame inside ground spans ≤ 0.005); retarget help for `--reduce` (thins rotate keys within deg) and `--leg-scale`.
2. **Expect:** the 0.0087 step on foot_r at frames 83→84 comes from `--reduce` thinning the planted leg's keys. Removing `--reduce` should lower it without breaking the others.
3. **Chose / turned down:** run/nr = run/map_v2.json, `--plant-feet --stance 0.035 --flip 90 --short 0.35 --leg-scale 0.8,1.05`, no `--reduce`. Turned down retuning `--leg-scale` range first (larger change, less direct).
4. **Happened:** matched. 13 pass / 0 fail. Slide 0.00003, support-foot 0.0000, two-feet 0.0000 with median lift ratio 0.963, floor 0.0000. Cost: the key count is no longer thinned (motion.json larger).

## Entry 6
1. **Read:** PROBLEM.md "Hand in" (after/ holds motion · build · render · camera.json); grade.py NOTE lines.
2. **Expect:** promoting run/nr's artifacts into run/after/ and re-grading gives the same 13/13 lines.
3. **Chose / turned down:** promote run/nr to run/after (copy, not re-run), then grade from run/after. Turned down a fresh retarget (the same inputs give the same output; a re-run is not needed).
4. **Happened:** matched. run/evidence/grade_final_promoted.txt: 13 pass, 0 fail; camera NOTE "313 entries … max difference 0.000000 s".

## At the end
- **Where I guessed:** (a) the `pelvis` chain aim (leg_r0) — chosen by reading aim rules, confirmed only by the hip-tilt row passing; (b) `--bends clamp` as the bend-guard answer, with 566 one-way knee frames inside -6.4 deg, not checked against the video; (c) `--stance 0.035` and dropping `--reduce` picked by sweep, not by a closed-form reason; (d) leg-scale 0.8,1.05 kept from the card default without a sweep.
- **What I could not find:** no document said how a non-looping sequence should map the pelvis tilt (I found it by reading the map source); the R3 floor row takes its spans from the report only when `--cycle` is absent (found in grade.py); I could not compare against the original video (only the proctor has it), so the evidence frames are side by side with stick.mp4 only.
