started: 2026-10-20T14:06:14Z

```
$ npx rig-parts build --config runs/2026-10-20-gemini-4-argon-high-05-dance/config.json --source tasks/01-build/inputs/painting.png --full tasks/01-build/inputs/layers/full --head tasks/01-build/inputs/layers/head --out runs/2026-10-20-gemini-4-argon-high-05-dance/out
rig-parts build: runs/2026-10-20-gemini-4-argon-high-05-dance/config.json -> runs/2026-10-20-gemini-4-argon-high-05-dance/out, seam rule near-white, projection rule core, page edges free, pack shape polygon
[assemble]   FAIL  CONFIG_FIELD_PRESENT: config.motion.animations_from (/Users/firejune/Workspace/Firejune/exam-runs/gemini-4-argon-high-basic/exam-gemini-4-argon-high/runs/2026-10-20-gemini-4-argon-high-05-dance/dance.json).spec — is absent and required
[assemble] refused: 1 problem(s)
build: stopped at assemble; no later stage ran
```

```
$ npx rig-parts build --config runs/2026-10-20-gemini-4-argon-high-05-dance/config.json --source tasks/01-build/inputs/painting.png --full tasks/01-build/inputs/layers/full --head tasks/01-build/inputs/layers/head --out runs/2026-10-20-gemini-4-argon-high-05-dance/out
[check]   TIP_OVER_ROOT: PASS — instrument geometry; parts part handwear_l, root_rig_px 1.541, tip_rig_px 5.566, ratio 3.611 | part handwear_r, root_rig_px 1.439, tip_rig_px 5.308, ratio 3.689 | part bottomwear, root_rig_px 0.268, tip_rig_px 0.983, ratio 3.673; ratio_floor 1.4725
[check]   STILL_REGIONS_DARK: PASS — face parts face, head_bone head, instrument geometry, still_slots slot face, max_rig_px 3.882e-13, rms_rig_px 1.23e-13, max_rig_px 3.882e-13, at null, rms_rig_px 1.23e-13, tolerance_rig_px 2.286e-11, crossing slot hair_front, depth_rig_px 1.14, area_rig_px2 40.775, frame 18, driven_slots none; feet parts shoes, instrument geometry, still_slots slot shoes, max_rig_px 0, rms_rig_px 0, max_rig_px 0, at null, rms_rig_px 0, tolerance_rig_px 5.627e-12, crossing none
[check]   TEXTURE_STRETCH: PASS — meshes 9; triangles 890; frames 41; severity 1.084; severity_ceiling 1.926544
[check]   ANIMATIONS_DO_NOT_FOLD: PASS — 2 animation(s) read by rigc render --folds at 12 fps, its 1 physics constraint(s) left out (idle, dance): 0 folding mesh(es), 0 not declared in may_fold (<= 0)
[check]   RECOMPOSITE_HOLES: REPORTED — error_px 6275; uncovered_error_px 2059; hole_count 605; largest px 402, box 405,1073 39x25, borders shoes 58 px | legwear 43 px
[check]   gate: spine-html green (cli_core.ts, rigc's own validator)
[check] check: PASS; 10 of 10 bar(s) measured, 0 skipped
build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from
  runs/2026-10-20-gemini-4-argon-high-05-dance/out/check/build/skeleton.json
  runs/2026-10-20-gemini-4-argon-high-05-dance/out/check/build/skeleton.atlas
  runs/2026-10-20-gemini-4-argon-high-05-dance/out/check/build/skeleton.png
```

```
$ python3 grade.py runs/2026-10-20-gemini-4-argon-high-05-dance
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 2059 against <= 4200"
PASS  does_not_fold: []
PASS  budget: "890 triangles against <= 1000"
PASS  dance_as_timed: "`dance` lasts 4 s against 4.0"
PASS  closes: "the last frame is 0.0 rig px from the first at its furthest vertex, against <= 0.5 (keys only, physics out)"
PASS  both_hands: "`handwear_l` travels 277.8 rig px and `handwear_r` 275.9 at their furthest vertex, measured from the middle of `topwear`, each against >= 100.0"
PASS  whole_body: "the vertex of `topwear` that travels least travels 20.0 rig px, measured from the middle of `shoes`, against >= 15.0"
PASS  arms_bend_at_the_joints: "along its own length an upper arm or a forearm bends at most 0.4 degrees more than at rest, against <= 8.0"
PASS  on_her_feet: "the end of a leg (`legwear`) gets 0.0 rig px from where it meets `shoes`, against <= 6.0"
PASS  keeps_time: "1.0 of the variation in how fast she moves repeats every two beats, against >= 0.5"
PASS  soft_in_the_dance: "`topwear` differs from the same build without its physics by 5.357 rig px at dance frame 42, against 3.0 to 15.0"
PASS  dance_does_not_fold: []
clock: no started:/finished: lines in transcript.md
14 of 14 line(s); journal present, 1 entry(ies) whose line 4 begins WTF?:; log .grade/2026-10-20-gemini-4-argon-high-05-dance/grade.log
```

finished: 2026-10-20T14:34:50Z



