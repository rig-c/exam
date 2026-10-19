# Step 2 Findings — Baseline ("Before") Measurement

## 1. Baseline Pass Table (`run/before/grade.txt`)

Command:
```sh
python3 tools/grade.py --round R3 \
  --geometry run/before/render/dance@24fps/geometry.json \
  --sequence inputs/pose/sequence.json \
  --report run/before/report.json \
  --build run/before/build.log \
  --folds run/before/render/dance@24fps/folds.json \
  --passthrough run/before/render/dance@24fps/pass-through.json \
  --map run/map.json \
  --camera run/before/camera.json \
  --trunk chest,head
```

| Row | Status | Baseline Figure | Bar |
| --- | --- | --- | --- |
| `gate` | **PASS** | `build green (52 assertions: 24 measured, 0 failed); 13/13 landings within tolerance (worst at 0.14 of its tolerance)` | green, every bone landed |
| `support-foot` | **FAIL** | `max \|lower foot - floor\| 0.0615 leg lengths at frame 148 over 299 grounded frames (floor 141.094 units)` | `<= 0.01` leg lengths |
| `two-feet` | **FAIL** | `two-foot frames: max height difference 0.0624 leg lengths at frame 254 over 235 [bar <= 0.02]; lifted frames (sequence ankles > 0.04 apart): 35 of 35 with the lifted foot within 0.01 of the support foot (lowest lift 0.0027 at frame 278) [bar 0]; median rig/sequence lift 0.083 [bar 0.85-1.15]` | two-foot `<= 0.02`; lifted `0` within `0.01` of support, median ratio `0.85–1.15` |
| `slide` | **FAIL** | `max support-foot move 0.02205 leg lengths/frame (foot_r, frame 216->217) over 294 steps` | `<= 0.005` leg lengths/frame |
| `floor` | **FAIL** | `per-support-span floor spread 0.0434 leg lengths over 5 spans` | `<= 0.01` leg lengths |
| `jitter` | **FAIL** | `limbs 1.000x sequence (1.323 vs 1.323 deg/f^2, 8 bones) [bar <= 1.1], trunk+head 1.201x sequence (0.891 vs 0.742 deg/f^2, chest,head) [bar <= 1.1]` | `<= 1.1x` sequence on limbs and trunk+head |
| `folds` | **PASS** | `0 frames fold over 6 mesh(es)` | `0` |
| `pass-through` | **PASS** | `bottomwear:thigh_r 0 of 313; bottomwear:thigh_l 0 of 313; bottomwear:shin_r 0 of 313; bottomwear:shin_l 0 of 313` | `0` frames |
| `airborne` | **PASS** | `airborne spans 3 (88-91, 179-181, 267-269); 0 of 10 span frame(s) with a foot not above the floor; min peak airborne foot height 0.0804 leg lengths above the floor at frame 89` | `3` spans, `0` grounded frames, peak `> 0.01` |
| `hip-vertical` | **FAIL** | `rig/sequence 0.055 (rig 0.0069, sequence 0.0997 leg lengths, median per-span width over 5 spans)` | `0.85–1.15` |
| `hip-horizontal` | **PASS** | `rig/sequence 1.099 (rig 0.5351, sequence 0.4338 hip widths, median per-span width over 5 spans)` | `0.85–1.15` |
| `rebound` | **FAIL** | `median rig/sequence peak upward hip acceleration in the stance windows 0.647 over 2 windows` | `0.7–1.43` |
| `hip-tilt` | **FAIL** | `rig tilt range 0.000 deg = 0.000 of the sequence's 54.769 [bar >= 0.85], sign DISAGREES (covariance +0)` | `>= 0.85`, covariance `> 0` |

## 2. Root-Cause Diagnosis per Failing Row

1. **`support-foot` (0.0615 > 0.01), `slide` (0.02205 > 0.005), `floor` (0.0434 > 0.01):**
   - Without `--plant-feet`, `rig-pose retarget` drives `hip` directly from the 2D `mid_hip` trajectory (`translate.scale` using `mid_hip -> neck`). Because the knees bend toward the camera in 2D and camera depth residuals shift the ankles across spans, the unplanted lower foot floats and sinks by up to 0.0615 leg lengths (`before_f0148.png`), slides horizontally up to 0.02205 leg lengths/frame (`before_f0217.png`), and the 5 support spans sit at different floor heights (spread 0.0434 leg lengths).
   - **Fix:** Pass `--plant-feet` to `rig-pose retarget` (`node_modules/@rig-c/pose/README.md`, "The legs: foreshortening and planted feet").

