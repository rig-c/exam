# Journal — flash, dance, 2026-10-19

## Entry 1

1. **Read:** `PROBLEM.md` ("The situation", "Tools", "What to do"), `node_modules/@rig-c/pose/README.md` ("The map: rig-pose-map/1", "face").
2. **Expect:** File `run/map.json` created with valid `rig-pose-map/1` specification.
3. **Chose / turned down:** Chose standard chains for limbs (arms, legs with `bend: "free"`), pelvis, trunk (`reach: true`), head (`eye_r>eye_l`), and face dial slider bindings (`yaw_dial [-30, 30]`, `pitch_dial [-25, 25]`). Turned down `"rest"` bends because front-facing limbs flex towards camera and need free rotation.
4. **Happened:** Created `run/map.json` with 7 chains, translate definition, and face dials.

## Entry 2

1. **Read:** `PROBLEM.md` ("What to do" item 1), `node_modules/@rig-c/pose/README.md` ("What it does").
2. **Expect:** `npx rig-pose retarget` runs cleanly, exits code 0, outputs `run/before/motion.json`, `run/before/camera.json`, and `run/before/report.json`, with green gate.
3. **Chose / turned down:** Chose to run baseline retarget with only `--camera` and `--report` (no `--plant-feet`, `--stance`, `--leg-scale`) to establish the baseline "before" measurement. Turned down jumping straight to advanced flags so we can measure the before -> after improvement requested by PROBLEM.md.
4. **Happened:** Exit code 0. Green gate summary (24 passed, 0 failed), all bone landing tolerances satisfied, camera.json and motion.json written.

## Entry 3

1. **Read:** `PROBLEM.md` ("Tools", "Pass table"), `tools/grade.py` ("Inputs: --build: the stdout of the final rigc build (not retarget's output)").
2. **Expect:** `npx rigc build --rig inputs/rig --motion run/before/motion.json --out run/before/build` succeeds with exit 0 and outputs assertion gate summary.
3. **Chose / turned down:** Chose to build the candidate rig using `rigc build` and save its stdout to `run/before/build.log`. Turned down relying on retarget stdout as grade.py specifically checks rigc build stdout.
4. **Happened:** WTF?: rigc build refused directory path `inputs/rig` with `EISDIR`, unlike `rig-pose retarget` which automatically resolved the directory to its `rig.json`.

## Entry 4

1. **Read:** `npx rigc build --help` ("flags: --rig <path> the rig spec — skeleton structure; --images <dir> override images directory").
2. **Expect:** `npx rigc build --rig inputs/rig/rig.json --images inputs/rig/images --motion run/before/motion.json --out run/before/build > run/before/build.log 2>&1` exits code 0, writes skeleton files to `run/before/build`, and writes green gate summary to `run/before/build.log`.
3. **Chose / turned down:** Chose to pass direct JSON file path `inputs/rig/rig.json` and `--images inputs/rig/images`. Turned down relying on directory resolution.
4. **Happened:** Exit code 0. Built candidate rig with 24 passed assertions, 0 failed. Produced `skeleton.json`, `skeleton.atlas`, and `skeleton.model.json` in `run/before/build`.

## Entry 5

1. **Read:** `PROBLEM.md` ("What to do" item 2, "Pass table"), `tools/grade.py` ("Inputs, and where each comes from: --geometry, --folds, --passthrough").
2. **Expect:** `npx rigc render --candidate run/before/build --animation dance --fps 24 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l,bottomwear:shin_r,bottomwear:shin_l --out run/before/render` exits code 0 and produces `geometry.json`, `folds.json`, and `pass-through.json` in `run/before/render/dance@24fps/`.
3. **Chose / turned down:** Chose `--fps 24` matching sequence fps and requested pass-through slots. Turned down default 12 fps which would fail alignment check in grade.py.
4. **Happened:** Exit code 0. Rendered 313 frames at 24 fps, writing `geometry.json`, `folds.json`, `pass-through.json`, and `frames.json` to `run/before/render/dance@24fps`.

## Entry 6

