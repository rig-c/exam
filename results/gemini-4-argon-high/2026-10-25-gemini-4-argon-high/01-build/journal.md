# Journal

## Entry 1 (opened 2026-10-25T09:22:16Z)

1. **Read:** tasks/01-build/TASK.md, tasks/01-build/inputs/seethrough.json, and node_modules/@rig-c/parts/docs/AUTHORING.md §3 (assemble.rig_scale) & §4 (step 6, assemble --propose-plan)
2. **Expect:** Exit code 0, printing JSON with proposed assemble.plan, assemble.extend_below_crop, and notes on stdout, and updating runs/2026-10-25-gemini-4-argon-high-01-build/config.json with plan and extend_below_crop.
3. **Chose / turned down:** Wrote initial runs/2026-10-25-gemini-4-argon-high-01-build/config.json with key '01-build', seethrough settings from inputs/seethrough.json, and assemble.rig_scale 0.5 (for a 1664x2432 painting -> 832x1216 rig), then run rig-parts assemble --propose-plan with --write-config instead of manually guessing plan rows.
4. **Happened** (2026-10-25T09:22:48Z): Exited 0; added assemble.plan (22 rows) and assemble.extend_below_crop (2 rows) to config.json; notes reported "headwear: head run 526 rig px < 0.8 x full run 1516 -> full-run layer, drawn behind the face" and empty tags below floor 150.

## Entry 2 (opened 2026-10-25T09:23:01Z)

1. **Read:** node_modules/@rig-c/parts/docs/AUTHORING.md §4 (step 7, assemble) and §5 (After each stage: assemble)
2. **Expect:** Exit code 0, writing merged parts and parts.json to runs/2026-10-25-gemini-4-argon-high-01-build/work/rig, recomposite images to work/render, and printing part counts, recomposite vs source, and uncovered holes with uncovered error px <= 3700.
3. **Chose / turned down:** Run rig-parts assemble with --out runs/2026-10-25-gemini-4-argon-high-01-build/work using the proposed plan before running propose --parts.
4. **Happened** (2026-10-25T09:23:40Z): Exited 0; printed "recomposite vs source: mean |d|=1.09, within 8: 97.6%, error px > 40: 7465, uncovered error px: 1812" (well within <= 3700) and wrote 22 parts to work/rig/parts.

## Entry 3 (opened 2026-10-25T09:23:52Z)

1. **Read:** node_modules/@rig-c/parts/docs/AUTHORING.md §4 (step 7, propose --parts) and §5 (After each stage: propose)
2. **Expect:** Exit code 0, writing proposal.json, basis.json, and landmarks.png into work/, updating config.json with bones, meshes, regions, motion, and proposed_rig_scale, and printing 0 LINT lines.
3. **Chose / turned down:** Run rig-parts propose --parts with --write-config runs/2026-10-25-gemini-4-argon-high-01-build/config.json rather than manually authoring bones, meshes, regions, and motion.
4. **Happened** (2026-10-25T09:24:23Z): WTF?: I expected 0 LINT lines on task 01's proposal, but propose printed '1 LINT line(s) over 8 mesh(es) and the hip': hairback_r and hairback_l on mesh 'hair_back' have opposed amplitudes ([0.6, 1.4, 2.4] and [-0.6, -1.4, -2.4]) with tips 55.0 px apart, squeezing edge 27-26 of triangle 135 to 2.455 against <= 1.926544; the LINT message directly instructs to 'give both the same sign (then 1.051), or drop one chain'.

## Entry 4 (opened 2026-10-25T09:24:51Z)

1. **Read:** Step 3 LINT output ('give both the same sign (then 1.051), or drop one chain') and node_modules/@rig-c/parts/docs/AUTHORING.md §4 (step 8, propose --from-config)
2. **Expect:** Exit code 0 and '0 LINT line(s) over 8 mesh(es) and the hip' with all 39 checked bones clean.
3. **Chose / turned down:** Edited runs/2026-10-25-gemini-4-argon-high-01-build/config.json so motion.tracks hairback_l amps are [0.6, 1.4, 2.4] (same sign as hairback_r) rather than dropping one chain, then run propose --from-config to verify 0 LINT lines.
4. **Happened** (2026-10-25T09:25:34Z): Exited 0; printed "0 LINT line(s) over 8 mesh(es) and the hip" and "coverage: 47 bone(s) — 39 checked and clean, 0 checked with a LINT line, 8 not checked".

## Entry 5 (opened 2026-10-25T09:25:46Z)

1. **Read:** tasks/01-build/TASK.md and node_modules/@rig-c/parts/docs/AUTHORING.md §4 (step 9, rig-parts build)
2. **Expect:** Exit code 0, printing 'check: PASS' and 'build: PASS — the packed atlas is the artifact', with all check bars passing and 0 folding meshes.
3. **Chose / turned down:** Run rig-parts build into runs/2026-10-25-gemini-4-argon-high-01-build/out to inspect full check output before running grade.py.
4. **Happened** (2026-10-25T09:26:26Z): Exited 0; printed "[check] check: PASS; 11 of 11 bar(s) measured, 0 skipped" and "build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from" with TEXTURE_STRETCH severity 1.119 and 0 folding meshes.

## Entry 6 (opened 2026-10-25T09:26:36Z)

1. **Read:** tasks/01-build/TASK.md (Pass lines) and grade.py
2. **Expect:** Exit code 0, printing PASS for built, checked, whole, and does_not_fold, '4 of 4 line(s)', and 'journal: chain intact, 6 entries, 1 WTF'.
3. **Chose / turned down:** Run python3 grade.py runs/2026-10-25-gemini-4-argon-high-01-build to verify all 4 pass lines and write result.json.
4. **Happened** (2026-10-25T09:27:31Z): Exited 0; printed "4 of 4 line(s); journal present, 1 entry(ies) whose line 4 begins WTF?:; log .grade/2026-10-25-gemini-4-argon-high-01-build/grade.log" and "journal: chain intact, 6 entries, 1 WTF".

## At the end (2026-10-25T09:27:51Z)

- **Where I guessed:** None: assemble.rig_scale 0.5 came from AUTHORING.md §3 for a 1664x2432 painting, seethrough settings came from inputs/seethrough.json, and changing hairback_l amps to [0.6, 1.4, 2.4] came directly from propose's LINT message.
- **What I could not find:** Nothing for task 01: propose's LINT message directly diagnosed and gave the fix for the opposed back-hair chains.
