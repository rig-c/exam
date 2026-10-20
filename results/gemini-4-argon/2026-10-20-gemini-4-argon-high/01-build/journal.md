# Journal — gemini-4-argon-high, 01-build, 2026-10-20

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry 1

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §3 (`config.json`, field by field) and §4 (The command order, `layers` loader row), and `tasks/01-build/inputs/seethrough.json`.
2. **Expect:** Writing an initial `config.json` with `key: "01-build"`, `seethrough` from `inputs/seethrough.json`, and `assemble: { "rig_scale": 0.5 }`, then running `npx rig-parts assemble --propose-plan` against `tasks/01-build/inputs` will exit 0 and print a JSON object containing `plan`, `extend_below_crop`, and `notes`.
3. **Chose / turned down:** Chose `rig_scale: 0.5` (matching the 0.5 scale used for 1664x2432 paintings in `AUTHORING.md` §3) and `seethrough` verbatim from `inputs/seethrough.json`; turned down running `propose --head-box` because `inputs/layers/head` was already generated with `inputs/seethrough.json`.
4. **Happened:** Exited 0 and printed a 22-part `plan` (`hair_back`, `handwear_l`, `handwear_r`, `legwear`, `shoes`, `neck`, `bottomwear`, `topwear`, `hairpin`, `ear_l`, `ear_r`, `face`, `mouth`, `eyewhite_r`, `eyewhite_l`, `iris_l`, `iris_r`, `lash_l`, `lash_r`, `brow_r`, `brow_l`, `hair_front`), `extend_below_crop` for `hair_front` and `hair_back`, and 7 notes explaining empty unused layers and `nose`.

## Entry 2

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 step 6 & step 7 (`assemble`), and §5 (`assemble` output lines).
2. **Expect:** Copying `plan` and `extend_below_crop` into `config.json` and running `npx rig-parts assemble` into `work/` will exit 0, write `work/rig/parts.json` and `work/rig/parts/*.png`, and print per-part pixel counts along with `recomposite vs source` showing `uncovered error px <= 4200` and no large missing-body `uncovered:` warning.
3. **Chose / turned down:** Chose the proposed 22-part plan and `extend_below_crop` as printed; turned down adding `["nose", "head", "nose"]` because `AUTHORING.md` §4 step 6 states `nose` is never planned by default and only used for reading head pitch notes.
4. **Happened:** Exited 0, wrote 22 part PNGs and `parts.json`, and printed `recomposite vs source: mean |d|=1.13, within 8: 97.8%, error px > 40: 6275, uncovered error px: 2059` with 605 uncovered holes (largest 402 px at 405,1073 39x25 between `"shoes"` and `"legwear"`) and no missing-layer `uncovered:` line.

## Entry 3

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 step 7 (`propose --parts`) and §5 (`propose` row).
2. **Expect:** Running `npx rig-parts propose --parts runs/2026-10-20-gemini-4-argon-high-01-build/work/rig --source tasks/01-build/inputs/painting.png --out runs/2026-10-20-gemini-4-argon-high-01-build/work` will exit 0, write `work/proposal.json`, `work/basis.json`, and `work/render/landmarks.png`, and print `0 LINT line(s)` along with per-bone coverage lines.
3. **Chose / turned down:** Chose default `propose` (`--grid-rule figure`) without `--keypoints`; turned down `--keypoints` because `tasks/01-build/TASK.md` states the character is standing on white.
4. **Happened:** Exited 0, wrote `proposal.json` (21 bone entries, 8 meshes), `basis.json`, and `render/landmarks.png`, and printed `0 LINT line(s) over 8 mesh(es) and the hip` and `coverage: 40 bone(s) — 31 checked and clean, 0 checked with a LINT line, 9 not checked`.

## Entry 4

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 step 7 & step 9 (`build`), and `tasks/01-build/TASK.md`.
2. **Expect:** Copying `bones`, `meshes`, `regions`, and `motion` from `work/proposal.json` into `config.json` and running `npx rig-parts build --config runs/2026-10-20-gemini-4-argon-high-01-build/config.json --source tasks/01-build/inputs/painting.png --full tasks/01-build/inputs/layers/full --head tasks/01-build/inputs/layers/head --out runs/2026-10-20-gemini-4-argon-high-01-build/out` will exit 0 with `check: PASS; 10 of 10 bar(s) measured, 0 skipped` and `build: PASS`.
3. **Chose / turned down:** Chose to copy `bones`, `meshes`, `regions`, and `motion` from `work/proposal.json` unmodified since `propose` reported `0 LINT line(s)`; turned down modifying any bone positions before running `build`.
4. **Happened:** Exited 0 with `[check] check: PASS; 10 of 10 bar(s) measured, 0 skipped`, `uncovered_error_px 2059`, `ANIMATIONS_DO_NOT_FOLD: PASS`, and `build: PASS`.

## Entry 5

1. **Read:** `README.md` (Submitting: `python3 grade.py runs/<run>` writes `result.json`) and `tasks/01-build/TASK.md` (Pass lines: Built, Checked, Whole, Does not fold).
2. **Expect:** Running `python3 grade.py runs/2026-10-20-gemini-4-argon-high-01-build` will exit 0, print 4 PASS lines (`Built`, `Checked`, `Whole`, `Does not fold`) with `4 / 4`, and write `result.json`.
3. **Chose / turned down:** Chose to run `grade.py` on the current `config.json` without further edits; turned down adding `assemble.patches` for the 402 px hole between `shoes` and `legwear` because `uncovered_error_px` is 2059, well below the 4,200 ceiling.
4. **Happened:** Exited 0, printed `4 of 4 line(s)` (`built`, `checked`, `whole`, `does_not_fold` all PASS), and wrote `result.json`.

## At the end

- **Where I guessed:** `assemble.rig_scale: 0.5` was chosen from the convention in `AUTHORING.md` §3 (`0.5 in both examples (a 1664x2432 painting makes an 832x1216 rig)`) rather than a required value in `TASK.md`; every other value came from `inputs/seethrough.json`, `assemble --propose-plan`, and `propose`.
- **What I could not find:** Nothing for this task; the standard command order in `AUTHORING.md` §4 passed all 4 bars unmodified.





