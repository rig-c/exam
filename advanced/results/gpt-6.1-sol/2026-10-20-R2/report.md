# R2 report — gpt-6.1-sol

RESULT PASS (15 pass, 0 fail, 0 skip of 15 rows). Baseline: 7 pass, 7 fail, 1 skip.

| Measure | Before | After |
| --- | --- | --- |
| Gate | green; 12/12 landings | green; 18/18 landings |
| Support foot | 0.0368 L | 0.0000 L |
| Two feet | lift ratio 1.422; 0 low lifts / 60 | lift ratio 1.058; 0 low lifts / 60 |
| Shin scale | p5 1.000 | p5 0.405 |
| Slide | SKIP: no consecutive grounded support pairs | 0.00003 L/frame; scale 1.15418 |
| Floor | spread 0.0000 L | spread 0.0000 L |
| Jitter | limbs 1.000x; trunk/head 0.942x | limbs 1.038x; trunk/head 1.000x |
| Folds | 26 frames | 0 frames / 6 meshes |
| Pass-through | 0/200 both pairs | 0/200 both pairs |
| Loop | 0.8520 degrees; position 0.0000 L | 0.0082 degrees; position 0.0000 L |
| Airborne | 2 spans/cycle; min foot height -0.0069 L | 2 spans/cycle; min foot height 0.0464 L |
| Hip vertical range | 1.466x | 0.987x |
| Hip horizontal range | 1.749x | 1.130x |
| Rebound | 1.466x | 1.332x |
| Hip tilt | 14.390 degrees; 1.000x; positive covariance | 14.390 degrees; 1.000x; positive covariance |

## Fixes and documentation

The seven-chain map keys the pelvis, trunk, eye-line head, both arms and both legs. Bone names came from inputs/rig/rig.json; map syntax, a>b pelvis/head aims, and free hinges came from @rig-c/pose README §The map. Front-facing limbs use bend: free as that section advises.

--leg-scale 0.405,1.2 --plant-feet --stance 0.02 preserve the supplied cleaned sequence while shortening bent legs and holding the support foot to one floor. These flags and the in-place ankle tracking/loop closure are documented in pose README §The legs: foreshortening and planted feet. A 0.400 lower bound was not robust at the exact numeric comparison, despite printing as 0.400; 0.405 supplies a small measured margin. No reduce, smooth, flip, carry-idle or jump override was used.

The original torso-derived translation scale was 1.781042008794223 rig units/pixel, too large for this character's legs. Setup L=485.0927608035908 and sequence Ls=399.2763715909713 give 1.2149297962979186. The map can name two calibration points, so a non-art child of hip, retarget_scale, was placed at L/Ls times the sequence median torso length (202.12886513761842), initially 245.57238094757622 units. This changes no art attachment or body proportion. That run passed 14 rows but horizontal travel was 1.185x. A documented empirical 0.95 correction of this marker yields final scale 1.1541833064830227, vertical 0.987x and horizontal 1.130x. See calibration.json, calibrated/rig.json and calibrated-map.json. README §The map explains translate.scale; these measured calibration values and the last gain are this sitting's work.

Only skirt physics constraints were softened: inertia 0.1, damping 0.6, existing wind and gravity multiplied by 0.2. All 44 physics constraints remain enabled; no mix was muted. AUTHORING.md §4.6 physics gives the tuning fields and their effects. The values are empirical settings tested here, not package defaults. Bottomwear folds decreased 26 -> 16 from foot/leg changes, then to zero with this tuning. Other art and physics parameters were retained.

## Remaining scope and verification

All fifteen official rows pass. No remaining failed or skipped grader row. Two-foot frames do not occur in this input; the two-feet row passes its lifted-foot clause on 60 grounded frames, not an invented flat-foot observation. Detected airborne spans start at cycle frames 3 and 13 and end at 9 and 19; they are within the printed reference 4–9 and 14–19 by the allowed one-frame margin.

The build uses rigc's core/model gate: 52 assertions, 21 measured and passed, 17 skipped, 14 outside the spine profile. In particular, the official Spine runtime parse is SKIP because that runtime is not one of the three pinned packages. This is recorded in after-build.log and is not claimed as an executed check. The grader itself passes without missing inputs.

The evidence uses the supplied stick.mp4, never the unavailable original camera video. evidence/comparison.png shows actual video frames beside before/after render frames at indices 0,3,4,7,10,13,14,17,19. The evidence was visually opened and checked: corresponding labels and alternating leg lifts are visible, with less extreme hem movement. Quantitative floor, airborne and fold claims come from geometry and diagnostics rather than inferring them from pictures. No pose detector exists here, so rig-pose compare was not run. Source inputs were not edited; no commit or push was made.

## What the tools should have done

## Parent output directories are not created
- **I was trying to:** Write the first retarget motion and report into run/before/.
- **The tool gave me:** "FAIL  ARG_PATH: --out run/before/motion.json — directory run/before does not exist" and the matching --report failure.
- **What would have helped:** The Try it command could say, "Create the parent directories for --out and --report first; retarget does not create them."
- **Cost:** Roughly a minute including recording and retrying; resolved with mkdir.

