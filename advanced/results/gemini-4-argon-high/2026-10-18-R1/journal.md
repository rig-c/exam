# Journal — argon, walk (Advanced R1), 2026-10-18

## Entry 1

1. **Read:** `PROBLEM.md` ("## What to do", item 1; "## Pass table", Jitter row), `node_modules/@rig-c/pose/README.md` ("## The map (`rig-pose-map/1`)" and "## CLI"), `inputs/rig/rig.json` (`bones`), and `inputs/pose/sequence.json` (`frames[0].people[0].joints`).
2. **Expect:** Writing `run/map.json` with spec `rig-pose-map/1`, mapping `trunk` (`chest` <- `mid_hip`..`mid_shoulder`), `head` (`head` <- `mid_shoulder`..`nose`), `arm_r` (`sleeve_r0`, `sleeve_r1` <- `r_shoulder`, `r_elbow`, `r_wrist`), `arm_l` (`sleeve_l0`, `sleeve_l1` <- `l_shoulder`, `l_elbow`, `l_wrist`), `leg_r` (`leg_r0`, `leg_r1` <- `r_hip`, `r_knee`, `r_ankle`), `leg_l` (`leg_l0`, `leg_l1` <- `l_hip`, `l_knee`, `l_ankle`), and `translate` (`hip` <- `mid_hip`) will produce a valid map file on disk matching all 10 rotatable limb/trunk/head bones and the hip root bone.
3. **Chose / turned down:** Chose to map `chest` and `head` directly (rather than `chest_ctl` and `head_ctl`, which have zero length in `rig.json`) and omitted a `pelvis` rotation chain on `hip` because `PROBLEM.md` R1 pass table only grades `limbs` and `trunk · head` for rotation jitter and does not include R2's hip-tilt row.
4. **Happened:** Wrote `run/map.json` (41 lines) with the 6 chains (`trunk`, `head`, `arm_r`, `arm_l`, `leg_r`, `leg_l`) and `translate` on `hip`. Matched expectation. Next is running baseline `rig-pose retarget` to put the sequence on the rig before applying any fixes.

## Entry 2

1. **Read:** `PROBLEM.md` ("## What to do", item 1: "Put it on: retarget the sequence onto the rig with `rig-pose retarget`... The gate must be green") and `node_modules/@rig-c/pose/README.md` ("## CLI" for `rig-pose retarget` flags and report output).
2. **Expect:** Running `mkdir -p run/before && npx rig-pose retarget --sequence inputs/pose/sequence.json --rig inputs/rig/rig.json --map run/map.json --animation walk --out run/before/motion.json --report run/before/report.json` will exit 0, write `run/before/motion.json` and `run/before/report.json`, and print `RESULT PASS` with all 10 angle landings and 1 translate landing within tolerance.
3. **Chose / turned down:** Chose to run `rig-pose retarget` without `--plant-feet`, `--stance`, or `--leg-scale` first so we can measure the true unfixed ("before") pass-table figures required by `PROBLEM.md` ("the table before and after"), rather than jumping straight to the fixed retarget flags.
4. **Happened:** `WTF?:` Exited with code 2 (`rig-pose retarget: unknown flag --sequence; the flags are --rig, --map, --pose, --out, --name...`) — I mixed up `grade.py`'s `--sequence` and `rigc render`'s `--animation` flags with `rig-pose retarget`'s `--pose` and `--name` flags in `node_modules/@rig-c/pose/README.md`.

## Entry 3

