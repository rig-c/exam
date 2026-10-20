# Journal — claude-fable-5-1, 03-correct, 2026-10-20

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry <n>

1. **Read:** which document, section or message this step rests on (path and heading, or the message quoted).
2. **Expect:** what the step will produce, concretely — an exit code, a file, a number, a line of output.
3. **Chose / turned down:** what you are about to do, and the alternative you considered and why not.
4. **Happened:** what the step actually produced. If it differs from line 2, begin the line with
   `WTF?:` and say in one sentence what you now think you misread — or that nothing told you. Say it
   the way it landed. Politeness is not graded here; a line that understates the surprise hides it.

## At the end

- **Where I guessed:** every value you wrote without a source (a number, a name), and what you would
  have needed to read to not guess.
- **What I could not find:** questions you had that no document or message answered.

---

## Entry 1

1. **Read:** TASK.md (same command as task 01, uncovered bar 3,500, plus Kept ≥ 8 meshes and Still moves: back hair ≥ 23 rig px against the head, "the draft's own amplitudes give 45.9 once what is wrong with them is put right"); AUTHORING §3 *A posed figure* — "Sitting alone does not call for it: a seated figure whose skirt starts at the waist has its hip there (issue #314: a seated character proposed without joints … built green once its back-hair chains were fixed)", and "a pose file named by `generation.control.skeleton` is not that file": `inputs/pose_seated.json` is `{width 832, height 1216, points}` — the control-pose shape, not `spine-parts-keypoints/1`, so I will not feed it to `--keypoints`. `inputs/seethrough.json`: head_box [538, 158, 1100, 720]. `rig-parts layers` printed 0 WARN on both runs.
2. **Expect:** the same first two steps as task 01: config with key/seethrough/rig_scale 0.5 → `assemble --propose-plan` exits 0 with a plan of about 22 rows and the usual notes.
3. **Chose / turned down:** rig_scale 0.5 (same painting size); no keypoints (the guide's own seated precedent did without, and the file given is in the control-pose shape at 832x1216, which the keypoints reader would refuse by `spec`/`space`).
4. **Happened:** exit 0, 22 rows; one new note: `headwear: head run 5 rig px < 0.8 x full run 2146 -> full-run layer, drawn behind the face` (the hairpin comes from the full run this time). Otherwise as task 01. As expected.

## Entry 2

1. **Read:** AUTHORING §4 step 7 — paste plan and extend_below_crop, `assemble … --out work`, read `uncovered hole` lines; TASK.md's Whole bar is 3,500 here (grade.py's comment says the proposed plan leaves 1,726).
2. **Expect:** exit 0, 22 parts, `uncovered error px` in the low thousands, under 3,500.
3. **Chose / turned down:** plan as proposed; default seam and projection rules.
4. **Happened:** exit 0, 22 parts, `uncovered error px: 1726`, 444 holes, the largest 154 px between shoes and legwear. Under 3,500. As expected.

## Entry 3

1. **Read:** AUTHORING §4 step 7, `propose --parts work/rig --source … --out work`; the task says the draft does not pass as proposed, and README *What is in a round* says "on 1.13.0 `propose` names task 03's fault itself, one step before the build".
2. **Expect:** exit 0 with a proposal; among its `note:` or `LINT` lines one that names the back hair — the grade comment speaks of the back hair's "two chains" agreeing — probably two hair_back chains drafted with amplitudes or phases that do not agree, or a chain off its art.
3. **Chose / turned down:** default rules, no keypoints (entry 1).
4. **Happened:** exit 0, 22 bone entries, 8 meshes, and one LINT line that names the fault — `LINT hairback_r and hairback_l on mesh 'hair_back' squeeze it: swung together, every other bone held, edge 37-117 of triangle 167 closes to 0.064 times its rest length at idle frame 22 (max(ratio, 1/ratio) 15.572; <= 1.926544 is required, check's TEXTURE_STRETCH bar) … Their tips are 39.0 px apart and their amplitudes are opposed (hairback_r [0.6, 1.4, 2.4], hairback_l [-0.6, -1.4, -2.4]), so their tips swing towards each other and apart: give both the same sign (then 1.046), or drop one chain`. In `proposal.json` the two chains run from [358,219] and [450,219] down to tips [386,614] and [425,614]; on `landmarks.png` the back hair is one ponytail falling in front of the chest, and the two chains converge on it. As expected in kind (the back hair, two chains), and the message says the correction.

