# Proctor reading

Independent rebuild: 11 / 11 measured lines, three fixture-specific SKIPs. Final journal chain: one entry and one WTF. The captured self-grader output printed zero WTF before closing its own step; that output remains unchanged. This regrade reads the final closed journal and correctly reports one.

The native 24fps dance sheet, physics-free counterpart and idle sheets were inspected. The motion alternates arm reach and a bent-knee hip bounce; knee/neck seam warnings remain present. Machine acceptance is not a claim of zero visible seam artifacts. No human quality rating is assigned.

The private judging clip follows TASK.md: three complete loops, 12 seconds, and a click on each of 24 beats at 120 BPM. Its stream and decoded click timing were checked; the receipt is adjacent. The 4-second base preview is provenance, not the judging format.

| Line | Result | Read |
| --- | --- | --- |
| built | PASS | "rig-parts build exit 0" |
| checked | PASS | {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "SKIP", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "SKIP", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "SKIP", "ANIMATIONS_DO_NOT_FOLD": "PASS", "FEET_STAY_LEVEL": "PASS", "STRESS_OFF_CHAIN": "SKIP", "LIMB_ONE_BONE": "PASS", "SEAM_OVER_RANGE": "PASS", "SEAM_OVER_MOTION": "WARN", "RECOMPOSITE_HOLES": "REPORTED"} |
| whole | PASS | "uncovered_error_px 73 against <= 4200" |
| does_not_fold | PASS | [] |
| dance_as_timed | PASS | "`dance` lasts 4 s against 4.0" |
| closes | PASS | "the last frame is 0.0 rig px from the first at its furthest vertex, against <= 0.5 (keys only, physics out)" |
| both_hands | PASS | "`hand_l` travels 403.6 rig px and `hand_r` 409.0 at their furthest vertex, measured from the middle of `topwear`, each against >= 100.0" |
| whole_body | PASS | "the vertex of `topwear` that travels least travels 54.2 rig px, measured from the middle of `foot_l` and `foot_r`, against >= 15.0" |
| on_her_feet | PASS | "the end of a leg (`shin_l`, `shin_r`) gets 4.95 rig px from where it meets `foot_l`, `foot_r`, against <= 6.0" |
| keeps_time | PASS | "1.0 of the variation in how fast she moves repeats every two beats, against >= 0.5" |
| dance_does_not_fold | PASS | [] |
| budget | SKIP | not read on this fixture: the rig is given and has no mesh to count (tasks/05-dance/TASK.md) |
| arms_bend_at_the_joints | SKIP | not measured: every arm part (`upperarm_l`, `forearm_l`, `upperarm_r`, `forearm_r`) is rigid on one bone and turns only at a joint that declares its range (elbow [-45, 45], wrist [-45, 45]); a rigid part cannot bend along its own length, so the line has nothing on this rig to tell apart |
| soft_in_the_dance | SKIP | not read on this fixture: the rig is given and has no physics (tasks/05-dance/TASK.md) |

The required prompt/README hashes match the post-fix source. The original ledger, transcript and captured outputs are unedited; the raw-path integrity exception is recorded in who.json. No delegation or forbidden-answer read was observed.

The independent dynamic seam reader reports thigh_l|shin_l open on 17 frames (max 50 cells/pixels as reported) and neckpiece|headpiece on nine (max 6), while static range validation passes. These reported warnings are retained rather than treated as clean seams.
