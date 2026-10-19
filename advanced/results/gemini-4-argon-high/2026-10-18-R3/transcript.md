started: 2026-10-18T23:35:39Z

$ npm install
added 6 packages, and audited 7 packages in 835ms
found 0 vulnerabilities

$ npx rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --out run/before/motion.json --build run/before/build --report run/before/report.json --camera run/before/camera.json > run/before/retarget.log 2>&1
  GATE   rigc build --profile spine: green — 52 assertions: 24 measured (24 passed, 0 failed), 14 skipped, 14 not in profile "spine"
  FEET   the posed build, outside jumps: the lowest ankle's vertical range 75.89 units = 0.1463 leg lengths (rig leg r 512.9, l 524.5 units) over 303 frames
  FEET   the supporting ankle over each support span: worst vertical range 62.24 units = 0.1213 leg lengths (r 183–266), worst horizontal drift 56.11 units = 0.1094 leg lengths (r 183–266)
  FOLD   rigc render --folds at 24 fps: no mesh folds
  wrote run/before/camera.json — camera track (313 frames)
  wrote run/before/motion.json — animations: idle, pose_arms_up, pose_hands_behind_head, pose_hand_on_hip, pose_arms_crossed, pose_legs_apart, pose_hip_tilt_pos, pose_hip_tilt_neg, sweep_elbow_r_pos, sweep_elbow_r_neg, sweep_knee_r_pos, sweep_knee_r_neg, sweep_shoulder_r_out, sweep_shoulder_r_in, sweep_hip_tilt_pos, sweep_hip_tilt_neg, sweep_thigh_r_out, sweep_thigh_r_in, sway, set_K1, range_K1, set_K2, range_K2, set_K3, range_K3, set_K4, range_K4, set_K0, range_K0, turn, tilt, dance

$ npx rigc build --rig inputs/rig/rig.json --motion run/before/motion.json --images inputs/rig/images --out run/before/build > run/before/build.log 2>&1
  ..    52 assertions: 24 measured (24 passed, 0 failed), 14 skipped, 14 not in profile "spine"
rigc: wrote run/before/build/skeleton.json
rigc: wrote run/before/build/skeleton.atlas
rigc: wrote run/before/build/skeleton.model.json

$ npx rigc render --candidate run/before/build --animation dance --fps 24 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l,bottomwear:shin_r,bottomwear:shin_l --out run/before/render > run/before/render.log 2>&1
  ..    dance            313 frame(s), 13.000s + contact.png + geometry.json + folds.json (0 of 6 mesh(es) fold) + pass-through.json (0 of 4 pair(s) pass through) -> run/before/render/dance@24fps
rigc: wrote run/before/render/frames.json

$ python3 tools/grade.py --round R3 --geometry run/before/render/dance@24fps/geometry.json --sequence inputs/pose/sequence.json --report run/before/report.json --build run/before/build.log --folds run/before/render/dance@24fps/folds.json --passthrough run/before/render/dance@24fps/pass-through.json --map run/map.json --camera run/before/camera.json --trunk chest,head > run/before/grade.txt 2>&1
FAIL  support-foot    Support foot: max |lower foot - floor| 0.0615 leg lengths at frame 148 over 299 grounded frames (floor 141.094 units) [bar <= 0.01]
FAIL  two-feet        Two feet: two-foot frames: max height difference 0.0624 leg lengths at frame 254 over 235 [bar <= 0.02]; lifted frames (sequence ankles > 0.04 apart): 35 of 35 with the lifted foot within 0.01 of the support foot (lowest lift 0.0027 at frame 278) [bar 0]; median rig/sequence lift 0.083 [bar 0.85-1.15]
FAIL  slide           Slide: max support-foot move 0.02205 leg lengths/frame (foot_r, frame 216->217) over 294 steps [bar <= 0.005]
FAIL  floor           Floor: per-support-span floor spread 0.0434 leg lengths over 5 spans [bar <= 0.01, the support-foot band: the table gives this row no number of its own]
FAIL  jitter          Jitter: limbs 1.000x sequence (1.323 vs 1.323 deg/f^2, 8 bones) [bar <= 1.1], trunk+head 1.201x sequence (0.891 vs 0.742 deg/f^2, chest,head) [bar <= 1.1]; joint pairs from the map
FAIL  hip-vertical    Hip vertical range: rig/sequence 0.055 (rig 0.0069, sequence 0.0997 leg lengths, median per-span width over 5 spans) [bar 0.85-1.15]
FAIL  rebound         Rebound: median rig/sequence peak upward hip acceleration in the stance windows 0.647 over 2 windows [bar 0.7-1.43]
FAIL  hip-tilt        Hip tilt: rig tilt range 0.000 deg = 0.000 of the sequence's 54.769 [bar >= 0.85], sign DISAGREES (covariance +0)
RESULT FAIL (5 pass, 8 fail, 0 skip of 13 rows)

