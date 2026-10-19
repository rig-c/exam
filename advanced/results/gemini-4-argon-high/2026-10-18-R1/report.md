# Report — walk (Advanced R1), argon

## 1. Pass Table: Before vs. After

- **Rig leg length ($L$)**: `485.0928` world units (setup pose mean of `leg_l0 -> foot_l` and `leg_r0 -> foot_r`; hip width `84.0000` units)
- **Sequence leg length ($L_s$)**: `426.70` picture px (95th percentile `hip -> ankle`, mean of sides)
- **Airborne spans**: `0` (`report.feet.jumps = []`, all 224 frames grounded)

| Measure | Bar | Before (`run/before/`) | After (`run/after/`) |
| --- | --- | --- | --- |
| **Gate** | green, every bone landed | **PASS** — build green (`52 assertions: 21 measured, 0 failed`); `11/11` landings within tolerance (worst `0.12` of tolerance) | **PASS** — build green (`52 assertions: 21 measured, 0 failed`); `17/17` landings within tolerance (worst `0.12` of tolerance) |
| **Support foot** | lower foot = floor ± `0.01` $L$ | **FAIL** — `max \|lower foot - floor\| 0.0608` leg lengths at frame 183 over 224 grounded frames (floor `137.135` units) | **PASS** — `max \|lower foot - floor\| 0.0000` leg lengths at frame 104 over 224 grounded frames (floor `94.868` units) |
| **Two feet** | two-foot frames ($\le 0.02 L_s$): rig feet $\le 0.02 L$; lifted frames ($> 0.04 L_s$): 0 within $0.01 L$ of support, median rig/seq lift `0.85–1.15` | **FAIL** — two-foot frames: max diff `0.0074` $L$ at frame 203 over 35; lifted frames: `168 of 168` within `0.01` $L$ of support (lowest lift `-0.0097` at frame 42); median rig/seq lift `-0.010` | **PASS** — two-foot frames: max diff `0.0000` $L$ at frame 203 over 35; lifted frames: `0 of 168` within `0.01` $L$ of support (lowest lift `0.0176` at frame 173); median rig/seq lift `0.913` |
| **Slide** | in-place: `\|support move - closure - seq ankle move × scale\|` $\le 0.005 L$/frame | **FAIL** — max `0.01176` leg lengths/frame (`foot_l`, frame `1->2`) over 152 steps (`feet.closure` absent, drift taken as 0) | **PASS** — max `0.00002` leg lengths/frame (`foot_l`, frame `7->8`) over 209 steps (`closure +1.01080` units/frame removed, `drift -225.41` over 224 frames) |
| **Floor** | per-cycle floor spread $\le 0.01 L$ | **PASS** — `0.0000` leg lengths over 7 cycles | **PASS** — `0.0000` leg lengths over 7 cycles |
| **Jitter** | mean \|2nd diff\| of local rotation $\le 1.1\times$ sequence (limbs and trunk+head each) | **FAIL** — `limbs 1.000x` (`0.941 vs 0.941 deg/f^2`, 8 bones), `trunk+head 1.277x` (`0.918 vs 0.719 deg/f^2`, `chest,head`) | **PASS** — `limbs 0.988x` (`0.929 vs 0.941 deg/f^2`, 8 bones), `trunk+head 1.000x` (`0.614 vs 0.614 deg/f^2`, `chest,head`) |
| **Folds** | `0`, with physics on | **PASS** — `0` frames fold over 6 meshes | **PASS** — `0` frames fold over 6 meshes |
| **Pass-through** | `bottomwear:thigh_r,bottomwear:thigh_l` `0` frames | **PASS** — `bottomwear:thigh_r 0 of 224 frames; bottomwear:thigh_l 0 of 224 frames` | **PASS** — `bottomwear:thigh_r 0 of 224 frames; bottomwear:thigh_l 0 of 224 frames` |
| **Loop** | cycle 1 vs cycle 7: keyed world angles $\le 1^\circ$, `hip`/`foot_l`/`foot_r` world pos $\le 0.01 L$ | **FAIL** — max keyed-bone angle diff `1.3809 deg` (`head`, cycle frame 13), max world pos diff `0.0000` leg lengths (`hip`, cycle frame 31) | **PASS** — max keyed-bone angle diff `0.0001 deg` (`sleeve_r1`, cycle frame 31), max world pos diff `0.0000` leg lengths (`foot_r`, cycle frame 31) |
| **Overall** | 9 of 9 rows PASS | **FAIL (4 pass, 5 fail, 0 skip)** | **PASS (9 pass, 0 fail, 0 skip)** |

