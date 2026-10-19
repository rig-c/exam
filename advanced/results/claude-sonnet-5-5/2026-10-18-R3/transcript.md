started: 2026-10-18T22:28:08Z
$ cd run/after; ../../node_modules/.bin/rig-pose retarget --rig ../../inputs/rig --map map.json --pose ../../inputs/pose/sequence.json --out motion.json --name dance --plant-feet --leg-scale 0.8,1.05 --stance 0.07 --camera camera.json --report report.json --build build --render render
(tail: gate green, wrote camera.json, motion.json)
$ cd run/after; ../../node_modules/.bin/rigc build --rig ../../inputs/rig/rig.json --motion motion.json --out rbuild > build.txt
rigc: wrote run/after/rbuild/skeleton.atlas
rigc: wrote run/after/rbuild/skeleton.model.json
rigc: look at it: rigc render --candidate run/after/rbuild
$ ../../node_modules/.bin/rigc render --candidate rbuild --animation dance --fps 24 --max 256 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l,bottomwear:shin_r,bottomwear:shin_l --out rrender > render.txt
  ..    pass     "dance": cloth "bottomwear" over leg "thigh_l" passes through on 0 of 313 frame(s) read at 24 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0489) on its left side
  ..    pass     "dance": cloth "bottomwear" over leg "shin_r" passes through on 0 of 313 frame(s) read at 24 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0489) on its left side
  ..    pass     "dance": cloth "bottomwear" over leg "shin_l" passes through on 0 of 313 frame(s) read at 24 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0489) on its left side
rigc: wrote run/after/rrender/frames.json
$ python3 ../../tools/grade.py --round R3 --geometry rrender/dance@24fps/geometry.json --sequence ../../inputs/pose/sequence.json --report report.json --build build.txt --folds rrender/dance@24fps/folds.json --passthrough render.txt --camera camera.json --map map.json --trunk chest,head,hip --feet leg_r1,leg_l1 --hip hip
$ python3 ../../tools/grade.py --round R3 --geometry rrender/dance@24fps/geometry.json --sequence ../../inputs/pose/sequence.json --report report.json --build build.txt --folds rrender/dance@24fps/folds.json --passthrough render.txt --camera camera.json --map map.json --trunk hip,chest,head
$ ../pipe.sh (script: retarget --plant-feet --camera + rigc build + rigc render + grade); run per experiment with extra flags
$ ../pipe.sh --leg-scale 0.8,1.05 --stance 0.03  -> 12 pass 1 fail (jitter)
$ ../pipe.sh --leg-scale 0.8,1.05 --stance 0.03 --reduce {1,0.5,0.25} -> slide FAIL(0.0165,0.011) / PASS; jitter limbs 1.04/1.105/1.134 trunk 1.154/1.344/1.492
$ ../pipe.sh --leg-scale 0.8,1.05 --stance 0.03 (map without reach) ; final grade: RESULT PASS (13 pass)
finished: 2026-10-18T22:46:52Z
