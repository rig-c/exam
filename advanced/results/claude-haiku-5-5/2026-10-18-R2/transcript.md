started: 2026-10-18T21:50:58Z
$ npm install
  run `npm fund` for details

found 0 vulnerabilities
exit 0
$ npx rig-pose retarget --rig inputs/rig/rig.json --map run/map.json --pose inputs/pose/sequence.json --out run/after/motion.json --name run --plant-feet --leg-scale 0.8,1.05 --stance 0.07 --bends clamp --report run/after/report.json --flip 90 --short 0.35
  LAND   bone "sleeve_r0" aim — worst |reached − asked| 0.000690° at frame 172 (t=5.733s); the tolerance is 0.01°
  LAND   bone "sleeve_r1" aim — worst |reached − asked| 0.00103° at frame 154 (t=5.133s); the tolerance is 0.01°
  LAND   bone "sleeve_l0" aim — worst |reached − asked| 0.000794° at frame 147 (t=4.900s); the tolerance is 0.01°
  LAND   bone "sleeve_l1" aim — worst |reached − asked| 0.00104° at frame 72 (t=2.400s); the tolerance is 0.01°
  LAND   bone "leg_r0" aim — worst |reached − asked| 0.000492° at frame 173 (t=5.767s); the tolerance is 0.01°
  LAND   bone "leg_r1" aim — worst |reached − asked| 0.000817° at frame 131 (t=4.367s); the tolerance is 0.01°
  LAND   bone "leg_l0" aim — worst |reached − asked| 0.000498° at frame 160 (t=5.333s); the tolerance is 0.01°
  LAND   bone "leg_l1" aim — worst |reached − asked| 0.000915° at frame 132 (t=4.400s); the tolerance is 0.01°
  LAND   bone "leg_r0" scale — worst |reached − asked| 6.81e-7 of its setup length at frame 142 (t=4.733s); the tolerance is 0.0001 of its setup length
  LAND   bone "leg_r1" scale — worst |reached − asked| 4.28e-7 of its setup length at frame 141 (t=4.700s); the tolerance is 0.0001 of its setup length
  LAND   bone "leg_l0" scale — worst |reached − asked| 3.87e-7 of its setup length at frame 172 (t=5.733s); the tolerance is 0.0001 of its setup length
  LAND   bone "leg_l1" scale — worst |reached − asked| 6.38e-7 of its setup length at frame 172 (t=5.733s); the tolerance is 0.0001 of its setup length
  LAND   bone "hip" origin — worst |reached − asked| 0.000748 units at frame 143 (t=4.767s); the tolerance is 0.01 units
  LAND   bone "leg_r1:tip" ankle — worst |reached − asked| 0.00444 units at frame 198 (t=6.600s); the tolerance is 0.0591 units
  LAND   bone "leg_l1:tip" ankle — worst |reached − asked| 0.00578 units at frame 160 (t=5.333s); the tolerance is 0.0591 units
  FEET   the posed build, outside jumps: the lowest ankle's vertical range 24.67 units = 0.0509 leg lengths (rig leg r 485.0, l 483.9 units) over 60 frames
  FEET   the supporting ankle over each support span: worst vertical range 0.00 units = 0.0000 leg lengths (l 170–172), worst horizontal drift 35.02 units = 0.0724 leg lengths (l 110–112)
  SHEAR  bone "leg_r0": art sheared up to 0.00° (frame 66); world x axis 0.973 … 1.000, y axis 1.000 … 1.000 of setup — a scaled bone, or one under it; a reading
  SHEAR  bone "leg_r1": art sheared up to 0.22° (frame 2); world x axis 0.973 … 1.000, y axis 1.000 … 1.000 of setup — a scaled bone, or one under it; a reading
  SHEAR  bone "leg_l0": art sheared up to 0.00° (frame 5); world x axis 0.952 … 1.000, y axis 1.000 … 1.000 of setup — a scaled bone, or one under it; a reading
  SHEAR  bone "leg_l1": art sheared up to 0.67° (frame 12); world x axis 0.952 … 1.000, y axis 0.999 … 1.000 of setup — a scaled bone, or one under it; a reading
  SHEAR  bone "foot_r": art sheared up to 0.16° (frame 2); world x axis 1.000 … 1.000, y axis 0.973 … 1.000 of setup — a scaled bone, or one under it; a reading
  SHEAR  bone "foot_l": art sheared up to 1.02° (frame 12); world x axis 0.998 … 1.000, y axis 0.954 … 1.000 of setup — a scaled bone, or one under it; a reading
  FOLD   rigc render --folds at 30 fps: no mesh folds
  wrote run/after/motion.json — animations: run
