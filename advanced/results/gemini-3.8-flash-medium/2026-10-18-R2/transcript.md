started: 2026-10-18T23:18:07Z

```bash
$ npm install
added 6 packages, and audited 7 packages in 3s

1 package is looking for funding
  run `npm fund` for details

found 0 vulnerabilities
```

```bash
$ npx rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --out run/motion.json --name run --build run/build --render run/render --report run/report.json
  POSTURE hip tilt range (chain "pelvis", r_hip → l_hip, Spine degrees): reference 14.4° (−7.4° … +7.0°), rig 14.4° (−7.4° … +7.0°) — rig/reference 1.000
  POSTURE sway, x-range of mid_hip − mid_shoulder: reference 36.7 units = picture px × scale (0.146 shoulder widths), rig 34.7 units (0.228 shoulder widths; mid_hip = "hip", mid_shoulder = "sleeve_r0+sleeve_l0") — rig/reference 0.945 in units, 1.564 in shoulder widths
  FEET   the posed build, outside jumps: the lowest ankle's vertical range 31.83 units = 0.0657 leg lengths (rig leg r 484.8, l 484.2 units) over 60 frames
  FEET   the supporting ankle over each support span: worst vertical range 0.00 units = 0.0000 leg lengths (r 0–0), worst horizontal drift 0.00 units = 0.0000 leg lengths (r 0–0)
  FOLD   mesh "bottomwear" (slot "bottomwear") folds on 26 frame(s) at 30 fps: t=1.033–1.067, 1.400, 1.700–1.733, 2.067, 2.367–2.400, 2.733, 3.033–3.067, 3.400, 3.700–3.733, 4.067, 4.367–4.400, 4.733, 5.033–5.067, 5.400, 5.700–5.733, 6.067, 6.367–6.400
  wrote run/motion.json — animations: idle, run
```

```bash
$ npx rigc build --rig inputs/rig/rig.json --motion run/motion.json --out run/build > run/build.stdout 2>&1
  ..    52 assertions: 21 measured (21 passed, 0 failed), 17 skipped, 14 not in profile "spine"
  ..    pages=28 regions=28 bones=81 slots=28 animations=2 version=4.3.13 regionAttachments=22 meshAttachments=6 physicsConstraints=44 physicsTimelineKeys=0 rig=wind_painting profile=spine
  ..    here: 42 rule(s) on the model side over the document, 9 of the round trip's own restated over the emitted text; not run: A00_ROUNDTRIP_PARSE — spine-core's parse, which only the entry that links spine-core runs, on build and validate: installed, the same `rigc` once @esotericsoftware/spine-core is installed beside the package; from a source checkout, `bun cli.ts`
rigc: wrote run/build/skeleton.json
rigc: wrote run/build/skeleton.atlas
rigc: wrote run/build/skeleton.model.json
rigc: look at it: rigc render --candidate run/build
```

```bash
$ npx rigc render --candidate run/build --animation run --fps 30 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l --out run/render/ > run/render/render.stdout 2>&1
  ..    run              200 frame(s), 6.633s + contact.png + geometry.json + folds.json (1 of 6 mesh(es) fold) + pass-through.json (0 of 2 pair(s) pass through) -> run/render/run@30fps
  ..    folds    "run": mesh "bottomwear" (slot "bottomwear") folds on 26 frame(s) [31-32, 42, 51-52, 62, 71-72, 82, 91-92, 102, 111-112, 122, 131-132, 142, 151-152, 162, 171-172, 182, 191-192] at 30 fps; worst frame 31 (t=1.0333s): 2 of 204 triangle(s) [188, 189] in world box x [-5.91, 28.04] y [411.97, 455.24] (33.94 × 43.25), setup-pose area 961.00 units² = 0.992% of the mesh's; 3 triangle(s) fold on some frame [110, 188, 189]
  ..    pass     "run": cloth "bottomwear" over leg "thigh_r" passes through on 0 of 200 frame(s) read at 30 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0000) on its left side
  ..    pass     "run": cloth "bottomwear" over leg "thigh_l" passes through on 0 of 200 frame(s) read at 30 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0000) on its left side
rigc: wrote run/render/frames.json
```

