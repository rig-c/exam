started: 2026-10-20T13:52:01Z

```
$ ../../node_modules/.bin/rig-parts propose --parts ../2026-10-20-claude-opus-5-5-04-soft/out/rig --source inputs/painting.png --out work/fc --from-config config.json
  FAIL  PARTS_FILE_PRESENT: ../2026-10-20-claude-opus-5-5-04-soft/out/rig/parts.json — no such file
refused: 1 problem(s)
[exit 1]
```

```
$ ../../node_modules/.bin/rig-parts propose --parts ../2026-10-20-claude-opus-5-5-04-soft/out --source inputs/painting.png --out work/fc --from-config config.json
coverage skirt_c1 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_r on mesh 'bottomwear', squeeze with skirt_l on mesh 'bottomwear'
coverage skirt_c2 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_r on mesh 'bottomwear', squeeze with skirt_l on mesh 'bottomwear'
coverage skirt_l0 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_r on mesh 'bottomwear', squeeze with skirt_c on mesh 'bottomwear'
coverage skirt_l1 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_r on mesh 'bottomwear', squeeze with skirt_c on mesh 'bottomwear'
coverage skirt_l2 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_r on mesh 'bottomwear', squeeze with skirt_c on mesh 'bottomwear'
coverage shin_r [deforms]: not checked — named as a single bone by meshes.legwear.segments[1]: a single bone has no links, and the off-art check reads only the links <segment><digits> of a chain
coverage shin_l [deforms]: not checked — named as a single bone by meshes.legwear.segments[3]: a single bone has no links, and the off-art check reads only the links <segment><digits> of a chain
coverage: 43 bone(s) — 31 checked and clean, 0 checked with a LINT line, 12 not checked; roles 0 target, 42 deforms, 1 control, 0 unclassified
[exit 0]
```

