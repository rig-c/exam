started: 2026-10-18T22:52:24Z

```
$ npm install
1 package is looking for funding
found 0 vulnerabilities
[exit 0]
```

```
$ npx rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --out run/before/motion.json --build run/before/build --report run/before/report.json --camera run/before/camera.json
  IDLE-DROPPED bone "skirt_l0_ctl" rotate: 9 key(s) over the idle's 3.333s; "dance" does not key it — not carried (no --carry-idle)
  IDLE-DROPPED bone "skirt_l1_ctl" rotate: 9 key(s) over the idle's 3.333s; "dance" does not key it — not carried (no --carry-idle)
  IDLE-DROPPED bone "skirt_l2_ctl" rotate: 9 key(s) over the idle's 3.333s; "dance" does not key it — not carried (no --carry-idle)
  IDLE-DROPPED group "eyes" (eye_r, eye_l) scaley: 6 key(s) over the idle's 3.333s; "dance" does not key it — not carried (no --carry-idle)
  IDLE-DROPPED group "brows" (brow_r, brow_l) translatey: 6 key(s) over the idle's 3.333s; "dance" does not key it — not carried (no --carry-idle)
  IDLE-DROPPED bone "skirt_rm0_ctl" rotate: 9 key(s) over the idle's 3.333s; "dance" does not key it — not carried (no --carry-idle)
  IDLE-DROPPED bone "skirt_rm1_ctl" rotate: 9 key(s) over the idle's 3.333s; "dance" does not key it — not carried (no --carry-idle)
  IDLE-DROPPED bone "skirt_rm2_ctl" rotate: 9 key(s) over the idle's 3.333s; "dance" does not key it — not carried (no --carry-idle)
  IDLE-DROPPED bone "skirt_lm0_ctl" rotate: 9 key(s) over the idle's 3.333s; "dance" does not key it — not carried (no --carry-idle)
  IDLE-DROPPED bone "skirt_lm1_ctl" rotate: 9 key(s) over the idle's 3.333s; "dance" does not key it — not carried (no --carry-idle)
  IDLE-DROPPED bone "skirt_lm2_ctl" rotate: 9 key(s) over the idle's 3.333s; "dance" does not key it — not carried (no --carry-idle)
  IDLE-KEPT-OUT bone "chest_ctl" scalex: moves mapped bone(s) "chest", "head", "sleeve_r0", "sleeve_r1", "sleeve_l0", "sleeve_l1" below it; the retarget's keys assume it at setup, so the idle's track is not carried
  IDLE-KEPT-OUT bone "head_ctl" rotate: moves mapped bone(s) "head" below it; the retarget's keys assume it at setup, so the idle's track is not carried
  IDLE-KEPT-OUT bone "neck" rotate: moves mapped bone(s) "head" below it; the retarget's keys assume it at setup, so the idle's track is not carried
  IDLE-KEPT-OUT bone "sleeve_r0" rotate: "dance"'s own bone "sleeve_r0" rotate keys it, so the idle's track is not carried
  IDLE-KEPT-OUT bone "sleeve_r1" rotate: "dance"'s own bone "sleeve_r1" rotate keys it, so the idle's track is not carried
  IDLE-KEPT-OUT bone "sleeve_l0" rotate: "dance"'s own bone "sleeve_l0" rotate keys it, so the idle's track is not carried
  IDLE-KEPT-OUT bone "sleeve_l1" rotate: "dance"'s own bone "sleeve_l1" rotate keys it, so the idle's track is not carried
  GATE   rigc build --profile spine: green — 52 assertions: 24 measured (24 passed, 0 failed), 14 skipped, 14 not in profile "spine"
  LAND   bone "hip" aim — worst |reached − asked| 0.000509° at frame 130 (t=5.417s); the tolerance is 0.01°
  LAND   bone "chest" aim — worst |reached − asked| 0.000891° at frame 80 (t=3.333s); the tolerance is 0.01°
  LAND   bone "head" aim — worst |reached − asked| 0.00137° at frame 260 (t=10.833s); the tolerance is 0.01°
  LAND   bone "sleeve_r0" aim — worst |reached − asked| 0.00138° at frame 260 (t=10.833s); the tolerance is 0.01°
  LAND   bone "sleeve_r1" aim — worst |reached − asked| 0.00186° at frame 260 (t=10.833s); the tolerance is 0.01°
  LAND   bone "sleeve_l0" aim — worst |reached − asked| 0.00134° at frame 101 (t=4.208s); the tolerance is 0.01°
  LAND   bone "sleeve_l1" aim — worst |reached − asked| 0.00144° at frame 247 (t=10.292s); the tolerance is 0.01°
  LAND   bone "leg_r0" aim — worst |reached − asked| 0.000930° at frame 259 (t=10.792s); the tolerance is 0.01°
  LAND   bone "leg_r1" aim — worst |reached − asked| 0.00120° at frame 265 (t=11.042s); the tolerance is 0.01°
  LAND   bone "leg_l0" aim — worst |reached − asked| 0.000970° at frame 133 (t=5.542s); the tolerance is 0.01°
  LAND   bone "leg_l1" aim — worst |reached − asked| 0.00135° at frame 173 (t=7.208s); the tolerance is 0.01°
  LAND   bone "yaw_dial" aim — worst |reached − asked| 0.0000202° at frame 193 (t=8.042s); the tolerance is 0.01°
  LAND   bone "pitch_dial" aim — worst |reached − asked| 0.0000231° at frame 119 (t=4.958s); the tolerance is 0.01°
  LAND   bone "hip" origin — worst |reached − asked| 0.000662 units at frame 214 (t=8.917s); the tolerance is 0.01 units
  POSTURE hip tilt range (chain "pelvis", r_hip → l_hip, Spine degrees): reference 54.8° (−24.4° … +30.4°), rig 54.8° (−24.4° … +30.4°) — rig/reference 1.000; tilt measured (B' v2.2 skirt waistband (rig-c/pose#86)) on 313 frame(s): 168 read, 18 interpolated, 127 scaled (scaled: 178–267, 276–312, gain 2.73×, r=0.938), 0 held (held: none)
  POSTURE sway, x-range of mid_hip − mid_shoulder: reference 114.9 units = picture px × scale (0.960 shoulder widths), rig 110.1 units (0.915 shoulder widths; mid_hip = "hip", mid_shoulder = "sleeve_r0+sleeve_l0") — rig/reference 0.959 in units, 0.953 in shoulder widths
  FEET   the posed build, outside jumps: the lowest ankle's vertical range 73.67 units = 0.1420 leg lengths (rig leg r 512.9, l 524.5 units) over 303 frames
  FEET   the supporting ankle over each support span: worst vertical range 65.44 units = 0.1276 leg lengths (r 183–266), worst horizontal drift 53.72 units = 0.1047 leg lengths (r 183–266)
  FOLD   rigc render --folds at 24 fps: no mesh folds
  wrote run/before/camera.json — camera track (313 frames)
  wrote run/before/motion.json — animations: idle, pose_arms_up, pose_hands_behind_head, pose_hand_on_hip, pose_arms_crossed, pose_legs_apart, pose_hip_tilt_pos, pose_hip_tilt_neg, sweep_elbow_r_pos, sweep_elbow_r_neg, sweep_knee_r_pos, sweep_knee_r_neg, sweep_shoulder_r_out, sweep_shoulder_r_in, sweep_hip_tilt_pos, sweep_hip_tilt_neg, sweep_thigh_r_out, sweep_thigh_r_in, sway, set_K1, range_K1, set_K2, range_K2, set_K3, range_K3, set_K4, range_K4, set_K0, range_K0, turn, tilt, dance
[exit 0]
```

