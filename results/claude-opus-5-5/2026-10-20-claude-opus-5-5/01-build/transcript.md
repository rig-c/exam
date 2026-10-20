started: 2026-10-20T13:19:48Z

```
$ rig-parts assemble --propose-plan --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --config config.json
    "eyewear: in no plan row — full run: 70 px, empty: below the proposer's floor of 150 (PROPOSE_MIN_PX, src/assemble.ts); head run: 73 px, but the proposer takes eyewear from the full run only (it is not one of PROPOSE_HEAD_TAGS, src/assemble.ts) (px: run pixels of alpha above 8 after ghost clean-up)",
    "earwear: in no plan row — full run: 73 px, empty: below the proposer's floor of 150 (PROPOSE_MIN_PX, src/assemble.ts); head run: 69 px, empty: below the proposer's floor of 150 (PROPOSE_MIN_PX, src/assemble.ts) (px: run pixels of alpha above 8 after ghost clean-up)",
    "nose: in no plan row — the proposer never plans nose (the reference implementation's rule, which this port keeps); full run 114 px, head run 1309 px (px: run pixels of alpha above 8 after ghost clean-up); propose reads the head's pitch (where the nose sits between the eye midpoint and the mouth) only off a part tagged nose, and without one prints \"not read: no part tagged nose\"; to have it read, add [\"nose\", \"head\", \"nose\"] to assemble.plan after the row that takes \"face\" (the head run's layer holds the more of it) and run assemble and propose again"
  ]
}
[exit 0]  (22 plan rows; extend_below_crop hair_front, hair_back from full; notes: neckwear/tail/wings/objects/eyewear/earwear empty, nose never planned)
```

```
$ ../../node_modules/.bin/rig-parts assemble --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --config config.json --out work
  brow_r      head:eyebrow-r   34x8      @ 397, 108 op=    84 vis=     6 src=     0/     0 unproj=    6 drift=    0 (no core) merged=0 seam=0
  brow_l      head:eyebrow-l   31x19     @ 464, 115 op=    99 vis=    10 src=     0/     0 unproj=   10 drift=    0 (no core) merged=0 seam=0
  hair_front  head:front hair  138x252   @ 376,  33 op= 16006 vis= 16006 src= 11813/ 11824 unproj= 4204 drift=    1 (0.0% of core) merged=417 seam=29
  fringe pushed back: "bottomwear" 1 px, where the painting shows "legwear" 1 px
  fringe pushed back: "topwear" 61 px, where the painting shows "handwear_r" 27 px, "neck" 18 px, "handwear_l" 8 px, "bottomwear" 8 px
  fringe pushed back: "hairpin" 15 px, where the painting shows "topwear" 7 px, "neck" 5 px, "hair_back" 3 px
  fringe pushed back: "ear_l" 6 px, where the painting shows "hair_back" 6 px
  fringe pushed back: "face" 30 px, where the painting shows "ear_l" 18 px, "hair_back" 7 px, "neck" 5 px
  fringe pushed back: "eyewhite_r" 3 px, where the painting shows "face" 3 px
  fringe pushed back: "eyewhite_l" 4 px, where the painting shows "face" 4 px
  fringe pushed back: "iris_l" 4 px, where the painting shows "eyewhite_l" 3 px, "face" 1 px
  fringe pushed back: "iris_r" 3 px, where the painting shows "eyewhite_r" 2 px, "face" 1 px
  fringe pushed back: "lash_l" 14 px, where the painting shows "face" 10 px, "iris_l" 4 px
  fringe pushed back: "lash_r" 42 px, where the painting shows "face" 40 px, "eyewhite_r" 2 px
  fringe pushed back: "hair_front" 69 px, where the painting shows "topwear" 41 px, "face" 13 px, "hair_back" 9 px, "handwear_l" 5 px, "brow_l" 1 px
  pixels: opaque 285469 = visible 222651 + occluded 62818 (22.0%); taken from the painting 180998 (63.4%); visible but not projected 41664 (14.6%)
  ghost px removed: 1183 over 58 layer(s)
recomposite vs source: mean |d|=1.13, within 8: 97.8%, error px > 40: 6275, uncovered error px: 2059
uncovered holes (8-connected): 605, the largest 5 listed
  uncovered hole 1: 402 px at 405,1073 39x25 (between "shoes" 58 px, "legwear" 43 px)
  uncovered hole 2: 98 px at 354,33 69x77 (between "hair_back" 146 px)
  uncovered hole 3: 55 px at 487,190 6x47 (between "hair_front" 50 px, "topwear" 9 px, "hair_back" 4 px, "hairpin" 4 px)
  uncovered hole 4: 38 px at 376,191 1x38 (between "hair_front" 40 px)
  uncovered hole 5: 33 px at 364,388 7x9 (between "topwear" 8 px, "handwear_r" 5 px)
wrote work/rig/parts.json, 22 PNG(s) in work/rig/parts, work/render/recomposite_rig.png, work/render/recomposite_error_rig.png (uncovered error px red, covered error px blue, the painting grey)
[exit 0]
```

