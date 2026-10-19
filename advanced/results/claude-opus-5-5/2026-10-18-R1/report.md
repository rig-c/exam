# Report — walk (Advanced R1), claude-opus-5-5

Final: `rig-pose retarget --rig inputs/rig --map run/after/map.json --pose inputs/pose/sequence.json --out run/after/motion.json --name walk --leg-scale 0.45,1.05 --plant-feet --stance 0.035 --build run/after/build --report run/after/report.json`, then `rigc build --rig inputs/rig/rig.json --motion run/after/motion.json --out run/after/rigc-build` and `rigc render --candidate run/after/rigc-build --animation walk --fps 30 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l`. Rig spec and physics values unchanged.

## The table

"Before" is the plain retarget with my first map (run/map.json: trunk with `reach`, head on the eye line, no leg flags).

| Measure | Bar | Before | After |
| --- | --- | --- | --- |
| Gate | green, every bone lands | PASS (11/11 landings) | PASS (17/17, worst 0.12 of tolerance) |
| Support foot | ≤ 0.01 L | FAIL 0.0608 | PASS 0.0000 |
| Two feet | two-foot ≤ 0.02; lifted > 0.01 on every frame; median ratio 0.85–1.15 | FAIL 0.0074 / 168 of 168 flat / −0.010 | PASS 0.0000 / 0 of 168 (lowest 0.0176) / 0.913 |
| Slide | ≤ 0.005 L/frame | FAIL 0.01176 | PASS 0.00002 |
| Floor | ≤ 0.01 L | PASS 0.0000 | PASS 0.0000 |
| Jitter | ≤ 1.1× (limbs; trunk+head) | FAIL 1.056× / 1.601× | PASS 0.988× / 1.000× |
| Folds | 0 | PASS 0 | PASS 0 |
| Pass-through | 0 frames | PASS 0 / 0 | PASS 0 / 0 |
| Loop | ≤ 1°, ≤ 0.01 L | FAIL 1.3799° (head) / 0.0000 | PASS 0.0001° / 0.0000 |

Note: the jitter row's trunk+head denominator changed with the map (0.719 → 0.427 deg/f²) because the head is now graded against neck→nose, the pair it is keyed from.

## What I fixed, and where I found how

- **Loop and trunk+head jitter** — head chain moved off the eye line to `["neck","nose"]` aimed at `head_up:tip`. Found by comparing cycle 1 and 7 keys (only `head rotate`/`head translate` differ) and the README "What it does" paragraph on the eye-line nod: "the clamped vertical nod (`clampedY`) is coupled in phase into … the head bone's `rotate` track (+1.6°/unit)". Aim syntax from README "The map" (`aim` point, `name:tip`).
- **Limb jitter** — trunk `reach` removed. README "The map": reach exists because "a tilted pelvis carries the chest's origin sideways"; this map has no pelvis chain.
- **Support foot, slide, floor** — `--plant-feet` (README "The legs", the "In place (#92)" and "One floor (#85)" bullets): each support follows its ankle's scaled x, all spans on one floor, loop closed (feet.closure drift −225.41).
- **Two feet (lift)** — `--leg-scale` with floor 0.45; the `LEG-SCALE` line's "77 frame(s) under 0.8, clamped … asked 0.451–0.786" said the card's 0.8 withheld the lift.
- **Two feet (two-foot frames, no lifted frame planted)** — `--stance 0.035`; the `STANCE planted both … up to 0.0629 leg lengths` lines plus the `--stance` text ("the leg length FEET uses") against grade.py's lifted threshold (0.04 Ls, Ls the 95th percentile).

## What I could not fix, and why

Nothing on the table fails. What the numbers do not show: the lifted foot is drawn by squashing the shin to as little as 0.45 of its length (evidence/frame005.png) — it reads as a short shin with the boot at mid-shin height, not a knee coming toward the camera. A rig with no depth and no alternate drawing for that knee cannot do better; it needs a painted foreshortened-shin alternate.

## What the tools should have done

1. **The eye-line nod should be periodic on a periodic input, or switchable.** A sequence cleaned with `--loop` and declared `"travel": "in-place"` got a head rotate that differs 1.38° between identical cycles. Either compute it per cycle / wrapped like `clean --loop`, or give `--nod off`; and say in the README what window the nod is read over.
2. **`--stance` and the `FEET` leg length should state their unit next to the number.** 0.07 "leg lengths" is the median hip→ankle, not the 95th-percentile straight leg the leg-scale and the bars use — a 7 % difference on this clip — and the card's 0.07 plants feet that are visibly lifted in a walk. A `STANCE` line could say "0.07 × 399 px = 28 px".
3. **`--leg-scale`'s clamp should say what it cost.** The line lists "asked 0.451–0.786" but not what that does to the feet; a "lift withheld: median X leg lengths" figure would have pointed straight at the fix.
4. **`reach` should warn when the map has no pelvis chain**, since then it only moves the chest (and its arms) off the pose.
5. **`rigc render` should say whether physics ran** (a `physics on/off` line), since a table row is defined "with physics on".
