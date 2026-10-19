started: 2026-10-18T22:51:53Z

## npm install
```
npm install
1 package is looking for funding
found 0 vulnerabilities
```

## retarget (baseline)
```
npx rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --out run/after/motion.json --name run --plant-feet --leg-scale 0.8,1.05 --stance 0.07 --build run/after/build --report run/after/report.json > run/after/retarget.txt
exit 0
  FOLD   mesh "bottomwear" (slot "bottomwear") folds on 16 frame(s) at 30 fps: t=1.400, …
  wrote run/after/motion.json — animations: idle, run
```
## rigc build (first try)
```
npx rigc build --rig ../../inputs/rig --motion motion.json --out build   (cwd run/after)
exit 1
rigc compile error: cannot read …/inputs/rig: EISDIR: illegal operation on a directory, read (see rigc guide CE_COMPILE_JSON_READ_FAILED)
```
## rigc build + render (baseline)
```
npx rigc build --rig ../../inputs/rig/rig.json --motion motion.json --out build > build.txt   (cwd run/after)
exit 0
rigc: look at it: rigc render --candidate …/run/after/build
npx rigc render --candidate build --animation run --fps 30 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l --out render
exit 0
  ..    run              200 frame(s), 6.633s + contact.png + geometry.json + folds.json (1 of 6 mesh(es) fold) + pass-through.json (0 of 2 pair(s) pass through)
```
## grade (baseline) — run/after/grade0.txt
```
python3 tools/grade.py --round R2 --geometry run/after/render/run@30fps/geometry.json --sequence inputs/pose/sequence.json --report run/after/report.json --build run/after/build.txt --folds run/after/render/run@30fps/folds.json --passthrough run/after/render/run@30fps/pass-through.json --map run/map.json --cycle 20 --feet foot_l,foot_r --hip hip --trunk hip,chest,head
RESULT FAIL (8 pass, 6 fail, 0 skip of 14 rows)
```

## try_leg (scale on r_hip→r_ankle / leg_r0→foot_r)
```
run/pipeline.sh run/try_leg run/map_leg.json inputs/rig/rig.json --plant-feet --leg-scale 0.8,1.05 --stance 0.07
retarget exit 0
  SCALE  1.60049 rig units per picture px (rig 485.19 / pose median 303.15)
  FOLD   rigc render --folds at 30 fps: no mesh folds
build exit 0 / render exit 0 / grade exit 1
RESULT FAIL (9 pass, 5 fail, 0 skip of 14 rows)
```

## try_v4 (trunk without reach; scale on shoulder width)
```
run/pipeline.sh run/try_v4 run/map_v4.json inputs/rig/rig.json --plant-feet --leg-scale 0.8,1.05 --stance 0.07
retarget exit 0
  SCALE  1.07585 rig units per picture px (rig 152.00 / pose median 141.28)
  FOLD   rigc render --folds at 30 fps: no mesh folds
build exit 0 / render exit 0 / grade exit 1
FAIL  two-feet … median rig/sequence lift 1.294 [bar 0.85-1.15]
RESULT FAIL (13 pass, 1 fail, 0 skip of 14 rows)
```

## try_v5 (leg-scale floor 0.05)
```
run/pipeline.sh run/try_v5 run/map_v4.json inputs/rig/rig.json --plant-feet --leg-scale 0.05,1.05 --stance 0.07
retarget exit 0
  SCALE  1.07585 rig units per picture px (rig 152.00 / pose median 141.28)
  FOLD   rigc render --folds at 30 fps: no mesh folds
build exit 0 / render exit 0 / grade exit 0
RESULT PASS (14 pass, 0 fail, 0 skip of 14 rows)
```

## rig_v6 (feet inherit onlyTranslation) + try_v6
```
cp -r inputs/rig run/rig_v6 ; python edit: foot_r, foot_l "inherit": "onlyTranslation"
run/pipeline.sh run/try_v6 run/map_v4.json run/rig_v6/rig.json --plant-feet --leg-scale 0.05,1.05 --stance 0.07
retarget exit 0 / build exit 0 / render exit 0 / grade exit 0
  SHEAR  bone "foot_r": art sheared up to 0.00° …
RESULT PASS (14 pass, 0 fail, 0 skip of 14 rows)
python3 run/sheet.py run/try_v6/render/run@30fps run/evidence/sheet_v6_cycle2.png 40,42,…,58
```
## arrange
```
mv run/after run/before ; mv run/try_v6 run/after
```

## final grade — run/after/grade_final.txt
```
python3 tools/grade.py --round R2 --geometry run/after/render/run@30fps/geometry.json --sequence inputs/pose/sequence.json --report run/after/report.json --build run/after/build.txt --folds run/after/render/run@30fps/folds.json --passthrough run/after/render/run@30fps/pass-through.json --map run/map_v4.json --cycle 20 --feet foot_l,foot_r --hip hip --trunk hip,chest,head
exit 0
RESULT PASS (14 pass, 0 fail, 0 skip of 14 rows)
```
finished: 2026-10-18T23:00:37Z
