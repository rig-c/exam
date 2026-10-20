started: 2026-10-20T13:53:20Z

$ cp ../2026-10-20-claude-fable-5-1-01-build/config.json config.json; cp ../../tasks/04-soft/hop.json hop.json
$ python3 (animations_from hop.json; bone chest_jiggle under chest at [446,332]; topwear grid 31 -> contour {tolerance 2, margin 2, spacing 31, stray 4, regions [bust circle cx 446 cy 332 r 30 bone chest_jiggle spacing 12 band 16]}; constraints [bust_phys physics on chest_jiggle x 0.5 y 1 inertia 0.25 strength 120 damping 0.92 mass 1 mix 1])
$ rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out
[rig]   mesh topwear      v= 112 t= 188 hull= 34 contour tol=2 margin=2 spacing=31 bones=3 infl max 3 mean 1.91 cover 1.00000 overshoot 4 min angle 5.768728 region bust->chest_jiggle reaches 52 (26 whole)
[rig]   animations beside the idle, from <clone>/runs/2026-10-20-claude-fable-5-1-04-soft/hop.json as written: hop
[check]   loop physics: 1 physics constraint(s) left out of the loop's frames, reported, not judged — "bust_phys" on bone "chest_jiggle" (rig.json)
[check]   beside the idle: 1 animation(s), hop — built and gated by rigc with the rig; ANIMATIONS_DO_NOT_FOLD reads each for folds, every other bar here reads the idle
[check]   TEXTURE_STRETCH: PASS — meshes 8; triangles 692; frames 41; severity 1.098; severity_ceiling 1.926544; worst slot topwear, triangle 128, vertices 53 | 97 | 54, edge 97 | 54, frame 11, ratio 1.098; max_ratio 1.098; min_ratio 0.924; per_mesh slot hai
[check]   ANIMATIONS_DO_NOT_FOLD: PASS — 2 animation(s) read by rigc render --folds at 12 fps, its 1 physics constraint(s) left out (idle, hop): 0 folding mesh(es), 0 not declared in may_fold (<= 0)
build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from
  out/check/build/skeleton.json
  out/check/build/skeleton.atlas
  out/check/build/skeleton.png
exit 0 (real 2m38s)

$ python3 grade.py runs/2026-10-20-claude-fable-5-1-04-soft
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 2059 against <= 4200"
PASS  does_not_fold: []
PASS  budget: "692 triangles against <= 700"
PASS  hop_as_given: "the built rig holds `hop` exactly as tasks/04-soft/hop.json gives it"
PASS  soft: "`topwear` differs from the same build without its physics by 6.61 rig px at hop frame 14, against 3.0 to 15.0"
PASS  a_patch: "40 of 112 `topwear` vertices move over 0.5 rig px, against >= 8 and <= 80 %"
PASS  hop_does_not_fold: []
9 of 9 line(s); journal present, 0 entry(ies) whose line 4 begins WTF?:
finished: 2026-10-20T14:03:23Z
