started: 2026-10-18T21:56:33Z
$ npm install   # last lines: "found 0 vulnerabilities"
$ mkdir -p run/evidence run/after && write run/map.json (first map)
$ rig-pose retarget --rig inputs/rig/rig.json ...   # exit 1: "RIG_GATE_BASE … motion spec is red"
$ rig-pose retarget --rig inputs/rig --map run/map.json ... > run/after/retarget1.log   # exit 1: "566 problem(s) — nothing written" (POSE_BEND_ONE_WAY)
$ rig-pose retarget ... --bends clamp > run/after/retarget2.log   # exit 0; "wrote run/after/motion.json"
$ rig-pose retarget ... --report run/after/report.json ... > run/after/retarget3.log   # exit 0
$ rigc build --rig inputs/rig/rig.json --motion run/after/motion.json --out run/after/build --profile spine > run/after/build.stdout.txt   # exit 0; "rigc: wrote …skeleton.model.json"
$ rigc render --candidate run/after/build --animation dance --fps 24 --geometry --folds --pass-through … --out run/after/render > run/after/render.stdout.txt   # exit 0; "rigc: wrote …frames.json"
$ python3 tools/grade.py --round R3 … (no --cycle)   # baseline: RESULT FAIL (9 pass, 4 fail, 0 skip of 13 rows) → run/evidence/grade_before.txt
$ write run/map_v2.json (pelvis chain added)
$ run/pipe.sh run/v2 run/map_v2.json --plant-feet --stance 0.07 --flip 90 --short 0.35 --leg-scale 0.8,1.05 --reduce 0.5   # RESULT FAIL (11 pass, 2 fail)
$ run/pipe.sh run/v3 run/map_v2.json (no --stance)   # RESULT FAIL (10 pass, 3 fail)
$ run/pipe.sh run/st0.02 … --stance 0.02   # RESULT FAIL (10 pass, 3 fail)
$ run/pipe.sh run/st0.035 … --stance 0.035   # RESULT FAIL (12 pass, 1 fail)
$ run/pipe.sh run/nr run/map_v2.json --plant-feet --stance 0.035 --flip 90 --short 0.35 --leg-scale 0.8,1.05   # exit 0; RESULT PASS (13 pass, 0 fail, 0 skip of 13 rows)
$ cp run/nr/{map.json,motion.json,camera.json,report.json,build,build.stdout.txt,render} → run/after/ ; cp run/nr/grade.txt → run/evidence/grade_after.txt
$ ffmpeg -i inputs/pose/stick.mp4 (frames 0, 90, 180, 268) + hstack → run/evidence/side_by_side_*.png
$ python3 tools/grade.py … --report run/after/report.json … > run/evidence/grade_final_promoted.txt   # exit 0; RESULT PASS (13 pass, 0 fail, 0 skip of 13 rows)
$ grep -c "^## Entry" run/journal.md   # 6
$ grep -c "WTF?:" run/journal.md   # 2
finished: 2026-10-18T22:03:55Z
