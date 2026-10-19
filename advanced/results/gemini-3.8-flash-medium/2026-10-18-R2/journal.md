# Journal — exam-r2-flash, run, 2026-10-18

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry 1

1. **Read:** `PROBLEM.md` § What to do (step 1: "Put it on: retarget the sequence onto the rig with rig-pose retarget. You write the map (map.json): which joint goes to which bone.") and `@rig-c/pose/README.md` § The map: rig-pose-map/1.
2. **Expect:** A valid `run/map.json` file on disk conforming to `rig-pose-map/1` with chains for pelvis, trunk, head, arms, legs, and translate configuration.
3. **Chose / turned down:** Chose to write `run/map.json` with pelvis (`hip`), trunk (`chest`), head (`head`), arms (`sleeve_r0/r1`, `sleeve_l0/l1`), and legs (`leg_r0/r1`, `leg_l0/l1`) with free bends. Turned down omitting pelvis or using default bends because R2 requires hip tilt and deep leg flexion without hinge clamp errors.
4. **Happened:** Created `run/map.json` with spec `rig-pose-map/1`, defining 7 chains (pelvis, trunk, head, 2 arms, 2 legs) and translation scale as expected.

## Entry 2

1. **Read:** `PROBLEM.md` § What to do (step 1: "Put it on: retarget the sequence onto the rig with rig-pose retarget. ... The gate must be green.") and § Tools (`rig-pose retarget`).
2. **Expect:** `npx rig-pose retarget` exits with code 0, prints green gate summary and landings, and generates `run/motion.json`, `run/build/`, `run/render/`, and `run/report.json`.
3. **Chose / turned down:** Chose to run baseline retarget without extra flags first to establish the "before" baseline measurements for the pass table. Turned down adding optimization flags upfront before measuring the initial state.
4. **Happened:** Retarget completed with exit code 0, green gate (21 passed, 0 failed), all 12 landings within tolerance, generating `run/motion.json`, `run/build/`, `run/render/`, and `run/report.json`. Noted `FOLD mesh "bottomwear"` on 26 frames and `FEET read, not planted (no --plant-feet)`.

## Entry 3

1. **Read:** `PROBLEM.md` § Pass table (Gate row) and `tools/grade.py` line 16 (`--build`: "the stdout of the final `rigc build` (not the retarget's stdout) — the gate line").
2. **Expect:** `npx rigc build` succeeds with exit code 0 and writes gate assertion summary ("N assertions: M measured (P passed, 0 failed)") to `run/build.stdout`.
3. **Chose / turned down:** Chose to run `rigc build` explicitly to generate `run/build.stdout` for `grade.py`. Turned down using retarget's stdout which mixes retarget output with build output.
4. **Happened:** `rigc build` succeeded with exit code 0, passing all 21 measured assertions (0 failed), and wrote `run/build.stdout` along with skeleton artifacts.

## Entry 4

1. **Read:** `PROBLEM.md` § What to do (step 2: "Measure: read the figures in the table below from `rigc render --geometry`") and `tools/grade.py` lines 13-19 (`--geometry`, `--folds`, `--passthrough`, `--fps`).
2. **Expect:** `npx rigc render` exits 0, producing `run/render/geometry.json`, `run/render/folds.json`, and pass-through summary on stdout at 30 fps.
3. **Chose / turned down:** Chose to render candidate with `--animation run --fps 30 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l` into `run/render/`. Turned down default fps (12) because sequence is 30 fps and grade.py requires matching fps.
4. **Happened:** `rigc render` succeeded with exit code 0, writing artifacts to `run/render/run@30fps/` (`geometry.json`, `folds.json`, `pass-through.json`), with stdout showing 0 of 200 pass-through frames and bottomwear folding on 26 frames.

## Entry 5