```
$ ../../node_modules/.bin/rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out
[check]   BREATH_VISIBLE: PASS — torso_parts topwear; torso_heat_mean 16.447; torso_floor 3.809; feet_parts shoes; feet_heat_max 0; feet_ceiling 0
[check]   BLINK_NO_HOLE: PASS — eye_parts eyewhite_r | eyewhite_l; closed group eyes scaley 0.12 from 2.37s to 2.454s; idle_frames_closed 29; box_px 2937; hole_px 0; hole_bar 0; patch_max 8; patch_px_over_40 0
[check]   CHAIN_LAG: PASS — chains neck > head_ctl: period 3.333s, phase 0.080 0.120, amp 0.350 0.900 | bang_r0_ctl > bang_r1_ctl: period 3.333s, phase 0.180 0.280, amp 1.000 2.200 | bang_c0_ctl > bang_c1_ctl: period 3.333s, phase 0.180 0.280, amp 0.800 1.760 | bang_l0_ctl > bang_l1_ctl: period 3.333s, phase 0.180 0.280, amp 1.000 2.200 | lock0_ctl > lock1_ctl > lock2_ctl > lock3_ctl: period 3.333s, phase 0.160 0.230 0.300 0.370, amp 0.800 1.600 2.600 3.600 | lock1_0_ctl > lock1_1_ctl > lock1_2_ctl > lock1_3_ctl: period 3.333s, phase 0.160 0.230 0.300 0.370, amp 0.800 1.600 2.600 3.600 | sleeve_r0_ctl > sleeve_r1_ctl > sleeve_r2_ctl: period 3.333s, phase 0.220 0.300 0.380, amp 0.200 0.600 1.200 | sleeve_l0_ctl > sleeve_l1_ctl > sleeve_l2_ctl: period 3.333s, phase 0.770 0.850 0.930, amp 0.200 0.600 1.200 | skirt_r0_ctl > skirt_r1_ctl > skirt_r2_ctl: period 3.333s, phase 0.300 0.370 0.440, amp 0.150 0.350 0.700 | skirt_c0_ctl > skirt_c1_ctl > skirt_c2_ctl: period 3.333s, phase 0.340 0.410 0.480, amp 0.150 0.350 0.700 | skirt_l0_ctl > skirt_l1_ctl > skirt_l2_ctl: period 3.333s, phase 0.380 0.450 0.520, amp 0.150 0.350 0.700; lags neck > head_ctl +0.040 | head_ctl > bun_ctl +0.080 | head_ctl > bang_r0_ctl +0.060 | bang_r0_ctl > bang_r1_ctl +0.100 | head_ctl > bang_c0_ctl +0.060 | bang_c0_ctl > bang_c1_ctl +0.100 | head_ctl > bang_l0_ctl +0.060 | bang_l0_ctl > bang_l1_ctl +0.100 | head_ctl > lock0_ctl +0.040 | lock0_ctl > lock1_ctl +0.070 | lock1_ctl > lock2_ctl +0.070 | lock2_ctl > lock3_ctl +0.070 | head_ctl > lock1_0_ctl +0.040 | lock1_0_ctl > lock1_1_ctl +0.070 | lock1_1_ctl > lock1_2_ctl +0.070 | lock1_2_ctl > lock1_3_ctl +0.070 | sleeve_r0_ctl > sleeve_r1_ctl +0.080 | sleeve_r1_ctl > sleeve_r2_ctl +0.080 | sleeve_l0_ctl > sleeve_l1_ctl +0.080 | sleeve_l1_ctl > sleeve_l2_ctl +0.080 | skirt_r0_ctl > skirt_r1_ctl +0.070 | skirt_r1_ctl > skirt_r2_ctl +0.070 | skirt_c0_ctl > skirt_c1_ctl +0.070 | skirt_c1_ctl > skirt_c2_ctl +0.070 | skirt_l0_ctl > skirt_l1_ctl +0.070 | skirt_l1_ctl > skirt_l2_ctl +0.070; min_step 0.04; step_floor 0.001; other_period none; unread none; first_violation null
[check]   TIP_OVER_ROOT: PASS — instrument geometry; parts part handwear_l, root_rig_px 1.524, tip_rig_px 5.606, ratio 3.677 | part handwear_r, root_rig_px 1.432, tip_rig_px 5.365, ratio 3.747 | part bottomwear, root_rig_px 0.268, tip_rig_px 0.983, ratio 3.673; ratio_floor 1.4725
[check]   STILL_REGIONS_DARK: PASS — face parts face, head_bone head, instrument geometry, still_slots slot face, max_rig_px 3.882e-13, rms_rig_px 1.23e-13, max_rig_px 3.882e-13, at null, rms_rig_px 1.23e-13, tolerance_rig_px 2.286e-11, crossing slot hair_front, depth_rig_px 0.982, area_rig_px2 37.243, frame 18, driven_slots none; feet parts shoes, instrument geometry, still_slots slot shoes, max_rig_px 0, rms_rig_px 0, max_rig_px 0, at null, rms_rig_px 0, tolerance_rig_px 5.627e-12, crossing none
[check]   TEXTURE_STRETCH: PASS — meshes 9; triangles 919; frames 41; severity 1.115; severity_ceiling 1.926544; worst slot hair_front, triangle 68, vertices 56 | 30 | 28, edge 30 | 28, frame 8, ratio 1.115; max_ratio 1.115; min_ratio 0.901; per_mesh slot hair_back, triangles 72, max_ratio 1.02, max_at triangle 59 (vertices 47 19 18), edge 19-18, idle frame 16, min_ratio 0.988, min_at triangle 59 (vertices 47 19 18), edge 19-18, idle frame 36, severity 1.02 | slot handwear_l, triangles 78, max_ratio 1.016, max_at triangle 73 (vertices 24 23 22), edge 23-22, idle frame 8, min_ratio 0.99, min_at triangle 65 (vertices 16 57 17), edge 17-16, idle frame 7, severity 1.016 | slot handwear_r, triangles 78, max_ratio 1.017, max_at triangle 69 (vertices 17 19 18), edge 19-18, idle frame 7, min_ratio 0.991, min_at triangle 58 (vertices 57 15 14), edge 15-14, idle frame 25, severity 1.017 | slot legwear, triangles 236, max_ratio 1, max_at triangle 0 (vertices 0 82 1), edge 0-82, idle frame 0, min_ratio 1, min_at triangle 0 (vertices 0 82 1), edge 0-82, idle frame 0, severity 1 | slot neck, triangles 12, max_ratio 1.01, max_at triangle 8 (vertices 8 6 11), edge 8-6, idle frame 37, min_ratio 0.992, min_at triangle 4 (vertices 9 8 10), edge 9-8, idle frame 14, severity 1.01 | slot bottomwear, triangles 182, max_ratio 1.02, max_at triangle 101 (vertices 35 34 88), edge 35-34, idle frame 27, min_ratio 0.98, min_at triangle 101 (vertices 35 34 88), edge 35-34, idle frame 7, severity 1.02 | slot topwear, triangles 179, max_ratio 1.087, max_at triangle 131 (vertices 65 99 66), edge 99-66, idle frame 11, min_ratio 0.97, min_at triangle 98 (vertices 52 53 73), edge 73-52, idle frame 12, severity 1.087 | slot hairpin, triangles 8, max_ratio 1.008, max_at triangle 0 (vertices 0 8 1), edge 1-0, idle frame 10, min_ratio 1, min_at triangle 4 (vertices 7 6 8), edge 7-6, idle frame 30, severity 1.008 | slot hair_front, triangles 74, max_ratio 1.115, max_at triangle 68 (vertices 56 30 28), edge 30-28, idle frame 8, min_ratio 0.901, min_at triangle 60 (vertices 26 28 27), edge 26-28, idle frame 7, severity 1.115
[check]   ANIMATIONS_DO_NOT_FOLD: PASS — 3 animation(s) read by rigc render --folds at 12 fps, its 9 physics constraint(s) left out (idle, wave, hop): 0 folding mesh(es), 0 not declared in may_fold (<= 0)
[check]   RECOMPOSITE_HOLES: REPORTED — error_px 6275; uncovered_error_px 2059; hole_count 605; largest px 402, box 405,1073 39x25, borders shoes 58 px | legwear 43 px
[check]   gate: spine-html green (cli_core.ts, rigc's own validator)
[check]   wrote out/check/gate_spine-html.txt, out/check/contact.png, out/check/motion_heat.png, out/check/check.json, out/check/build/, out/check/idle_frames/
[check] check: PASS; 10 of 10 bar(s) measured, 0 skipped
build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from
  pack: skeleton.png 1001x721, 22 region(s), 93.8% covered, padding 2, page edges free, shape polygon; page opaque 39.9% (alpha > 0) — spineboy yardstick 1024x256, 40 region(s), 45.8% opaque (alpha > 0), a reference and not a bar
  out/check/build/skeleton.json
  out/check/build/skeleton.atlas
  out/check/build/skeleton.png
[exit 0]
```

