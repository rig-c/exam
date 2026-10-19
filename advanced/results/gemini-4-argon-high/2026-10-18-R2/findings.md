# Findings — Advanced R2 (run)

## 1. Inputs & Proportions

- **Sequence (`inputs/pose/sequence.json`):**
  - `spec`: `"rig-pose-sequence/1"`, 200 frames at 30 fps (`t = 0.0` to `6.633333s`), `"travel": "in-place"`, no `camera`.
  - 10 identical repetitions of a 20-frame running cycle (`0..19`, `20..39`, ..., `180..199`).
  - Already cleaned (`rig-pose-clean/1`, `loop: true`, `legs: 5`, `rest: 5`, jitter `17.06 -> 7.99 px/f^2`).
  - Sequence leg length (`Ls`, 95th percentile `hip -> ankle`, mean of sides): `399.28 px`.
  - Sequence standing shoulder width: `141.28 px`; sequence standing hip width: `82.51 px`; sequence median `mid_hip -> neck`: `202.13 px` (foreshortened by forward trunk lean during running).
- **Rig (`inputs/rig/rig.json`, `"wind_painting"`):**
  - Setup leg length (`L`, `leg_l0 -> foot_l` and `leg_r0 -> foot_r` mean): `485.0928 units`.
  - Setup hip width (`leg_r0` at `x = -42` to `leg_l0` at `x = +42`): `84.0000 units`.
  - Setup shoulder width (`sleeve_r0` at `x = -76` to `sleeve_l0` at `x = +76`): `152.0000 units`.
  - Setup torso length (`hip` at `y = 602` to `neck` at `y = 962`): `360.0000 units`.
  - Setup knee inner angles (`leg_r1.rotation = 0.179268°`, `leg_l1.rotation = 0.278852°`) are below `0.5°`, requiring `"bend": "free"` on limb chains.
  - Natural rig-to-sequence ratios:
    - Leg length ratio `L / Ls = 485.0928 / 399.28 = 1.2149 units/px` (`0.85–1.15` target band for `hip-vertical`: `[1.0327, 1.3972]`).
    - Hip width ratio `W_rig / W_seq = 84.0 / 82.51 = 1.0180 units/px` (`0.85–1.15` target band for `hip-horizontal`: `[0.8653, 1.1707]`).
    - Intersection of both scale bands: **`[1.0327, 1.1707] units/px`**.

## 2. Baseline ("Before") Failures

Running unflagged `rig-pose retarget` with the 6-chain baseline map (`run/before/map.json`) and `translate.scale` on `["mid_hip", "neck"]` / `["hip", "neck"]` gave `RESULT FAIL (6 pass, 7 fail, 1 skip of 14 rows)`:

1. **`support-foot` (FAIL, `0.0350` vs `<= 0.01`):** Without `--plant-feet`, the supporting foot is not held on a unified floor across grounded frames (`0–2`, `10–12` per cycle).
2. **`two-feet` (FAIL, median lift ratio `1.436` vs `0.85–1.15`):** Without `--leg-scale`, the rig's fixed-length 2D legs swing in the plane instead of foreshortening when the knee bends toward/away from the camera, exaggerating the vertical lift ratio to `1.436`.
3. **`slide` (SKIP, `no two consecutive grounded frames with sequence ankles`):** Without `--plant-feet`, `rig-pose retarget` ignores `"travel": "in-place"` when computing `feet.supports` and applies step-release (`r 1–199 -> the pose's travel, never re-planted`), leaving only single-frame support spans (`[0,0]`, `[2,2]`, `[22,22]`, ...) in `report.json`.
4. **`airborne` (FAIL, lowest foot `-0.0057` leg lengths at frame 143 vs `> 0.01`):** Without `--leg-scale`, the unscaled shin (`leg_r1` / `leg_l1`) extends straight down during flight and pokes below the floor line (`110.018 units`) on airborne frames even though the sequence's knee is flexed (`asked scalex = 0.089–0.491`).
5. **`hip-vertical` (`1.466`), `hip-horizontal` (`1.749`), and `rebound` (`1.466`):** Because `translate.scale` used `["mid_hip", "neck"]` / `["hip", "neck"]`, the foreshortened running torso (`202.13 px`) against the painting's long torso (`360.00 units`) produced `scale.factor = 1.78104 units/px`—far above both the leg-length ratio (`1.2149`) and the hip-width ratio (`1.0180`).
6. **`hip-tilt` (FAIL, `0.000 deg = 0.000x`):** The baseline map had no `pelvis` chain on `hip`, leaving `hip` rotation unkeyed (`0°`).