1. **Read:** `node_modules/@rig-c/pose/README.md` ("## CLI" under `rig-pose retarget`: `--rig`, `--map`, `--pose`, `--out`, `--name`, `--base-motion`, `--report`) and the error message from Entry 2.
2. **Expect:** Running `npx rig-pose retarget --rig inputs/rig/rig.json --map run/map.json --pose inputs/pose/sequence.json --base-motion inputs/rig/motion.json --name walk --out run/before/motion.json --report run/before/report.json` will exit 0, print `RESULT PASS` with all 10 angle landings and 1 translate landing within tolerance, and write `run/before/motion.json` and `run/before/report.json`.
3. **Chose / turned down:** Chose `--pose inputs/pose/sequence.json --name walk --base-motion inputs/rig/motion.json` instead of omitting `--base-motion`, so the rig's existing `idle` animation stays in the motion file alongside `walk`.
4. **Happened:** `WTF?:` Exited with code 1 (`FAIL MAP_TRANSLATE_SCALE: run/map.json "translate" "scale" is undefined; it must be { pose: [joint, joint], rig: [bone, bone] }, the same length measured in each`) — I had only read the top of `node_modules/@rig-c/pose/README.md` before writing `run/map.json` and missed `## The map: rig-pose-map/1` (lines 299–320), which requires `translate.scale` (`{ "pose": ["mid_hip", "neck"], "rig": ["hip", "neck"] }`), `aim` on `trunk`/`head`, and `"bend": "free"` on front-facing limbs.

## Entry 4

1. **Read:** `node_modules/@rig-c/pose/README.md` ("## The map: `rig-pose-map/1`", lines 299–320) and the `MAP_TRANSLATE_SCALE` refusal from Entry 3.
2. **Expect:** Updating `run/map.json` to use `joints: ["mid_hip", "neck"]` with `aim: ["neck"]` on `trunk`, `joints: ["r_eye", "l_eye"]` with `aim: ["eye_r>eye_l"]` on `head`, `"bend": "free"` on the four limb chains (`arm_r`, `arm_l`, `leg_r`, `leg_l`), and `"scale": { "pose": ["mid_hip", "neck"], "rig": ["hip", "neck"] }` on `translate` will produce a complete `rig-pose-map/1` file on disk.
3. **Chose / turned down:** Chose `"scale": { "pose": ["mid_hip", "neck"], "rig": ["hip", "neck"] }`, `"aim": ["eye_r>eye_l"]` for `head`, and `"bend": "free"` on all four limbs as directly recommended by `node_modules/@rig-c/pose/README.md` lines 304–320 for front-facing material, instead of leaving `bend` at its `"rest"` default which refuses front-facing elbow/knee crossings.
4. **Happened:** Updated `run/map.json` (51 lines) with `translate.scale`, `aim` fields on `trunk` and `head`, and `"bend": "free"` on the four limb chains. Matched expectation. Next is re-running baseline `rig-pose retarget`.

## Entry 5

1. **Read:** `node_modules/@rig-c/pose/README.md` ("## What it does", lines 104–121; "## The map: `rig-pose-map/1`", lines 299–320) and `run/map.json`.
2. **Expect:** Running `npx rig-pose retarget --rig inputs/rig/rig.json --map run/map.json --pose inputs/pose/sequence.json --base-motion inputs/rig/motion.json --name walk --out run/before/motion.json --report run/before/report.json` will exit 0, pass the rig-c gate and all landing checks, and write `run/before/motion.json` and `run/before/report.json`.
3. **Chose / turned down:** Chose to run baseline `retarget` without `--plant-feet`, `--stance`, or `--leg-scale` to capture the unfixed ("before") motion and report first.
4. **Happened:** Exited 0, wrote `run/before/motion.json` and `run/before/report.json`. Gate was green (`52 assertions: 21 measured (21 passed, 0 failed)`), all 11 landings passed (max angle error 0.00123° on `sleeve_l1`, origin error 0.000687u on `hip`), and `FOLD` reported no mesh folds at 30 fps, while `FEET` reported unplanted vertical range 0.0985 leg lengths and worst horizontal drift 0.1828 leg lengths. Matched expectation. Next is running `rigc build` on `run/before/motion.json` to produce the compiled candidate and build stdout for the grader.

## Entry 6

