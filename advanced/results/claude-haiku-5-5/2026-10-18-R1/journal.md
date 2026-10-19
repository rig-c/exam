# Journal — claude-haiku-5-5, walk (R1), 2026-10-18

## Entry 1
1. **Read:** PROBLEM.md "Tools" and `@rig-c/pose` README "The map: `rig-pose-map/1`" (chains, `aim` "a>b", `reach`, `translate.scale`).
2. **Expect:** a map that the retarget accepts; no output file yet.
3. **Chose / turned down:** write map.json with trunk (chest, reach), head (eye_r>eye_l), two arms, two legs, hip translate from mid_hip/neck. Turned down a one-chain-per-side variant without the head chain: the head is needed for the trunk/head jitter row.
4. **Happened:** map.json written; it parses as JSON. Gate not yet tested.

## Entry 2
1. **Read:** PROBLEM.md step 1 ("Put it on"); `rig-pose retarget --help` (--plant-feet, --stance, --leg-scale, --report, --build, --render).
2. **Expect:** a green gate and a motion.json at run/ with report.json, or a refusal line naming the failing bone.
3. **Chose / turned down:** first run with the card's settings `--plant-feet --stance 0.07 --leg-scale 0.8,1.05 --bends refuse --report run/report.json --build run/build --render run/render --out run/motion.json`. Turned down `--reduce` and `--flip`/`--short` for now: they change keys before I know the baseline.
4. **Happened:** refused, exit 1, 226 problems: POSE_BEND_ONE_WAY on arm_r r_elbow frames 200–223 (inner angle 2–10°, rest −9.5°). Nothing written. Not what I expected: I took the bend check as a real joint limit.

## Entry 3
1. **Read:** map.json `bend` rule in `@rig-c/pose` README ("Seen from the front, an elbow's side is not a joint limit"); PROBLEM.md step 3 allows changing the map.
2. **Expect:** the same retarget green once arm chains are `"bend": "free"`.
3. **Chose / turned down:** `"bend": "free"` on the two arm chains, per the README's front-view note. Turned down `--bends clamp`, which straightens the elbow on those frames and changes the measured angle the jitter row reads.
4. **Happened:** arm bend check passed; two MAP_BEND_SIDE on leg_r and leg_l: knees straight at rest (0.18°, 0.28°), side undeclared.

## Entry 4
1. **Read:** the `MAP_BEND_SIDE` line (names `"bend": "ccw" | "cw" | "free"`); the README's front-view note on elbows, which applies to knees too.
2. **Expect:** a green gate if the knees are `"free"`; the side is not in the rest pose, so I cannot read it from the rig.
3. **Chose / turned down:** `"bend": "free"` on the leg chains. Turned down picking ccw or cw by reading a sign: the rest pose says nothing, and a wrong guess would make `--bends refuse` reject the real walk.
4. **Happened:** green. retarget exit 0, gate green, every bone LAND within tolerance, FEET no vertical range, FOLD none, motion.json written (animations idle, walk). Wrote report.json, build/, render/. Matched.

## Entry 5
1. **Read:** PROBLEM.md step 2 (measure with `rigc render --geometry`) and "Pass table"; grade.py header (inputs: `rigc build` stdout, geometry, folds, passthrough).
2. **Expect:** build stdout with the gate line; geometry.json, folds.json, pass-through.json under run/after/.
3. **Chose / turned down:** run `rigc build --rig ../inputs/rig --motion motion.json --out after/build` and capture stdout to after/build.stdout; then the three renders. Turned down reusing retarget's own build as the grader input, since PROBLEM.md says it must be the last `rigc build`'s standard output, not retarget's.
4. **Happened:** WTF?: `rigc build --rig inputs/rig` exit 1, EISDIR, it wants the rig.json file, not the directory, though retarget accepted the directory. The three renders then exited 2 with no output (no build). Nothing was written.

## Entry 6
1. **Read:** the EISDIR line from entry 5 (CE_COMPILE_JSON_READ_FAILED); `rigc build --help` for the rig path form.
2. **Expect:** build exit 0 with --rig inputs/rig/rig.json, a build directory, and gate line.
3. **Chose / turned down:** rerun with `--rig inputs/rig/rig.json`. Turned down copying the rig into run/, since the file path is what the flag asks for.
4. **Happened:** build exit 0 with rig.json. Matched.

