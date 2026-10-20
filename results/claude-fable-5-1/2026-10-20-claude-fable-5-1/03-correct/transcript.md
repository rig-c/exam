started: 2026-10-20T13:42:14Z

$ cat > config.json   # key, seethrough (head_box [538,158,1100,720]), assemble.rig_scale 0.5
$ rig-parts assemble --propose-plan --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --config config.json
{ "plan": [ 22 rows: hair_back(head), hairpin(full), handwear_l, shoes, legwear, neck(head), bottomwear, topwear, handwear_r, ears, face, mouth, eyewhites, irises, lashes, brows, hair_front(head) ],
  "extend_below_crop": [hair_front, hair_back from full], "notes": [ "headwear: head run 5 rig px < 0.8 x full run 2146 -> full-run layer, drawn behind the face", neckwear/tail/wings/objects/eyewear/earwear empty, nose never planned ] }
exit 0

$ python3 (paste plan + extend_below_crop)
$ rig-parts assemble --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --config config.json --out work
rig-parts assemble: 22 part(s) on a 832x1216 rig (0.5 rig px per source px), seam rule near-white, projection rule core
  pixels: opaque 310012 = visible 208962 + occluded 101050 (32.6%); taken from the painting 146975 (47.4%); visible but not projected 61967 (20.0%)
recomposite vs source: mean |d|=1.09, within 8: 97.9%, error px > 40: 6164, uncovered error px: 1726
uncovered holes (8-connected): 444, the largest 5 listed
  uncovered hole 1: 154 px at 321,1077 18x35 (between "shoes" 40 px, "legwear" 21 px)
  … (holes 2–5: 150, 100, 48, 37 px)
exit 0

$ rig-parts propose --parts work/rig --source inputs/painting.png --out work
wrote proposal.json (22 bone entries, 8 meshes) and render/landmarks.png (+_head) under work
note: … (head frame roll 21.038; head pitch not read; lash_r note; breath 5.02 px; hair_front template; handwear two blobs; no robe chains; bottomwear hangs from the waist; legwear region on hip; grid 30)
LINT hairback_r and hairback_l on mesh 'hair_back' squeeze it: swung together, every other bone held, edge 37-117 of triangle 167 closes to 0.064 times its rest length at idle frame 22 (max(ratio, 1/ratio) 15.572; <= 1.926544 is required, check's TEXTURE_STRETCH bar) — vertex 37 rides hairback_r2 0.91971, vertex 117 rides hairback_l2 0.90416; alone, hairback_r reads 1.880 and hairback_l 1.883. Their tips are 39.0 px apart and their amplitudes are opposed (hairback_r [0.6, 1.4, 2.4], hairback_l [-0.6, -1.4, -2.4]), so their tips swing towards each other and apart: give both the same sign (then 1.046), or drop one chain
1 LINT line(s) over 8 mesh(es) and the hip
coverage: 45 bone(s) — 35 checked and clean, 2 checked with a LINT line, 8 not checked
exit 0
$ python3 (paste bones/meshes/regions/motion; motion.tracks hairback_l amps [-0.6,-1.4,-2.4] -> [0.6,1.4,2.4], with a note)
$ rig-parts propose --parts work/rig --source inputs/painting.png --out work --from-config config.json
0 LINT line(s) over 8 mesh(es) and the hip
coverage: 45 bone(s) — 37 checked and clean, 0 checked with a LINT line, 8 not checked
exit 0

$ rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out
[check]   pack: skeleton.png 517x1348, 22 region(s), 92.9% covered, padding 2, page edges free, shape polygon; page opaque 44.8% (alpha > 0) — spineboy yardstick 1024x256, 40 region(s), 45.8% opaque (alpha > 0), a reference and not a bar
[check]   loop: idle 41 frame(s) at 12 fps, f0000 vs f0040 (t = 3.333333333333333s): max |d| 0 (0 required)
[check]   seam: setup pose at 504x1216, scale 1.0098: mean |d| 0.148 (<= 1.0), 2 px over 40, 1.96 rig px (the count / s²; <= 50), 0 px over 80 (reported)
[check]   BREATH_VISIBLE: PASS — torso_parts topwear; torso_heat_mean 15.692; torso_floor 3.809; feet_parts shoes; feet_heat_max 0; feet_ceiling 0
[check]   BLINK_NO_HOLE: PASS — eye_parts eyewhite_r | eyewhite_l; closed group eyes scaley 0.12 from 2.37s to 2.454s; idle_frames_closed 29; box_px 5148; hole_px 0; hole_bar 0; patch_max 10; patch_px_over_40 0
[check]   CHAIN_LAG: PASS — chains neck > head_ctl: period 3.333s, phase 0.080 0.120, amp 0.350 0.900 | hairback_r0_ctl > hairback_r1_ctl > hairback_r2_ctl: period 3.333s, phase 0.200 0.280 0.360, amp 0.600 1.400 2.400 | hairback_l0_ctl > hairback_l1_ctl > h
[check]   TIP_OVER_ROOT: PASS — instrument geometry; parts part handwear_l, root_rig_px 1.219, tip_rig_px 5.883, ratio 4.828 | part bottomwear, root_rig_px 0.351, tip_rig_px 1.264, ratio 3.604 | part handwear_r, root_rig_px 1.212, tip_rig_px 5.114, ratio 4.2
[check]   STILL_REGIONS_DARK: PASS — face parts face, head_bone head, instrument geometry, still_slots slot face, max_rig_px 4.093e-13, rms_rig_px 1.146e-13, max_rig_px 4.093e-13, at null, rms_rig_px 1.146e-13, tolerance_rig_px 2.286e-11, crossing slot hair_
[check]   TEXTURE_STRETCH: PASS — meshes 8; triangles 722; frames 41; severity 1.126; severity_ceiling 1.926544; worst slot hair_front, triangle 86, vertices 31 | 36 | 32, edge 36 | 32, frame 22, ratio 0.888; max_ratio 1.114; min_ratio 0.888; per_mesh slot h
[check]   ANIMATIONS_DO_NOT_FOLD: PASS — 1 animation(s) read by rigc render --folds at 12 fps (idle): 0 folding mesh(es), 0 not declared in may_fold (<= 0)
[check]   RECOMPOSITE_HOLES: REPORTED — error_px 6164; uncovered_error_px 1726; hole_count 444; largest px 154, box 321,1077 18x35, borders shoes 40 px | legwear 21 px
build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from
  out/check/build/skeleton.json
  out/check/build/skeleton.atlas
  out/check/build/skeleton.png
exit 0 (real 2m50s)

$ python3 grade.py runs/2026-10-20-claude-fable-5-1-03-correct
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 1726 against <= 3500"
PASS  does_not_fold: []
PASS  kept: "8 mesh(es) deformed against >= 8"
PASS  still_moves: "the back hair travels 45.881 rig px against the head over the idle, against >= 23"
6 of 6 line(s); journal present, 0 entry(ies) whose line 4 begins WTF?:
finished: 2026-10-20T13:53:20Z
