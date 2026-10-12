# Transcript — gpt-6-sol, 03-correct, 2026-10-13

## 1. Create staged config

```text
apply_patch: created config.json with key exam-03-correct, seethrough resolution
1024, head_box [538,158,1100,720], and assemble.rig_scale 0.5.
```

## 2. Copy proposed plan

```text
apply_patch: added the 22 rows and two hair extensions printed by
assemble --propose-plan. Its note said: headwear: head run 5 rig px < 0.8 x
full run 2146 -> full-run layer, drawn behind the face.
```

## 3. Assemble the proposed plan

```sh
../../node_modules/.bin/rig-parts assemble --source ../../tasks/03-correct/inputs/painting.png --full ../../tasks/03-correct/inputs/layers/full --head ../../tasks/03-correct/inputs/layers/head --config config.json --out work
```

```text
rig-parts assemble: 22 part(s) on a 832x1216 rig (0.5 rig px per source px), seam rule near-white, projection rule core
recomposite vs source: mean |d|=1.09, within 8: 97.9%, error px > 40: 6164, uncovered error px: 1726
uncovered holes (8-connected): 444, the largest 5 listed
  uncovered hole 1: 154 px at 321,1077 18x35 (between "shoes" 40 px, "legwear" 21 px)
wrote work/rig/parts.json, 22 PNG(s) in work/rig/parts, work/render/recomposite_rig.png, work/render/recomposite_error_rig.png (uncovered error px red, covered error px blue, the painting grey)
```

## 4. Draft the seated rig

```sh
../../node_modules/.bin/rig-parts propose --parts work/rig --source ../../tasks/03-correct/inputs/painting.png --out work
```

```text
wrote proposal.json (22 bone entries, 8 meshes) and render/landmarks.png (+_head) under work
0 LINT line(s) over 8 mesh(es) and the hip
coverage: 45 bone(s) — 37 checked and clean, 0 checked with a LINT line, 8 not checked; roles 0 target, 44 deforms, 1 control, 0 unclassified
wrote basis.json (45 bone record(s) by the basis of their origin: 0 joint, 38 mask, 6 ratio, 1 derived) under work
```

## 5. Copy uncorrected proposal sections

```text
apply_patch: copied proposal bones, meshes, regions, and motion into config.json
without corrections (22 bone entries; 8 meshes).
```

## 6. Baseline build, before correction

```sh
../../node_modules/.bin/rig-parts build --config config.json --source ../../tasks/03-correct/inputs/painting.png --full ../../tasks/03-correct/inputs/layers/full --head ../../tasks/03-correct/inputs/layers/head --out out
```

```text
[rig]   bones 84 (37 control) slots 22 meshes 8 regions 14 vertices 508; idle 3.3333333333333335 s, 41 track(s), 363 key(s)
[check]   TEXTURE_STRETCH: FAIL — meshes 8; triangles 722; frames 41; severity 15.338; severity_ceiling 1.926544; worst slot hair_back, triangle 167, vertices 115 | 37 | 117, edge 37 | 117, frame 22, ratio 0.065
[check]   FAIL  CHECK_TEXTURE_STRETCH: mesh "hair_back" triangle 167 (vertices 115 37 117), edge 37-117, idle frame 22 — the edge is 0.065 times its rest length (max(ratio, 1/ratio) 15.338); <= 1.926544 is required — the texture on it is squeezed: the bones this mesh is weighted to move apart (amplitudes too large down a chain), or a vertex blends bones that move against each other
[check] check: FAIL — 1 bar(s) not met; 9 of 9 bar(s) measured, 0 skipped
build: stopped at check; 1 bar(s) not met, so no loop was encoded and no artifact is reported
```

## 7. Reduce the two opposing back-hair chain amplitudes

```text
apply_patch: changed hairback_r amps [0.6,1.4,2.4] to [0.15,0.35,0.6]
and hairback_l amps [-0.6,-1.4,-2.4] to [-0.15,-0.35,-0.6].
```

## 8. Rebuild after the isolated correction

```sh
../../node_modules/.bin/rig-parts build --config config.json --source ../../tasks/03-correct/inputs/painting.png --full ../../tasks/03-correct/inputs/layers/full --head ../../tasks/03-correct/inputs/layers/head --out out
```

```text
[rig]   bones 84 (37 control) slots 22 meshes 8 regions 14 vertices 508; idle 3.3333333333333335 s, 41 track(s), 363 key(s)
[check]   TEXTURE_STRETCH: PASS — meshes 8; triangles 722; frames 41; severity 1.303; severity_ceiling 1.926544; worst slot hair_back, triangle 167, vertices 115 | 37 | 117, edge 37 | 117, frame 22, ratio 0.768
[check]   RECOMPOSITE_HOLES: REPORTED — error_px 6164; uncovered_error_px 1726; hole_count 444; largest px 154, box 321,1077 18x35, borders shoes 40 px | legwear 21 px
[check] check: PASS; 9 of 9 bar(s) measured, 0 skipped
build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from
  out/check/build/skeleton.png
```

## 9. Grade the final hand-in

```sh
python3 grade.py runs/2026-10-13-gpt-6-sol-03-correct
```

```text
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 1726 against <= 3500"
PASS  does_not_fold: []
PASS  kept: "8 mesh(es) deformed against >= 8"
5 of 5 line(s); journal present, 0 entry(ies) whose line 4 begins SURPRISE:; log .grade/2026-10-13-gpt-6-sol-03-correct/grade.log
```
