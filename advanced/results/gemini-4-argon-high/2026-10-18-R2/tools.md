## `rigc render` `--fps` output directory suffix (`@<fps>fps`) omitted in `README.md`
- **I was trying to:** Render the 30 fps `run` animation with `--geometry`, `--folds`, and `--pass-through` and pass the resulting JSON files in `--out run/before/render` to `tools/grade.py`.
- **The tool gave me:** In `node_modules/rig-c/README.md` ("### Posing and checking", line 429):
  > "`render` poses every animation (or `--animation <name>`) through the model and writes `render/<animation>/f0000.png…`, a `sheet.png` contact grid, and `frames.json`."
  And on the first grader run:
  > `SKIP  support-foot    Support foot: --geometry run/before/render/run/geometry.json is not on disk`
- **What would have helped:** State in `node_modules/rig-c/README.md` (at line 429 and in the `render` row of `## Commands` at line 606) that when `--fps` differs from the default `12`, `rigc render` writes to `<out>/<animation>@<fps>fps/` instead of `<out>/<animation>/`.
- **Cost:** ~1 minute (one failed `tools/grade.py` invocation in Entry 3 before checking `run/before/render.txt` and re-running in Entry 4); got there in the end.

## Unplanted `rig-pose retarget` on `"in-place"` sequences fragments `feet.supports` and causes `grade.py`'s `slide` row to `SKIP`
- **I was trying to:** Measure the baseline ("before") figures across all 14 rows of `tools/grade.py --round R2` on an unflagged `rig-pose retarget` run.
- **The tool gave me:** In `run/before/report.json` (and `rig-pose retarget` stdout), `feet.supports` was fragmented into 1-frame spans (`r 0–0, l 2–2, l 22–22, ...`) with `steps`: `r 1–199 -> the pose's travel, never re-planted`, which caused `tools/grade.py` to output:
  > `SKIP  slide           Slide: no two consecutive grounded frames with sequence ankles`
- **What would have helped:** `rig-pose retarget` should read `"travel": "in-place"` when identifying `feet.supports` even when `--plant-feet` is not passed (so an in-place treadmill/loop sequence does not release support as a forward step on frame 1), or `tools/grade.py` should measure `slide` on grounded frames outside `feet.jumps` when `feet.supports` has no multi-frame spans.
- **Cost:** ~2 minutes inspecting `tools/grade.py` (`row_slide`) and `run/before/report.json` to verify why `slide` skipped on the unplanted baseline; got there in the end once `--plant-feet` was enabled.

## No warning when `translate.scale` uses a foreshortened segment that disagrees with leg-length and hip-width scale ratios
- **I was trying to:** Pass `hip-vertical`, `hip-horizontal`, `rebound`, and `folds` after enabling `--plant-feet --stance 0.02 --leg-scale 0.5,1.0` using the README's example `translate.scale` (`["mid_hip", "neck"]` / `["hip", "neck"]`).
- **The tool gave me:** In `node_modules/@rig-c/pose/README.md` ("## The map: `rig-pose-map/1`", lines 109–110 and 120):
  > `"translate": { "bone": "hip", "joint": "mid_hip", "scale": { "pose": ["mid_hip", "neck"], "rig": ["hip", "neck"] } }`
  > "`translate.scale` is one length measured on both: two points on the rig, two points in the pose (its median over the frames where both are good). Pick a long segment that does not foreshorten much."
  And in `rig-pose retarget` stdout:
  > `SCALE  1.78104 rig units per picture px (rig 360.00 / pose median 202.13)`
   Which caused `tools/grade.py` in Entry 6 to fail four rows:
  > `FAIL  folds           Folds: 16 frame(s) with a folded triangle, most in slot 'bottomwear' (16 frames) [bar 0]`
  > `FAIL  hip-vertical    Hip vertical range: rig/sequence 1.460 ... [bar 0.85-1.15]`
  > `FAIL  hip-horizontal  Hip horizontal range: rig/sequence 1.712 ... [bar 0.85-1.15]`
  > `FAIL  rebound         Rebound: median rig/sequence peak upward hip acceleration in the stance windows 1.929 over 19 windows [bar 0.7-1.43]`
- **What would have helped:** Have `rig-pose retarget` print the rig-to-sequence leg-length scale ratio (`485.09 / 399.28 = 1.215 units/px`) and hip-width scale ratio (`84.0 / 82.5 = 1.018 units/px`) on the `SCALE` line, and emit a warning when `scale.factor` (`1.78104`) lies outside `0.85–1.15×` of those ratios because the chosen `translate.scale` segment (`mid_hip -> neck`) is foreshortened or disproportionately sized relative to the legs and pelvis.
- **Cost:** ~4 minutes diagnosing why `--plant-feet` still left `hip-vertical`, `hip-horizontal`, `rebound`, and `bottomwear` `folds` failing (because 14 of every 20 frames are airborne jump frames that use `translate.scale` directly); got there in the end by switching `translate.scale` to the shoulder line.

## `SHEAR` line on `--leg-scale` does not name `"inherit": "noScale"` / `"onlyTranslation"` when feet squash under scaled shins
- **I was trying to:** Prevent the lifted boot (`foot_r` / `foot_l`) from squashing vertically to `0.5×` its height and shearing up to `30.93°` when `--leg-scale 0.5,1.0` foreshortens the shins (`leg_r1` / `leg_l1`).
- **The tool gave me:** In `run/after/retarget.txt` (lines 122–126):
  > `SHEAR  bone "leg_r1": art sheared up to 12.09° (frame 174); world x axis 0.500 … 1.000, y axis 0.933 … 1.000 of setup — a scaled bone, or one under it; a reading`
  > `SHEAR  bone "foot_r": art sheared up to 30.93° (frame 173); world x axis 0.661 … 1.000, y axis 0.500 … 1.000 of setup — a scaled bone, or one under it; a reading`
- **What would have helped:** Have the `SHEAR` diagnostic line name the bone `inherit` remedy directly (e.g., *"set `inherit: \"noScale\"` on child limb links and `inherit: \"onlyTranslation\"` on level feet to prevent parent `scalex` from shearing or squashing their art"*), and have `@rig-c/parts` propose `"inherit": "onlyTranslation"` instead of `"noRotationOrReflection"` on `foot_r`/`foot_l`.
- **Cost:** ~3 minutes cross-referencing `@rig-c/pose/README.md` and `@rig-c/parts/docs/AUTHORING.md` §3 (`bones` row) and rebuilding with `run/after/rig/rig.json`; got there in the end (`0.00°` shear across all leg and foot bones).
