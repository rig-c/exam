started: 2026-10-20T13:39:13Z
$ (wrote config.json; assemble --propose-plan; merged plan + extend_below_crop)

$ node_modules/.bin/rig-parts assemble --source tasks/03-correct/inputs/painting.png --full tasks/03-correct/inputs/layers/full --head tasks/03-correct/inputs/layers/head --config runs/2026-10-20-claude-sonnet-5-5-03-correct/config.json --out runs/2026-10-20-claude-sonnet-5-5-03-correct/work
  fringe pushed back: "legwear" 14 px, where the painting shows "shoes" 14 px
  fringe pushed back: "bottomwear" 393 px, where the painting shows "legwear" 393 px
  fringe pushed back: "topwear" 47 px, where the painting shows "bottomwear" 15 px, "hair_back" 11 px, "handwear_l" 11 px, "neck" 9 px, "hairpin" 1 px
  fringe pushed back: "handwear_r" 192 px, where the painting shows "bottomwear" 113 px, "topwear" 79 px
  fringe pushed back: "ear_l" 6 px, where the painting shows "hair_back" 6 px
  fringe pushed back: "face" 20 px, where the painting shows "neck" 19 px, "ear_r" 1 px
  fringe pushed back: "eyewhite_r" 6 px, where the painting shows "face" 6 px
  fringe pushed back: "eyewhite_l" 2 px, where the painting shows "face" 2 px
  fringe pushed back: "iris_r" 7 px, where the painting shows "face" 6 px, "eyewhite_r" 1 px
  fringe pushed back: "iris_l" 5 px, where the painting shows "eyewhite_l" 3 px, "face" 2 px
  fringe pushed back: "lash_l" 47 px, where the painting shows "face" 47 px
  fringe pushed back: "lash_r" 17 px, where the painting shows "face" 14 px, "eyewhite_r" 2 px, "iris_r" 1 px
  fringe pushed back: "brow_l" 6 px, where the painting shows "face" 6 px
  fringe pushed back: "brow_r" 8 px, where the painting shows "face" 8 px
  fringe pushed back: "hair_front" 109 px, where the painting shows "face" 42 px, "handwear_r" 34 px, "topwear" 31 px, "brow_r" 2 px
  pixels: opaque 310012 = visible 208962 + occluded 101050 (32.6%); taken from the painting 146975 (47.4%); visible but not projected 61967 (20.0%)
  ghost px removed: 1008 over 58 layer(s)
recomposite vs source: mean |d|=1.09, within 8: 97.9%, error px > 40: 6164, uncovered error px: 1726
uncovered holes (8-connected): 444, the largest 5 listed
  uncovered hole 1: 154 px at 321,1077 18x35 (between "shoes" 40 px, "legwear" 21 px)
  uncovered hole 2: 150 px at 353,296 32x24 (between "hair_back" 68 px, "hairpin" 27 px, "handwear_r" 15 px, "topwear" 3 px, "hair_front" 3 px)
  uncovered hole 3: 100 px at 401,1068 9x31 (between "legwear" 24 px, "shoes" 20 px)
  uncovered hole 4: 48 px at 493,518 8x23 (between "handwear_l" 28 px, "bottomwear" 14 px)
  uncovered hole 5: 37 px at 325,103 31x31 (between "hair_back" 63 px)
wrote runs/2026-10-20-claude-sonnet-5-5-03-correct/work/rig/parts.json, 22 PNG(s) in runs/2026-10-20-claude-sonnet-5-5-03-correct/work/rig/parts, runs/2026-10-20-claude-sonnet-5-5-03-correct/work/render/recomposite_rig.png, runs/2026-10-20-claude-sonnet-5-5-03-correct/work/render/recomposite_error_rig.png (uncovered error px red, covered error px blue, the painting grey)
[exit 0]

