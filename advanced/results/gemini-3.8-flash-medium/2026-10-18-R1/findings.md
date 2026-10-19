# Findings — walk (Advanced R1)

## 1. Executive Summary

The walk sequence (`inputs/pose/sequence.json`, 224 frames, 30 fps, 7 gait cycles) was retargeted onto the 2D rig (`inputs/rig/rig.json`). The initial baseline retarget passed 4 of 9 bars (gate, floor, folds, pass-through) but failed 5 bars (support-foot, two-feet, slide, jitter, loop). 

By diagnosing the underlying kinematic constraints and tool semantics, full compliance (9 of 9 bars PASS) was achieved using:
```sh
rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json \
  --out run/after/motion.json --name walk --report run/after/report.json \
  --plant-feet --leg-scale 0.45,1.05 --stance 0.02
```

## 2. Technical Findings

### Finding 1: Knee Foreshortening vs. Rigid Bone Kinematics
- **Symptom:** In baseline, the `two-feet` row failed with `median rig/sequence lift -0.010 [bar 0.85-1.15]` and 168 of 168 lifted frames failing to lift above the support foot band.
- **Root Cause:** In face-on walk sequences, the swing leg flexes forward toward the camera. In a 2D perspective projection, this appears as foreshortening rather than large rotational angles. Measuring `inputs/pose/sequence.json` revealed that while the thigh segments remain between 0.85 and 1.01 of straight length, the right shin (`r_knee` to `r_ankle`) compresses to 0.451 of its straight length. With rigid bones, `rig-pose` could not represent this compression, leaving both feet at nearly identical world heights on every frame.
- **Resolution:** Enabling `--leg-scale 0.45,1.05` allows scaling along each leg segment's x axis (`scalex` track). This faithfully lifted the swing foot, achieving a median rig/sequence lift ratio of 0.913 (comfortably within the 0.85–1.15 bar) and 0 lifted frames failing.

### Finding 2: In-Place Support Pinning and Loop Closure
- **Symptom:** In baseline, `support-foot` failed at 0.0608 leg lengths (bar <= 0.01), and `slide` failed at 0.01176 leg lengths/frame (bar <= 0.005).
- **Root Cause:** A walking motion in place carries continuous relative foot movement and horizontal camera drift. Without `--plant-feet`, the hip position was derived from mid_hip travel rather than grounded foot pinning. Consequently, supporting feet drifted across support spans and across gait cycles.
- **Resolution:** Enabling `--plant-feet` activated:
  1. Grounded ankle pinning to one unified floor line (floor = 94.868 units, max deviation 0.0000 leg lengths).
  2. In-place loop closure (`feet.closure`): -225.41 units of total horizontal drift across 224 frames were evenly compensated (+1.01080 units/frame), reducing slide deviation to 0.00002 leg lengths/frame.
  3. Adding `--stance 0.02` stretched free legs within the 0.02 leg length band to touch the floor on two-foot frames (max height difference 0.0000 leg lengths).

### Finding 3: `inPlace` Dependency and Head Nod Discontinuity
- **Symptom:** In baseline, `loop` failed with `max keyed-bone angle difference 1.3809 deg (head, cycle frame 13) [bar <= 1.0]`, and `jitter` failed on `trunk+head` with `1.277x sequence [bar <= 1.1]`.
- **Root Cause:** Inspection of `node_modules/@rig-c/pose/src/retarget.ts` (line 733 and lines 1320–1370) revealed an unexpected coupling:
  - `inPlace` is computed as `const inPlace = plantOn && opts.travel === TRAVEL_IN_PLACE;`.
  - When `--plant-feet` was omitted, `inPlace` became `false` despite the sequence declaring `"travel": "in-place"`.
  - With `inPlace === false`, `maxNod` became `0.02 * neckRestLen` instead of `Infinity`.
  - Vertical eye travel against the neck was smoothed with a non-wrapping sliding window (`nodBase`), creating asymmetric baseline offsets at the beginning (frame 0–15) versus the end (frame 200–223).
  - This clamped nod signal (`clampedY`) was coupled into `head.rotate` at `+1.6°/unit`, injecting 1.38° of artificial angular difference between cycle 1 (frame 13: -8.748°) and cycle 7 (frame 205: -10.129°), despite the input joint coordinates being identical.
- **Resolution:** Enabling `--plant-feet` satisfied `plantOn === true`, enabling `inPlace === true`. This set `maxNod = Infinity` (disabling the non-looping nod filter), eliminating the artificial rotation and restoring cycle-to-cycle head angle difference to 0.0001° and trunk+head jitter to 1.000x.

### Finding 4: CLI Argument Inconsistency
- **Symptom:** `rig-pose retarget --rig inputs/rig` succeeded, but `rigc build --rig inputs/rig` crashed with `EISDIR`.
- **Root Cause:** `rig-pose` resolves `--rig` either to a directory containing `rig.json` or directly to `rig.json`. Conversely, `rigc build` unconditionally attempts `fs.readFileSync` on the `--rig` argument without checking directory status or resolving to `rig.json`.
- **Resolution:** Always specify the explicit file path `inputs/rig/rig.json` when invoking `rigc build`.
