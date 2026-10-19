# Journal — claude-sonnet-5-5, Advanced R3 dance, 2026-10-19

## Entry 1

1. **Read:** node_modules/@rig-c/pose/README.md "The map: rig-pose-map/1" (chains, aim, reach, bend free for front-facing, face block) and `rig-pose retarget --help`.
2. **Expect:** run/after/map.json that resolves against inputs/rig/rig.json (no MAP_* refusal).
3. **Chose / turned down:** chains arm_r/arm_l (sleeve_*), leg_r/leg_l (leg_*), pelvis (hip, aim leg_r0>leg_l0), trunk (chest, reach, aim sleeve shoulders midpoint), head (aim eye_r>eye_l), all bends free; translate hip from mid_hip scaled by mid_hip→neck; face yaw/pitch dials. Turned down a plain trunk without reach: README says tilted pelvis carries the chest sideways.
4. **Happened:** (filled below)
4. **Happened:** map resolved first time; retarget with --plant-feet --leg-scale 0.8,1.05 --stance 0.07 --camera camera.json wrote motion.json; gate green, all LAND within tolerance, 0 folds. Matched expectation. Next: rigc build + render --geometry/--folds/--pass-through, then grade.

## Entry 2

1. **Read:** `rigc build/render --help` (--geometry, --folds, --pass-through) and tools/grade.py usage (--feet default foot_l,foot_r, --trunk).
2. **Expect:** build.txt, geometry.json, folds.json, render.txt for the grader; a first grade with several rows failing.
3. **Chose / turned down:** graded with --feet leg_r1,leg_l1 first, thinking the ankle bone is the leg tip; turned down keeping that once seen wrong.
4. **Happened:** WTF?: with --feet leg_r1,leg_l1 support-foot read 0.1757 and slide 0.077; leg_l1's origin is the knee, not the ankle, and the grader's default foot_l,foot_r (origin at the ankle) is right. Re-graded with the default: 11 pass, 2 fail (two-feet: lifted foot flat on the floor because --stance 0.07 plants lifted feet; jitter limbs 1.150x, trunk+head 1.664x). This is the "before" figure set. Next: stance tighter, then jitter.

## Entry 3

1. **Read:** retarget README "--stance" (planted-both within tolerance; above it lifted) and the two-feet bar (lifted-frames are sequence ankles > 0.04 apart).
2. **Expect:** --stance 0.03 (under the 0.04 lifted band) frees the lifted feet; two-feet passes; jitter unchanged.
3. **Chose / turned down:** --stance 0.03 instead of dropping --stance (without it two-foot frames would float); instead of 0.07 (the README's "card" value), which plants lifted feet.
4. **Happened:** matched. 12 pass, 1 fail (jitter limbs 1.149x, trunk+head 1.664x). Next: --reduce (README says it smooths trunk bones to minimise 2nd difference when --leg-scale is on).

## Entry 4

1. **Read:** README "--reduce" and the grader's jitter row (rig local rotation vs the sequence's map-pair angle against the keyed parent).
2. **Expect:** --reduce lowers jitter but moves ankles (slide). Per-bone ratios (my script run/perbone.py, grader's own functions) show where jitter sits.
3. **Chose / turned down:** tried --reduce 1, 0.5, 0.25 (each ~2 min); turned down accepting it because the slide row fails at 1 and 0.5, and jitter still fails at 0.25.
4. **Happened:** reduce 1: slide 0.0165 FAIL, jitter limbs 1.04 trunk 1.15; 0.5: slide 0.011 FAIL, 1.105/1.344; 0.25: slide PASS, jitter 1.134/1.492 FAIL. One flag trades the two rows against each other. Per bone (dense): chest 2.03x, head 2.28x, upper arms 1.7-1.9x, the rest ~1.0. Chest is aimed with reach:true (aim from the posed hip origin), so its angle is not the pair's angle. Next: try reach false on the trunk.

## Entry 5

1. **Read:** README map section: `reach: true` aims the chest from the posed hip origin; the per-bone table above shows chest 2.03x with it.
2. **Expect:** without `reach` the chest angle equals the shoulder-pair angle, chest ratio ~1.0, jitter rows pass, other rows unchanged.
3. **Chose / turned down:** removed `reach` from the trunk chain; kept --reduce off (it fails slide). Turned down keeping reach because the README says tilted pelvis then carries the chest sideways, but no row measures that.
4. **Happened:** matched. 13 pass, 0 fail: jitter limbs 0.989x, trunk+head 1.060x; chest 1.0x. Next: evidence frames, report, tools.md, final grade.