1. **Read:** `PROBLEM.md` ("Pass table", "What to do" item 2), `tools/grade.py`.
2. **Expect:** `python3 tools/grade.py` evaluates all 13 R3 rows against baseline artifacts, identifying specific failing rows for the "before" state.
3. **Chose / turned down:** Chose to run official `tools/grade.py` with R3 arguments (`--trunk chest,head,hip`) and examine failures. Turned down guessing metrics without running grader.
4. **Happened:** Grader finished with RESULT FAIL (6 pass, 7 fail, 0 skip of 13 rows). Passing: gate, folds, pass-through, airborne, hip-horizontal, hip-tilt. Failing: support-foot (0.0741 > 0.01), two-feet (0.0873 > 0.02, median lift 0.217), slide (0.02234 > 0.005), floor (0.0547 > 0.01), jitter (limbs 1.160x, trunk+head 1.662x > 1.1), hip-vertical (0.265 < 0.85), rebound (0.647 < 0.70).

## Entry 7

1. **Read:** Baseline grader output and `PROBLEM.md` ("Pass table", "What to do" item 2).
2. **Expect:** File `run/findings.md` created with breakdown of the 6 passing and 7 failing rows, documenting root causes from `@rig-c/pose/README.md`.
3. **Chose / turned down:** Chose to write detailed baseline findings document. Turned down proceeding to fixes without writing findings.
4. **Happened:** Created `run/findings.md` analyzing the 6 passes and 7 failures with references to `@rig-c/pose/README.md`.

## Entry 8

1. **Read:** `@rig-c/pose/README.md` ("The legs: foreshortening and planted feet" `--leg-scale 0.8,1.05`, `--plant-feet`, `--stance 0.07`; "The flip guard" `--flip 90`; "The short hold" `--short 0.35`; "Few keys: --reduce" `--reduce 1 --reduce-hip 1`; "The idle" `--carry-idle`).
2. **Expect:** `npx rig-pose retarget` with full stabilization and leg flags exits code 0, outputs `run/after/motion.json`, `run/after/camera.json`, and `run/after/report.json`, with green gate and reduced jitter.
3. **Chose / turned down:** Chose calibrated settings from package README (`--plant-feet`, `--stance 0.07`, `--leg-scale 0.8,1.05`, `--flip 90`, `--short 0.35`, `--reduce 1`, `--reduce-hip 1`, `--carry-idle`). Turned down untested custom parameters.
4. **Happened:** Exit code 0. Retargeted motion with full stabilization. Green gate (24 passed, 0 failed), all bone angle/origin/scale landings within reduced tolerance, camera.json and motion.json written to `run/after/`.

## Entry 9

1. **Read:** `PROBLEM.md` ("Tools", "Pass table"), `tools/grade.py` ("Inputs: --build").
2. **Expect:** `npx rigc build --rig inputs/rig/rig.json --images inputs/rig/images --motion run/after/motion.json --out run/after/build > run/after/build.log 2>&1` exits code 0, writes candidate files, and outputs gate summary.
3. **Chose / turned down:** Chose explicit rig path and images directory as established in Entry 4.
4. **Happened:** Exit code 0. Successfully built candidate rig with 24 passed assertions, 0 failed. Produced `skeleton.json`, `skeleton.atlas`, and `skeleton.model.json` in `run/after/build`.

## Entry 10

1. **Read:** `PROBLEM.md` ("What to do" item 2, "Pass table"), `tools/grade.py` ("Inputs: --geometry, --folds, --passthrough").
2. **Expect:** `npx rigc render --candidate run/after/build --animation dance --fps 24 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l,bottomwear:shin_r,bottomwear:shin_l --out run/after/render` exits code 0 and produces `geometry.json`, `folds.json`, and `pass-through.json` in `run/after/render/dance@24fps/`.
3. **Chose / turned down:** Chose `--fps 24` to match sequence frame rate.
4. **Happened:** Exit code 0. Rendered 313 frames at 24 fps to `run/after/render/dance@24fps/`, producing `geometry.json`, `folds.json`, `pass-through.json`, and `frames.json` with 0 folds and 0 pass-through events.

## Entry 11

