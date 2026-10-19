started: 2026-10-18T23:35:37Z

```
$ npm install
added 6 packages, and audited 7 packages in 3s
1 package is looking for funding
  run `npm fund` for details
found 0 vulnerabilities
```

```
$ npx rig-pose retarget --rig inputs/rig --map run/before/map.json --pose inputs/pose/sequence.json --out run/before/motion.json --build run/before/build --report run/before/report.json --name run
  GATE   rigc build --profile spine: green — 52 assertions: 21 measured (21 passed, 0 failed), 17 skipped, 14 not in profile "spine"
  ...
  FEET   the posed build, outside jumps: the lowest ankle's vertical range 30.75 units = 0.0635 leg lengths (rig leg r 484.8, l 484.2 units) over 60 frames
  FEET   the supporting ankle over each support span: worst vertical range 0.00 units = 0.0000 leg lengths (r 0–0), worst horizontal drift 0.00 units = 0.0000 leg lengths (r 0–0)
  FOLD   rigc render --folds at 30 fps: no mesh folds
  wrote run/before/motion.json — animations: idle, run
```

```
$ npx rigc build --rig inputs/rig/rig.json --motion run/before/motion.json --images inputs/rig/images --out run/before/build > run/before/build.txt && npx rigc render --candidate run/before/build --animation run --fps 30 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l --out run/before/render > run/before/render.txt && python3 tools/grade.py --round R2 --geometry run/before/render/run/geometry.json --sequence inputs/pose/sequence.json --report run/before/report.json --build run/before/build.txt --folds run/before/render/run/folds.json --passthrough run/before/render/run/pass-through.json --map run/before/map.json --cycle 20 --trunk chest,head
grade R2
...
PASS  gate            Gate: build green (52 assertions: 21 measured, 0 failed); 11/11 landings within tolerance (worst at 0.14 of its tolerance)
SKIP  support-foot    Support foot: --geometry run/before/render/run/geometry.json is not on disk
...
RESULT INCOMPLETE (1 pass, 0 fail, 13 skip of 14 rows)
```

```
$ python3 tools/grade.py --round R2 --geometry run/before/render/run@30fps/geometry.json --sequence inputs/pose/sequence.json --report run/before/report.json --build run/before/build.txt --folds run/before/render/run@30fps/folds.json --passthrough run/before/render/run@30fps/pass-through.json --map run/before/map.json --cycle 20 --trunk chest,head
grade R2
NOTE  airborne spans: report feet.jumps, 20 span(s)
NOTE  rig leg length 485.0928 units (setup pose, leg_l0->foot_l, leg_r0->foot_r); hip width 84.0000
NOTE  sequence leg length 399.28 (95th percentile hip->ankle, mean of sides, the sequence's own units); the sequence carries no camera
PASS  gate            Gate: build green (52 assertions: 21 measured, 0 failed); 11/11 landings within tolerance (worst at 0.14 of its tolerance)
FAIL  support-foot    Support foot: max |lower foot - floor| 0.0350 leg lengths at frame 12 over 60 grounded frames (floor 110.018 units) [bar <= 0.01]
FAIL  two-feet        Two feet: two-foot frames: none in the sequence; lifted frames (sequence ankles > 0.04 apart): 0 of 60 with the lifted foot within 0.01 of the support foot (lowest lift 0.0274 at frame 80) [bar 0]; median rig/sequence lift 1.436 [bar 0.85-1.15]
SKIP  slide           Slide: no two consecutive grounded frames with sequence ankles
PASS  floor           Floor: per-cycle floor spread 0.0000 leg lengths over 10 cycles [bar <= 0.01, the support-foot band: the table gives this row no number of its own]
PASS  jitter          Jitter: limbs 1.000x sequence (11.040 vs 11.041 deg/f^2, 8 bones) [bar <= 1.1], trunk+head 0.931x sequence (1.581 vs 1.699 deg/f^2, chest,head) [bar <= 1.1]; joint pairs from the map
PASS  folds           Folds: 0 frames fold over 6 mesh(es) [bar 0]
PASS  pass-through    Pass-through: bottomwear:thigh_r 0 of 200 frames; bottomwear:thigh_l 0 of 200 frames [bar 0]
PASS  loop            Loop: cycle 1 vs cycle 10: max keyed-bone angle difference 0.8520 deg (head, cycle frame 4) [bar <= 1.0], max hip/foot_l/foot_r world position difference 0.0000 leg lengths (foot_l, cycle frame 19) [bar <= 0.01]
FAIL  airborne        Airborne: airborne spans per cycle [2, 2, 2, 2, 2, 2, 2, 2, 2, 2] [bar 2 each]; 0 detected span(s) off the printed spans [(4, 9), (14, 19)] +/- 1 [bar 0]; lowest foot on an airborne frame -0.0057 leg lengths above the floor at frame 143 [bar > 0.01: above the support-foot band]
FAIL  hip-vertical    Hip vertical range: rig/sequence 1.466 (rig 0.1398, sequence 0.0954 leg lengths, median per-cycle width over 10 cycles) [bar 0.85-1.15]
FAIL  hip-horizontal  Hip horizontal range: rig/sequence 1.749 (rig 0.5757, sequence 0.3291 hip widths, median per-cycle width over 10 cycles) [bar 0.85-1.15]
FAIL  rebound         Rebound: median rig/sequence peak upward hip acceleration in the stance windows 1.466 over 19 windows [bar 0.7-1.43]
FAIL  hip-tilt        Hip tilt: rig tilt range 0.000 deg = 0.000 of the sequence's 14.390 [bar >= 0.85], sign DISAGREES (covariance +0)
RESULT FAIL (6 pass, 7 fail, 1 skip of 14 rows)
```

