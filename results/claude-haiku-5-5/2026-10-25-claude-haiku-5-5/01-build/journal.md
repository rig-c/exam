# Journal

## Entry 1 (opened 2026-10-25T11:29:26Z)

1. **Read:** PROMPT boundaries + README rule 3; packages' AUTHORING.md §4 step 1 (inputs: 'writes st_input_full.png, the painting centred on a white square of its longer side'). Wrote runs/…-01-build/config.json by hand (key, generation copied from tasks/01-build/inputs/generation.json, seethrough from seethrough.json, assemble.rig_scale 0.5 per AUTHORING §3 rig_scale: keep figure 1100-1200 rig px).
2. **Expect:** exit 0; writes st_input_full.png as a square 2432x2432 (painting 1664x2432 white-padded left and right)
3. **Chose / turned down:** rig-parts inputs with the clone's node_modules bin, config in the run dir, out in runs/…-01-build/work. Turned down: passing a hand-padded square, since the doc says that padding becomes part of the rig.
4. **Happened** (2026-10-25T11:29:37Z): WTF?: exit 1, not 0. My hand-copied generation block was refused: "FAIL  CONFIG_KEY_KNOWN: config.generation.size — is not a field here" and nine problems in all. I had copied generation.json's keys (size, upscale) which the loader does not know; the docs say generation is only for the comfy adapter and is left out for another painting route. Nothing said so at the point I wrote it; I guessed from generation.json.

## Entry 2 (opened 2026-10-25T11:29:42Z)

1. **Read:** Previous refusal (entry 1): AUTHORING.md §3 — generation is recorded, checked only when present, and left out for a painting not made by the comfy adapter. Rewrote runs/…-01-build/config.json by hand without the generation block (key, seethrough, assemble.rig_scale 0.5).
2. **Expect:** exit 0; st_input_full.png written as a 2432x2432 square under runs/…-01-build/work/inputs
3. **Chose / turned down:** Same inputs step, rerun. Turned down: keeping generation with the keys I guessed, since the loader refuses unknown keys.
4. **Happened** (2026-10-25T11:30:02Z): exit 0; it printed "st_input_full.png 2432x2432: the painting at x 384, white either side (384 + 384 px)" and "no seethrough.head_box in the config, so no st_input_head.png". The expectation matched; the See-through run itself is the layers the task gave, so no external run is needed.

## Entry 3 (opened 2026-10-25T11:30:08Z)

1. **Read:** AUTHORING.md §4 step 3 ('rig-parts layers inputs/layers/full — read it'). The layers are the task's own See-through output (tasks/01-build/inputs/layers/full, the task says no need to regenerate).
2. **Expect:** exit 0; one line per layer (box, opaque px, depth, plausibility); WARN lines for any layer that is not plausibly the figure; refuses nothing
3. **Chose / turned down:** Run layers on the full run. Turned down: reading layers.json by hand first, since the tool prints the same figures and names the WARNs.
4. **Happened** (2026-10-25T11:30:14Z): exit 0; it printed "29 layer(s): 29 with opaque pixels, 0 with none" and "0 WARN line(s)". No WARN, so nothing is left out at step 6 for plausibility; the layers match the figure's expected count.

## Entry 4 (opened 2026-10-25T11:30:18Z)

1. **Read:** AUTHORING.md §4 step 4: 'rig-parts propose --head-box --full inputs/layers/full --canvas <W>x<H> --write-config config.json', <W>x<H> is the original painting's size (1664x2432), not the padded square's. Config: writes seethrough.head_box into the existing config.
2. **Expect:** exit 0; seethrough.head_box written into config.json (square, source pixels); head box near the head: roughly x 584..1111 and y 69..596 as in seethrough.json's head_box (the task's own value, which I will compare)
3. **Chose / turned down:** Run propose --head-box with --write-config on the run-dir config. Turned down: typing head_box by hand from seethrough.json, since the doc says it is proposed by this command.
4. **Happened** (2026-10-25T11:30:25Z): exit 0; it printed "config .../config.json: added seethrough.head_box" and "head_box [584, 69, 1111, 596], 527x527". The value is the same as the task's seethrough.json head_box [584, 69, 1111, 596], so the head layers the task gave match this crop.

## Entry 5 (opened 2026-10-25T11:30:31Z)

