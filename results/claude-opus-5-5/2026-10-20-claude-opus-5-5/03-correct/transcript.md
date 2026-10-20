started: 2026-10-20T13:32:28Z

```
$ rig-parts assemble --propose-plan --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --config config.json > plan.out
[exit 0]  22 rows; extend_below_crop hair_front, hair_back; note: headwear head run 5 rig px < 0.8 x full run 2146 -> full-run layer
```

```
$ ../../node_modules/.bin/rig-parts assemble --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --config config.json --out work
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
wrote work/rig/parts.json, 22 PNG(s) in work/rig/parts, work/render/recomposite_rig.png, work/render/recomposite_error_rig.png (uncovered error px red, covered error px blue, the painting grey)
[exit 0]
```

```
$ ../../node_modules/.bin/rig-parts propose --parts work/rig --source inputs/painting.png --out work
wrote proposal.json (22 bone entries, 8 meshes) and render/landmarks.png (+_head) under work
note: head frame: the bar runs through eye_r [374.0, 232.0] and eye_l [439.0, 207.0], the eye bones' origins, 69.642 px; roll 21.038 degrees (Spine's, counter-clockwise) — the line the rig turns the face bones to and declares as invariants.axes; eye midpoint [406.5, 219.5]
note: head pitch: the nose sits — (not read: no part tagged nose) of the way from the eye midpoint to the mouth (frontal 0.474..0.630); the stem, eye midpoint -> mouth, is 0.592 of the bar (frontal 0.510..0.675); frontal ranges read on demo, scarf, the rig-c/trailer character; the turn is not reported (src/propose.ts FRONTAL_REFERENCE says why)
note: lash_r (head:eyelash-r) reaches 9 px above eyewhite_r's top, 26 % of its 35 px height (noted above 35 %) and is 1.30x the height of lash_l, 27 px (noted above 1.20x): the blink squashes whatever is painted there, a crease included — no row between its top and the lid is clear across its width, so it is not split; if a crease is painted in, clear a row between it and the lash line and set motion.blink.still by hand
note: breath: chest translatey 5.02 px peak to peak (amp 2.51, base 2.51) = 2.5 % of the torso's length, 201.1 px (neck [406, 308] -> hip [412, 509]), once per 40-frame idle at 12 fps
note: hair_front (head:front hair): bang_r, bang_c, bang_l are a template, not its locks — columns at 0.25, 0.5 and 0.75 of the face box's width, along the head's down axis (the eye line's perpendicular, roll 21.038 degrees), each rooted on the part's art; the opaque shape does not separate the locks painted inside one mass of hair, so a lock that runs elsewhere is not followed — move the chains onto the locks
note: handwear is two blobs: one sleeve chain per mesh, chest only at the shoulder
note: topwear ends at y=518 (hip 509): no robe chains -- add a sash chain by hand if one hangs
note: bottomwear (full:bottomwear): its art starts 77.8 px below chest's origin, so it hangs from the waist — its mesh takes the hip line and its skirt chains, no chest segment, and the breath does not carry its root
note: legwear (full:legwear): no rule -> region on hip
note: mesh spacing: grid 30 = round(H / 37), H 1107 rig px the height of every part's box together (rows 94 to 1201), in place of a tenth of each part's short side (hair_back 21 -> 30, hair_front 16 -> 30, hairpin 6 -> 30, neck 5 -> 30, handwear_r 14 -> 30, handwear_l 17 -> 30, topwear 16 -> 30; kept, already as coarse: bottomwear 32); r is the part's own. Calibrated on three figures of similar size (H 1106-1185 rig px, issue #265 Stage A), where every check bar passed at this divisor and the idle moved by up to 1.427 rig px against the finer lattice — no bar reads that. propose --grid-rule part drafts the part's own spacing
LINT hairback_r and hairback_l on mesh 'hair_back' squeeze it: swung together, every other bone held, edge 37-117 of triangle 167 closes to 0.064 times its rest length at idle frame 22 (max(ratio, 1/ratio) 15.572; <= 1.926544 is required, check's TEXTURE_STRETCH bar) — vertex 37 rides hairback_r2 0.91971, vertex 117 rides hairback_l2 0.90416; alone, hairback_r reads 1.880 and hairback_l 1.883. Their tips are 39.0 px apart and their amplitudes are opposed (hairback_r [0.6, 1.4, 2.4], hairback_l [-0.6, -1.4, -2.4]), so their tips swing towards each other and apart: give both the same sign (then 1.046), or drop one chain
1 LINT line(s) over 8 mesh(es) and the hip
coverage hip [deforms]: checked, clean — read by hip-not-below-chest, hip-too-high
coverage chest [deforms]: checked, clean — read by hip-not-below-chest
coverage neck [control]: not checked — its role is control (binds nothing; keyed by motion.tracks[3]): it binds nothing, so there is no art to hold it to, and a control may sit off the art by design
coverage head [deforms]: not checked — bound by the explicit [bone, from, to] segments meshes.hair_back.segments[0], meshes.hair_front.segments[0], meshes.neck.segments[1]: a segment is a line, not an origin, and the off-art check reads origins; bound rigidly by regions.ear_r, regions.ear_l, regions.face: no check reads a region's bone
coverage eye_r [deforms]: not checked — bound rigidly by regions.eyewhite_r, regions.iris_r, regions.lash_r: no check reads a region's bone
coverage eye_l [deforms]: not checked — bound rigidly by regions.eyewhite_l, regions.iris_l, regions.lash_l: no check reads a region's bone
coverage brow_r [deforms]: not checked — bound rigidly by regions.brow_r: no check reads a region's bone
coverage brow_l [deforms]: not checked — bound rigidly by regions.brow_l: no check reads a region's bone
coverage mouth [deforms]: not checked — bound rigidly by regions.mouth: no check reads a region's bone
coverage hairback_r0 [deforms]: checked, clean — read by off-art on mesh 'hair_back', squeeze with hairback_l on mesh 'hair_back'
coverage hairback_r1 [deforms]: checked, clean — read by off-art on mesh 'hair_back', squeeze with hairback_l on mesh 'hair_back'
coverage hairback_r2 [deforms]: checked, LINT — read by off-art on mesh 'hair_back', squeeze with hairback_l on mesh 'hair_back'; named by 1 LINT line(s)
coverage hairback_l0 [deforms]: checked, clean — read by off-art on mesh 'hair_back', squeeze with hairback_r on mesh 'hair_back'
coverage hairback_l1 [deforms]: checked, clean — read by off-art on mesh 'hair_back', squeeze with hairback_r on mesh 'hair_back'
coverage hairback_l2 [deforms]: checked, LINT — read by off-art on mesh 'hair_back', squeeze with hairback_r on mesh 'hair_back'; named by 1 LINT line(s)
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
coverage: 45 bone(s) — 35 checked and clean, 2 checked with a LINT line, 8 not checked; roles 0 target, 44 deforms, 1 control, 0 unclassified
wrote basis.json (45 bone record(s) by the basis of their origin: 0 joint, 38 mask, 6 ratio, 1 derived) under work
[exit 0]
```