$ mkdir -p run/evidence && for f in 0089 0132 0148 0217 0254 0278; do idx=$((10#$f)); ffmpeg -y -loglevel error -i inputs/pose/stick.mp4 -i "run/before/render/dance@24fps/f${f}.png" -filter_complex "[0:v]select=eq(n\\,${idx}),setpts=PTS-STARTPTS,scale=-1:512[s];[1:v]scale=-1:512:flags=neighbor[r];[s][r]hstack=inputs=2" -frames:v 1 "run/evidence/before_f${f}.png"; done
wrote run/evidence/before_f0089.png .. before_f0278.png (6 side-by-side frames) and run/findings.md

$ npx rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --plant-feet --stance 0.03 --leg-scale 0.7,1.05 --carry-idle --out run/after/motion.json --build run/after/build --report run/after/report.json --camera run/after/camera.json > run/after/retarget.log 2>&1
  POSTURE hip tilt range (chain "pelvis", r_hip → l_hip, Spine degrees): reference 54.8° (−24.4° … +30.4°), rig 54.8° (−24.4° … +30.4°) — rig/reference 1.000
  FEET   the posed build, outside jumps: the lowest ankle's vertical range 23.02 units = 0.0475 leg lengths (rig leg r 481.0, l 489.1 units) over 303 frames
  FEET   the supporting ankle over each support span: worst vertical range 0.01 units = 0.0000 leg lengths (r 183–266), worst horizontal drift 0.02 units = 0.0000 leg lengths (l 272–312)
  FOLD   rigc render --folds at 24 fps: no mesh folds
  wrote run/after/camera.json — camera track (313 frames)
  wrote run/after/motion.json

$ npx rigc build --rig inputs/rig/rig.json --motion run/after/motion.json --images inputs/rig/images --out run/after/build > run/after/build.log 2>&1
  ..    52 assertions: 24 measured (24 passed, 0 failed), 14 skipped, 14 not in profile "spine"

$ npx rigc render --candidate run/after/build --animation dance --fps 24 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l,bottomwear:shin_r,bottomwear:shin_l --out run/after/render > run/after/render.log 2>&1
  ..    dance            313 frame(s), 13.000s + contact.png + geometry.json + folds.json (0 of 6 mesh(es) fold) + pass-through.json (0 of 4 pair(s) pass through) -> run/after/render/dance@24fps

$ python3 tools/grade.py --round R3 --geometry run/after/render/dance@24fps/geometry.json --sequence inputs/pose/sequence.json --report run/after/report.json --build run/after/build.log --folds run/after/render/dance@24fps/folds.json --passthrough run/after/render/dance@24fps/pass-through.json --map run/map.json --camera run/after/camera.json --trunk hip,chest,head > run/after/grade.txt 2>&1
FAIL  jitter          Jitter: limbs 1.150x sequence (2.000 vs 1.740 deg/f^2, 8 bones) [bar <= 1.1], trunk+head 1.664x sequence (2.763 vs 1.660 deg/f^2, hip,chest,head) [bar <= 1.1]; joint pairs from the map
RESULT FAIL (12 pass, 1 fail, 0 skip of 13 rows)

$ npx rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --plant-feet --stance 0.03 --leg-scale 0.7,1.05 --carry-idle --reduce 1 --out run/after/motion.json --build run/after/build --report run/after/report.json --camera run/after/camera.json > run/after/retarget.log 2>&1 && npx rigc build --rig inputs/rig/rig.json --motion run/after/motion.json --images inputs/rig/images --out run/after/build > run/after/build.log 2>&1 && npx rigc render --candidate run/after/build --animation dance --fps 24 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l,bottomwear:shin_r,bottomwear:shin_l --out run/after/render > run/after/render.log 2>&1 && python3 tools/grade.py --round R3 --geometry run/after/render/dance@24fps/geometry.json --sequence inputs/pose/sequence.json --report run/after/report.json --build run/after/build.log --folds run/after/render/dance@24fps/folds.json --passthrough run/after/render/dance@24fps/pass-through.json --map run/map.json --camera run/after/camera.json --trunk chest,head > run/after/grade.txt 2>&1
FAIL  slide           Slide: max support-foot move 0.01651 leg lengths/frame (foot_r, frame 64->65) over 294 steps [bar <= 0.005]
FAIL  jitter          Jitter: limbs 1.020x sequence (1.807 vs 1.771 deg/f^2, 9 bones) [bar <= 1.1], trunk+head 1.332x sequence (1.971 vs 1.480 deg/f^2, chest,head) [bar <= 1.1]; joint pairs from the map
RESULT FAIL (11 pass, 2 fail, 0 skip of 13 rows)
$ npx rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --plant-feet --stance 0.03 --leg-scale 0.68,1.1 --carry-idle --out run/after/motion.json --build run/after/build --report run/after/report.json --camera run/after/camera.json > run/after/retarget.log 2>&1 && npx rigc build --rig inputs/rig/rig.json --motion run/after/motion.json --images inputs/rig/images --out run/after/build > run/after/build.log 2>&1 && npx rigc render --candidate run/after/build --animation dance --fps 24 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l,bottomwear:shin_r,bottomwear:shin_l --out run/after/render > run/after/render.log 2>&1 && python3 tools/grade.py --round R3 --geometry run/after/render/dance@24fps/geometry.json --sequence inputs/pose/sequence.json --report run/after/report.json --build run/after/build.log --folds run/after/render/dance@24fps/folds.json --passthrough run/after/render/dance@24fps/pass-through.json --map run/map.json --camera run/after/camera.json --trunk hip,chest,head > run/after/grade.txt 2>&1
PASS  jitter          Jitter: limbs 0.989x sequence (1.722 vs 1.741 deg/f^2, 8 bones) [bar <= 1.1], trunk+head 1.060x sequence (1.761 vs 1.662 deg/f^2, hip,chest,head) [bar <= 1.1]; joint pairs from the map
PASS  hip-tilt        Hip tilt: rig tilt range 54.769 deg = 1.000 of the sequence's 54.769 [bar >= 0.85], sign agrees (covariance +4.36e+04)
RESULT PASS (13 pass, 0 fail, 0 skip of 13 rows)

$ npx rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --plant-feet --stance 0.03 --leg-scale 0.68,1.1 --carry-idle --out run/after/motion.json --build run/after/build --report run/after/report.json --camera run/after/camera.json > run/after/retarget.log 2>&1 && npx rigc build --rig inputs/rig/rig.json --motion run/after/motion.json --images inputs/rig/images --out run/after/build > run/after/build.log 2>&1 && npx rigc render --candidate run/after/build --animation dance --fps 24 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l,bottomwear:shin_r,bottomwear:shin_l --out run/after/render > run/after/render.log 2>&1 && python3 tools/grade.py --round R3 --geometry run/after/render/dance@24fps/geometry.json --sequence inputs/pose/sequence.json --report run/after/report.json --build run/after/build.log --folds run/after/render/dance@24fps/folds.json --passthrough run/after/render/dance@24fps/pass-through.json --map run/map.json --camera run/after/camera.json --trunk chest,head > run/after/grade_chest_head.txt 2>&1 && python3 tools/grade.py --round R3 --geometry run/after/render/dance@24fps/geometry.json --sequence inputs/pose/sequence.json --report run/after/report.json --build run/after/build.log --folds run/after/render/dance@24fps/folds.json --passthrough run/after/render/dance@24fps/pass-through.json --map run/map.json --camera run/after/camera.json --trunk hip,chest,head > run/after/grade.txt 2>&1
PASS  jitter          Jitter: limbs 0.991x sequence (1.755 vs 1.772 deg/f^2, 9 bones) [bar <= 1.1], trunk+head 1.000x sequence (1.387 vs 1.388 deg/f^2, chest,head) [bar <= 1.1]; joint pairs from the map
RESULT PASS (13 pass, 0 fail, 0 skip of 13 rows)
PASS  jitter          Jitter: limbs 0.989x sequence (1.722 vs 1.741 deg/f^2, 8 bones) [bar <= 1.1], trunk+head 1.000x sequence (1.599 vs 1.599 deg/f^2, hip,chest,head) [bar <= 1.1]; joint pairs from the map
RESULT PASS (13 pass, 0 fail, 0 skip of 13 rows)

$ for f in 0089 0132 0148 0217 0254 0278; do idx=$((10#$f)); ffmpeg -y -loglevel error -i inputs/pose/stick.mp4 -i "run/before/render/dance@24fps/f${f}.png" -i "run/after/render/dance@24fps/f${f}.png" -filter_complex "[0:v]select=eq(n\\,${idx}),setpts=PTS-STARTPTS,scale=-1:512[s];[1:v]scale=-1:512:flags=neighbor[b];[2:v]scale=-1:512:flags=neighbor[a];[s][b][a]hstack=inputs=3" -frames:v 1 "run/evidence/after_f${f}.png"; done && python3 tools/grade.py --round R3 --geometry run/after/render/dance@24fps/geometry.json --sequence inputs/pose/sequence.json --report run/after/report.json --build run/after/build.log --folds run/after/render/dance@24fps/folds.json --passthrough run/after/render/dance@24fps/pass-through.json --map run/map.json --camera run/after/camera.json --trunk hip,chest,head > run/after/grade.txt 2>&1 && cat run/after/grade.txt && date -u +%Y-%m-%dT%H:%M:%SZ
PASS  hip-vertical    Hip vertical range: rig/sequence 1.049 (rig 0.1150, sequence 0.0997 leg lengths, median per-span width over 5 spans) [bar 0.85-1.15]
PASS  hip-horizontal  Hip horizontal range: rig/sequence 1.023 (rig 0.5239, sequence 0.4338 hip widths, median per-span width over 5 spans) [bar 0.85-1.15]
PASS  rebound         Rebound: median rig/sequence peak upward hip acceleration in the stance windows 1.334 over 2 windows [bar 0.7-1.43]
PASS  hip-tilt        Hip tilt: rig tilt range 54.769 deg = 1.000 of the sequence's 54.769 [bar >= 0.85], sign agrees (covariance +4.36e+04)
RESULT PASS (13 pass, 0 fail, 0 skip of 13 rows)

finished: 2026-10-19T00:08:08Z