---

## 2. What Was Fixed and Where We Found How

1. **Map structure (`translate.scale`, `aim`, and `"bend": "free"`)**:
   - **What**: Added `"scale": { "pose": ["mid_hip", "neck"], "rig": ["hip", "neck"] }` to `translate`, `"aim": ["neck"]` on `trunk`, `"aim": ["eye_r>eye_l"]` on `head`, and `"bend": "free"` on all four limb chains (`arm_r`, `arm_l`, `leg_r`, `leg_l`).
   - **Where found**: Refusal message `FAIL MAP_TRANSLATE_SCALE: run/map.json "translate" "scale" is undefined; it must be { pose: [joint, joint], rig: [bone, bone] }, the same length measured in each` and `node_modules/@rig-c/pose/README.md` (`## The map: rig-pose-map/1`, lines 299–320).
2. **Support foot, Floor, and In-place Slide (`--plant-feet`)**:
   - **What**: Passed `--plant-feet` to `rig-pose retarget`. Because `inputs/pose/sequence.json` declares `"travel": "in-place"`, `--plant-feet` moved all support spans onto a single floor (`y = 94.868` units), stretched the supporting leg within `[0.92, 1.08]` across 3-frame support hand-over blends so the support foot never leaves the floor (`0.0000` leg lengths), anchored each supporting foot to its scaled reference ankle horizontal track, and closed the hip's horizontal loop drift (`drift -225.41` units over 224 frames -> `+1.01080` units/frame), reducing slide to `0.00002` leg lengths/frame.
   - **Where found**: `node_modules/@rig-c/pose/README.md` (`### The legs: foreshortening and planted feet`, lines 207–216: `--plant-feet`, **In place** `#92`, and **One floor** `#85`).
3. **Two-foot frames and Lifted-foot frames (`--stance 0.03` and `--leg-scale 0.45,1.05`)**:
   - **What**: Passed `--stance 0.03` and `--leg-scale 0.45,1.05` to `rig-pose retarget`.
     - `--stance 0.03` stretches the free leg to the floor on two-foot frames (`max height difference 0.0000` leg lengths over all 35 two-foot frames). Choosing `0.03` ensures both the exit threshold (`0.03 < 0.04`) and the `0.8×` re-entry hysteresis threshold (`0.8 × 0.03 = 0.024 >= 0.02`) lie inside the `[0.02, 0.04]` band between two-foot and lifted frames.
     - `--leg-scale 0.45,1.05` scales each leg bone along its local `x` axis (`scalex`) by its 2D foreshortened length over its 95th-percentile straight length. After Entry 11 (`--leg-scale 0.6,1.05`) showed in `run/after/report.json` (`legScale[1]`) that `leg_r1` (`r_knee -> r_ankle`) foreshortens down to `0.45108` on frames 4–6 of each cycle, lowering the bound to `0.45,1.05` eliminated all clamping and achieved `0 of 168` lifted frames within `0.01` of support (lowest lift `0.0176`) and median rig/sequence lift `0.913` (`[bar 0.85-1.15]`).
   - **Where found**: `node_modules/@rig-c/pose/README.md` (`### The legs: foreshortening and planted feet`, lines 203–205 for `--leg-scale` and lines 217–218 for `--stance` and its `0.8×` hysteresis `#87`), plus `legScale` in `run/after/report.json`.
4. **Head Jitter and Loop Angle Seam (`run/after/map.json`: `"joints": ["r_ear", "l_ear"]` on `head`)**:
   - **What**: Changed the `head` chain's `joints` in `run/after/map.json` from `["r_eye", "l_eye"]` to `["r_ear", "l_ear"]` (keeping `"aim": ["eye_r>eye_l"]`).
   - **Where found**: `node_modules/@rig-c/pose/README.md` (`## What it does`, line 110, issues `#111`, `#181`, `#190`, `#205`) and `tools/grade.py` (`row_jitter`, lines 760–806; `row_loop`, lines 866–895). Line 110 documents that when a head chain carries `r_eye -> l_eye`, `retarget` couples the clamped detrended vertical nod (`clampedY`) into `head.rotate` at `+1.6°/unit`. Because the detrending window is non-periodic at the ends of the clip and adds vertical nod acceleration onto `head.rotate`, `r_eye -> l_eye` caused `trunk+head` jitter to read `1.277x` (`> 1.1x`) and cycle 1 vs. cycle 7 `head` angle to differ by `1.3809°` (`> 1.0°`) at cycle frame 13. Mapping `head` to `["r_ear", "l_ear"]` tracks the same horizontal head roll without triggering the `r_eye -> l_eye` nod coupling, bringing `trunk+head` jitter to `1.000x` (`0.614 vs 0.614 deg/f^2`) and loop angle difference to `0.0001°`.