```
$ ../../node_modules/.bin/rig-parts propose --parts work/rig --source inputs/painting.png --out work
coverage neck [control]: not checked — its role is control (binds nothing; keyed by motion.tracks[3]): it binds nothing, so there is no art to hold it to, and a control may sit off the art by design
coverage head [deforms]: not checked — bound by the explicit [bone, from, to] segments meshes.hair_back.segments[0], meshes.hair_front.segments[0], meshes.neck.segments[1]: a segment is a line, not an origin, and the off-art check reads origins; bound rigidly by regions.ear_l, regions.ear_r, regions.face: no check reads a region's bone
coverage eye_r [deforms]: not checked — bound rigidly by regions.eyewhite_r, regions.iris_r, regions.lash_r: no check reads a region's bone
coverage eye_l [deforms]: not checked — bound rigidly by regions.eyewhite_l, regions.iris_l, regions.lash_l: no check reads a region's bone
coverage brow_r [deforms]: not checked — bound rigidly by regions.brow_r: no check reads a region's bone
coverage brow_l [deforms]: not checked — bound rigidly by regions.brow_l: no check reads a region's bone
coverage mouth [deforms]: not checked — bound rigidly by regions.mouth: no check reads a region's bone
coverage bun [deforms]: not checked — named as a single bone by meshes.hair_back.segments[1]: a single bone has no links, and the off-art check reads only the links <segment><digits> of a chain
coverage bang_r0 [deforms]: checked, clean — read by off-art on mesh 'hair_front', off-lock on mesh 'hair_front', squeeze with bang_c on mesh 'hair_front', squeeze with bang_l on mesh 'hair_front', squeeze with lock on mesh 'hair_front', squeeze with lock1_ on mesh 'hair_front'
coverage bang_r1 [deforms]: checked, clean — read by off-art on mesh 'hair_front', off-lock on mesh 'hair_front', squeeze with bang_c on mesh 'hair_front', squeeze with bang_l on mesh 'hair_front', squeeze with lock on mesh 'hair_front', squeeze with lock1_ on mesh 'hair_front'
coverage bang_c0 [deforms]: checked, clean — read by off-art on mesh 'hair_front', off-lock on mesh 'hair_front', squeeze with bang_r on mesh 'hair_front', squeeze with bang_l on mesh 'hair_front', squeeze with lock on mesh 'hair_front', squeeze with lock1_ on mesh 'hair_front'
coverage bang_c1 [deforms]: checked, clean — read by off-art on mesh 'hair_front', off-lock on mesh 'hair_front', squeeze with bang_r on mesh 'hair_front', squeeze with bang_l on mesh 'hair_front', squeeze with lock on mesh 'hair_front', squeeze with lock1_ on mesh 'hair_front'
coverage bang_l0 [deforms]: checked, clean — read by off-art on mesh 'hair_front', off-lock on mesh 'hair_front', squeeze with bang_r on mesh 'hair_front', squeeze with bang_c on mesh 'hair_front', squeeze with lock on mesh 'hair_front', squeeze with lock1_ on mesh 'hair_front'
coverage bang_l1 [deforms]: checked, clean — read by off-art on mesh 'hair_front', off-lock on mesh 'hair_front', squeeze with bang_r on mesh 'hair_front', squeeze with bang_c on mesh 'hair_front', squeeze with lock on mesh 'hair_front', squeeze with lock1_ on mesh 'hair_front'
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
coverage: 40 bone(s) — 31 checked and clean, 0 checked with a LINT line, 9 not checked; roles 0 target, 39 deforms, 1 control, 0 unclassified
wrote basis.json (40 bone record(s) by the basis of their origin: 0 joint, 32 mask, 7 ratio, 1 derived) under work
[exit 0]
```

