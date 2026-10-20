# Journal — claude-sonnet-5-5, 03-correct, 2026-10-20

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry 1

1. **Read:** Task 01 experience plus AUTHORING §4 steps 6 (assemble --propose-plan) with the layers row config (key, seethrough from inputs/seethrough.json, assemble.rig_scale 0.5).
2. **Expect:** A config with plan and extend_below_crop; notes about empty layers like task 01.
3. **Chose / turned down:** Same minimal-config then propose-plan path as task 01. Turned down: guessing the plan by hand.
4. **Happened:** plan with 22 parts and extend_below_crop merged; note: headwear head run 5 px vs full 2146, so the ribbon comes from the full run. As expected.

## Entry 2

1. **Read:** AUTHORING §4 step 7: assemble then read uncovered holes and recomposite_error_rig.png.
2. **Expect:** exit 0; uncovered error px maybe higher than 3,500 on a seated pose (crossed ankles, hand in lap).
3. **Chose / turned down:** Run assemble and read holes. Turned down: building first.
4. **Happened:** exit 0, uncovered error px 1726 (<= 3500), 444 holes, largest 154 px. As expected.

## Entry 3

1. **Read:** README loop: 'propose --parts work/rig --source … --out work' ; AUTHORING §4 step 7 (read LINT lines, notes, landmarks.png).
2. **Expect:** proposal.json plus LINT lines or notes saying what the seated pose breaks (hip/chest screen-y rules, sleeves); exit 0 possibly with LINT.
3. **Chose / turned down:** Run propose with no keypoints first, to see what it itself says. Turned down: passing pose_seated.json immediately, since I want the message that tells me to.
4. **Happened:** exit 0 but 1 LINT line: 'hairback_r and hairback_l on mesh hair_back squeeze it ... edge 37-117 closes to 0.064 times its rest length at idle frame 22 (15.572; <= 1.926544 required) ... amplitudes are opposed (hairback_r [0.6, 1.4, 2.4], hairback_l [-0.6, -1.4, -2.4]) ... give both the same sign (then 1.046), or drop one chain'. Expectation mostly met (I guessed hip/chest or sleeves; it was the two back-hair chains instead, no WTF but my guess about the cause was wrong).

## Entry 4

1. **Read:** The LINT line above (propose, AUTHORING §4 step 8: correct then 'propose … --from-config' until no LINT).
2. **Expect:** After pasting the four blocks and flipping hairback_l's amps to [0.6, 1.4, 2.4] (the same sign as hairback_r), propose --from-config prints 0 LINT line(s), exit 0; the message promised 1.046.
3. **Chose / turned down:** Flip the sign on hairback_l rather than drop a chain: dropping would remove a deforming bone and risk the 'Kept' line and the 'Still moves' line (back hair travel against head). Turned down: lowering amplitudes (the task says not to turn motion down).
4. **Happened:** propose --from-config printed '0 LINT line(s) over 8 mesh(es) and the hip', 37 checked clean. As expected.

## Entry 5

1. **Read:** Task statement build command; AUTHORING §5/§7 for check bars.
2. **Expect:** build exit 0, check PASS 10/10, ANIMATIONS_DO_NOT_FOLD 0; unknown risk: seated pose might fail another bar (hip/chest, TEXTURE_STRETCH).
3. **Chose / turned down:** Build as is. Turned down: adding --keypoints without a failure naming it.
4. **Happened:** build exit 0, check PASS 10 of 10, TEXTURE_STRETCH 1.126 vs 1.926544, uncovered_error_px 1726, ANIMATIONS_DO_NOT_FOLD 0. As expected after the flip; I did not build the unedited proposal, so that it fails is taken from the LINT line, not from a failed build.

## Entry 6

1. **Read:** Task 03 pass lines (Kept 8 meshes, Still moves >= 23 px of back hair against the head).
2. **Expect:** 9 PASS lines incl. still-moves near 45.9 (the task statement's figure for the draft's amplitudes put right) and kept 8.
3. **Chose / turned down:** Run the grader.
4. **Happened:** 6 of 6 PASS; still_moves 45.881 (matches the 45.9 the task statement gave), kept 8. No WTF.

## At the end

- **Where I guessed:** Nothing without a source except key 'exam03' and rig_scale 0.5 (copied from task 01's reading of AUTHORING §3). I decided from the propose LINT line, the squeeze sentence naming amplitudes; I did not open any picture.
- **What I could not find:** I did not learn whether the unedited proposal would fail the build, or what pose_seated.json is for (I never used it; propose put hip and chest acceptably without --keypoints, LINT clean).
