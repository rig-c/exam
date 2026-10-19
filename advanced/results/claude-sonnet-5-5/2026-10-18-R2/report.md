# R2 report — claude-sonnet-5-5

Final command: `rig-pose retarget --plant-feet --stance 0.07 --leg-scale 0.5,1.05` with `run/map.json`; `run/go.sh` builds, renders and grades. Evidence: `evidence/side_by_side_frames_0_6_12_16.png` (stick video left, rig right, frames 0/6/12/16), `evidence/grade_final.txt`.

| Row | First run (stance 0.07, leg-scale 0.8,1.05, trunk-pair scale, reach) | Final |
| --- | --- | --- |
| Gate | green | green |
| Support foot | 0.0000 | 0.0000 |
| Two feet | FAIL lift ratio 1.281 | PASS (0.5 floor) |
| Slide | 0.00003 | 0.00003 |
| Floor | 0.0000 | 0.0000 |
| Jitter | FAIL limbs 1.049x, trunk+head 1.520x | 1.038x / 1.000x |
| Folds | FAIL 16 frames | 0 |
| Pass-through | 0 | 0 |
| Loop | 0.0082° / 0.0000 | same |
| Airborne | PASS | PASS |
| Hip vertical | FAIL 1.460 | 0.928 |
| Hip horizontal | FAIL 1.712 | 1.059 |
| Rebound | FAIL 1.929 | 1.257 |
| Hip tilt | 1.000 | 1.000 |

RESULT PASS (14 pass, 0 fail).

## What I fixed, where I found how
- Hip ranges and rebound: translate.scale pair changed to shoulders (1.08). Found by arithmetic from the grader's NOTE lines (rig/sequence leg length, hip width) and the first run's ratios; the README map bullet says only "pick a long segment that does not foreshorten much".
- Jitter/folds: dropped `reach` from the trunk (README `reach` bullet: aimed at the end "scaled"). Found by experiment.
- Two-feet: `--leg-scale` minimum 0.8 -> 0.5. Found by sweeping; the help gives 0.8,1.05 as "the card's range".

## Could not fix
Nothing in the table is open. Not checked: how the art looks in motion beyond four frames.

## What the tools should have done
- `retarget` should create the output directory (or say which) — it refused `--out` into a missing dir.
- State in the map docs that translate.scale also sizes `reach`, and warn when trunk and leg proportions make hip travel exceed the pose's by >15%.
- Print the rig/pose leg and hip-width ratios in retarget's output so the scale pair can be chosen without the grader.
- A `rigc build --rig` that accepts the directory retarget accepts.
- The map error for a foot bone should say body-18 has no toe joint.