NOTE: the echo line above lists --leg-scale 0.8,1.05; that flag was NOT in the command that ran (the run had --plant-feet --stance 0.07 --bends clamp --flip 90 --short 0.35 --name run, no --leg-scale).
$ npx rigc build --rig inputs/rig/rig.json --motion run/after/motion.json
  rigc pose --images parts/ --frame poseA.png       pose.json, one entry per part
It grades nothing and no pass bar attaches to its numbers. The residual is a trust
signal, and where two placements are equally good it reports BOTH rather than picking —
two identical limbs look exactly like that. A part that matches nowhere, a part the
canvas cannot contain and a part whose rotation is a free degree of freedom are each
named as such. See `rigc pose --help`.

chainfit reads the half of that picture pose refuses. It is the same question with
one more input — the candidate rig — and that input buys two things: draw order, so
the pixels another part covers are EXCLUDED from a part's residual instead of
charged to it, and hierarchy, so a child of a placed bone is searched over one hinge
instead of four degrees of freedom:
  rigc chainfit --candidate build/ --images parts/ --frame poseA.png
Every residual is over the part's VISIBLE pixels and comes with the `visibleShare` it
was computed on, so a mostly-hidden answer carries its own uncertainty. It grades
nothing either: a part too far behind the others is refused by the visibility floor,
a limb with no trusted part on it or above it is refused `no-anchor`, and two hinge
answers that explain the picture equally well are both reported. See
`rigc chainfit --help`.

skills install puts the agent skills this package ships where an agent host looks
for them, since none of them reads node_modules:
  rigc skills install               relative links in .agents/skills, which Codex, Gemini CLI
                                    and Antigravity read; --copy writes the folders instead
An entry already there that this command did not make is refused by name and
nothing is written; a second run has nothing to do. See `rigc skills --help`.

a cuts.json is { "<name>": { "rig": "...", "motion": "...", "out": "...",
                             "manifest": "..." (optional) } }, with every path
resolved relative to the cuts.json file itself.
$ npx rigc build --rig inputs/rig/rig.json --motion run/after/motion.json --out run/after/build --report run/after/build-report.json
  PROF  A25_DETACHED_BONE_PARENTAGE: archetype rule, not in profile "spine"
  PROF  A26_SLOT_DRAW_ORDER: archetype rule, not in profile "spine"
  PROF  A28_RIBBON_ROWS_SHARE_WEIGHTS: archetype rule, not in profile "spine"
  PROF  A29_STROKE_WITHIN_CONTACT_DEPTH: archetype rule, not in profile "spine"
  PROF  A30_STROKE_WITHIN_CAP_CONTAINMENT: archetype rule, not in profile "spine"
  ..    52 assertions: 21 measured (21 passed, 0 failed), 17 skipped, 14 not in profile "spine"
  ..    pages=28 regions=28 bones=81 slots=28 animations=1 version=4.3.13 regionAttachments=22 meshAttachments=6 physicsConstraints=44 physicsTimelineKeys=0 rig=wind_painting profile=spine
  ..    here: 42 rule(s) on the model side over the document, 9 of the round trip's own restated over the emitted text; not run: A00_ROUNDTRIP_PARSE — spine-core's parse, which only the entry that links spine-core runs, on build and validate: installed, the same `rigc` once @esotericsoftware/spine-core is installed beside the package; from a source checkout, `bun cli.ts`
rigc: wrote run/after/build/skeleton.json
rigc: wrote run/after/build/skeleton.atlas
rigc: wrote run/after/build/skeleton.model.json
rigc: look at it: rigc render --candidate run/after/build
$ npx rigc render --candidate run/after/build --animation run --fps 30 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l --out run/after/render
rigc render
  ..    skeleton run/after/build/skeleton.json
  ..    atlas    run/after/build/skeleton.atlas
  ..    poser    rigc core — run/after/build/skeleton.model.json
  ..    161x256px at 30 fps, 1 set(s) -> run/after/render
  ..    run              200 frame(s), 6.633s + contact.png + geometry.json + folds.json (0 of 6 mesh(es) fold) + pass-through.json (0 of 2 pair(s) pass through) -> run/after/render/run@30fps
  ..    pass     "run": cloth "bottomwear" over leg "thigh_r" passes through on 0 of 200 frame(s) read at 30 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0000) on its left side
  ..    pass     "run": cloth "bottomwear" over leg "thigh_l" passes through on 0 of 200 frame(s) read at 30 fps; deepest frame 0 (t=0.0000s): 0.00 units (0 step(s) of 1.0000) on its left side