```
$ npx rigc build --rig inputs/rig --motion run/before/motion.json --out run/before/build > run/before/build.stdout 2>&1; echo exit $?; tail -5 run/before/build.stdout
exit 1
rigc build inputs/rig
  ..    rig    inputs/rig
  ..    motion run/before/motion.json
rigc compile error: cannot read inputs/rig: EISDIR: illegal operation on a directory, read (see rigc guide CE_COMPILE_JSON_READ_FAILED)
[exit 0]
```

```
$ npx rigc build --rig inputs/rig/rig.json --motion run/before/motion.json --out run/before/build > run/before/build.stdout 2>&1; echo exit $?; tail -4 run/before/build.stdout
exit 0
rigc: wrote run/before/build/skeleton.json
rigc: wrote run/before/build/skeleton.atlas
rigc: wrote run/before/build/skeleton.model.json
rigc: look at it: rigc render --candidate run/before/build
[exit 0]
```

```
$ npx rigc render --candidate run/before/build --animation dance --fps 24 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l,bottomwear:shin_r,bottomwear:shin_l --out run/before/render
rigc render
  ..    skeleton run/before/build/skeleton.json
  ..    atlas    run/before/build/skeleton.atlas
  ..    poser    rigc core — run/before/build/skeleton.model.json
  ..    201x256px at 24 fps, 1 set(s) -> run/before/render
  ..    dance            313 frame(s), 13.000s + contact.png + geometry.json + folds.json (0 of 6 mesh(es) fold) + pass-through.json (0 of 4 pair(s) pass through) -> run/before/render/dance@24fps
  ..    pass     "dance": cloth "bottomwear" over leg "thigh_r" passes through on 0 of 313 frame(s) read at 24 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0489) on its left side
  ..    pass     "dance": cloth "bottomwear" over leg "thigh_l" passes through on 0 of 313 frame(s) read at 24 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0489) on its left side
  ..    pass     "dance": cloth "bottomwear" over leg "shin_r" passes through on 0 of 313 frame(s) read at 24 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0489) on its left side
  ..    pass     "dance": cloth "bottomwear" over leg "shin_l" passes through on 0 of 313 frame(s) read at 24 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0489) on its left side
rigc: wrote run/before/render/frames.json
[exit 0]
```

```
$ <session scratchpad>/g.sh run/before
grade R3
NOTE  camera submission: present, rig-pose-camera/1, 313 entries, t = report frameTimes (max difference 0.000000 s)
NOTE  airborne spans: report feet.jumps, 3 span(s)
NOTE  rig leg length 518.8746 units (setup pose, leg_l0->foot_l, leg_r0->foot_r); hip width 92.2020
NOTE  sequence leg length 722.45 (95th percentile hip->ankle, mean of sides, the sequence's own units); the sequence's joints are camera-normalised, not divided by camera.s again
PASS  gate            Gate: build green (52 assertions: 24 measured, 0 failed); 14/14 landings within tolerance (worst at 0.19 of its tolerance)
FAIL  support-foot    Support foot: max |lower foot - floor| 0.0741 leg lengths at frame 137 over 299 grounded frames (floor 139.444 units) [bar <= 0.01]
FAIL  two-feet        Two feet: two-foot frames: max height difference 0.0873 leg lengths at frame 153 over 235 [bar <= 0.02]; lifted frames (sequence ankles > 0.04 apart): 2 of 35 with the lifted foot within 0.01 of the support foot (lowest lift 0.0097 at frame 279) [bar 0]; median rig/sequence lift 0.217 [bar 0.85-1.15]
FAIL  slide           Slide: max support-foot move 0.02234 leg lengths/frame (foot_r, frame 216->217) over 294 steps [bar <= 0.005]
FAIL  floor           Floor: per-support-span floor spread 0.0547 leg lengths over 5 spans [bar <= 0.01, the support-foot band: the table gives this row no number of its own]
FAIL  jitter          Jitter: limbs 1.160x sequence (2.019 vs 1.740 deg/f^2, 8 bones) [bar <= 1.1], trunk+head 1.664x sequence (2.763 vs 1.660 deg/f^2, hip,chest,head) [bar <= 1.1]; joint pairs from the map
PASS  folds           Folds: 0 frames fold over 6 mesh(es) [bar 0]
PASS  pass-through    Pass-through: bottomwear:thigh_r 0 of 313 frames; bottomwear:thigh_l 0 of 313 frames; bottomwear:shin_r 0 of 313 frames; bottomwear:shin_l 0 of 313 frames [bar 0]
PASS  airborne        Airborne: airborne spans 3 (88-91, 179-181, 267-269) [bar 3]; 0 of 10 span frame(s) with a foot not above the floor [bar 0]; min peak airborne foot height 0.0835 leg lengths above the floor at frame 89 (span 88-91) [bar > 0.01: above the support-foot band]
FAIL  hip-vertical    Hip vertical range: rig/sequence 0.265 (rig 0.0242, sequence 0.0997 leg lengths, median per-span width over 5 spans) [bar 0.85-1.15]
PASS  hip-horizontal  Hip horizontal range: rig/sequence 1.094 (rig 0.5355, sequence 0.4338 hip widths, median per-span width over 5 spans) [bar 0.85-1.15]
FAIL  rebound         Rebound: median rig/sequence peak upward hip acceleration in the stance windows 0.647 over 2 windows [bar 0.7-1.43]
PASS  hip-tilt        Hip tilt: rig tilt range 54.769 deg = 1.000 of the sequence's 54.769 [bar >= 0.85], sign agrees (covariance +4.36e+04)
RESULT FAIL (6 pass, 7 fail, 0 skip of 13 rows)
[exit 1]
```

