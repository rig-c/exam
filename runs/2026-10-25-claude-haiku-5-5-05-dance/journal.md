# Journal

## Entry 1 (opened 2026-10-25T12:06:22Z)

1. **Read:** TASK.md 05 (dance on the mannequin fixture, 4.0 s loop, 8 beats at 120 bpm; pass lines; feet planted by the two iks, fixture README 'Feet are planted by the rig'). fixtures/mannequin/README.md 'The joints' table (bones, ranges, signs: positive sleeve_l0 raises the left, positive sleeve_r0 lowers the right). Config: copied fixtures/mannequin/config.json unchanged into runs/…-05-dance/config.json; caps/ copied beside it (the config names caps/*.png, so the build reads them from the run dir).
2. **Expect:** exit 0; check: PASS; 9 of 14 bar(s) measured, 5 skipped (the fixture README's own check line)
3. **Chose / turned down:** Build the fixture as given first, to match its check line before any change. Turned down: adding dance first, since the task says the rig builds as given and I want a baseline.
4. **Happened** (2026-10-25T12:07:38Z): exit 0; "[check] check: PASS; 9 of 14 bar(s) measured, 5 skipped (BLINK_NO_HOLE, TIP_OVER_ROOT, TEXTURE_STRETCH, FEET_STAY_LEVEL, STRESS_OFF_CHAIN)" and "build: PASS — the packed atlas is the artifact". Matched the fixture README's check line exactly.

## Entry 2 (opened 2026-10-25T12:07:51Z)

1. **Read:** TASK.md 05: 'Give the rig one more animation, named dance': 4.0 s loop; 8 beats at 120 bpm = 2 beats per 1.0 s. AUTHORING 'expressions and other named animations': motion.animations_from file, rigc-motion/1 spec, key times strictly increasing, last key at duration. Wrote runs/…-05-dance/animations.json by a generator (python, one cycle of 1.0 s repeated 4 times: hip translatey dips on the off-beats, hip translatex sways 18 px, chest lean 3 deg, sleeve_r0 -40 (raises the right arm: negative raises it), sleeve_l0 +40 (raises the left), head 6 deg, neck -3 deg). Config: runs/…-05-dance/config.json motion.animations_from 'animations.json' added by hand. Feet: no change; the two iks hold them.
2. **Expect:** exit 0; check PASS; dance listed beside the idle; the same 9 of 14 bars plus FEET_STAY_LEVEL measured (10 of 14)
3. **Chose / turned down:** Build with out to work/dance, the exact fixture command. Turned down: no --loop, same as the other tasks.
4. **Happened** (2026-10-25T12:09:23Z): exit 0; "[check] check: PASS; 10 of 14 bar(s) measured, 4 skipped (BLINK_NO_HOLE, TIP_OVER_ROOT, TEXTURE_STRETCH, STRESS_OFF_CHAIN); 2 warning(s) (SEAM_OVER_MOTION, not a bar)". Expected 10 of 14 with FEET_STAY_LEVEL measured: it is PASS ("2 animation(s) read by rigc render --folds --geometry at 12 fps (idle, dance)"). "beside the idle: 1 animation(s), dance" is listed. Two SEAM_OVER_MOTION warnings in the dance were not in my expectation; they are never a bar, so I note them and go on to the grader.

## Entry 3 (opened 2026-10-25T12:09:25Z)

1. **Read:** TASK.md 05 pass lines (dance as timed 4.0 s; closes; both hands 100 px; arms bend (SKIP); whole body topwear 15 px from feet middle; on its feet 6 px; keeps time: half of the speed variation repeats every two beats; dance does not fold). The proctor grades from my config and animations.json. Expected: closes and keeps time pass by construction (4.0 s, 1.0 s period); hands and whole-body depend on the 40 deg and 18 px amplitudes.
2. **Expect:** the grader prints PASS for dance as timed, closes, both hands, whole body, on its feet, keeps time, dance does not fold; arms bend SKIP with its reason
3. **Chose / turned down:** Run grade.py on the 05 run dir. Turned down: none; the grader is the proctor's own.
4. **Happened** (2026-10-25T12:11:41Z): exit 0; grader printed "11 of 11 line(s), 3 skipped (budget, arms_bend_at_the_joints, soft_in_the_dance)" with PASS dance_as_timed "4 s against 4.0", PASS closes "0.0 rig px from the first", PASS both_hands "hand_l travels 265.3 rig px and hand_r 268.2", PASS whole_body "37.9 rig px", PASS on_her_feet "3.32 rig px", PASS keeps_time "1.0 of the variation ... repeats every two beats", PASS dance_does_not_fold. Expected all of them: the closes and keeps-time lines hold by construction; the hand and whole-body figures were above my 40-degree and 18-px estimates. The journal chain is intact ("journal: chain intact, 3 entries, 0 WTF").

## At the end (2026-10-25T12:11:43Z)

- **Where I guessed:** The dance's joint keys (hip translatey -10 and translatex ±18; chest 3 deg; sleeve_r0 -40 and sleeve_l0 +40; head 6 deg; neck -3 deg) and the 1.0 s cycle are my choices, from the 120 bpm beat, not from the fixture or the packages; none is a measured best. The 18 px and 40 deg were not computed from the bar before the first build.
- **What I could not find:** Whether the dance reads as a dance on the beat (only the proctor's person score judges it); and whether the SEAM_OVER_MOTION warnings in the dance (2, never a bar) are a real crease at the shoulder or hip. I did not open the seam picture.