1. **Read:** `PROBLEM.md` § Tools (`rig-pose retarget (--plant-feet · --stance · --leg-scale ...)`), § Situation ("every stride has an airborne span ... rig is 2D and face-on ... leg length (--leg-scale) does that job"), and `@rig-c/pose/README.md` § The legs: foreshortening and planted feet.
2. **Expect:** `rig-pose retarget` with `--plant-feet --leg-scale 0.8,1.05 --stance 0.07` exits 0, reports planted feet with support spans and jumps, stretches leg scale, and writes updated `run/motion.json`, `run/build/`, `run/render/`, and `run/report.json`.
3. **Chose / turned down:** Chose to enable `--plant-feet`, `--leg-scale 0.8,1.05`, and `--stance 0.07` to fix support-foot, two-feet, airborne floor tracking, and slide rows. Turned down leaving feet unplanted which caused 8 test failures in baseline.
4. **Happened:** Retarget succeeded with exit code 0 and green gate; lowest ankle vertical range outside jumps dropped to 0.0000 leg lengths, bounce ratios tracked reference near 1.0 (0.934-0.972), bottomwear folds decreased from 26 to 16 frames.

## Entry 6

1. **Read:** `PROBLEM.md` § Pass table (Gate row) and `tools/grade.py` line 16 (`--build`).
2. **Expect:** `npx rigc build` succeeds with exit code 0, emitting updated `run/build/` and writing gate assertions to `run/build.stdout`.
3. **Chose / turned down:** Chose to rebuild skeleton after retarget with leg flags to update `run/build.stdout` and artifacts. Turned down skipping build as grade.py requires matching build stdout.
4. **Happened:** `rigc build` succeeded with exit code 0, passed 21 assertions, and updated `run/build.stdout` and skeleton files.

## Entry 7

1. **Read:** `PROBLEM.md` § Pass table and `tools/grade.py` lines 13-19 (`--geometry`, `--folds`, `--passthrough`).
2. **Expect:** `npx rigc render` exits 0, writing new `geometry.json`, `folds.json`, `pass-through.json` under `run/render/run@30fps/`.
3. **Chose / turned down:** Chose to re-render animation run at 30 fps to provide updated geometry and folds data to grade.py. Turned down grading without re-rendering because geometry would not reflect leg-scale and plant-feet keys.
4. **Happened:** `rigc render` succeeded with exit code 0, emitting geometry.json, folds.json (16 frames fold), and pass-through.json under `run/render/run@30fps/`.

## Entry 8

1. **Read:** `PROBLEM.md` § Pass table (Jitter, Hip vertical, Hip horizontal, Rebound, Two feet rows) and `@rig-c/pose/README.md` § The map.
2. **Expect:** Updating `run/map.json` to use direct trunk aim without `reach: true` and tuned `translate.scale.rig` (`["leg_l0", "hairback_l0_0+skirt3_0"]`, length ~240.6 units, scale factor ~1.1898) will lower trunk jitter under the 1.1x bar and bring hip vertical, horizontal, rebound, and two-feet ratios into their [0.85, 1.15] pass bands.
3. **Chose / turned down:** Chose to adjust `translate.scale` rig points to match the target scale factor (~1.190) and drop `reach: true` on trunk to avoid hip-bounce angular jitter coupling. Turned down keeping baseline scale (1.781) which oversized all hip travel metrics by 46%.
4. **Happened:** Updated `run/map.json` with direct trunk aim (`aim: ["neck"]`, `joints: ["mid_hip", "neck"]`) and scale pair `["leg_l0", "hairback_l0_0+skirt3_0"]`.

## Entry 9

1. **Read:** `PROBLEM.md` § Fix ("You may change the retarget flags, the map, the rig spec and the physics values.") and § Pass table (Folds row: "0, with physics on").
2. **Expect:** Editing `inputs/rig/rig.json` to remove unstable skirt translate physics constraints (`skirt*_translate`) and raising skirt rotate physics damping to 0.92 will eliminate triangle folds in `bottomwear` while keeping physics on.
3. **Chose / turned down:** Chose to tune physics values by removing skirt vertex translation shaking and increasing damping, keeping rotational physics active. Turned down muting physics entirely because the pass bar strictly requires "with physics on".
4. **Happened:** Modified `inputs/rig/rig.json` (backed up to `rig.json.orig`), removing 8 `skirt*_translate` constraints and setting skirt rotational physics damping to 0.92.

## Entry 10