```
$ npx rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --out run/v2/motion.json --report run/v2/report.json --camera run/v2/camera.json  > run/v2/retarget.stdout 2>&1; echo retarget exit $?; grep -E 'GATE|FEET|STANCE|LEG-SCALE|POSTURE|FAIL|POSE_|refused' run/v2/retarget.stdout | cut -c1-300 | head -30
retarget exit 0
  FEET   read, not planted (no --plant-feet): leg length (median hip → ankle) r 608.6px, l 613.1px; 5 support span(s), 1 change(s) of support, 3 jump(s), 1 step(s)
  FEET   supports: l 0–62, r 63–87, l 92–177, r 183–266, l 272–312
  FEET   jumps (both ankles and mid_hip > 0.05 leg lengths above their rolling floor, ≥ 2 frames): 88–91, 179–181, 267–269
  FEET   steps (the supporting ankle > 0.03 leg lengths a frame; re-planted after 2 frames < 0.01): l 178–184 → the pose's travel, re-planted at 185
  GATE   rigc build --profile spine: green — 52 assertions: 24 measured (24 passed, 0 failed), 14 skipped, 14 not in profile "spine"
  POSTURE hip tilt range (chain "pelvis", r_hip → l_hip, Spine degrees): reference 54.8° (−24.4° … +30.4°), rig 54.8° (−24.4° … +30.4°) — rig/reference 1.000; tilt measured (B' v2.2 skirt waistband (rig-c/pose#86)) on 313 frame(s): 168 read, 18 interpolated, 127 scaled (scaled: 178
  POSTURE sway, x-range of mid_hip − mid_shoulder: reference 114.9 units = picture px × scale (0.960 shoulder widths), rig 145.6 units (1.209 shoulder widths; mid_hip = "hip", mid_shoulder = "sleeve_r0+sleeve_l0") — rig/reference 1.268 in units, 1.260 in shoulder widths
  FEET   the posed build, outside jumps: the lowest ankle's vertical range 73.67 units = 0.1420 leg lengths (rig leg r 512.9, l 524.5 units) over 303 frames
  FEET   the supporting ankle over each support span: worst vertical range 65.44 units = 0.1276 leg lengths (r 183–266), worst horizontal drift 53.72 units = 0.1047 leg lengths (r 183–266)
[exit 0]
```

```
$ npx rigc build --rig inputs/rig/rig.json --motion run/v2/motion.json --out run/v2/build > run/v2/build.stdout 2>&1; echo build exit $?; grep assertions run/v2/build.stdout
build exit 0
  ..    52 assertions: 24 measured (24 passed, 0 failed), 14 skipped, 14 not in profile "spine"
[exit 0]
```

```
$ npx rigc render --candidate run/v2/build --animation dance --fps 24 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l,bottomwear:shin_r,bottomwear:shin_l --out run/v2/render > run/v2/render.stdout 2>&1; echo render exit $?; grep -E 'fold|pass ' run/v2/render.stdout | cut -c1-200
render exit 0
  ..    dance            313 frame(s), 13.000s + contact.png + geometry.json + folds.json (0 of 6 mesh(es) fold) + pass-through.json (0 of 4 pair(s) pass through) -> [path cut off in the original]
  ..    pass     "dance": cloth "bottomwear" over leg "thigh_r" passes through on 0 of 313 frame(s) read at 24 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0489) on its left side
  ..    pass     "dance": cloth "bottomwear" over leg "thigh_l" passes through on 0 of 313 frame(s) read at 24 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0489) on its left side
  ..    pass     "dance": cloth "bottomwear" over leg "shin_r" passes through on 0 of 313 frame(s) read at 24 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0489) on its left side
  ..    pass     "dance": cloth "bottomwear" over leg "shin_l" passes through on 0 of 313 frame(s) read at 24 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0489) on its left side
[exit 0]
```

```
$ <session scratchpad>/g.sh run/v2
grade R3
NOTE  camera submission: present, rig-pose-camera/1, 313 entries, t = report frameTimes (max difference 0.000000 s)
NOTE  airborne spans: report feet.jumps, 3 span(s)
NOTE  rig leg length 518.8746 units (setup pose, leg_l0->foot_l, leg_r0->foot_r); hip width 92.2020
NOTE  sequence leg length 722.45 (95th percentile hip->ankle, mean of sides, the sequence's own units); the sequence's joints are camera-normalised, not divided by camera.s again
PASS  gate            Gate: build green (52 assertions: 24 measured, 0 failed); 14/14 landings within tolerance (worst at 0.17 of its tolerance)
FAIL  support-foot    Support foot: max |lower foot - floor| 0.0741 leg lengths at frame 137 over 299 grounded frames (floor 139.444 units) [bar <= 0.01]
FAIL  two-feet        Two feet: two-foot frames: max height difference 0.0873 leg lengths at frame 153 over 235 [bar <= 0.02]; lifted frames (sequence ankles > 0.04 apart): 2 of 35 with the lifted foot within 0.01 of the support foot (lowest lift 0.0097 at frame 279) [bar 0]; median rig/sequence lift 0.217 [bar 0.85-1.15]
FAIL  slide           Slide: max support-foot move 0.02234 leg lengths/frame (foot_r, frame 216->217) over 294 steps [bar <= 0.005]
FAIL  floor           Floor: per-support-span floor spread 0.0547 leg lengths over 5 spans [bar <= 0.01, the support-foot band: the table gives this row no number of its own]
PASS  jitter          Jitter: limbs 1.000x sequence (1.740 vs 1.740 deg/f^2, 8 bones) [bar <= 1.1], trunk+head 1.060x sequence (1.760 vs 1.660 deg/f^2, hip,chest,head) [bar <= 1.1]; joint pairs from the map
PASS  folds           Folds: 0 frames fold over 6 mesh(es) [bar 0]
PASS  pass-through    Pass-through: bottomwear:thigh_r 0 of 313 frames; bottomwear:thigh_l 0 of 313 frames; bottomwear:shin_r 0 of 313 frames; bottomwear:shin_l 0 of 313 frames [bar 0]
PASS  airborne        Airborne: airborne spans 3 (88-91, 179-181, 267-269) [bar 3]; 0 of 10 span frame(s) with a foot not above the floor [bar 0]; min peak airborne foot height 0.0835 leg lengths above the floor at frame 89 (span 88-91) [bar > 0.01: above the support-foot band]
FAIL  hip-vertical    Hip vertical range: rig/sequence 0.265 (rig 0.0242, sequence 0.0997 leg lengths, median per-span width over 5 spans) [bar 0.85-1.15]
PASS  hip-horizontal  Hip horizontal range: rig/sequence 1.094 (rig 0.5355, sequence 0.4338 hip widths, median per-span width over 5 spans) [bar 0.85-1.15]
FAIL  rebound         Rebound: median rig/sequence peak upward hip acceleration in the stance windows 0.647 over 2 windows [bar 0.7-1.43]
PASS  hip-tilt        Hip tilt: rig tilt range 54.769 deg = 1.000 of the sequence's 54.769 [bar >= 0.85], sign agrees (covariance +4.36e+04)
RESULT FAIL (7 pass, 6 fail, 0 skip of 13 rows)
[exit 1]
```

