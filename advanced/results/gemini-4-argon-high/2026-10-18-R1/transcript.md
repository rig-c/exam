started: 2026-10-18T23:35:36Z

```
$ npm install
added 6 packages, and audited 7 packages in 3s

1 package is looking for funding
  run `npm fund` for details

found 0 vulnerabilities
```

```
$ mkdir -p run/before && npx rig-pose retarget --sequence inputs/pose/sequence.json --rig inputs/rig/rig.json --map run/map.json --animation walk --out run/before/motion.json --report run/before/report.json
rig-pose retarget: unknown flag --sequence; the flags are --rig, --map, --pose, --out, --name, --person, --base-motion, --images, --min-score, --smooth, --flip, --short, --bends, --bend-tolerance, --switch-tolerance, --switch-min, --switch-at, --profile, --build, --render, --report, --camera, --leg-scale, --idle, --merge, --reduce, --reduce-hip, --stance, --floor, --coco, --plant-feet, --carry-idle, --raised-by-head (rig-pose --help)
```

```
$ npx rig-pose retarget --rig inputs/rig/rig.json --map run/map.json --pose inputs/pose/sequence.json --base-motion inputs/rig/motion.json --name walk --out run/before/motion.json --report run/before/report.json
FAIL  MAP_TRANSLATE_SCALE: run/map.json "translate" "scale" is undefined; it must be { pose: [joint, joint], rig: [bone, bone] }, the same length measured in each
rig-pose retarget: 1 problem(s) — nothing written
```

```
$ npx rig-pose retarget --rig inputs/rig/rig.json --map run/map.json --pose inputs/pose/sequence.json --base-motion inputs/rig/motion.json --name walk --out run/before/motion.json --report run/before/report.json
rig-pose retarget: 224 frame(s), 7.433s, onto "wind_painting" as "walk" — 12 track(s); min-score 0.3, flip off, short off, bends refuse (tolerance 0°)
  ...
  GATE   rigc build --profile spine: green — 52 assertions: 21 measured (21 passed, 0 failed), 17 skipped, 14 not in profile "spine"
  LAND   bone "chest" aim — worst |reached − asked| 0.000495° at frame 204 (t=6.800s); the tolerance is 0.01°
  LAND   bone "head" aim — worst |reached − asked| 0.000985° at frame 12 (t=0.400s); the tolerance is 0.01°
  LAND   bone "sleeve_r0" aim — worst |reached − asked| 0.000885° at frame 157 (t=5.233s); the tolerance is 0.01°
  LAND   bone "sleeve_r1" aim — worst |reached − asked| 0.00100° at frame 87 (t=2.900s); the tolerance is 0.01°
  LAND   bone "sleeve_l0" aim — worst |reached − asked| 0.000881° at frame 102 (t=3.400s); the tolerance is 0.01°
  LAND   bone "sleeve_l1" aim — worst |reached − asked| 0.00123° at frame 200 (t=6.667s); the tolerance is 0.01°
  LAND   bone "leg_r0" aim — worst |reached − asked| 0.000481° at frame 158 (t=5.267s); the tolerance is 0.01°
  LAND   bone "leg_r1" aim — worst |reached − asked| 0.000931° at frame 117 (t=3.900s); the tolerance is 0.01°
  LAND   bone "leg_l0" aim — worst |reached − asked| 0.000497° at frame 49 (t=1.633s); the tolerance is 0.01°
  LAND   bone "leg_l1" aim — worst |reached − asked| 0.000854° at frame 1 (t=0.033s); the tolerance is 0.01°
  LAND   bone "hip" origin — worst |reached − asked| 0.000687 units at frame 187 (t=6.233s); the tolerance is 0.01 units
  FEET   the posed build, outside jumps: the lowest ankle's vertical range 47.76 units = 0.0985 leg lengths (rig leg r 485.0, l 484.9 units) over 224 frames
  FEET   the supporting ankle over each support span: worst vertical range 49.04 units = 0.1011 leg lengths (l 0–14), worst horizontal drift 88.67 units = 0.1828 leg lengths (l 129–146)
  FOLD   rigc render --folds at 30 fps: no mesh folds
  wrote run/before/motion.json — animations: idle, walk
```