```bash
$ npx rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --out run/motion.json --name run --build run/build --render run/render --report run/report.json --plant-feet --leg-scale 0.8,1.05 --stance 0.07
  POSTURE bounce r 180–182 (detrended y sd, rig/reference): hip 0.972 (6.6/6.8u, r=0.999), neck 0.880 (6.6/7.5u, r=0.875), eyes − neck 4.159 (3.3/0.8u, r=0.990)
  POSTURE bounce l 190–192 (detrended y sd, rig/reference): hip 0.934 (14.0/15.0u, r=0.961), neck 1.200 (13.6/11.3u, r=0.858), eyes − neck 3.453 (2.3/0.7u, r=0.983)
  FEET   the posed build, outside jumps: the lowest ankle's vertical range 0.00 units = 0.0000 leg lengths (rig leg r 388.1, l 392.0 units) over 60 frames
  FEET   the supporting ankle over each support span: worst vertical range 0.00 units = 0.0000 leg lengths (r 140–142), worst horizontal drift 34.41 units = 0.0878 leg lengths (l 110–112)
  FOLD   mesh "bottomwear" (slot "bottomwear") folds on 16 frame(s) at 30 fps: t=1.400, 1.733, 2.067, 2.400, 2.733, 3.067, 3.400, 3.733, 4.067, 4.400, 4.733, 5.067, 5.400, 5.733, 6.067, 6.400
  wrote run/motion.json — animations: idle, run
```

```bash
$ npx rigc build --rig inputs/rig/rig.json --motion run/motion.json --out run/build > run/build.stdout 2>&1
  ..    52 assertions: 21 measured (21 passed, 0 failed), 17 skipped, 14 not in profile "spine"
  ..    pages=28 regions=28 bones=81 slots=28 animations=2 version=4.3.13 regionAttachments=22 meshAttachments=6 physicsConstraints=44 physicsTimelineKeys=0 rig=wind_painting profile=spine
  ..    here: 42 rule(s) on the model side over the document, 9 of the round trip's own restated over the emitted text; not run: A00_ROUNDTRIP_PARSE — spine-core's parse, which only the entry that links spine-core runs, on build and validate: installed, the same `rigc` once @esotericsoftware/spine-core is installed beside the package; from a source checkout, `bun cli.ts`
rigc: wrote run/build/skeleton.json
rigc: wrote run/build/skeleton.atlas
rigc: wrote run/build/skeleton.model.json
rigc: look at it: rigc render --candidate run/build
```

```bash
$ npx rigc render --candidate run/build --animation run --fps 30 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l --out run/render/ > run/render/render.stdout 2>&1
  ..    run              200 frame(s), 6.633s + contact.png + geometry.json + folds.json (1 of 6 mesh(es) fold) + pass-through.json (0 of 2 pair(s) pass through) -> run/render/run@30fps
  ..    folds    "run": mesh "bottomwear" (slot "bottomwear") folds on 16 frame(s) [42, 52, 62, 72, 82, 92, 102, 112, 122, 132, 142, 152, 162, 172, 182, 192] at 30 fps; worst frame 52 (t=1.7333s): 2 of 204 triangle(s) [188, 189] in world box x [-4.12, 29.49] y [411.19, 452.62] (33.60 × 41.42), setup-pose area 961.00 units² = 0.992% of the mesh's; 3 triangle(s) fold on some frame [110, 188, 189]
  ..    pass     "run": cloth "bottomwear" over leg "thigh_r" passes through on 0 of 200 frame(s) read at 30 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0000) on its left side
  ..    pass     "run": cloth "bottomwear" over leg "thigh_l" passes through on 0 of 200 frame(s) read at 30 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0000) on its left side
rigc: wrote run/render/frames.json
```

```bash
$ npx rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --out run/motion.json --name run --build run/build --render run/render --report run/report.json --plant-feet --leg-scale 0.8,1.05 --stance 0.07
  POSTURE bounce r 180–182 (detrended y sd, rig/reference): hip 1.079 (4.9/4.5u, r=0.993), neck 1.024 (5.1/5.0u, r=0.907), eyes − neck 2.747 (2.2/0.8u, r=0.991)
  POSTURE bounce l 190–192 (detrended y sd, rig/reference): hip 1.049 (10.5/10.0u, r=0.963), neck 1.377 (10.4/7.6u, r=0.856), eyes − neck 2.329 (1.5/0.7u, r=0.996)
  FEET   the posed build, outside jumps: the lowest ankle's vertical range 0.00 units = 0.0000 leg lengths (rig leg r 388.1, l 392.0 units) over 60 frames
  FEET   the supporting ankle over each support span: worst vertical range 0.00 units = 0.0000 leg lengths (r 140–142), worst horizontal drift 24.21 units = 0.0618 leg lengths (l 130–132)
  FOLD   mesh "bottomwear" (slot "bottomwear") folds on 88 frame(s) at 30 fps
  wrote run/motion.json — animations: idle, run
```