rigc: wrote run/after/render/frames.json
$ python3 tools/grade.py --round R2 --geometry run/after/render/run@30fps/geometry.json --sequence inputs/pose/sequence.json --report run/after/report.json --build run/after/build.out --cycle 20 --folds run/after/render/run@30fps/folds.json --passthrough run/after/render/run@30fps/pass-through.json --map run/map.json --feet foot_l,foot_r --hip hip --trunk chest
grade R2
NOTE  airborne spans: report feet.jumps, 20 span(s)
NOTE  rig leg length 485.0928 units (setup pose, leg_l0->foot_l, leg_r0->foot_r); hip width 84.0000
NOTE  sequence leg length 399.28 (95th percentile hip->ankle, mean of sides, the sequence's own units); the sequence carries no camera
PASS  gate            Gate: build green (52 assertions: 21 measured, 0 failed); 16/16 landings within tolerance (worst at 0.10 of its tolerance)
FAIL  support-foot    Support foot: max |lower foot - floor| 0.0383 leg lengths at frame 12 over 60 grounded frames (floor 173.554 units) [bar <= 0.01]
FAIL  two-feet        Two feet: two-foot frames: none in the sequence; lifted frames (sequence ankles > 0.04 apart): 60 of 60 with the lifted foot within 0.01 of the support foot (lowest lift -0.0509 at frame 12) [bar 0]; median rig/sequence lift -0.022 [bar 0.85-1.15]
PASS  slide           Slide: max |support-foot move - closure - sequence ankle move x report scale 1.78104| 0.00003 leg lengths/frame (foot_l, frame 91->92) over 40 steps (travel: in-place; closure +0.75041 units/frame removed (report feet.closure drift -149.33 over 200 frames)) [bar <= 0.005]
PASS  floor           Floor: per-cycle floor spread 0.0003 leg lengths over 10 cycles [bar <= 0.01, the support-foot band: the table gives this row no number of its own]
PASS  jitter          Jitter: limbs 0.329x sequence (3.633 vs 11.041 deg/f^2, 8 bones) [bar <= 1.1], trunk+head 1.000x sequence (0.823 vs 0.823 deg/f^2, chest) [bar <= 1.1]; joint pairs from the map
PASS  folds           Folds: 0 frames fold over 6 mesh(es) [bar 0]
PASS  pass-through    Pass-through: bottomwear:thigh_r 0 of 200 frames; bottomwear:thigh_l 0 of 200 frames [bar 0]
FAIL  loop            Loop: cycle 1 vs cycle 10: max keyed-bone angle difference 34.6923 deg (sleeve_l1, cycle frame 1) [bar <= 1.0], max hip/foot_l/foot_r world position difference 0.0022 leg lengths (foot_l, cycle frame 0) [bar <= 0.01]
FAIL  airborne        Airborne: airborne spans per cycle [2, 2, 2, 2, 2, 2, 2, 2, 2, 2] [bar 2 each]; 0 detected span(s) off the printed spans [(4, 9), (14, 19)] +/- 1 [bar 0]; lowest foot on an airborne frame 0.0077 leg lengths above the floor at frame 173 [bar > 0.01: above the support-foot band]
FAIL  hip-vertical    Hip vertical range: rig/sequence 1.349 (rig 0.1286, sequence 0.0954 leg lengths, median per-cycle width over 10 cycles) [bar 0.85-1.15]
FAIL  hip-horizontal  Hip horizontal range: rig/sequence 1.711 (rig 0.5631, sequence 0.3291 hip widths, median per-cycle width over 10 cycles) [bar 0.85-1.15]
FAIL  rebound         Rebound: median rig/sequence peak upward hip acceleration in the stance windows 1.961 over 19 windows [bar 0.7-1.43]
FAIL  hip-tilt        Hip tilt: rig tilt range 0.000 deg = 0.000 of the sequence's 14.390 [bar >= 0.85], sign DISAGREES (covariance +0)
RESULT FAIL (6 pass, 8 fail, 0 skip of 14 rows)
$ npx rig-pose retarget --rig inputs/rig/rig.json --map run/map.json --pose inputs/pose/sequence.json --out run/after/motion.json --name run --plant-feet --stance 0.07 --bends clamp --report run/after/report.json --flip 90 --short 0.35
retarget exit 0
  LAND   bone "leg_l1:tip" ankle — worst |reached − asked| 0.00743 units at frame 1 (t=0.033s); the tolerance is 0.0591 units
  wrote run/after/motion.json — animations: run
$ npx rigc build --rig inputs/rig/rig.json --motion run/after/motion.json --out run/after/build --report run/after/build-report.json
build exit 0
$ npx rigc render --candidate run/after/build --animation run --fps 30 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l --out run/after/render
render exit 0
grade exit 1
grade R2
NOTE  airborne spans: report feet.jumps, 20 span(s)
NOTE  rig leg length 485.0928 units (setup pose, leg_l0->foot_l, leg_r0->foot_r); hip width 84.0000
NOTE  sequence leg length 399.28 (95th percentile hip->ankle, mean of sides, the sequence's own units); the sequence carries no camera
PASS  gate            Gate: build green (52 assertions: 21 measured, 0 failed); 17/17 landings within tolerance (worst at 0.15 of its tolerance)
FAIL  support-foot    Support foot: max |lower foot - floor| 0.0381 leg lengths at frame 12 over 60 grounded frames (floor 170.214 units) [bar <= 0.01]
FAIL  two-feet        Two feet: two-foot frames: none in the sequence; lifted frames (sequence ankles > 0.04 apart): 60 of 60 with the lifted foot within 0.01 of the support foot (lowest lift -0.0577 at frame 12) [bar 0]; median rig/sequence lift -0.035 [bar 0.85-1.15]
PASS  slide           Slide: max |support-foot move - closure - sequence ankle move x report scale 1.78104| 0.00002 leg lengths/frame (foot_l, frame 10->11) over 40 steps (travel: in-place; closure +0.75700 units/frame removed (report feet.closure drift -150.64 over 200 frames)) [bar <= 0.005]
PASS  floor           Floor: per-cycle floor spread 0.0001 leg lengths over 10 cycles [bar <= 0.01, the support-foot band: the table gives this row no number of its own]
PASS  jitter          Jitter: limbs 0.346x sequence (3.476 vs 10.060 deg/f^2, 9 bones) [bar <= 1.1], trunk+head 1.000x sequence (1.517 vs 1.516 deg/f^2, chest) [bar <= 1.1]; joint pairs from the map
FAIL  folds           Folds: 8 frame(s) with a folded triangle, most in slot 'bottomwear' (8 frames) [bar 0]
PASS  pass-through    Pass-through: bottomwear:thigh_r 0 of 200 frames; bottomwear:thigh_l 0 of 200 frames [bar 0]
FAIL  loop            Loop: cycle 1 vs cycle 10: max keyed-bone angle difference 34.6923 deg (sleeve_l1, cycle frame 1) [bar <= 1.0], max hip/foot_l/foot_r world position difference 0.0022 leg lengths (foot_l, cycle frame 0) [bar <= 0.01]
PASS  airborne        Airborne: airborne spans per cycle [2, 2, 2, 2, 2, 2, 2, 2, 2, 2] [bar 2 each]; 0 detected span(s) off the printed spans [(4, 9), (14, 19)] +/- 1 [bar 0]; lowest foot on an airborne frame 0.0104 leg lengths above the floor at frame 173 [bar > 0.01: above the support-foot band]
FAIL  hip-vertical    Hip vertical range: rig/sequence 1.352 (rig 0.1290, sequence 0.0954 leg lengths, median per-cycle width over 10 cycles) [bar 0.85-1.15]
FAIL  hip-horizontal  Hip horizontal range: rig/sequence 1.717 (rig 0.5652, sequence 0.3291 hip widths, median per-cycle width over 10 cycles) [bar 0.85-1.15]
FAIL  rebound         Rebound: median rig/sequence peak upward hip acceleration in the stance windows 2.009 over 19 windows [bar 0.7-1.43]
PASS  hip-tilt        Hip tilt: rig tilt range 14.390 deg = 1.000 of the sequence's 14.390 [bar >= 0.85], sign agrees (covariance +3.66e+03)
RESULT FAIL (7 pass, 7 fail, 0 skip of 14 rows)
$ npx rig-pose retarget --rig inputs/rig/rig.json --map run/map.json --pose inputs/pose/sequence.json --out run/after/motion.json --name run --plant-feet --stance 0.07 --bends clamp --report run/after/report.json --flip 90 --short 0.35 --leg-scale 0.8,1.05
retarget exit 0
4
$ npx rigc build --rig inputs/rig/rig.json --motion run/after/motion.json --out run/after/build --report run/after/build-report.json
build exit 0
$ npx rigc render --candidate run/after/build --animation run --fps 30 --geometry --folds --pass-through bottomwear:thigh_r,bottomwear:thigh_l --out run/after/render
render exit 0
grade exit 1
grade R2
NOTE  airborne spans: report feet.jumps, 20 span(s)
NOTE  rig leg length 485.0928 units (setup pose, leg_l0->foot_l, leg_r0->foot_r); hip width 84.0000
NOTE  sequence leg length 399.28 (95th percentile hip->ankle, mean of sides, the sequence's own units); the sequence carries no camera
PASS  gate            Gate: build green (52 assertions: 21 measured, 0 failed); 17/17 landings within tolerance (worst at 0.15 of its tolerance)
PASS  support-foot    Support foot: max |lower foot - floor| 0.0000 leg lengths at frame 110 over 60 grounded frames (floor 146.203 units) [bar <= 0.01]
FAIL  two-feet        Two feet: two-foot frames: none in the sequence; lifted frames (sequence ankles > 0.04 apart): 0 of 60 with the lifted foot within 0.01 of the support foot (lowest lift 0.0137 at frame 51) [bar 0]; median rig/sequence lift 0.145 [bar 0.85-1.15]
PASS  slide           Slide: max |support-foot move - closure - sequence ankle move x report scale 1.78104| 0.00003 leg lengths/frame (foot_l, frame 10->11) over 40 steps (travel: in-place; closure +1.05979 units/frame removed (report feet.closure drift -210.90 over 200 frames)) [bar <= 0.005]
PASS  floor           Floor: per-cycle floor spread 0.0000 leg lengths over 10 cycles [bar <= 0.01, the support-foot band: the table gives this row no number of its own]
PASS  jitter          Jitter: limbs 0.339x sequence (3.407 vs 10.060 deg/f^2, 9 bones) [bar <= 1.1], trunk+head 1.000x sequence (1.517 vs 1.516 deg/f^2, chest) [bar <= 1.1]; joint pairs from the map
FAIL  folds           Folds: 16 frame(s) with a folded triangle, most in slot 'bottomwear' (16 frames) [bar 0]
PASS  pass-through    Pass-through: bottomwear:thigh_r 0 of 200 frames; bottomwear:thigh_l 0 of 200 frames [bar 0]
FAIL  loop            Loop: cycle 1 vs cycle 10: max keyed-bone angle difference 34.6923 deg (sleeve_l1, cycle frame 1) [bar <= 1.0], max hip/foot_l/foot_r world position difference 0.0018 leg lengths (foot_l, cycle frame 0) [bar <= 0.01]
PASS  airborne        Airborne: airborne spans per cycle [2, 2, 2, 2, 2, 2, 2, 2, 2, 2] [bar 2 each]; 0 detected span(s) off the printed spans [(4, 9), (14, 19)] +/- 1 [bar 0]; lowest foot on an airborne frame 0.0513 leg lengths above the floor at frame 143 [bar > 0.01: above the support-foot band]
FAIL  hip-vertical    Hip vertical range: rig/sequence 1.460 (rig 0.1393, sequence 0.0954 leg lengths, median per-cycle width over 10 cycles) [bar 0.85-1.15]
FAIL  hip-horizontal  Hip horizontal range: rig/sequence 1.712 (rig 0.5636, sequence 0.3291 hip widths, median per-cycle width over 10 cycles) [bar 0.85-1.15]
FAIL  rebound         Rebound: median rig/sequence peak upward hip acceleration in the stance windows 1.929 over 19 windows [bar 0.7-1.43]
PASS  hip-tilt        Hip tilt: rig tilt range 14.390 deg = 1.000 of the sequence's 14.390 [bar >= 0.85], sign agrees (covariance +3.66e+03)
RESULT FAIL (8 pass, 6 fail, 0 skip of 14 rows)
$ python3 tools/grade.py --round R2 (final, grade3)
RESULT FAIL (8 pass, 6 fail, 0 skip of 14 rows)
finished: 2026-10-18T21:53:21Z