```
$ npx rig-pose retarget --rig inputs/rig --map run/after/map.json --pose inputs/pose/sequence.json --out run/after/motion.json --build run/after/build --report run/after/report.json --name run --plant-feet --stance 0.02 --leg-scale 0.5,1.0 > run/after/retarget.txt && npx rigc build --rig inputs/rig/rig.json --motion run/after/motion.json --images inputs/rig/images --out run/after/build > run/after/build.txt && npx rigc render --candidate run/after/build --animation run --fps 30 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l --out run/after/render > run/after/render.txt && python3 tools/grade.py --round R2 --geometry run/after/render/run@30fps/geometry.json --sequence inputs/pose/sequence.json --report run/after/report.json --build run/after/build.txt --folds run/after/render/run@30fps/folds.json --passthrough run/after/render/run@30fps/pass-through.json --map run/after/map.json --cycle 20 --trunk hip,chest,head
grade R2
...
PASS  gate            Gate: build green (52 assertions: 21 measured, 0 failed); 18/18 landings within tolerance (worst at 0.15 of its tolerance)
PASS  support-foot    Support foot: max |lower foot - floor| 0.0000 leg lengths at frame 110 over 60 grounded frames (floor 146.203 units) [bar <= 0.01]
PASS  two-feet        Two feet: two-foot frames: none in the sequence; lifted frames (sequence ankles > 0.04 apart): 0 of 60 with the lifted foot within 0.01 of the support foot (lowest lift 0.3288 at frame 80) [bar 0]; median rig/sequence lift 1.104 [bar 0.85-1.15]
PASS  slide           Slide: max |support-foot move - closure - sequence ankle move x report scale 1.78104| 0.00003 leg lengths/frame (foot_l, frame 10->11) over 40 steps (travel: in-place; closure +1.05979 units/frame removed (report feet.closure drift -210.90 over 200 frames)) [bar <= 0.005]
PASS  floor           Floor: per-cycle floor spread 0.0000 leg lengths over 10 cycles [bar <= 0.01, the support-foot band: the table gives this row no number of its own]
PASS  jitter          Jitter: limbs 1.038x sequence (11.568 vs 11.142 deg/f^2, 8 bones) [bar <= 1.1], trunk+head 1.000x sequence (1.832 vs 1.832 deg/f^2, hip,chest,head) [bar <= 1.1]; joint pairs from the map
FAIL  folds           Folds: 16 frame(s) with a folded triangle, most in slot 'bottomwear' (16 frames) [bar 0]
PASS  pass-through    Pass-through: bottomwear:thigh_r 0 of 200 frames; bottomwear:thigh_l 0 of 200 frames [bar 0]
PASS  loop            Loop: cycle 1 vs cycle 10: max keyed-bone angle difference 0.0082 deg (sleeve_l1, cycle frame 19) [bar <= 1.0], max hip/foot_l/foot_r world position difference 0.0000 leg lengths (foot_r, cycle frame 19) [bar <= 0.01]
PASS  airborne        Airborne: airborne spans per cycle [2, 2, 2, 2, 2, 2, 2, 2, 2, 2] [bar 2 each]; 0 detected span(s) off the printed spans [(4, 9), (14, 19)] +/- 1 [bar 0]; lowest foot on an airborne frame 0.0513 leg lengths above the floor at frame 143 [bar > 0.01: above the support-foot band]
FAIL  hip-vertical    Hip vertical range: rig/sequence 1.460 (rig 0.1393, sequence 0.0954 leg lengths, median per-cycle width over 10 cycles) [bar 0.85-1.15]
FAIL  hip-horizontal  Hip horizontal range: rig/sequence 1.712 (rig 0.5636, sequence 0.3291 hip widths, median per-cycle width over 10 cycles) [bar 0.85-1.15]
FAIL  rebound         Rebound: median rig/sequence peak upward hip acceleration in the stance windows 1.929 over 19 windows [bar 0.7-1.43]
PASS  hip-tilt        Hip tilt: rig tilt range 14.390 deg = 1.000 of the sequence's 14.390 [bar >= 0.85], sign agrees (covariance +3.66e+03)
RESULT FAIL (10 pass, 4 fail, 0 skip of 14 rows)
```