## 3. Fixes Applied ("After")

1. **Added `pelvis` chain (`run/after/map.json`):**
   - Added `{ "name": "pelvis", "bones": ["hip"], "joints": ["r_hip", "l_hip"], "aim": ["leg_r0>leg_l0"] }` (`@rig-c/pose/README.md`, "## The map: `rig-pose-map/1`").
   - Result: `hip-tilt` passed with `14.390 deg = 1.000` of the sequence's `14.390` and covariance `+3.66e+03`.
2. **Enabled `--plant-feet --stance 0.02 --leg-scale 0.5,1.0`:**
   - Planted support spans (`0–2`, `10–12` per cycle) onto a single floor (`122.026 units`), closed the in-place horizontal loop drift (`16.37 units` over 200 frames, `-0.08227 units/frame`), and foreshortened the thigh/shin links during knee flexion.
   - Result: `support-foot` (`0.0000`), `two-feet` (`1.116`), `slide` (`0.00003`), and `airborne` (`+0.0456` leg lengths above floor at frame 139) all passed.
3. **Switched `translate.scale` to the shoulder line (`run/after/map.json`):**
   - In Entry 6, keeping `translate.scale` on `["mid_hip", "neck"]` / `["hip", "neck"]` (`1.78104`) with `--plant-feet` still failed `hip-vertical` (`1.460`), `hip-horizontal` (`1.712`), `rebound` (`1.929`), and caused **16 frames of mesh folds in `bottomwear`** (triangles 110, 188, 189) because 14 of every 20 frames in the run cycle are airborne jump frames where `--plant-feet` releases the plant and moves `hip` by the pose's `mid_hip` travel multiplied by `scale.factor`.
   - Changing `translate.scale` to `{ "pose": ["r_shoulder", "l_shoulder"], "rig": ["sleeve_r0", "sleeve_l0"] }` (following `@rig-c/pose/README.md`: *"Pick a long segment that does not foreshorten much"*) set `scale.factor = 1.07585` (`152.00 / 141.28`), inside `[1.0327, 1.1707]`.
   - Result: `hip-vertical` dropped to `0.928`, `hip-horizontal` to `1.059`, `rebound` to `1.257`, and `folds` dropped from 16 frames to **`0 frames fold over 6 mesh(es)`**.
4. **Eliminated shin and foot art shear/squash (`run/after/rig/rig.json`):**
   - Under `--leg-scale 0.5,1.0`, `inputs/rig/rig.json`'s default `"normal"` inheritance on `leg_r1`/`leg_l1` and `"noRotationOrReflection"` on `foot_r`/`foot_l` caused `leg_r1`/`leg_l1` art to shear up to `12.09°`/`13.74°` and squashed `foot_r`/`foot_l` vertically to `0.500×` (sheared up to `30.93°`/`29.13°`).
   - Setting `"inherit": "noScale"` on `leg_r1` and `leg_l1` and `"inherit": "onlyTranslation"` on `foot_r` and `foot_l` (`@rig-c/pose/README.md` "### The legs: foreshortening and planted feet" and `@rig-c/parts/docs/AUTHORING.md` §3 `bones` row) reduced all six leg/foot `SHEAR` readings to `0.00°` and preserved the boots' full `1.000 × 1.000` setup dimensions across all 200 frames while keeping all 14 grader rows passing.
