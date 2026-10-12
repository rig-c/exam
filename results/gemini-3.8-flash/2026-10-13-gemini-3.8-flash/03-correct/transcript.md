# Transcript — gemini-3.8-flash, 03-correct, 2026-10-13

```
$ npx rig-parts assemble --source tasks/03-correct/inputs/painting.png --full tasks/03-correct/inputs/layers/full --head tasks/03-correct/inputs/layers/head --config runs/2026-10-13-gemini-3.8-flash-03-correct/config.json --out work/03-correct
recomposite vs source: mean |d|=1.09, within 8: 97.9%, error px > 40: 6164, uncovered error px: 1726
uncovered holes (8-connected): 444, the largest 5 listed
  uncovered hole 1: 154 px at 321,1077 18x35 (between "shoes" 40 px, "legwear" 21 px)
  uncovered hole 2: 150 px at 353,296 32x24 (between "hair_back" 68 px, "hairpin" 27 px, "handwear_r" 15 px, "topwear" 3 px, "hair_front" 3 px)
  uncovered hole 3: 100 px at 401,1068 9x31 (between "legwear" 24 px, "shoes" 20 px)
  uncovered hole 4: 48 px at 493,518 8x23 (between "handwear_l" 28 px, "bottomwear" 14 px)
  uncovered hole 5: 37 px at 325,103 31x31 (between "hair_back" 63 px)
wrote work/03-correct/rig/parts.json, 22 PNG(s) in work/03-correct/rig/parts, work/03-correct/render/recomposite_rig.png, work/03-correct/render/recomposite_error_rig.png (uncovered error px red, covered error px blue, the painting grey)
```

```
$ npx rig-parts propose --parts work/03-correct/rig --source tasks/03-correct/inputs/painting.png --out work/03-correct
wrote proposal.json (22 bone entries, 8 meshes) and render/landmarks.png (+_head) under work/03-correct
0 LINT line(s) over 8 mesh(es) and the hip
coverage: 45 bone(s) — 37 checked and clean, 0 checked with a LINT line, 8 not checked; roles 0 target, 44 deforms, 1 control, 0 unclassified
wrote basis.json (45 bone record(s) by the basis of their origin: 0 joint, 38 mask, 6 ratio, 1 derived) under work/03-correct
```

```
$ python3 grade.py runs/2026-10-13-gemini-3.8-flash-03-correct
FAIL  built: "rig-parts build exit 1"
FAIL  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "FAIL", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 1726 against <= 3500"
PASS  does_not_fold: []
PASS  kept: "8 mesh(es) deformed against >= 8"
3 of 5 line(s); journal present, 0 entry(ies) whose line 4 begins SURPRISE:; log .grade/2026-10-13-gemini-3.8-flash-03-correct/grade.log
```

```
$ python3 grade.py runs/2026-10-13-gemini-3.8-flash-03-correct
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 1726 against <= 3500"
PASS  does_not_fold: []
PASS  kept: "8 mesh(es) deformed against >= 8"
5 of 5 line(s); journal present, 1 entry(ies) whose line 4 begins SURPRISE:; log .grade/2026-10-13-gemini-3.8-flash-03-correct/grade.log
```