```
$ npx rig-pose retarget --rig inputs/rig --map run/after/map.json --pose inputs/pose/sequence.json --out run/after/motion.json --build run/after/build --report run/after/report.json --name run --plant-feet --stance 0.02 --leg-scale 0.5,1.0 > run/after/retarget.txt && npx rigc build --rig inputs/rig/rig.json --motion run/after/motion.json --images inputs/rig/images --out run/after/build > run/after/build.txt && npx rigc render --candidate run/after/build --animation run --fps 30 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l --out run/after/render > run/after/render.txt && python3 tools/grade.py --round R2 --geometry run/after/render/run@30fps/geometry.json --sequence inputs/pose/sequence.json --report run/after/report.json --build run/after/build.txt --folds run/after/render/run@30fps/folds.json --passthrough run/after/render/run@30fps/pass-through.json --map run/after/map.json --cycle 20 --trunk hip,chest,head
grade R2
NOTE  airborne spans: report feet.jumps, 20 span(s)
NOTE  rig leg length 485.0928 units (setup pose, leg_l0->foot_l, leg_r0->foot_r); hip width 84.0000
NOTE  sequence leg length 399.28 (95th percentile hip->ankle, mean of sides, the sequence's own units); the sequence carries no camera
PASS  gate            Gate: build green (52 assertions: 21 measured, 0 failed); 18/18 landings within tolerance (worst at 0.15 of its tolerance)
PASS  support-foot    Support foot: max |lower foot - floor| 0.0000 leg lengths at frame 110 over 60 grounded frames (floor 122.026 units) [bar <= 0.01]
PASS  two-feet        Two feet: two-foot frames: none in the sequence; lifted frames (sequence ankles > 0.04 apart): 0 of 60 with the lifted foot within 0.01 of the support foot (lowest lift 0.3288 at frame 80) [bar 0]; median rig/sequence lift 1.116 [bar 0.85-1.15]
PASS  slide           Slide: max |support-foot move - closure - sequence ankle move x report scale 1.07585| 0.00003 leg lengths/frame (foot_l, frame 171->172) over 40 steps (travel: in-place; closure -0.08227 units/frame removed (report feet.closure drift 16.37 over 200 frames)) [bar <= 0.005]
PASS  floor           Floor: per-cycle floor spread 0.0000 leg lengths over 10 cycles [bar <= 0.01, the support-foot band: the table gives this row no number of its own]
PASS  jitter          Jitter: limbs 1.038x sequence (11.567 vs 11.142 deg/f^2, 8 bones) [bar <= 1.1], trunk+head 1.000x sequence (1.832 vs 1.832 deg/f^2, hip,chest,head) [bar <= 1.1]; joint pairs from the map
PASS  folds           Folds: 0 frames fold over 6 mesh(es) [bar 0]
PASS  pass-through    Pass-through: bottomwear:thigh_r 0 of 200 frames; bottomwear:thigh_l 0 of 200 frames [bar 0]
PASS  loop            Loop: cycle 1 vs cycle 10: max keyed-bone angle difference 0.0082 deg (sleeve_l1, cycle frame 19) [bar <= 1.0], max hip/foot_l/foot_r world position difference 0.0000 leg lengths (foot_l, cycle frame 19) [bar <= 0.01]
PASS  airborne        Airborne: airborne spans per cycle [2, 2, 2, 2, 2, 2, 2, 2, 2, 2] [bar 2 each]; 0 detected span(s) off the printed spans [(4, 9), (14, 19)] +/- 1 [bar 0]; lowest foot on an airborne frame 0.0456 leg lengths above the floor at frame 139 [bar > 0.01: above the support-foot band]
PASS  hip-vertical    Hip vertical range: rig/sequence 0.928 (rig 0.0885, sequence 0.0954 leg lengths, median per-cycle width over 10 cycles) [bar 0.85-1.15]
PASS  hip-horizontal  Hip horizontal range: rig/sequence 1.059 (rig 0.3485, sequence 0.3291 hip widths, median per-cycle width over 10 cycles) [bar 0.85-1.15]
PASS  rebound         Rebound: median rig/sequence peak upward hip acceleration in the stance windows 1.257 over 19 windows [bar 0.7-1.43]
PASS  hip-tilt        Hip tilt: rig tilt range 14.390 deg = 1.000 of the sequence's 14.390 [bar >= 0.85], sign agrees (covariance +3.66e+03)
RESULT PASS (14 pass, 0 fail, 0 skip of 14 rows)
```

