started: 2026-10-20T13:35:29Z

$ ./node_modules/.bin/rig-parts assemble --source tasks/03-correct/inputs/painting.png --full tasks/03-correct/inputs/layers/full --head tasks/03-correct/inputs/layers/head --config runs/2026-10-20-gemini-3.8-flash-medium-03-correct/config.json --out work
recomposite vs source: mean |d|=1.09, within 8: 97.9%, error px > 40: 6164, uncovered error px: 1726
wrote work/rig/parts.json, 22 PNG(s) in work/rig/parts, work/render/recomposite_rig.png, work/render/recomposite_error_rig.png (uncovered error px red, covered error px blue, the painting grey)

$ ./node_modules/.bin/rig-parts propose --parts work/rig --source tasks/03-correct/inputs/painting.png --out work
LINT hairback_r and hairback_l on mesh 'hair_back' squeeze it: swung together, every other bone held, edge 37-117 of triangle 167 closes to 0.064 times its rest length at idle frame 22 (max(ratio, 1/ratio) 15.572; <= 1.926544 is required, check's TEXTURE_STRETCH bar) — vertex 37 rides hairback_r2 0.91971, vertex 117 rides hairback_l2 0.90416; alone, hairback_r reads 1.880 and hairback_l 1.883. Their tips are 39.0 px apart and their amplitudes are opposed (hairback_r [0.6, 1.4, 2.4], hairback_l [-0.6, -1.4, -2.4]), so their tips swing towards each other and apart: give both the same sign (then 1.046), or drop one chain
1 LINT line(s) over 8 mesh(es) and the hip
coverage: 45 bone(s) — 35 checked and clean, 2 checked with a LINT line, 8 not checked; roles 0 target, 44 deforms, 1 control, 0 unclassified
wrote basis.json (45 bone record(s) by the basis of their origin: 0 joint, 38 mask, 6 ratio, 1 derived) under work

$ ./node_modules/.bin/rig-parts propose --parts work/rig --source tasks/03-correct/inputs/painting.png --out work --from-config runs/2026-10-20-gemini-3.8-flash-medium-03-correct/config.json
0 LINT line(s) over 8 mesh(es) and the hip
coverage: 45 bone(s) — 37 checked and clean, 0 checked with a LINT line, 8 not checked; roles 0 target, 44 deforms, 1 control, 0 unclassified

$ python3 grade.py runs/2026-10-20-gemini-3.8-flash-medium-03-correct
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 1726 against <= 3500"
PASS  does_not_fold: []
PASS  kept: "8 mesh(es) deformed against >= 8"
PASS  still_moves: "the back hair travels 45.881 rig px against the head over the idle, against >= 23"
finished: 2026-10-20T13:39:57Z
