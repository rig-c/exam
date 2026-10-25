# Proctor reading — gpt-5.6-sol, 05-dance

Filed from `7c3535564fd7a2c9dc3e3a653d1dd5789c1fc042` on source parent `0643977fb2adb99eb91fc48cceb166b1b587b3bf`. Only submitted inputs are trusted.

Independent regrade on @rig-c/parts 1.60.0 and rig-c 2.67.2: **11 of 11**, 3 skipped.

```text
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "SKIP", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "SKIP", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "SKIP", "ANIMATIONS_DO_NOT_FOLD": "PASS", "FEET_STAY_LEVEL": "PASS", "STRESS_OFF_CHAIN": "SKIP", "LIMB_ONE_BONE": "PASS", "SEAM_OVER_RANGE": "PASS", "SEAM_OVER_MOTION": "WARN", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 73 against <= 4200"
PASS  does_not_fold: []
PASS  dance_as_timed: "`dance` lasts 4 s against 4.0"
PASS  closes: "the last frame is 0.0 rig px from the first at its furthest vertex, against <= 0.5 (keys only, physics out)"
PASS  both_hands: "`hand_l` travels 152.0 rig px and `hand_r` 236.3 at their furthest vertex, measured from the middle of `topwear`, each against >= 100.0"
PASS  whole_body: "the vertex of `topwear` that travels least travels 17.3 rig px, measured from the middle of `foot_l` and `foot_r`, against >= 15.0"
PASS  on_her_feet: "the end of a leg (`shin_l`, `shin_r`) gets 0.87 rig px from where it meets `foot_l`, `foot_r`, against <= 6.0"
PASS  keeps_time: "1.0 of the variation in how fast she moves repeats every two beats, against >= 0.5"
PASS  dance_does_not_fold: []
SKIP  budget: "not read on this fixture: the rig is given and has no mesh to count (tasks/05-dance/TASK.md)"
SKIP  arms_bend_at_the_joints: "not measured: every arm part (`upperarm_l`, `forearm_l`, `upperarm_r`, `forearm_r`) is rigid on one bone and turns only at a joint that declares its range (elbow [-45, 45], wrist [-45, 45]); a rigid part cannot bend along its own length, so the line has nothing on this rig to tell apart"
SKIP  soft_in_the_dance: "not read on this fixture: the rig is given and has no physics (tasks/05-dance/TASK.md)"
journal: chain intact, 5 entries, 3 WTF
```

Seven sheets inspected. Idle stays upright; dance repeats an alternating arm, torso and hip sway four times while feet remain in the same floor region. Figure stays visible throughout the sheets. Small joint cracks are below dependable sheet-scale visual resolution; retain the measured forearm_r|hand_r and neckpiece|headpiece motion warnings. No human dance or beat mark assigned.

Pictures and the [render receipt](render-receipt.json) bind the retained sheets to normalized commands and ordered frame hashes. Grader exit 0 is process completion; the individual lines above are the machine verdict.

The fixture config differs only by `motion.animations_from`; no bones, parts, constraints or physics were added. Static `SEAM_OVER_RANGE` PASS and `SEAM_OVER_MOTION` WARN are different readings. The latter remains a warning in the successful build, and machine 11/11 does not erase it. The blind three-loop click-track clip is prepared separately; human mark remains empty.

Clock: 2026-10-25T09:58:55Z to 2026-10-25T10:05:21Z, 386 seconds by the unedited transcript. The clock includes stopped attempts where present.