```
$ npx rigc build --rig inputs/rig/rig.json --motion run/before/motion.json --images inputs/rig/images --out run/before/build | tee run/before/build.txt
  ...
  ..    52 assertions: 21 measured (21 passed, 0 failed), 17 skipped, 14 not in profile "spine"
  ..    pages=28 regions=28 bones=81 slots=28 animations=2 version=4.3.13 regionAttachments=22 meshAttachments=6 physicsConstraints=44 physicsTimelineKeys=0 rig=wind_painting profile=spine
  ..    here: 42 rule(s) on the model side over the document, 9 of the round trip's own restated over the emitted text; not run: A00_ROUNDTRIP_PARSE — spine-core's parse, which only the entry that links spine-core runs, on build and validate: installed, the same `rigc` once @esotericsoftware/spine-core is installed beside the package; from a source checkout, `bun cli.ts`
rigc: wrote run/before/build/skeleton.json
rigc: wrote run/before/build/skeleton.atlas
rigc: wrote run/before/build/skeleton.model.json
rigc: look at it: rigc render --candidate run/before/build
```

```
$ npx rigc render --candidate run/before/build --animation walk --fps 30 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l --out run/before/render
rigc render
  ..    skeleton run/before/build/skeleton.json
  ..    atlas    run/before/build/skeleton.atlas
  ..    poser    rigc core — run/before/build/skeleton.model.json
  ..    157x256px at 30 fps, 1 set(s) -> run/before/render
  ..    walk             224 frame(s), 7.433s + contact.png + geometry.json + folds.json (0 of 6 mesh(es) fold) + pass-through.json (0 of 2 pair(s) pass through) -> run/before/render/walk@30fps
  ..    pass     "walk": cloth "bottomwear" over leg "thigh_r" passes through on 0 of 224 frame(s) read at 30 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0000) on its left side
  ..    pass     "walk": cloth "bottomwear" over leg "thigh_l" passes through on 0 of 224 frame(s) read at 30 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0000) on its left side
rigc: wrote run/before/render/frames.json
```

```
$ python3 tools/grade.py --round R1 --geometry run/before/render/walk@30fps/geometry.json --sequence inputs/pose/sequence.json --report run/before/report.json --build run/before/build.txt --cycle 32 --folds run/before/render/walk@30fps/folds.json --passthrough run/before/render/walk@30fps/pass-through.json --map run/map.json --feet foot_l,foot_r --hip hip --trunk chest,head | tee run/before/grade.txt
grade R1
NOTE  airborne spans: report feet.jumps, 0 span(s)
NOTE  rig leg length 485.0928 units (setup pose, leg_l0->foot_l, leg_r0->foot_r); hip width 84.0000
NOTE  sequence leg length 426.70 (95th percentile hip->ankle, mean of sides, the sequence's own units); the sequence carries no camera
PASS  gate            Gate: build green (52 assertions: 21 measured, 0 failed); 11/11 landings within tolerance (worst at 0.12 of its tolerance)
FAIL  support-foot    Support foot: max |lower foot - floor| 0.0608 leg lengths at frame 183 over 224 grounded frames (floor 137.135 units) [bar <= 0.01]
FAIL  two-feet        Two feet: two-foot frames: max height difference 0.0074 leg lengths at frame 203 over 35 [bar <= 0.02]; lifted frames (sequence ankles > 0.04 apart): 168 of 168 with the lifted foot within 0.01 of the support foot (lowest lift -0.0097 at frame 42) [bar 0]; median rig/sequence lift -0.010 [bar 0.85-1.15]
FAIL  slide           Slide: max |support-foot move - closure - sequence ankle move x report scale 1.77071| 0.01176 leg lengths/frame (foot_l, frame 1->2) over 152 steps (travel: in-place; feet.closure absent from the report: closure drift taken as 0) [bar <= 0.005]
PASS  floor           Floor: per-cycle floor spread 0.0000 leg lengths over 7 cycles [bar <= 0.01, the support-foot band: the table gives this row no number of its own]
FAIL  jitter          Jitter: limbs 1.000x sequence (0.941 vs 0.941 deg/f^2, 8 bones) [bar <= 1.1], trunk+head 1.277x sequence (0.918 vs 0.719 deg/f^2, chest,head) [bar <= 1.1]; joint pairs from the map
PASS  folds           Folds: 0 frames fold over 6 mesh(es) [bar 0]
PASS  pass-through    Pass-through: bottomwear:thigh_r 0 of 224 frames; bottomwear:thigh_l 0 of 224 frames [bar 0]
FAIL  loop            Loop: cycle 1 vs cycle 7: max keyed-bone angle difference 1.3809 deg (head, cycle frame 13) [bar <= 1.0], max hip/foot_l/foot_r world position difference 0.0000 leg lengths (hip, cycle frame 31) [bar <= 0.01]
RESULT FAIL (4 pass, 5 fail, 0 skip of 9 rows)
```

