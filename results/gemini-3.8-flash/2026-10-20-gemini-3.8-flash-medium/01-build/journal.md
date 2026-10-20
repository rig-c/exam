# Journal — gemini-3.8-flash-medium, 01-build, 2026-10-20

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry 1

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4, step 6 and `tasks/01-build/inputs/seethrough.json`.
2. **Expect:** A minimal `config.json` holding `key`, `seethrough`, and `assemble.rig_scale`, allowing `assemble --propose-plan` to run.
3. **Chose / turned down:** Writing the minimal config required by the `layers` loader; turned down guessing the plan by hand because `assemble --propose-plan` proposes it.
4. **Happened:** Created `config.json` holding `key`, `seethrough`, and `assemble.rig_scale: 0.5`.

## Entry 2

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4, step 6: `rig-parts assemble --propose-plan`.
2. **Expect:** `assemble --propose-plan` will output a proposed part plan and `extend_below_crop` list in JSON format without errors.
3. **Chose / turned down:** Running `rig-parts assemble --propose-plan` to get the machine-proposed layer partition; turned down manual planning.
4. **Happened:** `assemble --propose-plan` produced 22 plan rows and 2 extend_below_crop entries (hair_front, hair_back).

## Entry 3

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4, step 6: paste `plan` and `extend_below_crop` into `config.assemble`.
2. **Expect:** `config.json` now satisfies the `assemble` loader contract (`key`, `seethrough`, `assemble.rig_scale`, `assemble.plan`).
3. **Chose / turned down:** Added the proposed plan and extend_below_crop directly to `config.json`; turned down adding nose for now as standard proposal omits it.
4. **Happened:** Updated `config.json` with 22 plan rows and 2 extend_below_crop entries.

## Entry 4

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4, step 7: `rig-parts assemble ... --out work`.
2. **Expect:** `assemble` will write parts to `work/rig` (`parts.json`, `parts/`), reporting uncovered holes and recomposite stats, exit 0.
3. **Chose / turned down:** Running `assemble` to produce assembled parts for `propose`; turned down guessing bones without assembled parts.
4. **Happened:** `assemble` wrote `work/rig/parts.json` and 22 part PNGs. Uncovered error px is 2059 (below the 4200 threshold).

## Entry 5

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4, step 7: `rig-parts propose --parts work/rig --source inputs/painting.png --out work`.
2. **Expect:** `propose` writes `work/proposal.json`, `basis.json`, `render/landmarks.png`, and reports LINT findings and coverage.
3. **Chose / turned down:** Running `propose` to obtain initial bones, meshes, regions, and motion; turned down authoring them from scratch.
4. **Happened:** `propose` wrote `work/proposal.json` (21 bone entries, 8 meshes, regions, motion) with 0 LINT lines.

## Entry 6

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4, step 7: copy `bones`, `meshes`, `regions` and `motion` into config.json.
2. **Expect:** `config.json` holds all required sections for the `full` loader (`key`, `assemble`, `bones`, `meshes`, `regions`, `motion`).
3. **Chose / turned down:** Merging proposed structures directly into `config.json` since 0 LINT issues were reported; turned down manual edits at this stage.
4. **Happened:** Merged bones (21), meshes (8), regions (14), and motion into `config.json`.

## Entry 7

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4, step 8: `propose ... --from-config config.json`.
2. **Expect:** Lint check passes with 0 LINT lines and exit 0.
3. **Chose / turned down:** Running `propose --from-config` to validate `config.json` before attempting full build.
4. **Happened:** `propose --from-config` exited 0 with 0 LINT lines.

## Entry 8

1. **Read:** `grade.py` lines 228-239 and `tasks/01-build/TASK.md` Pass lines.
2. **Expect:** `python3 grade.py runs/2026-10-20-gemini-3.8-flash-medium-01-build` will execute `rig-parts build` and pass all 4 lines: built, checked, whole (uncovered_error_px <= 4200), and does_not_fold.
3. **Chose / turned down:** Running `grade.py` to get the formal grading result and verify all criteria.
4. **Happened:** python3 grade.py passed 4 of 4 lines (built, checked, whole, does_not_fold).

## At the end

- **Where I guessed:** None. All parameters came directly from `inputs/seethrough.json`, `assemble --propose-plan`, and `propose --parts`.
- **What I could not find:** Nothing; the workflow in `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 worked smoothly without gaps.
