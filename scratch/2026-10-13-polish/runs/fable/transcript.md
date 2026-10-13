started: 2026-10-13T10:52:24Z

# Transcript — Fable 5.1, dancing-rig polish, 2026-10-13

## 1. bun install
```
$ bun install
+ @rig-c/parts@1.17.0
+ @rig-c/pose@0.6.0
+ rig-c@2.51.1
6 packages installed [932.00ms]
```
## 2. render the given build (evidence source)
```
$ bunx rigc render --candidate inputs/dance/build --animation dance --fps 24 --max 960 --geometry --folds --out run/evidence/_work/render_before
  ..    poser    rigc core — …/inputs/dance/build/skeleton.model.json
  ..    754x960px at 24 fps, 1 set(s) -> …/run/evidence/_work/render_before
dance@24fps
exit 0
```
## 3. baseline rebuild
```
$ bunx rigc build --rig inputs/rig/rig.json --motion inputs/dance/motion.json --out run/evidence/_work/build_baseline --report run/evidence/_work/build_baseline.report.json
  ..    52 assertions: 21 measured (21 passed, 0 failed), 17 skipped, 14 not in profile "spine"
rigc: wrote …/build_baseline/skeleton.json / skeleton.atlas / skeleton.model.json
real 11.10   exit 0
```
## 4–5. skirt physics trials (rig fix) — run/after/rig/rig.json
```
$ bunx rigc build --rig run/after/rig/rig.json --images inputs/rig/images --motion inputs/dance/motion.json --out run/evidence/_work/build_physA
  ..    52 assertions: 21 measured (21 passed, 0 failed), 17 skipped, 14 not in profile "spine"   (exit 0)
$ bunx rigc render --candidate run/evidence/_work/build_physA --animation dance --fps 12 --max 480 --geometry --out run/evidence/_work/render_physA   (exit 0)
   skirt_c2 − hip range: clip 130.7°, K1 87.8°  → too loose (inertia .5/.6/.7, strength 120/90/60, damping .85)
$ bunx rigc build … --out run/evidence/_work/build_physB   (exit 0, same gate line)
$ bunx rigc render --candidate run/evidence/_work/build_physB … --out run/evidence/_work/render_physB   (exit 0)
   skirt_c2 − hip range: clip 64.6°, K1 41.0°, jump1 24.0°  → accepted (inertia .3/.35/.4, strength 200/170/140, damping .82; given rig: 21.9° / 13.6° / 5.0°)
```
## 6. motion post-process + build M1
```
$ python3 run/after/post_motion.py inputs/dance/motion.json run/evidence/_work/render_before/dance@24fps/geometry.json inputs/reference/pose.json run/after/dance/motion.json
frames 313  rest foot y 152.80  airborne frames 15: [88, 89, 90, 99, 100, 101, 178, 179, 180, 187, 188, 189, 267, 268, 269]
dy min -23.0 max 52.7; breath keys 33 last t 13; blink keys 18
$ bunx rigc build --rig run/after/rig/rig.json --images inputs/rig/images --motion run/after/dance/motion.json --out run/evidence/_work/build_M1 --report run/evidence/_work/build_M1.report.json
  ..    52 assertions: 21 measured (21 passed, 0 failed), 17 skipped, 14 not in profile "spine"   (exit 0)
$ bunx rigc render --candidate run/evidence/_work/build_M1 --animation dance --fps 24 --max 960 --geometry --folds --out run/evidence/_work/render_M1   (exit 0)
   lower foot at rest height on 298/313 frames, +28.4 max on the 15 airborne ones, never below
```

## Entry 7 — retarget again with a `frames` window on K4 (map fix) — run/after/map.json
## 7–7b. retarget with a K4 frames window (map fix attempt) — no effect on the span
```
$ bunx rig-pose retarget --rig run/after/rig/rig.json --map run/after/map.json --pose inputs/reference/pose.json --out run/after/dance/motion.retarget.json --name dance --min-score 0.3 --smooth 7 --flip 90 --short 0.35 --bends clamp --report run/after/dance/report.json
FAIL  POSE_KEYS: inputs/reference/pose.json has a key this reader does not know: "fps"; the keys it reads are spec, space, width, height, source, frames
FAIL  POSE_SPEC: inputs/reference/pose.json "spec" is the string "rig-c-pose-frames/0"; this reader reads "rig-pose-sequence/1"
FAIL  POSE_SPACE: … "space" is {"units":"painting-px",…}; it must be exactly {"units":"picture-px",…}
exit 1
$ (same, --pose run/after/dance/pose.seq.json — converted copy)
FAIL  RIG_GATE_BASE: run/after/rig/rig.json with no motion spec is red under rigc build --profile spine before any animation
FAIL  RIGC: rigc compile error: image "hair_back.png" is not on disk at run/after/rig/images/hair_back.png
exit 1
$ (same, after setting rig.json "images": "../../../inputs/rig/images")
  SWITCH set "K4_hand_up" … frames 27–33 (t=1.125s until 1.417s)   ← unchanged
  GATE   rigc build --profile spine: green — 52 assertions: 21 measured (21 passed, 0 failed), 17 skipped, 14 not in profile "spine"
  wrote run/after/dance/motion.retarget.json — animations: dance
exit 0
```

## 8–10. K4 timing by key edit, final build, render, clip
```
$ python3 run/after/post_motion.py inputs/dance/motion.json run/evidence/_work/render_before/dance@24fps/geometry.json inputs/reference/pose.json run/after/dance/motion.json
K4 keys moved 10 -> t=0.9375
frames 313  rest foot y 152.80  airborne frames 15: [88, 89, 90, 99, 100, 101, 178, 179, 180, 187, 188, 189, 267, 268, 269]
dy min -23.0 max 52.7; breath keys 33 last t 13; blink keys 18
$ bunx rigc build --rig run/after/rig/rig.json --motion run/after/dance/motion.json --out run/after/build --copy-images --report run/after/build.report.json
  ..    52 assertions: 21 measured (21 passed, 0 failed), 17 skipped, 14 not in profile "spine"   (exit 0)
$ bunx rigc render --candidate run/after/build --animation dance --fps 24 --max 960 --geometry --folds --out run/evidence/_work/render_after   (exit 0, 313 frames)
$ ffmpeg -y -i inputs/reference/ref1080.mp4 -framerate 24 -i run/evidence/_work/render_after/dance@24fps/f%04d.png -i inputs/reference/audio.mp3 -filter_complex "[0:v]scale=270:480[a];[1:v]format=rgba,scale=378:480,format=rgb24[b];[a][b]hstack,format=yuv420p[v]" -map "[v]" -map 2:a -c:v libx264 -crf 18 -r 24 -c:a aac -b:a 160k -shortest run/after/clip-audio.mp4
ffmpeg exit 0 → video 648x480 24/1 nb_frames=313, audio aac 13.03 s
(first attempt with scale=-1:480 + pad=378 failed: "Padded dimensions cannot be smaller than input dimensions" — the width rounds to 378 already)
```

finished: 2026-10-13T11:17:38Z
