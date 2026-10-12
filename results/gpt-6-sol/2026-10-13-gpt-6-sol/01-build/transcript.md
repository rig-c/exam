# Transcript — gpt-6-sol, 01-build, 2026-10-13

## 1. Install pinned tools

```sh
npm ci
```

```text
added 5 packages, and audited 6 packages in 2s
1 package is looking for funding
found 0 vulnerabilities
```

## 2. Create staged config

```text
apply_patch: created config.json with key exam-01-build, seethrough resolution 1024,
head_box [616,32,1132,548], and assemble.rig_scale 0.5.
```

## 3. Copy measured plan

```text
apply_patch: added 22 plan rows and two extend_below_crop entries printed by
rig-parts assemble --propose-plan (exit 0; notes []).
```

## 4. Assemble proposed plan

```sh
../../node_modules/.bin/rig-parts assemble --source ../../tasks/01-build/inputs/painting.png --full ../../tasks/01-build/inputs/layers/full --head ../../tasks/01-build/inputs/layers/head --config config.json --out work
```

```text
rig-parts assemble: 22 part(s) on a 832x1216 rig (0.5 rig px per source px), seam rule near-white, projection rule core
recomposite vs source: mean |d|=1.13, within 8: 97.8%, error px > 40: 6275, uncovered error px: 2059
uncovered holes (8-connected): 605, the largest 5 listed
  uncovered hole 1: 402 px at 405,1073 39x25 (between "shoes" 58 px, "legwear" 43 px)
wrote work/rig/parts.json, 22 PNG(s) in work/rig/parts, work/render/recomposite_rig.png, work/render/recomposite_error_rig.png (uncovered error px red, covered error px blue, the painting grey)
```

## 5. Draft rig

```sh
../../node_modules/.bin/rig-parts propose --parts work/rig --source ../../tasks/01-build/inputs/painting.png --out work
```

```text
wrote proposal.json (21 bone entries, 8 meshes) and render/landmarks.png (+_head) under work
0 LINT line(s) over 8 mesh(es) and the hip
coverage: 40 bone(s) — 31 checked and clean, 0 checked with a LINT line, 9 not checked; roles 0 target, 39 deforms, 1 control, 0 unclassified
wrote basis.json (40 bone record(s) by the basis of their origin: 0 joint, 32 mask, 7 ratio, 1 derived) under work
```

## 6. Copy proposal sections

```text
apply_patch: copied bones, meshes, regions, and motion from work/proposal.json
into config.json; JSON parse: 21 bone entries, 8 meshes, 14 regions.
```

## 7. Build from config

```sh
../../node_modules/.bin/rig-parts build --config config.json --source ../../tasks/01-build/inputs/painting.png --full ../../tasks/01-build/inputs/layers/full --head ../../tasks/01-build/inputs/layers/head --out out
```

```text
[assemble] recomposite vs source: mean |d|=1.13, within 8: 97.8%, error px > 40: 6275, uncovered error px: 2059
[check]   TIP_OVER_ROOT: PASS — instrument geometry; parts part handwear_l, root_rig_px 1.404, tip_rig_px 7.052, ratio 5.024 | part handwear_r, root_rig_px 1.36, tip_rig_px 6.914, ratio 5.085 | part bottomwear, root_rig_px 0.268, tip_rig_px 0.983, ratio 3.673; ratio_floor 1.4725
[check]   RECOMPOSITE_HOLES: REPORTED — error_px 6275; uncovered_error_px 2059; hole_count 605; largest px 402, box 405,1073 39x25, borders shoes 58 px | legwear 43 px
[check] check: PASS; 9 of 9 bar(s) measured, 0 skipped
build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from
  out/check/build/skeleton.png
```

## 8. Grade the hand-in

```sh
python3 grade.py runs/2026-10-13-gpt-6-sol-01-build
```

```text
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 2059 against <= 4200"
PASS  does_not_fold: []
4 of 4 line(s); journal present, 0 entry(ies) whose line 4 begins SURPRISE:; log .grade/2026-10-13-gpt-6-sol-01-build/grade.log
```