---

## 3. What Could Not Be Fixed and Why

Every row in the R1 pass table (`9 of 9`) passed after the fixes above. No row remained failing or skipped.

---

## 4. What the Tools Should Have Done (`run/tools.md`)

1. **Eye-line head mapping couples non-periodic vertical nod into `head.rotate` and breaks `loop` and `jitter`**:
   - `rig-pose retarget` should wrap its vertical nod detrending window periodically when the input sequence is a loop (`cleaned.params.loop: true` or `"travel": "in-place"`), and either only couple `clampedY` into `face.pitch` when `face` is declared or provide a flag (and README note under `## The map: rig-pose-map/1`) so the recommended `r_eye -> l_eye` head chain does not fail `jitter` and `loop` out of the box.
2. **Leg foreshortening range is only reported after a run with `--leg-scale`**:
   - `rig-pose retarget` should always print each mapped leg segment's picture-to-straight ratio (`min`, `median`, `max`) in the `FEET` readout and `report.json` even when `--leg-scale` is off, so the user does not have to guess a lower bound first to discover that `leg_r1` reaches `0.4511`.
3. **CLI flag naming mismatch across tools for sequence and animation inputs**:
   - `rig-pose retarget` uses `--pose` and `--name` whereas `rigc render` uses `--animation` and `grade.py` uses `--sequence`. Accepting `--sequence` and `--animation` as aliases in `rig-pose retarget` would avoid an unnecessary CLI refusal on first invocation.

---

## 5. Summary Answers (`PROBLEM.md` § "Answer when you finish")

1. **Each row of the table: before → after figures**:
   - **Gate**: `PASS (52 assertions: 21 measured, 0 failed; 11/11 landings, worst 0.12 of tol)` → `PASS (52 assertions: 21 measured, 0 failed; 17/17 landings, worst 0.12 of tol)`
   - **Support foot**: `FAIL (max |lower foot - floor| 0.0608 leg lengths at frame 183, floor 137.135u)` → `PASS (max |lower foot - floor| 0.0000 leg lengths at frame 104, floor 94.868u)`
   - **Two feet**: `FAIL (two-foot max diff 0.0074 L at frame 203 over 35; lifted 168/168 within 0.01 L of support, lowest lift -0.0097 at frame 42; median rig/seq lift -0.010)` → `PASS (two-foot max diff 0.0000 L at frame 203 over 35; lifted 0/168 within 0.01 L of support, lowest lift 0.0176 at frame 173; median rig/seq lift 0.913)`
   - **Slide**: `FAIL (max 0.01176 leg lengths/frame on foot_l frame 1->2 over 152 steps; feet.closure absent)` → `PASS (max 0.00002 leg lengths/frame on foot_l frame 7->8 over 209 steps; closure +1.01080 u/frame removed, drift -225.41 over 224 frames)`
   - **Floor**: `PASS (per-cycle floor spread 0.0000 leg lengths over 7 cycles)` → `PASS (per-cycle floor spread 0.0000 leg lengths over 7 cycles)`
   - **Jitter**: `FAIL (limbs 1.000x: 0.941 vs 0.941 deg/f^2; trunk+head 1.277x: 0.918 vs 0.719 deg/f^2)` → `PASS (limbs 0.988x: 0.929 vs 0.941 deg/f^2; trunk+head 1.000x: 0.614 vs 0.614 deg/f^2)`
   - **Folds**: `PASS (0 frames fold over 6 meshes)` → `PASS (0 frames fold over 6 meshes)`
   - **Pass-through**: `PASS (bottomwear:thigh_r 0/224; bottomwear:thigh_l 0/224)` → `PASS (bottomwear:thigh_r 0/224; bottomwear:thigh_l 0/224)`
   - **Loop**: `FAIL (max keyed-bone angle diff 1.3809 deg on head at cycle frame 13; max world pos diff 0.0000 L)` → `PASS (max keyed-bone angle diff 0.0001 deg on sleeve_r1 at cycle frame 31; max world pos diff 0.0000 L)`