1. **Read:** AUTHORING.md §4 step 5: after propose --head-box, run inputs again, it writes st_input_head.png (the painting cropped to head_box). The head run is the task's layers/head, so no external run is needed. Config: runs/…-01-build/config.json now holds seethrough.head_box (its written value, read back on disk).
2. **Expect:** exit 0; writes st_input_head.png at the exact crop size 527x527
3. **Chose / turned down:** Rerun inputs with the same --out as entry 2. Turned down: skipping it, since assemble reads the head crop as the head run's canvas.
4. **Happened** (2026-10-25T11:30:41Z): exit 0; it printed "st_input_head.png 527x527: seethrough.head_box [584, 69, 1111, 596]". Matched the expected 527x527 crop.

## Entry 6 (opened 2026-10-25T11:30:46Z)

1. **Read:** AUTHORING.md §4 step 6: 'rig-parts assemble --propose-plan --source … --full … --head … --config config.json --write-config config.json' saves assemble.plan and assemble.extend_below_crop; read its notes for each unplanned layer. The head run is the task's tasks/01-build/inputs/layers/head.
2. **Expect:** exit 0; a plan of about 23 to 26 parts in draw order; notes name any layer left out (neckwear, tail, wings, objects, eyewear are small and may be named empty); writes assemble.plan and extend_below_crop into config.json
3. **Chose / turned down:** Run the proposer with --write-config on the run-dir config. Turned down: writing assemble.plan by hand, since the doc says each row is a proposal from this command and the plan's names drive every later section.
4. **Happened** (2026-10-25T11:31:09Z): WTF?: exit 0, but the plan has 22 rows, not the 23 to 26 I wrote in line 2; I had taken the README's 23-part demo as the count and should not have. The rest matched: notes name neckwear, tail, wings, objects, eyewear and earwear as empty, and nose as never planned ("headwear: head run 526 rig px < 0.8 x full run 1516 -> full-run layer, drawn behind the face"). extend_below_crop lists hair_front and hair_back.

## Entry 7 (opened 2026-10-25T11:31:11Z)

1. **Read:** AUTHORING.md §4 step 7: 'rig-parts assemble … --out work' then read its 'uncovered hole' and 'uncovered:' lines and look at work/render/recomposite_error_rig.png. Config: the assemble row (key, seethrough, rig_scale, plan) — now holds assemble.plan from entry 6 (22 rows).
2. **Expect:** exit 0; writes work/rig (parts.json and parts/); recomposite error printed; a few uncovered hole lines of small size; uncovered_error_px well under 3,700 rig px
3. **Chose / turned down:** Run assemble with --out runs/…-01-build/work. Turned down: adding an assemble.patches entry now, since the doc says to add one only for a large red hole, and I will look at the number first.
4. **Happened** (2026-10-25T11:31:46Z): exit 0; it printed "22 part(s) on a 832x1216 rig" and "recomposite vs source: mean |d|=1.09, within 8: 97.6%, error px > 40: 7465, uncovered error px: 1812". Expected uncovered well under 3,700: 1812 matches. The largest hole is 94 px at 458,203 between hair_front and hair_back, which is small; no assemble.patches entry needed.

## Entry 8 (opened 2026-10-25T11:31:48Z)

1. **Read:** AUTHORING.md §4 step 7 (propose --parts work/rig, --write-config): drafts bones, meshes, regions, limbs (only with --keypoints), motion, proposed_rig_scale into config and writes proposal.json, basis.json and render/landmarks.png. Config: assemble row plus the assemble.plan from entry 6.
2. **Expect:** exit 0; proposal.json and landmarks.png written under work/; LINT lines (exit 1 while any remain at step 8); one coverage line per bone
3. **Chose / turned down:** Run propose with --write-config into the run-dir config, no --keypoints (no keypoints file in the task inputs). Turned down: adding --keypoints from a pose file I did not find in the task inputs.
4. **Happened** (2026-10-25T11:32:00Z): exit 0; it wrote proposal.json, basis.json and landmarks.png and added bones, meshes, regions, motion, proposed_rig_scale to config.json. It printed "1 LINT line(s) over 8 mesh(es) and the hip": "LINT hairback_r and hairback_l on mesh 'hair_back' squeeze it", and the fix it names is "give both the same sign (then 1.051), or drop one chain". Coverage: "47 bone(s) — 37 checked and clean, 2 checked with a LINT line, 8 not checked". The expected LINT lines appeared, so step 8 (correction) is next.

## Entry 9 (opened 2026-10-25T11:32:24Z)

