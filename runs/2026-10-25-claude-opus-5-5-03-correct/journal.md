# Journal

## Entry 1 (opened 2026-10-25T11:38:29Z)

1. **Read:** AUTHORING §4 step 6 (assemble --propose-plan --write-config), as on task 01; the painting viewed: seated figure from about y 180 to 2420 of 2432 source px, so rig_scale 0.5 puts it ~1,120 rig px tall (AUTHORING §3 assemble.rig_scale: 1,100-1,200)
2. **Expect:** exit 0; plan of ~22 rows written into config.json; probably a note on the back hair (her low side ponytail leaves the head crop) proposing extend_below_crop from the full run
3. **Chose / turned down:** config.json with key, seethrough copied from inputs/seethrough.json, rig_scale 0.5; turned down a smaller scale since the seated figure is still near full painting height
4. **Happened** (2026-10-25T11:38:53Z): partly as expected: exit 0, 'added assemble.plan' (22 rows) and extend_below_crop for hair_front and hair_back from the full run; no note on the back hair leaving the crop; headwear from the full run ('head run 5 rig px < 0.8 x full run 2146')

## Entry 2 (opened 2026-10-25T11:38:53Z)

1. **Read:** AUTHORING §4 step 7: assemble --out work, read 'uncovered hole' lines; TASK 03 Whole: uncovered_error_px <= 3,500
2. **Expect:** exit 0, 22 parts on 832x1216; uncovered error px around 2,000 (like task 01's 1812); the crossed ankles and the hand in the lap may leave holes
3. **Chose / turned down:** assemble alone before proposing, as on task 01
4. **Happened** (2026-10-25T11:39:40Z): WTF?: uncovered was as expected ('uncovered error px: 1726'), but I did not expect the drift line: '"bottomwear" refuses 21999 px of full:bottomwear … the painting is within 90 of "legwear" (21839 px at alpha >= 250, drawn behind "bottomwear")' — See-through's skirt layer covers her seated thighs, which the painting shows in front of the skirt; the line says what it refused but not whether the plan's order should change

## Entry 3 (opened 2026-10-25T11:39:47Z)

1. **Read:** AUTHORING §4 step 7 (propose --parts … --write-config); README 'What it does not do': 'seated in a skirt that does not start at the hip — needs propose --keypoints; sitting alone does not'; error map viewed: thin red fringes only, a red patch at the crossed ankles
2. **Expect:** exit 0; bones/meshes/regions/motion written; some LINT lines — the TASK says the draft does not pass check as proposed, and the 'Still moves' line points at the back hair's amplitudes, so I expect a LINT on hairback_r/hairback_l like task 01's opposed-amplitude squeeze
3. **Chose / turned down:** propose without --keypoints first: pose_seated.json is a body-18 control pose for comfy paint (generation.control.skeleton), not the keypoints file shape propose reads, and the skirt here starts at the waist; turned down converting it before seeing what the draft gets wrong
4. **Happened** (2026-10-25T11:40:04Z): as expected: exit 0, one LINT on the back hair, the same shape as task 01's but far worse: 'edge 37-117 of triangle 167 closes to 0.064 times its rest length' ('max(ratio, 1/ratio) 15.572; <= 1.926544 is required'), 'their amplitudes are opposed (hairback_r [0.6, 1.4, 2.4], hairback_l [-0.6, -1.4, -2.4])', tips 39.0 px apart; fix offered 'give both the same sign (then 1.046)'

## Entry 4 (opened 2026-10-25T11:40:05Z)

1. **Read:** TASK 03: 'what the tool proposes does not pass its own check as proposed'; propose LINT just read (squeeze 15.572 vs TEXTURE_STRETCH 1.926544)
2. **Expect:** exit 1 or a red check: TEXTURE_STRETCH FAIL on slot hair_back with a severity near 15 at idle frame ~22, everything else PASS — confirming the LINT is the check's fault before I change anything
3. **Chose / turned down:** build the uncorrected draft once (copy kept at work/config.draft.json, outside the hand-in files) so the journal shows the check's own refusal; turned down fixing blind from the LINT alone, since the TASK asks which message I decided from
4. **Happened** (2026-10-25T11:41:20Z): as expected: 'check: FAIL — 1 bar(s) not met', 'FAIL  CHECK_TEXTURE_STRETCH: mesh "hair_back" triangle 167 (vertices 115 37 117), edge 37-117, idle frame 22 — the edge is 0.065 times its rest length (max(ratio, 1/ratio) 15.338)'; vertex 37 rides hairback_r2, vertex 117 hairback_l2 — the two back-hair chains swing against each other; every other bar PASS

## Entry 5 (opened 2026-10-25T11:41:28Z)

1. **Read:** the draft build's 'FAIL  CHECK_TEXTURE_STRETCH: mesh "hair_back" … 15.338' and propose's LINT 'give both the same sign (then 1.046), or drop one chain'
2. **Expect:** exit 0, '0 LINT line(s) over 8 mesh(es) and the hip'
3. **Chose / turned down:** flipped hairback_l amps to [0.6, 1.4, 2.4] with an amps_note beside them; kept both chains and their sizes (TASK: not rigid, not turned down — Still moves wants >= 23 px). Turned down dropping a chain or shrinking amplitudes
4. **Happened** (2026-10-25T11:41:38Z): as expected: '0 LINT line(s) over 8 mesh(es) and the hip', 37 checked and clean; the amps_note was accepted by the loader

## Entry 6 (opened 2026-10-25T11:41:44Z)

1. **Read:** landmarks_config.png viewed: chains on the art, hairback_r/l hanging side by side down the front of the chest 39 px apart; TASK 03 Do: the build command; LINT clean
2. **Expect:** exit 0, 'check: PASS; 11 of 11', TEXTURE_STRETCH on hair_back near 1.05 (LINT predicted 1.046), uncovered_error_px 1726 <= 3,500, 8 meshes
3. **Chose / turned down:** the TASK's build on the corrected config; turned down also re-placing the leg or sleeve bones by keypoints: nothing fails there
4. **Happened** (2026-10-25T11:42:51Z): as expected: 'check: PASS; 11 of 11 bar(s) measured, 0 skipped', hair_back now 'max_ratio 1.045', uncovered_error_px 1726, 'build: PASS'

## Entry 7 (opened 2026-10-25T11:42:51Z)

1. **Read:** PROMPT: grade.py; TASK 03 lines incl. Kept (8 meshes) and Still moves (back hair >= 23 rig px against the head; the TASK says 45.9 once corrected)
2. **Expect:** 6 of 6 PASS; still_moves about 45.9 rig px since I kept the draft's amplitudes and only flipped the sign
3. **Chose / turned down:** grade now
4. **Happened** (2026-10-25T11:43:54Z): as expected: '6 of 6 line(s)', 'the back hair travels 45.881 rig px against the head over the idle, against >= 23', '8 mesh(es) deformed against >= 8'

## At the end (2026-10-25T11:43:54Z)

- **Where I guessed:** rig_scale 0.5 from the painting viewed by eye (figure ~2,240 of 2,432 source px); propose's H 1107 confirmed it. The fix itself was the LINT's own suggestion (same sign), not a value I chose.
- **What I could not find:** Whether the bottomwear drift (21,999 px of skirt layer over the seated thighs, refused and shown from the painting) needs a plan change for motion; nothing failed on it and no line said it should change. Also: pose_seated.json is in the comfy control-pose shape, and no document said whether to convert it to propose --keypoints for this task.