```
$ npx rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --out run/v3/motion.json --report run/v3/report.json --camera run/v3/camera.json --leg-scale 0.8,1.05 --plant-feet --stance 0.07 > run/v3/retarget.stdout 2>&1; echo retarget exit $?; grep -E 'GATE|FEET|STANCE|LEG-SCALE|POSTURE|FAIL|POSE_|refused' run/v3/retarget.stdout | cut -c1-300 | head -30
retarget exit 0
  LEG-SCALE chain "leg_r" bone "leg_r0" (r_hip → r_knee): straight length 305.0px (larger 95th percentile of 313 frames, both legs); picture length ÷ straight 0.802 … 1.098 (median 0.968); scalex keyed in [0.8, 1.05]: none under 0.8; 11 frame(s) over 1.05, clamped (frames 266–276) (asked 1.05
  LEG-SCALE chain "leg_r" bone "leg_r1" (r_knee → r_ankle): straight length 279.0px (larger 95th percentile of 313 frames, both legs); picture length ÷ straight 0.683 … 1.068 (median 0.882); scalex keyed in [0.8, 1.05]: 51 frame(s) under 0.8, clamped (frames 94–100, 103–108, 115–118, 123�
  LEG-SCALE chain "leg_l" bone "leg_l0" (l_hip → l_knee): straight length 314.4px (larger 95th percentile of 313 frames, both legs); picture length ÷ straight 0.802 … 1.008 (median 0.907); scalex keyed in [0.8, 1.05]: none under 0.8; none over 1.05
  LEG-SCALE chain "leg_l" bone "leg_l1" (l_knee → l_ankle): straight length 282.4px (larger 95th percentile of 313 frames, both legs); picture length ÷ straight 0.694 … 1.083 (median 0.949); scalex keyed in [0.8, 1.05]: 30 frame(s) under 0.8, clamped (frames 94–97, 106–108, 114–118, 126�
  LEG-SCALE past the floor (support): chain "leg_r" bone "leg_r1" (supporting foot r) frames 183–186 (t=7.625–7.750s) — asked 0.6989–0.7663 under 0.8, used 0.6989–0.7663 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_r" bone "leg_r1" (supporting foot r) frames 194–196 (t=8.083–8.167s) — asked 0.7551–0.7761 under 0.8, used 0.7551–0.7761 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_r" bone "leg_r1" (supporting foot r) frames 205–206 (t=8.542–8.583s) — asked 0.7865–0.7876 under 0.8, used 0.7865–0.7876 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_r" bone "leg_r1" (supporting foot r) frames 214–217 (t=8.917–9.042s) — asked 0.7373–0.7909 under 0.8, used 0.7373–0.7909 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_r" bone "leg_r1" (supporting foot r) frame 226 (t=9.417s) — asked 0.7925 under 0.8, used 0.7925 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_r" bone "leg_r1" (supporting foot r) frame 237 (t=9.875s) — asked 0.7986 under 0.8, used 0.7986 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_r" bone "leg_r1" (supporting foot r) frames 260–263 (t=10.833–10.958s) — asked 0.7815–0.7999 under 0.8, used 0.7815–0.7999 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_l" bone "leg_l1" (supporting foot l) frames 94–97 (t=3.917–4.042s) — asked 0.6939–0.7462 under 0.8, used 0.6939–0.7462 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_l" bone "leg_l1" (supporting foot l) frames 106–108 (t=4.417–4.500s) — asked 0.7464–0.7665 under 0.8, used 0.7464–0.7665 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_l" bone "leg_l1" (supporting foot l) frames 114–118 (t=4.750–4.917s) — asked 0.7384–0.7995 under 0.8, used 0.7384–0.7995 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_l" bone "leg_l1" (supporting foot l) frames 126–128 (t=5.250–5.333s) — asked 0.7648–0.7921 under 0.8, used 0.7648–0.7921 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_l" bone "leg_l1" (supporting foot l) frames 136–139 (t=5.667–5.792s) — asked 0.7342–0.7908 under 0.8, used 0.7342–0.7908 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_l" bone "leg_l1" (supporting foot l) frames 148–149 (t=6.167–6.208s) — asked 0.7720–0.7726 under 0.8, used 0.7720–0.7726 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_l" bone "leg_l1" (supporting foot l) frames 158–159 (t=6.583–6.625s) — asked 0.7753–0.7805 under 0.8, used 0.7753–0.7805 (within the leg's own range, #95; ankle stays on the floor)
  FEET   planted: leg length (median hip → ankle) r 608.6px, l 613.1px; 5 support span(s), 1 change(s) of support, 3 jump(s), 1 step(s)
  FEET   supports: l 0–62, r 63–87, l 92–177, r 183–266, l 272–312
  FEET   jumps (both ankles and mid_hip > 0.05 leg lengths above their rolling floor, ≥ 2 frames): 88–91, 179–181, 267–269
  FEET   support read from the lower ankle (a foot ≥ 0.02 leg lengths higher than the other does not take support, rig-c/pose#113): no frame reads differently from before
  FEET   steps (the supporting ankle > 0.03 leg lengths a frame; re-planted after 2 frames < 0.01): l 178–184 → the pose's travel, re-planted at 185
  FEET   floor: world y 212.03 (the median of the 5 support span(s)' planted heights); each span's supporting ankle moved onto it, the hip and everything above with it — shift per span in units (leg lengths: the rig's at setup, thigh origin → ankle, r 513.1, l 524.6 units): l 0–62 +35.46 (+0.0
  FEET   blend held on the floor: supporting foot r frames 63–65 (t=2.625–2.708s) — the hip blends between two derivations there, so its leg is stretched by k 0.9850–0.9933 within [0.92, 1.08] to keep the ankle on the floor
  FEET   blend held on the floor: supporting foot l frames 93–94 (t=3.875–3.917s) — the hip blends between two derivations there, so its leg is stretched by k 1.0028–1.0100 within [0.7991, 1.08] to keep the ankle on the floor
  FEET   blend held on the floor: supporting foot r frames 184–185 (t=7.667–7.708s) — the hip blends between two derivations there, so its leg is stretched by k 1.0073–1.0166 within [0.7425, 1.08] to keep the ankle on the floor
  FEET   blend held on the floor: supporting foot l frames 273–274 (t=11.375–11.417s) — the hip blends between two derivations there, so its leg is stretched by k 0.9964–0.9982 within [0.92, 1.08] to keep the ankle on the floor
  FEET   bound from the leg's own range: on a frame where the picture folds the supporting leg below 0.92 of its straight length (hip → ankle, its 95th percentile), the lower bound is that fold — lowest r 0.7425, l 0.7991; the upper stays 1.08
  STANCE planted both: free foot r frames 0–62 (t=0.000–2.583s) — its ankle up to 0.0263 leg lengths above the supporting one in the picture, within the tolerance 0.07 leg lengths; its leg stretched by k 0.9744 … 1.0321 (largest 1.0321)
[exit 0]
```

```
$ npx rigc build --rig inputs/rig/rig.json --motion run/v3/motion.json --out run/v3/build > run/v3/build.stdout 2>&1; echo build exit $?; grep assertions run/v3/build.stdout
build exit 0
  ..    52 assertions: 24 measured (24 passed, 0 failed), 14 skipped, 14 not in profile "spine"
[exit 0]
```

```
$ npx rigc render --candidate run/v3/build --animation dance --fps 24 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l,bottomwear:shin_r,bottomwear:shin_l --out run/v3/render > run/v3/render.stdout 2>&1; echo render exit $?; grep -E 'fold|pass ' run/v3/render.stdout | cut -c1-200
render exit 0
  ..    dance            313 frame(s), 13.000s + contact.png + geometry.json + folds.json (0 of 6 mesh(es) fold) + pass-through.json (0 of 4 pair(s) pass through) -> [path cut off in the original]
  ..    pass     "dance": cloth "bottomwear" over leg "thigh_r" passes through on 0 of 313 frame(s) read at 24 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0489) on its left side
  ..    pass     "dance": cloth "bottomwear" over leg "thigh_l" passes through on 0 of 313 frame(s) read at 24 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0489) on its left side
  ..    pass     "dance": cloth "bottomwear" over leg "shin_r" passes through on 0 of 313 frame(s) read at 24 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0489) on its left side
  ..    pass     "dance": cloth "bottomwear" over leg "shin_l" passes through on 0 of 313 frame(s) read at 24 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0489) on its left side
[exit 0]
```

