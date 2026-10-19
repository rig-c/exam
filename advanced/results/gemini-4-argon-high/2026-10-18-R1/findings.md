# Findings — walk (Advanced R1)

## 1. Baseline ("Before") Measurement Summary

With the sequence (`inputs/pose/sequence.json`, 224 frames at 30 fps, 7 cycles of 32 frames, `"travel": "in-place"`) retargeted onto `inputs/rig/rig.json` using default `rig-pose retarget` flags (no `--plant-feet`, `--stance`, or `--leg-scale`) and the initial map (`run/map.json`, where `head` carried the eye line `r_eye -> l_eye`), `tools/grade.py --round R1` reported **4 PASS, 5 FAIL, 0 SKIP**:

- **PASS `gate`**: Build green (`52 assertions: 21 measured, 0 failed`), `11/11` landings within tolerance.
- **FAIL `support-foot`**: `max |lower foot - floor| 0.0608 leg lengths at frame 183 over 224 grounded frames (floor 137.135 units) [bar <= 0.01]`
  - **Cause**: Without `--plant-feet`, `hip` follows `mid_hip`'s raw scaled translation while the rigid rig legs rotate around `hip`. Because the camera-facing walk foreshortens the legs differently from the 2D rig's fixed segment lengths, the lower ankle drifts vertically by up to `47.76` units (`0.0985` leg lengths range, `0.0608` leg lengths from the median floor `137.135`).
  - **Evidence**: `run/evidence/before_f0183.png` (and `run/evidence/compare_f0183.png`).
- **FAIL `two-feet`**: `two-foot frames: max height difference 0.0074 leg lengths at frame 203 over 35 [bar <= 0.02]; lifted frames (sequence ankles > 0.04 apart): 168 of 168 with the lifted foot within 0.01 of the support foot (lowest lift -0.0097 at frame 42) [bar 0]; median rig/sequence lift -0.010 [bar 0.85-1.15]`
  - **Cause**: Seen face-on, a lifted knee/ankle in a walk is foreshortened along the leg's axis in 2D (`r_knee -> r_ankle` drops to `0.4511` of its straight length at frame 6; `l_knee -> l_ankle` drops to `0.720`). Without `--leg-scale`, both rig legs remain at 100% setup length (`~485.09` units) pointing straight down, so the lifted foot never rises above the support foot (168 of 168 lifted frames fail, median lift ratio `-0.010`).
  - **Evidence**: `run/evidence/before_f0006.png` (right foot peak lift in sequence), `run/evidence/before_f0018.png` (left foot peak lift in sequence), `run/evidence/before_f0042.png` (worst negative lift `-0.0097` leg lengths), and `run/evidence/before_f0203.png` (two-foot frame).
- **FAIL `slide`**: `max |support-foot move - closure - sequence ankle move x report scale 1.77071| 0.01176 leg lengths/frame (foot_l, frame 1->2) over 152 steps (travel: in-place; feet.closure absent from the report: closure drift taken as 0) [bar <= 0.005]`
  - **Cause**: The sequence declares `"travel": "in-place"`. Without `--plant-feet`, the supporting foot is not anchored to its scaled reference ankle x-track and loop drift closure (`feet.closure`) is not applied (`node_modules/@rig-c/pose/README.md`, "## What it does" / "### The legs: foreshortening and planted feet", line 212).
- **PASS `floor`**: `per-cycle floor spread 0.0000 leg lengths over 7 cycles [bar <= 0.01]`
- **FAIL `jitter`**: `limbs 1.000x sequence (0.941 vs 0.941 deg/f^2, 8 bones) [bar <= 1.1], trunk+head 1.277x sequence (0.918 vs 0.719 deg/f^2, chest,head) [bar <= 1.1]; joint pairs from the map`
  - **Cause**: In `run/map.json`, `head` was mapped to `"joints": ["r_eye", "l_eye"], "aim": ["eye_r>eye_l"]`. Per `node_modules/@rig-c/pose/README.md` ("## What it does", line 110, issues `#111`, `#181`, `#190`, `#205`), when a head chain carries the eye line (`r_eye -> l_eye`), `retarget` extracts the eyes' detrended vertical nod against `neck`, clamps it to `±2%` of setup neck length (`clampedY`), and couples `+1.6°/unit` of `clampedY` into `head.rotate`. Because `grade.py`'s `row_jitter` compares `head`'s local rotation against the pure 2D angle of `head`'s mapped joint pair (`r_eye -> l_eye`), the added pitch-to-roll nod coupling inflates `trunk+head`'s mean second difference from `0.719` to `0.918 deg/f^2` (`1.277x > 1.1x`).
- **PASS `folds`**: `0 frames fold over 6 mesh(es) [bar 0]`
- **PASS `pass-through`**: `bottomwear:thigh_r 0 of 224 frames; bottomwear:thigh_l 0 of 224 frames [bar 0]`
- **FAIL `loop`**: `cycle 1 vs cycle 7: max keyed-bone angle difference 1.3809 deg (head, cycle frame 13) [bar <= 1.0], max hip/foot_l/foot_r world position difference 0.0000 leg lengths (hip, cycle frame 31) [bar <= 0.01]`
  - **Cause**: The same `r_eye -> l_eye` vertical nod coupling (`clampedY`) uses a finite non-periodic detrending window across the clip, producing a `1.3809°` boundary discrepancy on `head.rotate` at cycle frame 13 between cycle 1 (frames 0–31) and cycle 7 (frames 192–223), even though the input sequence is an exact 32-frame loop repeated 7 times.

## 2. Applied Fixes and Verification ("After")

1. **Planted feet and in-place loop closure (`--plant-feet`)**:
   - Anchored each support span onto one unified floor (`94.868` world units) and tracked the supporting ankle's scaled horizontal move with in-place loop closure (`drift -225.41` over 224 frames, `+1.01080` units/frame).
   - Fixed **`support-foot`** (`0.0608` -> `0.0000` leg lengths) and **`slide`** (`0.01176` -> `0.00002` leg lengths/frame).
2. **Leg foreshortening scale (`--leg-scale 0.45,1.05`) and two-foot stance (`--stance 0.03`)**:
   - Inspecting `legScale` in `report.json` showed `leg_r1` (`r_knee -> r_ankle`) foreshortens to `0.45108` of its straight length on lifted frames (frames 4–6 of each cycle). Setting `--leg-scale 0.45,1.05` allowed full foreshortening without clamping (`median rig/sequence lift 0.913`, lowest lift `0.0176 > 0.01`).
   - Setting `--stance 0.03` placed both the stance exit (`0.03 < 0.04`) and the `0.8×` hysteresis re-entry (`0.024 >= 0.02`) inside the `[0.02, 0.04]` band between two-foot and lifted frames, stretching the free leg to the floor on all 35 two-foot frames (`max height difference 0.0000` leg lengths).
   - Fixed **`two-feet`** (both two-foot and lifted-frame clauses).
3. **Ear-line head mapping (`run/after/map.json`: `"joints": ["r_ear", "l_ear"], "aim": ["eye_r>eye_l"]`)**:
   - Replaced `"joints": ["r_eye", "l_eye"]` with `"joints": ["r_ear", "l_ear"]` on the `head` chain so `head` tracks the sequence's horizontal head-roll line without triggering the `r_eye -> l_eye` `clampedY` nod coupling into `head.rotate`.
   - Fixed **`jitter`** (`trunk+head` `1.277x` -> `1.000x`, `limbs` `0.988x`) and **`loop`** (`max keyed-bone angle difference` `1.3809 deg` -> `0.0001 deg`, position difference `0.0000` leg lengths).
