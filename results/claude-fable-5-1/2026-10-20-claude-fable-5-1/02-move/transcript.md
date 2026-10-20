started: 2026-10-20T13:26:58Z

$ cp ../2026-10-20-claude-fable-5-1-01-build/config.json config.json; cat > wave.json; python3 (motion.animations_from = "wave.json"; 8 physics constraints on lock0..3, lock1_0..3: rotate 1, inertia 0.8, strength 90/79.5/69/58.5, damping 0.85, mass 1, mix 1)
$ rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out
[rig]   animations beside the idle, from <clone>/runs/2026-10-20-claude-fable-5-1-02-move/wave.json as written: wave
[check]   loop: idle 41 frame(s) at 12 fps, f0000 vs f0040 (t = 3.333333333333333s) with the rig's 8 physics constraint(s) left out (named on the `loop physics:` line; rendered with them, the ends need not meet — `build --loop --lead-in <n>`): max |d| 0 (0 required)
[check]   loop physics: 8 physics constraint(s) left out of the loop's frames, reported, not judged — "lock0_phys" on bone "lock0" (rig.json), "lock1_phys" on bone "lock1" (rig.json), "lock2_phys" on bone "lock2" (rig.json), "lock3_phys" on bone "lock3" (rig.json), "lock1_0_phys" on bone "lock1_0"
[check]   beside the idle: 1 animation(s), wave — built and gated by rigc with the rig; ANIMATIONS_DO_NOT_FOLD reads each for folds, every other bar here reads the idle
[check]   BREATH_VISIBLE: PASS — torso_parts topwear; torso_heat_mean 16.171; torso_floor 3.809; feet_parts shoes; feet_heat_max 0; feet_ceiling 0
[check]   BLINK_NO_HOLE: PASS — eye_parts eyewhite_r | eyewhite_l; closed group eyes scaley 0.12 from 2.37s to 2.454s; idle_frames_closed 29; box_px 2937; hole_px 0; hole_bar 0; patch_max 8; patch_px_over_40 0
[check]   CHAIN_LAG: PASS — chains neck > head_ctl: period 3.333s, phase 0.080 0.120, amp 0.350 0.900 | bang_r0_ctl > bang_r1_ctl: period 3.333s, phase 0.180 0.280, amp 1.000 2.200 | bang_c0_ctl > bang_c1_ctl: period 3.333s, phase 0.180 0.280, amp 0.800 1.760 | bang_l0_ctl > bang_l1_ctl: period 3.
[check]   TIP_OVER_ROOT: PASS — instrument geometry; parts part handwear_l, root_rig_px 1.404, tip_rig_px 7.052, ratio 5.024 | part handwear_r, root_rig_px 1.36, tip_rig_px 6.914, ratio 5.085 | part bottomwear, root_rig_px 0.268, tip_rig_px 0.983, ratio 3.673; ratio_floor 1.4725
[check]   STILL_REGIONS_DARK: PASS — face parts face, head_bone head, instrument geometry, still_slots slot face, max_rig_px 3.882e-13, rms_rig_px 1.23e-13, max_rig_px 3.882e-13, at null, rms_rig_px 1.23e-13, tolerance_rig_px 2.286e-11, crossing slot hair_front, depth_rig_px 0.982, area_rig_px2 37
[check]   TEXTURE_STRETCH: PASS — meshes 8; triangles 590; frames 41; severity 1.115; severity_ceiling 1.926544; worst slot hair_front, triangle 68, vertices 56 | 30 | 28, edge 30 | 28, frame 8, ratio 1.115; max_ratio 1.115; min_ratio 0.901; per_mesh slot hair_back, triangles 72, max_ratio 1.02, m
[check]   ANIMATIONS_DO_NOT_FOLD: PASS — 2 animation(s) read by rigc render --folds at 12 fps, its 8 physics constraint(s) left out (idle, wave): 0 folding mesh(es), 0 not declared in may_fold (<= 0)
[check]   RECOMPOSITE_HOLES: REPORTED — error_px 6275; uncovered_error_px 2059; hole_count 605; largest px 402, box 405,1073 39x25, borders shoes 58 px | legwear 43 px
build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from
  out/check/build/skeleton.json
  out/check/build/skeleton.atlas
  out/check/build/skeleton.png
exit 0 (real 4m03s)

$ python3 (wave.json: sleeve_l0 keys 0→50 hold →0, sleeve_l1 0→75 hold →0; sleeve_l2 unchanged)
$ rm -rf out; rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out
[check]   TEXTURE_STRETCH: PASS — meshes 8; triangles 590; frames 41; severity 1.115; severity_ceiling 1.926544; worst slot hair_front, triangle 68, vertices 56 | 30 | 28, edge 30 | 28, frame 8, ratio 1.115; max_ratio 1.115; min_ratio 0.901; per_me
[check]   ANIMATIONS_DO_NOT_FOLD: PASS — 2 animation(s) read by rigc render --folds at 12 fps, its 8 physics constraint(s) left out (idle, wave): 0 folding mesh(es), 0 not declared in may_fold (<= 0)
build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from
exit 0 (real 2m36s)

$ python3 grade.py runs/2026-10-20-claude-fable-5-1-02-move
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 2059 against <= 4200"
PASS  does_not_fold: []
PASS  trails: "8 bone(s) on a physics constraint: lock0, lock1, lock1_0, lock1_1, lock1_2, lock1_3, lock2, lock3"
PASS  moves: {"animation": "wave", "duration": 2.2, "rise": 300.2, "folds": []}
PASS  moves_without_folding: []
7 of 7 line(s); journal present, 0 entry(ies) whose line 4 begins WTF?:
(an earlier grade of the first wave.json read rise 259.1, 7 of 7; the arm pointed sideways, so the elbow was bent further and the build and grade run again)
finished: 2026-10-20T13:42:14Z
