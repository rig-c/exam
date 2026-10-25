# Journal

## Entry 1 (opened 2026-10-25T11:35:17Z)

1. **Read:** AUTHORING §4 step 3: 'rig-parts layers inputs/layers/full — read it. A refusal here is about the files, not the art. A WARN line is about the art … It refuses nothing.' Config written by hand first (named here): key, seethrough from inputs/seethrough.json, assemble.rig_scale 0.5 per §3.
2. **Expect:** exit 0; a table of 29 layers (meta.json layer_count 29) with boxes and opaque px; the five accessory tags (neckwear, tail, wings, objects, eyewear) nearly empty; 0 or a few WARN lines; from the boxes I read the figure's height in run px to confirm rig_scale 0.5 gives ~1,150 rig px.
3. **Chose / turned down:** Run layers on the full run first to read the figure's extent and any WARN before planning. Turned down skipping straight to assemble --propose-plan: §4 puts layers first and I want the figure height for rig_scale.
4. **Happened** (2026-10-25T11:35:52Z): WTF?: exit 0, '29 layer(s): 29 with opaque pixels, 0 with none' and '0 WARN line(s)' as expected, and the five accessory tags hold 75-81 px — but the boxes of the body layers are the whole canvas '0,0 1024,1024 1024x1024' (the manifest's box, not an alpha box), so the figure's height cannot be read off this table; nothing told me the box is the file's and not the art's. rig_scale 0.5 stays on §3's 1664x2432 → 832x1216 sentence alone.

## Entry 2 (opened 2026-10-25T11:35:52Z)

1. **Read:** AUTHORING §4 step 6: 'rig-parts assemble --propose-plan --source … --full … --head … --config config.json --write-config config.json saves assemble.plan and assemble.extend_below_crop. Config: the layers row, with head_box.' README: --write-config for --propose-plan 'the destination must name --config itself'.
2. **Expect:** exit 0; a plan JSON on stdout of about 20 rows [name, run, tag] in draw order, with eyes/brows/lashes/irides/mouth/face taken from the head run and body tags from the full run; notes naming the five near-empty accessory layers as 'in no plan row' and nose never planned; config.json gains assemble.plan and assemble.extend_below_crop (change lines on stderr).
3. **Chose / turned down:** Write the plan into config.json with --write-config rather than copying by hand, since the flag writes exactly the two fields and the loader validates them. Turned down running layers on the head run first: --propose-plan reads both runs and names every layer it leaves out.
4. **Happened** (2026-10-25T11:36:37Z): exit 0, as expected: 'config …/config.json: added assemble.plan' and 'added assemble.extend_below_crop'; 22 plan rows, the face group from the head run, body tags from the full run; hair_back is taken from the head run with extend_below_crop continuing hair_front and hair_back from the full run; notes name the six accessory tags 'in no plan row' (66-74 px, below the floor of 150) and 'nose: in no plan row — the proposer never plans nose'. I leave nose out: the head-pitch reading is not a pass line.

## Entry 3 (opened 2026-10-25T11:36:37Z)

1. **Read:** AUTHORING §4 step 7: 'rig-parts assemble … --out work — read its uncovered hole and uncovered: lines and look at work/render/recomposite_error_rig.png (§5): red is painting no part holds, which no later stage can see'. §5 assemble row: 'uncovered holes (8-connected): N and the largest five'. TASK.md Whole line: uncovered_error_px at most 3,700; grade.py's comment says the proposed plan leaves about 1,812 on this painting.
2. **Expect:** exit 0; one line per part with op=/vis=/src= counts; a 'recomposite vs source' line with uncovered error px somewhere near 1,800 (well under 3,700); a few hundred small holes, the largest under ~100 px; scratch/01/work/rig/parts.json and parts/ written.
3. **Chose / turned down:** Assemble into scratch/01/work (outside the run directory so build output is not handed in). Turned down adding a nose row or patches before seeing the hole lines: patches answer measured holes, not guessed ones.
4. **Happened** (2026-10-25T11:37:25Z): exit 0, as expected: 'recomposite vs source: mean |d|=1.09, within 8: 97.6%, error px > 40: 7465, uncovered error px: 1812' — exactly the 1,812 grade.py's comment names, under 3,700; 'uncovered holes (8-connected): 672', the largest 94 px between hair_front and hair_back; 22 PNGs written. No patch needed.

## Entry 4 (opened 2026-10-25T11:37:25Z)

1. **Read:** AUTHORING §4 step 7, second half: 'rig-parts propose --parts work/rig --source inputs/painting.png --out work --write-config config.json → work/proposal.json and work/render/landmarks.png. The flag saves each of bones, meshes, regions, limbs, motion, constraints, turn and proposed_rig_scale it wrote into the config'; limbs only with --keypoints, so none here. §5 propose row: 'no LINT line' is green; read the coverage lines and basis.json's ratio/fallback bones.
2. **Expect:** exit 0; note: lines (mesh spacing with H around 1,100-1,200 rig px, blink, fringe template, 'not read: no part tagged nose'); 0 or a few LINT lines; coverage lines per bone; config.json gains bones, meshes, regions, motion, proposed_rig_scale 0.5; proposal.json and basis.json under scratch/01/work.
3. **Chose / turned down:** Let --write-config paste the proposal, then lint it with --from-config in the next step and correct only what LINT or the overlay names. Turned down --keypoints: the figure stands front-on with arms away from the body, which is the pose the proposer's screen-y ratios assume (README 'What it does not do').
4. **Happened** (2026-10-25T11:38:01Z): exit 0 and the config gained bones, meshes, regions, motion, proposed_rig_scale as expected ('wrote proposal.json (23 bone entries, 8 meshes)'; 'mesh spacing: grid 29 = round(H / 37), H 1087 rig px' — H just under the 1106-1185 calibration band, so rig_scale 0.5 holds). One LINT line, which I half expected: 'LINT hairback_r and hairback_l on mesh hair_back squeeze it: … closes to 0.407 … (max(ratio, 1/ratio) 2.455; <= 1.926544 is required …) give both the same sign (then 1.051), or drop one chain'. Coverage: 37 clean, 2 LINT, 8 not checked (regions, controls, segment-bound). Correction (by hand, named here): hairback_l amps [-0.6,-1.4,-2.4] -> [0.6,1.4,2.4], note kept beside it.

## Entry 5 (opened 2026-10-25T11:38:01Z)

1. **Read:** AUTHORING §4 step 8: 'Correct, then rig-parts propose … --from-config config.json to redraw the config's own bones and LINT them … repeat until it prints no LINT line (exit 0).' The LINT line from step 4: 'give both the same sign (then 1.051)'.
2. **Expect:** exit 0 and '0 LINT line(s)' now that hairback_l's amplitudes share hairback_r's sign; the squeeze figure drops to about 1.051 as the LINT predicted; coverage 39 clean, 0 LINT, 8 not checked.
3. **Chose / turned down:** Take the LINT's first remedy (same sign) rather than dropping a chain: both chains keep the hair swinging, and the figure it quotes (1.051) is well inside the bar. Turned down editing the chain points: off-art read clean on every link.
4. **Happened** (2026-10-25T11:38:30Z): exit 0, as expected: '0 LINT line(s) over 8 mesh(es) and the hip' and 'coverage: 47 bone(s) — 39 checked and clean, 0 checked with a LINT line, 8 not checked'. The squeeze figure itself is not reprinted on a clean lint, so 1.051 is the LINT's prediction, not a reading.

## Entry 6 (opened 2026-10-25T11:38:30Z)

1. **Read:** TASK.md 'Do': 'rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out exits 0'; AUTHORING §4 step 9 and §5 check row: the gate lines, 'loop:', 'seam:', the judgement lines, ANIMATIONS_DO_NOT_FOLD; README: the last lines of a green build are 'build: PASS — the packed atlas is the artifact' and the three artifact paths. §8: 12.7-27.5 s on the reference examples.
2. **Expect:** exit 0 within a minute or two; the rig stage prints 8 mesh lines with cover 1.00000 and both gate summaries '0 failed'; check: PASS with TEXTURE_STRETCH under 1.926544 on hair_back (the corrected squeeze), ANIMATIONS_DO_NOT_FOLD naming no mesh, RECOMPOSITE_HOLES uncovered_error_px 1812; last line 'build: PASS'.
3. **Chose / turned down:** Build without --loop (no pass line reads the GIF) into scratch/01/out, with the config as corrected. Turned down adding a nose row or physics: neither is asked by task 01's four lines.
4. **Happened** (2026-10-25T11:39:47Z): exit 0, as expected: 8 meshes at 'cover 1.00000', both gates '0 failed', 'TEXTURE_STRETCH: PASS — meshes 8; triangles 616; frames 41; severity 1.119' with hair_back at severity 1.048 (the LINT predicted 1.051), 'ANIMATIONS_DO_NOT_FOLD: PASS — … 0 folding mesh(es)', 'RECOMPOSITE_HOLES: REPORTED — error_px 7465; uncovered_error_px 1812', 'check: PASS; 11 of 11 bar(s) measured, 0 skipped' and 'build: PASS'. 65 s wall clock.

## Entry 7 (opened 2026-10-25T11:39:47Z)

1. **Read:** PROMPT: 'You may run python3 grade.py runs/<your run> whenever you like. It is the same grader the proctor runs.' grade.py main: copies the run's .json files beside tasks/01-build/inputs, runs the TASK.md build command, reads check.json (PASS, uncovered_error_px <= 3700) and rigc render --folds over the idle; prints one line per pass line, the journal verify line, the guide note and the clock.
2. **Expect:** exit 0; PASS built (exit 0), PASS checked (every bar PASS/REPORTED/SKIP), PASS whole (1812 against <= 3700), PASS does_not_fold ([]); 'journal: chain intact, 7 entries, 1 WTF'; '4 of 4 line(s)'. Takes about a minute (it rebuilds).
3. **Chose / turned down:** Grade now from the handed-in config alone, which is the proctor's path. Turned down --loop or a sheet first: no line reads them and the contact sheet is the person's reading.
4. **Happened** (2026-10-25T11:41:14Z): exit 0, as expected: 'PASS  built', 'PASS  checked' with every bar PASS and RECOMPOSITE_HOLES REPORTED, 'PASS  whole: "uncovered_error_px 1812 against <= 3700"', 'PASS  does_not_fold: []', 'journal: chain intact, 7 entries, 1 WTF', '4 of 4 line(s)'. The clock line says no finished: yet, which finish writes next.

## At the end (2026-10-25T11:41:19Z)

- **Where I guessed:** assemble.rig_scale 0.5: taken from AUTHORING §3's sentence that 0.5 on a 1664x2432 painting makes an 832x1216 rig and keeps the figure about 1,100-1,200 rig px tall; the layers table could not confirm the figure's height (its boxes are the manifest's whole canvas), and only propose's 'mesh spacing' note (H 1087) confirmed it afterwards. Every other value was proposed by the tool; the one hand edit (hairback_l amplitudes' sign) is the LINT line's own remedy.
- **What I could not find:** Whether the layers table's box column is the manifest's box or an alpha box (it is the manifest's, so a full-canvas layer reads 0,0 1024,1024 and says nothing about the art's extent). Whether leaving the nose row out costs anything a pass line reads (the head-pitch note is the only reader I found).