```
$ mkdir -p run/evidence && python3 -c '... subprocess.run(["ffmpeg", "-y", "-i", "inputs/pose/stick.mp4", "-vsync", "0", "run/evidence/stick_frames/f%04d.png"], check=True) ...'
subprocess.CalledProcessError: Command '['ffmpeg', '-y', '-i', 'inputs/pose/stick.mp4', '-vsync', '0', 'run/evidence/stick_frames/f%04d.png']' returned non-zero exit status 8.
```

```
$ python3 -c '... subprocess.run(["ffmpeg", "-y", "-i", "inputs/pose/stick.mp4", "run/evidence/stick_frames/f%04d.png"], check=True) ...' && rm -rf run/evidence/stick_frames
wrote run/evidence/before_f0000.png (385, 256)
wrote run/evidence/before_f0006.png (385, 256)
wrote run/evidence/before_f0018.png (385, 256)
wrote run/evidence/before_f0042.png (385, 256)
wrote run/evidence/before_f0183.png (385, 256)
wrote run/evidence/before_f0203.png (385, 256)
```

```
$ mkdir -p run/after && npx rig-pose retarget --rig inputs/rig/rig.json --map run/map.json --pose inputs/pose/sequence.json --base-motion inputs/rig/motion.json --name walk --plant-feet --stance 0.03 --leg-scale 0.6,1.05 --out run/after/motion.json --report run/after/report.json
  ...
  GATE   rigc build --profile spine: green — 52 assertions: 21 measured (21 passed, 0 failed), 17 skipped, 14 not in profile "spine"
  ...
  LAND   bone "leg_r1:tip" ankle — worst |reached − asked| 0.00503 units at frame 87 (t=2.900s); the tolerance is 0.0591 units
  LAND   bone "leg_l1:tip" ankle — worst |reached − asked| 0.00463 units at frame 199 (t=6.633s); the tolerance is 0.0591 units
  FEET   the posed build, outside jumps: the lowest ankle's vertical range 0.00 units = 0.0000 leg lengths (rig leg r 430.4, l 440.5 units) over 224 frames
  FEET   the supporting ankle over each support span: worst vertical range 0.00 units = 0.0000 leg lengths (l 92–107), worst horizontal drift 73.13 units = 0.1660 leg lengths (l 28–43)
  ...
  FOLD   rigc render --folds at 30 fps: no mesh folds
  wrote run/after/motion.json — animations: idle, walk
```

```
$ npx rig-pose retarget --rig inputs/rig/rig.json --map run/after/map.json --pose inputs/pose/sequence.json --base-motion inputs/rig/motion.json --name walk --plant-feet --stance 0.03 --leg-scale 0.45,1.05 --out run/after/motion.json --report run/after/report.json
  ...
  GATE   rigc build --profile spine: green — 52 assertions: 21 measured (21 passed, 0 failed), 17 skipped, 14 not in profile "spine"
  ...
  LAND   bone "leg_r1:tip" ankle — worst |reached − asked| 0.00503 units at frame 87 (t=2.900s); the tolerance is 0.0591 units
  LAND   bone "leg_l1:tip" ankle — worst |reached − asked| 0.00463 units at frame 199 (t=6.633s); the tolerance is 0.0591 units
  FEET   the posed build, outside jumps: the lowest ankle's vertical range 0.00 units = 0.0000 leg lengths (rig leg r 430.4, l 440.5 units) over 224 frames
  FEET   the supporting ankle over each support span: worst vertical range 0.00 units = 0.0000 leg lengths (l 92–107), worst horizontal drift 73.13 units = 0.1660 leg lengths (l 28–43)
  ...
  FOLD   rigc render --folds at 30 fps: no mesh folds
  wrote run/after/motion.json — animations: idle, walk
```

