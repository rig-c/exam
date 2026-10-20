# R1 — gpt-6.1-sol

RESULT PASS (10 pass, 0 fail, 0 skip of 10 rows).

| Measure | Before | After |
|---|---|---|
| Gate | green; 12/12 landings | green; 18/18 landings |
| Support foot max floor error | 0.0603 L | 0.0003 L |
| Two-foot max gap | 0.0165 L | 0.0006 L |
| Lifted frames too low | 140/168; minimum -0.0188 L | 0/168; minimum 0.0220 L |
| Median rig/source lift ratio | 0.013 | 0.938 |
| Shin scale p5 / minimum | 1.000 / 1.000 | 0.631 / 0.451 |
| Slide max residual | 0.01173 L/frame | 0.00315 L/frame |
| Cycle-floor spread | 0.0000 L | 0.0000 L |
| Jitter limbs | 1.142x; 1.253 vs 1.097 deg/frame² | 0.955x; 1.048 vs 1.097 |
| Jitter trunk/head | 1.588x; 1.790 vs 1.127 | 0.852x; 0.960 vs 1.127 |
| Folds | 0 frames / 6 meshes | 0 frames / 6 meshes |
| Pass-through | both pairs 0/224 | both pairs 0/224 |
| Loop angle / position | 1.3809° / 0.0000 L | 0.4928° / 0.0034 L |

## Fixes and sources

The final command uses --leg-scale 0.4,1.2 --plant-feet --stance 0.02 --reduce 0.25 and run/map-parallel.json. The rig spec and physics values are unchanged. The pose sequence is unchanged.

Pose README “The map” supplies the chains, eye-line and pelvis aims, free hinges for front-facing motion and measured trunk scale. “The legs: foreshortening and planted feet” supplies segment scaling, one floor, in-place closure and stance. “Few keys: --reduce” supplies bounded reduction and explains why ankle error increases with angle tolerance. Trial 0.5 passed jitter but failed slide; 0.2 passed slide but failed jitter; 0.35 failed both. The trunk had reach:true despite its origin being 180 rig units above the translated hip. The map section states that without reach the trunk stays parallel to the reference. Turning reach off and using 0.25 passed both. This sacrifices shoulder endpoint matching to follow the measured trunk angle without an origin-offset re-aim.

The measured translation scale is 1.7707134152696318 rig units/source unit, from hip→neck / median mid_hip→neck. Rig L is 485.0928; source Ls is 426.70. The declared in-place closure drift is -224.73 units over 224 frames; grader removes +1.00778 units/frame. These are not travel-free visual fidelity claims.

## Verification and remaining limits

All ten grader rows pass. Six synchronized evidence panels (0,8,16,24,77,205) were visually inspected in evidence/comparison.png. Each panel has separately fitted viewports: it is not a pixel comparison. Red lines are ankle-origin floor readings, not shoe-sole collision planes. The foot has one ankle bone; toe articulation and true sole contact were not added. Hair/skirt physics remain on with no new keyed physics bones. No detector is supplied, so rig-pose compare was not run and no detector-based or original-video similarity is claimed. Only the stick video and sequence were available.

The standalone build measured 21 assertions with zero failures; 17 assertions were skipped and 14 outside the spine profile. In particular A00_ROUNDTRIP_PARSE is skipped because the installed entry does not link spine-core. Grader itself reports zero skipped rows. No additional packages were installed to hide this distinction.

Initial setup broke prospective journaling and wrote a wrong placeholder timestamp. Those records are preserved verbatim in transcript.tmp, the journal and setup-history. Proctor message 0b4756d4-91df-45b2-92fe-d7d6348185f3 explicitly directed continuation and preservation. This report supersedes the premature termination claim, not the record of the slip.

## What tools should have done

See tools.md: separate reduction precision from smoothing, and warn about displaced-origin reach mapping.

## Final grader output

```text
grade R1
NOTE  airborne spans: report feet.jumps, 0 span(s)
NOTE  rig leg length 485.0928 units (setup pose, leg_l0->foot_l, leg_r0->foot_r); hip width 84.0000
NOTE  sequence leg length 426.70 (95th percentile hip->ankle, mean of sides, the sequence's own units); the sequence carries no camera
PASS  gate            Gate: build green (52 assertions: 21 measured, 0 failed); 18/18 landings within tolerance (worst at 0.95 of its tolerance)
PASS  support-foot    Support foot: max |lower foot - floor| 0.0003 leg lengths at frame 74 over 224 grounded frames (floor 70.981 units) [bar <= 0.01]
PASS  two-feet        Two feet: two-foot frames: max height difference 0.0006 leg lengths at frame 139 over 35 [bar <= 0.02]; lifted frames (sequence ankles > 0.04 apart): 0 of 168 with the lifted foot within 0.01 of the support foot (lowest lift 0.0220 at frame 77) [bar 0]; median rig/sequence lift 0.938 [bar 0.85-1.15]
PASS  shin-scale      Shin scale: 5th percentile shin x-scale 0.631 over 224 frames x 2 shins (leg_r1, leg_l1; 1.0 = setup length); min 0.451 at frame 165 (leg_r1) [bar >= 0.4]
PASS  slide           Slide: max |support-foot move - closure - sequence ankle move x report scale 1.77071| 0.00315 leg lengths/frame (foot_l, frame 74->75) over 209 steps (travel: in-place; closure +1.00778 units/frame removed (report feet.closure drift -224.73 over 224 frames)) [bar <= 0.005]
PASS  floor           Floor: per-cycle floor spread 0.0000 leg lengths over 7 cycles [bar <= 0.01, the support-foot band: the table gives this row no number of its own]
PASS  jitter          Jitter: limbs 0.955x sequence (1.048 vs 1.097 deg/f^2, 8 bones) [bar <= 1.1], trunk+head 0.852x sequence (0.960 vs 1.127 deg/f^2, hip,chest,head) [bar <= 1.1]; joint pairs from the map
PASS  folds           Folds: 0 frames fold over 6 mesh(es) [bar 0]
PASS  pass-through    Pass-through: bottomwear:thigh_r 0 of 224 frames; bottomwear:thigh_l 0 of 224 frames [bar 0]
PASS  loop            Loop: cycle 1 vs cycle 7: max keyed-bone angle difference 0.4928 deg (head, cycle frame 24) [bar <= 1.0], max hip/foot_l/foot_r world position difference 0.0034 leg lengths (foot_l, cycle frame 18) [bar <= 0.01]
RESULT PASS (10 pass, 0 fail, 0 skip of 10 rows)
```
