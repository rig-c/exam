# Advanced R3 (`dance`) Retarget Report

## 1. Before / After Grader Table

| Row | Metric / Bar | Before (`run/before/`) | After (`run/after/`) | Status |
|---|---|---|---|---|
| `gate` | Build green (52 assertions) & landings within tolerance | PASS (`19/19` landings, worst `0.15`) | PASS (`20/20` landings, worst `0.15`) | PASS |
| `support-foot` | Max `\|lower foot - floor\| <= 0.01` leg lengths (299 grounded frames) | **FAIL** (`0.1456` at frame 132, floor `251.579`) | **PASS** (`0.0000` at frame 266, floor `216.292`) | Fixed |
| `two-feet` | Two-foot diff `<= 0.02`; 0/35 lifted frames `<= 0.01`; median lift `0.85–1.15` | **FAIL** (two-foot `0.1636` at f148; 2/35 lifted pinned at f278; lift `0.946`) | **PASS** (two-foot `0.0000` at f234; 0/35 lifted pinned, min `0.0390` at f278; lift `0.933`) | Fixed |
| `slide` | Max support-foot move `<= 0.005` leg lengths/frame (294 steps) | **FAIL** (`0.04570` on `foot_r`, f253→254) | **PASS** (`0.00003` on `foot_l`, f277→278) | Fixed |
| `floor` | Per-support-span floor spread `<= 0.01` leg lengths (5 spans) | **FAIL** (`0.0252` leg lengths) | **PASS** (`0.0000` leg lengths) | Fixed |
| `jitter` | Mean `\|d²θ/dt²\| <= 1.1x` sequence on limbs and trunk+head | **FAIL** (`limbs 1.000x`, `chest,head 1.201x`; `hip,chest,head 1.031x`) | **PASS** (`limbs 0.991x / 0.989x`, `trunk+head 1.000x` for both `chest,head` and `hip,chest,head`) | Fixed |
| `folds` | `0` frames fold over 6 meshes | PASS (`0` frames) | PASS (`0` frames) | PASS |
| `pass-through` | `0` of 313 frames across 4 `bottomwear:{thigh,shin}_{r,l}` pairs | PASS (`0` frames) | PASS (`0` frames) | PASS |
| `airborne` | 3 spans (`88–91, 179–181, 267–269`), 0 frames `<= floor`, peak `> 0.01` | **FAIL** (6/10 frames not above floor; peak `-0.0287` at f89) | **PASS** (0/10 frames not above floor; min peak `+0.0245` at f179) | Fixed |
| `hip-vertical` | Median per-span vertical hip range `rig/sequence` in `0.85–1.15` | **FAIL** (`0.371`: rig `0.0397`, seq `0.0997` leg lengths) | **PASS** (`1.049`: rig `0.1150`, seq `0.0997` leg lengths) | Fixed |
| `hip-horizontal` | Median per-span horizontal hip range `rig/sequence` in `0.85–1.15` | PASS (`0.982`: rig `0.4220`, seq `0.4338` hip widths) | PASS (`1.023`: rig `0.5239`, seq `0.4338` hip widths) | PASS |
| `rebound` | Median peak upward hip accel `rig/sequence` in `0.7–1.43` (2 stance windows) | **FAIL** (`0.380` over 2 windows) | **PASS** (`1.334` over 2 windows) | Fixed |
| `hip-tilt` | Rig pelvic tilt range `>= 0.85x` sequence (`54.769°`) with matching sign | **FAIL** (`0.000° = 0.000x`, covariance `+0.00e+00`) | **PASS** (`54.769° = 1.000x`, covariance `+4.36e+04`) | Fixed |
| **Total** | **13 rows** | **5 PASS, 8 FAIL** | **13 PASS, 0 FAIL, 0 SKIP** | **PASS** |

---

## 2. What Was Fixed and Where We Found How to Fix It

1. **Missing Pelvic Tilt (`hip-tilt`: `0.000x` → `1.000x`)**
   - **Where found:** `node_modules/@rig-c/pose/README.md` ("Posture: pelvic tilt and torso lean", lines 142–188) and `run/before/retarget.log` (`POSTURE hip tilt range: reference 54.8°, rig 0.0° — rig/reference 0.000`).
   - **Fix:** Added a `pelvis` chain to `run/map.json` (`{ "name": "pelvis", "bones": ["hip"], "joints": ["r_hip", "l_hip"], "aim": ["leg_r0>leg_l0"] }`). Because `leg_r0` (`x: -44, y: 15`) and `leg_l0` (`x: 48, y: 11`) sit on opposite sides of `hip` (`(0,0)`), the chord `leg_r0>leg_l0` rotates `hip` directly with `r_hip → l_hip`, reproducing the full `54.769°` pelvic tilt range (`1.000x`).

