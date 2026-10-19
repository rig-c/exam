# Journal — claude-sonnet-5-5, Advanced R1 walk, 2026-10-19

## Entry 1

1. **Read:** @rig-c/pose README "The map: rig-pose-map/1" (chains, aim, reach, bend free for front-facing) and `--help` flag list; config.json `limbs` (leg_r0/leg_r1, foot_r; arms sleeve_*).
2. **Expect:** a first map.json (trunk reach, head, 2 arms free, 2 legs free, hip translate) that retarget accepts with the gate green.
3. **Chose / turned down:** write map by hand from the README example; leave all hinges `free` as the README warns for front-facing material; turned down `rest` bend (README says it straightens knees). Start with --plant-feet --stance 0.07 --leg-scale 0.8,1.05 as the card's values.
4. WTF?: Gate green on first try (52 assertions, 17 landings), but the grader gave 7 pass, 2 fail (two-feet: 42 lifted frames planted, median lift ratio 0.616; jitter trunk+head 1.39x). I expected the card's --stance 0.07 to be safe; the PROBLEM bar's lifted-foot threshold is 0.04, so 0.07 plants feet the bar wants lifted. Nothing in the retarget output said so. Next: lower --stance. (Entries 2-6 were written after their steps ran, in one pass at the end, not before: I did not keep lines 1-3 ahead of the steps from here on.)

## Entry 2

1. **Read:** `rigc build --help` (needs `--rig` and `--motion`), PROBLEM.md: grader reads the stdout of the last `rigc build`.
2. **Expect:** `rigc build --rig ../inputs/rig --motion after/motion.json --out after/build` builds; rig is "a directory holding one" per the retarget help.
3. **Chose / turned down:** wrap retarget, build, render --geometry --folds --pass-through and grade in `run/pipeline.sh` + `run/grade.sh` so each trial is one command; turned down running each by hand (too many flags to repeat).
4. WTF?: build exit 1: `cannot read .../inputs/rig: EISDIR (see rigc guide CE_COMPILE_JSON_READ_FAILED)`. retarget's `--rig` takes a directory, `rigc build --rig` does not. Fixed with `--rig ../inputs/rig/rig.json`; build and render then exit 0, pass-through 0/224 on both.

## Entry 3

1. **Read:** retarget `--help`: `--stance <leg lengths>` ("0.07 is the card's"), PROBLEM.md Two feet row (lifted = ankles > 0.04 apart).
2. **Expect:** `--stance 0.03` stops the planter flattening lifted feet, two-feet row passes.
3. **Chose / turned down:** `--stance 0.03` (under the 0.04 lifted threshold); turned down dropping `--stance` entirely (the 0.02 two-foot band needs it).
4. WTF?: lifted frames within 0.01 of support went 42 → 0 but the median rig/sequence lift stayed low, 0.676 (bar 0.85-1.15). Stance was only half the cause.

## Entry 4

1. **Read:** retarget `--help` LEG-SCALE text; the `LEG-SCALE ... leg_r1 ... 77 frame(s) under 0.8, clamped (asked 0.451-0.786)` lines of retarget output; my per-frame lift table (run/lift.py) showing lift missing only on frames 0-9 (and cycle repeats), the frames the clamp names.
2. **Expect:** lowering the --leg-scale floor from the card's 0.8 to 0.45 lets the shin shorten as the picture asks, lift ratio goes into 0.85-1.15.
3. **Chose / turned down:** `--leg-scale 0.45,1.05`; turned down changing translate.scale to the thigh (tried: ratio unchanged 0.676, jitter worse 2.2x; reverted) and `--short`.
4. Lift ratio 0.913, two-feet PASS. (0.3,1.1 gave identical figures.) Matched expectation after the diagnosis; the diagnosis took reading LEG-SCALE lines against my own table, no message linked the clamp to the lift row.

## Entry 5

1. **Read:** README map section on `reach: true`; grade.py jitter section (chest and head are the trunk bones).
2. **Expect:** with `reach` on, chest jitter 1.39x the sequence (0.999 vs 0.719) is from the reach re-aim; removing `reach` brings it near 1.0.
3. **Chose / turned down:** drop `"reach": true` from the trunk chain (kept the reach map as map.reach.json); turned down smoothing with `--reduce` (it thins keys and the bar reads rendered keys).
4. WTF?: all 9 pass with reach removed, trunk+head exactly 1.000x. The README presents reach as the right setting for a trunk bone ("Without it, a tilted pelvis carries the chest's origin sideways"); on this rig the hip is never rotated so reach only added jitter. Nothing in the retarget output hinted at that.

## Entry 6

1. **Read:** PROBLEM.md step 2 (evidence frames beside the stick video).
2. **Expect:** a sheet of 5 stick frames next to the 5 matching render frames.
3. **Chose / turned down:** ffmpeg frame grab + PIL; turned down making a video (not asked).
4. `run/evidence/stick_vs_render.png` written (first try failed: this ffmpeg has no `-vsync` option; dropped it). Poses match: weight shift, lifted foot, arm swing; feet on a common floor.

## At the end

- **Where I guessed:** `--stance 0.03` (anything under 0.04); `--leg-scale` floor 0.45 (just under the observed 0.451 minimum; no source gave it); evidence frame choice (0,6,12,17,24); `--trunk chest,head` from the map. To not guess I would have needed a statement of how the lift row relates to --stance and --leg-scale.
- **What I could not find:** why reach hurts jitter here; whether the grader's lift ratio is meant to be reachable with the card's own 0.8 floor; the detector for `compare` (not available), so compare was not run.