```
$ <session scratchpad>/g.sh run/v3
grade R3
NOTE  camera submission: present, rig-pose-camera/1, 313 entries, t = report frameTimes (max difference 0.000000 s)
NOTE  airborne spans: report feet.jumps, 3 span(s)
NOTE  rig leg length 518.8746 units (setup pose, leg_l0->foot_l, leg_r0->foot_r); hip width 92.2020
NOTE  sequence leg length 722.45 (95th percentile hip->ankle, mean of sides, the sequence's own units); the sequence's joints are camera-normalised, not divided by camera.s again
PASS  gate            Gate: build green (52 assertions: 24 measured, 0 failed); 20/20 landings within tolerance (worst at 0.17 of its tolerance)
PASS  support-foot    Support foot: max |lower foot - floor| 0.0000 leg lengths at frame 235 over 299 grounded frames (floor 212.032 units) [bar <= 0.01]
FAIL  two-feet        Two feet: two-foot frames: max height difference 0.0000 leg lengths at frame 234 over 235 [bar <= 0.02]; lifted frames (sequence ankles > 0.04 apart): 35 of 35 with the lifted foot within 0.01 of the support foot (lowest lift -0.0000 at frame 295) [bar 0]; median rig/sequence lift -0.000 [bar 0.85-1.15]
PASS  slide           Slide: max support-foot move 0.00003 leg lengths/frame (foot_l, frame 277->278) over 294 steps [bar <= 0.005]
PASS  floor           Floor: per-support-span floor spread 0.0000 leg lengths over 5 spans [bar <= 0.01, the support-foot band: the table gives this row no number of its own]
PASS  jitter          Jitter: limbs 0.990x sequence (1.722 vs 1.740 deg/f^2, 8 bones) [bar <= 1.1], trunk+head 1.060x sequence (1.760 vs 1.660 deg/f^2, hip,chest,head) [bar <= 1.1]; joint pairs from the map
PASS  folds           Folds: 0 frames fold over 6 mesh(es) [bar 0]
PASS  pass-through    Pass-through: bottomwear:thigh_r 0 of 313 frames; bottomwear:thigh_l 0 of 313 frames; bottomwear:shin_r 0 of 313 frames; bottomwear:shin_l 0 of 313 frames [bar 0]
PASS  airborne        Airborne: airborne spans 3 (88-91, 179-181, 267-269) [bar 3]; 0 of 10 span frame(s) with a foot not above the floor [bar 0]; min peak airborne foot height 0.0245 leg lengths above the floor at frame 179 (span 179-181) [bar > 0.01: above the support-foot band]
PASS  hip-vertical    Hip vertical range: rig/sequence 1.049 (rig 0.1067, sequence 0.0997 leg lengths, median per-span width over 5 spans) [bar 0.85-1.15]
PASS  hip-horizontal  Hip horizontal range: rig/sequence 1.023 (rig 0.5239, sequence 0.4338 hip widths, median per-span width over 5 spans) [bar 0.85-1.15]
PASS  rebound         Rebound: median rig/sequence peak upward hip acceleration in the stance windows 1.334 over 2 windows [bar 0.7-1.43]
PASS  hip-tilt        Hip tilt: rig tilt range 54.769 deg = 1.000 of the sequence's 54.769 [bar >= 0.85], sign agrees (covariance +4.36e+04)
RESULT FAIL (12 pass, 1 fail, 0 skip of 13 rows)
[exit 1]
```

```
$ npx rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --out run/v4/motion.json --report run/v4/report.json --camera run/v4/camera.json --leg-scale 0.8,1.05 --plant-feet --stance 0.03 > run/v4/retarget.stdout 2>&1; echo retarget exit $?; grep -E 'GATE|FEET|STANCE|LEG-SCALE|POSTURE|FAIL|POSE_|refused' run/v4/retarget.stdout | cut -c1-300 | head -30
retarget exit 0
  LEG-SCALE chain "leg_r" bone "leg_r0" (r_hip → r_knee): straight length 305.0px (larger 95th percentile of 313 frames, both legs); picture length ÷ straight 0.802 … 1.098 (median 0.968); scalex keyed in [0.8, 1.05]: none under 0.8; 11 frame(s) over 1.05, clamped (frames 266–276) (asked 1.05
  LEG-SCALE chain "leg_r" bone "leg_r1" (r_knee → r_ankle): straight length 279.0px (larger 95th percentile of 313 frames, both legs); picture length ÷ straight 0.683 … 1.068 (median 0.882); scalex keyed in [0.8, 1.05]: 51 frame(s) under 0.8, clamped (frames 94–100, 103–108, 115–118, 123�
  LEG-SCALE chain "leg_l" bone "leg_l0" (l_hip → l_knee): straight length 314.4px (larger 95th percentile of 313 frames, both legs); picture length ÷ straight 0.802 … 1.008 (median 0.907); scalex keyed in [0.8, 1.05]: none under 0.8; none over 1.05
  LEG-SCALE chain "leg_l" bone "leg_l1" (l_knee → l_ankle): straight length 282.4px (larger 95th percentile of 313 frames, both legs); picture length ÷ straight 0.694 … 1.083 (median 0.949); scalex keyed in [0.8, 1.05]: 30 frame(s) under 0.8, clamped (frames 94–97, 106–108, 114–118, 126�
  LEG-SCALE past the floor (support): chain "leg_r" bone "leg_r1" (supporting foot r) frames 183–186 (t=7.625–7.750s) — asked 0.6989–0.7663 under 0.8, used 0.6989–0.7663 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_r" bone "leg_r1" (supporting foot r) frames 194–196 (t=8.083–8.167s) — asked 0.7551–0.7761 under 0.8, used 0.7551–0.7761 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_r" bone "leg_r1" (supporting foot r) frames 205–206 (t=8.542–8.583s) — asked 0.7865–0.7876 under 0.8, used 0.7865–0.7876 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_r" bone "leg_r1" (supporting foot r) frames 214–217 (t=8.917–9.042s) — asked 0.7373–0.7909 under 0.8, used 0.7373–0.7909 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_r" bone "leg_r1" (supporting foot r) frame 226 (t=9.417s) — asked 0.7925 under 0.8, used 0.7925 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_r" bone "leg_r1" (supporting foot r) frame 237 (t=9.875s) — asked 0.7986 under 0.8, used 0.7986 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_r" bone "leg_r1" (supporting foot r) frames 260–263 (t=10.833–10.958s) — asked 0.7815–0.7999 under 0.8, used 0.7815–0.7999 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_l" bone "leg_l1" (supporting foot l) frames 94–97 (t=3.917–4.042s) — asked 0.6939–0.7462 under 0.8, used 0.6939–0.7462 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_l" bone "leg_l1" (supporting foot l) frames 106–108 (t=4.417–4.500s) — asked 0.7464–0.7665 under 0.8, used 0.7464–0.7665 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_l" bone "leg_l1" (supporting foot l) frames 114–118 (t=4.750–4.917s) — asked 0.7384–0.7995 under 0.8, used 0.7384–0.7995 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_l" bone "leg_l1" (supporting foot l) frames 126–128 (t=5.250–5.333s) — asked 0.7648–0.7921 under 0.8, used 0.7648–0.7921 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_l" bone "leg_l1" (supporting foot l) frames 136–139 (t=5.667–5.792s) — asked 0.7342–0.7908 under 0.8, used 0.7342–0.7908 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_l" bone "leg_l1" (supporting foot l) frames 148–149 (t=6.167–6.208s) — asked 0.7720–0.7726 under 0.8, used 0.7720–0.7726 (within the leg's own range, #95; ankle stays on the floor)
  LEG-SCALE past the floor (support): chain "leg_l" bone "leg_l1" (supporting foot l) frames 158–159 (t=6.583–6.625s) — asked 0.7753–0.7805 under 0.8, used 0.7753–0.7805 (within the leg's own range, #95; ankle stays on the floor)
  FEET   planted: leg length (median hip → ankle) r 608.6px, l 613.1px; 5 support span(s), 1 change(s) of support, 3 jump(s), 1 step(s)
  FEET   supports: l 0–62, r 63–87, l 92–177, r 183–266, l 272–312
  FEET   jumps (both ankles and mid_hip > 0.05 leg lengths above their rolling floor, ≥ 2 frames): 88–91, 179–181, 267–269
  FEET   support read from the lower ankle (a foot ≥ 0.02 leg lengths higher than the other does not take support, rig-c/pose#113): no frame reads differently from before
  FEET   steps (the supporting ankle > 0.03 leg lengths a frame; re-planted after 2 frames < 0.01): l 178–184 → the pose's travel, re-planted at 185
  FEET   floor: world y 212.03 (the median of the 5 support span(s)' planted heights); each span's supporting ankle moved onto it, the hip and everything above with it — shift per span in units (leg lengths: the rig's at setup, thigh origin → ankle, r 513.1, l 524.6 units): l 0–62 +35.46 (+0.0
  FEET   blend held on the floor: supporting foot r frames 63–65 (t=2.625–2.708s) — the hip blends between two derivations there, so its leg is stretched by k 0.9850–0.9933 within [0.92, 1.08] to keep the ankle on the floor
  FEET   blend held on the floor: supporting foot l frames 93–94 (t=3.875–3.917s) — the hip blends between two derivations there, so its leg is stretched by k 1.0028–1.0100 within [0.7991, 1.08] to keep the ankle on the floor
  FEET   blend held on the floor: supporting foot r frames 184–185 (t=7.667–7.708s) — the hip blends between two derivations there, so its leg is stretched by k 1.0073–1.0166 within [0.7425, 1.08] to keep the ankle on the floor
  FEET   blend held on the floor: supporting foot l frames 273–274 (t=11.375–11.417s) — the hip blends between two derivations there, so its leg is stretched by k 0.9964–0.9982 within [0.92, 1.08] to keep the ankle on the floor
  FEET   bound from the leg's own range: on a frame where the picture folds the supporting leg below 0.92 of its straight length (hip → ankle, its 95th percentile), the lower bound is that fold — lowest r 0.7425, l 0.7991; the upper stays 1.08
  STANCE planted both: free foot r frames 0–62 (t=0.000–2.583s) — its ankle up to 0.0263 leg lengths above the supporting one in the picture, within the tolerance 0.03 leg lengths; its leg stretched by k 0.9744 … 1.0321 (largest 1.0321)
[exit 0]
```