```
$ mkdir -p run/after/rig && cp inputs/rig/motion.json run/after/rig/motion.json && ln -sfn ../../../inputs/rig/images run/after/rig/images && python3 -c '...' && npx rig-pose retarget --rig run/after/rig --map run/after/map.json --pose inputs/pose/sequence.json --out run/after/motion.json --build run/after/build --report run/after/report.json --name run --plant-feet --stance 0.02 --leg-scale 0.5,1.0 > run/after/retarget.txt && npx rigc build --rig run/after/rig/rig.json --motion run/after/motion.json --images inputs/rig/images --out run/after/build > run/after/build.txt && npx rigc render --candidate run/after/build --animation run --fps 30 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l --out run/after/render > run/after/render.txt && python3 tools/grade.py --round R2 --geometry run/after/render/run@30fps/geometry.json --sequence inputs/pose/sequence.json --report run/after/report.json --build run/after/build.txt --folds run/after/render/run@30fps/folds.json --passthrough run/after/render/run@30fps/pass-through.json --map run/after/map.json --cycle 20 --trunk hip,chest,head
grade R2
NOTE  airborne spans: report feet.jumps, 20 span(s)
NOTE  rig leg length 485.0928 units (setup pose, leg_l0->foot_l, leg_r0->foot_r); hip width 84.0000
NOTE  sequence leg length 399.28 (95th percentile hip->ankle, mean of sides, the sequence's own units); the sequence carries no camera
PASS  gate            Gate: build green (52 assertions: 21 measured, 0 failed); 18/18 landings within tolerance (worst at 0.15 of its tolerance)
PASS  support-foot    Support foot: max |lower foot - floor| 0.0000 leg lengths at frame 110 over 60 grounded frames (floor 122.026 units) [bar <= 0.01]
PASS  two-feet        Two feet: two-foot frames: none in the sequence; lifted frames (sequence ankles > 0.04 apart): 0 of 60 with the lifted foot within 0.01 of the support foot (lowest lift 0.3288 at frame 80) [bar 0]; median rig/sequence lift 1.116 [bar 0.85-1.15]
PASS  slide           Slide: max |support-foot move - closure - sequence ankle move x report scale 1.07585| 0.00003 leg lengths/frame (foot_l, frame 171->172) over 40 steps (travel: in-place; closure -0.08227 units/frame removed (report feet.closure drift 16.37 over 200 frames)) [bar <= 0.005]
PASS  floor           Floor: per-cycle floor spread 0.0000 leg lengths over 10 cycles [bar <= 0.01, the support-foot band: the table gives this row no number of its own]
PASS  jitter          Jitter: limbs 1.038x sequence (11.567 vs 11.142 deg/f^2, 8 bones) [bar <= 1.1], trunk+head 1.000x sequence (1.832 vs 1.832 deg/f^2, hip,chest,head) [bar <= 1.1]; joint pairs from the map
PASS  folds           Folds: 0 frames fold over 6 mesh(es) [bar 0]
PASS  pass-through    Pass-through: bottomwear:thigh_r 0 of 200 frames; bottomwear:thigh_l 0 of 200 frames [bar 0]
PASS  loop            Loop: cycle 1 vs cycle 10: max keyed-bone angle difference 0.0082 deg (sleeve_l1, cycle frame 19) [bar <= 1.0], max hip/foot_l/foot_r world position difference 0.0000 leg lengths (foot_l, cycle frame 19) [bar <= 0.01]
PASS  airborne        Airborne: airborne spans per cycle [2, 2, 2, 2, 2, 2, 2, 2, 2, 2] [bar 2 each]; 0 detected span(s) off the printed spans [(4, 9), (14, 19)] +/- 1 [bar 0]; lowest foot on an airborne frame 0.0456 leg lengths above the floor at frame 139 [bar > 0.01: above the support-foot band]
PASS  hip-vertical    Hip vertical range: rig/sequence 0.928 (rig 0.0885, sequence 0.0954 leg lengths, median per-cycle width over 10 cycles) [bar 0.85-1.15]
PASS  hip-horizontal  Hip horizontal range: rig/sequence 1.059 (rig 0.3485, sequence 0.3291 hip widths, median per-cycle width over 10 cycles) [bar 0.85-1.15]
PASS  rebound         Rebound: median rig/sequence peak upward hip acceleration in the stance windows 1.257 over 19 windows [bar 0.7-1.43]
PASS  hip-tilt        Hip tilt: rig tilt range 14.390 deg = 1.000 of the sequence's 14.390 [bar >= 0.85], sign agrees (covariance +3.66e+03)
RESULT PASS (14 pass, 0 fail, 0 skip of 14 rows)
```

