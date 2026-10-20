# Journal — claude-opus-5-5, 03-correct, 2026-10-20

## Entry 1

1. **Read:** task 01's path through AUTHORING §4 (same loader table); `inputs/seethrough.json` for this painting (head_box [538,158,1100,720]); the painting is 1664x2432, same as task 01.
2. **Expect:** `assemble --propose-plan` exits 0 with a plan much like task 01's (same character, same tags).
3. **Chose / turned down:** start a fresh config with `key`, `seethrough` from the inputs and `rig_scale` 0.5 — same reasoning as task 01; turned down copying task 01's config, whose bones belong to the standing painting. Noticed `inputs/pose_seated.json`: it is a `generation.control.skeleton`-shaped pose file (width/height 832x1216, `points` by body-18 name), not the keypoints file `propose --keypoints` reads; I leave it aside for now.
4. **Happened:** exit 0, 22 rows, the same part names as task 01 in a different order (handwear_r drawn after topwear — one hand in the lap, in front of the body); `hairpin` comes from the full run (head run 5 px). As expected.

## Entry 2

1. **Read:** plan output; AUTHORING §4 step 7.
2. **Expect:** `assemble` exit 0 and an `uncovered error px` figure; the bar here is 3,500.
3. **Chose / turned down:** paste plan + extend_below_crop unchanged.
4. **Happened:** exit 0, `uncovered error px: 1726`, 444 holes, the largest 154 px between shoes and legwear. Under 3,500.

## Entry 3

1. **Read:** README *The loop*; README *What it does not do* ("A figure whose joints are not there — reclining, an arm raised, or seated in a skirt that does not start at the hip — needs `propose --keypoints`; sitting alone does not").
2. **Expect:** exit 0, a proposal, maybe LINT lines or notes about the seated pose; the TASK says it will not pass check as proposed, so I expect the failure to show only at build.
3. **Chose / turned down:** run propose plain first to see what the draft and its notes say; turned down converting `pose_seated.json` into a keypoints file before knowing whether it is needed — it is the generation's control skeleton, not something measured off this painting.
4. **Happened:** exit 0 but one LINT line, verbatim in part: `LINT hairback_r and hairback_l on mesh 'hair_back' squeeze it: swung together, every other bone held, edge 37-117 of triangle 167 closes to 0.064 times its rest length at idle frame 22 (max(ratio, 1/ratio) 15.572; <= 1.926544 is required, check's TEXTURE_STRETCH bar) … Their tips are 39.0 px apart and their amplitudes are opposed (hairback_r [0.6, 1.4, 2.4], hairback_l [-0.6, -1.4, -2.4]), so their tips swing towards each other and apart: give both the same sign (then 1.046), or drop one chain`. The overlay (`work/render/landmarks.png`) shows both back-hair chains hanging inside one narrow mass of hair down the middle of her front (the outline reaches y≈690), tips 39 px apart. So the fault is named before the build — the README's round-3 note says `propose` names task 03's fault itself.

## Entry 4

1. **Read:** the LINT line above (its remedy: "give both the same sign (then 1.046), or drop one chain"); TASK.md *Still moves* (back hair must still travel ≥ 23 rig px against the head; *Kept*: eight meshes must stay meshes).
2. **Expect:** with the proposal copied and `hairback_l`'s amps flipped to [0.6, 1.4, 2.4], `propose … --from-config config.json` prints `0 LINT line(s)` and exits 0.
3. **Chose / turned down:** flip the sign of `hairback_l` (keeps both chains and their amplitudes, so the travel stays); turned down dropping one chain (half the hair would follow the other through weights, and a lone chain over a two-chain mesh is a bigger change than the fault), turned down turning the amplitudes down (the task forbids passing by damping motion) and making `hair_back` a region (forbidden by *Kept*).
4. **Happened:** `0 LINT line(s) over 8 mesh(es) and the hip`, exit 0; the loader accepted my `amps_note` beside the value.

## Entry 5

1. **Read:** TASK.md build command; AUTHORING §4 step 9.
2. **Expect:** exit 0, `check: PASS; 10 of 10`, TEXTURE_STRETCH near the 1.046 the LINT line predicted for hair_back (or a higher worst elsewhere), uncovered 1726.
3. **Chose / turned down:** build the corrected config as is.
4. **Happened:** exit 0, `check: PASS; 10 of 10 bar(s) measured, 0 skipped`; hair_back max_ratio 1.045 (the LINT line said 1.046), worst mesh now hair_front 1.126; uncovered 1726; folds 0. As expected.

## Entry 6

1. **Read:** the prompt (grade.py); TASK.md's six lines.
2. **Expect:** 6 of 6 — kept 8 meshes, back hair travel near the TASK's 45.9.
3. **Chose / turned down:** grade now; turned down also building the uncorrected draft to watch it fail — the LINT line already measured the failure (15.572 against 1.926544) and the TASK states it.
4. **Happened:** `6 of 6 line(s)`; kept 8 meshes, back hair travels 45.881 rig px (the TASK's 45.9). As expected.

## At the end

- **What was wrong, and what told me:** the draft keyed the two back-hair chains `hairback_r` and `hairback_l` with opposed amplitudes ([0.6,1.4,2.4] against [-0.6,-1.4,-2.4]) while their tips hang 39 px apart inside one narrow mass of hair, so they swing into each other and crush `hair_back` (edge 37-117 to 0.064 of its length, 15.572 against 1.926544). Decided from `propose`'s LINT line (quoted in entry 3) and confirmed on `work/render/landmarks.png`. Changed: `motion.tracks` → `hairback_l.amps` to [0.6, 1.4, 2.4], nothing else.
- **Where I guessed:** nothing beyond task 01's `key` and `rig_scale`.
- **What I could not find:** what `inputs/pose_seated.json` was for; it was not needed — README says sitting alone does not need `--keypoints`, and its format is not the keypoints file's.