2. **`two-feet` (0.0624 > 0.02 on two-foot frames; 35/35 lifted frames <= 0.01; lift ratio 0.083) & `hip-vertical` (0.055) & `rebound` (0.647):**
   - Without `--leg-scale <min,max>`, the rig's leg bones (`leg_r0`, `leg_r1`, `leg_l0`, `leg_l1`) have rigid setup lengths. When the dancer bends her knees toward the camera or lifts one foot while bending the knee in depth, the 2D segment foreshortens in the sequence, but the rigid rig legs stay at full length:
     - On two-foot frames (`before_f0254.png`), slight asymmetries or hip tilts leave the free foot up to 0.0624 leg lengths off the support foot (`--stance` is also absent).
     - On lifted frames (`before_f0278.png`), the lifted leg's knee bends toward the camera in the video so its ankle rises in 2D without swinging sideways; on a rigid-leg rig without `--leg-scale`, the unscaled lifted leg reaches all the way down to the floor (median rig/sequence lift 0.083, 35/35 frames within 0.01 of the support foot).
     - Over the 5 support spans, the rigid supporting leg prevents `hip` from dropping relative to the planted ankle during knee-bend bounces (`hip-vertical` ratio 0.055), and dampens the upward pelvis acceleration between jumps (`rebound` 0.647 < 0.70).
   - **Fix:** Enable `--leg-scale` (with a lower bound low enough to cover the sequence's deepest foreshortening) and `--stance` (with a tolerance around `0.02–0.03` so two-foot frames `<= 0.02` are planted both while lifted frames `> 0.04` remain lifted).

3. **`hip-tilt` (0.000 deg = 0.000 of 54.769):**
   - `run/map.json` did not include a `pelvis` chain on `hip`, so `hip.rotate` was never keyed and the thigh-root line (`leg_r0 -> leg_l0`) stayed flat at 0°.
   - **Fix:** Add `{ "name": "pelvis", "bones": ["hip"], "joints": ["r_hip", "l_hip"], "aim": ["leg_r0>leg_l0"] }` to `map.json` and update `trunk` to use `"reach": true` (`{ "name": "trunk", "bones": ["chest"], "joints": ["mid_hip", "mid_shoulder"], "aim": ["sleeve_r0+sleeve_l0"], "reach": true }`) as documented in `node_modules/@rig-c/pose/README.md` ("The map: `rig-pose-map/1`").

4. **`jitter` on `trunk+head` (1.201x sequence > 1.1):**
   - In `@rig-c/pose` 0.31.1, when `head` carries `r_eye -> l_eye`, `retarget` couples the clamped vertical head nod (`clampedY * +1.6°/unit`, issues `#190`/`#205`) into `head`'s `rotate` track on top of the 2D `r_eye -> l_eye` angle. However, `tools/grade.py` (`row_jitter`) compares `head`'s local rotation second-difference strictly against the raw 2D segment angle of the mapped joint pair (`r_eye -> l_eye` minus `chest`'s pair), so the extra nod-coupled rotation inflates `trunk+head` jitter to `1.201x`.
   - Furthermore, `@rig-c/pose/README.md` ("Few keys: `--reduce`", issue `#116`) states: *"When `--leg-scale` is active, each trunk bone (`chest` and `head`, not an ancestor of any scaled bone) has its kept knots and Bézier handles smoothed within `deg` of its dense world aim to minimise the mean absolute second difference of its evaluated local angle and its child's compensated local angle"*. We can test `--leg-scale` + `--reduce` (or mapping/aim adjustments) to bring `trunk+head` jitter well under `1.1x`.

## 3. Evidence Frames (`run/evidence/`)

- `before_f0089.png`: Frame 89 — Jump 1 peak (`airborne` span 88–91).
- `before_f0132.png`: Frame 132 — Hands behind head with hip sway/tilt (`hip-tilt` 0° on baseline rig vs tilted pelvis on stick figure).
- `before_f0148.png`: Frame 148 — Worst `support-foot` error (0.0615 leg lengths off the floor).
- `before_f0217.png`: Frame 217 — Worst `slide` step (`foot_r` moves 0.02205 leg lengths in one frame).
- `before_f0254.png`: Frame 254 — Worst `two-feet` height mismatch on a two-foot frame (0.0624 leg lengths).
- `before_f0278.png`: Frame 278 — Lifted-foot frame where the sequence lifts the right ankle (`> 0.04` Ls) but the rigid-leg baseline rig leaves both feet at the same height (`0.0027` L).
