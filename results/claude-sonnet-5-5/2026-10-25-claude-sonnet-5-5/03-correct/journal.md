# Journal

## Entry 1 (opened 2026-10-25T11:41:56Z)

1. **Read:** TASK.md 03; same loop as task 01 (README 'The loop'; AUTHORING §4 step 6)
2. **Expect:** assemble --propose-plan writes assemble.plan; possibly a note about long hair or a seated-figure layer
3. **Chose / turned down:** same sequence as task 01 with head_box from inputs/seethrough.json; not using pose_seated.json (it is the generation control pose, not a keypoints file for propose)
4. **Happened** (2026-10-25T11:42:22Z): exit 0; "config ...: added assemble.plan" and added assemble.extend_below_crop; 22 rows; same kinds of notes as task 01.

## Entry 2 (opened 2026-10-25T11:42:22Z)

1. **Read:** AUTHORING §4 step 7
2. **Expect:** assemble prints 22 parts and uncovered holes; uncovered error px under 3,500 hopefully
3. **Chose / turned down:** assemble to work/, no patches yet
4. **Happened** (2026-10-25T11:43:01Z): exit 0; "uncovered error px: 1726" is under 3,500; largest hole 154 px at 321,1077.

## Entry 3 (opened 2026-10-25T11:43:02Z)

1. **Read:** AUTHORING §4 step 7 propose --parts --write-config
2. **Expect:** writes bones/meshes/regions/motion/turn; LINT lines possibly (seated figure: hip/chest? hairback squeeze again)
3. **Chose / turned down:** same propose --parts as task 01 with --full/--head, no --keypoints
4. **Happened** (2026-10-25T11:43:16Z): exit 0 but: "LINT hairback_r and hairback_l on mesh 'hair_back' squeeze it ... closes to 0.064 times its rest length ... their amplitudes are opposed ... give both the same sign (then 1.046), or drop one chain". Expected a LINT; the message names the fix.

## Entry 4 (opened 2026-10-25T11:43:16Z)

1. **Read:** propose LINT line: 'give both the same sign (then 1.046), or drop one chain'
2. **Expect:** after setting hairback_l amps to the positive values (hand edit), propose --from-config prints 0 LINT lines
3. **Chose / turned down:** flip the sign, keep both chains and the amplitudes (the task's 'Still moves' line wants back hair to travel >= 23 px, so dropping a chain is out)
4. **Happened** (2026-10-25T11:43:28Z): 0 LINT line(s) over 8 mesh(es) and the hip; exit 0.

## Entry 5 (opened 2026-10-25T11:43:28Z)

1. **Read:** TASK.md 03 build command
2. **Expect:** build exits 0 and check PASS; but task says the proposal fails its check, so I expect hair was only the LINT and a check bar (maybe TIP_OVER_ROOT or SEAM) may still fail
3. **Chose / turned down:** build with the corrected config; read check lines before deciding more
4. **Happened** (2026-10-25T11:44:20Z): exit=0; "check: PASS; 11 of 12 bar(s) measured, 1 skipped (FEET_STAY_LEVEL)"; "build: PASS". The one correction was the hairback_l sign; no other bar failed.

## Entry 6 (opened 2026-10-25T11:44:20Z)

1. **Read:** TASK.md 03 pass lines
2. **Expect:** grader 6 of 6: built, checked, whole 1726<=3500, does_not_fold, kept (8 meshes), still moves >= 23 (draft's corrected value is 45.9)
3. **Chose / turned down:** grade now
4. **Happened** (2026-10-25T11:45:19Z): exit 0; "6 of 6 line(s)"; still_moves "the back hair travels 45.881 rig px against the head over the idle, against >= 23".

## At the end (2026-10-25T11:45:19Z)

- **Where I guessed:** none: the only edit (hairback_l amps sign) was the value the LINT line named
- **What I could not find:** I decided from the propose LINT line (hairback_r/hairback_l opposed amplitudes, 'give both the same sign') and did not look at any picture; no document said that was the fault before the build.
