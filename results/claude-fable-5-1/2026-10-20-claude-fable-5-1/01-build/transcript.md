started: 2026-10-20T13:20:07Z

$ cat > config.json   # key, seethrough (from inputs/seethrough.json), assemble.rig_scale 0.5
$ rig-parts assemble --propose-plan --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --config config.json
{ "plan": [ ["hair_back","head","back hair"], ["handwear_l","full","handwear-l"], ["handwear_r","full","handwear-r"], ["legwear","full","legwear"], ["shoes","full","footwear"], ["neck","head","neck"], ["bottomwear","full","bottomwear"], ["topwear","full","topwear"], ["hairpin","head","headwear"], ["ear_l","head","ears-l"], ["ear_r","head","ears-r"], ["face","head","face"], ["mouth","head","mouth"], ["eyewhite_r","head","eyewhite-r"], ["eyewhite_l","head","eyewhite-l"], ["iris_l","head","irides-l"], ["iris_r","head","irides-r"], ["lash_l","head","eyelash-l"], ["lash_r","head","eyelash-r"], ["brow_r","head","eyebrow-r"], ["brow_l","head","eyebrow-l"], ["hair_front","head","front hair"] ],
  "extend_below_crop": [ {"part":"hair_front","run":"full","tag":"front hair"}, {"part":"hair_back","run":"full","tag":"back hair"} ],
  "notes": [ "neckwear: in no plan row — … below the proposer's floor of 150 …", "tail: …", "wings: …", "objects: …", "eyewear: …", "earwear: …", "nose: in no plan row — the proposer never plans nose … add [\"nose\", \"head\", \"nose\"] to assemble.plan after the row that takes \"face\" …" ] }
exit 0

$ python3 (paste plan + extend_below_crop into config.json assemble)
$ rig-parts assemble --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --config config.json --out work
rig-parts assemble: 22 part(s) on a 832x1216 rig (0.5 rig px per source px), seam rule near-white, projection rule core
  … (22 part lines, 12 fringe pushed back lines)
  pixels: opaque 285469 = visible 222651 + occluded 62818 (22.0%); taken from the painting 180998 (63.4%); visible but not projected 41664 (14.6%)
  ghost px removed: 1183 over 58 layer(s)
recomposite vs source: mean |d|=1.13, within 8: 97.8%, error px > 40: 6275, uncovered error px: 2059
uncovered holes (8-connected): 605, the largest 5 listed
  uncovered hole 1: 402 px at 405,1073 39x25 (between "shoes" 58 px, "legwear" 43 px)
  uncovered hole 2: 98 px at 354,33 69x77 (between "hair_back" 146 px)
  uncovered hole 3: 55 px at 487,190 6x47 (between "hair_front" 50 px, "topwear" 9 px, "hair_back" 4 px, "hairpin" 4 px)
  uncovered hole 4: 38 px at 376,191 1x38 (between "hair_front" 40 px)
  uncovered hole 5: 33 px at 364,388 7x9 (between "topwear" 8 px, "handwear_r" 5 px)
wrote work/rig/parts.json, 22 PNG(s) in work/rig/parts, work/render/recomposite_rig.png, work/render/recomposite_error_rig.png
exit 0

$ rig-parts propose --parts work/rig --source inputs/painting.png --out work
wrote proposal.json (21 bone entries, 8 meshes) and render/landmarks.png (+_head) under work
note: head frame: the bar runs through eye_r [412.0, 138.0] and eye_l [474.0, 149.0] … roll -10.061 degrees …
note: head pitch: the nose sits — (not read: no part tagged nose) …
note: lash_l (head:eyelash-l) reaches 4 px above eyewhite_l's top … not split …
note: breath: chest translatey 4.98 px peak to peak (amp 2.49, base 2.49) = 2.5 % of the torso's length, 199.0 px (neck [443, 226] -> hip [446, 425]) …
note: hair_front (head:front hair): bang_r, bang_c, bang_l are a template, not its locks … move the chains onto the locks
note: handwear is two blobs: one sleeve chain per mesh, chest only at the shoulder
note: topwear ends at y=428 (hip 425): no robe chains -- add a sash chain by hand if one hangs
note: bottomwear (full:bottomwear): its art starts 78.6 px below chest's origin, so it hangs from the waist …
note: legwear (full:legwear): no rule -> region on hip
note: mesh spacing: grid 31 = round(H / 37), H 1160 rig px …
0 LINT line(s) over 8 mesh(es) and the hip
coverage … (40 lines)
coverage: 40 bone(s) — 31 checked and clean, 0 checked with a LINT line, 9 not checked; roles 0 target, 39 deforms, 1 control, 0 unclassified
wrote basis.json (40 bone record(s) by the basis of their origin: 0 joint, 32 mask, 7 ratio, 1 derived) under work
exit 0