```
$ ../../node_modules/.bin/rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out
[check]   STILL_REGIONS_DARK: PASS — face parts face, head_bone head, instrument geometry, still_slots slot face, max_rig_px 3.882e-13, rms_rig_px 1.23e-13, max_rig_px 3.882e-13, at null, rms_rig_px 1.23e-13, tolerance_rig_px 2.286e-11, crossing slot hair_front, depth_rig_px 0.982, area_rig_px2 37.243, frame 18, driven_slots none; feet parts shoes, instrument geometry, still_slots slot shoes, max_rig_px 0, rms_rig_px 0, max_rig_px 0, at null, rms_rig_px 0, tolerance_rig_px 5.627e-12, crossing none
[check]   TEXTURE_STRETCH: PASS — meshes 9; triangles 919; frames 41; severity 1.115; severity_ceiling 1.926544; worst slot hair_front, triangle 68, vertices 56 | 30 | 28, edge 30 | 28, frame 8, ratio 1.115; max_ratio 1.115; min_ratio 0.901; per_mesh slot hair_back, triangles 72, max_ratio 1.02, max_at triangle 59 (vertices 47 19 18), edge 19-18, idle frame 16, min_ratio 0.988, min_at triangle 59 (vertices 47 19 18), edge 19-18, idle frame 36, severity 1.02 | slot handwear_l, triangles 78, max_ratio 1.016, max_at triangle 73 (vertices 24 23 22), edge 23-22, idle frame 8, min_ratio 0.99, min_at triangle 65 (vertices 16 57 17), edge 17-16, idle frame 7, severity 1.016 | slot handwear_r, triangles 78, max_ratio 1.017, max_at triangle 69 (vertices 17 19 18), edge 19-18, idle frame 7, min_ratio 0.991, min_at triangle 58 (vertices 57 15 14), edge 15-14, idle frame 25, severity 1.017 | slot legwear, triangles 236, max_ratio 1, max_at triangle 0 (vertices 0 82 1), edge 0-82, idle frame 0, min_ratio 1, min_at triangle 0 (vertices 0 82 1), edge 0-82, idle frame 0, severity 1 | slot neck, triangles 12, max_ratio 1.01, max_at triangle 8 (vertices 8 6 11), edge 8-6, idle frame 37, min_ratio 0.992, min_at triangle 4 (vertices 9 8 10), edge 9-8, idle frame 14, severity 1.01 | slot bottomwear, triangles 182, max_ratio 1.02, max_at triangle 101 (vertices 35 34 88), edge 35-34, idle frame 27, min_ratio 0.98, min_at triangle 101 (vertices 35 34 88), edge 35-34, idle frame 7, severity 1.02 | slot topwear, triangles 179, max_ratio 1.087, max_at triangle 131 (vertices 65 99 66), edge 99-66, idle frame 11, min_ratio 0.97, min_at triangle 98 (vertices 52 53 73), edge 73-52, idle frame 12, severity 1.087 | slot hairpin, triangles 8, max_ratio 1.008, max_at triangle 0 (vertices 0 8 1), edge 1-0, idle frame 10, min_ratio 1, min_at triangle 4 (vertices 7 6 8), edge 7-6, idle frame 30, severity 1.008 | slot hair_front, triangles 74, max_ratio 1.115, max_at triangle 68 (vertices 56 30 28), edge 30-28, idle frame 8, min_ratio 0.901, min_at triangle 60 (vertices 26 28 27), edge 26-28, idle frame 7, severity 1.115
[check]   ANIMATIONS_DO_NOT_FOLD: PASS — 4 animation(s) read by rigc render --folds at 12 fps, its 9 physics constraint(s) left out (idle, wave, hop, dance): 0 folding mesh(es), 0 not declared in may_fold (<= 0)
[check]   RECOMPOSITE_HOLES: REPORTED — error_px 6275; uncovered_error_px 2059; hole_count 605; largest px 402, box 405,1073 39x25, borders shoes 58 px | legwear 43 px
[check]   gate: spine-html green (cli_core.ts, rigc's own validator)
[check]   wrote out/check/gate_spine-html.txt, out/check/contact.png, out/check/motion_heat.png, out/check/check.json, out/check/build/, out/check/idle_frames/
[check] check: PASS; 10 of 10 bar(s) measured, 0 skipped
build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from
  pack: skeleton.png 1001x721, 22 region(s), 93.8% covered, padding 2, page edges free, shape polygon; page opaque 39.9% (alpha > 0) — spineboy yardstick 1024x256, 40 region(s), 45.8% opaque (alpha > 0), a reference and not a bar
  out/check/build/skeleton.json
  out/check/build/skeleton.atlas
  out/check/build/skeleton.png
[exit 0]
```

