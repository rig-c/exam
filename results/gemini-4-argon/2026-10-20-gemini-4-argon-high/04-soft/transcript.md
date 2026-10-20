started: 2026-10-20T13:53:06Z

$ npx rig-parts build --config runs/2026-10-20-gemini-4-argon-high-04-soft/config.json --source tasks/01-build/inputs/painting.png --full tasks/01-build/inputs/layers/full --head tasks/01-build/inputs/layers/head --out runs/2026-10-20-gemini-4-argon-high-04-soft/out
[rig]   mesh topwear      v= 143 t= 214 hull= 70 contour tol=1 margin=1 spacing=31 bones=3 infl max 3 mean 1.90 cover 1.00000 overshoot 2 min angle 6.192618 region bust->chest_jiggle reaches 46 (21 whole)
[check]   TEXTURE_STRETCH: PASS — meshes 8; triangles 718; frames 41; severity 1.087; severity_ceiling 1.926544
[check]   ANIMATIONS_DO_NOT_FOLD: PASS — 2 animation(s) read by rigc render --folds at 12 fps, its 1 physics constraint(s) left out (idle, hop): 0 folding mesh(es), 0 not declared in may_fold (<= 0)
[check] check: PASS; 10 of 10 bar(s) measured, 0 skipped
build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from

$ npx rig-parts build --config runs/2026-10-20-gemini-4-argon-high-04-soft/config.json --source tasks/01-build/inputs/painting.png --full tasks/01-build/inputs/layers/full --head tasks/01-build/inputs/layers/head --out runs/2026-10-20-gemini-4-argon-high-04-soft/out
[check]   TEXTURE_STRETCH: PASS — meshes 8; triangles 654; frames 41; severity 1.084; severity_ceiling 1.926544
[check]   ANIMATIONS_DO_NOT_FOLD: PASS — 2 animation(s) read by rigc render --folds at 12 fps, its 1 physics constraint(s) left out (idle, hop): 0 folding mesh(es), 0 not declared in may_fold (<= 0)
[check] check: PASS; 10 of 10 bar(s) measured, 0 skipped
build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from
  pack: skeleton.png 382x1960, 22 region(s), 90.4% covered, padding 2, page edges free, shape polygon; page opaque 38.4% (alpha > 0) — spineboy yardstick 1024x256, 40 region(s), 45.8% opaque (alpha > 0), a reference and not a bar
  runs/2026-10-20-gemini-4-argon-high-04-soft/out/check/build/skeleton.json
  runs/2026-10-20-gemini-4-argon-high-04-soft/out/check/build/skeleton.atlas
  runs/2026-10-20-gemini-4-argon-high-04-soft/out/check/build/skeleton.png


$ python3 grade.py runs/2026-10-20-gemini-4-argon-high-04-soft
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 2059 against <= 4200"
PASS  does_not_fold: []
PASS  budget: "654 triangles against <= 700"
PASS  hop_as_given: "the built rig holds `hop` exactly as tasks/04-soft/hop.json gives it"
PASS  soft: "`topwear` differs from the same build without its physics by 6.61 rig px at hop frame 14, against 3.0 to 15.0"
PASS  a_patch: "14 of 111 `topwear` vertices move over 0.5 rig px, against >= 8 and <= 80 %"
PASS  hop_does_not_fold: []
clock: no started:/finished: lines in transcript.md
9 of 9 line(s); journal present, 1 entry(ies) whose line 4 begins WTF?:; log .grade/2026-10-20-gemini-4-argon-high-04-soft/grade.log

finished: 2026-10-20T14:06:14Z
