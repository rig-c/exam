# Journal

## Entry 1 (opened 2026-10-25T09:59:29Z)

1. **Read:** Task 05 timing and pass lines; fixtures/mannequin/README Joints, Signs, and Feet are planted by the rig
2. **Expect:** build exits 0; dance is 4.0 s, the two IKs keep feet planted, check measures FEET_STAY_LEVEL and reports no folds
3. **Chose / turned down:** repeat one 1-second two-beat body cycle four times: hip shifts/dips under planted IK feet, chest/head counter-rotate, shoulders swing and elbows/wrists bend within ±45; turned down disabling IK because the README says root targets plant the ankles
4. **Happened** (2026-10-25T09:59:38Z): WTF?: build stopped at assemble with CONFIG_KEY_KNOWN because my patch inserted animations_from under seethrough instead of motion; the message named the exact bad path config.seethrough.animations_from.

## Entry 2 (opened 2026-10-25T09:59:44Z)

1. **Read:** Previous CONFIG_KEY_KNOWN refusal named config.seethrough.animations_from; AUTHORING says named animations belong at motion.animations_from
2. **Expect:** build now reads dance.json, exits 0, measures FEET_STAY_LEVEL, and reports no fold
3. **Chose / turned down:** move only animations_from into motion; turned down changing dance keys before the rig can read them
4. **Happened** (2026-10-25T09:59:52Z): WTF?: the second patch matched assemble.plan instead of motion.tracks, so build refused config.assemble.animations_from; the output again named the exact misplaced path.

## Entry 3 (opened 2026-10-25T09:59:59Z)

1. **Read:** Second refusal named config.assemble.animations_from; direct inspection now shows it at config.motion.animations_from line 475
2. **Expect:** build reads dance.json and exits 0 with 10 of 14 measured, FEET_STAY_LEVEL PASS, and no folds
3. **Chose / turned down:** rebuild after verifying the exact JSON context; turned down any motion changes until the loader and checker run
4. **Happened** (2026-10-25T10:00:08Z): WTF?: build reached config loading but refused nine ASSEMBLE_LIMB_CAP_PRESENT paths because my temporary caps symlink used one too many parent components; every missing file resolved under the run caps path.

## Entry 4 (opened 2026-10-25T10:00:12Z)

1. **Read:** ASSEMBLE_LIMB_CAP_PRESENT refusals resolved every cap relative to the run config; the temporary symlink now points two parents up to fixtures/mannequin/caps
2. **Expect:** build now completes and check measures the dance with FEET_STAY_LEVEL PASS and no folds
3. **Chose / turned down:** retry unchanged motion after fixing only the local cap path; turned down editing fixture cap declarations because the submitted config must retain them
4. **Happened** (2026-10-25T10:01:48Z): build exited 0 with "check: PASS; 10 of 14 bar(s) measured, 4 skipped"; FEET_STAY_LEVEL and ANIMATIONS_DO_NOT_FOLD passed, with two non-bar seam warnings.

## Entry 5 (opened 2026-10-25T10:01:51Z)

1. **Read:** Task 05 machine lines; successful build has 4.0 s dance, active planted-foot IKs, and fold-free motion
2. **Expect:** grader passes timed, closes, hand travel, whole body, feet, timing and folds; arm bend, budget and soft lines skip by fixture contract
3. **Chose / turned down:** grade the four repeated two-beat cycles; turned down reacting to non-bar seam warnings because the task machine lines do not include seam-over-motion
4. **Happened** (2026-10-25T10:05:16Z): grader printed "11 of 11 line(s), 3 skipped"; hands traveled 152.0/236.3 px, minimum trunk travel 17.3 px, feet gap 0.87 px, closure 0.0 px, and timing repetition 1.0.

## At the end (2026-10-25T10:05:19Z)

- **Where I guessed:** The authored dance amplitudes were chosen without a worked dance reference: hip x ±20/y 8..12, chest ±6, head ±10, shoulders -35..35, elbows -30..30, wrists ±20; their machine effects were then measured by the grader.
- **What I could not find:** The fixture docs give joints, signs and planted-foot IKs but no worked whole-body dance or preview command that scores beat repetition before the grader.