```
$ ../../node_modules/.bin/rigc render --candidate out/check/build --animation dance --fps 12 --max 400 --folds --geometry --out work/dance
  ..    254x400px at 12 fps, 1 set(s) -> <clone>/runs/2026-10-20-claude-opus-5-5-05-dance/work/dance
  ..    dance            49 frame(s), 4.000s + contact.png + geometry.json + folds.json (0 of 9 mesh(es) fold) -> <clone>/runs/2026-10-20-claude-opus-5-5-05-dance/work/dance/dance
rigc: wrote <clone>/runs/2026-10-20-claude-opus-5-5-05-dance/work/dance/frames.json
[exit 0]
```

```
$ python3 grade.py runs/2026-10-20-claude-opus-5-5-05-dance
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 2059 against <= 4200"
PASS  does_not_fold: []
PASS  budget: "919 triangles against <= 1000"
PASS  dance_as_timed: "`dance` lasts 4 s against 4.0"
PASS  closes: "the last frame is 0.0 rig px from the first at its furthest vertex, against <= 0.5 (keys only, physics out)"
PASS  both_hands: "`handwear_l` travels 101.3 rig px and `handwear_r` 101.5 at their furthest vertex, measured from the middle of `topwear`, each against >= 100.0"
FAIL  whole_body: "the vertex of `topwear` that travels least travels 11.0 rig px, measured from the middle of `shoes`, against >= 15.0"
PASS  arms_bend_at_the_joints: "along its own length an upper arm or a forearm bends at most 6.9 degrees more than at rest, against <= 8.0"
PASS  on_her_feet: "the end of a leg (`legwear`) gets 0.0 rig px from where it meets `shoes`, against <= 6.0"
PASS  keeps_time: "1.0 of the variation in how fast she moves repeats every two beats, against >= 0.5"
FAIL  soft_in_the_dance: "`topwear` differs from the same build without its physics by 2.037 rig px at dance frame 16, against 3.0 to 15.0"
PASS  dance_does_not_fold: []
clock: no started:/finished: lines in transcript.md
12 of 14 line(s); journal present, 0 entry(ies) whose line 4 begins WTF?:; log .grade/2026-10-20-claude-opus-5-5-05-dance/grade.log
[exit 0]
```

