# Advanced R3 (Dance) Retarget Report

## 1. Pass Table: Before and After Figures

| Measure | Bar | Before (Baseline) | After (Final) | Status |
| --- | --- | --- | --- | --- |
| Gate | green, every bone landed | 52 assertions: 24 measured, 0 failed; 14/14 landings within tolerance | 52 assertions: 24 measured, 0 failed; 20/20 landings within tolerance | PASS |
| Support foot | <= 0.01 leg lengths | 0.0741 leg lengths at frame 137 | 0.0000 leg lengths at frame 235 | PASS |
| Two feet | two-foot <= 0.02; lifted bar 0; ratio 0.85–1.15 | two-foot: 0.0873; lifted: 2/35 within 0.01; ratio: 0.217 | two-foot: 0.0000; lifted: 0/35 within 0.01; ratio: 0.933 | PASS |
| Slide | <= 0.005 leg lengths/frame | 0.02234 leg lengths/frame (frame 216->217) | 0.00003 leg lengths/frame (frame 277->278) | PASS |
| Floor | <= 0.01 leg lengths | 0.0547 leg lengths over 5 spans | 0.0000 leg lengths over 5 spans | PASS |
| Jitter | <= 1.1x sequence | limbs 1.160x, trunk+head 1.662x | limbs 0.902x, trunk+head 1.060x | PASS |
| Folds | 0, with physics on | 0 frames fold over 6 meshes | 0 frames fold over 6 meshes | PASS |
| Pass-through | 0 frames | 0 of 313 frames | 0 of 313 frames | PASS |
| Airborne | 3 spans, feet above floor, peak > 0.01 | 3 spans, 0 below floor, peak 0.0835 | 3 spans, 0 below floor, peak 0.0245 | PASS |
| Hip vertical range | 0.85–1.15 of sequence | 0.265 | 1.049 | PASS |
| Hip horizontal range | 0.85–1.15 of sequence | 1.094 | 1.023 | PASS |
| Rebound | 0.70–1.43 | 0.647 | 1.334 | PASS |
| Hip tilt | >= 85%, covariance > 0 | 100.0%, covariance +4.36e+04 | 100.0%, covariance +4.36e+04 | PASS |
| **Result** | **13 PASS** | **6 pass, 7 fail** | **13 pass, 0 fail** | **PASS** |

*Note on submission check:* `after/camera.json` verified present, `rig-pose-camera/1`, 313 entries matching report `frameTimes` (max difference 0.000000 s).

---

## 2. What Was Fixed and Where We Found How

1. **Foot Planting, Single Floor, and Slide Reduction (`--plant-feet`)**
   - **Fix:** Enabled `--plant-feet`.
   - **Source:** `@rig-c/pose/README.md` ("The legs: foreshortening and planted feet", lines 207–216).
   - **Effect:** Locked supporting feet to a uniform median ground plane (`#85`), eliminating per-span floor spread (from 0.0547 down to 0.0000) and preventing support foot drift.

2. **Leg Foreshortening & Hip Vertical Range / Rebound (`--leg-scale 0.8,1.05`)**
   - **Fix:** Added `--leg-scale 0.8,1.05`.
   - **Source:** `@rig-c/pose/README.md` ("The legs: foreshortening and planted feet", lines 201–204).
   - **Effect:** Allowed thigh and shin bones to scale along their local x-axes during knee bends, enabling the pelvis to sink properly. This lifted hip vertical range from 0.265 up to 1.049, and increased rebound acceleration ratio from 0.647 up to 1.334 (both well within the required bars).

3. **Stance Balancing on Two-Foot and Lifted Frames (`--stance 0.035`)**
   - **Fix:** Set `--stance 0.035`.
   - **Source:** `@rig-c/pose/README.md` ("The legs: foreshortening and planted feet", line 217; `tools/grade.py` lines 602–641).
   - **Effect:** The default recommendation of `0.07` in documentation absorbed subtle foot lifts in choreography (sequence lifted heights were 0.0416–0.0579). Choosing `0.035` covered the landing two-foot gap (0.0296) while preserving intentional foot lifts (> 0.0416), bringing two-foot difference to 0.0000 and lifted ratio to 0.933 (bar 0.85–1.15, with 0 unlifted frames).

4. **Trunk and Limb Jitter Reduction (removing `reach: true` from trunk)**
   - **Fix:** Removed `"reach": true` from the `trunk` chain in `map.json`.
   - **Source:** Inspection of `tools/grade.py` (`row_jitter` / `local_angle`), `@rig-c/pose/README.md` line 316.
   - **Effect:** `"reach": true` dynamically repointed `chest` based on moving `hip` origin, creating second-order angular acceleration not present in the sequence. Removing it aligned `chest` rotation directly to the sequence `mid_hip -> neck` angle, lowering trunk+head jitter from 1.662x down to 1.060x (<= 1.1x).

5. **Slide Prevention Across Blends (Omission of `--reduce` on leg bones)**
   - **Fix:** Omitted `--reduce` and `--reduce-hip`.
   - **Source:** Inspection of frame 64->65 coordinates in `run/after/render/dance@24fps/geometry.json` vs report landings.
   - **Effect:** Curve thinning from `--reduce` allowed ankle tolerance up to 11.8 units, causing 0.01651 leg lengths of support foot slide during stance transitions. Dense keys held support foot movement to 0.00003 leg lengths/frame (bar <= 0.005).

6. **Motion Smoothing and Artifact Guards (`--flip 90`, `--short 0.35`, `--carry-idle`)**
   - **Fix:** Enabled `--flip 90`, `--short 0.35`, `--carry-idle`.
   - **Source:** `@rig-c/pose/README.md` lines 182–198, lines 229–237.
   - **Effect:** Guarded against sudden rotational pops and carried idle breathing/sway tracks without interfering with dance performance.

---

## 3. What Could Not Be Fixed and Why

All 13 rows of the pass table were successfully brought to a **PASS** state.

The subtle trade-off investigated was between **keyframe reduction (`--reduce`)** and **support-foot sliding (`slide`)**:
- While `--reduce 1` compresses motion data significantly, the solver allows the ankle to wander within a widened tolerance (several units) on thinned frames. This causes rapid jumps (e.g. 0.0165 leg lengths/frame at blend boundaries) that violate the strict slide bar (<= 0.005).
- Retaining dense keys on leg bones and hip translation maintained absolute physical pinning on the floor (0.00003 leg lengths/frame) while still satisfying the jitter requirements without key reduction.

---

## 4. What the Tools Should Have Done

1. **Consistent Path Handling in CLI:**
   `rig-pose retarget --rig <path>` accepts a directory (`inputs/rig`) and resolves `rig.json` inside it. However, `rigc build --rig <path>` expects a direct file path and crashes with `EISDIR: illegal operation on a directory, read`. The toolchain should standardize CLI path resolution or provide actionable error messages.

2. **Decoupled Key Reduction for Planted Chains:**
   `--reduce` applies curve thinning across all mapped bones uniformly. An option like `--reduce-limbs` or automatic preservation of dense keys on planted/supporting legs would allow users to reduce file size and upper-body jitter without introducing support foot sliding.

3. **Choreography-Aware Stance Thresholding:**
   The documentation suggests `--stance 0.07`, but this is broader than the pass table's lifted-foot classification bar (0.04). The tool could warn when `--stance` exceeds the detection threshold of lifted steps or automatically adapt tolerance based on sequence lift distribution.
