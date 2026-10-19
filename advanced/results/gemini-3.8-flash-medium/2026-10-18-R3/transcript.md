started: 2026-10-18T23:18:07Z

```sh
npm install
# added 6 packages, and audited 7 packages in 3s
# found 0 vulnerabilities

mkdir -p run/before && npx rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --out run/before/motion.json --name dance --camera run/before/camera.json --report run/before/report.json
#   GATE   rigc build --profile spine: green — 52 assertions: 24 measured (24 passed, 0 failed), 14 skipped, 14 not in profile "spine"
#   FOLD   rigc render --folds at 24 fps: no mesh folds
#   wrote run/before/camera.json — camera track (313 frames)
#   wrote run/before/motion.json — animations: idle, ..., dance

npx rigc build --rig inputs/rig --motion run/before/motion.json --out run/before/build > run/before/build.log 2>&1
# rigc compile error: cannot read inputs/rig: EISDIR: illegal operation on a directory, read (see rigc guide CE_COMPILE_JSON_READ_FAILED)

npx rigc build --rig inputs/rig/rig.json --images inputs/rig/images --motion run/before/motion.json --out run/before/build > run/before/build.log 2>&1
#   ..    52 assertions: 24 measured (24 passed, 0 failed), 14 skipped, 14 not in profile "spine"
# rigc: wrote run/before/build/skeleton.json
# rigc: wrote run/before/build/skeleton.atlas
# rigc: wrote run/before/build/skeleton.model.json

npx rigc render --candidate run/before/build --animation dance --fps 24 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l,bottomwear:shin_r,bottomwear:shin_l --out run/before/render
#   ..    dance            313 frame(s), 13.000s + contact.png + geometry.json + folds.json (0 of 6 mesh(es) fold) + pass-through.json (0 of 4 pair(s) pass through) -> run/before/render/dance@24fps
# rigc: wrote run/before/render/frames.json

mkdir -p run/after && npx rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --out run/after/motion.json --name dance --camera run/after/camera.json --report run/after/report.json --plant-feet --stance 0.07 --leg-scale 0.8,1.05 --flip 90 --short 0.35 --reduce 1 --reduce-hip 1 --carry-idle
#   GATE   rigc build --profile spine: green — 52 assertions: 24 measured (24 passed, 0 failed), 14 skipped, 14 not in profile "spine"
#   FOLD   rigc render --folds at 24 fps: no mesh folds
#   wrote run/after/camera.json — camera track (313 frames)
#   wrote run/after/motion.json — animations: idle, ..., dance

npx rigc build --rig inputs/rig/rig.json --images inputs/rig/images --motion run/after/motion.json --out run/after/build > run/after/build.log 2>&1
#   ..    52 assertions: 24 measured (24 passed, 0 failed), 14 skipped, 14 not in profile "spine"
# rigc: wrote run/after/build/skeleton.json
# rigc: wrote run/after/build/skeleton.atlas
# rigc: wrote run/after/build/skeleton.model.json

npx rigc render --candidate run/after/build --animation dance --fps 24 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l,bottomwear:shin_r,bottomwear:shin_l --out run/after/render
#   ..    dance            313 frame(s), 13.000s + contact.png + geometry.json + folds.json (0 of 6 mesh(es) fold) + pass-through.json (0 of 4 pair(s) pass through) -> run/after/render/dance@24fps
# rigc: wrote run/after/render/frames.json

npx rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --out run/after/motion.json --name dance --camera run/after/camera.json --report run/after/report.json --plant-feet --stance 0.02 --leg-scale 0.8,1.05 --flip 90 --short 0.35 --reduce 0.5 --carry-idle
#   GATE   rigc build --profile spine: green — 52 assertions: 24 measured (24 passed, 0 failed), 14 skipped, 14 not in profile "spine"
#   FOLD   rigc render --folds at 24 fps: no mesh folds
#   wrote run/after/camera.json — camera track (313 frames)
#   wrote run/after/motion.json — animations: idle, ..., dance

npx rigc build --rig inputs/rig/rig.json --images inputs/rig/images --motion run/after/motion.json --out run/after/build > run/after/build.log 2>&1
#   ..    52 assertions: 24 measured (24 passed, 0 failed), 14 skipped, 14 not in profile "spine"
# rigc: wrote run/after/build/skeleton.json
# rigc: wrote run/after/build/skeleton.atlas
# rigc: wrote run/after/build/skeleton.model.json

npx rigc render --candidate run/after/build --animation dance --fps 24 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l,bottomwear:shin_r,bottomwear:shin_l --out run/after/render
#   ..    dance            313 frame(s), 13.000s + contact.png + geometry.json + folds.json (0 of 6 mesh(es) fold) + pass-through.json (0 of 4 pair(s) pass through) -> run/after/render/dance@24fps
# rigc: wrote run/after/render/frames.json

npx rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --out run/after/motion.json --name dance --camera run/after/camera.json --report run/after/report.json --plant-feet --stance 0.035 --leg-scale 0.8,1.05 --flip 90 --short 0.35 --carry-idle
#   GATE   rigc build --profile spine: green — 52 assertions: 24 measured (24 passed, 0 failed), 14 skipped, 14 not in profile "spine"
#   FOLD   rigc render --folds at 24 fps: no mesh folds
#   wrote run/after/camera.json — camera track (313 frames)
#   wrote run/after/motion.json — animations: idle, ..., dance

npx rigc build --rig inputs/rig/rig.json --images inputs/rig/images --motion run/after/motion.json --out run/after/build > run/after/build.log 2>&1
#   ..    52 assertions: 24 measured (24 passed, 0 failed), 14 skipped, 14 not in profile "spine"
# rigc: wrote run/after/build/skeleton.json
# rigc: wrote run/after/build/skeleton.atlas
# rigc: wrote run/after/build/skeleton.model.json

npx rigc render --candidate run/after/build --animation dance --fps 24 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l,bottomwear:shin_r,bottomwear:shin_l --out run/after/render
#   ..    dance            313 frame(s), 13.000s + contact.png + geometry.json + folds.json (0 of 6 mesh(es) fold) + pass-through.json (0 of 4 pair(s) pass through) -> run/after/render/dance@24fps
# rigc: wrote run/after/render/frames.json

python3 -c "import os, subprocess; from PIL import Image; ..." # generated side-by-side evidence frames
# Wrote run/evidence/frame_0040_comparison.png
# Wrote run/evidence/frame_0089_comparison.png
# Wrote run/evidence/frame_0130_comparison.png
# Wrote run/evidence/frame_0180_comparison.png
# Wrote run/evidence/frame_0240_comparison.png
# Wrote run/evidence/frame_0268_comparison.png
# Wrote run/evidence/frame_0278_comparison.png
```

finished: 2026-10-18T23:29:32Z