```
$ ../../node_modules/.bin/rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out
[check]   RECOMPOSITE_HOLES: REPORTED — error_px 6275; uncovered_error_px 2059; hole_count 605; largest px 402, box 405,1073 39x25, borders shoes 58 px | legwear 43 px
[check]   gate: spine-html green (cli_core.ts, rigc's own validator)
[check]   wrote out/check/gate_spine-html.txt, out/check/contact.png, out/check/motion_heat.png, out/check/check.json, out/check/build/, out/check/idle_frames/
[check]   FAIL  CHECK_ANIMATIONS_DO_NOT_FOLD: animation "wave", mesh "handwear_l" (slot "handwear_l") — rigc render --folds at 12 fps, its 9 physics constraint(s) left out: "wave": mesh "handwear_l" (slot "handwear_l") folds on 15 frame(s) [5-19] at 12 fps; worst frame 5 (t=0.4167s): 1 of 78 triangle(s) [3] in world box x [100.39, 101.66] y [967.50, 986.47] (1.26 × 18.96), setup-pose area 480.50 units² = 1.32% of the mesh's; 1 triangle(s) fold on some frame [3]; no triangle turned over against the setup pose is required — a fold the art means is declared in the --requirements file's may_fold, { "slot": "handwear_l", "animation": "wave", "why": … }
[check] check: FAIL — 1 bar(s) not met; 10 of 10 bar(s) measured, 0 skipped
build: stopped at check; 1 bar(s) not met, so no loop was encoded and no artifact is reported
[exit 1]
```

```
$ ../../node_modules/.bin/rigc render --candidate out/check/build --animation dance --fps 12 --max 400 --folds --geometry --out work/dance
  ..    dance            49 frame(s), 4.000s + contact.png + geometry.json + folds.json (1 of 9 mesh(es) fold) -> <clone>/runs/2026-10-20-claude-opus-5-5-05-dance/work/dance/dance
  ..    folds    "dance": mesh "hair_front" (slot "hair_front") folds on 8 frame(s) [21-22, 27, 33-34, 39, 45-46] at 12 fps; worst frame 21 (t=1.7500s): 3 of 74 triangle(s) [61, 68, 69] in world box x [-22.12, 58.19] y [974.21, 1001.27] (80.30 × 27.05), setup-pose area 852.50 units² = 2.76% of the mesh's; 3 triangle(s) fold on some frame [61, 68, 69]
rigc: wrote <clone>/runs/2026-10-20-claude-opus-5-5-05-dance/work/dance/frames.json
[exit 0]
```

```
$ ../../node_modules/.bin/rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out
[check] check: PASS; 10 of 10 bar(s) measured, 0 skipped
build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from
  pack: skeleton.png 1001x721, 22 region(s), 93.8% covered, padding 2, page edges free, shape polygon; page opaque 39.9% (alpha > 0) — spineboy yardstick 1024x256, 40 region(s), 45.8% opaque (alpha > 0), a reference and not a bar
  out/check/build/skeleton.json
  out/check/build/skeleton.atlas
  out/check/build/skeleton.png
[exit 0]
```

```
$ ../../node_modules/.bin/rigc render --candidate out/check/build --animation dance --fps 12 --max 400 --folds --geometry --out work/dance
  ..    dance            49 frame(s), 4.000s + contact.png + geometry.json + folds.json (1 of 9 mesh(es) fold) -> <clone>/runs/2026-10-20-claude-opus-5-5-05-dance/work/dance/dance
  ..    folds    "dance": mesh "hair_front" (slot "hair_front") folds on 3 frame(s) [19, 31, 43] at 12 fps; worst frame 19 (t=1.5833s): 1 of 74 triangle(s) [61] in world box x [-13.58, 50.20] y [962.60, 986.78] (63.78 × 24.17), setup-pose area 480.50 units² = 1.56% of the mesh's; 1 triangle(s) fold on some frame [61]
rigc: wrote <clone>/runs/2026-10-20-claude-opus-5-5-05-dance/work/dance/frames.json
[exit 0]
```

