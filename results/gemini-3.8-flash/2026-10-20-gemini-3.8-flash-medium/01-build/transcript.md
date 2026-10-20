started: 2026-10-20T13:23:10Z

$ ./node_modules/.bin/rig-parts assemble --source tasks/01-build/inputs/painting.png --full tasks/01-build/inputs/layers/full --head tasks/01-build/inputs/layers/head --config runs/2026-10-20-gemini-3.8-flash-medium-01-build/config.json --out work
recomposite vs source: mean |d|=1.13, within 8: 97.8%, error px > 40: 6275, uncovered error px: 2059
uncovered holes (8-connected): 605, the largest 5 listed
  uncovered hole 1: 402 px at 405,1073 39x25 (between "shoes" 58 px, "legwear" 43 px)
  uncovered hole 2: 98 px at 354,33 69x77 (between "hair_back" 146 px)
  uncovered hole 3: 55 px at 487,190 6x47 (between "hair_front" 50 px, "topwear" 9 px, "hair_back" 4 px, "hairpin" 4 px)
  uncovered hole 4: 38 px at 376,191 1x38 (between "hair_front" 40 px)
  uncovered hole 5: 33 px at 364,388 7x9 (between "topwear" 8 px, "handwear_r" 5 px)
wrote work/rig/parts.json, 22 PNG(s) in work/rig/parts, work/render/recomposite_rig.png, work/render/recomposite_error_rig.png (uncovered error px red, covered error px blue, the painting grey)

$ ./node_modules/.bin/rig-parts propose --parts work/rig --source tasks/01-build/inputs/painting.png --out work
coverage: 40 bone(s) — 31 checked and clean, 0 checked with a LINT line, 9 not checked; roles 0 target, 39 deforms, 1 control, 0 unclassified
wrote basis.json (40 bone record(s) by the basis of their origin: 0 joint, 32 mask, 7 ratio, 1 derived) under work

$ ./node_modules/.bin/rig-parts propose --parts work/rig --source tasks/01-build/inputs/painting.png --out work --from-config runs/2026-10-20-gemini-3.8-flash-medium-01-build/config.json
0 LINT line(s) over 8 mesh(es) and the hip
coverage: 40 bone(s) — 31 checked and clean, 0 checked with a LINT line, 9 not checked; roles 0 target, 39 deforms, 1 control, 0 unclassified

$ python3 grade.py runs/2026-10-20-gemini-3.8-flash-medium-01-build
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 2059 against <= 4200"
PASS  does_not_fold: []
finished: 2026-10-20T13:28:25Z
