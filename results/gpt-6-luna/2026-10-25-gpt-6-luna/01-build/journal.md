# Journal

## Entry 1 (opened 2026-10-25T08:58:52Z)

1. **Read:** AUTHORING.md §4 steps 6–7; TASK.md Given
2. **Expect:** assemble --propose-plan writes plan and notes; exit 0
3. **Chose / turned down:** Use the supplied full/head layers and source painting with the recorded head box; no external See-through run is needed.
4. **Happened** (2026-10-25T08:59:00Z): WTF?: It refused because seethrough.steps, seed, and offload were required; I copied only resolution and head_box from the fixture.

## Entry 2 (opened 2026-10-25T08:59:05Z)

1. **Read:** AUTHORING.md §3 seethrough fields; tasks/01-build/inputs/seethrough.json
2. **Expect:** assemble --propose-plan writes the plan and reports omitted layers
3. **Chose / turned down:** Retry the same operation with all recorded See-through metadata required by the loader.
4. **Happened** (2026-10-25T08:59:34Z): It added assemble.plan and assemble.extend_below_crop; the headwear note says full-run layer, drawn behind the face.

## Entry 3 (opened 2026-10-25T08:59:37Z)

1. **Read:** AUTHORING.md §4 step 7
2. **Expect:** assemble writes work/rig and recomposite reports holes with exit 0
3. **Chose / turned down:** Materialize the proposed plan to work for the next proposal stage.
4. **Happened** (2026-10-25T09:00:22Z): recomposite vs source: mean |d|=1.09, within 8: 97.6%, error px > 40: 7465, uncovered error px: 1812

## Entry 4 (opened 2026-10-25T09:00:45Z)

1. **Read:** AUTHORING.md §3 A posed figure and §4 step 7
2. **Expect:** propose writes bones, meshes, regions, limbs, motion and reports geometry findings
3. **Chose / turned down:** Supply explicitly eye-estimated keypoints because the task has no keypoint file; record that their positions are approximations.
4. **Happened** (2026-10-25T09:00:55Z): wrote proposal.json (23 bone entries, 6 meshes) and render/landmarks.png (+_head) under runs/2026-10-25-gpt-6-luna-01-build/work; coverage: 45 bone(s)

## Entry 5 (opened 2026-10-25T09:00:58Z)

1. **Read:** TASK.md pass lines and AUTHORING.md §4 step 9
2. **Expect:** build exits 0 and reports a check verdict; uncovered_error_px <= 3700
3. **Chose / turned down:** Run the required build directly from the proposed config; treat any refusal or red gate as evidence to correct.
4. **Happened** (2026-10-25T09:01:33Z): WTF?: ASSEMBLE_LIMB_JOINT_ON_ART refused sleeve_r1 because the estimated elbow [290, 390] is 15.952 px from the nearest arm art; the visual estimate was too far off the joint line.

## Entry 6 (opened 2026-10-25T09:01:38Z)

1. **Read:** assemble refusal ASSEMBLE_LIMB_JOINT_ON_ART; AUTHORING.md §3 posed figure
2. **Expect:** propose replaces the limb elbow positions with estimates on sleeve art and writes config
3. **Chose / turned down:** Shift both elbow joints to the layer landmarks nearest their drawn joints, then regenerate the proposal.
4. **Happened** (2026-10-25T09:01:55Z): config.json: replaced bones; wrote proposal.json (23 bone entries, 6 meshes)

## Entry 7 (opened 2026-10-25T09:01:58Z)

1. **Read:** TASK.md pass lines; previous ASSEMBLE_LIMB_JOINT_ON_ART refusal and corrected elbow estimates
2. **Expect:** build gets past assemble and prints check verdict or next named refusal
3. **Chose / turned down:** Rebuild with regenerated bones and the unchanged proposed plan, meshes, and layers.
4. **Happened** (2026-10-25T09:03:14Z): WTF?: The build reached check but failed CHECK_TIP_OVER_ROOT on bottomwear and CHECK_TEXTURE_STRETCH on hair_back; the proposal needs correction before it can pass.

## Entry 8 (opened 2026-10-25T09:03:26Z)

1. **Read:** AUTHORING.md §6 CHECK_TIP_OVER_ROOT and CHECK_TEXTURE_STRETCH; build output
2. **Expect:** Removing the chest mesh segment and aligning hairback chain signs clears both named failures
3. **Chose / turned down:** Apply the documented remedies directly in config: drop chest from bottomwear segments and give both back-hair chains the same sign.
4. **Happened** (2026-10-25T09:04:44Z): WTF?: CHECK_TEXTURE_STRETCH cleared, but CHECK_TIP_OVER_ROOT now says the mesh is weighted off-chain to hip (29 of 84 vertices); the segment removal exposed hip as the remaining binding.

## Entry 9 (opened 2026-10-25T09:04:51Z)

1. **Read:** CHECK_TIP_OVER_ROOT refusal from prior build; AUTHORING.md §6 remedy
2. **Expect:** Dropping hip from bottomwear segments clears the remaining TIP_OVER_ROOT bar
3. **Chose / turned down:** Remove the hip segment as the refusal explicitly directs, preserving the three skirt chains.
4. **Happened** (2026-10-25T09:06:00Z): WTF?: CHECK_TIP_OVER_ROOT still finds hip weights because hip is declared as an explicit [bone, from, to] segment, not the string hip; my filter only removed strings.

## Entry 10 (opened 2026-10-25T09:06:05Z)

1. **Read:** CHECK_TIP_OVER_ROOT output and the exact segments array in config.json
2. **Expect:** Removing the explicit hip segment by bone name clears the last bar
3. **Chose / turned down:** Drop the full explicit hip segment tuple from bottomwear.segments and rebuild.
4. **Happened** (2026-10-25T09:07:12Z): WTF?: Removing hip influence changed the ratio but the lower half still travels less than the upper (1.941 versus 3.368 px); the refusal now points to larger skirt-chain amplitudes.

## Entry 11 (opened 2026-10-25T09:07:19Z)

1. **Read:** CHECK_TIP_OVER_ROOT output; AUTHORING.md §6 named remedy
2. **Expect:** Larger skirt-chain amplitudes will make lower-half tip travel exceed the moving root by the required ratio
3. **Chose / turned down:** Raise each skirt chain to [1, 2, 4] degrees and rebuild; this is a trial value not specified by the docs.
4. **Happened** (2026-10-25T09:08:24Z): WTF?: The larger amplitudes scaled travel up (11.466 and 19.981 px) but left the ratio at 0.574, so CHECK_TIP_OVER_ROOT remains red; no package message explains how to reverse the measured upper/lower response.

## Entry 12 (opened 2026-10-25T09:08:26Z)

1. **Read:** README.md rule 7 and TASK.md pass lines
2. **Expect:** grade.py prints the task’s current lines, including the red CHECK_TIP_OVER_ROOT status
3. **Chose / turned down:** Grade this honest partial configuration before ending the task.
4. **Happened** (2026-10-25T09:09:07Z): FAIL  built: "rig-parts build exit 1"; PASS  whole: "uncovered_error_px 1816 against <= 3700"; PASS  does_not_fold: []

## At the end (2026-10-25T09:09:09Z)

- **Where I guessed:** I estimated all keypoint coordinates from the displayed painting; the elbow corrections, trial skirt amplitudes [1,2,4], and arm joint choices are not documented values.
- **What I could not find:** The docs say to grow chain amplitudes toward the tip but do not explain why this figure keeps the lower-half travel ratio at 0.574 or how to reverse it without guessing.
