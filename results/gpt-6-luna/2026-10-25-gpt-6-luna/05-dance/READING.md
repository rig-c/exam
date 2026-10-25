# Proctor reading

Independent regrade: 11/11 measured lines and three fixture-specific SKIPs. The final journal chain is intact: three entries, one WTF. Task clock: 4.2 minutes from transcript stamps.

The native dance, physics-free and idle sheets were inspected. The mannequin alternates side sway and arm movement while the feet remain on their targets; the measured shin-foot art separation is 5.34 rig pixels. Dynamic seam status is CLEAR for this choreography. No human quality mark is assigned.

The private judge clip is three loops, 12 seconds, with 24 clicks at 120 BPM. The motion file is authored, while all fixture config fields except the added named-motion path remain identical.

| Line | Result | Read |
| --- | --- | --- |
| built | PASS | "rig-parts build exit 0" |
| checked | PASS | {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "SKIP", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "SKIP", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "SKIP", "ANIMATIONS_DO_NOT_FOLD": "PASS", "FEET_STAY_LEVEL": "PASS", "STRESS_OFF_CHAIN": "SKIP", "LIMB_ONE_BONE": "PASS", "SEAM_OVER_RANGE": "PASS", "SEAM_OVER_MOTION": "CLEAR", "RECOMPOSITE_HOLES": "REPORTED"} |
| whole | PASS | "uncovered_error_px 73 against <= 4200" |
| does_not_fold | PASS | [] |
| dance_as_timed | PASS | "`dance` lasts 4 s against 4.0" |
| closes | PASS | "the last frame is 0.0 rig px from the first at its furthest vertex, against <= 0.5 (keys only, physics out)" |
| both_hands | PASS | "`hand_l` travels 132.3 rig px and `hand_r` 227.9 at their furthest vertex, measured from the middle of `topwear`, each against >= 100.0" |
| whole_body | PASS | "the vertex of `topwear` that travels least travels 15.2 rig px, measured from the middle of `foot_l` and `foot_r`, against >= 15.0" |
| on_her_feet | PASS | "the end of a leg (`shin_l`, `shin_r`) gets 5.34 rig px from where it meets `foot_l`, `foot_r`, against <= 6.0" |
| keeps_time | PASS | "1.0 of the variation in how fast she moves repeats every two beats, against >= 0.5" |
| dance_does_not_fold | PASS | [] |
| budget | SKIP | not read on this fixture: the rig is given and has no mesh to count (tasks/05-dance/TASK.md) |
| arms_bend_at_the_joints | SKIP | not measured: every arm part (`upperarm_l`, `forearm_l`, `upperarm_r`, `forearm_r`) is rigid on one bone and turns only at a joint that declares its range (elbow [-45, 45], wrist [-45, 45]); a rigid part cannot bend along its own length, so the line has nothing on this rig to tell apart |
| soft_in_the_dance | SKIP | not read on this fixture: the rig is given and has no physics (tasks/05-dance/TASK.md) |

Numeric overlap check: the authored hip-X magnitude 18 also appears in the earlier gpt-6-sol sitting. Key times, phase and the vertical track differ; none of ten other handed-in complete dance definitions matched. The shared number is recorded alongside tool-call provenance, without attributing copying. No forbidden-answer read or delegation was observed.

The original journal/transcript and captured outputs remain unedited. The cap-path refusal was resolved in the sitting; the canonical grader supplies fixture cap closure independently.