```
$ ../../node_modules/.bin/rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out
[check] check: PASS; 10 of 10 bar(s) measured, 0 skipped
build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from
  pack: skeleton.png 1001x721, 22 region(s), 93.8% covered, padding 2, page edges free, shape polygon; page opaque 39.9% (alpha > 0) — spineboy yardstick 1024x256, 40 region(s), 45.8% opaque (alpha > 0), a reference and not a bar
  out/check/build/skeleton.json
  out/check/build/skeleton.atlas
  out/check/build/skeleton.png
[exit 0]
```

```
$ ../../node_modules/.bin/rigc render --candidate out/check/build --animation dance --fps 24 --max 400 --folds --geometry --out work/dance
  ..    254x400px at 24 fps, 1 set(s) -> <clone>/runs/2026-10-20-claude-opus-5-5-05-dance/work/dance
  ..    dance            97 frame(s), 4.000s + contact.png + geometry.json + folds.json (0 of 9 mesh(es) fold) -> <clone>/runs/2026-10-20-claude-opus-5-5-05-dance/work/dance/dance@24fps
rigc: wrote <clone>/runs/2026-10-20-claude-opus-5-5-05-dance/work/dance/frames.json
[exit 0]
```

```
$ python3 grade.py runs/2026-10-20-claude-opus-5-5-05-dance
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 2059 against <= 4200"
PASS  does_not_fold: []
PASS  budget: "919 triangles against <= 1000"
PASS  dance_as_timed: "`dance` lasts 4 s against 4.0"
PASS  closes: "the last frame is 0.0 rig px from the first at its furthest vertex, against <= 0.5 (keys only, physics out)"
PASS  both_hands: "`handwear_l` travels 158.8 rig px and `handwear_r` 160.0 at their furthest vertex, measured from the middle of `topwear`, each against >= 100.0"
PASS  whole_body: "the vertex of `topwear` that travels least travels 26.1 rig px, measured from the middle of `shoes`, against >= 15.0"
FAIL  arms_bend_at_the_joints: "along its own length an upper arm or a forearm bends at most 10.1 degrees more than at rest, against <= 8.0"
PASS  on_her_feet: "the end of a leg (`legwear`) gets 0.0 rig px from where it meets `shoes`, against <= 6.0"
PASS  keeps_time: "1.0 of the variation in how fast she moves repeats every two beats, against >= 0.5"
PASS  soft_in_the_dance: "`topwear` differs from the same build without its physics by 5.026 rig px at dance frame 18, against 3.0 to 15.0"
PASS  dance_does_not_fold: []
clock: no started:/finished: lines in transcript.md
13 of 14 line(s); journal present, 0 entry(ies) whose line 4 begins WTF?:; log .grade/2026-10-20-claude-opus-5-5-05-dance/grade.log
[exit 0]
```

```
$ ../../node_modules/.bin/rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out
  pack: skeleton.png 1001x721, 22 region(s), 93.8% covered, padding 2, page edges free, shape polygon; page opaque 39.9% (alpha > 0) — spineboy yardstick 1024x256, 40 region(s), 45.8% opaque (alpha > 0), a reference and not a bar
  out/check/build/skeleton.json
  out/check/build/skeleton.atlas
  out/check/build/skeleton.png
[exit 0]
```

```
$ ../../node_modules/.bin/rigc render --candidate out/check/build --animation dance --fps 24 --max 400 --folds --geometry --out work/dance
  ..    254x400px at 24 fps, 1 set(s) -> <clone>/runs/2026-10-20-claude-opus-5-5-05-dance/work/dance
  ..    dance            97 frame(s), 4.000s + contact.png + geometry.json + folds.json (0 of 9 mesh(es) fold) -> <clone>/runs/2026-10-20-claude-opus-5-5-05-dance/work/dance/dance@24fps
rigc: wrote <clone>/runs/2026-10-20-claude-opus-5-5-05-dance/work/dance/frames.json
[exit 0]
```
handwear_l upper n per band [5, 5, 5] rest -180.0 worst 0.95 at frame 21
handwear_l fore n per band [4, 4, 4] rest 135.0 worst 2.43 at frame 6
handwear_r upper n per band [10, 5, 5] rest 180.0 worst 0.59 at frame 8
handwear_r fore n per band [4, 3, 4] rest -180.0 worst 10.12 at frame 0