```
$ npx rigc build --rig inputs/rig/rig.json --motion run/v4/motion.json --out run/v4/build > run/v4/build.stdout 2>&1; echo build exit $?; grep assertions run/v4/build.stdout
build exit 0
  ..    52 assertions: 24 measured (24 passed, 0 failed), 14 skipped, 14 not in profile "spine"
[exit 0]
```

```
$ npx rigc render --candidate run/v4/build --animation dance --fps 24 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l,bottomwear:shin_r,bottomwear:shin_l --out run/v4/render > run/v4/render.stdout 2>&1; echo render exit $?; grep -E 'fold|pass ' run/v4/render.stdout | cut -c1-200
render exit 0
  ..    dance            313 frame(s), 13.000s + contact.png + geometry.json + folds.json (0 of 6 mesh(es) fold) + pass-through.json (0 of 4 pair(s) pass through) -> [path cut off in the original]
  ..    pass     "dance": cloth "bottomwear" over leg "thigh_r" passes through on 0 of 313 frame(s) read at 24 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0489) on its left side
  ..    pass     "dance": cloth "bottomwear" over leg "thigh_l" passes through on 0 of 313 frame(s) read at 24 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0489) on its left side
  ..    pass     "dance": cloth "bottomwear" over leg "shin_r" passes through on 0 of 313 frame(s) read at 24 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0489) on its left side
  ..    pass     "dance": cloth "bottomwear" over leg "shin_l" passes through on 0 of 313 frame(s) read at 24 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0489) on its left side
[exit 0]
```

```
$ <session scratchpad>/g.sh run/v4
grade R3
NOTE  camera submission: present, rig-pose-camera/1, 313 entries, t = report frameTimes (max difference 0.000000 s)
NOTE  airborne spans: report feet.jumps, 3 span(s)
NOTE  rig leg length 518.8746 units (setup pose, leg_l0->foot_l, leg_r0->foot_r); hip width 92.2020
NOTE  sequence leg length 722.45 (95th percentile hip->ankle, mean of sides, the sequence's own units); the sequence's joints are camera-normalised, not divided by camera.s again
PASS  gate            Gate: build green (52 assertions: 24 measured, 0 failed); 20/20 landings within tolerance (worst at 0.17 of its tolerance)
PASS  support-foot    Support foot: max |lower foot - floor| 0.0000 leg lengths at frame 235 over 299 grounded frames (floor 212.032 units) [bar <= 0.01]
PASS  two-feet        Two feet: two-foot frames: max height difference 0.0000 leg lengths at frame 234 over 235 [bar <= 0.02]; lifted frames (sequence ankles > 0.04 apart): 0 of 35 with the lifted foot within 0.01 of the support foot (lowest lift 0.0390 at frame 278) [bar 0]; median rig/sequence lift 0.933 [bar 0.85-1.15]
PASS  slide           Slide: max support-foot move 0.00003 leg lengths/frame (foot_l, frame 277->278) over 294 steps [bar <= 0.005]
PASS  floor           Floor: per-support-span floor spread 0.0000 leg lengths over 5 spans [bar <= 0.01, the support-foot band: the table gives this row no number of its own]
PASS  jitter          Jitter: limbs 0.989x sequence (1.721 vs 1.740 deg/f^2, 8 bones) [bar <= 1.1], trunk+head 1.060x sequence (1.760 vs 1.660 deg/f^2, hip,chest,head) [bar <= 1.1]; joint pairs from the map
PASS  folds           Folds: 0 frames fold over 6 mesh(es) [bar 0]
PASS  pass-through    Pass-through: bottomwear:thigh_r 0 of 313 frames; bottomwear:thigh_l 0 of 313 frames; bottomwear:shin_r 0 of 313 frames; bottomwear:shin_l 0 of 313 frames [bar 0]
PASS  airborne        Airborne: airborne spans 3 (88-91, 179-181, 267-269) [bar 3]; 0 of 10 span frame(s) with a foot not above the floor [bar 0]; min peak airborne foot height 0.0245 leg lengths above the floor at frame 179 (span 179-181) [bar > 0.01: above the support-foot band]
PASS  hip-vertical    Hip vertical range: rig/sequence 1.049 (rig 0.1067, sequence 0.0997 leg lengths, median per-span width over 5 spans) [bar 0.85-1.15]
PASS  hip-horizontal  Hip horizontal range: rig/sequence 1.023 (rig 0.5239, sequence 0.4338 hip widths, median per-span width over 5 spans) [bar 0.85-1.15]
PASS  rebound         Rebound: median rig/sequence peak upward hip acceleration in the stance windows 1.334 over 2 windows [bar 0.7-1.43]
PASS  hip-tilt        Hip tilt: rig tilt range 54.769 deg = 1.000 of the sequence's 54.769 [bar >= 0.85], sign agrees (covariance +4.36e+04)
RESULT PASS (13 pass, 0 fail, 0 skip of 13 rows)
[exit 0]
```