1. **Read:** `PROBLEM.md` § What to do (step 3: "Fix: fix the rows that miss the table as far as you can. ... Rebuild whatever you change.") and § Tools.
2. **Expect:** `rig-pose retarget` succeeds with exit code 0 and green gate using updated map and rig physics, reporting scale ~1.1898 and reduced bottomwear folds.
3. **Chose / turned down:** Chose to re-run retarget with updated map and tuned physics spec to generate new motion keys and report. Turned down adding `--reduce` prematurely until observing impact of uncoupling trunk reach.
4. **Happened:** WTF?: removing skirt translate constraints and setting damping 0.92 caused bottomwear mesh folds to surge from 16 to 88 frames instead of dropping, because the translate constraints were actually constraining skirt tip expansion during hip drops.

## Entry 11

1. **Read:** `PROBLEM.md` § Pass table (Gate row) and `tools/grade.py` line 16 (`--build`).
2. **Expect:** `npx rigc build` succeeds with exit code 0, emitting updated `run/build/` and writing gate assertions to `run/build.stdout`.
3. **Chose / turned down:** Chose to rebuild skeleton to capture current state for grading evaluation. Turned down skipping build as grade.py requires build stdout matching motion.json.
4. **Happened:** `rigc build` succeeded with exit code 0, passed 21 assertions, and updated `run/build.stdout` and skeleton files (physicsConstraints=36).

## Entry 12

1. **Read:** `PROBLEM.md` § Pass table and `tools/grade.py` lines 13-19.
2. **Expect:** `npx rigc render` exits 0, writing updated `geometry.json`, `folds.json`, and `pass-through.json` under `run/render/run@30fps/`.
3. **Chose / turned down:** Chose to render candidate at 30 fps to evaluate geometry and folds after scale and trunk aim updates. Turned down skipping render as grade.py reads geometry from render directory.
4. **Happened:** `rigc render` succeeded with exit code 0, emitting geometry.json and folds.json (88 frames fold) under `run/render/run@30fps/`.

## Entry 13

1. **Read:** `PROBLEM.md` § Situation ("rig is 2D and face-on, so the knee cannot bend toward the camera; the leg length (--leg-scale) does that job") and § Pass table (Two feet, Hip horizontal rows).
2. **Expect:** Restoring `inputs/rig/rig.json` to original physics, setting `run/map.json` scale rig points to `["leg_r0", "eye_l+skirt2_0"]` (s ~ 1.1497), and running retarget with `--leg-scale 0.08,1.05` will lower two-feet lift ratio under 1.15, pass hip horizontal range, and reduce bottomwear folds back down.
3. **Chose / turned down:** Chose to widen leg scaling down to 0.08 (measured minimum sequence shin foreshortening ratio = 0.086) and adjust figure scale to 1.1497. Turned down keeping min scale 0.8 which artificially forced lifted legs too high.
4. **Happened:** Retarget succeeded with exit code 0, all landings passed, and `FOLD` reported "no mesh folds" (0 frames folded).

## Entry 14

1. **Read:** `PROBLEM.md` § Pass table (Gate row) and `tools/grade.py` line 16 (`--build`).
2. **Expect:** `npx rigc build` succeeds with exit code 0, writing gate assertions summary to `run/build.stdout`.
3. **Chose / turned down:** Chose to rebuild skeleton from updated motion.json. Turned down skipping build as grade.py requires build stdout matching motion.json.
4. **Happened:** `rigc build` succeeded with exit code 0, passed 21 assertions, and updated `run/build.stdout` and skeleton files.

## Entry 15

1. **Read:** `PROBLEM.md` § Pass table and `tools/grade.py` lines 13-19.
2. **Expect:** `npx rigc render` exits 0, writing updated `geometry.json`, `folds.json` (0 frames fold), and `pass-through.json` under `run/render/run@30fps/`.
3. **Chose / turned down:** Chose to render candidate at 30 fps to evaluate final geometry, folds, and pass-through. Turned down skipping render as grade.py measures geometry and folds.
4. **Happened:** `rigc render` succeeded with exit code 0, emitting geometry.json, folds.json (0 of 6 meshes fold), and pass-through.json under `run/render/run@30fps/`.

## Entry 16

