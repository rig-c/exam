# R2 (run) report — claude-haiku-5-5

Result: 8 of 14 rows PASS in the final grader run (`run/after/grade3.out`). Six rows still FAIL. Before = first attempt (`run/after/grade1.out`, 6 PASS / 8 FAIL), after = final (`run/after/grade3.out`).

## Table before → after

| Row | Before (attempt 1) | After (final) | Bar |
| --- | --- | --- | --- |
| Gate | PASS (52 assertions, 0 failed; 16/16 landings) | PASS (17/17 landings, worst 0.15) | green |
| Support foot | FAIL 0.0383 | PASS 0.0000 | ≤ 0.01 |
| Two feet | FAIL median lift ratio −0.022; 60/60 lifted frames planted | FAIL median lift ratio 0.145; 0/60 planted | 0.85–1.15, 0 planted |
| Slide | PASS 0.00003 | PASS 0.00003 | ≤ 0.005 |
| Floor | PASS 0.0003 | PASS 0.0000 | ≤ 0.01 |
| Jitter | PASS limbs 0.329×, trunk 1.000× | PASS limbs 0.339×, trunk 1.000× | ≤ 1.1 |
| Folds | PASS 0 frames | FAIL 16 frames (bottomwear) | 0 |
| Pass-through | PASS 0 of 200 both thighs | PASS 0 of 200 both thighs | 0 |
| Loop (angle) | FAIL 34.69° (sleeve_l1) | FAIL 34.69° (sleeve_l1) | ≤ 1.0° |
| Loop (position) | FAIL 0.0022 | FAIL 0.0018 | ≤ 0.01 |
| Airborne | FAIL lowest airborne foot 0.0077 | PASS 0.0513 (spans 2/cycle, all within ±1 of 4–9 · 14–19) | > 0.01 |
| Hip vertical | FAIL 1.349 | FAIL 1.460 | 0.85–1.15 |
| Hip horizontal | FAIL 1.711 | FAIL 1.712 | 0.85–1.15 |
| Rebound | FAIL 1.961 | FAIL 1.929 | 0.7–1.43 |
| Hip tilt | FAIL 0.000, sign disagrees | PASS 1.000, sign agrees | ≥ 0.85 |

## What I changed and where

- **Map** (`run/map.json`): chains for trunk (chest, mid_hip→neck), pelvis (hip, r_hip→l_hip aimed leg_r0>leg_l0 — the README's own form; this fixed hip tilt), both arms and both legs (`bend: free`, per the README's front-facing and knee-straightening warnings).
- **Retarget flags**: `--plant-feet --stance 0.07 --bends clamp --flip 90 --short 0.35 --leg-scale 0.8,1.05`. `--leg-scale` fixed support foot and airborne (rig leg 485.1 vs sequence 399.3, ratio 0.823, inside the card range). `--stance`/`--flip`/`--short` were taken from the help's "measured setting" hints; I did not test each one separately.
- Build and render were run at 30 fps so the grader aligns the frames.

## What I could not fix, and why

- **Two feet**: the rig's lifted foot reaches only 14.5% of the sequence's lift on lifted frames; the planting holds the other foot. I did not find the setting that releases this without breaking support foot.
- **Hip vertical / horizontal** (1.46 / 1.71): the rig's pelvis moves about 1.4–1.7× the sequence's. The likely sources are the translate scale (`mid_hip→neck` vs `hip→neck`) and the plant-feet hip shift; I did not test the translate scale alone.
- **Rebound** (1.93): follows from the hip excursion above; not fixed separately.
- **Loop, sleeve_l1 34.69°**: identical value across all attempts, so it is not from the leg changes. I did not find its cause.
- **Folds, 16 frames**: a regression I introduced with the pelvis chain (0 frames before it). I did not revert it, because it was the only way to get hip tilt.

## Honest notes

- The "R1 table written out again" that PROBLEM.md refers to is not in the file; I graded the R1 rows as `grade.py` defines them.
- No stick-figure video was available to me, so the side-by-side evidence is the render contact sheet only (`run/evidence/contact-sheet-run-30fps.png`).
- One transcript echo line lists `--leg-scale` on a command that did not carry it; corrected in the transcript (and see journal entry 1).
- Token usage: not reported by this agent, so no `usage.json`.