1. **Read:** `PROBLEM.md` ("## Pass table", line 52: "the build output = the standard output of the last `rigc build` (not retarget's output)") and `node_modules/rig-c/docs/AUTHORING.md` ("## 0. The loop", lines 112–117).
2. **Expect:** Running `npx rigc build --rig inputs/rig/rig.json --motion run/before/motion.json --images inputs/rig/images --out run/before/build | tee run/before/build.txt` will exit 0, write `skeleton.json`, `skeleton.atlas`, and `skeleton.model.json` into `run/before/build/`, and record the build's stdout (`52 assertions: 21 measured (21 passed, 0 failed)`) in `run/before/build.txt`.
3. **Chose / turned down:** Chose default profile (`spine`) matching `rig-pose retarget`'s internal gate and captured stdout via `tee run/before/build.txt` because `grade.py --build` requires the stdout of `rigc build`, not `retarget`'s stdout.
4. **Happened:** Exited 0, wrote `run/before/build/skeleton.json`, `skeleton.atlas`, and `skeleton.model.json`, and saved stdout (`52 assertions: 21 measured (21 passed, 0 failed), 17 skipped, 14 not in profile "spine"`) to `run/before/build.txt`. Matched expectation. Next is rendering the baseline `walk` animation at 30 fps with `--geometry`, `--folds`, and `--pass-through bottomwear:thigh_r,bottomwear:thigh_l`.

## Entry 7

1. **Read:** `PROBLEM.md` ("## Tools", line 19; "## What to do", item 2; "## Pass table", Folds and Pass-through rows) and `node_modules/rig-c/docs/AUTHORING.md` (lines 255–257 and 280–283 on `--geometry`, `--folds`, `--pass-through`, and `--fps 30` writing to `walk@30fps/`).
2. **Expect:** Running `npx rigc render --candidate run/before/build --animation walk --fps 30 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l --out run/before/render` will exit 0, write 224 PNG frames plus `geometry.json`, `folds.json`, and `pass-through.json` into `run/before/render/walk@30fps/`, and print the folds and pass-through readings.
3. **Chose / turned down:** Chose `--fps 30` (matching the 30 fps sequence rate required by `grade.py`) and `--animation walk` (instead of rendering all animations) so only the graded animation is rendered.
4. **Happened:** Exited 0, wrote 224 PNG frames, `contact.png`, `geometry.json`, `folds.json` (`0 of 6 mesh(es) fold`), and `pass-through.json` (`0 of 2 pair(s) pass through`) into `run/before/render/walk@30fps/`. Matched expectation. Next is running `tools/grade.py --round R1` on the baseline outputs to read all 9 "before" rows of the pass table.

## Entry 8