```
$ npx rigc build --rig inputs/rig/rig.json --motion run/after/motion.json --images inputs/rig/images --out run/after/build | tee run/after/build.txt
  ...
  ..    52 assertions: 21 measured (21 passed, 0 failed), 17 skipped, 14 not in profile "spine"
  ..    pages=28 regions=28 bones=81 slots=28 animations=2 version=4.3.13 regionAttachments=22 meshAttachments=6 physicsConstraints=44 physicsTimelineKeys=0 rig=wind_painting profile=spine
  ..    here: 42 rule(s) on the model side over the document, 9 of the round trip's own restated over the emitted text; not run: A00_ROUNDTRIP_PARSE — spine-core's parse, which only the entry that links spine-core runs, on build and validate: installed, the same `rigc` once @esotericsoftware/spine-core is installed beside the package; from a source checkout, `bun cli.ts`
rigc: wrote run/after/build/skeleton.json
rigc: wrote run/after/build/skeleton.atlas
rigc: wrote run/after/build/skeleton.model.json
rigc: look at it: rigc render --candidate run/after/build
```

```
$ npx rigc render --candidate run/after/build --animation walk --fps 30 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l --out run/after/render
rigc render
  ..    skeleton run/after/build/skeleton.json
  ..    atlas    run/after/build/skeleton.atlas
  ..    poser    rigc core — run/after/build/skeleton.model.json
  ..    159x256px at 30 fps, 1 set(s) -> run/after/render
  ..    walk             224 frame(s), 7.433s + contact.png + geometry.json + folds.json (0 of 6 mesh(es) fold) + pass-through.json (0 of 2 pair(s) pass through) -> run/after/render/walk@30fps
  ..    pass     "walk": cloth "bottomwear" over leg "thigh_r" passes through on 0 of 224 frame(s) read at 30 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0000) on its left side
  ..    pass     "walk": cloth "bottomwear" over leg "thigh_l" passes through on 0 of 224 frame(s) read at 30 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0000) on its left side
rigc: wrote run/after/render/frames.json
```

```
$ python3 tools/grade.py --round R1 --geometry run/after/render/walk@30fps/geometry.json --sequence inputs/pose/sequence.json --report run/after/report.json --build run/after/build.txt --cycle 32 --folds run/after/render/walk@30fps/folds.json --passthrough run/after/render/walk@30fps/pass-through.json --map run/after/map.json --feet foot_l,foot_r --hip hip --trunk chest,head | tee run/after/grade.txt
grade R1
NOTE  airborne spans: report feet.jumps, 0 span(s)
NOTE  rig leg length 485.0928 units (setup pose, leg_l0->foot_l, leg_r0->foot_r); hip width 84.0000
NOTE  sequence leg length 426.70 (95th percentile hip->ankle, mean of sides, the sequence's own units); the sequence carries no camera
PASS  gate            Gate: build green (52 assertions: 21 measured, 0 failed); 17/17 landings within tolerance (worst at 0.12 of its tolerance)
PASS  support-foot    Support foot: max |lower foot - floor| 0.0000 leg lengths at frame 104 over 224 grounded frames (floor 94.868 units) [bar <= 0.01]
PASS  two-feet        Two feet: two-foot frames: max height difference 0.0000 leg lengths at frame 203 over 35 [bar <= 0.02]; lifted frames (sequence ankles > 0.04 apart): 0 of 168 with the lifted foot within 0.01 of the support foot (lowest lift 0.0176 at frame 173) [bar 0]; median rig/sequence lift 0.913 [bar 0.85-1.15]
PASS  slide           Slide: max |support-foot move - closure - sequence ankle move x report scale 1.77071| 0.00002 leg lengths/frame (foot_l, frame 7->8) over 209 steps (travel: in-place; closure +1.01080 units/frame removed (report feet.closure drift -225.41 over 224 frames)) [bar <= 0.005]
PASS  floor           Floor: per-cycle floor spread 0.0000 leg lengths over 7 cycles [bar <= 0.01, the support-foot band: the table gives this row no number of its own]
PASS  jitter          Jitter: limbs 0.988x sequence (0.929 vs 0.941 deg/f^2, 8 bones) [bar <= 1.1], trunk+head 1.000x sequence (0.614 vs 0.614 deg/f^2, chest,head) [bar <= 1.1]; joint pairs from the map
PASS  folds           Folds: 0 frames fold over 6 mesh(es) [bar 0]
PASS  pass-through    Pass-through: bottomwear:thigh_r 0 of 224 frames; bottomwear:thigh_l 0 of 224 frames [bar 0]
PASS  loop            Loop: cycle 1 vs cycle 7: max keyed-bone angle difference 0.0001 deg (sleeve_r1, cycle frame 31) [bar <= 1.0], max hip/foot_l/foot_r world position difference 0.0000 leg lengths (foot_r, cycle frame 31) [bar <= 0.01]
RESULT PASS (9 pass, 0 fail, 0 skip of 9 rows)
```