$ node_modules/.bin/rig-parts propose --parts runs/2026-10-20-claude-sonnet-5-5-03-correct/work/rig --source tasks/03-correct/inputs/painting.png --out runs/2026-10-20-claude-sonnet-5-5-03-correct/work
coverage lock1 [deforms]: checked, clean — read by off-art on mesh 'hair_front', squeeze with bang_r on mesh 'hair_front', squeeze with bang_c on mesh 'hair_front', squeeze with bang_l on mesh 'hair_front', squeeze with lock1_ on mesh 'hair_front'
coverage lock2 [deforms]: checked, clean — read by off-art on mesh 'hair_front', squeeze with bang_r on mesh 'hair_front', squeeze with bang_c on mesh 'hair_front', squeeze with bang_l on mesh 'hair_front', squeeze with lock1_ on mesh 'hair_front'
coverage lock3 [deforms]: checked, clean — read by off-art on mesh 'hair_front', squeeze with bang_r on mesh 'hair_front', squeeze with bang_c on mesh 'hair_front', squeeze with bang_l on mesh 'hair_front', squeeze with lock1_ on mesh 'hair_front'
coverage lock1_0 [deforms]: checked, clean — read by off-art on mesh 'hair_front', squeeze with bang_r on mesh 'hair_front', squeeze with bang_c on mesh 'hair_front', squeeze with bang_l on mesh 'hair_front', squeeze with lock on mesh 'hair_front'
coverage lock1_1 [deforms]: checked, clean — read by off-art on mesh 'hair_front', squeeze with bang_r on mesh 'hair_front', squeeze with bang_c on mesh 'hair_front', squeeze with bang_l on mesh 'hair_front', squeeze with lock on mesh 'hair_front'
coverage lock1_2 [deforms]: checked, clean — read by off-art on mesh 'hair_front', squeeze with bang_r on mesh 'hair_front', squeeze with bang_c on mesh 'hair_front', squeeze with bang_l on mesh 'hair_front', squeeze with lock on mesh 'hair_front'
coverage lock1_3 [deforms]: checked, clean — read by off-art on mesh 'hair_front', squeeze with bang_r on mesh 'hair_front', squeeze with bang_c on mesh 'hair_front', squeeze with bang_l on mesh 'hair_front', squeeze with lock on mesh 'hair_front'
coverage hairpin [deforms]: not checked — bound by the explicit [bone, from, to] segments meshes.hairpin.segments[0], meshes.hairpin.segments[1]: a segment is a line, not an origin, and the off-art check reads origins
coverage sleeve_r0 [deforms]: checked, clean — read by off-art on mesh 'handwear_r'
coverage sleeve_r1 [deforms]: checked, clean — read by off-art on mesh 'handwear_r'
coverage sleeve_r2 [deforms]: checked, clean — read by off-art on mesh 'handwear_r'
coverage sleeve_l0 [deforms]: checked, clean — read by off-art on mesh 'handwear_l'
coverage sleeve_l1 [deforms]: checked, clean — read by off-art on mesh 'handwear_l'
coverage sleeve_l2 [deforms]: checked, clean — read by off-art on mesh 'handwear_l'
coverage skirt_r0 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_c on mesh 'bottomwear', squeeze with skirt_l on mesh 'bottomwear'
coverage skirt_r1 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_c on mesh 'bottomwear', squeeze with skirt_l on mesh 'bottomwear'
coverage skirt_r2 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_c on mesh 'bottomwear', squeeze with skirt_l on mesh 'bottomwear'
coverage skirt_c0 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_r on mesh 'bottomwear', squeeze with skirt_l on mesh 'bottomwear'
coverage skirt_c1 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_r on mesh 'bottomwear', squeeze with skirt_l on mesh 'bottomwear'
coverage skirt_c2 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_r on mesh 'bottomwear', squeeze with skirt_l on mesh 'bottomwear'
coverage skirt_l0 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_r on mesh 'bottomwear', squeeze with skirt_c on mesh 'bottomwear'
coverage skirt_l1 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_r on mesh 'bottomwear', squeeze with skirt_c on mesh 'bottomwear'
coverage skirt_l2 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_r on mesh 'bottomwear', squeeze with skirt_c on mesh 'bottomwear'
coverage: 45 bone(s) — 35 checked and clean, 2 checked with a LINT line, 8 not checked; roles 0 target, 44 deforms, 1 control, 0 unclassified
wrote basis.json (45 bone record(s) by the basis of their origin: 0 joint, 38 mask, 6 ratio, 1 derived) under runs/2026-10-20-claude-sonnet-5-5-03-correct/work
[exit 0]
$ (pasted proposal bones/meshes/regions/motion; set motion hairback_l amps to [0.6, 1.4, 2.4])