1. **Read:** `PROBLEM.md` ("## Pass table", lines 38–53) and `tools/grade.py` (`main` arguments and `R1_ROWS`).
2. **Expect:** Running `python3 tools/grade.py --round R1 --geometry run/before/render/walk@30fps/geometry.json --sequence inputs/pose/sequence.json --report run/before/report.json --build run/before/build.txt --cycle 32 --folds run/before/render/walk@30fps/folds.json --passthrough run/before/render/walk@30fps/pass-through.json --map run/map.json --feet foot_l,foot_r --hip hip --trunk chest,head | tee run/before/grade.txt` will evaluate all 9 R1 rows (0 `SKIP`), passing `gate`, `floor`, `jitter`, `folds`, `pass-through`, and `loop`, while failing `support-foot`, `two-feet`, and `slide` (because `--plant-feet`, `--stance`, and `--leg-scale` are off).
3. **Chose / turned down:** Chose `--feet foot_l,foot_r --hip hip --trunk chest,head --cycle 32` matching the rig's ankle origins, hip bone, mapped trunk+head bones, and 32-frame walk cycle.
4. **Happened:** `WTF?:` Exited 1 with 4 pass (`gate`, `floor`, `folds`, `pass-through`) and 5 fail — `support-foot` (0.0608 > 0.01), `two-feet` (168/168 lifted frames within 0.01 of support, median lift ratio -0.010), and `slide` (0.01176 > 0.005) failed as expected without the foot/leg flags, but `jitter` (`trunk+head 1.277x > 1.1`) and `loop` (`head` angle difference `1.3809 deg > 1.0` at cycle frame 13) also failed! I misread the effect of mapping `head` to `["r_eye", "l_eye"]`: per `node_modules/@rig-c/pose/README.md` line 110 (#190, #205), an eye-line head chain couples the clamped vertical nod (`clampedY`, `+1.6°/unit`) into `head.rotate`, which adds non-periodic boundary differences between cycle 1 and cycle 7 and inflates `head`'s local rotation second difference relative to the raw `r_eye -> l_eye` segment angle that `grade.py` compares against.

## Entry 9

1. **Read:** `PROBLEM.md` ("## What to do", item 2: "Put evidence frames, side by side with the stick-figure video, in `run/evidence/`") and `run/before/grade.txt` (frames 6, 18, 42, 183, 203).
2. **Expect:** Running a Python script with `ffmpeg` / `PIL` (or `cv2`) to extract frames 0, 6, 18, 42, 183, and 203 from `inputs/pose/stick.mp4` and concatenate each side-by-side with `run/before/render/walk@30fps/fXXXX.png` into `run/evidence/before_fXXXX.png` will exit 0 and create 6 side-by-side PNG files in `run/evidence/`.
3. **Chose / turned down:** Chose frames 0 (cycle start), 6 (peak right foot lift in sequence), 18 (peak left foot lift in sequence), 42 (worst lifted-foot drop `-0.0097 L` in `two-feet`), 183 (worst `support-foot` error `0.0608 L`), and 203 (worst two-foot height diff `0.0074 L`) rather than arbitrary frame numbers, so each evidence image directly illustrates a measured row from `grade.py`.
4. **Happened:** `WTF?:` Exited 1 (`ffmpeg ... -vsync 0 ... returned non-zero exit status 8`) — modern ffmpeg removed `-vsync` in favor of `-fps_mode` (or default CFR extraction without `-vsync`).

## Entry 10

1. **Read:** `PROBLEM.md` ("## What to do", item 2: "Put evidence frames, side by side with the stick-figure video, in `run/evidence/`") and the `ffmpeg` exit status 8 from Entry 9.
2. **Expect:** Running `ffmpeg -y -i inputs/pose/stick.mp4` without `-vsync 0` inside the Python script will extract all 224 frames and write `run/evidence/before_f0000.png`, `before_f0006.png`, `before_f0018.png`, `before_f0042.png`, `before_f0183.png`, and `before_f0203.png` with exit code 0.
3. **Chose / turned down:** Chose plain `ffmpeg -y -i inputs/pose/stick.mp4` instead of `-vsync 0` because `stick.mp4` is already a constant-30-fps 224-frame video.
4. **Happened:** Exited 0 and wrote 6 side-by-side PNG images (`before_f0000.png`, `before_f0006.png`, `before_f0018.png`, `before_f0042.png`, `before_f0183.png`, `before_f0203.png`, each 385x256) into `run/evidence/`. Viewing `before_f0006.png` and `before_f0183.png` confirmed visually that when the stick figure lifts a foreshortened leg, the unfixed rig leaves both feet near the ground and drifts vertically. Matched expectation. Next is Step 3 (Fix): running `rig-pose retarget` with `--plant-feet`, `--stance`, and `--leg-scale`.

## Entry 11

1. **Read:** `PROBLEM.md` ("## Tools", line 20; "## What to do", item 3; "## Pass table", Support foot, Two feet, Slide, and Floor rows) and `node_modules/@rig-c/pose/README.md` ("### The legs: foreshortening and planted feet", lines 199–220, specifically `--leg-scale <min,max>`, `--plant-feet`, in-place loop closure `#92`, one floor `#85`, and `--stance <leg lengths>` with `0.8×` re-entry hysteresis `#87`).
2. **Expect:** Running `mkdir -p run/after && npx rig-pose retarget --rig inputs/rig/rig.json --map run/map.json --pose inputs/pose/sequence.json --base-motion inputs/rig/motion.json --name walk --plant-feet --stance 0.03 --leg-scale 0.6,1.05 --out run/after/motion.json --report run/after/report.json` will exit 0, plant all support spans on one floor, close the in-place loop drift (`feet.closure`), scale the foreshortened legs without clamping, plant both feet on two-foot frames (`<= 0.02` leg lengths), and write `run/after/motion.json` and `run/after/report.json`.
3. **Chose / turned down:** Chose `--stance 0.03` instead of `--stance 0.02` because `node_modules/@rig-c/pose/README.md` line 217 states that a lifted foot re-enters stance only below `0.8 × tolerance`; with `0.03`, both the exit threshold (`0.03 < 0.04`) and the re-entry threshold (`0.8 × 0.03 = 0.024 >= 0.02`) sit strictly inside the grader's `[0.02, 0.04]` deadband between two-foot and lifted frames. Chose `--leg-scale 0.6,1.05` so foreshortened lifted legs are not clamped at the lower bound.
4. **Happened:** `WTF?:` Exited 0, planted every support span onto one floor (`lowest ankle's vertical range 0.0000 leg lengths`), and passed all 17 landings, but `run/after/report.json` (`legScale[1]`, `leg_r1`) showed 7 clamped runs (frames 4–6, 36–38, ..., 196–198) where `r_knee -> r_ankle` foreshortened down to `0.4511` of its straight length and hit the `0.6` lower bound — nothing before running `--leg-scale` told me the sequence's right shin foreshortens to `0.4511`. Next is updating `run/map.json` (`head` joints) to eliminate the eye-line nod coupling that failed `jitter` and `loop`, and lowering `--leg-scale` to `0.45,1.05`.

## Entry 12

1. **Read:** `node_modules/@rig-c/pose/README.md` ("## What it does", line 110: "When a head chain carries the eye line (`r_eye → l_eye`)... the clamped vertical nod (`clampedY`) is coupled in phase into ... the head bone's `rotate` track (`+1.6°/unit`)", and "## The map: `rig-pose-map/1`", lines 313–315) and `tools/grade.py` (`row_jitter`, lines 760–806, and `row_loop`, lines 866–895).
2. **Expect:** Writing `run/after/map.json` with `head` mapped to `"joints": ["r_ear", "l_ear"], "aim": ["eye_r>eye_l"]` (keeping `run/map.json` untouched as the `before` map) will give `rig-pose retarget` a horizontal head-roll segment that does not trigger the `r_eye -> l_eye` vertical-nod coupling on `head.rotate`.
3. **Chose / turned down:** Chose `"joints": ["r_ear", "l_ear"]` with `"aim": ["eye_r>eye_l"]` (and saved to `run/after/map.json` so `run/before/report.json`'s `inputs.map.sha256` continues to match `run/map.json`) instead of `"joints": ["r_eye", "l_eye"]` (which couples non-periodic detrended `clampedY` into `head.rotate`, failing `jitter` at `1.277x` and `loop` at `1.3809°`) or `"joints": ["neck", "nose"]` (which turns head yaw into large 2D roll).
4. **Happened:** Wrote `run/after/map.json` (51 lines) with `head.joints` set to `["r_ear", "l_ear"]`. Matched expectation. Next is re-running `rig-pose retarget` with `--map run/after/map.json --plant-feet --stance 0.03 --leg-scale 0.45,1.05`.

## Entry 13

1. **Read:** `node_modules/@rig-c/pose/README.md` ("### The legs: foreshortening and planted feet", lines 199–220), `run/after/report.json` from Entry 11 (`leg_r1` min ratio `0.45108`), and `run/after/map.json`.
2. **Expect:** Running `npx rig-pose retarget --rig inputs/rig/rig.json --map run/after/map.json --pose inputs/pose/sequence.json --base-motion inputs/rig/motion.json --name walk --plant-feet --stance 0.03 --leg-scale 0.45,1.05 --out run/after/motion.json --report run/after/report.json` will exit 0, emit 15 tracks (no `head` nod translate track), report 0 clamped frames across all 4 leg segments (`leg_r0`, `leg_r1`, `leg_l0`, `leg_l1`), pass the gate and all 17 landings, and report 0 mesh folds at 30 fps.
3. **Chose / turned down:** Chose `--leg-scale 0.45,1.05` (just below `leg_r1`'s minimum `0.45108`) instead of `0.6,1.05` so no lifted-leg frame is clamped at the lower bound.
4. **Happened:** Exited 0, wrote `run/after/motion.json` and `run/after/report.json`, passed the gate (`52 assertions: 21 measured, 0 failed`) and all 17 landings, kept lowest ankle vertical range at `0.0000` leg lengths, scaled `leg_r1` down to `0.451` without clamping, and reported 0 mesh folds at 30 fps. Matched expectation. Next is building `run/after/build` with `rigc build`.

## Entry 14

1. **Read:** `PROBLEM.md` ("## Run directory", line 29: "`after/` (motion · build · render)"; "## Pass table", line 52: "the build output = the standard output of the last `rigc build`").
2. **Expect:** Running `npx rigc build --rig inputs/rig/rig.json --motion run/after/motion.json --images inputs/rig/images --out run/after/build | tee run/after/build.txt` will exit 0, write `skeleton.json`, `skeleton.atlas`, and `skeleton.model.json` into `run/after/build/`, and record the green build stdout in `run/after/build.txt`.
3. **Chose / turned down:** Chose to write the build output to `run/after/build` and stdout to `run/after/build.txt` as required by `PROBLEM.md`.
4. **Happened:** Exited 0, wrote `run/after/build/skeleton.json`, `skeleton.atlas`, and `skeleton.model.json`, and saved stdout (`52 assertions: 21 measured (21 passed, 0 failed)`) to `run/after/build.txt`. Matched expectation. Next is rendering `run/after/build` at 30 fps with `--geometry`, `--folds`, and `--pass-through bottomwear:thigh_r,bottomwear:thigh_l`.

## Entry 15

1. **Read:** `PROBLEM.md` ("## Run directory", line 29: "`after/` (motion · build · render)"; "## Pass table", Folds and Pass-through rows) and `node_modules/rig-c/docs/AUTHORING.md` (lines 255–257).
2. **Expect:** Running `npx rigc render --candidate run/after/build --animation walk --fps 30 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l --out run/after/render` will exit 0, write 224 PNG frames, `geometry.json`, `folds.json` (`0 of 6 mesh(es) fold`), and `pass-through.json` (`0 of 2 pair(s) pass through`) into `run/after/render/walk@30fps/`.
3. **Chose / turned down:** Chose `--fps 30` and `--animation walk` matching the sequence rate and the baseline render setup.
4. **Happened:** Exited 0, wrote 224 PNG frames, `contact.png`, `geometry.json`, `folds.json` (`0 of 6 mesh(es) fold`), and `pass-through.json` (`0 of 2 pair(s) pass through`) into `run/after/render/walk@30fps/`. Matched expectation. Next is grading the fixed build with `tools/grade.py --round R1`.

## Entry 16

1. **Read:** `PROBLEM.md` ("## Pass table", lines 38–53) and `tools/grade.py` (`R1_ROWS`).
2. **Expect:** Running `python3 tools/grade.py --round R1 --geometry run/after/render/walk@30fps/geometry.json --sequence inputs/pose/sequence.json --report run/after/report.json --build run/after/build.txt --cycle 32 --folds run/after/render/walk@30fps/folds.json --passthrough run/after/render/walk@30fps/pass-through.json --map run/after/map.json --feet foot_l,foot_r --hip hip --trunk chest,head | tee run/after/grade.txt` will exit 0 and print `RESULT PASS (9 pass, 0 fail, 0 skip of 9 rows)`.
3. **Chose / turned down:** Chose the exact same grader flags (`--cycle 32 --feet foot_l,foot_r --hip hip --trunk chest,head`) pointed at `run/after/` so the before and after pass tables are directly comparable.
4. **Happened:** Exited 0 with `RESULT PASS (9 pass, 0 fail, 0 skip of 9 rows)`: `gate` green (17/17 landings), `support-foot` 0.0000 leg lengths, `two-feet` 0.0000 leg lengths on two-foot frames and 0/168 lifted within 0.01 (lowest lift 0.0176, median ratio 0.913), `slide` 0.00002 leg lengths/frame, `floor` 0.0000 leg lengths spread, `jitter` limbs 0.988x / trunk+head 1.000x, `folds` 0, `pass-through` 0, and `loop` 0.0001 deg / 0.0000 leg lengths. Matched expectation. Next is writing side-by-side Stick + Before + After evidence frames to `run/evidence/`.

## Entry 17

1. **Read:** `PROBLEM.md` ("## What to do", item 2: "Put evidence frames, side by side with the stick-figure video, in `run/evidence/`") and `run/after/grade.txt`.
2. **Expect:** Running a Python script to generate side-by-side Stick + After (`run/evidence/after_fXXXX.png`) and Stick + Before + After (`run/evidence/compare_fXXXX.png`) images for frames 0, 6, 18, 42, 183, and 203, followed by a final verification run of `tools/grade.py --round R1`, will exit 0 and write 12 comparison PNGs in `run/evidence/` and `RESULT PASS (9 pass, 0 fail, 0 skip of 9 rows)`.
3. **Chose / turned down:** Chose to generate both 2-up (`after_fXXXX.png`) and 3-up (`compare_fXXXX.png`) side-by-side panels and run the final `grade.py` check immediately before clocking `finished:` in `run/transcript.md`.
4. **Happened:** Exited 0, wrote `after_f0000.png`..`after_f0203.png` (387x256) and `compare_f0000.png`..`compare_f0203.png` (544x256) into `run/evidence/`, confirmed `RESULT PASS (9 pass, 0 fail, 0 skip of 9 rows)`, and clocked `finished: 2026-10-18T23:52:26Z`. Matched expectation.

## At the end

- **Where I guessed:**
  - In Entry 11, I initially guessed `--leg-scale 0.6,1.05` before seeing the sequence's per-segment foreshortening range. Reading the `legScale` block in `run/after/report.json` (or running `rig-pose retarget` once with any `--leg-scale` to read the `LEG-SCALE` line) was needed to know that `r_knee -> r_ankle` (`leg_r1`) foreshortens down to `0.45108` of its straight length, which led to setting `--leg-scale 0.45,1.05` in Entry 13.
  - For `--stance 0.03`, I chose `0.03` from the two pass-table bands in `PROBLEM.md` (`<= 0.02` for two-foot frames and `> 0.04` for lifted frames) combined with the `0.8 × tolerance` re-entry hysteresis documented in `node_modules/@rig-c/pose/README.md` ("### The legs: foreshortening and planted feet", line 217), so `0.8 × 0.03 = 0.024 >= 0.02` and `0.03 < 0.04`.
- **What I could not find:**
  - Nothing in `node_modules/@rig-c/pose/README.md` warned that the eye-line head mapping (`"joints": ["r_eye", "l_eye"], "aim": ["eye_r>eye_l"]`, recommended at line 314) couples a non-periodic detrended vertical nod (`clampedY`, `+1.6°/unit`, line 110) into `head.rotate` in a way that fails both `grade.py`'s `jitter` row (`trunk+head 1.277x > 1.1x`) and `loop` row (`1.3809° > 1.0°` between cycle 1 and cycle 7).

