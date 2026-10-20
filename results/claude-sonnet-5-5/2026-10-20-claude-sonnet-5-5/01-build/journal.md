# Journal — claude-sonnet-5-5, 01-build, 2026-10-20

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry 1

1. **Read:** README.md 'The loop, for an agent' and AUTHORING §3 table rows key/seethrough/assemble.rig_scale, §4 loader table (layers row: key, seethrough, assemble.rig_scale).
2. **Expect:** A config.json holding only key, seethrough (copied from tasks/01-build/inputs/seethrough.json) and assemble.rig_scale 0.5 (the doc's 832x1216 example for a 1664x2432 painting); no run yet, so no output.
3. **Chose / turned down:** Write the minimal config first and run the read-only steps (layers, propose --head-box, assemble --propose-plan) against it. Turned down: writing the whole config at once, because the plan and bones come from commands, not from guessing.
4. **Happened:** config.json written with those three fields.

## Entry 2

1. **Read:** AUTHORING §4 step 6: paste 'plan' and 'extend_below_crop' from assemble --propose-plan into config.assemble; read its notes.
2. **Expect:** config.assemble gets plan (22 parts) and extend_below_crop (hair_front, hair_back); the notes name 7 tags empty/unplanned (neckwear, tail, wings, objects, eyewear, earwear, nose) which are tiny noise layers.
3. **Chose / turned down:** Paste the proposal as is. Turned down: adding the nose row (note says it only buys a head-pitch reading, not needed to build).
4. **Happened:** plan and extend_below_crop written into config.json (22 parts).

## Entry 3

1. **Read:** README loop: 'rig-parts assemble --source … --full … --head … --config … --out work'; AUTHORING §4 step 7: read the uncovered hole lines and recomposite_error_rig.png.
2. **Expect:** exit 0, work/rig/parts.json and parts/, several 'uncovered hole N:' lines; config needs no bones yet.
3. **Chose / turned down:** Run assemble with the proposed plan. Turned down: going straight to build, because holes are only visible in assemble's output.
4. **Happened:** exit 0, 22 parts, 605 uncovered holes of which the largest is 402 px (between shoes and legwear); 'recomposite vs source: ... uncovered error px: 2059', already under the 4,200 Whole bar. As expected, no WTF.

## Entry 4

1. **Read:** README loop and AUTHORING §4 step 7: 'rig-parts propose --parts work/rig --source painting.png --out work' writes proposal.json, basis.json; copy bones/meshes/regions/motion into config.
2. **Expect:** proposal.json with bones, meshes, regions, motion; per-bone coverage lines and LINT lines; notes where it guessed.
3. **Chose / turned down:** Run propose and paste proposal blocks unedited first. Turned down: hand-editing before seeing a failure, since the README says the demo proposal fails at one point and the check will name it.
4. **Happened:** exit 0, proposal.json with 21 bone entries and 8 meshes, 0 LINT lines, 31 bones checked clean, 9 not checked (reasons given). No WTF.

## Entry 5

1. **Read:** README 'The loop': copy bones/meshes/regions/motion from proposal.json into config.json, then 'rig-parts build --config … --out out --loop'; task statement's exact build command.
2. **Expect:** build exits 0 after ~30-60 s; check PASS or a named FAIL (README says the demo's unedited proposal fails at TIP_OVER_ROOT on skirt chains; this skirt may or may not).
3. **Chose / turned down:** Paste the four blocks unedited and build, to learn what actually fails. Turned down: pre-emptively moving the skirt chains as the demo did, since that is a guess about a different painting.
4. **Happened:** exit 0 on the first build with the unedited proposal: check PASS, 10 of 10 bars measured, uncovered_error_px 2059, ANIMATIONS_DO_NOT_FOLD 0 folding. I expected a possible TIP_OVER_ROOT failure; it passed (bottomwear ratio 3.673 vs floor 1.4725). No WTF, only a pleasant miss.

## Entry 6

1. **Read:** README Rules 6: 'python3 grade.py runs/<your run>' is the grader; Task 01 pass lines (Built, Checked, Whole, Does not fold).
2. **Expect:** Four lines passing; it rebuilds from config.json alone, takes up to a minute.
3. **Chose / turned down:** Run the grader now. Turned down: more tuning of the config, since the bars pass.
4. **Happened:** 4 of 4 lines PASS (built, checked, whole 2059 <= 4200, does_not_fold []). Grader also printed 'clock: no started:/finished: lines in transcript.md' because I had not yet appended the finished line when it ran; the started line was there. No WTF.

## At the end

- **Where I guessed:** Nothing written without a source: rig_scale 0.5 came from AUTHORING §3 ('0.5 in both examples'); key 'exam01' is my own name; head_box and the See-through fields were copied from inputs/seethrough.json; everything else was pasted from propose output.
- **What I could not find:** Nothing blocked me. I did not look at contact.png or the recomposite error map (no pictures were read, only the printed lines).
