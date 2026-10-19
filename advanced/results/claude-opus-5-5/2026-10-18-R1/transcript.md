started: 2026-10-18T22:51:30Z

## 1. npm install
```
$ npm install
1 package is looking for funding
found 0 vulnerabilities
(exit 0)
```

## 2. baseline retarget (run/map.json, no leg flags)
```
$ npx rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --out run/before/motion.json --name walk --build run/before/build --report run/before/report.json
  GATE   rigc build --profile spine: green — 52 assertions: 21 measured (21 passed, 0 failed), 17 skipped, 14 not in profile "spine"
  FEET   the posed build, outside jumps: the lowest ankle's vertical range 47.76 units = 0.0985 leg lengths
  FOLD   rigc render --folds at 30 fps: no mesh folds
  wrote run/before/motion.json — animations: idle, walk
(exit 0)
```

## 3. baseline build + render + grade
```
$ npx rigc build --rig inputs/rig/rig.json --motion run/before/motion.json --out run/before/rigc-build > run/before/build.out
  ..    52 assertions: 21 measured (21 passed, 0 failed), 17 skipped, 14 not in profile "spine"
rigc: wrote …/run/before/rigc-build/skeleton.model.json   (exit 0)
$ npx rigc render --candidate run/before/rigc-build --animation walk --fps 30 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l --out run/before/render
  ..    walk  224 frame(s), 7.433s + contact.png + geometry.json + folds.json (0 of 6 mesh(es) fold) + pass-through.json (0 of 2 pair(s) pass through)
(exit 0)
$ python3 tools/grade.py --round R1 … (run/before) > run/before/grade.out
RESULT FAIL (4 pass, 5 fail, 0 skip of 9 rows)   (exit 1)
```

## 4. map2 (trunk without reach, head neck→nose at head_up:tip), no leg flags
```
$ run/pipeline.sh run/try2 run/map2.json      # retarget → rigc build → rigc render --fps 30 --geometry --folds --pass-through … → grade.py
retarget exit=0 · GATE green 52 assertions: 21 measured (21 passed, 0 failed)
build exit=0 · render exit=0 (0 of 6 meshes fold, 0 of 2 pairs pass through)
PASS jitter limbs 1.000x, trunk+head 1.000x · PASS loop 0.0001 deg
RESULT FAIL (6 pass, 3 fail, 0 skip of 9 rows)
```

## 5. + --leg-scale 0.8,1.05 --plant-feet --stance 0.07
```
$ run/pipeline.sh run/try3 run/map2.json --leg-scale 0.8,1.05 --plant-feet --stance 0.07
retarget exit=0 · build exit=0 · render exit=0
FAIL two-feet … 42 of 168 with the lifted foot within 0.01 of the support foot … median rig/sequence lift 0.616
RESULT FAIL (8 pass, 1 fail, 0 skip of 9 rows)
```

## 6. two variants
```
$ run/pipeline.sh run/try4a run/map2.json --leg-scale 0.45,1.05 --plant-feet
FAIL two-feet: two-foot frames: max height difference 0.0209 leg lengths at frame 203 over 35 [bar <= 0.02]
RESULT FAIL (8 pass, 1 fail, 0 skip of 9 rows)
$ run/pipeline.sh run/try4b run/map2.json --leg-scale 0.45,1.05 --plant-feet --stance 0.035
RESULT PASS (9 pass, 0 fail, 0 skip of 9 rows)
```

## 7. final run
```
$ cp run/map2.json run/after/map.json
$ run/pipeline.sh run/after run/after/map.json --leg-scale 0.45,1.05 --plant-feet --stance 0.035
retarget exit=0 · GATE green — 52 assertions: 21 measured (21 passed, 0 failed); wrote run/after/motion.json
build exit=0 · 52 assertions: 21 measured (21 passed, 0 failed)
render exit=0 · walk 224 frame(s) + geometry.json + folds.json (0 of 6 mesh(es) fold) + pass-through.json (0 of 2 pair(s) pass through)
RESULT PASS (9 pass, 0 fail, 0 skip of 9 rows)
```

## 8. evidence
```
$ npx rigc render --candidate run/before/rigc-build --animation walk --fps 30 --max 540 --out run/evidence/render-before   (exit 0, 224 frames)
$ npx rigc render --candidate run/after/rigc-build  --animation walk --fps 30 --max 540 --out run/evidence/render-after    (exit 0, 224 frames)
$ ffmpeg -i inputs/pose/stick.mp4 <scratchpad>/stick/s%04d.png   ← outside the package by mistake; deleted immediately
$ ffmpeg -v error -y -i inputs/pose/stick.mp4 run/evidence/stick_tmp/s%04d.png   (224 frames; folder removed after composing)
$ python3 (PIL) → run/evidence/frame000,005,012,018,026,173,203.png   ok
```

## 9. last grader run
```
$ python3 tools/grade.py --round R1 --geometry run/after/render/walk@30fps/geometry.json --sequence inputs/pose/sequence.json --report run/after/report.json --build run/after/build.out --cycle 32 --folds run/after/render/walk@30fps/folds.json --passthrough run/after/render/walk@30fps/pass-through.json --map run/after/map.json --feet foot_l,foot_r --hip hip --trunk chest,head > run/after/grade.out
RESULT PASS (9 pass, 0 fail, 0 skip of 9 rows)   (exit 0)
```
finished: 2026-10-18T22:59:41Z