```bash
$ npx rigc build --rig inputs/rig/rig.json --motion run/motion.json --out run/build > run/build.stdout 2>&1
  ..    52 assertions: 21 measured (21 passed, 0 failed), 17 skipped, 14 not in profile "spine"
  ..    pages=28 regions=28 bones=81 slots=28 animations=2 version=4.3.13 regionAttachments=22 meshAttachments=6 physicsConstraints=36 physicsTimelineKeys=0 rig=wind_painting profile=spine
rigc: wrote run/build/skeleton.json
rigc: wrote run/build/skeleton.atlas
rigc: wrote run/build/skeleton.model.json
```

```bash
$ npx rigc render --candidate run/build --animation run --fps 30 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l --out run/render/ > run/render/render.stdout 2>&1
  ..    run              200 frame(s), 6.633s + contact.png + geometry.json + folds.json (1 of 6 mesh(es) fold) + pass-through.json (0 of 2 pair(s) pass through) -> run/render/run@30fps
  ..    folds    "run": mesh "bottomwear" (slot "bottomwear") folds on 88 frame(s)
  ..    pass     "run": cloth "bottomwear" over leg "thigh_r" passes through on 0 of 200 frame(s) read at 30 fps
  ..    pass     "run": cloth "bottomwear" over leg "thigh_l" passes through on 0 of 200 frame(s) read at 30 fps
rigc: wrote run/render/frames.json
```

```bash
$ npx rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --out run/motion.json --name run --build run/build --render run/render --report run/report.json --plant-feet --leg-scale 0.08,1.05 --stance 0.07
  POSTURE bounce r 180–182 (detrended y sd, rig/reference): hip 1.091 (4.8/4.4u, r=0.992), neck 1.036 (5.0/4.8u, r=0.909), eyes − neck 2.653 (2.1/0.8u, r=0.991)
  POSTURE bounce l 190–192 (detrended y sd, rig/reference): hip 1.061 (10.3/9.7u, r=0.963), neck 1.393 (10.2/7.3u, r=0.856), eyes − neck 2.246 (1.5/0.7u, r=0.996)
  FEET   the posed build, outside jumps: the lowest ankle's vertical range 0.00 units = 0.0000 leg lengths (rig leg r 347.3, l 378.2 units) over 60 frames
  FEET   the supporting ankle over each support span: worst vertical range 0.00 units = 0.0000 leg lengths (r 140–142), worst horizontal drift 23.52 units = 0.0622 leg lengths (l 130–132)
  FOLD   rigc render --folds at 30 fps: no mesh folds
  wrote run/motion.json — animations: idle, run
```

```bash
$ npx rigc build --rig inputs/rig/rig.json --motion run/motion.json --out run/build > run/build.stdout 2>&1
  ..    52 assertions: 21 measured (21 passed, 0 failed), 17 skipped, 14 not in profile "spine"
  ..    pages=28 regions=28 bones=81 slots=28 animations=2 version=4.3.13 regionAttachments=22 meshAttachments=6 physicsConstraints=44 physicsTimelineKeys=0 rig=wind_painting profile=spine
rigc: wrote run/build/skeleton.json
rigc: wrote run/build/skeleton.atlas
rigc: wrote run/build/skeleton.model.json
```

```bash
$ npx rigc render --candidate run/build --animation run --fps 30 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l --out run/render/ > run/render/render.stdout 2>&1
  ..    run              200 frame(s), 6.633s + contact.png + geometry.json + folds.json (0 of 6 mesh(es) fold) + pass-through.json (0 of 2 pair(s) pass through) -> run/render/run@30fps
  ..    pass     "run": cloth "bottomwear" over leg "thigh_r" passes through on 0 of 200 frame(s) read at 30 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0000) on its left side
  ..    pass     "run": cloth "bottomwear" over leg "thigh_l" passes through on 0 of 200 frame(s) read at 30 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0000) on its left side
rigc: wrote run/render/frames.json
```

