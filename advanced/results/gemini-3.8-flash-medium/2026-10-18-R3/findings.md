# Baseline Findings (R3 Dance)

Baseline run was conducted with `run/map.json` and basic flags (`--camera`, `--report`).
Result from grader: `RESULT FAIL (6 pass, 7 fail, 0 skip of 13 rows)`.

## 1. Passing Rows (6)

| Row | Measurement | Bar | Status |
| --- | --- | --- | --- |
| Gate | 52 assertions: 24 measured, 0 failed; 14/14 landings within tolerance | green | PASS |
| Folds | 0 frames fold over 6 mesh(es) | 0 | PASS |
| Pass-through | bottomwear:thigh_r, thigh_l, shin_r, shin_l: 0 of 313 frames | 0 | PASS |
| Airborne | 3 spans (88–91, 179–181, 267–269), 0 frames below floor, min peak 0.0835 > 0.01 | 3 spans, peaks > 0.01 | PASS |
| Hip horizontal range | rig/sequence 1.094 (rig 0.5355, seq 0.4338 hip widths) | 0.85–1.15 | PASS |
| Hip tilt | rig tilt range 54.769 deg = 1.000 of seq, covariance +4.36e+04 | >= 0.85, cov > 0 | PASS |

## 2. Failing Rows (7) and Root Cause Analysis

### 1) Support foot (FAIL)
- **Measurement:** max |lower foot - floor| 0.0741 leg lengths at frame 137 [bar <= 0.01]
- **Cause:** Baseline retarget does not lock the supporting foot to the ground without `--plant-feet`.

### 2) Two feet (FAIL)
- **Measurement:** two-foot frames max height diff 0.0873 [bar <= 0.02]; lifted frames: 2 of 35 within 0.01, median lift 0.217 [bar 0.85–1.15]
- **Cause:** Free foot height floats when both feet should touch the floor. `--stance` is required to stretch/plant the second foot when near floor height.

### 3) Slide (FAIL)
- **Measurement:** max support-foot move 0.02234 leg lengths/frame [bar <= 0.005]
- **Cause:** Without `--plant-feet`, the support foot drifts horizontally with raw detector noise and camera pan.

### 4) Floor (FAIL)
- **Measurement:** per-support-span floor spread 0.0547 leg lengths over 5 spans [bar <= 0.01]
- **Cause:** Different support spans have different perceived floor heights without `--plant-feet`'s single-floor derivation (`#85`).

### 5) Jitter (FAIL)
- **Measurement:** limbs 1.160x sequence (2.020 vs 1.741 deg/f^2), trunk+head 1.662x sequence (2.762 vs 1.662 deg/f^2) [bar <= 1.1]
- **Cause:** Raw dense keys inherit detector jitter, especially across the trunk/head coupling and fast limb movements. Keyframe reduction (`--reduce <deg>`), flip guard (`--flip 90`), and short hold (`--short 0.35`) are designed to address this.

### 6) Hip vertical range (FAIL)
- **Measurement:** rig/sequence 0.265 (rig 0.0242, sequence 0.0997 leg lengths) [bar 0.85–1.15]
- **Cause:** Rigid leg bones cannot bend toward the camera in 2D without shortening the apparent leg length. Without `--leg-scale <min,max>`, the hip cannot drop during crouching or steps without lifting the feet off the ground.

### 7) Rebound (FAIL)
- **Measurement:** median rig/sequence peak upward hip acceleration in stance windows 0.647 [bar 0.70–1.43]
- **Cause:** Without leg scaling and foot planting, hip vertical acceleration at the bottom of the bounce is muted (0.647 vs bar >= 0.70). Once `--plant-feet` and `--leg-scale` are active, the hip movement matches the physical bounce dynamics.
