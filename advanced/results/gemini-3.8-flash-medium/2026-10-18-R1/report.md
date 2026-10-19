# Exam Report — Advanced R1 (walk)

## 1. Pass Table Before and After

| Measure | Bar | Before (Baseline) | After (Fix) | Result |
| :--- | :--- | :--- | :--- | :--- |
| **Gate** | green, every bone landed | PASS: build green (21 measured, 0 failed); 11/11 landings <= tol (worst 0.12) | PASS: build green (21 measured, 0 failed); 17/17 landings <= tol (worst 0.12) | **PASS** |
| **Support foot** | floor ± 0.01 L on non-airborne frames | FAIL: max \|lower foot - floor\| **0.0608 L** at f183 (floor 137.135u) | PASS: max \|lower foot - floor\| **0.0000 L** at f104 (floor 94.868u) | **PASS** |
| **Two feet** | two-foot <= 0.02 L; lifted > 0.01 L, median lift 0.85–1.15 | FAIL: two-foot 0.0074 L; lifted **168 of 168** within 0.01 L, median lift **-0.010** | PASS: two-foot **0.0000 L**; lifted **0 of 168** within 0.01 L, median lift **0.913** | **PASS** |
| **Slide** | move <= 0.005 L/frame (in-place adjusted) | FAIL: max move **0.01176 L/f** (foot_l, f1->2; closure absent) | PASS: max move **0.00002 L/f** (foot_l, f7->8; closure +1.01080u/f removed) | **PASS** |
| **Floor** | per-cycle floor spread <= 0.01 L | PASS: spread 0.0000 L over 7 cycles | PASS: spread 0.0000 L over 7 cycles | **PASS** |
| **Jitter** | limbs <= 1.1x, trunk+head <= 1.1x | FAIL: limbs 1.000x; trunk+head **1.277x** (0.918 vs 0.719 deg/f^2) | PASS: limbs **0.988x**; trunk+head **1.000x** (0.719 vs 0.719 deg/f^2) | **PASS** |
| **Folds** | 0 with physics on | PASS: 0 frames fold over 6 meshes | PASS: 0 frames fold over 6 meshes | **PASS** |
| **Pass-through** | bottomwear:thigh_r/l 0 frames | PASS: 0 of 224 frames | PASS: 0 of 224 frames | **PASS** |
| **Loop** | angle <= 1.0°, position <= 0.01 L | FAIL: angle **1.3809°** (head, f13); position 0.0000 L | PASS: angle **0.0001°** (sleeve_r1, f31); position **0.0000 L** | **PASS** |
| **Overall** | 9 PASS | **FAIL (4 PASS, 5 FAIL)** | **PASS (9 PASS, 0 FAIL)** | **PASS** |

## 2. What Was Fixed and Where Found

1. **Planted feet and in-place loop closure (`--plant-feet`)**:
   - **Fixed:** Support foot height error (0.0608 L -> 0.0000 L), horizontal slide error (0.01176 L/f -> 0.00002 L/f), and loop drift.
   - **Source:** `@rig-c/pose/README.md` § "The legs: foreshortening and planted feet" lines 207–216, and § "In place" line 212.
2. **Leg segment foreshortening scaling (`--leg-scale 0.45,1.05`)**:
   - **Fixed:** Lifted swing leg height in 2D perspective (lift ratio -0.010 -> 0.913, lifted frames failing bar 168 -> 0).
   - **Source:** `@rig-c/pose/README.md` § "The legs: foreshortening and planted feet" lines 201–205. The minimum scale 0.45 was derived by measuring the sequence's swing shin length ratio against its straight length.
3. **Stance adjustment on two-foot frames (`--stance 0.02`)**:
   - **Fixed:** Matched two-foot height difference to 0.0000 L.
   - **Source:** `@rig-c/pose/README.md` § line 217.
4. **Resolution of head nod asymmetry (`inPlace = true`)**:
   - **Fixed:** Head angular loop difference (1.3809° -> 0.0001°) and trunk+head jitter (1.277x -> 1.000x).
   - **Source:** `@rig-c/pose/src/retarget.ts` lines 733 and 1325. Activating `--plant-feet` satisfied `plantOn === true`, allowing `inPlace` to evaluate to true for `"travel": "in-place"`, disabling the boundary-clipped sliding window that polluted head rotation keys.

## 3. What Could Not Be Fixed and Why

Everything in the pass table was fully resolved (9 of 9 rows PASS). There were no unresolvable rows.

## 4. What the Tools Should Have Done

1. **CLI Path Resolution Consistency:** `rigc build --rig` should accept directory paths containing `rig.json` or suggest the file explicitly, matching `rig-pose retarget`.
2. **Explicit Diagnostics for in-place Sequences:** When a sequence declares `"travel": "in-place"`, `rig-pose retarget` should warn if `--plant-feet` is omitted, explaining that in-place loop closure and nod unconstraining are bypassed.
3. **Foreshortening Hints in Retarget Report:** `rig-pose retarget` should report observed segment compression ratios when limbs compress significantly past 0.8, recommending appropriate `--leg-scale` bounds.