```bash
$ mkdir -p run/after && cp run/motion.json run/after/ && cp -r run/build run/after/build && cp -r run/render run/after/render
```

```bash
$ mkdir -p run/evidence && node generate_evidence.js
Generated run/evidence/compare_0000.png
Generated run/evidence/compare_0006.png
Generated run/evidence/compare_0012.png
Generated run/evidence/compare_0016.png
```
```bash
$ python3 tools/grade.py --round R2 --geometry run/render/run@30fps/geometry.json --report run/report.json --build run/build.stdout --folds run/render/run@30fps/folds.json --passthrough run/render/run@30fps/pass-through.json --sequence inputs/pose/sequence.json --map run/map.json --cycle 20 --trunk body,chest,neck,head
grade R2
NOTE  airborne spans: report feet.jumps, 20 span(s)
NOTE  rig leg length 485.0928 units (setup pose, leg_l0->foot_l, leg_r0->foot_r); hip width 84.0000
NOTE  sequence leg length 399.28 (95th percentile hip->ankle, mean of sides, the sequence's own units); the sequence carries no camera
PASS  gate            Gate: build green (52 assertions: 21 measured, 0 failed); 18/18 landings within tolerance (worst at 0.15 of its tolerance)
PASS  support-foot    Support foot: max |lower foot - floor| 0.0000 leg lengths at frame 172 over 60 grounded frames (floor 124.575 units) [bar <= 0.01]
PASS  two-feet        Two feet: two-foot frames: none in the sequence; lifted frames (sequence ankles > 0.04 apart): 0 of 60 with the lifted foot within 0.01 of the support foot (lowest lift 0.5127 at frame 80) [bar 0]; median rig/sequence lift 0.965 [bar 0.85-1.15]
PASS  slide           Slide: max |support-foot move - closure - sequence ankle move x report scale 1.15021| 0.00002 leg lengths/frame (foot_r, frame 1->2) over 40 steps (travel: in-place; closure +0.03816 units/frame removed (report feet.closure drift -7.59 over 200 frames)) [bar <= 0.005]
PASS  floor           Floor: per-cycle floor spread 0.0000 leg lengths over 10 cycles [bar <= 0.01, the support-foot band: the table gives this row no number of its own]
PASS  jitter          Jitter: limbs 1.038x sequence (10.444 vs 10.060 deg/f^2, 9 bones) [bar <= 1.1], trunk+head 1.000x sequence (2.046 vs 2.046 deg/f^2, chest,head) [bar <= 1.1]; joint pairs from the map
PASS  folds           Folds: 0 frames fold over 6 mesh(es) [bar 0]
PASS  pass-through    Pass-through: bottomwear:thigh_r 0 of 200 frames; bottomwear:thigh_l 0 of 200 frames [bar 0]
PASS  loop            Loop: cycle 1 vs cycle 10: max keyed-bone angle difference 0.0082 deg (sleeve_l1, cycle frame 19) [bar <= 1.0], max hip/foot_l/foot_r world position difference 0.0000 leg lengths (foot_r, cycle frame 19) [bar <= 0.01]
PASS  airborne        Airborne: airborne spans per cycle [2, 2, 2, 2, 2, 2, 2, 2, 2, 2] [bar 2 each]; 0 detected span(s) off the printed spans [(4, 9), (14, 19)] +/- 1 [bar 0]; lowest foot on an airborne frame 0.0464 leg lengths above the floor at frame 139 [bar > 0.01: above the support-foot band]
PASS  hip-vertical    Hip vertical range: rig/sequence 0.984 (rig 0.0939, sequence 0.0954 leg lengths, median per-cycle width over 10 cycles) [bar 0.85-1.15]
PASS  hip-horizontal  Hip horizontal range: rig/sequence 1.126 (rig 0.3706, sequence 0.3291 hip widths, median per-cycle width over 10 cycles) [bar 0.85-1.15]
PASS  rebound         Rebound: median rig/sequence peak upward hip acceleration in the stance windows 1.328 over 19 windows [bar 0.7-1.43]
PASS  hip-tilt        Hip tilt: rig tilt range 14.390 deg = 1.000 of the sequence's 14.390 [bar >= 0.85], sign agrees (covariance +3.66e+03)
RESULT PASS (14 pass, 0 fail, 0 skip of 14 rows)
```

finished: 2026-10-18T23:32:23Z
