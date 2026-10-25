# Journal

## Entry 1 (opened 2026-10-25T09:19:18Z)

1. **Read:** fixtures/mannequin/README.md §§The joints and Feet are planted; AUTHORING.md §3 recipe for motion.animations_from
2. **Expect:** build gates green with the added 4-second dance and retains the fixture idle and IK constraints
3. **Chose / turned down:** Add a separate rigc-motion/1 animation file keyed on existing bones; leave all fixture rig data and planted-foot IK unchanged.
4. **Happened** (2026-10-25T09:19:25Z): WTF?: The build refused before rigging because all nine cap paths resolve relative to this run config and the fixture caps were not copied into the run directory.

## Entry 2 (opened 2026-10-25T09:19:29Z)

1. **Read:** fixtures/mannequin/README.md and cap path refusal from the first build
2. **Expect:** With cap PNGs present relative to config, build passes the fixture rig and reports the added dance
3. **Chose / turned down:** Copy the required fixture caps into the config-relative run path and rerun the build.
4. **Happened** (2026-10-25T09:20:42Z): check: PASS; 10 of 14 bar(s) measured, 4 skipped (BLINK_NO_HOLE, TIP_OVER_ROOT, TEXTURE_STRETCH, STRESS_OFF_CHAIN); 0 warning(s) (SEAM_OVER_MOTION, not a bar)

## Entry 3 (opened 2026-10-25T09:20:45Z)

1. **Read:** TASK.md Pass lines and README.md rule 6
2. **Expect:** grader reports 4-second closure, hand/trunk travel, joint motion, planted feet, timing and folds
3. **Chose / turned down:** Run the task grader on the fixture config and authored dance to measure all machine bars.
4. **Happened** (2026-10-25T09:22:39Z): PASS  both_hands: "`hand_l` travels 132.3 rig px and `hand_r` 227.9 at their furthest vertex"; PASS  keeps_time: "1.0 of the variation in how fast she moves repeats every two beats"; 11 of 11 line(s)

## At the end (2026-10-25T09:22:43Z)

- **Where I guessed:** I authored hip translatex ±18 and translatey -10 on alternating beats; chest ±4, head ±6, shoulder ±20/15, elbow ±15/10 and wrist ±10 degrees. The exact track amplitudes and key patterns are authored trial values. The fixture README documents joint names, ranges, IK targets and the positive rotation sign.
- **What I could not find:** The fixture README has no example dance for a body-wide movement that also clears the numeric travel and two-beat timing bars; the package recipe gave a smaller 3 px hip sway for another figure.
