started: 2026-10-18T22:07:50Z

$ npm install   (before started line was written; output tail: found 0 vulnerabilities)
$ cat > run/map.json  (trunk reach/head eye-line/arms free/legs free, translate hip)
$ ./pipeline.sh "--plant-feet --stance 0.07 --leg-scale 0.8,1.05"   # retarget -> rigc build -> rigc render --geometry --folds --pass-through
  retarget exit 0 (GATE green 52 assertions); build exit 0; render exit 0, pass-through 0/224 both
$ bash grade.sh
  RESULT FAIL (7 pass, 2 fail, 0 skip of 9 rows)  [two-feet, jitter]
$ ./pipeline.sh ...  (first try)  -> build exit 1: rigc compile error: cannot read .../inputs/rig: EISDIR (see rigc guide CE_COMPILE_JSON_READ_FAILED)
$ (edit pipeline.sh: rigc build --rig ../inputs/rig/rig.json)  -> retarget/build/render exit 0
$ ./pipeline.sh "--plant-feet --stance 0.07 --leg-scale 0.8,1.05" ; bash grade.sh  -> RESULT FAIL (7 pass, 2 fail)
$ ./pipeline.sh "--plant-feet --stance 0.03 --leg-scale 0.8,1.05" ; grade -> FAIL two-feet (lift ratio 0.676), jitter 1.390x
$ map.json translate.scale -> r_hip,r_knee / leg_r0,leg_r1 ; pipeline ; grade -> FAIL (jitter 2.224x), reverted
$ ./pipeline.sh "--plant-feet --stance 0.03 --leg-scale 0.45,1.05" ; grade -> RESULT FAIL (8 pass, 1 fail) [jitter 1.390x]
$ ./pipeline.sh "--plant-feet --stance 0.03 --leg-scale 0.3,1.1" ; grade -> same (8 pass, 1 fail)
$ map.json: removed "reach": true (kept map.reach.json) ; ./pipeline.sh "--plant-feet --stance 0.03 --leg-scale 0.45,1.05" ; bash grade.sh > after/grade.txt -> RESULT PASS (9 pass, 0 fail, 0 skip of 9 rows)
$ ffmpeg + PIL -> evidence/stick_vs_render.png (first try failed: -vsync unrecognised)
finished: 2026-10-18T22:15:11Z