```
$ cp -R run/v4 run/after (motion.json report.json camera.json build/ build.stdout render/ retarget.stdout)
bash: -c: line 0: `cp -R run/v4 run/after (motion.json report.json camera.json build/ build.stdout render/ retarget.stdout)'
[exit 2]
```

```
$ npx rigc render --candidate run/after/build --animation dance --fps 24 --max 640 --out run/evidence/render_after_640
  ..    510x640px at 24 fps, 1 set(s) -> run/evidence/render_after_640
  ..    dance            313 frame(s), 13.000s + contact.png -> run/evidence/render_after_640/dance@24fps
rigc: wrote run/evidence/render_after_640/frames.json
[exit 0]
```

```
$ npx rigc render --candidate run/before/build --animation dance --fps 24 --viewport-from run/evidence/render_after_640 --out run/evidence/render_before_640
  ..    viewport given by --viewport-from run/evidence/render_after_640/frames.json: world x -574.9477..499.6829, y -22.6796..1327.0537 at 0.4742 px per unit, y up (fitted, the box would be world x -574.2938..469.3265, y -49.564..1282.513) — every drawn piece of every frame is inside it
  ..    dance            313 frame(s), 13.000s + contact.png -> run/evidence/render_before_640/dance@24fps
rigc: wrote run/evidence/render_before_640/frames.json
[exit 0]
```

```
$ rm -rf run/after && cp -R run/v4 run/after
(no output; the logging wrapper line above failed on its parentheses, the copy itself ran)
[exit 0]
```

```
$ ffmpeg -v error -y -i inputs/pose/stick.mp4 -i run/evidence/render_before_640/dance@24fps/f0020.png -i run/evidence/render_after_640/dance@24fps/f0020.png -filter_complex "[0:v]select=eq(n\,20),scale=-2:640[a];[1:v]scale=-2:640[b];[2:v]scale=-2:640[c];[a][b][c]hstack=inputs=3,drawtext=text='frame 20  stick | before | after':x=10:y=10:fontsize=24:fontcolor=red" -frames:v 1 run/evidence/frame_0020.png
[AVFilterGraph @ 0x903008380] No such filter: 'drawtext'
Error : Filter not found
[exit 8]
```

```
$ ffmpeg -v error -y -i inputs/pose/stick.mp4 -i run/evidence/render_before_640/dance@24fps/f0089.png -i run/evidence/render_after_640/dance@24fps/f0089.png -filter_complex "[0:v]select=eq(n\,89),scale=-2:640[a];[1:v]scale=-2:640[b];[2:v]scale=-2:640[c];[a][b][c]hstack=inputs=3,drawtext=text='frame 89  stick | before | after':x=10:y=10:fontsize=24:fontcolor=red" -frames:v 1 run/evidence/frame_0089.png
[AVFilterGraph @ 0x97ac18000] No such filter: 'drawtext'
Error : Filter not found
[exit 8]
```

```
$ ffmpeg -v error -y -i inputs/pose/stick.mp4 -i run/evidence/render_before_640/dance@24fps/f0150.png -i run/evidence/render_after_640/dance@24fps/f0150.png -filter_complex "[0:v]select=eq(n\,150),scale=-2:640[a];[1:v]scale=-2:640[b];[2:v]scale=-2:640[c];[a][b][c]hstack=inputs=3,drawtext=text='frame 150  stick | before | after':x=10:y=10:fontsize=24:fontcolor=red" -frames:v 1 run/evidence/frame_0150.png
[AVFilterGraph @ 0xa6701c000] No such filter: 'drawtext'
Error : Filter not found
[exit 8]
```

```
$ ffmpeg -v error -y -i inputs/pose/stick.mp4 -i run/evidence/render_before_640/dance@24fps/f0180.png -i run/evidence/render_after_640/dance@24fps/f0180.png -filter_complex "[0:v]select=eq(n\,180),scale=-2:640[a];[1:v]scale=-2:640[b];[2:v]scale=-2:640[c];[a][b][c]hstack=inputs=3,drawtext=text='frame 180  stick | before | after':x=10:y=10:fontsize=24:fontcolor=red" -frames:v 1 run/evidence/frame_0180.png
[AVFilterGraph @ 0xadb020000] No such filter: 'drawtext'
Error : Filter not found
[exit 8]
```

```
$ ffmpeg -v error -y -i inputs/pose/stick.mp4 -i run/evidence/render_before_640/dance@24fps/f0230.png -i run/evidence/render_after_640/dance@24fps/f0230.png -filter_complex "[0:v]select=eq(n\,230),scale=-2:640[a];[1:v]scale=-2:640[b];[2:v]scale=-2:640[c];[a][b][c]hstack=inputs=3,drawtext=text='frame 230  stick | before | after':x=10:y=10:fontsize=24:fontcolor=red" -frames:v 1 run/evidence/frame_0230.png
[AVFilterGraph @ 0xa7b020000] No such filter: 'drawtext'
Error : Filter not found
[exit 8]
```

```
$ ffmpeg -v error -y -i inputs/pose/stick.mp4 -i run/evidence/render_before_640/dance@24fps/f0268.png -i run/evidence/render_after_640/dance@24fps/f0268.png -filter_complex "[0:v]select=eq(n\,268),scale=-2:640[a];[1:v]scale=-2:640[b];[2:v]scale=-2:640[c];[a][b][c]hstack=inputs=3,drawtext=text='frame 268  stick | before | after':x=10:y=10:fontsize=24:fontcolor=red" -frames:v 1 run/evidence/frame_0268.png
[AVFilterGraph @ 0x80501c000] No such filter: 'drawtext'
Error : Filter not found
[exit 8]
```

```
$ ffmpeg -v error -y -i inputs/pose/stick.mp4 -i run/evidence/render_before_640/dance@24fps/f0295.png -i run/evidence/render_after_640/dance@24fps/f0295.png -filter_complex "[0:v]select=eq(n\,295),scale=-2:640[a];[1:v]scale=-2:640[b];[2:v]scale=-2:640[c];[a][b][c]hstack=inputs=3,drawtext=text='frame 295  stick | before | after':x=10:y=10:fontsize=24:fontcolor=red" -frames:v 1 run/evidence/frame_0295.png
[AVFilterGraph @ 0x817008380] No such filter: 'drawtext'
Error : Filter not found
[exit 8]
```

```
$ ffmpeg -v error -y -i inputs/pose/stick.mp4 -i run/evidence/render_before_640/dance@24fps/f0020.png -i run/evidence/render_after_640/dance@24fps/f0020.png -filter_complex "[0:v]select=eq(n\,20),scale=-2:640[a];[1:v]scale=-2:640[b];[2:v]scale=-2:640[c];[a][b][c]hstack=inputs=3" -frames:v 1 run/evidence/frame_0020_stick_before_after.png