```
$ ../../node_modules/.bin/rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out
[rig]   FAIL  RIG_HEAT_ISLAND_SOURCE: config.meshes.handwear_r — the silhouette's 4-connected island of 2 px at rig (326, 268) holds no bound bone's source pixel, so the heat equation has no fixed temperature there and no answer; the island is dust — at most 4 px and at most 0.1 % of the part's 19539 art px, mesh-draft's dust line — which no bone is meant to sit on: declare config.meshes.handwear_r.stray at 2 or more (it is absent), which leaves an island that small out of the mesh and the silhouette heat solves over
[rig]   FAIL  RIG_HEAT_ISLAND_SOURCE: config.meshes.handwear_r — the silhouette's 4-connected island of 1 px at rig (323, 277) holds no bound bone's source pixel, so the heat equation has no fixed temperature there and no answer; the island is dust — at most 4 px and at most 0.1 % of the part's 19539 art px, mesh-draft's dust line — which no bone is meant to sit on: declare config.meshes.handwear_r.stray at 1 or more (it is absent), which leaves an island that small out of the mesh and the silhouette heat solves over
[rig] refused: 6 problem(s)
build: stopped at rig; no later stage ran
[exit 1]
```

```
$ ../../node_modules/.bin/rigc render --candidate out/check/build --animation dance --fps 24 --max 400 --folds --geometry --out work/dance
a cuts.json is { "<name>": { "rig": "...", "motion": "...", "out": "...",
                             "manifest": "..." (optional) } }, with every path
resolved relative to the cuts.json file itself.
[exit 2]
```
handwear_l upper n per band [5, 5, 5] rest -180.0 worst 0.95 at frame 21
handwear_l fore n per band [4, 4, 4] rest 135.0 worst 2.43 at frame 6
handwear_r upper n per band [10, 5, 5] rest 180.0 worst 0.59 at frame 8
handwear_r fore n per band [4, 3, 4] rest -180.0 worst 10.12 at frame 0

```
$ ../../node_modules/.bin/rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out
[check]   FAIL  CHECK_ANIMATIONS_DO_NOT_FOLD: animation "dance", mesh "handwear_l" (slot "handwear_l") — rigc render --folds at 12 fps, its 9 physics constraint(s) left out: "dance": mesh "handwear_l" (slot "handwear_l") folds on 12 frame(s) [5-7, 17-19, 29-31, 41-43] at 12 fps; worst frame 5 (t=0.4167s): 1 of 78 triangle(s) [40] in world box x [181.85, 216.53] y [856.27, 874.36] (34.67 × 18.09), setup-pose area 480.50 units² = 1.32% of the mesh's; 1 triangle(s) fold on some frame [40]; no triangle turned over against the setup pose is required — a fold the art means is declared in the --requirements file's may_fold, { "slot": "handwear_l", "animation": "dance", "why": … }
[check]   FAIL  CHECK_ANIMATIONS_DO_NOT_FOLD: animation "dance", mesh "handwear_r" (slot "handwear_r") — rigc render --folds at 12 fps, its 9 physics constraint(s) left out: "dance": mesh "handwear_r" (slot "handwear_r") folds on 13 frame(s) [0-1, 11-13, 23-25, 35-37, 47-48] at 12 fps; worst frame 0 (t=0.0000s): 1 of 78 triangle(s) [44] in world box x [-179.01, -146.75] y [848.50, 865.38] (32.26 × 16.87), setup-pose area 480.50 units² = 1.40% of the mesh's; 1 triangle(s) fold on some frame [44]; no triangle turned over against the setup pose is required — a fold the art means is declared in the --requirements file's may_fold, { "slot": "handwear_r", "animation": "dance", "why": … }
[check] check: FAIL — 3 bar(s) not met; 10 of 10 bar(s) measured, 0 skipped
build: stopped at check; 3 bar(s) not met, so no loop was encoded and no artifact is reported
[exit 1]
```