$ python3 (paste bones, meshes, regions, motion from work/proposal.json into config.json)
$ rig-parts propose --parts work/rig --source inputs/painting.png --out work --from-config config.json
wrote work/render/landmarks_config.png (+_head)
0 LINT line(s) over 8 mesh(es) and the hip
coverage: 40 bone(s) — 31 checked and clean, 0 checked with a LINT line, 9 not checked; roles 0 target, 39 deforms, 1 control, 0 unclassified
exit 0

$ rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out
[check]   pack: skeleton.png 382x1962, 22 region(s), 90.3% covered, padding 2, page edges free, shape polygon; page opaque 38.4% (alpha > 0) — spineboy yardstick 1024x256, 40 region(s), 45.8% opaque (alpha > 0), a reference and not a bar
[check]   loop: idle 41 frame(s) at 12 fps, f0000 vs f0040 (t = 3.333333333333333s): max |d| 0 (0 required)
[check]   seam: setup pose at 601x1216, scale 0.9640: mean |d| 0.117 (<= 1.0), 0 px over 40, 0.00 rig px (the count / s²; <= 50), 0 px over 80 (reported)
[check]   BREATH_VISIBLE: PASS — torso_parts topwear; torso_heat_mean 16.171; torso_floor 3.809; feet_parts shoes; feet_heat_max 0; feet_ceiling 0
[check]   BLINK_NO_HOLE: PASS — eye_parts eyewhite_r | eyewhite_l; closed group eyes scaley 0.12 from 2.37s to 2.454s; idle_frames_closed 29; box_px 2937; hole_px 0; hole_bar 0; patch_max 8; patch_px_over_40 0
[check]   CHAIN_LAG: PASS — chains neck > head_ctl: period 3.333s, phase 0.080 0.120, amp 0.350 0.900 | bang_r0_ctl > bang_r1_ctl: period 3.333s, phase 0.180 0.280, amp 1.000 2.200 | bang_c0_ctl > bang_c1_ctl: period 3.333s, phase 0.180 0.280, amp 0.800 1.760 | bang_l0_ctl > bang_l1_ctl: period 3.333s, phase 0.180 0.280, amp 1.000 2.200 | lock0_ctl > lock1_ctl > lock2_ctl > lock3_ctl: period 3.3
[check]   TIP_OVER_ROOT: PASS — instrument geometry; parts part handwear_l, root_rig_px 1.404, tip_rig_px 7.052, ratio 5.024 | part handwear_r, root_rig_px 1.36, tip_rig_px 6.914, ratio 5.085 | part bottomwear, root_rig_px 0.268, tip_rig_px 0.983, ratio 3.673; ratio_floor 1.4725
[check]   STILL_REGIONS_DARK: PASS — face parts face, head_bone head, instrument geometry, still_slots slot face, max_rig_px 3.882e-13, rms_rig_px 1.23e-13, max_rig_px 3.882e-13, at null, rms_rig_px 1.23e-13, tolerance_rig_px 2.286e-11, crossing slot hair_front, depth_rig_px 1.14, area_rig_px2 40.775, frame 18, driven_slots none; feet parts shoes, instrument geometry, still_slots slot shoes, max
[check]   TEXTURE_STRETCH: PASS — meshes 8; triangles 590; frames 41; severity 1.084; severity_ceiling 1.926544; worst slot hair_front, triangle 68, vertices 56 | 30 | 28, edge 30 | 28, frame 3, ratio 1.084; max_ratio 1.084; min_ratio 0.924; per_mesh slot hair_back, triangles 72, max_ratio 1.02, max_at triangle 59 (vertices 47 19 18), edge 19-18, idle frame 16, min_ratio 0.988, min_at triangle 5
[check]   ANIMATIONS_DO_NOT_FOLD: PASS — 1 animation(s) read by rigc render --folds at 12 fps (idle): 0 folding mesh(es), 0 not declared in may_fold (<= 0)
[check]   RECOMPOSITE_HOLES: REPORTED — error_px 6275; uncovered_error_px 2059; hole_count 605; largest px 402, box 405,1073 39x25, borders shoes 58 px | legwear 43 px
build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from
  pack: skeleton.png 382x1962, 22 region(s), 90.3% covered, padding 2, page edges free, shape polygon; page opaque 38.4% (alpha > 0) — spineboy yardstick 1024x256, 40 region(s), 45.8% opaque (alpha > 0), a reference and not a bar
  out/check/build/skeleton.json
  out/check/build/skeleton.atlas
  out/check/build/skeleton.png
exit 0 (real 1m17s)

$ python3 grade.py runs/2026-10-20-claude-fable-5-1-01-build
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 2059 against <= 4200"
PASS  does_not_fold: []
4 of 4 line(s); journal present, 1 entry(ies) whose line 4 begins WTF?:
finished: 2026-10-20T13:26:57Z