[exit 0]
```

```
$ ffmpeg -v error -y -i inputs/pose/stick.mp4 -i run/evidence/render_before_640/dance@24fps/f0089.png -i run/evidence/render_after_640/dance@24fps/f0089.png -filter_complex "[0:v]select=eq(n\,89),scale=-2:640[a];[1:v]scale=-2:640[b];[2:v]scale=-2:640[c];[a][b][c]hstack=inputs=3" -frames:v 1 run/evidence/frame_0089_stick_before_after.png

[exit 0]
```

```
$ ffmpeg -v error -y -i inputs/pose/stick.mp4 -i run/evidence/render_before_640/dance@24fps/f0150.png -i run/evidence/render_after_640/dance@24fps/f0150.png -filter_complex "[0:v]select=eq(n\,150),scale=-2:640[a];[1:v]scale=-2:640[b];[2:v]scale=-2:640[c];[a][b][c]hstack=inputs=3" -frames:v 1 run/evidence/frame_0150_stick_before_after.png

[exit 0]
```

```
$ ffmpeg -v error -y -i inputs/pose/stick.mp4 -i run/evidence/render_before_640/dance@24fps/f0180.png -i run/evidence/render_after_640/dance@24fps/f0180.png -filter_complex "[0:v]select=eq(n\,180),scale=-2:640[a];[1:v]scale=-2:640[b];[2:v]scale=-2:640[c];[a][b][c]hstack=inputs=3" -frames:v 1 run/evidence/frame_0180_stick_before_after.png

[exit 0]
```

```
$ ffmpeg -v error -y -i inputs/pose/stick.mp4 -i run/evidence/render_before_640/dance@24fps/f0230.png -i run/evidence/render_after_640/dance@24fps/f0230.png -filter_complex "[0:v]select=eq(n\,230),scale=-2:640[a];[1:v]scale=-2:640[b];[2:v]scale=-2:640[c];[a][b][c]hstack=inputs=3" -frames:v 1 run/evidence/frame_0230_stick_before_after.png

[exit 0]
```

```
$ ffmpeg -v error -y -i inputs/pose/stick.mp4 -i run/evidence/render_before_640/dance@24fps/f0268.png -i run/evidence/render_after_640/dance@24fps/f0268.png -filter_complex "[0:v]select=eq(n\,268),scale=-2:640[a];[1:v]scale=-2:640[b];[2:v]scale=-2:640[c];[a][b][c]hstack=inputs=3" -frames:v 1 run/evidence/frame_0268_stick_before_after.png

[exit 0]
```

```
$ ffmpeg -v error -y -i inputs/pose/stick.mp4 -i run/evidence/render_before_640/dance@24fps/f0295.png -i run/evidence/render_after_640/dance@24fps/f0295.png -filter_complex "[0:v]select=eq(n\,295),scale=-2:640[a];[1:v]scale=-2:640[b];[2:v]scale=-2:640[c];[a][b][c]hstack=inputs=3" -frames:v 1 run/evidence/frame_0295_stick_before_after.png

[exit 0]
```

```
$ <session scratchpad>/g.sh run/after
grade R3
NOTE  camera submission: present, rig-pose-camera/1, 313 entries, t = report frameTimes (max difference 0.000000 s)
NOTE  airborne spans: report feet.jumps, 3 span(s)
NOTE  rig leg length 518.8746 units (setup pose, leg_l0->foot_l, leg_r0->foot_r); hip width 92.2020
NOTE  sequence leg length 722.45 (95th percentile hip->ankle, mean of sides, the sequence's own units); the sequence's joints are camera-normalised, not divided by camera.s again
PASS  gate            Gate: build green (52 assertions: 24 measured, 0 failed); 20/20 landings within tolerance (worst at 0.17 of its tolerance)
PASS  support-foot    Support foot: max |lower foot - floor| 0.0000 leg lengths at frame 235 over 299 grounded frames (floor 212.032 units) [bar <= 0.01]
PASS  two-feet        Two feet: two-foot frames: max height difference 0.0000 leg lengths at frame 234 over 235 [bar <= 0.02]; lifted frames (sequence ankles > 0.04 apart): 0 of 35 with the lifted foot within 0.01 of the support foot (lowest lift 0.0390 at frame 278) [bar 0]; median rig/sequence lift 0.933 [bar 0.85-1.15]
PASS  slide           Slide: max support-foot move 0.00003 leg lengths/frame (foot_l, frame 277->278) over 294 steps [bar <= 0.005]
PASS  floor           Floor: per-support-span floor spread 0.0000 leg lengths over 5 spans [bar <= 0.01, the support-foot band: the table gives this row no number of its own]
PASS  jitter          Jitter: limbs 0.989x sequence (1.721 vs 1.740 deg/f^2, 8 bones) [bar <= 1.1], trunk+head 1.060x sequence (1.760 vs 1.660 deg/f^2, hip,chest,head) [bar <= 1.1]; joint pairs from the map
PASS  folds           Folds: 0 frames fold over 6 mesh(es) [bar 0]
PASS  pass-through    Pass-through: bottomwear:thigh_r 0 of 313 frames; bottomwear:thigh_l 0 of 313 frames; bottomwear:shin_r 0 of 313 frames; bottomwear:shin_l 0 of 313 frames [bar 0]
PASS  airborne        Airborne: airborne spans 3 (88-91, 179-181, 267-269) [bar 3]; 0 of 10 span frame(s) with a foot not above the floor [bar 0]; min peak airborne foot height 0.0245 leg lengths above the floor at frame 179 (span 179-181) [bar > 0.01: above the support-foot band]
PASS  hip-vertical    Hip vertical range: rig/sequence 1.049 (rig 0.1067, sequence 0.0997 leg lengths, median per-span width over 5 spans) [bar 0.85-1.15]
PASS  hip-horizontal  Hip horizontal range: rig/sequence 1.023 (rig 0.5239, sequence 0.4338 hip widths, median per-span width over 5 spans) [bar 0.85-1.15]
PASS  rebound         Rebound: median rig/sequence peak upward hip acceleration in the stance windows 1.334 over 2 windows [bar 0.7-1.43]
PASS  hip-tilt        Hip tilt: rig tilt range 54.769 deg = 1.000 of the sequence's 54.769 [bar >= 0.85], sign agrees (covariance +4.36e+04)
RESULT PASS (13 pass, 0 fail, 0 skip of 13 rows)
[exit 0]
```
finished: 2026-10-18T23:00:51Z
