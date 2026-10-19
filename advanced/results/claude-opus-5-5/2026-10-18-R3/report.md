# Report — Advanced R3 (dance), claude-opus-5-5

## Runs

| Run | Map | Retarget flags |
| --- | --- | --- |
| before (`run/before`) | trunk with `reach: true` (`before/map_v1_reconstructed.json`; the file was edited in place afterwards, so this copy is rebuilt, not byte-identical to the sha256 in `before/report.json`) | `--camera` only |
| v2 | trunk without `reach` | `--camera` |
| v3 | same | `--leg-scale 0.8,1.05 --plant-feet --stance 0.07 --camera` |
| after (`run/after` = v4) | same (`run/map.json`, copy in `after/map.json`) | `--leg-scale 0.8,1.05 --plant-feet --stance 0.03 --camera` |

Every run: `rig-pose retarget` → `rigc build --rig inputs/rig/rig.json --motion <motion>` (its stdout graded) → `rigc render --animation dance --fps 24 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l,bottomwear:shin_r,bottomwear:shin_l` → `grade.py --round R3 … --trunk hip,chest,head`. The rig spec and physics values were not changed.

## The table, before → after

| Row | Before | After | Bar |
| --- | --- | --- | --- |
| Gate | PASS, 14/14 landings | PASS, 20/20 landings (worst 0.17 of tolerance) | green |
| Support foot | FAIL 0.0741 | PASS 0.0000 | ≤ 0.01 |
| Two feet | FAIL two-foot 0.0873; lift ratio 0.217, 2/35 planted | PASS two-foot 0.0000; lift ratio 0.933, 0/35 planted | ≤ 0.02; 0.85–1.15 |
| Slide | FAIL 0.02234 | PASS 0.00003 | ≤ 0.005 |
| Floor | FAIL 0.0547 | PASS 0.0000 | ≤ 0.01 |
| Jitter | FAIL limbs 1.160×, trunk+head 1.664× | PASS limbs 0.989×, trunk+head 1.060× | ≤ 1.1 |
| Folds | PASS 0 | PASS 0 | 0 |
| Pass-through | PASS 0 | PASS 0 | 0 |
| Airborne | PASS 3 spans, min peak 0.0835 | PASS 3 spans (88–91, 179–181, 267–269), min peak 0.0245 | 3; > 0.01 |
| Hip vertical | FAIL 0.265 | PASS 1.049 | 0.85–1.15 |
| Hip horizontal | PASS 1.094 | PASS 1.023 | 0.85–1.15 |
| Rebound | FAIL 0.647 | PASS 1.334 | 0.7–1.43 |
| Hip tilt | PASS 1.000, sign agrees | PASS 1.000, sign agrees | ≥ 0.85, cov > 0 |

`after/camera.json`: rig-pose-camera/1, 313 entries, t = report frameTimes (grader NOTE).

## What I fixed and where I found how

1. **Jitter (trunk+head 1.664 → 1.060, limbs 1.160 → 0.989): removed `reach: true` from the trunk chain.** Found by breaking grade.py's jitter row down per bone: only `chest` and its children were off (chest 2.03×, head 2.28×, upper arms 1.7–1.9×); every other bone 1.000×. The @rig-c/pose README map bullet says `reach` aims the bone "from where its origin is posed — the hip moved and turned", and the pelvis chain turns `hip` by the measured hip line (54.8° of range), whose wobble swings the chest origin 100 units up. Cost: the POSTURE sway reads 1.268× the reference instead of 0.959×.
2. **Support foot, slide, floor, hip vertical, rebound: `--leg-scale 0.8,1.05 --plant-feet`.** README "The legs: foreshortening and planted feet" (`--plant-feet`, one floor #85; `--leg-scale` "0.8,1.05 is the card's range").
3. **Two feet: `--stance 0.03`, not the card's 0.07.** README `--stance` bullet: the tolerance is in "the free side's leg length — the leg length `FEET` uses" with a 0.8 release and a 0.1 s change. The report's `feet.legLength` (608.6 / 613.1 px) is the median, while the table's Ls is the 95th percentile (722.45). I converted the table's bands into FEET's unit (two-foot ≤ 0.0237, lifted > 0.047) and read the sequence: the only lifted frames are 278–312 (0.049–0.069), and 0.07 swallowed them all. 0.03 keeps two-foot frames planted and lets frame 272 (0.0301) start the lift.
4. Map choices that held from the start: a pelvis chain on `hip` (`r_hip → l_hip`, aim `leg_r0>leg_l0`) for the hip tilt row; arms and legs `bend: free` (README ⚠️ on front-facing elbows and `dance-b` knees); face yaw/pitch onto `yaw_dial`/`pitch_dial` with the sliders' own ranges ±30/±25.

## What I could not fix, and why

Nothing in the table is left failing. Left as is, outside the table:
- **Knee art shears under leg scaling** (report `shear`: leg_r1 3.39° at frame 184, leg_l1 5.15° at frame 95; seam visible in `evidence/frame_0295_stick_before_after.png`). A fix would be alternate shin art or `noScale` children; not attempted — the table does not read it and it would mean repainting.
- **Trunk sway 1.27× the reference** after dropping `reach`. Keeping `reach` and moving `chest_ctl`'s origin down onto the hip pivot in the rig spec might keep both, untried.
- **Rebound 1.334** sits near the 1.43 ceiling; the lowest jump peak (0.0245 leg lengths) is close to the 0.01 bar.

## What the tools should have done

- **retarget should warn when `reach` sits over a turning pelvis.** It knows the trunk chain has `reach`, that its translated bone carries a pelvis aim, and the lever (`PIVOT` already prints hip → thigh roots). A `POSTURE`-style line ("trunk reach re-aims chest by up to N° a frame from the pelvis tilt; its children carry it") would have saved the per-bone breakdown.
- **`--stance` should take the tolerance in the unit the user is graded in, or print both.** The STANCE line says "0.07 leg lengths" without saying FEET's leg length is the median hip → ankle, not the 95th-percentile straight length that `--leg-scale` and the table use. Two different "leg lengths" in one run, one name.
- ~~`--stance` should print the lifted frames it planted~~ — corrected: it did. v3's output has `STANCE planted both: free foot r frames 272–312 … up to 0.0687 leg lengths … within the tolerance 0.07`. I missed it because my own grep piped the lines through `head`, and saw only the first STANCE line. What the line still does not say is that a 0.0687 gap is a visibly lifted foot; a "the largest gap planted is N × the median" hint would have flagged it.
- **`rigc build --rig <dir>`** should accept the directory `rig-pose retarget --rig` accepts, or the failure should say "pass rig.json" instead of `EISDIR … CE_COMPILE_JSON_READ_FAILED`.
