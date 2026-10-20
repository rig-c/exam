# Journal — gemini-3.8-flash-medium, 03-correct, 2026-10-20

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry 1

1. **Read:** `tasks/03-correct/inputs/seethrough.json` and `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 step 6.
2. **Expect:** Minimal `config.json` created with `key: "exam-03"`, `seethrough` block from `inputs/seethrough.json`, and `assemble.rig_scale: 0.5`.
3. **Chose / turned down:** Created early config for `assemble --propose-plan`; turned down guessing the plan by hand.
4. **Happened:** Created `config.json` with early config parameters for task 03.

## Entry 2

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4, step 6: `rig-parts assemble --propose-plan`.
2. **Expect:** `assemble --propose-plan` outputs a proposed plan and `extend_below_crop` list for the seated character painting.
3. **Chose / turned down:** Running `assemble --propose-plan` to get the proposed part plan; turned down hand-authoring parts.
4. **Happened:** `assemble --propose-plan` produced 22 plan rows and 2 extend_below_crop entries.

## Entry 3

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4, step 6: paste plan and extend_below_crop into `config.assemble`.
2. **Expect:** `config.json` updated with proposed plan for task 03.
3. **Chose / turned down:** Applied proposed plan directly into `config.json`; turned down manual changes to plan.
4. **Happened:** Updated `config.json` with 22 plan rows and 2 extend_below_crop entries.

## Entry 4

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4, step 7: `rig-parts assemble ... --out work`.
2. **Expect:** `assemble` will write `work/rig/parts.json` and 22 part PNGs, reporting uncovered holes and error stats.
3. **Chose / turned down:** Running `assemble` to assemble parts for `propose`; turned down skipping this step.
4. **Happened:** `assemble` wrote `work/rig/parts.json` and 22 part PNGs. Uncovered error px is 1726 (<= 3500 threshold).

## Entry 5

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4, step 7: `rig-parts propose --parts work/rig --source inputs/painting.png --out work`.
2. **Expect:** `propose` drafts bones, meshes, regions, motion into `work/proposal.json`, and reports any LINT warnings or stretch issues.
3. **Chose / turned down:** Running `propose` to obtain the baseline proposal and identify what fails.
4. **Happened:** `propose` drafted `work/proposal.json` and printed 1 LINT line: `hairback_r` and `hairback_l` on mesh 'hair_back' squeeze it due to opposed amplitudes ([0.6, 1.4, 2.4] vs [-0.6, -1.4, -2.4]) on tips 39.0 px apart, suggesting "give both the same sign (then 1.046)".

## Entry 6

1. **Read:** `propose` LINT message ("give both the same sign (then 1.046)") and `tasks/03-correct/TASK.md` Still moves line ("The draft's own amplitudes give 45.9 once what is wrong with them is put right").
2. **Expect:** Merging proposal into `config.json` with `hairback_l.amps` flipped to positive `[0.6, 1.4, 2.4]` will eliminate the squeeze while preserving back hair travel.
3. **Chose / turned down:** Set `hairback_l.amps` to `[0.6, 1.4, 2.4]` matching `hairback_r`; turned down dropping `hairback_l` or reducing amplitude values which would degrade hair motion.
4. **Happened:** Merged proposal into `config.json` and changed `hairback_l` amplitudes from `[-0.6, -1.4, -2.4]` to `[0.6, 1.4, 2.4]`.

## Entry 7

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4, step 8: `propose ... --from-config config.json`.
2. **Expect:** `propose --from-config` reports 0 LINT lines and exits 0 now that amplitudes share sign.
3. **Chose / turned down:** Running `propose --from-config` to confirm elimination of LINT error; turned down moving straight to build without verification.
4. **Happened:** `propose --from-config` exited 0 with 0 LINT lines.

## Entry 8

1. **Read:** `grade.py` lines 240-244 and `tasks/03-correct/TASK.md` Pass lines.
2. **Expect:** `python3 grade.py runs/2026-10-20-gemini-3.8-flash-medium-03-correct` passes all 6 lines: built, checked, whole, does_not_fold, kept (>= 8 meshes deformed), still_moves (>= 23 rig px).
3. **Chose / turned down:** Running `grade.py` to verify the build and grading criteria.
4. **Happened:** python3 grade.py passed 6 of 6 lines (built, checked, whole, does_not_fold, kept, still_moves [45.881 px]).

## At the end

- **Where I guessed:** None. The correction was directly instructed by the tool's LINT output ("give both the same sign (then 1.046)").
- **What I could not find:** None; the diagnostic reporting from `propose` pin-pointed the mesh squeeze issue and the exact remedy.
