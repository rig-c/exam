# Journal

## Entry 1 (opened 2026-10-25T09:56:39Z)

1. **Read:** tasks/05-dance/TASK.md, tasks/05-dance/fixture.json, fixtures/mannequin/README.md, fixtures/mannequin/config.json, and AUTHORING.md §3 Recipe: planted feet on a parts figure
2. **Expect:** grade.py passes all 11 counted lines (built, checked, whole, does_not_fold, dance_as_timed, closes, both_hands, whole_body, on_her_feet, keeps_time, dance_does_not_fold) with 3 SKIP lines (budget, arms_bend_at_the_joints, soft_in_the_dance)
3. **Chose / turned down:** run python3 grade.py runs/2026-10-25-gemini-4-argon-high-05-dance
4. **Happened** (2026-10-25T10:01:03Z): 11 of 11 line(s), 3 skipped (budget, arms_bend_at_the_joints, soft_in_the_dance); PASS keeps_time: "1.0 of the variation in how fast she moves repeats every two beats, against >= 0.5"; PASS on_her_feet: "the end of a leg (`shin_l`, `shin_r`) gets 5.83 rig px from where it meets `foot_l`, `foot_r`, against <= 6.0"

## At the end (2026-10-25T10:01:14Z)

- **Where I guessed:** the exact hip translatex/translatey combination (+-15 / -18 rig px) so that the lowest 4 % of shin_l and shin_r stay within 6.0 rig px of foot_l and foot_r as leg_l1 and leg_r1 rotate about the ankle pivots
- **What I could not find:** although foot_r_tgt and foot_l_tgt hold the ankle joints at [320, 1108] and [507, 1108], the shin art extends slightly below the ankle pivot and rotates with leg_*1 while foot_* keeps inherit: noRotationOrReflection, so even zero ankle-pivot error produces ~5.83 rig px of bottom-4% shin-to-foot vertex shift; a pre-build kinematics or requirement check for bottom-of-part offset under IK rotation would avoid having to run a full build to measure it
