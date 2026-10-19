started: 2026-10-18T23:18:06Z

```sh
npm install
```
```
added 6 packages, and audited 7 packages in 3s
1 package is looking for funding
  run `npm fund` for details
found 0 vulnerabilities
```

```sh
npx rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --out run/baseline.motion.json --name walk --report run/baseline.report.json
```
```
  LAND   bone "hip" origin — worst |reached − asked| 0.000687 units at frame 187 (t=6.233s); the tolerance is 0.01 units
  FEET   the posed build, outside jumps: the lowest ankle's vertical range 47.76 units = 0.0985 leg lengths (rig leg r 485.0, l 484.9 units) over 224 frames
  FEET   the supporting ankle over each support span: worst vertical range 49.04 units = 0.1011 leg lengths (l 0–14), worst horizontal drift 88.67 units = 0.1828 leg lengths (l 129–146)
  FOLD   rigc render --folds at 30 fps: no mesh folds
  wrote run/baseline.motion.json — animations: idle, walk
```

```sh
npx rigc build --rig inputs/rig --motion run/baseline.motion.json --out run/baseline_build | tee run/baseline_build.stdout.txt
```
```
rigc compile error: cannot read inputs/rig: EISDIR: illegal operation on a directory, read (see rigc guide CE_COMPILE_JSON_READ_FAILED)
```

```sh
npx rigc build --rig inputs/rig/rig.json --motion run/baseline.motion.json --out run/baseline_build | tee run/baseline_build.stdout.txt
```
```
  ..    52 assertions: 21 measured (21 passed, 0 failed), 17 skipped, 14 not in profile "spine"
  ..    pages=28 regions=28 bones=81 slots=28 animations=2 version=4.3.13 regionAttachments=22 meshAttachments=6 physicsConstraints=44 physicsTimelineKeys=0 rig=wind_painting profile=spine
rigc: wrote run/baseline_build/skeleton.json
rigc: wrote run/baseline_build/skeleton.atlas
rigc: wrote run/baseline_build/skeleton.model.json
rigc: look at it: rigc render --candidate run/baseline_build
```

```sh
npx rigc render --candidate run/baseline_build --animation walk --fps 30 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l --out run/baseline_render
```
```
  ..    pass     "walk": cloth "bottomwear" over leg "thigh_r" passes through on 0 of 224 frame(s) read at 30 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0000) on its left side
  ..    pass     "walk": cloth "bottomwear" over leg "thigh_l" passes through on 0 of 224 frame(s) read at 30 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0000) on its left side
rigc: wrote run/baseline_render/frames.json
```

```sh
npx rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --out run/fix1.motion.json --name walk --report run/fix1.report.json --plant-feet --leg-scale 0.45,1.05 --stance 0.02
```
```
  FEET   the posed build, outside jumps: the lowest ankle's vertical range 0.00 units = 0.0000 leg lengths (rig leg r 430.4, l 439.9 units) over 224 frames
  FEET   the supporting ankle over each support span: worst vertical range 0.00 units = 0.0000 leg lengths (l 92–107), worst horizontal drift 73.13 units = 0.1662 leg lengths (l 28–43)
  FOLD   rigc render --folds at 30 fps: no mesh folds
  wrote run/fix1.motion.json — animations: idle, walk
```

```sh
npx rigc build --rig inputs/rig/rig.json --motion run/fix1.motion.json --out run/fix1_build | tee run/fix1_build.stdout.txt
```
```
  ..    52 assertions: 21 measured (21 passed, 0 failed), 17 skipped, 14 not in profile "spine"
  ..    pages=28 regions=28 bones=81 slots=28 animations=2 version=4.3.13 regionAttachments=22 meshAttachments=6 physicsConstraints=44 physicsTimelineKeys=0 rig=wind_painting profile=spine
rigc: wrote run/fix1_build/skeleton.json
rigc: wrote run/fix1_build/skeleton.atlas
rigc: wrote run/fix1_build/skeleton.model.json
rigc: look at it: rigc render --candidate run/fix1_build
```

```sh
npx rigc render --candidate run/fix1_build --animation walk --fps 30 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l --out run/fix1_render
```
```
  ..    pass     "walk": cloth "bottomwear" over leg "thigh_r" passes through on 0 of 224 frame(s) read at 30 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0000) on its left side
  ..    pass     "walk": cloth "bottomwear" over leg "thigh_l" passes through on 0 of 224 frame(s) read at 30 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0000) on its left side
rigc: wrote run/fix1_render/frames.json
```

```sh
mkdir -p run/after && cp run/fix1.motion.json run/after/motion.json && cp run/fix1.report.json run/after/report.json && cp -r run/fix1_build run/after/build && cp -r run/fix1_render run/after/render && cp run/fix1_build.stdout.txt run/after/build.stdout.txt
```
```
(copied files and directories into run/after/)
```

```sh
mkdir -p run/evidence && for i in 0 5 16 21 31 64; do pad=$(printf "%04d" $i); ffmpeg -y -i inputs/pose/stick.mp4 -vf "select=eq(n\,$i)" -vframes 1 /tmp/stick_$pad.png 2>/dev/null; ffmpeg -y -i /tmp/stick_$pad.png -i run/after/render/walk@30fps/f$pad.png -filter_complex "[0:v]scale=-1:256[s];[s][1:v]hstack" run/evidence/frame_$pad.png 2>/dev/null; rm -f /tmp/stick_$pad.png; done
```
```
frame_0000.png frame_0005.png frame_0016.png frame_0021.png frame_0031.png frame_0064.png generated
```

finished: 2026-10-18T23:26:11Z