```
$ ../../node_modules/.bin/rig-parts propose --parts work/rig --source inputs/painting.png --out work/fc --from-config config.json
coverage skirt_c1 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_r on mesh 'bottomwear', squeeze with skirt_l on mesh 'bottomwear'
coverage skirt_c2 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_r on mesh 'bottomwear', squeeze with skirt_l on mesh 'bottomwear'
coverage skirt_l0 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_r on mesh 'bottomwear', squeeze with skirt_c on mesh 'bottomwear'
coverage skirt_l1 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_r on mesh 'bottomwear', squeeze with skirt_c on mesh 'bottomwear'
coverage skirt_l2 [deforms]: checked, clean — read by off-art on mesh 'bottomwear', squeeze with skirt_r on mesh 'bottomwear', squeeze with skirt_c on mesh 'bottomwear'
coverage: 45 bone(s) — 37 checked and clean, 0 checked with a LINT line, 8 not checked; roles 0 target, 44 deforms, 1 control, 0 unclassified
[exit 0]
```

```
$ ../../node_modules/.bin/rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out
[check]   CHAIN_LAG: PASS — chains neck > head_ctl: period 3.333s, phase 0.080 0.120, amp 0.350 0.900 | hairback_r0_ctl > hairback_r1_ctl > hairback_r2_ctl: period 3.333s, phase 0.200 0.280 0.360, amp 0.600 1.400 2.400 | hairback_l0_ctl > hairback_l1_ctl > hairback_l2_ctl: period 3.333s, phase 0.200 0.280 0.360, amp 0.600 1.400 2.400 | bang_r0_ctl > bang_r1_ctl: period 3.333s, phase 0.180 0.280, amp 1.000 2.200 | bang_c0_ctl > bang_c1_ctl: period 3.333s, phase 0.180 0.280, amp 0.800 1.760 | bang_l0_ctl > bang_l1_ctl: period 3.333s, phase 0.180 0.280, amp 1.000 2.200 | lock0_ctl > lock1_ctl > lock2_ctl > lock3_ctl: period 3.333s, phase 0.160 0.230 0.300 0.370, amp 0.800 1.600 2.600 3.600 | lock1_0_ctl > lock1_1_ctl > lock1_2_ctl > lock1_3_ctl: period 3.333s, phase 0.160 0.230 0.300 0.370, amp 0.800 1.600 2.600 3.600 | sleeve_r0_ctl > sleeve_r1_ctl > sleeve_r2_ctl: period 3.333s, phase 0.220 0.300 0.380, amp 0.200 0.600 1.200 | sleeve_l0_ctl > sleeve_l1_ctl > sleeve_l2_ctl: period 3.333s, phase 0.770 0.850 0.930, amp 0.200 0.600 1.200 | skirt_r0_ctl > skirt_r1_ctl > skirt_r2_ctl: period 3.333s, phase 0.300 0.370 0.440, amp 0.150 0.350 0.700 | skirt_c0_ctl > skirt_c1_ctl > skirt_c2_ctl: period 3.333s, phase 0.340 0.410 0.480, amp 0.150 0.350 0.700 | skirt_l0_ctl > skirt_l1_ctl > skirt_l2_ctl: period 3.333s, phase 0.380 0.450 0.520, amp 0.150 0.350 0.700; lags neck > head_ctl +0.040 | head_ctl > hairback_r0_ctl +0.080 | hairback_r0_ctl > hairback_r1_ctl +0.080 | hairback_r1_ctl > hairback_r2_ctl +0.080 | head_ctl > hairback_l0_ctl +0.080 | hairback_l0_ctl > hairback_l1_ctl +0.080 | hairback_l1_ctl > hairback_l2_ctl +0.080 | head_ctl > bang_r0_ctl +0.060 | bang_r0_ctl > bang_r1_ctl +0.100 | head_ctl > bang_c0_ctl +0.060 | bang_c0_ctl > bang_c1_ctl +0.100 | head_ctl > bang_l0_ctl +0.060 | bang_l0_ctl > bang_l1_ctl +0.100 | head_ctl > lock0_ctl +0.040 | lock0_ctl > lock1_ctl +0.070 | lock1_ctl > lock2_ctl +0.070 | lock2_ctl > lock3_ctl +0.070 | head_ctl > lock1_0_ctl +0.040 | lock1_0_ctl > lock1_1_ctl +0.070 | lock1_1_ctl > lock1_2_ctl +0.070 | lock1_2_ctl > lock1_3_ctl +0.070 | sleeve_r0_ctl > sleeve_r1_ctl +0.080 | sleeve_r1_ctl > sleeve_r2_ctl +0.080 | sleeve_l0_ctl > sleeve_l1_ctl +0.080 | sleeve_l1_ctl > sleeve_l2_ctl +0.080 | skirt_r0_ctl > skirt_r1_ctl +0.070 | skirt_r1_ctl > skirt_r2_ctl +0.070 | skirt_c0_ctl > skirt_c1_ctl +0.070 | skirt_c1_ctl > skirt_c2_ctl +0.070 | skirt_l0_ctl > skirt_l1_ctl +0.070 | skirt_l1_ctl > skirt_l2_ctl +0.070; min_step 0.04; step_floor 0.001; other_period none; unread none; first_violation null
[check]   TIP_OVER_ROOT: PASS — instrument geometry; parts part handwear_l, root_rig_px 1.219, tip_rig_px 5.883, ratio 4.828 | part bottomwear, root_rig_px 0.351, tip_rig_px 1.264, ratio 3.604 | part handwear_r, root_rig_px 1.212, tip_rig_px 5.114, ratio 4.22; ratio_floor 1.4725
[check]   STILL_REGIONS_DARK: PASS — face parts face, head_bone head, instrument geometry, still_slots slot face, max_rig_px 4.093e-13, rms_rig_px 1.146e-13, max_rig_px 4.093e-13, at null, rms_rig_px 1.146e-13, tolerance_rig_px 2.286e-11, crossing slot hair_front, depth_rig_px 1.223, area_rig_px2 77.068, frame 38, driven_slots none; feet parts shoes, instrument geometry, still_slots slot shoes, max_rig_px 0, rms_rig_px 0, max_rig_px 0, at null, rms_rig_px 0, tolerance_rig_px 2.814e-12, crossing none
[check]   TEXTURE_STRETCH: PASS — meshes 8; triangles 722; frames 41; severity 1.126; severity_ceiling 1.926544; worst slot hair_front, triangle 86, vertices 31 | 36 | 32, edge 36 | 32, frame 22, ratio 0.888; max_ratio 1.114; min_ratio 0.888; per_mesh slot hair_back, triangles 178, max_ratio 1.045, max_at triangle 136 (vertices 104 107 105), edge 107-105, idle frame 2, min_ratio 0.957, min_at triangle 136 (vertices 104 107 105), edge 107-105, idle frame 22, severity 1.045 | slot hairpin, triangles 14, max_ratio 1.008, max_at triangle 1 (vertices 0 11 12), edge 11-12, idle frame 10, min_ratio 1, min_at triangle 4 (vertices 2 4 3), edge 4-3, idle frame 30, severity 1.008 | slot handwear_l, triangles 78, max_ratio 1.025, max_at triangle 65 (vertices 58 28 27), edge 28-27, idle frame 7, min_ratio 0.983, min_at triangle 65 (vertices 58 28 27), edge 28-27, idle frame 27, severity 1.025 | slot neck, triangles 12, max_ratio 1.015, max_at triangle 10 (vertices 11 6 4), edge 6-4, idle frame 13, min_ratio 0.991, min_at triangle 10 (vertices 11 6 4), edge 6-4, idle frame 33, severity 1.015 | slot bottomwear, triangles 182, max_ratio 1.018, max_at triangle 162 (vertices 105 112 106), edge 105-112, idle frame 32, min_ratio 0.982, min_at triangle 162 (vertices 105 112 106), edge 105-112, idle frame 12, severity 1.019 | slot topwear, triangles 92, max_ratio 1.056, max_at triangle 84 (vertices 57 18 58), edge 18-58, idle frame 10, min_ratio 0.996, min_at triangle 52 (vertices 44 49 45), edge 49-45, idle frame 10, severity 1.056 | slot handwear_r, triangles 74, max_ratio 1.019, max_at triangle 65 (vertices 53 21 20), edge 21-20, idle frame 23, min_ratio 0.989, min_at triangle 65 (vertices 53 21 20), edge 21-20, idle frame 3, severity 1.019 | slot hair_front, triangles 92, max_ratio 1.114, max_at triangle 86 (vertices 31 36 32), edge 36-32, idle frame 2, min_ratio 0.888, min_at triangle 86 (vertices 31 36 32), edge 36-32, idle frame 22, severity 1.126
[check]   ANIMATIONS_DO_NOT_FOLD: PASS — 1 animation(s) read by rigc render --folds at 12 fps (idle): 0 folding mesh(es), 0 not declared in may_fold (<= 0)
[check]   RECOMPOSITE_HOLES: REPORTED — error_px 6164; uncovered_error_px 1726; hole_count 444; largest px 154, box 321,1077 18x35, borders shoes 40 px | legwear 21 px
[check]   gate: spine-html green (cli_core.ts, rigc's own validator)
[check]   wrote out/check/gate_spine-html.txt, out/check/contact.png, out/check/motion_heat.png, out/check/check.json, out/check/build/, out/check/idle_frames/
[check] check: PASS; 10 of 10 bar(s) measured, 0 skipped
build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from
  pack: skeleton.png 517x1348, 22 region(s), 92.9% covered, padding 2, page edges free, shape polygon; page opaque 44.8% (alpha > 0) — spineboy yardstick 1024x256, 40 region(s), 45.8% opaque (alpha > 0), a reference and not a bar
  out/check/build/skeleton.json
  out/check/build/skeleton.atlas
  out/check/build/skeleton.png
[exit 0]
```

```
$ python3 grade.py runs/2026-10-20-claude-opus-5-5-03-correct
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 1726 against <= 3500"
PASS  does_not_fold: []
PASS  kept: "8 mesh(es) deformed against >= 8"
PASS  still_moves: "the back hair travels 45.881 rig px against the head over the idle, against >= 23"
clock: no started:/finished: lines in transcript.md
6 of 6 line(s); journal present, 0 entry(ies) whose line 4 begins WTF?:; log .grade/2026-10-20-claude-opus-5-5-03-correct/grade.log
[exit 0]
```
finished: 2026-10-20T13:41:32Z