## Translation calibration needs an anatomical recipe
- **I was trying to:** Match normalized pelvis travel on a rig whose torso-to-leg proportions differ from the subject's.
- **The tool gave me:** README §The map: "Pick a long segment that does not foreshorten much." The first SCALE line was "1.78104 rig units per picture px (rig 360.00 / pose median 202.13)".
- **What would have helped:** A documented leg-length calibration option or recipe, with the exact percentile definition and a separate horizontal gain, plus a warning when torso and leg calibration disagree substantially.
- **Cost:** Several minutes and two calibration retarget/build/render iterations; resolved with a measured marker plus a 0.95 empirical gain correction.

## Reported scale hides exact-boundary precision
- **I was trying to:** Keep every rendered shin scale at or above the 0.4 bar.
- **The tool gave me:** "world x axis 0.400 … 1.036" in SHEAR, and LEG-SCALE said scalex was keyed in [0.4, 1.2], while the exact rendered geometry's p5 failed the >=0.4 comparison.
- **What would have helped:** Print more digits on a clamped minimum, or explicitly state that the landing tolerance and serialized transform precision can place the measured value slightly below the requested minimum.
- **Cost:** One failed grading iteration and a small clamp-margin adjustment; resolved at 0.405. This was numeric precision, not a new motion error.

## Final grader output (verbatim)

```text
grade R2
NOTE  airborne spans: report feet.jumps, 20 span(s)
NOTE  rig leg length 485.0928 units (setup pose, leg_l0->foot_l, leg_r0->foot_r); hip width 84.0000
NOTE  sequence leg length 399.28 (95th percentile hip->ankle, mean of sides, the sequence's own units); the sequence carries no camera
PASS  gate            Gate: build green (52 assertions: 21 measured, 0 failed); 18/18 landings within tolerance (worst at 0.15 of its tolerance)
PASS  support-foot    Support foot: max |lower foot - floor| 0.0000 leg lengths at frame 172 over 60 grounded frames (floor 124.711 units) [bar <= 0.01]
PASS  two-feet        Two feet: two-foot frames: none in the sequence; lifted frames (sequence ankles > 0.04 apart): 0 of 60 with the lifted foot within 0.01 of the support foot (lowest lift 0.3718 at frame 80) [bar 0]; median rig/sequence lift 1.058 [bar 0.85-1.15]
PASS  shin-scale      Shin scale: 5th percentile shin x-scale 0.405 over 200 frames x 2 shins (leg_r1, leg_l1; 1.0 = setup length); min 0.405 at frame 173 (leg_r1) [bar >= 0.4]
PASS  slide           Slide: max |support-foot move - closure - sequence ankle move x report scale 1.15418| 0.00003 leg lengths/frame (foot_l, frame 10->11) over 40 steps (travel: in-place; closure +0.04459 units/frame removed (report feet.closure drift -8.87 over 200 frames)) [bar <= 0.005]
PASS  floor           Floor: per-cycle floor spread 0.0000 leg lengths over 10 cycles [bar <= 0.01, the support-foot band: the table gives this row no number of its own]
PASS  jitter          Jitter: limbs 1.038x sequence (10.445 vs 10.060 deg/f^2, 9 bones) [bar <= 1.1], trunk+head 1.000x sequence (2.046 vs 2.046 deg/f^2, chest,head) [bar <= 1.1]; joint pairs from the map
PASS  folds           Folds: 0 frames fold over 6 mesh(es) [bar 0]
PASS  pass-through    Pass-through: bottomwear:thigh_r 0 of 200 frames; bottomwear:thigh_l 0 of 200 frames [bar 0]
PASS  loop            Loop: cycle 1 vs cycle 10: max keyed-bone angle difference 0.0082 deg (sleeve_l1, cycle frame 19) [bar <= 1.0], max hip/foot_l/foot_r world position difference 0.0000 leg lengths (foot_r, cycle frame 19) [bar <= 0.01]
PASS  airborne        Airborne: airborne spans per cycle [2, 2, 2, 2, 2, 2, 2, 2, 2, 2] [bar 2 each]; 0 detected span(s) off the printed spans [(4, 9), (14, 19)] +/- 1 [bar 0]; lowest foot on an airborne frame 0.0464 leg lengths above the floor at frame 139 [bar > 0.01: above the support-foot band]
PASS  hip-vertical    Hip vertical range: rig/sequence 0.987 (rig 0.0942, sequence 0.0954 leg lengths, median per-cycle width over 10 cycles) [bar 0.85-1.15]
PASS  hip-horizontal  Hip horizontal range: rig/sequence 1.130 (rig 0.3718, sequence 0.3291 hip widths, median per-cycle width over 10 cycles) [bar 0.85-1.15]
PASS  rebound         Rebound: median rig/sequence peak upward hip acceleration in the stance windows 1.332 over 19 windows [bar 0.7-1.43]
PASS  hip-tilt        Hip tilt: rig tilt range 14.390 deg = 1.000 of the sequence's 14.390 [bar >= 0.85], sign agrees (covariance +3.66e+03)
RESULT PASS (15 pass, 0 fail, 0 skip of 15 rows)
```
