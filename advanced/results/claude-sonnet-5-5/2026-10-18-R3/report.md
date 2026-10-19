# R3 dance — claude-sonnet-5-5

Final command (run/after, via run/pipe.sh): `rig-pose retarget --rig inputs/rig --map map.json --pose inputs/pose/sequence.json --plant-feet --leg-scale 0.8,1.05 --stance 0.03 --camera camera.json --report report.json`, then `rigc build`, `rigc render --geometry --folds --pass-through …`. Grader: 13 pass, 0 fail.

## Table, before → after
"Before" = first valid run (map with trunk `reach:true`, `--stance 0.07`, no `--reduce`).

| Row | Before | After |
| --- | --- | --- |
| Gate | green, 20/20 landings | green, 20/20 |
| Support foot | 0.0000 | 0.0000 |
| Two feet | FAIL: lifted frames 0 of 35 clear of the support foot | PASS, lift ratio 0.933 |
| Slide | 0.00003 | 0.00003 |
| Floor | 0.0000 | 0.0000 |
| Jitter | FAIL limbs 1.150x, trunk+head 1.664x | PASS 0.989x / 1.060x |
| Folds | 0 | 0 |
| Pass-through | 0 | 0 |
| Airborne | 3 spans (88-91, 179-181, 267-269) | same, min peak 0.0245 |
| Hip vertical | 1.049 | 1.049 |
| Hip horizontal | 1.023 | 1.023 |
| Rebound | 1.334 | 1.334 |
| Hip tilt | 1.000, sign agrees | same |

## What I fixed, and where I found how
- **Two feet:** `--stance 0.07` (the value `rig-pose retarget --help` calls "the card's") plants the free foot within 0.07 leg lengths, but the bar calls a foot lifted from 0.04. `--stance 0.03` clears it. Source: README "The legs…" `--stance` paragraph plus the bar in PROBLEM.md.
- **Jitter:** `--reduce` lowers it (limbs 1.04x, trunk 1.15x at 1°) but the reduced legs move the planted ankle: slide fails at 1° (0.0165) and 0.5° (0.011), and at 0.25° slide passes but jitter does not. I turned it off. A per-bone table with the grader's own functions (run/perbone.py) showed the chest at 2.03x and the head 2.28x with the other bones ≈1.0; the chest was aimed with `reach:true`, whose aim runs from the posed hip origin, not along the shoulder pair. Removing `reach` put the chest on the pair's own angle (1.0x). Source: README map section, `reach`.
- Mistake along the way: I first graded with `--feet leg_r1,leg_l1`, whose origins are the knees; support-foot and slide failed for that reason alone. The default `foot_l,foot_r` is right.

## Not fixed
- Head 1.29x on its own (inside the combined bar). The README warns that without `reach` a tilted pelvis carries the chest origin sideways, so the shoulders may miss; no row measures that, and I did not look at it in the render beyond the evidence frames.
- I did not use the `face` readings beyond writing the dial blocks; yaw/pitch were not checked against the video (the proctor has it).

## What the tools should have done
- `rig-pose retarget --help` should say that `--stance`'s card value 0.07 plants feet the R3-style lifted band (0.04) calls lifted, or print the sequence's own lifted/two-foot threshold in the `STANCE` line.
- `--reduce` should say which line of the report moved the ankles when slide would worsen, or offer `--reduce` that holds the ankle to a tolerance in leg lengths of the slide bar.
- `reach:true` should print the jitter cost (its angle is not the pair's angle); a per-bone jitter reading would have saved the experiment.
- The grader's `--feet` default needs the doc to say which bone origin counts as the ankle.
