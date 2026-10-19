# Report — dance (Advanced R3), claude-haiku-5-5

## Table: before → after (grader, same script)

Before = run/evidence/grade_before.txt (first working retarget, no pelvis chain, `--stance 0.07`, `--reduce 0.5`).
After = run/evidence/grade_final_promoted.txt (the files in run/after/).

| Measure | Before | After | Bar |
| --- | --- | --- | --- |
| Gate | PASS, 52 assertions green, 24 measured | PASS, 52 green, 18/18 landings | green |
| Support foot | FAIL 0.0240 | PASS 0.0000 | ≤ 0.01 |
| Two feet | FAIL two-foot max 0.0310; median lift 0.003 | PASS two-foot 0.0000; median lift 0.963 | ≤ 0.02; 0.85–1.15 |
| Slide | FAIL 0.00766 (foot_l) | PASS 0.00003 | ≤ 0.005 |
| Floor | PASS 0.0003 | PASS 0.0000 | ≤ 0.01 |
| Jitter | PASS limbs 0.736×, trunk+head 0.857× | PASS limbs 0.860×, trunk+head 1.000× | ≤ 1.1× |
| Folds | PASS 0 | PASS 0 | 0 |
| Pass-through | PASS 0 | PASS 0 | 0 |
| Airborne | PASS 3 spans, min peak 0.0116 | PASS 3 spans, min peak 0.0246 | 3 spans; > 0.01 |
| Hip vertical | PASS 1.024 | PASS 1.049 | 0.85–1.15 |
| Hip horizontal | PASS 1.094 | PASS 1.045 | 0.85–1.15 |
| Rebound | PASS 1.333 | PASS 1.334 | 0.7–1.43 |
| Hip tilt | FAIL 0.000 (sign disagrees) | PASS 1.000 (sign agrees) | ≥ 0.85 |
| **Rows** | **9 pass, 4 fail** | **13 pass, 0 fail** | |

Camera NOTE (hand-in): present, 313 entries, t = frameTimes (max diff 0.000000 s).

## What I fixed and where I found how

- **Hip tilt** — translate-only map never keys hip rotation. Found by reading map.ts header (chain aim "a bone name" = direction to that descendant). Fix: `pelvis` chain on `hip` (run/map.json).
- **Support, two-feet and slide** — swept `--stance` (0.07 → 0.02 → 0.035) and `--reduce` (on → off). `--stance 0.035` with no `--reduce` passes all three. Found by the grader's rows plus the retarget's FEET/STANCE lines.
- **Knee bend guard** — `--bends clamp` (566 one-way frames on leg_l l_knee, up to -6.4 deg).

## What I could not fix or verify

- **Knee clamp is unverified against the video.** The 566 frames were at up to -6.4 deg past straight, and `--bends clamp` straightens them. I did not check the video, so this may hide a real bent knee.
- **Stance and reduce are a sweep, not a derivation.** Every result is one grader run. Small change (e.g. --reduce 0.5 → 0.3) not tried.
- **Hip-vertical margin is narrow** (1.049 inside 0.85–1.15) and the rig vertical range is 0.107 vs 0.0997 leg lengths. Not tuned.
- **Jitter trunk+head at 1.000×** sits on the bar edge (≤ 1.1, so passes) — not checked for stability.
- **Face yaw/pitch dials** were not mapped (the task mentions them; the table has no row for them). Left unmapped.
- **Video comparison**: only the proctor has the original video. Evidence frames (run/evidence/side_by_side_*.png) compare the rig render with stick.mp4 only.

## What the tools should have done

- `rig-pose retarget --rig inputs/rig/rig.json` refused with the gate's message but did not say the motion.json beside it is required; the directory form works. A one-line hint would have saved a round trip.
- The bend guard prints one line per frame (566). A per-hinge summary (count, worst angle, frames) on the first line would make `--bends clamp` a deliberate choice rather than a flood.
- `--report` is needed for grade.py but is not default; the `retarget` output has no pointer to it.
- grade.py's R3 floor row silently changes to the report's support spans only when `--cycle` is absent; the reason is in the row text but not in `--help`.
- Nothing in rig-pose tells you that `--stance` and `--reduce` interact on the slide row.