```
$ ../../node_modules/.bin/rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out
[check]   ..    pages=22 regions=22 bones=74 slots=22 animations=1 version=4.3.13 regionAttachments=14 meshAttachments=8 physicsConstraints=0 rig=exam-01-build_painting profile=spine-html
[check]   ..    here: 44 rule(s) on the model side over the document, 8 of the round trip's own restated over the emitted text; not run: A00_ROUNDTRIP_PARSE — spine-core's parse, which only the entry that links spine-core runs, on build and validate: installed, the same `rigc` once @esotericsoftware/spine-core is installed beside the package; from a source checkout, `bun cli.ts`
[check]   ..    pack: skeleton.png 382x1962, 22 region(s), 90.3% covered, padding 2, page edges free, shape polygon
[check]   ..    53 assertions: 26 measured (26 passed, 0 failed), 27 skipped, 0 not in profile "spine-html"
[check]   ..    pages=1 regions=22 bones=74 slots=22 animations=1 version=4.3.13 regionAttachments=14 meshAttachments=8 physicsConstraints=0 rig=exam-01-build_painting profile=spine-html
[check]   ..    here: 44 rule(s) on the model side over the document, 8 of the round trip's own restated over the emitted text; not run: A00_ROUNDTRIP_PARSE — spine-core's parse, which only the entry that links spine-core runs, on build and validate: installed, the same `rigc` once @esotericsoftware/spine-core is installed beside the package; from a source checkout, `bun cli.ts`
[check]   pack: skeleton.png 382x1962, 22 region(s), 90.3% covered, padding 2, page edges free, shape polygon; page opaque 38.4% (alpha > 0) — spineboy yardstick 1024x256, 40 region(s), 45.8% opaque (alpha > 0), a reference and not a bar
[check]   loop: idle 41 frame(s) at 12 fps, f0000 vs f0040 (t = 3.333333333333333s): max |d| 0 (0 required)
[check]   seam: setup pose at 601x1216, scale 0.9640: mean |d| 0.117 (<= 1.0), 0 px over 40, 0.00 rig px (the count / s²; <= 50), 0 px over 80 (reported)
[check]   BREATH_VISIBLE: PASS — torso_parts topwear; torso_heat_mean 16.171; torso_floor 3.809; feet_parts shoes; feet_heat_max 0; feet_ceiling 0
[check]   BLINK_NO_HOLE: PASS — eye_parts eyewhite_r | eyewhite_l; closed group eyes scaley 0.12 from 2.37s to 2.454s; idle_frames_closed 29; box_px 2937; hole_px 0; hole_bar 0; patch_max 8; patch_px_over_40 0
[check]   CHAIN_LAG: PASS — chains neck > head_ctl: period 3.333s, phase 0.080 0.120, amp 0.350 0.900 | bang_r0_ctl > bang_r1_ctl: period 3.333s, phase 0.180 0.280, amp 1.000 2.200 | bang_c0_ctl > bang_c1_ctl: period 3.333s, phase 0.180 0.280, amp 0.800 1.760 | bang_l0_ctl > bang_l1_ctl: period 3.333s, phase 0.180 0.280, amp 1.000 2.200 | lock0_ctl > lock1_ctl > lock2_ctl > lock3_ctl: period 3.333s, phase 0.160 0.230 0.300 0.370, amp 0.800 1.600 2.600 3.600 | lock1_0_ctl > lock1_1_ctl > lock1_2_ctl > lock1_3_ctl: period 3.333s, phase 0.160 0.230 0.300 0.370, amp 0.800 1.600 2.600 3.600 | sleeve_r0_ctl > sleeve_r1_ctl > sleeve_r2_ctl: period 3.333s, phase 0.220 0.300 0.380, amp 0.200 0.600 1.200 | sleeve_l0_ctl > sleeve_l1_ctl > sleeve_l2_ctl: period 3.333s, phase 0.770 0.850 0.930, amp 0.200 0.600 1.200 | skirt_r0_ctl > skirt_r1_ctl > skirt_r2_ctl: period 3.333s, phase 0.300 0.370 0.440, amp 0.150 0.350 0.700 | skirt_c0_ctl > skirt_c1_ctl > skirt_c2_ctl: period 3.333s, phase 0.340 0.410 0.480, amp 0.150 0.350 0.700 | skirt_l0_ctl > skirt_l1_ctl > skirt_l2_ctl: period 3.333s, phase 0.380 0.450 0.520, amp 0.150 0.350 0.700; lags neck > head_ctl +0.040 | head_ctl > bun_ctl +0.080 | head_ctl > bang_r0_ctl +0.060 | bang_r0_ctl > bang_r1_ctl +0.100 | head_ctl > bang_c0_ctl +0.060 | bang_c0_ctl > bang_c1_ctl +0.100 | head_ctl > bang_l0_ctl +0.060 | bang_l0_ctl > bang_l1_ctl +0.100 | head_ctl > lock0_ctl +0.040 | lock0_ctl > lock1_ctl +0.070 | lock1_ctl > lock2_ctl +0.070 | lock2_ctl > lock3_ctl +0.070 | head_ctl > lock1_0_ctl +0.040 | lock1_0_ctl > lock1_1_ctl +0.070 | lock1_1_ctl > lock1_2_ctl +0.070 | lock1_2_ctl > lock1_3_ctl +0.070 | sleeve_r0_ctl > sleeve_r1_ctl +0.080 | sleeve_r1_ctl > sleeve_r2_ctl +0.080 | sleeve_l0_ctl > sleeve_l1_ctl +0.080 | sleeve_l1_ctl > sleeve_l2_ctl +0.080 | skirt_r0_ctl > skirt_r1_ctl +0.070 | skirt_r1_ctl > skirt_r2_ctl +0.070 | skirt_c0_ctl > skirt_c1_ctl +0.070 | skirt_c1_ctl > skirt_c2_ctl +0.070 | skirt_l0_ctl > skirt_l1_ctl +0.070 | skirt_l1_ctl > skirt_l2_ctl +0.070; min_step 0.04; step_floor 0.001; other_period none; unread none; first_violation null
[check]   TIP_OVER_ROOT: PASS — instrument geometry; parts part handwear_l, root_rig_px 1.404, tip_rig_px 7.052, ratio 5.024 | part handwear_r, root_rig_px 1.36, tip_rig_px 6.914, ratio 5.085 | part bottomwear, root_rig_px 0.268, tip_rig_px 0.983, ratio 3.673; ratio_floor 1.4725
[check]   STILL_REGIONS_DARK: PASS — face parts face, head_bone head, instrument geometry, still_slots slot face, max_rig_px 3.882e-13, rms_rig_px 1.23e-13, max_rig_px 3.882e-13, at null, rms_rig_px 1.23e-13, tolerance_rig_px 2.286e-11, crossing slot hair_front, depth_rig_px 1.14, area_rig_px2 40.775, frame 18, driven_slots none; feet parts shoes, instrument geometry, still_slots slot shoes, max_rig_px 0, rms_rig_px 0, max_rig_px 0, at null, rms_rig_px 0, tolerance_rig_px 5.627e-12, crossing none
[check]   TEXTURE_STRETCH: PASS — meshes 8; triangles 590; frames 41; severity 1.084; severity_ceiling 1.926544; worst slot hair_front, triangle 68, vertices 56 | 30 | 28, edge 30 | 28, frame 3, ratio 1.084; max_ratio 1.084; min_ratio 0.924; per_mesh slot hair_back, triangles 72, max_ratio 1.02, max_at triangle 59 (vertices 47 19 18), edge 19-18, idle frame 16, min_ratio 0.988, min_at triangle 59 (vertices 47 19 18), edge 19-18, idle frame 36, severity 1.02 | slot handwear_l, triangles 78, max_ratio 1.022, max_at triangle 61 (vertices 56 26 25), edge 26-25, idle frame 7, min_ratio 0.986, min_at triangle 61 (vertices 56 26 25), edge 26-25, idle frame 27, severity 1.022 | slot handwear_r, triangles 78, max_ratio 1.022, max_at triangle 69 (vertices 17 19 18), edge 19-18, idle frame 6, min_ratio 0.986, min_at triangle 69 (vertices 17 19 18), edge 19-18, idle frame 26, severity 1.022 | slot neck, triangles 12, max_ratio 1.01, max_at triangle 8 (vertices 8 6 11), edge 8-6, idle frame 37, min_ratio 0.992, min_at triangle 4 (vertices 9 8 10), edge 9-8, idle frame 14, severity 1.01 | slot bottomwear, triangles 182, max_ratio 1.02, max_at triangle 101 (vertices 35 34 88), edge 35-34, idle frame 27, min_ratio 0.98, min_at triangle 101 (vertices 35 34 88), edge 35-34, idle frame 7, severity 1.02 | slot topwear, triangles 86, max_ratio 1.078, max_at triangle 72 (vertices 52 57 53), edge 57-53, idle frame 10, min_ratio 0.993, min_at triangle 48 (vertices 42 48 43), edge 42-48, idle frame 10, severity 1.078 | slot hairpin, triangles 8, max_ratio 1.008, max_at triangle 0 (vertices 0 8 1), edge 1-0, idle frame 10, min_ratio 1, min_at triangle 4 (vertices 7 6 8), edge 7-6, idle frame 30, severity 1.008 | slot hair_front, triangles 74, max_ratio 1.084, max_at triangle 68 (vertices 56 30 28), edge 30-28, idle frame 3, min_ratio 0.924, min_at triangle 68 (vertices 56 30 28), edge 30-28, idle frame 23, severity 1.084
[check]   ANIMATIONS_DO_NOT_FOLD: PASS — 1 animation(s) read by rigc render --folds at 12 fps (idle): 0 folding mesh(es), 0 not declared in may_fold (<= 0)
[check]   RECOMPOSITE_HOLES: REPORTED — error_px 6275; uncovered_error_px 2059; hole_count 605; largest px 402, box 405,1073 39x25, borders shoes 58 px | legwear 43 px
[check]   gate: spine-html green (cli_core.ts, rigc's own validator)
[check]   wrote out/check/gate_spine-html.txt, out/check/contact.png, out/check/motion_heat.png, out/check/check.json, out/check/build/, out/check/idle_frames/
[check] check: PASS; 10 of 10 bar(s) measured, 0 skipped
build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from
  pack: skeleton.png 382x1962, 22 region(s), 90.3% covered, padding 2, page edges free, shape polygon; page opaque 38.4% (alpha > 0) — spineboy yardstick 1024x256, 40 region(s), 45.8% opaque (alpha > 0), a reference and not a bar
  out/check/build/skeleton.json
  out/check/build/skeleton.atlas
  out/check/build/skeleton.png
[exit 0]
```

```
$ python3 grade.py runs/2026-10-20-claude-opus-5-5-01-build
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 2059 against <= 4200"
PASS  does_not_fold: []
clock: no started:/finished: lines in transcript.md
4 of 4 line(s); journal present, 0 entry(ies) whose line 4 begins WTF?:; log .grade/2026-10-20-claude-opus-5-5-01-build/grade.log
[exit 0]
```
finished: 2026-10-20T13:25:09Z
