started: 2026-10-18T22:26:57Z

$ rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --out run/after/motion.json --name run --plant-feet --stance 0.07 --leg-scale 0.8,1.05 --report run/after/report.json --build run/after/build
(mkdir -p run/after run/evidence first)
... exit/last lines in run/after/retarget.out
FAIL  MAP_CHAIN_JOINTS: chain "leg_r" has 3 bone(s) and 3 joint(s); bone k carries the segment from joint k to joint k+1, so it needs 4
FAIL  MAP_CHAIN_JOINTS: chain "leg_l" has 3 bone(s) and 3 joint(s); bone k carries the segment from joint k to joint k+1, so it needs 4
rig-pose retarget: 2 problem(s) — nothing written

$ (map: legs 2 bones, foot dropped) rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --out run/after/motion.json --name run --plant-feet --stance 0.07 --leg-scale 0.8,1.05 --report run/after/report.json --build run/after/build
FAIL  MAP_CHAIN_JOINTS: chain "leg_r" has 3 bone(s) and 3 joint(s); bone k carries the segment from joint k to joint k+1, so it needs 4
FAIL  MAP_CHAIN_JOINTS: chain "leg_l" has 3 bone(s) and 3 joint(s); bone k carries the segment from joint k to joint k+1, so it needs 4
rig-pose retarget: 2 problem(s) — nothing written

$ (map: legs 2 bones, foot dropped) rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --out run/after/motion.json --name run --plant-feet --stance 0.07 --leg-scale 0.8,1.05 --report run/after/report.json --build run/after/build
  SHEAR  bone "leg_r0": art sheared up to 0.00° (frame 30); world x axis 0.800 … 1.050, y axis 1.000 … 1.000 of setup — a scaled bone, or one under it; a reading
  SHEAR  bone "leg_r1": art sheared up to 11.02° (frame 174); world x axis 0.800 … 1.036, y axis 0.933 … 1.001 of setup — a scaled bone, or one under it; a reading
  SHEAR  bone "leg_l0": art sheared up to 0.00° (frame 161); world x axis 0.800 … 0.949, y axis 1.000 … 1.000 of setup — a scaled bone, or one under it; a reading
  SHEAR  bone "leg_l1": art sheared up to 10.68° (frame 1); world x axis 0.800 … 0.980, y axis 0.818 … 1.000 of setup — a scaled bone, or one under it; a reading
  SHEAR  bone "foot_r": art sheared up to 7.22° (frame 173); world x axis 0.839 … 1.000, y axis 0.800 … 1.036 of setup — a scaled bone, or one under it; a reading
  SHEAR  bone "foot_l": art sheared up to 8.63° (frame 143); world x axis 0.801 … 1.000, y axis 0.804 … 0.980 of setup — a scaled bone, or one under it; a reading
  FOLD   mesh "bottomwear" (slot "bottomwear") folds on 16 frame(s) at 30 fps: t=1.400, 1.733, 2.067, 2.400, 2.733, 3.067, 3.400, 3.733, 4.067, 4.400, 4.733, 5.067, 5.400, 5.733, 6.067, 6.400
  wrote run/after/motion.json — animations: idle, run

(go.sh/rt.sh: build with 'rigc build --rig inputs/rig/rig.json --motion run/after/motion.json --out run/after/build', render --fps 30 --geometry --folds --pass-through, grade; final: PASS 14/14, see run/after/grade_final.txt)
finished: 2026-10-18T22:37:17Z