2. **Floating Support Foot, Foot Slide, Multi-Level Floor, Sunken Jumps, and Crushed Hip Travel/Rebound (`support-foot`, `two-feet`, `slide`, `floor`, `airborne`, `hip-vertical`, `rebound`)**
   - **Where found:** `node_modules/@rig-c/pose/README.md` ("The legs: foreshortening and planted feet", lines 201–220) and `tools/grade.py` (`BAR_TWO_FEET = 0.02`, `LIFT_FLOOR = 0.04`).
   - **Fix:** Passed `--plant-feet --stance 0.03 --leg-scale 0.68,1.1 --carry-idle` to `npx rig-pose retarget`:
     - `--plant-feet` and `--camera run/after/camera.json` infer a single world floor (`216.292` units), pin the supporting ankle horizontally and vertically across all 5 support spans (`support-foot 0.0000`, `floor 0.0000`, `slide 0.00003`), elevate all 3 jump spans (`88–91`, `179–181`, `267–269`) above the floor (`min peak airborne foot height 0.0245`), and restore full vertical hip travel (`1.049x`) and landing rebound (`1.334x`).
     - `--stance 0.03` sits cleanly between the grader's two-foot threshold (`0.02` sequence leg lengths) and lifted-foot threshold (`0.04` sequence leg lengths), so all 235 two-foot frames have both ankles planted at identical height (`0.0000` difference) while all 35 lifted frames in span `272–312` keep the lifted foot above the `0.01` band (lowest lift `0.0390` at frame 278, median lift ratio `0.933`).
     - `--leg-scale 0.68,1.1` accommodates the full foreshortening range of `dance` (`0.683..1.098`) without clamping.

3. **Trunk and Head Jitter (`jitter`: `1.201x` / `1.664x` → `1.000x` on `trunk+head`, `0.989x–0.991x` on `limbs`)**
   - **Where found:** `tools/grade.py` (`row_jitter` lines 778–798) and `node_modules/@rig-c/pose/src/retarget.js` (head vertical nod coupling on `r_eye`/`l_eye`).
   - **Fix:**
     - Kept `"trunk"` on direct angle aiming (`{ "name": "trunk", "bones": ["chest"], "joints": ["mid_hip", "neck"], "aim": ["neck"] }`, without `"reach": true`). Because `chest` is offset 100 units above `hip`, `"reach": true` caused `chest` to counter-rotate against every `hip` tilt (`1.664x` jitter); direct angle aiming matches `w_seq['chest'] - w_seq['hip']` (`1.000x`).
     - Mapped `"head"` to `{ "name": "head", "bones": ["head"], "joints": ["r_ear", "l_ear"], "aim": ["ear_r>ear_l"] }`. When `head` is mapped to `["r_eye", "l_eye"]`, `retarget.js` adds a vertical eye-nod coupling (`clampedY * +1.6°/unit`) into `head.rotate`, inflating `head`'s local second difference to `1.298x` of the 2D `r_eye -> l_eye` chord (`1.201x` for `--trunk chest,head`). Switching `head` to `r_ear -> l_ear` (`ear_r>ear_l`) aims `head` purely along the 2D ear chord, achieving `1.000x` jitter under both `--trunk chest,head` and `--trunk hip,chest,head`.

---

## 3. What Could Not Be Fixed and Why

Nothing remained unfixed: all 13 rows of `tools/grade.py --round R3` pass (`13 pass, 0 fail, 0 skip of 13 rows`, exit 0), with 0 mesh folds across all 6 deformed meshes and 0 pass-through frames across all 4 `bottomwear` limb pairs.

---

## 4. What the Tools Should Have Done

1. **`rig-pose retarget` should warn when `hip` tilt is `0.000` despite large reference pelvic tilt (`54.8°`) and when unplanted feet float/slide:** In the baseline run, `retarget` printed `GATE green` and treated `POSTURE hip tilt range ... rig/reference 0.000` and `FEET ... 0.1726 leg lengths` as passive notes rather than warnings.
2. **`rig-pose retarget --plant-feet` should report frame counts in the `[0.02, 0.04]` stance band or auto-select `--stance`:** The README's reference card suggests `--stance 0.07`, which pins lifted frames (`> 0.04` ankle separation) to the floor and fails `two-feet`. Reporting how `--stance` partitions frames relative to `0.02` and `0.04` would prevent blind tuning.
3. **`rig-pose retarget --reduce` should constrain support-ankle horizontal drift when `--plant-feet` is active:** Using `--reduce 1` thinned leg `rotate` curves while keeping `hip.translate` dense, introducing `0.01651` leg lengths/frame of support-foot slide between kept rotate keys.
4. **`rig-pose retarget` should make vertical head-nod coupling into `head.rotate` opt-in (or report it in `report.json`):** Coupling `clampedY * +1.6°/unit` into `head.rotate` whenever `head` maps `r_eye`/`l_eye` causes `head`'s local rotation to diverge from its 2D joint chord (`1.298x` jitter in `grade.py`).