```
$ mkdir -p run/evidence && python3 -c '...'
wrote run/evidence/f0001_side_by_side.png (561, 280)
wrote run/evidence/f0006_side_by_side.png (561, 280)
wrote run/evidence/f0011_side_by_side.png (561, 280)
wrote run/evidence/f0016_side_by_side.png (561, 280)
wrote run/evidence/f0143_side_by_side.png (561, 280)
```

```
$ python3 tools/grade.py --round R2 --geometry run/after/render/run@30fps/geometry.json --sequence inputs/pose/sequence.json --report run/after/report.json --build run/after/build.txt --folds run/after/render/run@30fps/folds.json --passthrough run/after/render/run@30fps/pass-through.json --map run/after/map.json --cycle 20 --trunk hip,chest,head
grade R2
NOTE  airborne spans: report feet.jumps, 20 span(s)
NOTE  rig leg length 485.0928 units (setup pose, leg_l0->foot_l, leg_r0->foot_r); hip width 84.0000
NOTE  sequence leg length 399.28 (95th percentile hip->ankle, mean of sides, the sequence's own units); the sequence carries no camera
PASS  gate            Gate: build green (52 assertions: 21 measured, 0 failed); 18/18 landings within tolerance (worst at 0.15 of its tolerance)
PASS  support-foot    Support foot: max |lower foot - floor| 0.0000 leg lengths at frame 110 over 60 grounded frames (floor 122.026 units) [bar <= 0.01]
PASS  two-feet        Two feet: two-foot frames: none in the sequence; lifted frames (sequence ankles > 0.04 apart): 0 of 60 with the lifted foot within 0.01 of the support foot (lowest lift 0.3288 at frame 80) [bar 0]; median rig/sequence lift 1.116 [bar 0.85-1.15]
PASS  slide           Slide: max |support-foot move - closure - sequence ankle move x report scale 1.07585| 0.00003 leg lengths/frame (foot_l, frame 171->172) over 40 steps (travel: in-place; closure -0.08227 units/frame removed (report feet.closure drift 16.37 over 200 frames)) [bar <= 0.005]
PASS  floor           Floor: per-cycle floor spread 0.0000 leg lengths over 10 cycles [bar <= 0.01, the support-foot band: the table gives this row no number of its own]
PASS  jitter          Jitter: limbs 1.038x sequence (11.567 vs 11.142 deg/f^2, 8 bones) [bar <= 1.1], trunk+head 1.000x sequence (1.832 vs 1.832 deg/f^2, hip,chest,head) [bar <= 1.1]; joint pairs from the map
PASS  folds           Folds: 0 frames fold over 6 mesh(es) [bar 0]
PASS  pass-through    Pass-through: bottomwear:thigh_r 0 of 200 frames; bottomwear:thigh_l 0 of 200 frames [bar 0]
PASS  loop            Loop: cycle 1 vs cycle 10: max keyed-bone angle difference 0.0082 deg (sleeve_l1, cycle frame 19) [bar <= 1.0], max hip/foot_l/foot_r world position difference 0.0000 leg lengths (foot_l, cycle frame 19) [bar <= 0.01]
PASS  airborne        Airborne: airborne spans per cycle [2, 2, 2, 2, 2, 2, 2, 2, 2, 2] [bar 2 each]; 0 detected span(s) off the printed spans [(4, 9), (14, 19)] +/- 1 [bar 0]; lowest foot on an airborne frame 0.0456 leg lengths above the floor at frame 139 [bar > 0.01: above the support-foot band]
PASS  hip-vertical    Hip vertical range: rig/sequence 0.928 (rig 0.0885, sequence 0.0954 leg lengths, median per-cycle width over 10 cycles) [bar 0.85-1.15]
PASS  hip-horizontal  Hip horizontal range: rig/sequence 1.059 (rig 0.3485, sequence 0.3291 hip widths, median per-cycle width over 10 cycles) [bar 0.85-1.15]
PASS  rebound         Rebound: median rig/sequence peak upward hip acceleration in the stance windows 1.257 over 19 windows [bar 0.7-1.43]
PASS  hip-tilt        Hip tilt: rig tilt range 14.390 deg = 1.000 of the sequence's 14.390 [bar >= 0.85], sign agrees (covariance +3.66e+03)
RESULT PASS (14 pass, 0 fail, 0 skip of 14 rows)
```

finished: 2026-10-18T23:55:55Z
