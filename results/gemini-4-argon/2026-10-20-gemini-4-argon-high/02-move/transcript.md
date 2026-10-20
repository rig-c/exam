started: 2026-10-20T13:33:45Z

$ npx rig-parts build --config runs/2026-10-20-gemini-4-argon-high-02-move/config.json --source tasks/01-build/inputs/painting.png --full tasks/01-build/inputs/layers/full --head tasks/01-build/inputs/layers/head --out runs/2026-10-20-gemini-4-argon-high-02-move/out
[check]   ANIMATIONS_DO_NOT_FOLD: PASS — 2 animation(s) read by rigc render --folds at 12 fps, its 8 physics constraint(s) left out (idle, wave): 0 folding mesh(es), 0 not declared in may_fold (<= 0)
[check]   RECOMPOSITE_HOLES: REPORTED — error_px 6275; uncovered_error_px 2059; hole_count 605; largest px 402, box 405,1073 39x25, borders shoes 58 px | legwear 43 px
[check] check: PASS; 10 of 10 bar(s) measured, 0 skipped
build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from
  pack: skeleton.png 382x1962, 22 region(s), 90.3% covered, padding 2, page edges free, shape polygon; page opaque 38.4% (alpha > 0) — spineboy yardstick 1024x256, 40 region(s), 45.8% opaque (alpha > 0), a reference and not a bar
  runs/2026-10-20-gemini-4-argon-high-02-move/out/check/build/skeleton.json
  runs/2026-10-20-gemini-4-argon-high-02-move/out/check/build/skeleton.atlas
  runs/2026-10-20-gemini-4-argon-high-02-move/out/check/build/skeleton.png

$ python3 grade.py runs/2026-10-20-gemini-4-argon-high-02-move
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 2059 against <= 4200"
PASS  does_not_fold: []
PASS  trails: "8 bone(s) on a physics constraint: lock0, lock1, lock1_0, lock1_1, lock1_2, lock1_3, lock2, lock3"
PASS  moves: {"animation": "wave", "duration": 2, "rise": 178.0, "folds": []}
PASS  moves_without_folding: []
clock: no started:/finished: lines in transcript.md
7 of 7 line(s); journal present, 0 entry(ies) whose line 4 begins WTF?:; log .grade/2026-10-20-gemini-4-argon-high-02-move/grade.log
finished: 2026-10-20T13:42:14Z