## Entry 4

1. **Read:** the LINT line above (`give both the same sign (then 1.046), or drop one chain`); TASK.md *Still moves* ("a part is not made to pass by turning its motion down" — the draft's own amplitudes give 45.9 once put right) and *Kept* (eight meshes still deform). AUTHORING §4 step 8: `propose --from-config` until no LINT line.
2. **Expect:** after pasting the proposal and flipping `hairback_l`'s amps to [0.6, 1.4, 2.4], `propose … --from-config config.json` exits 0 with `0 LINT line(s)`.
3. **Chose / turned down:** the same sign, keeping both chains and their amplitudes — the first remedy the line names, and the one that keeps the motion the Still-moves bar reads; turned down dropping a chain (the second remedy; it halves what moves the ponytail) and lowering the amplitudes (the bar forbids it and the line did not suggest it).
4. **Happened:** exit 0, `0 LINT line(s) over 8 mesh(es) and the hip`, 37 checked and clean. As expected.

## Entry 5

1. **Read:** TASK.md *Do* command; AUTHORING §4 step 9; the LINT line's own prediction that with the same sign the squeeze reads 1.046.
2. **Expect:** exit 0, `check: PASS; 10 of 10`, `TEXTURE_STRETCH` worst below 1.926544 on hair_back, `build: PASS`, about 1–2 minutes.
3. **Chose / turned down:** the exact task command; nothing else changed in the config.
4. **Happened:** exit 0, `check: PASS; 10 of 10 bar(s) measured, 0 skipped`, `build: PASS` in 2m50s. `TEXTURE_STRETCH: PASS — meshes 8; triangles 722; … severity 1.126` (worst hair_front triangle 86, min ratio 0.888); `ANIMATIONS_DO_NOT_FOLD: PASS — 0 folding mesh(es)`; `RECOMPOSITE_HOLES … uncovered_error_px 1726`. As expected.

## Entry 6

1. **Read:** TASK.md's six pass lines; grade.py reads `TEXTURE_STRETCH.meshes` for Kept and `travel(idle_geo, 'hair_back', 'head')` for Still moves (≥ 23; the draft's own amplitudes give 45.9).
2. **Expect:** 6 of 6: built, checked, `uncovered_error_px 1726 against <= 3500`, no folds, `8 mesh(es) deformed`, back hair travels about 45.9 rig px against the head.
3. **Chose / turned down:** grade once.
4. **Happened:** `6 of 6 line(s)`: `kept: 8 mesh(es) deformed against >= 8`, `still_moves: the back hair travels 45.881 rig px against the head over the idle, against >= 23`, `uncovered_error_px 1726 against <= 3500`. As expected — 45.881 is the task's 45.9.

## At the end

- **Where I guessed:** `assemble.rig_scale: 0.5` (as in task 01); the choice between the LINT's two remedies was a reading of the task's bars, not a guess. Everything else was copied from the proposer and corrected only where the LINT line pointed.
- **What I could not find:** what `inputs/pose_seated.json` was for — the task does not mention it, its shape is the control-pose file (`generation.control.skeleton` names it in `generation.json`), and the guide says that file is not a keypoints file; I decided from the guide's seated precedent (#314) and from the fact that the LINT line already named the fault that no keypoints were needed. What I decided from: the `LINT hairback_r and hairback_l … squeeze it` line (the message) and `work/render/landmarks.png` (the picture — the two chains converging on one ponytail), in that order.
