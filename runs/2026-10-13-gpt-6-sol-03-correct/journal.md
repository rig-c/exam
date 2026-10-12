# Journal — gpt-6-sol, 03-correct, 2026-10-13

## Entry 1

1. **Read:** `tasks/03-correct/TASK.md` Given, `inputs/seethrough.json`, and `@rig-c/parts/docs/AUTHORING.md` §4 loader table: the plan step needs key, See-through fields, and rig scale.
2. **Expect:** A valid minimal `config.json` with the recorded 1024 resolution, `[538,158,1100,720]` head box, and 0.5 rig scale.
3. **Chose / turned down:** Start with recorded input settings and the same authored scale as 01; turned down borrowing the first painting's plan or bones.
4. **Happened:** `config.json` was created with only key, recorded See-through fields, and the 0.5 scale.

## Entry 2

1. **Read:** `@rig-c/parts/docs/AUTHORING.md` §4 step 6 and `assemble --propose-plan` output: 22 parts, two hair extensions; the headwear note says head run 5 rig px versus full run 2146, so use full.
2. **Expect:** The config gains all 22 plan rows and two hair extensions exactly as printed, with `hairpin` from `full:headwear`.
3. **Chose / turned down:** Copy the printed plan; turned down the head-run headwear because its measured area is nearly empty.
4. **Happened:** `config.json` now carries all 22 proposed rows, including full-run `hairpin`, and both hair extensions.

## Entry 3

1. **Read:** `@rig-c/parts/docs/AUTHORING.md` §4 step 7 and §5 assemble: assembly measures part coverage and uncovered holes.
2. **Expect:** `rig-parts assemble` exits 0, writes 22 parts, and reports uncovered error pixels around the expected plan scale (the grader comments about 1,726 for this painting).
3. **Chose / turned down:** Assemble to measure this painting's plan; turned down adding patches before the tool names uncovered areas.
4. **Happened:** Assembly exited 0, wrote 22 parts, and reported `uncovered error px: 1726`, below the 3500 task line; its largest hole was 154 px near shoes and legwear.

## Entry 4

1. **Read:** `@rig-c/parts/docs/AUTHORING.md` §4 step 7: proposal writes bones, meshes, regions, motion, landmarks, basis, and LINT lines against assembled parts.
2. **Expect:** `rig-parts propose` exits 0, drafts eight meshes, and names any seated-pose geometry problem in notes or LINT lines.
3. **Chose / turned down:** Draft from this painting's 22 assembled parts; turned down using the standing character's bone coordinates.
4. **Happened:** Proposal exited 0, drafted 22 bone entries and 8 meshes, printed 0 LINT lines, and wrote landmarks and basis; the seated skirt roots appeared tightly grouped in the overlay.

## Entry 5

1. **Read:** `@rig-c/parts/docs/AUTHORING.md` §4 step 7 and `work/proposal.json`: the full loader needs its generated bones, meshes, regions, and motion.
2. **Expect:** `config.json` gains those four proposal sections verbatim and remains parseable for a baseline build.
3. **Chose / turned down:** Use the exact draft first so its failure is recorded; turned down preemptively changing the skirt from the visual overlay alone.
4. **Happened:** `config.json` now contains the proposal's 22 bone entries, 8 meshes, regions, and idle motion without corrections.

## Entry 6

1. **Read:** `tasks/03-correct/TASK.md` Do and `@rig-c/parts/docs/AUTHORING.md` §5 check: the build's check names failed bars and quantitative thresholds.
2. **Expect:** The uncorrected draft builds its rig but exits 1 at check, with the seated-pose failure named and its found and required figures printed.
3. **Chose / turned down:** Run the exact build command to capture the first failure; turned down substituting a guessed correction for the tool's message.
4. **Happened:** Build exited 1 at check: `CHECK_TEXTURE_STRETCH` named `hair_back` triangle 167, edge 37-117, idle frame 22, ratio 0.065 and severity 15.338 against <= 1.926544; the other six judgement bars passed and 8 meshes remained.

## Entry 7

1. **Read:** The exact `CHECK_TEXTURE_STRETCH` refusal above; `@rig-c/parts/docs/AUTHORING.md` §6 says an edge squeezed this way can come from excessive chain amplitudes or a vertex blending opposing bones. `work/render/landmarks.png` shows `hair_back` as one part with two long chains, and `config.json` keys them with opposite ±0.6/1.4/2.4° amplitudes.
2. **Expect:** Reducing only the two `hairback_*` chain amplitudes to one quarter preserves eight deforming meshes and puts the worst edge under the 1.926544 stretch ceiling.
3. **Chose / turned down:** Scale the opposing back-hair motion down to ±0.15/0.35/0.6°; turned down deleting its mesh or making the hair rigid because the task requires keeping deformation.
4. **Happened:** Only the `hairback_r` and `hairback_l` idle `amps` arrays changed, from opposite ±0.6/1.4/2.4 to ±0.15/0.35/0.6; all eight mesh declarations remain.

## Entry 8

1. **Read:** The baseline `CHECK_TEXTURE_STRETCH` message and `@rig-c/parts/docs/AUTHORING.md` §6: the check reads the worst animated triangle edge after the change.
2. **Expect:** The corrected build exits 0, `TEXTURE_STRETCH` passes below 1.926544, and `check: PASS` keeps all eight meshes.
3. **Chose / turned down:** Rebuild with the same task command to isolate the amplitude change; turned down changing mesh topology in the same step because that would obscure which fix mattered.
4. **Happened:** Build exited 0 with `check: PASS; 9 of 9`; `TEXTURE_STRETCH` severity fell from 15.338 to 1.303, and the same worst edge's ratio rose from 0.065 to 0.768; 8 meshes and `uncovered_error_px 1726` remained.

## Entry 9

1. **Read:** `README.md` Submitting and `grade.py` main: the independent grader rebuilds the handed-in config, checks idle folds, counts the deformed meshes, and writes `result.json`.
2. **Expect:** Five PASS lines for 03: build, check, whole, no idle fold, and 8 kept meshes.
3. **Chose / turned down:** Grade the final config from only handed-in JSON; turned down trusting the local `out/` tree, which the grader ignores.
4. **Happened:** Grader exited 0 with five PASS lines, including no idle fold and `8 mesh(es) deformed against >= 8`; it wrote `result.json`.

## At the end

- **Where I guessed:** `key` and the 0.5 scale were authored from the task and guide. The choice to quarter the two hairback amplitude arrays was an initial corrective estimate; the rebuilt edge ratio and grader, not that estimate, establish the result.
- **What I could not find:** No measured target amplitude for the seated back hair was given. The refusal and subsequent check establish a safe value for this rig.
