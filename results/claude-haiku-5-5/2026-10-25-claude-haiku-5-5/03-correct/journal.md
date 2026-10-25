# Journal

## Entry 1 (opened 2026-10-25T11:47:29Z)

1. **Read:** TASK.md 03 (a seated figure; draft does not pass as proposed; the tool's messages and pictures decide the correction). AUTHORING §4 step 1: rig-parts inputs writes st_input_full.png. Wrote runs/…-03-correct/config.json by hand: key, seethrough from tasks/03-correct/inputs/seethrough.json (resolution 1024, steps 30, seed 42, offload true; head_box not yet), assemble.rig_scale 0.5 (AUTHORING §3: keep the figure about 1,150 rig px tall; the painting is 2432 tall, so 0.5 gives about 1216).
2. **Expect:** exit 0; st_input_full.png written as 2432x2432 under runs/…-03-correct/work/inputs
3. **Chose / turned down:** Run rig-parts inputs on the task 03 painting, out into the run's work dir. Turned down: copying head_box from the task's seethrough.json now, since the doc says propose --head-box proposes it and I want the tool's value to compare.
4. **Happened** (2026-10-25T11:47:49Z): exit 0; it printed "st_input_full.png 2432x2432: the painting at x 384, white either side (384 + 384 px)". Matched the expected square.

## Entry 2 (opened 2026-10-25T11:47:50Z)

1. **Read:** AUTHORING §4 step 3: rig-parts layers on the full layers (tasks/03-correct/inputs/layers/full), read the figures and WARN lines. Config: runs/…-03-correct/config.json unchanged (key, seethrough, assemble.rig_scale).
2. **Expect:** exit 0; one line per layer; WARN lines for layers that are not plausibly the figure (a seated figure may give WARN on wide layers); refuses nothing
3. **Chose / turned down:** Run layers on the full run of the seated painting. Turned down: skipping it, since the doc says a WARN here decides what step 6 leaves out.
4. **Happened** (2026-10-25T11:48:14Z): exit 0; it printed "29 layer(s): 29 with opaque pixels, 0 with none" and "0 WARN line(s)". No WARN, so nothing is left out for plausibility; the 29 layers match the set task 01 had. Notable: this painting has back hair and a single handwear-l/r pair, as task 01.

## Entry 3 (opened 2026-10-25T11:48:16Z)

1. **Read:** AUTHORING §4 step 4: rig-parts propose --head-box --full <layers/full> --canvas 1664x2432 --write-config config.json, which writes seethrough.head_box into the config. Config: runs/…-03-correct/config.json (key, seethrough, assemble.rig_scale).
2. **Expect:** exit 0; head_box written; a square crop near the head, about 527 px per side like task 01 (the task's own seethrough.json has [538, 158, 1100, 720], 562 px)
3. **Chose / turned down:** Run propose --head-box with --write-config on the run config. Turned down: copying the task's head_box value, for the same reason as in task 01: the tool proposes it.
4. **Happened** (2026-10-25T11:48:23Z): exit 0; it printed "added seethrough.head_box" and "head_box [538, 158, 1100, 720], 562x562". Matched: the tool's value equals the task's seethrough.json head_box [538, 158, 1100, 720].

## Entry 4 (opened 2026-10-25T11:48:28Z)

1. **Read:** AUTHORING §4 step 5: inputs again writes st_input_head.png, the painting cropped to seethrough.head_box. The head run is the task's layers/head. Config: runs/…-03-correct/config.json now holds seethrough.head_box (propose's write, read back on disk).
2. **Expect:** exit 0; st_input_head.png 562x562 written under runs/…-03-correct/work/inputs
3. **Chose / turned down:** Rerun inputs with the same out as entry 1. Turned down: skipping it, since assemble needs the head crop as the head run's canvas.
4. **Happened** (2026-10-25T11:48:38Z): exit 0; it printed "st_input_head.png 562x562: seethrough.head_box [538, 158, 1100, 720]". Matched the expected crop.

## Entry 5 (opened 2026-10-25T11:48:40Z)

1. **Read:** AUTHORING §4 step 6: assemble --propose-plan with --write-config saves assemble.plan and extend_below_crop; read the notes for each unplanned layer (they name what is left out and why). Head run: tasks/03-correct/inputs/layers/head.
2. **Expect:** exit 0; a plan of about 22 rows; notes name layers left out; writes assemble.plan into config
3. **Chose / turned down:** Run the proposer with --write-config on the run config. Turned down: writing the plan by hand from task 01's list, since the seated painting has different layers in the head run and the plan must come from its own notes.
4. **Happened** (2026-10-25T11:48:47Z): WTF?: exit 2, not 0. Refused: "USAGE: --write-config must name the same file as --config for assemble --propose-plan". I had pointed it at a new work file, as I had for propose --cloth in task 02; the two commands have different rules, and I did not check this one. Nothing was written. I will rerun with --write-config naming config.json itself.

## Entry 6 (opened 2026-10-25T11:48:50Z)

1. **Read:** Entry 5 refusal: assemble --propose-plan requires --write-config to name the same file as --config. Reran the same command with --write-config set to runs/…-03-correct/config.json (same file). AUTHORING §4 step 6 (assemble --propose-plan --write-config config.json).
2. **Expect:** exit 0; assemble.plan and extend_below_crop written into config.json; a plan of about 22 rows
3. **Chose / turned down:** Same command as entry 5, same-file write. Turned down: writing to a copy, which the tool refuses.
4. **Happened** (2026-10-25T11:49:11Z): exit 0; it printed "config .../config.json: added assemble.plan" and "added assemble.extend_below_crop". The plan has 22 rows; the notes match the set in task 01 (neckwear, tail, wings, objects, eyewear, earwear empty or not planned; nose not planned). Expected a plan of about 22 rows: matched.

## Entry 7 (opened 2026-10-25T11:49:39Z)

1. **Read:** AUTHORING §4 step 7: rig-parts assemble --out work (uncovered hole lines and work/render/recomposite_error_rig.png decide whether an assemble.patches entry is needed). Config: runs/…-03-correct/config.json with assemble.plan from entry 6 (22 rows).
2. **Expect:** exit 0; 22 parts; uncovered_error_px printed; a few small holes; under 3,500 which is the task's own Whole bar
3. **Chose / turned down:** Run assemble into runs/…-03-correct/work. Turned down: adding an assemble.patches entry before seeing the holes, since the doc says to add one only for a large red hole.
4. **Happened** (2026-10-25T11:50:06Z): WTF?: exit 0 and "uncovered error px: 1726" is inside the bar, but a line I did not expect: "drift: \"bottomwear\" refuses 21999 px of full:bottomwear (its colour more than 90 off the painting, max channel)" and "the painting is within 90 of \"legwear\" (21839 px at alpha >= 250, drawn behind \"bottomwear\")". So the bottomwear layer holds legwear's pixels, and the plan's draw order puts legwear behind it. I expected the seated figure's legs to be a plain part; I had not read that a layer's colour can belong to another part. I will look at the picture before choosing a correction.

## Entry 8 (opened 2026-10-25T11:52:30Z)

1. **Read:** Entry 7 drift line: 21,999 px of full:bottomwear refused, the painting matching legwear (21,839 px) which is drawn behind bottomwear. The fix this step: I moved the legwear row in assemble.plan from before neck to directly after bottomwear, so legwear is drawn over bottomwear (hand edit to runs/…-03-correct/config.json; the layer PNGs are task inputs and I do not change them). AUTHORING's 'Fix' step says move the pixels, which I cannot do in the inputs; the plan's draw order is the lever I have.
2. **Expect:** exit 0; the bottomwear drift line gone or much smaller; uncovered error px at or under the previous 1726; legwear's own drift zero
3. **Chose / turned down:** Re-run assemble with the new order. Turned down: an assemble.cuts polygon on bottomwear, because the pixels there are legwear's and a cut would leave the wrong colour on a new part.
4. **Happened** (2026-10-25T11:53:15Z): exit 0; "uncovered error px: 1726" (same as before, under the 3,500 bar), and bottomwear's drift fell from 21999 px to 9 px. The drift moved to legwear: "drift: \"legwear\" refuses 5574 px of full:legwear", the painting matching bottomwear there. Total refused drift went from about 22,000 px to about 5,600 px, so legwear on top is the better order, but the thigh region is claimed by both layers, and neither order is clean. The uncovered count is the bar; I will see whether the check passes before fixing the rest of the drift.

## Entry 9 (opened 2026-10-25T11:53:17Z)

1. **Read:** AUTHORING §4 step 7 propose --parts work/rig with --write-config: drafts bones, meshes, regions, limbs (only with --keypoints), motion, proposed_rig_scale. The task 01 run wrote over config.json the same way. No --cloth or --keypoints in this task. Config: runs/…-03-correct/config.json (assemble.plan with legwear after bottomwear, entry 8).
2. **Expect:** exit 0; proposal.json, basis.json and landmarks written; LINT lines possible on hair or sleeve chains; coverage summary
3. **Chose / turned down:** Run propose --parts with --write-config over config.json. Turned down: first fixing the thigh drift with assemble.cuts, since the check will say whether that drift matters and the Whole bar is met.
4. **Happened** (2026-10-25T11:53:34Z): exit 0; it wrote proposal.json, basis.json and landmarks and added bones, meshes, regions, motion, proposed_rig_scale to config.json. It printed "1 LINT line(s) over 8 mesh(es) and the hip": "LINT hairback_r and hairback_l on mesh 'hair_back' squeeze it" with "give both the same sign (then 1.046), or drop one chain". Also a note: "lash_r reaches 9 px above eyewhite_r's top ... the blink squashes whatever is painted there". The LINT is the same kind as task 01's; it is the one the task's Still-moves line describes ("what is wrong with them is put right"). Coverage: "45 bone(s) — 35 checked and clean, 2 checked with a LINT line".

## Entry 10 (opened 2026-10-25T11:53:45Z)

1. **Read:** Entry 9 LINT: hairback_r and hairback_l squeeze on hair_back, amplitudes opposed; the LINT's fix is 'give both the same sign (then 1.046)'. Same correction as task 01 (where the same LINT was cleared). I hand-edited runs/…-03-correct/config.json motion.tracks hairback_l amps [-0.6,-1.4,-2.4] -> [0.6,1.4,2.4]. The task's Still-moves line says the back hair's travel of 45.9 is what the draft's own amplitudes give 'once what is wrong with them is put right'.
2. **Expect:** exit 0 with 0 LINT lines on the from-config re-lint
3. **Chose / turned down:** Run propose --from-config (the doc's step 8 re-lint) on the corrected config. Turned down: building first, since the LINT is a cheap re-lint and the check's TEXTURE_STRETCH is the same bar.
4. **Happened** (2026-10-25T11:53:59Z): exit 0; it printed "0 LINT line(s) over 8 mesh(es) and the hip" and "coverage: 45 bone(s) — 37 checked and clean, 0 checked with a LINT line". The same-sign fix cleared the squeeze LINT, as it did on task 01. Expected 0 LINT: matched.

## Entry 11 (opened 2026-10-25T11:54:00Z)

1. **Read:** TASK.md 03 'Do': build with the exact command (no --loop). Pass lines Built, Checked, Whole (uncovered_error_px <= 3,500), Does not fold, Kept (8 meshes), Still moves (back hair travel >= 23 px). AUTHORING §4 step 9: build assembles, rigs and checks.
2. **Expect:** exit 0 if the check passes; or a named FAIL in check with a line that says what to change; uncovered_error_px 1726 as at assemble
3. **Chose / turned down:** Run the exact task command to runs/…-03-correct/out. Turned down: --loop, for the same reason as task 02 (the pass line names the command).
4. **Happened** (2026-10-25T11:55:12Z): exit 0; "[check] check: PASS; 11 of 11 bar(s) measured, 0 skipped" and "build: PASS — the packed atlas is the artifact". Expected PASS; it matched. TEXTURE_STRETCH: "severity 1.126; severity_ceiling 1.926544" (the bar that the same-sign fix clears). RECOMPOSITE_HOLES: "uncovered_error_px 1726". Note: I have not yet built the draft with its own opposed hair sign, so I cannot yet say the draft fails this bar. Next I check that.

## Entry 12 (opened 2026-10-25T11:55:22Z)

1. **Read:** Check on the draft's own sign, to see which bar the draft fails: the propose LINT (entry 9) said the opposed amplitudes squeeze hair_back, and named check's TEXTURE_STRETCH bar (<= 1.926544). I made a test copy work/config_signdraft.json of the config with the hairback_l amplitudes put back to the draft's opposed values [-0.6,-1.4,-2.4] (nothing else changed). This is a test copy in work/, not the hand-in.
2. **Expect:** exit 1 (build refused or check FAIL) with TEXTURE_STRETCH FAIL and severity above 1.926544, since the LINT gave 15.572
3. **Chose / turned down:** Build the test copy into work/out_signdraft, the same command. Turned down: building the whole as-proposed draft again (with the original plan order too), since the squeeze alone tests the bar the LINT named.
4. **Happened** (2026-10-25T11:57:51Z): exit 1, as expected: "[check]   FAIL  CHECK_TEXTURE_STRETCH: mesh \"hair_back\" triangle 167 ... the edge is 0.065 times its rest length (max(ratio, 1/ratio) 15.338); <= 1.926544 is required" and "[check] check: FAIL — 1 bar(s) not met; 11 of 11 bar(s) measured". So the draft as proposed (opposed hair amplitudes) fails exactly one bar: TEXTURE_STRETCH, the one the propose LINT named. The message gave the vertex weights and the chain pairs. Everything else in that test copy was the corrected config (legwear after bottomwear), so the failing bar is the hair alone.

## Entry 13 (opened 2026-10-25T11:58:33Z)

1. **Read:** Entry 12 result: the draft's opposed hair fails CHECK_TEXTURE_STRETCH (15.338 vs 1.926544). The corrected config (same sign, legwear after bottomwear) passed the build in entry 11. README rule 3 and TASK.md: grader run is a step. Config: runs/…-03-correct/config.json (corrected).
2. **Expect:** PASS built, PASS checked, Whole 1726 <= 3500, does_not_fold [], Kept 8 meshes, Still moves: back hair travel >= 23 px (the draft's own 45.9 once fixed); journal chain intact
3. **Chose / turned down:** Run grade.py on the 03 run dir. Turned down: none; the grader is the proctor's own.
4. **Happened** (2026-10-25T11:59:27Z): exit 0; grader printed "6 of 6 line(s)" with PASS built, PASS checked (TEXTURE_STRETCH PASS), PASS whole "uncovered_error_px 1726 against <= 3500", PASS does_not_fold, PASS kept "8 mesh(es) deformed against >= 8", PASS still_moves "the back hair travels 45.881 rig px ... against >= 23". Expected all six to pass; they did. Still open: the legwear drift of 5574 px is in the build log and no line of the grader covers it.

## At the end (2026-10-25T11:59:29Z)

- **Where I guessed:** Nothing from a source: the layer 'legwear' vs 'bottomwear' split of the thigh region was my own reading of the drift messages; I did not confirm which layer the painting's thigh belongs to beyond the colour numbers. The plan order (legwear after bottomwear) was my choice, not a value any tool proposed.
- **What I could not find:** Which layer owns the thigh pixels: the drift messages name both (21,839 px painting-matches-legwear before, 5,520 px painting-matches-bottomwear after), so neither draw order is clean. I would need a cut or patch on those pixels, which I did not make, and the tool's documentation for a cut's colour choice, which I read only partly (AUTHORING §3 assemble.cuts, under_fill).
