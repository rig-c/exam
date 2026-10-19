# Report — R2 (run), claude-opus-5-5

Final: `run/after/` (motion.json, build/, render/run@30fps/, report.json, grade_final.txt). Map `run/map_v4.json`. Rig `run/rig_v6/` (copy of inputs/rig, feet `inherit: onlyTranslation`). Retarget flags: `--plant-feet --leg-scale 0.05,1.05 --stance 0.07`. Baseline: `run/before/` (run/map.json, inputs/rig, `--leg-scale 0.8,1.05`).

## Table, before → after

| Row | Before | After | Bar |
| --- | --- | --- | --- |
| Gate | green, 18/18 land | green, 18/18 land | green |
| Support foot | 0.0000 | 0.0000 | ≤ 0.01 |
| Two feet | lift ratio 1.281 FAIL (no two-foot frames) | lift ratio 0.966, lowest lift 0.513 | 0.85–1.15, > 0.01 |
| Slide | 0.00003 | 0.00003 | ≤ 0.005 |
| Floor | 0.0000 | 0.0000 | ≤ 0.01 |
| Jitter | limbs 1.050×, trunk+head 1.387× FAIL | limbs 1.039×, trunk+head 1.000× | ≤ 1.1 |
| Folds | 16 frames (bottomwear) FAIL | 0 | 0 |
| Pass-through | 0 / 0 | 0 / 0 | 0 |
| Loop | 0.0082°, 0.0000 L | 0.0082°, 0.0000 L | ≤ 1°, ≤ 0.01 |
| Airborne | 2/cycle, 0 off, lowest 0.0513 | 2/cycle, 0 off, lowest 0.0456 | 2, ±1, > 0.01 |
| Hip vertical | 1.460 FAIL | 0.928 | 0.85–1.15 |
| Hip horizontal | 1.712 FAIL | 1.059 | 0.85–1.15 |
| Rebound | 1.929 FAIL | 1.257 | 0.7–1.43 |
| Hip tilt | 1.000, cov > 0 | 1.000, cov > 0 | ≥ 0.85, > 0 |

Grader: 8/14 → 14/14.

## What I fixed, and where I found how

1. **Translate scale → shoulder width** (`"pose": ["r_shoulder","l_shoulder"], "rig": ["sleeve_r0","sleeve_l0"]`): hip vertical, horizontal, rebound. Found from the `SCALE` line ("1.78104 rig units per picture px (rig 360.00 / pose median 202.13)") against the grader's hip-vertical figure (1.460 = 1.781 ÷ 485/399), and README "The map": "`translate.scale` … Pick a long segment that does not foreshorten much." The leg (the obvious choice for leg-length rows) foreshortens in a run: its median is 303 px against a 399 px straight leg.
2. **Trunk without `reach`**: trunk+head jitter. Found by splitting the grader's jitter per bone (run/jitter_by_bone.py); README "The map", `reach`: aimed "from where its origin is posed — the hip moved and turned".
3. **`--leg-scale 0.05,1.05`**: two-feet lift. Found from the `LEG-SCALE` line ("leg_r1 … picture length ÷ straight 0.089 … 1.036 … 110 frame(s) under 0.8, clamped") and README "--leg-scale": "clamped to [min, max]".
4. **Feet `inherit: onlyTranslation`** (rig spec): not a row — the feet were squashed (`SHEAR bone "foot_r": art sheared up to 78.08°`). README "--leg-scale": the foot under a `normal` shin "is squashed along the shin: `SHEAR` reads both"; inherit modes from rig-c docs/AUTHORING.md (`inherit` row).
5. Folds went to 0 as a side effect of fix 1; no physics value was changed.

Evidence: run/evidence/sheet_v6_cycle2.png (stick | rig, cycle frames 0–18 step 2; v5 sheet beside it shows the squashed feet).

## What I could not fix, and why

- Nothing fails the table. Not measured by it: the two-foot clause has no frames in this sequence (no grounded frame has ankles within 0.02 Ls), so it is untested; `--stance 0.07` plants nothing here.
- The rig cannot bend a knee toward the camera; on the heel-kick frames the shin is scaled to ~0.09 of its length, so the knee and boot read as stacked rather than folded (visible on frames 48–52). That is the 2D rig's limit, not something a flag fixes.

## What the tools should have done

- `retarget` should say when `SCALE`'s segment is foreshortened in the sequence (median ≪ p95, as the leg here: 303 vs 399 px), and print the hip rows' figures in leg lengths and hip widths beside `POSTURE`, so a wrong scale shows up at the retarget, not at the grader.
- `POSTURE` or `LAND` should read each trunk bone's rotation jitter against its pair; `reach: true` doubled the chest's and nothing printed it.
- `LEG-SCALE` should warn when the clamp floor holds an end-on segment long on frames where its leg is free (it moves the foot by up to ~0.3 leg lengths here), and suggest the asked minimum.
- `SHEAR` should say what to do about a squashed foot (an `inherit` mode), not only read it.
- `rigc build --rig <dir>` should accept the directory `rig-pose retarget --rig` accepts, or its error should say "pass rig.json".