$ node_modules/.bin/rig-parts propose --parts runs/2026-10-20-claude-sonnet-5-5-03-correct/work/rig --source tasks/03-correct/inputs/painting.png --out runs/2026-10-20-claude-sonnet-5-5-03-correct/work --from-config runs/2026-10-20-claude-sonnet-5-5-03-correct/config.json
coverage lock0 [deforms]: checked, clean — read by off-art on mesh 'hair_front', squeeze with bang_r on mesh 'hair_front', squeeze with bang_c on mesh 'hair_front', squeeze with bang_l on mesh 'hair_front', squeeze with lock1_ on mesh 'hair_front'
coverage lock1 [deforms]: checked, clean — read by off-art on mesh 'hair_front', squeeze with bang_r on mesh 'hair_front', squeeze with bang_c on mesh 'hair_front', squeeze with bang_l on mesh 'hair_front', squeeze with lock1_ on mesh 'hair_front'
coverage lock2 [deforms]: checked, clean — read by off-art on mesh 'hair_front', squeeze with bang_r on mesh 'hair_front', squeeze with bang_c on mesh 'hair_front', squeeze with bang_l on mesh 'hair_front', squeeze with lock1_ on mesh 'hair_front'
coverage lock3 [deforms]: checked, clean — read by off-art on mesh 'hair_front', squeeze with bang_r on mesh 'hair_front', squeeze with bang_c on mesh 'hair_front', squeeze with bang_l on mesh 'hair_front', squeeze with lock1_ on mesh 'hair_front'
coverage lock1_0 [deforms]: checked, clean — read by off-art on mesh 'hair_front', squeeze with bang_r on mesh 'hair_front', squeeze with bang_c on mesh 'hair_front', squeeze with bang_l on mesh 'hair_front', squeeze with lock on mesh 'hair_front'
coverage lock1_1 [deforms]: checked, clean — read by off-art on mesh 'hair_front', squeeze with bang_r on mesh 'hair_front', squeeze with bang_c on mesh 'hair_front', squeeze with bang_l on mesh 'hair_front', squeeze with lock on mesh 'hair_front'
coverage lock1_2 [deforms]: checked, clean — read by off-art on mesh 'hair_front', squeeze with bang_r on mesh 'hair_front', squeeze with bang_c on mesh 'hair_front', squeeze with bang_l on mesh 'hair_front', squeeze with lock on mesh 'hair_front'
coverage lock1_3 [deforms]: checked, clean — read by off-art on mesh 'hair_front', squeeze with bang_r on mesh 'hair_front', squeeze with bang_c on mesh 'hair_front', squeeze with bang_l on mesh 'hair_front', squeeze with lock on mesh 'hair_front'
coverage hairpin [deforms]: not checked — bound by the explicit [bone, from, to] segments meshes.hairpin.segments[0], meshes.hairpin.segments[1]: a segment is a line, not an origin, and the off-art check reads origins
coverage sleeve_r0 [deforms]: checked, clean — read by off-art on mesh 'handwear_r'
coverage sleeve_r1 [deforms]: checked, clean — read by off-art on mesh 'handwear_r'
coverage sleeve_r2 [deforms]: checked, clean — read by off-art on mesh 'handwear_r'
coverage sleeve_l0 [deforms]: checked, clean — read by off-art on mesh 'handwear_l'
coverage sleeve_l1 [deforms]: checked, clean — read by off-art on mesh 'handwear_l'
coverage sleeve_l2 [deforms]: checked, clean — read by off-art on mesh 'handwear_l'
coverage skirt_r0 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_c on mesh 'bottomwear', squeeze with skirt_l on mesh 'bottomwear'
coverage skirt_r1 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_c on mesh 'bottomwear', squeeze with skirt_l on mesh 'bottomwear'
coverage skirt_r2 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_c on mesh 'bottomwear', squeeze with skirt_l on mesh 'bottomwear'
coverage skirt_c0 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_r on mesh 'bottomwear', squeeze with skirt_l on mesh 'bottomwear'
coverage skirt_c1 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_r on mesh 'bottomwear', squeeze with skirt_l on mesh 'bottomwear'
coverage skirt_c2 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_r on mesh 'bottomwear', squeeze with skirt_l on mesh 'bottomwear'
coverage skirt_l0 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_r on mesh 'bottomwear', squeeze with skirt_c on mesh 'bottomwear'
coverage skirt_l1 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_r on mesh 'bottomwear', squeeze with skirt_c on mesh 'bottomwear'
coverage skirt_l2 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_r on mesh 'bottomwear', squeeze with skirt_c on mesh 'bottomwear'
coverage: 45 bone(s) — 37 checked and clean, 0 checked with a LINT line, 8 not checked; roles 0 target, 44 deforms, 1 control, 0 unclassified
[exit 0]