1. **Read:** propose's LINT line from entry 8: 'LINT hairback_r and hairback_l on mesh hair_back squeeze it ... give both the same sign (then 1.051), or drop one chain'. I hand-edited runs/…-01-build/config.json: motion.tracks hairback_l amps [-0.6,-1.4,-2.4] -> [0.6,1.4,2.4] (same sign as hairback_r). AUTHORING §4 step 8: propose --from-config config.json re-lints the config's bones; exit 1 while any LINT remains.
2. **Expect:** exit 0 with no LINT lines, or the same squeeze LINT on hair_back if the sign change does not clear it; coverage summary shows the two hairback_r2/hairback_l2 coverage lines clean
3. **Chose / turned down:** Run propose --from-config with --out work. Turned down: dropping hairback_l to avoid the squeeze, since the tool offered same-sign as the first fix and dropping one leaves the hair on one side only.
4. **Happened** (2026-10-25T11:32:32Z): exit 0; it printed "0 LINT line(s) over 8 mesh(es) and the hip" and "coverage: 47 bone(s) — 39 checked and clean, 0 checked with a LINT line, 8 not checked". The expectation matched: the hairback squeeze LINT is gone with the sign change; the 8 not-checked bones are the region-bound and segment-bound ones and the control neck.

## Entry 10 (opened 2026-10-25T11:32:34Z)

1. **Read:** AUTHORING.md §4 step 9 and TASK.md pass lines: 'rig-parts build --config config.json --source … --full … --head … --out out --loop' does assemble, rig and check in one process. Config: now the full row (key, seethrough, assemble, bones, meshes, regions, motion, proposed_rig_scale) after the corrected hairback_l sign.
2. **Expect:** exit 0 with a check: line; check PASS; uncovered_error_px 1812 (as at assemble); possible FAIL lines for something the proposal did not fold, which I would read and fix
3. **Chose / turned down:** Run build with --loop and --out runs/…-01-build/out, as the task command. Turned down: running build without --loop, since the README names --loop for the loop-level check and the task's own command has no flag I must drop.
4. **Happened** (2026-10-25T11:33:45Z): exit 0 with a --loop build: "[check] check: PASS; 11 of 11 bar(s) measured, 0 skipped" and "build: PASS — the packed atlas is the artifact". Expected a PASS and a check line; it matched. Two things differ from my line 3: I added --loop, which the task command does not have; I will run the exact task command next to confirm. Also "ANIMATIONS_DO_NOT_FOLD: PASS — 1 animation(s) read by rigc render --folds at 12 fps (idle): 0 folding mesh(es)" and "RECOMPOSITE_HOLES: REPORTED — error_px 7465; uncovered_error_px 1812".

## Entry 11 (opened 2026-10-25T11:33:46Z)

1. **Read:** TASK.md 01 'Do': the command exactly, 'rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out' exits 0. Its Built pass line requires that exact command. Config: runs/…-01-build/config.json unchanged since entry 9 (the hairback_l sign fix).
2. **Expect:** exit 0, without --loop; check PASS; the same 1812 uncovered_error_px
3. **Chose / turned down:** Run the exact task command, same --out (overwrites out/). Turned down: adding --loop again, since the pass line names the command without it.
4. **Happened** (2026-10-25T11:34:58Z): exit 0 for the exact task command, no --loop: "[check] check: PASS; 11 of 11 bar(s) measured, 0 skipped" and "build: PASS — the packed atlas is the artifact". Expected exit 0 and the same 1812 uncovered_error_px; it matched ("uncovered_error_px 1812").

## Entry 12 (opened 2026-10-25T11:34:59Z)

1. **Read:** README rule 6 and TASK.md pass lines: grade.py rebuilds from my config.json and inputs. Running it is a grader step.
2. **Expect:** result.json written; printed lines Built/Checked/Whole/Does not fold pass or fail; journal chain intact
3. **Chose / turned down:** Run grade.py on the run dir. Turned down: none; the grader is the proctor's own.
4. **Happened** (2026-10-25T11:36:01Z): exit 0; grader printed "4 of 4 line(s); journal present, 2 entry(ies) whose line 4 begins WTF?:" and "PASS  whole: \"uncovered_error_px 1812 against <= 3700\"". Expected all four lines to pass; they did, and the journal chain is intact ("journal: chain intact, 12 entries, 2 WTF").

## At the end (2026-10-25T11:59:37Z)

- **Where I guessed:** assemble.rig_scale 0.5 (AUTHORING §3 gives the figure-height rule, and the examples use 0.5); the figure's measured height in the rig was not checked against 1,100-1,200 before I chose it. Nothing else guessed: the head box, plan, bones, meshes, regions and motion were all written by the tools.
- **What I could not find:** How the propose step decides the head bone's rest frame vs the eyes' axis in the face's roll (the head frame note says 'roll 4.844 degrees'); I did not read why a head roll is chosen. And whether the hair squeeze LINT's same-sign fix is the designed correction or only the cheapest one: I took the tool's first suggestion.
