## `rigc build --rig` refused the rig directory
- **I was trying to:** build the retargeted motion with the same `--rig` I had given `rig-pose retarget`.
- **The tool gave me:** `rigc compile error: cannot read …/inputs/rig: EISDIR: illegal operation on a directory, read (see rigc guide CE_COMPILE_JSON_READ_FAILED)`
- **What would have helped:** accept a directory holding rig.json (as retarget does), or "--rig is a rig.json file; …/inputs/rig is a directory, did you mean …/inputs/rig/rig.json?"
- **Cost:** a minute; got there.

## No hint that the translate scale's segment foreshortens
- **I was trying to:** pick `translate.scale` so the hip's travel is in proportion to the rig.
- **The tool gave me:** `SCALE  1.60049 rig units per picture px (rig 485.19 / pose median 303.15)` — and the README's "Pick a long segment that does not foreshorten much."
- **What would have helped:** a line saying the pose segment's median is 0.76 of its 95th percentile (it foreshortens), and the hip's vertical/horizontal range in leg lengths and hip widths, pose beside rig, as POSTURE already does for tilt and sway.
- **Cost:** two retarget/render/grade rounds (~3 minutes); got there by measuring.

## `reach: true` costs jitter and nothing says so
- **I was trying to:** find why trunk+head jitter was 1.39–1.48× the sequence's.
- **The tool gave me:** `LAND bone "chest" aim — worst |reached − asked| 0.000822°` (it lands) and the README's recommendation of `reach` for a tilting pelvis; no jitter reading per bone.
- **What would have helped:** a per-bone rotation-jitter reading (rig vs the map's joint pair), or a README sentence that `reach` re-aims from the bobbing hip and adds rotation the pose does not have.
- **Cost:** wrote a per-bone script (~2 minutes); got there.

## LEG-SCALE's floor moves the free foot, silently
- **I was trying to:** find why the lifted foot was 1.3× higher than the picture's.
- **The tool gave me:** `LEG-SCALE chain "leg_r" bone "leg_r1" … picture length ÷ straight 0.089 … 1.036 … 110 frame(s) under 0.8, clamped` and `STANCE lifted: … the pose's height kept` (it was not kept: the clamp changed it).
- **What would have helped:** on clamped frames of a free leg, the foot's height vs the picture's in leg lengths ("free ankle 0.29 leg lengths above the picture's"), and that the 0.8 floor is the walk card's.
- **Cost:** one script and one rerun (~2 minutes); got there.

## SHEAR reads the squashed foot but not the fix
- **I was trying to:** stop the boots being squashed under the scaled shins.
- **The tool gave me:** `SHEAR  bone "foot_r": art sheared up to 78.08° (frame 173); … a scaled bone, or one under it; a reading`
- **What would have helped:** "a bone under a scaled one takes its scale unless its inherit is onlyTranslation / noScale" on that line.
- **Cost:** a grep in rig-c AUTHORING.md and one rerun (~2 minutes); got there.

## @rig-c/pose's only document is a 120 KB README
- **I was trying to:** read the retarget's flags and the map format; PROBLEM.md says each package's `docs/AUTHORING.md` is the source of truth.
- **The tool gave me:** no `docs/` in @rig-c/pose; README lines several KB long that truncated in a terminal.
- **What would have helped:** a docs/ split (map, legs, report fields) or the README's section index in `--help`.
- **Cost:** a few minutes of paging; got there.
