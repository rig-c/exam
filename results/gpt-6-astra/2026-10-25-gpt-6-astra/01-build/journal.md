# Journal

## Entry 1 (opened 2026-10-25T11:34:36Z)

1. **Read:** AUTHORING §4 steps 6-7; supplied seethrough.json
2. **Expect:** Plan proposal will save layer rows to config and name omitted layers.
3. **Chose / turned down:** Created config with supplied seethrough and chosen half-size rig_scale 0.5. Use automatic plan, not guessed layer grouping.
4. **Happened** (2026-10-25T11:35:00Z): Saved plan: added assemble.plan and added assemble.extend_below_crop; omitted empty layers and nose named as expected.

## Entry 2 (opened 2026-10-25T11:35:00Z)

1. **Read:** AUTHORING §4 step 7 and plan notes
2. **Expect:** Assemble writes parts and reports uncovered painting pixels.
3. **Chose / turned down:** Use proposed plan unchanged for first assembly; no speculative patches.
4. **Happened** (2026-10-25T11:35:36Z): 22 parts written; uncovered error px: 1812 is below task limit 3700.

## Entry 3 (opened 2026-10-25T11:35:37Z)

1. **Read:** AUTHORING §4 step 7; assembled parts output
2. **Expect:** Proposer writes bones, meshes, regions and idle; lint may identify draft corrections.
3. **Chose / turned down:** Derive skeleton from measured parts without external keypoints; save proposal into config.
4. **Happened** (2026-10-25T11:35:48Z): Wrote proposal.json (23 bone entries, 8 meshes); 1 LINT line(s) over 8 mesh(es) and the hip. Hairback opposed amplitudes squeeze to 2.455; same sign predicts 1.051.

## Entry 4 (opened 2026-10-25T11:35:54Z)

1. **Read:** Proposer squeeze LINT and landmarks.png; TASK pass lines
2. **Expect:** Same-sign hairback motion should remove squeeze; grader should build and pass four task lines.
3. **Chose / turned down:** Changed only hairback_l amplitudes from negative to positive [0.6,1.4,2.4]; preserve both chains rather than delete one. Grader supplies full build and fold measurement.
4. **Happened** (2026-10-25T11:36:52Z): 4 of 4 line(s); built, checked, whole 1812 and does_not_fold all PASS. Journal chain intact. Clock finish remains to be written after this grader.

## At the end (2026-10-25T11:36:52Z)

- **Where I guessed:** Authored key exam-astra and rig_scale 0.5, a convenient half resolution. All skeleton/mesh values proposed; hairback_l signs corrected from explicit LINT recommendation.
- **What I could not find:** No blocking documentation gaps for this task.
