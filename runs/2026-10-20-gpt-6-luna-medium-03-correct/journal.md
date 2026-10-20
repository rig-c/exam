# Journal — gpt-6-luna-medium, 03-correct, 2026-10-20

## Entry 1

1. **Read:** `tasks/03-correct/TASK.md`; `tasks/03-correct/inputs/seethrough.json`; `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 steps 1–6.
2. **Expect:** the recorded See-through settings and scale will let `inputs` write the correct square and head-crop images.
3. **Chose / turned down:** use the task's existing painting and layers; no new See-through run is needed.
4. **Happened:** `inputs` wrote the full square and 562x562 head crop; proposed head box matched the recorded box exactly.


## Entry 2

1. **Read:** `rig-parts assemble --propose-plan` output, especially the headwear and nose notes; `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 step 6.
2. **Expect:** adding the 22 proposed plan rows, the full-run headwear override, continuations, and nose row will let `assemble` produce the parts and uncovered-pixel report.
3. **Chose / turned down:** retain the proposed order and add nose as instructed so the head pitch can be read.
4. **Happened:** assembled 23 parts; recomposite uncovered_error_px is 1726 (under 3500), with 444 holes.


## Entry 3

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 step 7; assembled `work/rig/parts.json` and recomposite report.
2. **Expect:** `propose` will create bones, meshes, regions and idle motion plus notes and landmark overlays that reveal any draft issue.
3. **Chose / turned down:** use the proposal as the measured baseline before changing it.
4. **Happened:** `propose` wrote 22 bone entries and 8 meshes, then named the defect: `hairback_r`/`hairback_l` oppose each other on `hair_back`; an edge closes to 0.064x rest (severity 15.572 > 1.926544); same signs predict 1.046.


## Entry 4

1. **Read:** `tasks/03-correct/work/proposal.json` `motion.tracks`; the `LINT hairback_r and hairback_l on mesh 'hair_back'` line from `propose`.
2. **Expect:** copying the proposal into config and changing only `hairback_l.amps` from `[-0.6, -1.4, -2.4]` to `[0.6, 1.4, 2.4]` will remove the squeeze while preserving the proposal's back-hair motion.
3. **Chose / turned down:** match `hairback_l` signs to `hairback_r`, as the LINT remedy predicts; retain both chains rather than dropping one.
4. **Happened:** changed only `hairback_l.amps` to `[0.6, 1.4, 2.4]`; build and check passed, 8 meshes deform, and the same-sign idle cleared the squeeze.


## Entry 5

1. **Read:** `tasks/03-correct/TASK.md` hand-in and pass lines; completed build output.
2. **Expect:** staging the corrected config and running the official grader will verify all six lines, including retained back-hair motion.
3. **Chose / turned down:** run the grader against the submitted config and preserve its exact output.
4. **Happened:** grader passed all 6 lines; 8 meshes deform and back hair travels 45.881 rig px against the head.
