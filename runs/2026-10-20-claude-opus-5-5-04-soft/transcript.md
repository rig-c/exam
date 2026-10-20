started: 2026-10-20T13:41:35Z

```
$ ../../node_modules/.bin/rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out
[check]   CHAIN_LAG: PASS — chains neck > head_ctl: period 3.333s, phase 0.080 0.120, amp 0.350 0.900 | bang_r0_ctl > bang_r1_ctl: period 3.333s, phase 0.180 0.280, amp 1.000 2.200 | bang_c0_ctl > bang_c1_ctl: period 3.333s, phase 0.180 0.280, amp 0.800 1.760 | bang_l0_ctl > bang_l1_ctl: period 3.333s, phase 0.180 0.280, amp 1.000 2.200 | lock0_ctl > lock1_ctl > lock2_ctl > lock3_ctl: period 3.333s, phase 0.160 0.230 0.300 0.370, amp 0.800 1.600 2.600 3.600 | lock1_0_ctl > lock1_1_ctl > lock1_2_ctl > lock1_3_ctl: period 3.333s, phase 0.160 0.230 0.300 0.370, amp 0.800 1.600 2.600 3.600 | sleeve_r0_ctl > sleeve_r1_ctl > sleeve_r2_ctl: period 3.333s, phase 0.220 0.300 0.380, amp 0.200 0.600 1.200 | sleeve_l0_ctl > sleeve_l1_ctl > sleeve_l2_ctl: period 3.333s, phase 0.770 0.850 0.930, amp 0.200 0.600 1.200 | skirt_r0_ctl > skirt_r1_ctl > skirt_r2_ctl: period 3.333s, phase 0.300 0.370 0.440, amp 0.150 0.350 0.700 | skirt_c0_ctl > skirt_c1_ctl > skirt_c2_ctl: period 3.333s, phase 0.340 0.410 0.480, amp 0.150 0.350 0.700 | skirt_l0_ctl > skirt_l1_ctl > skirt_l2_ctl: period 3.333s, phase 0.380 0.450 0.520, amp 0.150 0.350 0.700; lags neck > head_ctl +0.040 | head_ctl > bun_ctl +0.080 | head_ctl > bang_r0_ctl +0.060 | bang_r0_ctl > bang_r1_ctl +0.100 | head_ctl > bang_c0_ctl +0.060 | bang_c0_ctl > bang_c1_ctl +0.100 | head_ctl > bang_l0_ctl +0.060 | bang_l0_ctl > bang_l1_ctl +0.100 | head_ctl > lock0_ctl +0.040 | lock0_ctl > lock1_ctl +0.070 | lock1_ctl > lock2_ctl +0.070 | lock2_ctl > lock3_ctl +0.070 | head_ctl > lock1_0_ctl +0.040 | lock1_0_ctl > lock1_1_ctl +0.070 | lock1_1_ctl > lock1_2_ctl +0.070 | lock1_2_ctl > lock1_3_ctl +0.070 | sleeve_r0_ctl > sleeve_r1_ctl +0.080 | sleeve_r1_ctl > sleeve_r2_ctl +0.080 | sleeve_l0_ctl > sleeve_l1_ctl +0.080 | sleeve_l1_ctl > sleeve_l2_ctl +0.080 | skirt_r0_ctl > skirt_r1_ctl +0.070 | skirt_r1_ctl > skirt_r2_ctl +0.070 | skirt_c0_ctl > skirt_c1_ctl +0.070 | skirt_c1_ctl > skirt_c2_ctl +0.070 | skirt_l0_ctl > skirt_l1_ctl +0.070 | skirt_l1_ctl > skirt_l2_ctl +0.070; min_step 0.04; step_floor 0.001; other_period none; unread none; first_violation null
[check]   TIP_OVER_ROOT: PASS — instrument geometry; parts part handwear_l, root_rig_px 1.404, tip_rig_px 7.052, ratio 5.024 | part handwear_r, root_rig_px 1.36, tip_rig_px 6.914, ratio 5.085 | part bottomwear, root_rig_px 0.268, tip_rig_px 0.983, ratio 3.673; ratio_floor 1.4725
[check]   STILL_REGIONS_DARK: PASS — face parts face, head_bone head, instrument geometry, still_slots slot face, max_rig_px 3.882e-13, rms_rig_px 1.23e-13, max_rig_px 3.882e-13, at null, rms_rig_px 1.23e-13, tolerance_rig_px 2.286e-11, crossing slot hair_front, depth_rig_px 0.982, area_rig_px2 37.243, frame 18, driven_slots none; feet parts shoes, instrument geometry, still_slots slot shoes, max_rig_px 0, rms_rig_px 0, max_rig_px 0, at null, rms_rig_px 0, tolerance_rig_px 5.627e-12, crossing none
[check]   TEXTURE_STRETCH: PASS — meshes 8; triangles 683; frames 41; severity 1.115; severity_ceiling 1.926544; worst slot hair_front, triangle 68, vertices 56 | 30 | 28, edge 30 | 28, frame 8, ratio 1.115; max_ratio 1.115; min_ratio 0.901; per_mesh slot hair_back, triangles 72, max_ratio 1.02, max_at triangle 59 (vertices 47 19 18), edge 19-18, idle frame 16, min_ratio 0.988, min_at triangle 59 (vertices 47 19 18), edge 19-18, idle frame 36, severity 1.02 | slot handwear_l, triangles 78, max_ratio 1.022, max_at triangle 61 (vertices 56 26 25), edge 26-25, idle frame 7, min_ratio 0.986, min_at triangle 61 (vertices 56 26 25), edge 26-25, idle frame 27, severity 1.022 | slot handwear_r, triangles 78, max_ratio 1.022, max_at triangle 69 (vertices 17 19 18), edge 19-18, idle frame 6, min_ratio 0.986, min_at triangle 69 (vertices 17 19 18), edge 19-18, idle frame 26, severity 1.022 | slot neck, triangles 12, max_ratio 1.01, max_at triangle 8 (vertices 8 6 11), edge 8-6, idle frame 37, min_ratio 0.992, min_at triangle 4 (vertices 9 8 10), edge 9-8, idle frame 14, severity 1.01 | slot bottomwear, triangles 182, max_ratio 1.02, max_at triangle 101 (vertices 35 34 88), edge 35-34, idle frame 27, min_ratio 0.98, min_at triangle 101 (vertices 35 34 88), edge 35-34, idle frame 7, severity 1.02 | slot topwear, triangles 179, max_ratio 1.087, max_at triangle 131 (vertices 65 99 66), edge 99-66, idle frame 11, min_ratio 0.97, min_at triangle 98 (vertices 52 53 73), edge 73-52, idle frame 12, severity 1.087 | slot hairpin, triangles 8, max_ratio 1.008, max_at triangle 0 (vertices 0 8 1), edge 1-0, idle frame 10, min_ratio 1, min_at triangle 4 (vertices 7 6 8), edge 7-6, idle frame 30, severity 1.008 | slot hair_front, triangles 74, max_ratio 1.115, max_at triangle 68 (vertices 56 30 28), edge 30-28, idle frame 8, min_ratio 0.901, min_at triangle 60 (vertices 26 28 27), edge 26-28, idle frame 7, severity 1.115
[check]   ANIMATIONS_DO_NOT_FOLD: PASS — 3 animation(s) read by rigc render --folds at 12 fps, its 9 physics constraint(s) left out (idle, wave, hop): 0 folding mesh(es), 0 not declared in may_fold (<= 0)
[check]   RECOMPOSITE_HOLES: REPORTED — error_px 6275; uncovered_error_px 2059; hole_count 605; largest px 402, box 405,1073 39x25, borders shoes 58 px | legwear 43 px
[check]   gate: spine-html green (cli_core.ts, rigc's own validator)
[check]   wrote out/check/gate_spine-html.txt, out/check/contact.png, out/check/motion_heat.png, out/check/check.json, out/check/build/, out/check/idle_frames/
[check] check: PASS; 10 of 10 bar(s) measured, 0 skipped
build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from
  pack: skeleton.png 382x1960, 22 region(s), 90.4% covered, padding 2, page edges free, shape polygon; page opaque 38.4% (alpha > 0) — spineboy yardstick 1024x256, 40 region(s), 45.8% opaque (alpha > 0), a reference and not a bar
  out/check/build/skeleton.json
  out/check/build/skeleton.atlas
  out/check/build/skeleton.png
[exit 0]
```

