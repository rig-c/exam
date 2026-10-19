# R1 walk — report

Final run: `run/after/` (motion, build, render, report, grade-final.txt). Map: `run/map.final.json` (= `run/map-noreach.json`).
Retarget flags: `--plant-feet --leg-scale 0.7,1.1 --stance 0.03` (defaults otherwise).

## Table: before → after

| Measure | Before (run/grade-before.txt) | After (run/after/grade-final.txt) |
| --- | --- | --- |
| Gate | PASS, 17/17 landings | PASS, 17/17 landings |
| Support foot | PASS, 0.0000 | PASS, 0.0000 |
| Two feet | FAIL: two-foot 0.0000; lift median 0.616 [0.85–1.15] | PASS: two-foot 0.0000; lift median 0.890 |
| Slide | PASS, 0.00002 | PASS, 0.00002 |
| Floor | PASS, 0.0000 | PASS, 0.0000 |
| Jitter | FAIL: limbs 1.038x; trunk+head 1.390x | PASS: limbs 0.988x; trunk+head 1.000x |
| Folds | PASS, 0 | PASS, 0 |
| Pass-through | PASS, 0 / 0 | PASS, 0 / 0 |
| Loop | PASS, 0.0001° / 0.0000 | PASS, 0.0001° / 0.0000 |

Before is the first run with the card's default `--stance 0.07`. Two-feet and jitter were failing; the rest passed.

## What I fixed and where I found how

1. **Arm elbow refusal (`POSE_BEND_ONE_WAY`):** `"bend": "free"` on arm chains. Found in the `@rig-c/pose` README, map section, "Seen from the front, an elbow's side is not a joint limit".
2. **Knee refusal (`MAP_BEND_SIDE`):** `"bend": "free"` on leg chains. The retarget message asked for a side; the rest pose is straight so no side can be read. Same README note applied.
3. **Lift too small (two-feet, lift median 0.616):** `--leg-scale 0.7,1.1` (was 0.8,1.05). `--leg-scale off` made the lift zero; the wider clamp gave 0.890.
4. **Two-foot frame over the band (0.0209):** `--stance 0.03` (was 0.07). The card's 0.07 pinned the lifted foot to the floor; 0.03 sits under the 0.04 lift threshold.
5. **Trunk+head jitter 1.390:** removed `reach: true` from the trunk chain. The README's reach option aims the chest from the posed hip; on this sequence it added jitter. Without it trunk+head is 1.000.

## What I could not fix

Nothing in the table is still failing. Not verified: the proctor's side-by-side check against the original video (only the proctor has the video). My evidence is `run/evidence/side-by-side.png`, the stick video next to the rig render at eight frames of the cycle, from the stick video I extracted in `run/evidence/stick/`.

## What the tools should have done

- `rig-pose retarget` should say which map field to set for a rig whose elbows and knees do not show a side. The `POSE_BEND_ONE_WAY` line gave a number but no option.
- `rigc build --rig <dir>` should accept a directory as `retarget --rig` does, or the error should name the file to use.
- The grader's trunk row could say which chain's reach drives the figure. It printed 1.390 and nothing else.
- The card default `--stance 0.07` should carry a warning that it can pin lifted feet on this kind of sequence.
