# Journal

## Entry 1 (opened 2026-10-25T09:10:43Z)

1. **Read:** AUTHORING.md §4 steps 6–7; tasks/03-correct/inputs/seethrough.json
2. **Expect:** The assembled plan will include the seated figure’s parts and crop extensions
3. **Chose / turned down:** Use the supplied paired layers and box; create the required plan before proposing the rig.
4. **Happened** (2026-10-25T09:11:02Z): config.json: added assemble.plan; the proposal notes both hair parts extend below the crop from the full run.

## Entry 2 (opened 2026-10-25T09:11:09Z)

1. **Read:** AUTHORING.md §4 step 7; seated pose fixture
2. **Expect:** assemble writes parts and reports recomposite coverage and holes
3. **Chose / turned down:** Materialize the proposed plan for the supplied seated painting.
4. **Happened** (2026-10-25T09:11:37Z): recomposite vs source: mean |d|=1.09, within 8: 97.9%, error px > 40: 6164, uncovered error px: 1726; drift: "bottomwear" refuses 21999 px

## Entry 3 (opened 2026-10-25T09:11:43Z)

1. **Read:** AUTHORING.md §4 step 7; pose_seated.json and assembled parts
2. **Expect:** propose writes draft bones, meshes, regions, limbs, and motion and reports seated keypoint bindings
3. **Chose / turned down:** Use coordinates scaled from the supplied pose file, recording that they are intended points rather than measured anatomy.
4. **Happened** (2026-10-25T09:11:56Z): wrote proposal.json (26 bone entries, 6 meshes) and render/landmarks.png (+_head); coverage: 49 bone(s)

## Entry 4 (opened 2026-10-25T09:12:09Z)

1. **Read:** proposal output LINT hairback_r and hairback_l on hair_back: the diagnostic says both signs opposed, and same sign yields 1.046
2. **Expect:** build clears TEXTURE_STRETCH on hair_back after the signs match; other issues may remain
3. **Chose / turned down:** Change only hairback_l from negative to positive amplitudes, preserving magnitudes and all other proposed fields.
4. **Happened** (2026-10-25T09:13:38Z): WTF?: The hair stretch lint is fixed, but build check still fails CHECK_SEAM_WITHIN_BAR for crossed shin cuts and CHECK_TIP_OVER_ROOT for bottomwear driven by chest; both need separate corrections.

## Entry 5 (opened 2026-10-25T09:14:07Z)

1. **Read:** Check output CHECK_SEAM_WITHIN_BAR for crossed shins and CHECK_TIP_OVER_ROOT for chest-driven bottomwear; AUTHORING.md §3 Limbs: Which limb and guide remedy
2. **Expect:** Painting-edge split keeps crossed-leg seam on the visible stroke; dropping chest and increasing skirt amplitudes clears the bottomwear motion ratio
3. **Chose / turned down:** Set leg_l.split to edge painting, remove the explicit chest segment, and test skirt amplitudes [0.5,1,2].
4. **Happened** (2026-10-25T09:15:43Z): WTF?: The painting-edge split reduced the shin seam from 101 to 17 px, but footwear still has 72 seam px; removing chest also exposes hip weights (86 of 114 vertices) and needs the explicit hip segment dropped.

## Entry 6 (opened 2026-10-25T09:15:50Z)

1. **Read:** CHECK_TIP_OVER_ROOT names an explicit hip segment; seam output shows foreground limb split requires edge painting
2. **Expect:** Dropping hip and assigning the painted-edge seam to leg_r clears both remaining setup failures
3. **Chose / turned down:** Remove the hip segment tuple and move the edge split to the other limb candidate; leave the tested movement values unchanged.
4. **Happened** (2026-10-25T09:16:49Z): WTF?: The explicit hip segment is gone and CHECK_TIP_OVER_ROOT no longer reports hip weights, but the ratio is 0.294; the setup seam remains 76 px between feet, above the 50 px bar.

## Entry 7 (opened 2026-10-25T09:16:54Z)

1. **Read:** README.md rule 6 and TASK.md pass lines
2. **Expect:** grader prints current build, check, uncovered error, fold, and mesh movement lines
3. **Chose / turned down:** Grade the corrected hair-sign config and the remaining setup problems as handed in.
4. **Happened** (2026-10-25T09:17:56Z): FAIL  built: "rig-parts build exit 1"; PASS  whole: "uncovered_error_px 1762 against <= 3500"; PASS  still_moves: "the back hair travels 45.881 rig px against the head over the idle, against >= 23"

## At the end (2026-10-25T09:18:00Z)

- **Where I guessed:** I treated pose_seated.json coordinates as keypoints by scaling x2, assigned observed states except occluded hips, chose leg_r as the painted-edge covering limb, and trialled skirt amplitudes [0.5,1,2].
- **What I could not find:** The build still fails TIP_OVER_ROOT and deforms only 6 of 8 required meshes; the seam correction for the crossed footwear and a passing bottomwear binding remain unresolved.