```
$ ../../node_modules/.bin/rigc render --candidate out/check/build --animation hop --fps 30 --max 512 --folds --geometry --out work/hop
  ..    poser    rigc core — /Users/firejune/Workspace/Firejune/exam-runs/claude-opus-5-5-basic/exam-claude-opus-5-5/runs/2026-10-20-claude-opus-5-5-04-soft/out/check/build/skeleton.model.json
  ..    323x512px at 30 fps, 1 set(s) -> /Users/firejune/Workspace/Firejune/exam-runs/claude-opus-5-5-basic/exam-claude-opus-5-5/runs/2026-10-20-claude-opus-5-5-04-soft/work/hop
  ..    hop              31 frame(s), 1.000s + contact.png + geometry.json + folds.json (0 of 8 mesh(es) fold) -> /Users/firejune/Workspace/Firejune/exam-runs/claude-opus-5-5-basic/exam-claude-opus-5-5/runs/2026-10-20-claude-opus-5-5-04-soft/work/hop/hop@30fps
rigc: wrote /Users/firejune/Workspace/Firejune/exam-runs/claude-opus-5-5-basic/exam-claude-opus-5-5/runs/2026-10-20-claude-opus-5-5-04-soft/work/hop/frames.json
[exit 0]
```

```
$ python3 grade.py runs/2026-10-20-claude-opus-5-5-04-soft
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 2059 against <= 4200"
PASS  does_not_fold: []
PASS  budget: "683 triangles against <= 700"
PASS  hop_as_given: "the built rig holds `hop` exactly as tasks/04-soft/hop.json gives it"
PASS  soft: "`topwear` differs from the same build without its physics by 6.61 rig px at hop frame 14, against 3.0 to 15.0"
PASS  a_patch: "34 of 112 `topwear` vertices move over 0.5 rig px, against >= 8 and <= 80 %"
PASS  hop_does_not_fold: []
clock: no started:/finished: lines in transcript.md
9 of 9 line(s); journal present, 0 entry(ies) whose line 4 begins WTF?:; log .grade/2026-10-20-claude-opus-5-5-04-soft/grade.log
[exit 0]
```
finished: 2026-10-20T13:51:57Z