$ node_modules/.bin/rig-parts build --config runs/2026-10-20-claude-sonnet-5-5-03-correct/config.json --source tasks/03-correct/inputs/painting.png --full tasks/03-correct/inputs/layers/full --head tasks/03-correct/inputs/layers/head --out runs/2026-10-20-claude-sonnet-5-5-03-correct/out
[check]   ..    pages=22 regions=22 bones=84 slots=22 animations=1 version=4.3.13 regionAttachments=14 meshAttachments=8 physicsConstraints=0 rig=exam03_painting profile=spine-html
[check]   ..    here: 44 rule(s) on the model side over the document, 8 of the round trip's own restated over the emitted text; not run: A00_ROUNDTRIP_PARSE — spine-core's parse, which only the entry that links spine-core runs, on build and validate: installed, the same `rigc` once @esotericsoftware/spine-core is installed beside the package; from a source checkout, `bun cli.ts`
[check]   ..    pack: skeleton.png 517x1348, 22 region(s), 92.9% covered, padding 2, page edges free, shape polygon
[check]   ..    53 assertions: 26 measured (26 passed, 0 failed), 27 skipped, 0 not in profile "spine-html"
[check]   ..    pages=1 regions=22 bones=84 slots=22 animations=1 version=4.3.13 regionAttachments=14 meshAttachments=8 physicsConstraints=0 rig=exam03_painting profile=spine-html
[check]   ..    here: 44 rule(s) on the model side over the document, 8 of the round trip's own restated over the emitted text; not run: A00_ROUNDTRIP_PARSE — spine-core's parse, which only the entry that links spine-core runs, on build and validate: installed, the same `rigc` once @esotericsoftware/spine-core is installed beside the package; from a source checkout, `bun cli.ts`
[check]   pack: skeleton.png 517x1348, 22 region(s), 92.9% covered, padding 2, page edges free, shape polygon; page opaque 44.8% (alpha > 0) — spineboy yardstick 1024x256, 40 region(s), 45.8% opaque (alpha > 0), a reference and not a bar
[check]   loop: idle 41 frame(s) at 12 fps, f0000 vs f0040 (t = 3.333333333333333s): max |d| 0 (0 required)
[check]   seam: setup pose at 504x1216, scale 1.0098: mean |d| 0.148 (<= 1.0), 2 px over 40, 1.96 rig px (the count / s²; <= 50), 0 px over 80 (reported)
[check]   BREATH_VISIBLE: PASS — torso_parts topwear; torso_heat_mean 15.692; torso_floor 3.809; feet_parts shoes; feet_heat_max 0; feet_ceiling 0
[check]   BLINK_NO_HOLE: PASS — eye_parts eyewhite_r | eyewhite_l; closed group eyes scaley 0.12 from 2.37s to 2.454s; idle_frames_closed 29; box_px 5148; hole_px 0; hole_bar 0; patch_max 10; patch_px_over_40 0
[check]   CHAIN_LAG: PASS — chains neck > head_ctl: period 3.333s, phase 0.080 0.120, amp 0.350 0.900 | hairback_r0_ctl > hairback_r1_ctl > hairback_r2_ctl: period 3.333s, phase 0.200 0.280 0.360, amp 0.600 1.400 2.400 | hairback_l0_ctl > hairback_l1_ctl > hairback_l2_ctl: period 3.333s, phase 0.200 0.280 0.360, amp 0.600 1.400 2.400 | bang_r0_ctl > bang_r1_ctl: period 3.333s, phase 0.180 0.280, amp 1.000 2.200 | bang_c0_ctl > bang_c1_ctl: period 3.333s, phase 0.180 0.280, amp 0.800 1.760 | bang_l0_ctl > bang_l1_ctl: period 3.333s, phase 0.180 0.280, amp 1.000 2.200 | lock0_ctl > lock1_ctl > lock2_ctl > lock3_ctl: period 3.333s, phase 0.160 0.230 0.300 0.370, amp 0.800 1.600 2.600 3.600 | lock1_0_ctl > lock1_1_ctl > lock1_2_ctl > lock1_3_ctl: period 3.333s, phase 0.160 0.230 0.300 0.370, amp 0.800 1.600 2.600 3.600 | sleeve_r0_ctl > sleeve_r1_ctl > sleeve_r2_ctl: period 3.333s, phase 0.220 0.300 0.380, amp 0.200 0.600 1.200 | sleeve_l0_ctl > sleeve_l1_ctl > sleeve_l2_ctl: period 3.333s, phase 0.770 0.850 0.930, amp 0.200 0.600 1.200 | skirt_r0_ctl > skirt_r1_ctl > skirt_r2_ctl: period 3.333s, phase 0.300 0.370 0.440, amp 0.150 0.350 0.700 | skirt_c0_ctl > skirt_c1_ctl > skirt_c2_ctl: period 3.333s, phase 0.340 0.410 0.480, amp 0.150 0.350 0.700 | skirt_l0_ctl > skirt_l1_ctl > skirt_l2_ctl: period 3.333s, phase 0.380 0.450 0.520, amp 0.150 0.350 0.700; lags neck > head_ctl +0.040 | head_ctl > hairback_r0_ctl +0.080 | hairback_r0_ctl > hairback_r1_ctl +0.080 | hairback_r1_ctl > hairback_r2_ctl +0.080 | head_ctl > hairback_l0_ctl +0.080 | hairback_l0_ctl > hairback_l1_ctl +0.080 | hairback_l1_ctl > hairback_l2_ctl +0.080 | head_ctl > bang_r0_ctl +0.060 | bang_r0_ctl > bang_r1_ctl +0.100 | head_ctl > bang_c0_ctl +0.060 | bang_c0_ctl > bang_c1_ctl +0.100 | head_ctl > bang_l0_ctl +0.060 | bang_l0_ctl > bang_l1_ctl +0.100 | head_ctl > lock0_ctl +0.040 | lock0_ctl > lock1_ctl +0.070 | lock1_ctl > lock2_ctl +0.070 | lock2_ctl > lock3_ctl +0.070 | head_ctl > lock1_0_ctl +0.040 | lock1_0_ctl > lock1_1_ctl +0.070 | lock1_1_ctl > lock1_2_ctl +0.070 | lock1_2_ctl > lock1_3_ctl +0.070 | sleeve_r0_ctl > sleeve_r1_ctl +0.080 | sleeve_r1_ctl > sleeve_r2_ctl +0.080 | sleeve_l0_ctl > sleeve_l1_ctl +0.080 | sleeve_l1_ctl > sleeve_l2_ctl +0.080 | skirt_r0_ctl > skirt_r1_ctl +0.070 | skirt_r1_ctl > skirt_r2_ctl +0.070 | skirt_c0_ctl > skirt_c1_ctl +0.070 | skirt_c1_ctl > skirt_c2_ctl +0.070 | skirt_l0_ctl > skirt_l1_ctl +0.070 | skirt_l1_ctl > skirt_l2_ctl +0.070; min_step 0.04; step_floor 0.001; other_period none; unread none; first_violation null
[check]   TIP_OVER_ROOT: PASS — instrument geometry; parts part handwear_l, root_rig_px 1.219, tip_rig_px 5.883, ratio 4.828 | part bottomwear, root_rig_px 0.351, tip_rig_px 1.264, ratio 3.604 | part handwear_r, root_rig_px 1.212, tip_rig_px 5.114, ratio 4.22; ratio_floor 1.4725
[check]   STILL_REGIONS_DARK: PASS — face parts face, head_bone head, instrument geometry, still_slots slot face, max_rig_px 4.093e-13, rms_rig_px 1.146e-13, max_rig_px 4.093e-13, at null, rms_rig_px 1.146e-13, tolerance_rig_px 2.286e-11, crossing slot hair_front, depth_rig_px 1.223, area_rig_px2 77.068, frame 38, driven_slots none; feet parts shoes, instrument geometry, still_slots slot shoes, max_rig_px 0, rms_rig_px 0, max_rig_px 0, at null, rms_rig_px 0, tolerance_rig_px 2.814e-12, crossing none
[check]   TEXTURE_STRETCH: PASS — meshes 8; triangles 722; frames 41; severity 1.126; severity_ceiling 1.926544; worst slot hair_front, triangle 86, vertices 31 | 36 | 32, edge 36 | 32, frame 22, ratio 0.888; max_ratio 1.114; min_ratio 0.888; per_mesh slot hair_back, triangles 178, max_ratio 1.045, max_at triangle 136 (vertices 104 107 105), edge 107-105, idle frame 2, min_ratio 0.957, min_at triangle 136 (vertices 104 107 105), edge 107-105, idle frame 22, severity 1.045 | slot hairpin, triangles 14, max_ratio 1.008, max_at triangle 1 (vertices 0 11 12), edge 11-12, idle frame 10, min_ratio 1, min_at triangle 4 (vertices 2 4 3), edge 4-3, idle frame 30, severity 1.008 | slot handwear_l, triangles 78, max_ratio 1.025, max_at triangle 65 (vertices 58 28 27), edge 28-27, idle frame 7, min_ratio 0.983, min_at triangle 65 (vertices 58 28 27), edge 28-27, idle frame 27, severity 1.025 | slot neck, triangles 12, max_ratio 1.015, max_at triangle 10 (vertices 11 6 4), edge 6-4, idle frame 13, min_ratio 0.991, min_at triangle 10 (vertices 11 6 4), edge 6-4, idle frame 33, severity 1.015 | slot bottomwear, triangles 182, max_ratio 1.018, max_at triangle 162 (vertices 105 112 106), edge 105-112, idle frame 32, min_ratio 0.982, min_at triangle 162 (vertices 105 112 106), edge 105-112, idle frame 12, severity 1.019 | slot topwear, triangles 92, max_ratio 1.056, max_at triangle 84 (vertices 57 18 58), edge 18-58, idle frame 10, min_ratio 0.996, min_at triangle 52 (vertices 44 49 45), edge 49-45, idle frame 10, severity 1.056 | slot handwear_r, triangles 74, max_ratio 1.019, max_at triangle 65 (vertices 53 21 20), edge 21-20, idle frame 23, min_ratio 0.989, min_at triangle 65 (vertices 53 21 20), edge 21-20, idle frame 3, severity 1.019 | slot hair_front, triangles 92, max_ratio 1.114, max_at triangle 86 (vertices 31 36 32), edge 36-32, idle frame 2, min_ratio 0.888, min_at triangle 86 (vertices 31 36 32), edge 36-32, idle frame 22, severity 1.126
[check]   ANIMATIONS_DO_NOT_FOLD: PASS — 1 animation(s) read by rigc render --folds at 12 fps (idle): 0 folding mesh(es), 0 not declared in may_fold (<= 0)
[check]   RECOMPOSITE_HOLES: REPORTED — error_px 6164; uncovered_error_px 1726; hole_count 444; largest px 154, box 321,1077 18x35, borders shoes 40 px | legwear 21 px
[check]   gate: spine-html green (cli_core.ts, rigc's own validator)
[check]   wrote runs/2026-10-20-claude-sonnet-5-5-03-correct/out/check/gate_spine-html.txt, runs/2026-10-20-claude-sonnet-5-5-03-correct/out/check/contact.png, runs/2026-10-20-claude-sonnet-5-5-03-correct/out/check/motion_heat.png, runs/2026-10-20-claude-sonnet-5-5-03-correct/out/check/check.json, runs/2026-10-20-claude-sonnet-5-5-03-correct/out/check/build/, runs/2026-10-20-claude-sonnet-5-5-03-correct/out/check/idle_frames/
[check] check: PASS; 10 of 10 bar(s) measured, 0 skipped
build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from
  pack: skeleton.png 517x1348, 22 region(s), 92.9% covered, padding 2, page edges free, shape polygon; page opaque 44.8% (alpha > 0) — spineboy yardstick 1024x256, 40 region(s), 45.8% opaque (alpha > 0), a reference and not a bar
  runs/2026-10-20-claude-sonnet-5-5-03-correct/out/check/build/skeleton.json
  runs/2026-10-20-claude-sonnet-5-5-03-correct/out/check/build/skeleton.atlas
  runs/2026-10-20-claude-sonnet-5-5-03-correct/out/check/build/skeleton.png
[exit 0]

$ python3 grade.py runs/2026-10-20-claude-sonnet-5-5-03-correct
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 1726 against <= 3500"
PASS  does_not_fold: []
PASS  kept: "8 mesh(es) deformed against >= 8"
PASS  still_moves: "the back hair travels 45.881 rig px against the head over the idle, against >= 23"
clock: no started:/finished: lines in transcript.md
6 of 6 line(s); journal present, 0 entry(ies) whose line 4 begins WTF?:; log .grade/2026-10-20-claude-sonnet-5-5-03-correct/grade.log
[exit 0]
finished: 2026-10-20T13:48:23Z