```
$ ../../node_modules/.bin/rigc render --candidate out/check/build --animation dance --fps 24 --max 400 --folds --geometry --out work/dance
  ..    folds    "dance": mesh "handwear_l" (slot "handwear_l") folds on 28 frame(s) [9-15, 33-39, 57-63, 81-87] at 24 fps; worst frame 9 (t=0.3750s): 1 of 78 triangle(s) [40] in world box x [178.48, 213.19] y [848.29, 866.99] (34.70 × 18.69), setup-pose area 480.50 units² = 1.32% of the mesh's; 1 triangle(s) fold on some frame [40]
  ..    folds    "dance": mesh "handwear_r" (slot "handwear_r") folds on 21 frame(s) [0-2, 22-26, 46-50, 70-74, 94-96] at 24 fps; worst frame 0 (t=0.0000s): 1 of 78 triangle(s) [44] in world box x [-179.01, -146.75] y [848.50, 865.38] (32.26 × 16.87), setup-pose area 480.50 units² = 1.40% of the mesh's; 1 triangle(s) fold on some frame [44]
rigc: wrote <clone>/runs/2026-10-20-claude-opus-5-5-05-dance/work/dance/frames.json
[exit 0]
```
handwear_l upper n per band [5, 5, 5] rest -180.0 worst 0.95 at frame 21
handwear_l fore n per band [4, 4, 4] rest 135.0 worst 2.43 at frame 6
handwear_r upper n per band [10, 5, 5] rest 180.0 worst 0.59 at frame 8
handwear_r fore n per band [4, 3, 4] rest -180.0 worst 10.12 at frame 0

```
$ ../../node_modules/.bin/rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out
  pack: skeleton.png 1001x721, 22 region(s), 93.8% covered, padding 2, page edges free, shape polygon; page opaque 39.9% (alpha > 0) — spineboy yardstick 1024x256, 40 region(s), 45.8% opaque (alpha > 0), a reference and not a bar
  out/check/build/skeleton.json
  out/check/build/skeleton.atlas
  out/check/build/skeleton.png
[exit 0]
```

```
$ ../../node_modules/.bin/rigc render --candidate out/check/build --animation dance --fps 24 --max 400 --folds --geometry --out work/dance
  ..    264x400px at 24 fps, 1 set(s) -> <clone>/runs/2026-10-20-claude-opus-5-5-05-dance/work/dance
  ..    dance            97 frame(s), 4.000s + contact.png + geometry.json + folds.json (0 of 9 mesh(es) fold) -> <clone>/runs/2026-10-20-claude-opus-5-5-05-dance/work/dance/dance@24fps
rigc: wrote <clone>/runs/2026-10-20-claude-opus-5-5-05-dance/work/dance/frames.json
[exit 0]
```
handwear_l upper n per band [5, 5, 5] rest -180.0 worst 2.37 at frame 84
handwear_l fore n per band [4, 4, 4] rest 135.0 worst 1.16 at frame 12
handwear_r upper n per band [10, 5, 5] rest 180.0 worst 0.38 at frame 9
handwear_r fore n per band [4, 3, 4] rest 180.0 worst 5.28 at frame 0

```
$ python3 grade.py runs/2026-10-20-claude-opus-5-5-05-dance
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 2059 against <= 4200"
PASS  does_not_fold: []
PASS  budget: "919 triangles against <= 1000"
PASS  dance_as_timed: "`dance` lasts 4 s against 4.0"
PASS  closes: "the last frame is 0.0 rig px from the first at its furthest vertex, against <= 0.5 (keys only, physics out)"
PASS  both_hands: "`handwear_l` travels 199.7 rig px and `handwear_r` 199.9 at their furthest vertex, measured from the middle of `topwear`, each against >= 100.0"
PASS  whole_body: "the vertex of `topwear` that travels least travels 26.1 rig px, measured from the middle of `shoes`, against >= 15.0"
PASS  arms_bend_at_the_joints: "along its own length an upper arm or a forearm bends at most 5.3 degrees more than at rest, against <= 8.0"
PASS  on_her_feet: "the end of a leg (`legwear`) gets 0.0 rig px from where it meets `shoes`, against <= 6.0"
PASS  keeps_time: "1.0 of the variation in how fast she moves repeats every two beats, against >= 0.5"
PASS  soft_in_the_dance: "`topwear` differs from the same build without its physics by 5.026 rig px at dance frame 18, against 3.0 to 15.0"
PASS  dance_does_not_fold: []
clock: no started:/finished: lines in transcript.md
14 of 14 line(s); journal present, 1 entry(ies) whose line 4 begins WTF?:; log .grade/2026-10-20-claude-opus-5-5-05-dance/grade.log
[exit 0]
```
finished: 2026-10-20T14:24:04Z