## Entry 7
1. **Read:** grade output of the first retarget (run/grade-before.txt): two-feet FAIL (rig/sequence lift median 0.616, bar 0.85–1.15) and jitter FAIL (trunk+head 1.390, bar 1.1). `rigc render --help` (`--pass-through`, `--folds`).
2. **Expect:** render with geometry/folds/pass-through gives 0 folds and 0 passes; grader shows the same two FAILs.
3. **Chose / turned down:** I suspect `--stance 0.07` plants the lifted ankle onto the floor (it pulls any free ankle within 0.07 leg lengths to the floor), which would shrink the lift. Next step tests that. Turned down changing the rig spec before I know that.
4. **Happened:** without --stance: two-feet still FAIL but on a different row: lifted frames now 0 of 168 within 0.01 (good), two-foot max height diff 0.0209 (bar 0.02, just over), lift median 0.676 (bar 0.85–1.15). Jitter unchanged FAIL (trunk+head 1.390). So --stance was not the cause of the low lift; it was the cause of the lifted foot being pinned. Expectation partly wrong: WTF? removing stance did not raise the lift ratio.

## Entry 8
1. **Read:** retarget `--leg-scale` text (clamp to [min,max] of the 95th-percentile picture length over straight length); grade two-feet line (lift median 0.676).
2. **Expect:** leg-scale is the candidate for the lift ratio, since the rig leg (485 units) is longer than the sequence leg (426.7), and the scale clamps at 0.8.
3. **Chose / turned down:** run two variants in separate dirs: `--leg-scale off` and `--leg-scale 0.7,1.1`. Turned down touching the rig spec's leg lengths first, because retarget flags are the cheaper lever and PROBLEM allows them.
4. **Happened:** legoff: two-feet fails the lift rows outright (lift ratio −0.009: lifted foot pinned to the floor, 168 of 168 within 0.01) so leg-scale is what gives lift. Wider 0.7,1.1: median lift 0.890 — inside the band, the first row to reach it. Two-feet still 0.0209 (bar 0.02) on frame 203. Jitter unchanged in all three (trunk+head 1.390).

## Entry 9
1. **Read:** entry 8 results; `--stance` text (plants free ankles within k leg lengths of the support: 0.03 is below the lift threshold 0.04 so it should spare real lifts).
2. **Expect:** with --leg-scale 0.7,1.1 and --stance 0.03, two-feet frame 203 drops under 0.02 while lift stays in band.
3. **Chose / turned down:** `--stance 0.03`. Turned down 0.07 (the card's value): it pinned lifts in the first run.
4. **Happened:** stance 0.03: two-feet PASS (max height diff 0.0000 at frame 203), lift median 0.890 kept. Jitter still FAIL on trunk+head (1.390). Matched in part: the stance fix worked, the trunk row did not.

## Entry 10
1. **Read:** the trunk jitter line (1.390 for chest,head, the largest failing row); `reach` text in the pose README (reach true aims the chest from the posed hip).
2. **Expect:** removing `reach` from the trunk map may change trunk jitter; a map file run/map-noreach.json, separate from map.json.
3. **Chose / turned down:** a separate map copy so map.json (already hashed in report) stays as is. Turned down editing the rig's chest bone: that is a bigger change and PROBLEM's order says map and flags first.
4. **Happened:** removing reach from the trunk chain: 9 of 9 PASS. Trunk+head jitter 1.000 (0.719 vs 0.719), limbs 0.988. Matched the prediction that trunk reach was driving the trunk jitter. Map file: run/map-noreach.json (run/map.final.json copy).

## Entry 11
1. **Read:** run/v6-noreach/grade.txt (9 of 9 PASS); PROBLEM.md "Answer when you finish".
2. **Expect:** the final grader run on the canonical run/after/ files prints RESULT PASS 9/9.
3. **Chose / turned down:** run the grader against run/after/ (copy of v6) rather than the v6 directory, so the final record reads from one place. Turned down re-running retarget: nothing changed.
4. **Happened:** RESULT PASS (9 pass, 0 fail, 0 skip of 9 rows). Matched.

## At the end
- **Where I guessed:** the knee and elbow bend side (`"free"`, not a read sign); the `--stance 0.03` value (I chose it to sit below the 0.04 lift threshold, not from a document figure); the trunk `reach: false` choice.
- **What I could not find:** no document says which `bend` value a knee on this rig takes; no tool output says which flag lowers trunk jitter, I found it by testing.
