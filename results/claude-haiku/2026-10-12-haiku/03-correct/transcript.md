# transcript (haiku, 03-correct, 2026-10-12)

$ npm ci
added 5 packages, and audited 6 packages in 1s
1 package is looking for funding
found 0 vulnerabilities
EXIT=0
$ write tasks/03-correct/config.json (key, seethrough, assemble.rig_scale)

$ rig-parts assemble --propose-plan ... (plan written into config.json assemble.plan / extend_below_crop)
plan: 21 entries, extend_below_crop: hair_front, hair_back; note: headwear kept full-run
EXIT=0
$ rig-parts assemble --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --config config.json --out work
rig-parts assemble: 22 part(s) on a 832x1216 rig (0.5 rig px per source px), seam rule near-white, projection rule core
  bottomwear  full:bottomwear  325x326 ... op= 75233 ... unproj=27513 drift=21999 ... seam=22338
pixels: opaque 310012 = visible 208962 + occluded 101050 (32.6%); taken from the painting 146975 (47.4%); visible but not projected 61967 (20.0%)
recomposite vs source: mean |d|=1.09, within 8: 97.9%, error px > 40: 6164, uncovered error px: 1726
uncovered holes (8-connected): 444, the largest 5 listed
wrote work/rig/parts.json, 22 PNG(s) in work/rig/parts, work/render/recomposite_rig.png, work/render/recomposite_error_rig.png
EXIT=0

$ rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out
[assemble] ... uncovered error px: 1726 ... wrote out/parts.json
[rig] rigc build --profile spine-html ... exit 0 ; 53 assertions 26 measured (26 passed, 0 failed)
[check] pack: skeleton.png 517x1348, 22 region(s) ...
[check] loop: max |d| 0 (0 required)
[check] seam: mean |d| 0.148 (<= 1.0), 2 px over 40
[check] TEXTURE_STRETCH: FAIL — worst slot hair_back, triangle 167, vertices 115 37 117, edge 37-117, frame 22, ratio 0.065; severity 15.338 (ceiling 1.926544)
[check] check: FAIL — 1 bar(s) not met; 9 of 9 bar(s) measured, 0 skipped
build: stopped at check; 1 bar(s) not met, so no loop was encoded and no artifact is reported
EXIT=1 (16 s)
$ edit tasks/03-correct/config.json: motion.tracks hairback_l amps made same sign as hairback_r (+0.6,+1.4,+2.4)
$ scratch build of the same change (e1.json, out in scratchpad): build PASS, check 9 of 9 PASS, TEXTURE_STRETCH severity 1.126
$ rigc render --folds on out/check/build -> 0 of 8 mesh(es) fold
$ cp tasks/03-correct/config.json runs/2026-10-12-haiku-03-correct/config.json (hand-in copy)
$ rig-parts propose --parts work/rig --source inputs/painting.png --out work --from-config config.json
wrote work/render/landmarks_config.png (+_head); 0 LINT line(s) over 8 mesh(es) and the hip; exit 0
$ rig-parts build --config config.json ... --out out   (first, unedited draft; this is the FAIL shown in entry 6)
check: FAIL — 1 bar(s) not met; TEXTURE_STRETCH hair_back triangle 167, ratio 0.065; exit 1
$ rigc render --candidate out/check/build --animation idle --folds --geometry (scratch out dir, draft build)
idle 41 frame(s) ... (0 of 8 mesh(es) fold); exit 0
$ rig-parts build ... (after the sign fix, checkout)   [same command as the task]
build: PASS; check: PASS; 9 of 9 bar(s) measured; exit 0
$ rigc render --candidate out/check/build --animation idle --folds --geometry (scratch out dir, fixed build)
idle 41 frame(s) ... (0 of 8 mesh(es) fold); exit 0
$ python3 grade.py runs/2026-10-12-haiku-03-correct
5 of 5 line(s) PASS (see final reply)
