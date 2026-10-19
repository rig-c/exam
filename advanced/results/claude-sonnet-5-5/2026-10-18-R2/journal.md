# Journal — claude-sonnet-5-5, Advanced R2 (run), 2026-10-19

## Entry 1

1. **Read:** @rig-c/pose README "The map: rig-pose-map/1" (pelvis aim example `leg_r0>leg_l0`, trunk `reach`, head `eye_r>eye_l`), `retarget --help` (--plant-feet, --stance, --leg-scale).
2. **Expect:** first retarget writes motion.json and a green gate (exit 0); unknown how many R2 rows pass.
3. **Chose / turned down:** map with pelvis chain on hip (r_hip>l_hip), trunk reach chest, head by eye line, arms free, legs free; flags `--plant-feet --stance 0.07 --leg-scale 0.8,1.05`. Turned down starting with no flags: R1-style legs need them for the foot rows anyway.
4. **Happened:** (below)
WTF?: first retarget failed twice before it ran: (a) `--out` into a directory that did not exist ("ARG_PATH ... directory run/after does not exist"), (b) a leg chain with the foot as a 3rd bone needs 4 joints (MAP_CHAIN_JOINTS) and body-18 has no toe, so I dropped the foot bone from the legs (it inherits). Then retarget exit 0 and gate green. My own `rigc build --rig <dir>` also failed (EISDIR) until I passed rig.json; retarget accepts the dir but build does not. First grade: 8 pass, 6 fail (two-feet lift ratio 1.281, jitter trunk+head 1.520x, folds 16 frames, hip-vertical 1.460, hip-horizontal 1.712, rebound 1.929).

## Entry 2

1. **Read:** grader notes: report scale 1.781 (from my map's translate.scale pose mid_hip-neck 202 px vs rig hip-neck 360); rig leg 485 vs sequence leg 399 (1.215); hip width 84 vs 82.5. Hip vertical wants scale in 1.04–1.40, horizontal 0.88–1.20 (both derived from the first run's ratios).
2. **Expect:** changing the translate scale pair to shoulders (pose r_shoulder-l_shoulder 141 px vs rig sleeve_r0-sleeve_l0 152, ratio about 1.08) brings hip-vertical and hip-horizontal into 0.85–1.15.
3. **Chose / turned down:** the shoulder pair; turned down the hip-width pair (1.02) because vertical would then be 0.83, under the bar.
4. **Happened:** (below)
WTF?: hip-vertical 0.928, hip-horizontal 1.059, rebound 1.257 passed as expected (11 pass, 3 fail) — but jitter trunk+head went from 1.52x to 3.625x and folds went 16 -> 155 frames (hair_front). Nothing told me that translate.scale also sizes the `reach` trunk aim; I think the reach target (mid_shoulder relative to mid_hip, "scaled") now lands at the wrong distance, so the chest angle wobbles.

## Entry 3

1. **Read:** README map bullets on `reach` ("where the pose puts the segment's end relative to mid_hip, scaled") — the scale is the translate scale.
2. **Expect:** trunk without `reach` (aim `neck`, joints mid_hip→mid_shoulder, plain direction) cuts trunk jitter below 1.1x and the hair_front folds, at the cost of the chest origin sliding on hip tilt.
3. **Chose / turned down:** remove reach; turned down going back to the 1.78 scale since vertical/horizontal hip rows need the smaller one.
4. **Happened:** (below)
Without `reach` (aim `neck`): 13 pass, 1 fail. Trunk+head jitter 1.000x and folds 0 — matched. Only two-feet left (lift ratio 1.294, bar 0.85–1.15).

## Entry 4

1. **Read:** retarget --help `--leg-scale <min,max>` ("clamped to [min, max]", default card 0.8,1.05) and `--stance`; the grader's lift row (rig lift ÷ sequence lift, in leg lengths). The rig's legs are 1.215x the sequence's, and a 0.8 floor stops a leg shortening enough to lift the foot as far as the sequence does.
2. **Expect:** lowering the leg-scale minimum lowers the lifted foot's height; ratio from 1.294 toward 1.0 somewhere between 0.4 and 0.8.
3. **Chose / turned down:** swept min 0.6 / 0.5 / 0.4 with max 1.05 and `--stance 0.07`. Turned down raising the max (1.3) and dropping `--stance`: both broke airborne and hip-vertical (11 pass).
4. **Happened:** 0.6 -> 1.175 (fail), 0.5 -> PASS 14/14, 0.4 -> PASS 14/14. Kept 0.5, the less extreme. Final grader: RESULT PASS (14 pass, 0 fail, 0 skip). Matched. (I guessed the 0.5/0.4 candidates; nothing in the docs gives a rule for the minimum.)

## At the end

- **Where I guessed:** the translate scale pair (shoulders, chosen by arithmetic from the grader's ratios, not from a doc); `--stance 0.07` (the card value from --help); `--leg-scale` minimum 0.5 (swept). To not guess I would have needed a doc line saying translate.scale sets hip travel and the reach trunk, and one on how the leg-scale floor relates to lifted-foot height.
- **What I could not find:** why `reach` with a changed translate scale makes trunk jitter 3.6x and folds hair_front; which scale pair the tools intend for a rig whose trunk/leg proportions differ from the person's. Whether `--carry-idle` / `--reduce` matter for this table (not used).