2. **What we fixed and where we found how**:
   - Authored `translate.scale`, `aim`, and `"bend": "free"` in `map.json` from the `MAP_TRANSLATE_SCALE` refusal message and `node_modules/@rig-c/pose/README.md` (`## The map: rig-pose-map/1`, lines 299–320).
   - Enabled `--plant-feet` to fix `support-foot` and in-place `slide` (`node_modules/@rig-c/pose/README.md`, `### The legs: foreshortening and planted feet`, lines 207–216).
   - Enabled `--stance 0.03` and `--leg-scale 0.45,1.05` to fix `two-feet` (`node_modules/@rig-c/pose/README.md`, `### The legs: foreshortening and planted feet`, lines 203–205 and 217–218; lower bound `0.45` read from `legScale[1].ratio.min = 0.45108` in `run/after/report.json`).
   - Changed `head.joints` from `["r_eye", "l_eye"]` to `["r_ear", "l_ear"]` in `run/after/map.json` to eliminate the `+1.6°/unit` `clampedY` vertical-nod coupling into `head.rotate` documented in `node_modules/@rig-c/pose/README.md` (`## What it does`, line 110) and verified against `tools/grade.py` (`row_jitter` and `row_loop`).
3. **Journal entries and `WTF?:` lines**:
   - **17** journal entries, **5** `WTF?:` lines (Entries 2, 3, 8, 9, 11).
4. **The three things that took the most time**:
   - Diagnosing why the `r_eye -> l_eye` head chain failed both `jitter` (`1.277x`) and `loop` (`1.3809°` at cycle frame 13) on an exact 32-frame loop and tracing it to the `clampedY` nod coupling in `node_modules/@rig-c/pose/README.md` line 110.
   - Reading the package documentation (`@rig-c/pose/README.md`, `rig-c/docs/AUTHORING.md`, `@rig-c/parts/docs/AUTHORING.md`, and `tools/grade.py`) to align the map schema, hysteresis deadband for `--stance`, and unscaled `legScale` bounds.
   - Extracting and compositing the side-by-side stick-figure / before / after evidence frames in `run/evidence/`.
5. **The entry titles in `tools.md`**:
   - `Eye-line head mapping couples non-periodic vertical nod into head.rotate and breaks loop and jitter`
   - `Leg foreshortening range is only reported after a run with --leg-scale`
   - `CLI flag naming mismatch across tools for sequence and animation inputs`

---

## 6. Verbatim Grader Output (Final Run)

```
grade R1
NOTE  airborne spans: report feet.jumps, 0 span(s)
NOTE  rig leg length 485.0928 units (setup pose, leg_l0->foot_l, leg_r0->foot_r); hip width 84.0000
NOTE  sequence leg length 426.70 (95th percentile hip->ankle, mean of sides, the sequence's own units); the sequence carries no camera
PASS  gate            Gate: build green (52 assertions: 21 measured, 0 failed); 17/17 landings within tolerance (worst at 0.12 of its tolerance)
PASS  support-foot    Support foot: max |lower foot - floor| 0.0000 leg lengths at frame 104 over 224 grounded frames (floor 94.868 units) [bar <= 0.01]
PASS  two-feet        Two feet: two-foot frames: max height difference 0.0000 leg lengths at frame 203 over 35 [bar <= 0.02]; lifted frames (sequence ankles > 0.04 apart): 0 of 168 with the lifted foot within 0.01 of the support foot (lowest lift 0.0176 at frame 173) [bar 0]; median rig/sequence lift 0.913 [bar 0.85-1.15]
PASS  slide           Slide: max |support-foot move - closure - sequence ankle move x report scale 1.77071| 0.00002 leg lengths/frame (foot_l, frame 7->8) over 209 steps (travel: in-place; closure +1.01080 units/frame removed (report feet.closure drift -225.41 over 224 frames)) [bar <= 0.005]
PASS  floor           Floor: per-cycle floor spread 0.0000 leg lengths over 7 cycles [bar <= 0.01, the support-foot band: the table gives this row no number of its own]
PASS  jitter          Jitter: limbs 0.988x sequence (0.929 vs 0.941 deg/f^2, 8 bones) [bar <= 1.1], trunk+head 1.000x sequence (0.614 vs 0.614 deg/f^2, chest,head) [bar <= 1.1]; joint pairs from the map
PASS  folds           Folds: 0 frames fold over 6 mesh(es) [bar 0]
PASS  pass-through    Pass-through: bottomwear:thigh_r 0 of 224 frames; bottomwear:thigh_l 0 of 224 frames [bar 0]
PASS  loop            Loop: cycle 1 vs cycle 7: max keyed-bone angle difference 0.0001 deg (sleeve_r1, cycle frame 31) [bar <= 1.0], max hip/foot_l/foot_r world position difference 0.0000 leg lengths (foot_r, cycle frame 31) [bar <= 0.01]
RESULT PASS (9 pass, 0 fail, 0 skip of 9 rows)
```