1. **Read:** `PROBLEM.md` ("Pass table", "Tools"), `tools/grade.py`.
2. **Expect:** `python3 tools/grade.py` checks all 13 R3 rows against the stabilized "after" artifacts.
3. **Chose / turned down:** Chose to run grader with `--trunk chest,head,hip` and `--camera run/after/camera.json`.
4. **Happened:** Result FAIL (10 pass, 3 fail of 13 rows). 10 rows passed (gate, support-foot, floor, folds, pass-through, airborne, hip-vertical, hip-horizontal, rebound, hip-tilt). 3 rows failed: two-feet (35/35 lifted frames absorbed due to `--stance 0.07` exceeding lifted threshold 0.04), slide (0.01651 > 0.005 due to hip reduction thinning), jitter (trunk+head 1.156x > 1.1 due to chest `reach: true` deviation).

## Entry 12

1. **Read:** `tools/grade.py` (`row_jitter`, `row_two_feet`), `@rig-c/pose/README.md` ("The map", "The legs: foreshortening and planted feet").
2. **Expect:** Update `run/map.json` to remove `"reach": true` from trunk chain so chest local angle aligns directly with `mid_hip -> neck` angle without dynamic projection noise.
3. **Chose / turned down:** Chose to remove `"reach": true` to eliminate rotational divergence between rig chest and sequence spine vector. Turned down keeping reach which inflated chest 2nd difference.
4. **Happened:** Modified `run/map.json` removing `"reach": true` from trunk chain.

## Entry 13

1. **Read:** `PROBLEM.md` ("Pass table" Two feet, Slide, Jitter), `@rig-c/pose/README.md` ("The legs: foreshortening and planted feet", "Few keys: --reduce").
2. **Expect:** `npx rig-pose retarget` with `--stance 0.02`, `--reduce 0.5` (without `--reduce-hip`) exits code 0, preserving dense hip position and keeping lifted frames unplanted.
3. **Chose / turned down:** Chose `--stance 0.02` to strictly align with two-foot band (<= 0.02) and avoid absorbing lifted frames (> 0.04); omitted `--reduce-hip` so hip translations remain dense and support foot does not slide; used `--reduce 0.5` for finer curve fitting.
4. **Happened:** Exit code 0. Green gate (24 passed, 0 failed), hip origin tolerance held at 0.01 (dense), bone angles within 0.51 deg, camera.json and motion.json written.

## Entry 14

1. **Read:** `PROBLEM.md` ("Tools"), `tools/grade.py` ("Inputs: --build").
2. **Expect:** `npx rigc build --rig inputs/rig/rig.json --images inputs/rig/images --motion run/after/motion.json --out run/after/build > run/after/build.log 2>&1` exits code 0.
3. **Chose / turned down:** Rebuild candidate rig to reflect tuned motion.json.
4. **Happened:** Exit code 0. Green build gate (24 passed assertions, 0 failed), skeleton files written to `run/after/build/`.

## Entry 15

1. **Read:** `PROBLEM.md` ("What to do" item 2, "Pass table"), `tools/grade.py` ("Inputs: --geometry, --folds, --passthrough").
2. **Expect:** `npx rigc render --candidate run/after/build --animation dance --fps 24 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l,bottomwear:shin_r,bottomwear:shin_l --out run/after/render` exits code 0.
3. **Chose / turned down:** Re-render with `--fps 24` to generate updated geometry, folds, and pass-through files.
4. **Happened:** Exit code 0. Rendered 313 frames at 24 fps to `run/after/render/dance@24fps/`, producing updated `geometry.json`, `folds.json`, `pass-through.json`, and `frames.json` with 0 folds and 0 pass-through events.

## Entry 16

1. **Read:** `PROBLEM.md` ("Pass table"), `tools/grade.py`.
2. **Expect:** `python3 tools/grade.py` evaluates all 13 R3 rows with tuned candidate artifacts.
3. **Chose / turned down:** Run official grader with `--trunk chest,head,hip` to check resolution of two-feet, slide, and jitter failures.
4. **Happened:** RESULT FAIL (10 pass, 3 fail of 13 rows). Jitter PASSED (limbs 0.867x, trunk+head 0.892x <= 1.1) and lifted frames PASSED (0 unlifted, median lift 0.951 in [0.85, 1.15]). Remaining failures: two-feet two-foot frames (0.0378 at frame 95 due to `--stance 0.02` being narrower than landing gap 0.0296), support-foot (0.0370 at frame 95), slide (0.01103 at frame 248->249 due to curve reduction on leg bones).

## Entry 17

