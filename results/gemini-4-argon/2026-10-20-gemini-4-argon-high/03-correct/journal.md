# Journal — gemini-4-argon-high, 03-correct, 2026-10-20

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry 1

1. **Read:** `tasks/03-correct/TASK.md`, `tasks/03-correct/inputs/seethrough.json`, and `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 step 6 (`assemble --propose-plan`).
2. **Expect:** Writing an initial `config.json` with `key: "03-correct"`, `seethrough` from `inputs/seethrough.json`, and `assemble: { "rig_scale": 0.5 }`, then running `npx rig-parts assemble --propose-plan` will exit 0 and print a JSON object with `plan`, `extend_below_crop`, and `notes`.
3. **Chose / turned down:** Chose `rig_scale: 0.5` and `seethrough` verbatim from `inputs/seethrough.json`; turned down running `propose --head-box` since `inputs/layers/head` is already provided.
4. **Happened:** Exited 0 and printed a 22-part `plan` (with `hairpin` taken from `"full"` because `headwear: head run 5 rig px < 0.8 x full run 2146`), `extend_below_crop` for `hair_front` and `hair_back`, and 8 notes.

## Entry 2

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 step 6 & step 7 (`assemble`), and `tasks/03-correct/TASK.md` (Whole: `uncovered_error_px <= 3500`).
2. **Expect:** Copying `plan` and `extend_below_crop` into `config.json` and running `npx rig-parts assemble` into `work/` will exit 0, write `work/rig/parts.json` and 22 part PNGs, and report `uncovered error px <= 3500`.
3. **Chose / turned down:** Chose the proposed `plan` and `extend_below_crop` verbatim; turned down adding `["nose", "head", "nose"]`.
4. **Happened:** Exited 0, wrote `work/rig/parts.json` and 22 part PNGs, and printed `recomposite vs source: mean |d|=1.09, within 8: 97.9%, error px > 40: 6164, uncovered error px: 1726` with 444 uncovered holes (largest 154 px).

## Entry 3

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 step 7 (`propose --parts`) and `tasks/03-correct/TASK.md` ("On this painting, what the tool proposes does not pass its own check as proposed").
2. **Expect:** Running `npx rig-parts propose --parts runs/2026-10-20-gemini-4-argon-high-03-correct/work/rig --source tasks/03-correct/inputs/painting.png --out runs/2026-10-20-gemini-4-argon-high-03-correct/work` will write `work/proposal.json`, `work/basis.json`, and `work/render/landmarks.png`, and print `LINT` or `note:` lines identifying the fault in the draft (specifically involving `hair_back`'s two chains disagreeing, as hinted by `TASK.md`'s "Still moves" bar).
3. **Chose / turned down:** Chose to run `propose` with default flags first to read its exact `LINT` and `note:` output; turned down passing `--keypoints` since no keypoints file is given in `tasks/03-correct/inputs/`.
4. **Happened:** Exited 0, wrote `work/proposal.json` (22 bone entries, 8 meshes), and printed 1 `LINT` line: `LINT hairback_r and hairback_l on mesh 'hair_back' squeeze it: swung together, every other bone held, edge 37-117 of triangle 167 closes to 0.064 times its rest length at idle frame 22 (max(ratio, 1/ratio) 15.572; <= 1.926544 is required, check's TEXTURE_STRETCH bar) — vertex 37 rides hairback_r2 0.91971, vertex 117 rides hairback_l2 0.90416; alone, hairback_r reads 1.880 and hairback_l 1.883. Their tips are 39.0 px apart and their amplitudes are opposed (hairback_r [0.6, 1.4, 2.4], hairback_l [-0.6, -1.4, -2.4]), so their tips swing towards each other and apart: give both the same sign (then 1.046), or drop one chain`.

## Entry 4

1. **Read:** The `propose` `LINT` line above (`give both the same sign (then 1.046), or drop one chain`), `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 step 8 (`propose --from-config`), and `tasks/03-correct/TASK.md` ("Still moves: The draft's own amplitudes give 45.9 once what is wrong with them is put right").
2. **Expect:** Copying `bones`, `meshes`, `regions`, and `motion` from `work/proposal.json` into `config.json` with `hairback_l`'s track `amps` changed from `[-0.6, -1.4, -2.4]` to `[0.6, 1.4, 2.4]`, then running `npx rig-parts propose --parts runs/2026-10-20-gemini-4-argon-high-03-correct/work/rig --source tasks/03-correct/inputs/painting.png --out runs/2026-10-20-gemini-4-argon-high-03-correct/work --from-config runs/2026-10-20-gemini-4-argon-high-03-correct/config.json` will exit 0 and print `0 LINT line(s) over 8 mesh(es) and the hip`.
3. **Chose / turned down:** Chose changing `hairback_l`'s `amps` to `[0.6, 1.4, 2.4]` (same positive sign as `hairback_r`); turned down dropping one chain or reducing the amplitudes because `TASK.md`'s "Still moves" bar requires `hair_back` to travel >= 23 rig px against `head` and notes that the draft's own amplitudes give 45.9 once both chains agree.
4. **Happened:** Exited 0, wrote `work/render/landmarks_config.png`, and printed `0 LINT line(s) over 8 mesh(es) and the hip` and `coverage: 45 bone(s) — 37 checked and clean, 0 checked with a LINT line, 8 not checked`.

## Entry 5

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 step 9 (`build`) and `tasks/03-correct/TASK.md`.
2. **Expect:** Running `npx rig-parts build --config runs/2026-10-20-gemini-4-argon-high-03-correct/config.json --source tasks/03-correct/inputs/painting.png --full tasks/03-correct/inputs/layers/full --head tasks/03-correct/inputs/layers/head --out runs/2026-10-20-gemini-4-argon-high-03-correct/out` will exit 0 with `check: PASS; 10 of 10 bar(s) measured, 0 skipped` (`TEXTURE_STRETCH` on `hair_back` around 1.046) and `build: PASS`.
3. **Chose / turned down:** Chose to run `rig-parts build` with the corrected `config.json` directly; turned down any other edits since `propose --from-config` passed with 0 LINT lines.
4. **Happened:** Exited 0 with `[check] check: PASS; 10 of 10 bar(s) measured, 0 skipped` (`slot hair_back` severity 1.045, `uncovered_error_px 1726`, `ANIMATIONS_DO_NOT_FOLD: PASS`) and `build: PASS`.

## Entry 6

1. **Read:** `tasks/03-correct/TASK.md` (Pass lines: Built, Checked, Whole, Does not fold, Kept, Still moves) and `grade.py`.
2. **Expect:** Running `python3 grade.py runs/2026-10-20-gemini-4-argon-high-03-correct` will exit 0, print `6 of 6 line(s)` (`built`, `checked`, `whole`, `does_not_fold`, `kept` with 8 meshes, and `still_moves` with 45.9 rig px >= 23), and write `result.json`.
3. **Chose / turned down:** Chose to run `grade.py` directly on the green build; turned down any further adjustments.
4. **Happened:** Exited 0, printed `6 of 6 line(s)` (`built`, `checked`, `whole`, `does_not_fold`, `kept: "8 mesh(es) deformed against >= 8"`, and `still_moves: "the back hair travels 45.881 rig px against the head over the idle, against >= 23"`), and wrote `result.json`.

## At the end

- **Where I guessed:** `assemble.rig_scale: 0.5` was chosen from the convention in `AUTHORING.md` §3 (`0.5 in both examples`); every other value came directly from `inputs/seethrough.json`, `assemble --propose-plan`, `propose`, and the `propose` `LINT` message remedy (`give both the same sign (then 1.046)`).
- **What I could not find:** Nothing; `rig-parts propose` explicitly named the `hairback_r`/`hairback_l` opposed-amplitude squeeze on `hair_back` and the exact remedy (`give both the same sign`).






