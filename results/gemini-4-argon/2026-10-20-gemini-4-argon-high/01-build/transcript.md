started: 2026-10-20T13:23:23Z

$ npx rig-parts assemble --propose-plan --source tasks/01-build/inputs/painting.png --full tasks/01-build/inputs/layers/full --head tasks/01-build/inputs/layers/head --config runs/2026-10-20-gemini-4-argon-high-01-build/config.json
  "plan": [ ... 22 parts ... ],
  "extend_below_crop": [
    { "part": "hair_front", "run": "full", "tag": "front hair" },
    { "part": "hair_back", "run": "full", "tag": "back hair" }
  ],
  "notes": [ ... 7 notes ... ]

$ npx rig-parts assemble --source tasks/01-build/inputs/painting.png --full tasks/01-build/inputs/layers/full --head tasks/01-build/inputs/layers/head --config runs/2026-10-20-gemini-4-argon-high-01-build/config.json --out runs/2026-10-20-gemini-4-argon-high-01-build/work
  pixels: opaque 285469 = visible 222651 + occluded 62818 (22.0%); taken from the painting 180998 (63.4%); visible but not projected 41664 (14.6%)
  ghost px removed: 1183 over 58 layer(s)
recomposite vs source: mean |d|=1.13, within 8: 97.8%, error px > 40: 6275, uncovered error px: 2059
uncovered holes (8-connected): 605, the largest 5 listed
  uncovered hole 1: 402 px at 405,1073 39x25 (between "shoes" 58 px, "legwear" 43 px)
wrote runs/2026-10-20-gemini-4-argon-high-01-build/work/rig/parts.json, 22 PNG(s) in runs/2026-10-20-gemini-4-argon-high-01-build/work/rig/parts, runs/2026-10-20-gemini-4-argon-high-01-build/work/render/recomposite_rig.png, runs/2026-10-20-gemini-4-argon-high-01-build/work/render/recomposite_error_rig.png (uncovered error px red, covered error px blue, the painting grey)

$ npx rig-parts propose --parts runs/2026-10-20-gemini-4-argon-high-01-build/work/rig --source tasks/01-build/inputs/painting.png --out runs/2026-10-20-gemini-4-argon-high-01-build/work
wrote proposal.json (21 bone entries, 8 meshes) and render/landmarks.png (+_head) under runs/2026-10-20-gemini-4-argon-high-01-build/work
0 LINT line(s) over 8 mesh(es) and the hip
coverage: 40 bone(s) — 31 checked and clean, 0 checked with a LINT line, 9 not checked; roles 0 target, 39 deforms, 1 control, 0 unclassified
wrote basis.json (40 bone record(s) by the basis of their origin: 0 joint, 32 mask, 7 ratio, 1 derived) under runs/2026-10-20-gemini-4-argon-high-01-build/work

$ npx rig-parts build --config runs/2026-10-20-gemini-4-argon-high-01-build/config.json --source tasks/01-build/inputs/painting.png --full tasks/01-build/inputs/layers/full --head tasks/01-build/inputs/layers/head --out runs/2026-10-20-gemini-4-argon-high-01-build/out
[check]   ANIMATIONS_DO_NOT_FOLD: PASS — 1 animation(s) read by rigc render --folds at 12 fps (idle): 0 folding mesh(es), 0 not declared in may_fold (<= 0)
[check]   RECOMPOSITE_HOLES: REPORTED — error_px 6275; uncovered_error_px 2059; hole_count 605; largest px 402, box 405,1073 39x25, borders shoes 58 px | legwear 43 px
[check] check: PASS; 10 of 10 bar(s) measured, 0 skipped
build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from
  pack: skeleton.png 382x1962, 22 region(s), 90.3% covered, padding 2, page edges free, shape polygon; page opaque 38.4% (alpha > 0) — spineboy yardstick 1024x256, 40 region(s), 45.8% opaque (alpha > 0), a reference and not a bar
  runs/2026-10-20-gemini-4-argon-high-01-build/out/check/build/skeleton.json
  runs/2026-10-20-gemini-4-argon-high-01-build/out/check/build/skeleton.atlas
  runs/2026-10-20-gemini-4-argon-high-01-build/out/check/build/skeleton.png

$ python3 grade.py runs/2026-10-20-gemini-4-argon-high-01-build
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 2059 against <= 4200"
PASS  does_not_fold: []
clock: no started:/finished: lines in transcript.md
4 of 4 line(s); journal present, 0 entry(ies) whose line 4 begins WTF?:; log .grade/2026-10-20-gemini-4-argon-high-01-build/grade.log
finished: 2026-10-20T13:33:34Z