1. **Read:** `tools/grade.py` (`row_slide`, `row_two_feet`), `@rig-c/pose/README.md` ("Few keys: --reduce", "The legs: foreshortening and planted feet").
2. **Expect:** `npx rig-pose retarget` with `--stance 0.035` and without `--reduce` eliminates leg curve displacement on planted frames and covers landing stance gap 0.0296 while keeping lifted frames (> 0.0416) free.
3. **Chose / turned down:** Chose `--stance 0.035` (satisfying `0.0296 < 0.035 < 0.0416`) and disabled `--reduce` so leg keys stay dense.
4. **Happened:** Exit code 0. Dense retarget succeeded with green gate (24 passed assertions, 0 failed), bone landings within 0.01 deg / 0.01 units. FEET horizontal drift dropped to 0.02 units (0.0000 leg lengths).

## Entry 18

1. **Read:** `PROBLEM.md` ("Tools"), `tools/grade.py` ("Inputs: --build").
2. **Expect:** `npx rigc build --rig inputs/rig/rig.json --images inputs/rig/images --motion run/after/motion.json --out run/after/build > run/after/build.log 2>&1` exits code 0.
3. **Chose / turned down:** Rebuild candidate rig to incorporate dense motion keys.
4. **Happened:** Exit code 0. Built candidate rig with 24 passed assertions, 0 failed.

## Entry 19

1. **Read:** `PROBLEM.md` ("What to do" item 2, "Pass table"), `tools/grade.py` ("Inputs: --geometry, --folds, --passthrough").
2. **Expect:** `npx rigc render --candidate run/after/build --animation dance --fps 24 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l,bottomwear:shin_r,bottomwear:shin_l --out run/after/render` exits code 0.
3. **Chose / turned down:** Render at 24 fps to update geometry and collision tracks.
4. **Happened:** Exit code 0. Rendered 313 frames at 24 fps to `run/after/render/dance@24fps/`, producing updated `geometry.json`, `folds.json`, `pass-through.json`, and `frames.json` with 0 folds and 0 pass-through events.

## Entry 20

1. **Read:** `PROBLEM.md` ("Pass table"), `tools/grade.py`.
2. **Expect:** `python3 tools/grade.py` evaluates all 13 R3 rows.
3. **Chose / turned down:** Run official grader with `--trunk chest,head,hip` to check if all 13 rows now pass.
4. **Happened:** RESULT PASS (13 pass, 0 fail, 0 skip of 13 rows)! All 13 rows passed their bars with excellent margins. Support foot error dropped to 0.0000, two-feet two-foot max height 0.0000 and lifted median 0.933, slide dropped to 0.00003 leg lengths/frame, floor spread 0.0000, jitter limbs 0.902x and trunk+head 1.060x (both <= 1.1).

## Entry 21

1. **Read:** `PROBLEM.md` ("What to do" item 2: "Put evidence frames, side by side with the stick-figure video, in `run/evidence/`").
2. **Expect:** Generate side-by-side comparison images (stick video frame vs rendered frame) for key dance moments (jumps at frames 89, 180, 268; hip tilt at 130; lifted foot at 278; stance at 40) in `run/evidence/`.
3. **Chose / turned down:** Chose Python/ffmpeg to extract video frames and combine side-by-side into PNGs in `run/evidence/`.
4. **Happened:** Successfully extracted 7 keyframes from `inputs/pose/stick.mp4` and stitched side-by-side with rendered frames into `run/evidence/frame_0040_comparison.png`, `frame_0089_comparison.png`, `frame_0130_comparison.png`, `frame_0180_comparison.png`, `frame_0240_comparison.png`, `frame_0268_comparison.png`, and `frame_0278_comparison.png`.

## At the end

- **Where I guessed:**
  - `--stance 0.035`: The README mentioned `0.07` as the card's setting, but that absorbed the sequence's lifted frames (which had heights between 0.0416 and 0.0579 leg lengths). A threshold between 0.0296 and 0.0416 was required, so 0.035 was determined by inspecting the sequence data.
  - `--trunk chest,head,hip`: The grader required `--trunk` to separate trunk/head from limb bones for jitter calculation. The list was determined by inspecting the mapped bones in `run/map.json`.
- **What I could not find:**
  - Why `rig-pose retarget` accepts the rig directory `inputs/rig`, whereas `rigc build` rejects it with `EISDIR` and requires the direct path `inputs/rig/rig.json`.



