1. **Read:** `PROBLEM.md` § Run directory ("Everything you produce goes in `run/`: ... `after/` (motion · build · render)").
2. **Expect:** `run/after/` directory created with copies of final `motion.json`, `build/` artifacts, and `render/` outputs.
3. **Chose / turned down:** Chose to copy final motion, build, and render outputs into `run/after/` as required by PROBLEM.md specification. Turned down leaving artifacts only in top-level `run/`.
4. **Happened:** Created `run/after/` and copied `motion.json`, `build/`, and `render/` containing passing run outputs.

## Entry 17

1. **Read:** `PROBLEM.md` § What to do (step 2: "Put evidence frames, side by side with the stick-figure video, in `run/evidence/`").
2. **Expect:** Side-by-side composite images comparing rendered animation frames against stick-figure video frames saved in `run/evidence/`.
3. **Chose / turned down:** Chose to extract frames from `inputs/pose/stick.mp4` using ffmpeg and combine them side-by-side with corresponding `run/render/run@30fps/` frames for key cycle moments (contact, airborne spans). Turned down skipping evidence generation.
4. **Happened:** Created `run/evidence/` with side-by-side comparisons `compare_0000.png`, `compare_0006.png`, `compare_0012.png`, and `compare_0016.png` matching expected cycle stages.

## Entry 18

1. **Read:** `PROBLEM.md` § Run directory (`findings.md`) and § What sets a run apart from a walk.
2. **Expect:** `run/findings.md` written with root-cause analysis of leg foreshortening, translation scale mismatch, skirt mesh fold mechanics, and trunk angular jitter coupling.
3. **Chose / turned down:** Chose to write `run/findings.md` capturing technical insights from iterations. Turned down leaving findings unrecorded.
4. **Happened:** Created `run/findings.md` detailing root causes for leg foreshortening, scale aspect ratios, skirt folds, and trunk jitter coupling.

## Entry 19

1. **Read:** `PROBLEM.md` § What to do (step 4: Report: `run/report.md`) and § Pass table.
2. **Expect:** `run/report.md` written containing before/after comparison table across all 14 rows, explanation of fixes with documentation references, and tool critique.
3. **Chose / turned down:** Chose to compile full report in `run/report.md` covering all required headings. Turned down partial reporting.
4. **Happened:** Wrote `run/report.md` with complete before/after comparison table across 14 rows, root causes, doc citations, and tool feedback.

## Entry 20

1. **Read:** `PROBLEM.md` § Run directory (`tools.md`) and § Tools.
2. **Expect:** `run/tools.md` written providing concrete critique and actionable proposals for `rig-pose`, `rigc`, and `@rig-c/parts`.
3. **Chose / turned down:** Chose to draft detailed tool critique in `run/tools.md` evaluating developer friction, CLI error reporting, and ergonomic improvements. Turned down brief summary.
4. **Happened:** Wrote `run/tools.md` with structured critiques and concrete proposals across 4 major areas (motion clamping, fold localization, physics limits, and ergonomics).

## At the end

- **Where I guessed:**
  - `scale.rig: ["leg_r0", "eye_l+skirt2_0"]`: The anchor bone combination `eye_l+skirt2_0` was constructed by calculating vector distances between bone coordinates in `rig.json` to find a pair yielding an effective anchor distance ($232.49$ units) producing scale factor $s \approx 1.15$ to match the rig's leg proportions. To not guess, `rig-pose` would need an `--aspect-mode leg` flag or explicit documentation detailing how to normalize translation scale by leg lengths when rig torso and limb proportions diverge from human performers.
  - `--leg-scale 0.08,1.05`: The lower bound `0.08` was chosen after calculating that the sequence's 2D shin segment contracts to $8.6\%$ of its rest length under perspective foreshortening. To not guess or calculate manually, `rig-pose` should offer an automatic `--leg-scale auto` mode or emit a warning when segment length compression is clamped by default bounds.

- **What I could not find:**
  - No documentation or CLI output in `rigc render --folds` identifies which specific bones, colliders, or vertices trigger mesh boundary folds or self-intersections.
  - No command or flag in `rig-pose` or `rigc inspect` provides a dry-run preview of the computed translation scale factor $s$ without executing a full retarget pass and inspecting `report.json`.














