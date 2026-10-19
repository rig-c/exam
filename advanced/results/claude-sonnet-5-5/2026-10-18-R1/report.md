# Report: walk, claude-sonnet-5-5

Final command: `rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --plant-feet --stance 0.03 --leg-scale 0.45,1.05` → `rigc build` → `rigc render --fps 30 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l`; graded with `--trunk chest,head`. Map: `run/map.json` (trunk chest aimed at neck without reach, head by eye line, arms and legs `bend: free`, hip translated by mid_hip with scale mid_hip→neck vs hip→neck).

## Table before → after
"Before" = first full run: `--plant-feet --stance 0.07 --leg-scale 0.8,1.05`, trunk with `reach: true`.

| Row | Before | After |
| --- | --- | --- |
| Gate | PASS 52 assertions, 17/17 landings | PASS same |
| Support foot | PASS 0.0000 | PASS 0.0000 |
| Two feet | FAIL: 42 of 168 lifted frames within 0.01 of support; median lift ratio 0.616 | PASS: 0 of 168; two-foot diff 0.0000; median ratio 0.913 |
| Slide | PASS 0.00002 | PASS 0.00002 |
| Floor | PASS 0.0000 | PASS 0.0000 |
| Jitter | FAIL limbs 1.038x, trunk+head 1.390x | PASS limbs 0.988x, trunk+head 1.000x |
| Folds | PASS 0 | PASS 0 |
| Pass-through | PASS 0/224 both | PASS 0/224 both |
| Loop | PASS 0.0001°, 0.0000 L | PASS 0.0001°, 0.0000 L |

Grader: RESULT PASS (9 pass, 0 fail, 0 skip). Full text in `run/after/grade.txt`. Evidence: `run/evidence/stick_vs_render.png` (stick frames 0,6,12,17,24 beside the render), `run/evidence/lift_cycle1.txt`.

## What I fixed, and where I found how
- Stance 0.07 → 0.03: retarget `--help` for `--stance` (planted within tolerance, lifted above) read against the Two-feet row's 0.04 threshold.
- `--leg-scale` floor 0.8 → 0.45: the `LEG-SCALE ... clamped (asked 0.451–0.786)` lines of retarget output, matched to my own per-frame lift table (`evidence/lift.py`) that showed lift missing only on those frames.
- Dropped `reach: true`: found by experiment after reading the README `reach` bullet and the grader's jitter code; no message pointed to it.

## Could not fix / not done
- `rig-pose compare` not run: needs detector output on the render, not available.
- I did not test whether `reach` could be kept with other settings.

## What the tools should have done
- `retarget` should warn when a `--leg-scale` clamp or `--stance` tolerance changes a lifted foot's height, e.g. a `LIFT` line comparing rig and picture lift per span (the median ratio the grader reads).
- `rig-pose retarget --rig` and `rigc build --rig` should accept the same thing, or the build error should say "pass rig.json".
- The README `reach` bullet should state when it adds jitter, and retarget could print the trunk jitter against the pose's.
- The retarget output could print the hips-to-ankles scale mismatch (rig trunk vs leg proportions; scale 1.77 vs leg ratio 1.14).