```
$ python3 -c '... write after_fXXXX.png and compare_fXXXX.png ...' && rm -rf run/evidence/stick_frames && python3 tools/grade.py --round R1 --geometry run/after/render/walk@30fps/geometry.json --sequence inputs/pose/sequence.json --report run/after/report.json --build run/after/build.txt --cycle 32 --folds run/after/render/walk@30fps/folds.json --passthrough run/after/render/walk@30fps/pass-through.json --map run/after/map.json --feet foot_l,foot_r --hip hip --trunk chest,head | tee run/after/grade.txt && date -u +%Y-%m-%dT%H:%M:%SZ
wrote run/evidence/after_f0000.png (387, 256) and run/evidence/compare_f0000.png (544, 256)
wrote run/evidence/after_f0006.png (387, 256) and run/evidence/compare_f0006.png (544, 256)
wrote run/evidence/after_f0018.png (387, 256) and run/evidence/compare_f0018.png (544, 256)
wrote run/evidence/after_f0042.png (387, 256) and run/evidence/compare_f0042.png (544, 256)
wrote run/evidence/after_f0183.png (387, 256) and run/evidence/compare_f0183.png (544, 256)
wrote run/evidence/after_f0203.png (387, 256) and run/evidence/compare_f0203.png (544, 256)
grade R1
NOTE  airborne spans: report feet.jumps, 0 span(s)
NOTE  rig leg length 485.0928 units (setup pose, leg_l0->foot_l, leg_r0->foot_r); hip width 84.0000
NOTE  sequence leg length 426.70 (95th percentile hip->ankle, mean of sides, the sequence's own units); the sequence carries no camera
PASS  gate            Gate: build green (52 assertions: 21 measured, 0 failed); 17/17 landings within tolerance (worst at 0.12 of its tolerance)
PASS  support-foot    Support foot: max |lower foot - floor| 0.0000 leg lengths at frame 104 over 224 grounded frames (floor 94.868 units) [bar <= 0.01]
PASS  two-feet        Two feet: two-foot frames: max height difference 0.0000 leg lengths at frame 203 over 35 [bar <= 0.02]; lifted frames (sequence ankles > 0.04 apart): 0 of 168 with the lifted foot within 0.01 of the support foot (lowest lift 0.0176 at frame 173) [bar 0]; median rig/sequence lift 0.913 [bar 0.85-1.15]
PASS  slide           Slide: max |support-foot move - closure - sequence ankle move x report scale 1.77071| 0.00002 leg lengths/frame (foot_l, frame 7->8) over 209 steps (travel: in-place; closure +1.01080 units/frame removed (report feet.closure drift -225.41 over 224 frames)) [bar <= 0.005]
PASS  floor           Floor: per-cycle floor spread 0.0000 leg lengths over 7 cycles [bar <= 0.01, the support-foot band: the table gives this row no number of its own]
PASS  jitter          Jitter: limbs 0.988x sequence (0.929 vs 0.941 deg/f^2, 8 bones) [bar <= 1.1], trunk+head 1.000x sequence (0.614 vs 0.614 deg/f^2, chest,head) [bar <= 1.1]; joint pairs from the map
PASS  folds           Folds: 0 frames fold over 6 mesh(es) [bar 0]
PASS  pass-through    Pass-through: bottomwear:thigh_r 0 of 224 frames; bottomwear:thigh_l 0 of 224 frames [bar 0]
PASS  loop            Loop: cycle 1 vs cycle 7: max keyed-bone angle difference 0.0001 deg (sleeve_r1, cycle frame 31) [bar <= 1.0], max hip/foot_l/foot_r world position difference 0.0000 leg lengths (foot_r, cycle frame 31) [bar <= 0.01]
RESULT PASS (9 pass, 0 fail, 0 skip of 9 rows)
```

finished: 2026-10-18T23:52:26Z
