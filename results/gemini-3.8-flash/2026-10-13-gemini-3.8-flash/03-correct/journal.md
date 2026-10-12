# Journal — gemini-3.8-flash, 03-correct, 2026-10-13

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry 1

1. **Read:** `tasks/03-correct/TASK.md` and `tasks/03-correct/inputs/seethrough.json` (`head_box: [538, 158, 1100, 720]`).
2. **Expect:** Create initial `runs/2026-10-13-gemini-3.8-flash-03-correct/config.json` containing `key`, `seethrough`, and `assemble.rig_scale`.
3. **Chose / turned down:** Chose key "character", seethrough from `inputs/seethrough.json`, and scale 0.5. Turned down omitting head_box as `assemble --propose-plan` requires it.
4. **Happened:** Created `config.json` with key, seethrough settings, and assemble.rig_scale as expected.

## Entry 2

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 "The command order" (step 6: `assemble --propose-plan` output).
2. **Expect:** Update `runs/2026-10-13-gemini-3.8-flash-03-correct/config.json` with proposed `assemble.plan` (22 parts) and `assemble.extend_below_crop` (2 entries).
3. **Chose / turned down:** Chose adopting proposed plan and extend_below_crop. Turned down altering headwear allocation because the rule cleanly picked the full run for headwear.
4. **Happened:** Updated `config.json` with assemble.plan (22 parts) and assemble.extend_below_crop (2 entries) as expected.

## Entry 3

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 "The command order" (step 7: `assemble`).
2. **Expect:** `rig-parts assemble` slices parts into `work/03-correct/rig/parts/` and writes `work/03-correct/rig/parts.json`, exiting 0.
3. **Chose / turned down:** Chose running `rig-parts assemble` to prepare measured parts into `work/03-correct`. Turned down skipping assemble because propose requires assembled parts.
4. **Happened:** Assemble wrote 22 parts into `work/03-correct/rig/parts/` with uncovered error px 1726 (<= 3500), exiting 0 as expected.

## Entry 4

1. **Read:** `tasks/03-correct/TASK.md` and `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 "The command order" (step 7: `propose`).
2. **Expect:** `rig-parts propose` drafts bones, meshes, regions, and motion into `work/03-correct/proposal.json` and exits 0.
3. **Chose / turned down:** Chose running standard `propose` to obtain the tool's proposed baseline draft. Turned down applying premature corrections before inspecting the tool's proposed output and check failures.
4. **Happened:** Propose wrote `proposal.json` with 22 bone entries, 8 meshes, and 0 LINT lines, exiting 0 as expected.

## Entry 5

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 "The command order" (step 7: "Copy `bones`, `meshes`, `regions` and `motion` into the config").
2. **Expect:** Update `runs/2026-10-13-gemini-3.8-flash-03-correct/config.json` with bones, meshes, regions, and motion blocks from `work/03-correct/proposal.json`.
3. **Chose / turned down:** Chose merging proposed draft blocks as-is into config.json to test the draft build. Turned down making pre-emptive modifications so the tool's check errors can be directly observed.
4. **Happened:** Merged draft bones, meshes, regions, and motion from proposal into `config.json` as expected.

## Entry 6

1. **Read:** `tasks/03-correct/TASK.md` ("On this painting, what the tool proposes does not pass its own check as proposed") and `README.md` rule 5.
2. **Expect:** `python3 grade.py runs/2026-10-13-gemini-3.8-flash-03-correct` builds the proposed draft and passes all check bars.
3. **Chose / turned down:** Chose running the grader on the draft proposal to observe the build output and check results. Turned down premature hand edits before seeing the tool's diagnostic messages.
4. **Happened:** SURPRISE: Grader reported build exit 1 because check bar TEXTURE_STRETCH failed on mesh "hair_back" (severity 15.338 against ceiling 1.926544 on triangle 167 at frame 22) — the proposed draft allows excessive deformation between chains pulling the same hair_back mesh.

## Entry 7

1. **Read:** `.grade/2026-10-13-gemini-3.8-flash-03-correct/grade.log` line 88 (`FAIL CHECK_TEXTURE_STRETCH: mesh "hair_back" triangle 167 ... the texture on it is squeezed: the bones this mesh is weighted to move apart (amplitudes too large down a chain), or a vertex blends bones that move against each other`) and `node_modules/@rig-c/parts/docs/AUTHORING.md` §6 (`CHECK_TEXTURE_STRETCH`).
2. **Expect:** Update `runs/2026-10-13-gemini-3.8-flash-03-correct/config.json` so `motion.tracks` for `hairback_l` uses `amps: [0.6, 1.4, 2.4]` matching `hairback_r`.
3. **Chose / turned down:** Chose aligning the rotational amplitudes of `hairback_l` with `hairback_r` (+0.6, +1.4, +2.4) so the single low ponytail sways together without stretching its central triangles. Turned down making `hair_back` rigid because `Kept` requires at least 8 deformed meshes.
4. **Happened:** Updated `config.json` setting `hairback_l` amplitudes to `[0.6, 1.4, 2.4]` to match `hairback_r` as expected.

## Entry 8

1. **Read:** `tasks/03-correct/TASK.md` (Pass lines: Built, Checked, Whole, Does not fold, Kept) and `README.md` rule 5.
2. **Expect:** `python3 grade.py runs/2026-10-13-gemini-3.8-flash-03-correct` passes 5 of 5 lines (`built`, `checked`, `whole`, `does_not_fold`, `kept`) and writes `result.json`.
3. **Chose / turned down:** Chose running the grader to confirm the corrected hairback tracks resolve `TEXTURE_STRETCH` and pass all bars. Turned down further edits as the fix cleanly addresses the failure.
4. **Happened:** Grader passed 5 of 5 lines (`built`, `checked`, `whole` 1726 <= 3500, `does_not_fold` [], `kept` 8 >= 8) and wrote `result.json` as expected.

## At the end

- **Where I guessed:** None. All initial values came from `inputs/seethrough.json`, `assemble --propose-plan`, or `propose`. The amplitude correction for `hairback_l` (+0.6, +1.4, +2.4) directly matched `hairback_r` to ensure synchronized sway.
- **What I could not find:** None. The diagnostic failure message in `grade.log` and `node_modules/@rig-c/parts/docs/AUTHORING.md` §6 clearly explained that opposing bone motion on shared mesh vertices caused the texture stretch.














