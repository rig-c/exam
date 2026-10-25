# Proctor reading

Independent rebuild: 11 / 11 measured lines; three fixture-specific SKIPs. Journal chain intact, two entries, zero WTF. Task clock: 2.9 minutes from the submitted started:/finished: lines.

The native 24fps dance sheet, physics-free counterpart and idle sheets were read. The whole mannequin remains in frame and repeats the shoulder/hip motif. This reading does not assign a dance-quality score. The blind 4-second clip was delivered privately; its stream/hash receipt is adjacent, and the human judgement remains empty.

**Rubric exposure:** before any task, this sitting read the then-required README containing prior results and task-05 grade-line names absent from TASK.md. HQ directed that the run continue and be graded with this flag. Its machine result must not be represented as a clean rubric-blind comparison. Later post-fix sessions are distinct.

| Machine line | Result | Read |
| --- | --- | --- |
| built | PASS | "rig-parts build exit 0" |
| checked | PASS | {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "SKIP", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "SKIP", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "SKIP", "ANIMATIONS_DO_NOT_FOLD": "PASS", "FEET_STAY_LEVEL": "PASS", "STRESS_OFF_CHAIN": "SKIP", "LIMB_ONE_BONE": "PASS", "SEAM_OVER_RANGE": "PASS", "SEAM_OVER_MOTION": "WARN", "RECOMPOSITE_HOLES": "REPORTED"} |
| whole | PASS | "uncovered_error_px 73 against <= 4200" |
| does_not_fold | PASS | [] |
| dance_as_timed | PASS | "`dance` lasts 4 s against 4.0" |
| closes | PASS | "the last frame is 0.0 rig px from the first at its furthest vertex, against <= 0.5 (keys only, physics out)" |
| both_hands | PASS | "`hand_l` travels 368.5 rig px and `hand_r` 195.4 at their furthest vertex, measured from the middle of `topwear`, each against >= 100.0" |
| whole_body | PASS | "the vertex of `topwear` that travels least travels 16.7 rig px, measured from the middle of `foot_l` and `foot_r`, against >= 15.0" |
| on_her_feet | PASS | "the end of a leg (`shin_l`, `shin_r`) gets 0.8 rig px from where it meets `foot_l`, `foot_r`, against <= 6.0" |
| keeps_time | PASS | "1.0 of the variation in how fast she moves repeats every two beats, against >= 0.5" |
| dance_does_not_fold | PASS | [] |
| budget | SKIP | not read on this fixture: the rig is given and has no mesh to count (tasks/05-dance/TASK.md) |
| arms_bend_at_the_joints | SKIP | not measured: every arm part (`upperarm_l`, `forearm_l`, `upperarm_r`, `forearm_r`) is rigid on one bone and turns only at a joint that declares its range (elbow [-45, 45], wrist [-45, 45]); a rigid part cannot bend along its own length, so the line has nothing on this rig to tell apart |
| soft_in_the_dance | SKIP | not read on this fixture: the rig is given and has no physics (tasks/05-dance/TASK.md) |

The supplied mannequin uses rigid jointed parts and no physics. Budget, along-part bending and physics softness are not measured here, rather than silently passed. The core check also reports SEAM_OVER_MOTION WARN; it is not hidden by the overall pass.

Original journal/transcript and ledger remain byte-identical to the hand-in. The raw transcript path exception is recorded in who.json. No delegation or forbidden-answer fetch was observed. The authored numeric and pre-build expectation checks are discussed in the other readings and who.json.
