# Journal — gemini-3.8-flash, 01-build, 2026-10-13

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry 1

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 "The command order" (loader `layers`: requires `key`, `seethrough`, `assemble.rig_scale`, `seethrough.head_box`) and `tasks/01-build/inputs/seethrough.json`.
2. **Expect:** A valid JSON file `runs/2026-10-13-gemini-3.8-flash-01-build/config.json` containing `key`, `seethrough`, and `assemble.rig_scale`.
3. **Chose / turned down:** Chose key "character", seethrough settings from `inputs/seethrough.json` with head_box, and assemble.rig_scale 0.5. Turned down omitting head_box since assemble --propose-plan requires it.
4. **Happened:** Created `config.json` with key, seethrough settings, and assemble.rig_scale as expected.

## Entry 2

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 "The command order" (step 6: `assemble --propose-plan` output).
2. **Expect:** Update `runs/2026-10-13-gemini-3.8-flash-01-build/config.json` with proposed `assemble.plan` (22 parts) and `assemble.extend_below_crop` (2 entries).
3. **Chose / turned down:** Chose the proposed plan and extend_below_crop verbatim as recommended. Turned down manual adjustments because `notes` was empty and all 22 layers resolved cleanly.
4. **Happened:** Updated `config.json` with assemble.plan (22 parts) and assemble.extend_below_crop (2 entries) as expected.

## Entry 3

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 "The command order" (step 7: `assemble`).
2. **Expect:** `rig-parts assemble` slices parts into `work/01-build/rig/parts/` and writes `work/01-build/rig/parts.json`, exiting 0.
3. **Chose / turned down:** Chose running `rig-parts assemble` to generate measured parts into `work/01-build`. Turned down skipping to `propose` because `propose` requires assembled parts.
4. **Happened:** Assemble wrote 22 parts into `work/01-build/rig/parts/`, `parts.json`, and recomposite images with uncovered error px 2059 (below 4,200), exiting 0 as expected.

## Entry 4

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 "The command order" (step 7: `propose`).
2. **Expect:** `rig-parts propose` writes `work/01-build/proposal.json`, `basis.json`, and overlay landmarks, printing proposed bone coverage and LINT lines.
3. **Chose / turned down:** Chose running `propose` on the assembled parts to obtain the draft skeleton and mesh/region mappings. Turned down authoring bones and meshes by hand since propose automates standard standing poses.
4. **Happened:** Propose wrote `proposal.json` with 21 bone entries, 8 meshes, and 0 LINT lines, exiting 0 as expected.

## Entry 5

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 "The command order" (step 7: "Copy `bones`, `meshes`, `regions` and `motion` into the config").
2. **Expect:** Update `runs/2026-10-13-gemini-3.8-flash-01-build/config.json` with bones (21 items), meshes (8 items), regions (14 items), and motion blocks from `work/01-build/proposal.json`.
3. **Chose / turned down:** Chose copying proposed bones, meshes, regions, and motion verbatim since propose reported 0 LINT lines. Turned down manual adjustments prior to validation via `propose --from-config`.
4. **Happened:** Merged bones, meshes, regions, and motion from proposal into `config.json` as expected.

## Entry 6

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 "The command order" (step 8: `propose --from-config`).
2. **Expect:** `rig-parts propose --from-config` validates bones in `config.json` against mesh artwork and exits 0 with 0 LINT lines.
3. **Chose / turned down:** Chose validating the populated `config.json` using `propose --from-config`. Turned down proceeding straight to `build` without verifying LINT status.
4. **Happened:** Validated `config.json` with 0 LINT lines over 8 meshes and 40 bones, exiting 0 as expected.

## Entry 7

1. **Read:** `tasks/01-build/TASK.md` (Pass lines: Built, Checked, Whole, Does not fold) and `README.md` rule 5 ("The grader rebuilds").
2. **Expect:** `python3 grade.py runs/2026-10-13-gemini-3.8-flash-01-build` passes 4 of 4 lines (`built`, `checked`, `whole`, `does_not_fold`) and writes `result.json`.
3. **Chose / turned down:** Chose running `python3 grade.py` to rebuild from `config.json` and verify all bars. Turned down running standalone build beforehand since `grade.py` runs the exact canonical build and measures all criteria.
4. **Happened:** Grader passed 4 of 4 lines (`built`, `checked`, `whole` 2059 px <= 4200, `does_not_fold` []) and wrote `result.json` as expected.

## At the end

- **Where I guessed:** None. All values were sourced directly from `inputs/seethrough.json`, `assemble --propose-plan`, or `propose`. The `assemble.rig_scale` 0.5 was taken from `AUTHORING.md` §3.
- **What I could not find:** None. The instructions and document sections in `AUTHORING.md` (§4, §6) clearly guided the entire authoring loop.












