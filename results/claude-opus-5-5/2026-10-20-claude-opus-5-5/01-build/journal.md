# Journal — claude-opus-5-5, 01-build, 2026-10-20

## Entry 1

1. **Read:** `@rig-c/parts` README *The loop, for an agent*; AUTHORING §4 table (`layers` loader requires `key`, `seethrough`, `assemble.rig_scale`; `--propose-plan` also needs `seethrough.head_box`); AUTHORING §3 `assemble.rig_scale` row ("0.5 in both examples (a 1664x2432 painting makes an 832x1216 rig)"); `inputs/seethrough.json` (resolution 1024, steps 30, seed 42, offload true, head_box [616,32,1132,548]).
2. **Expect:** a `config.json` holding `key`, `seethrough` (copied from inputs/seethrough.json) and `assemble.rig_scale: 0.5`; then `rig-parts assemble --propose-plan` exits 0 and prints a `plan` and `extend_below_crop` as JSON.
3. **Chose / turned down:** rig_scale 0.5 because this painting is the same 1664x2432 size as the examples; turned down 1.0 (no document says the pipeline is calibrated there). Head box taken from seethrough.json rather than re-proposing it, because the head run was already made on that crop and the box must match the crop.
4. **Happened:** exit 0; 22 plan rows (hair_back … hair_front), `extend_below_crop` for `hair_front` and `hair_back` from the full run, and notes naming six empty layers (62–75 px) and `nose` (never planned; head run 1309 px, would give a head pitch reading). As expected.

## Entry 2

1. **Read:** the plan output of entry 1; AUTHORING §4 step 6 ("paste `plan` and `extend_below_crop` into `config.assemble`") and step 7 (`assemble … --out work`, read `uncovered hole` lines).
2. **Expect:** `rig-parts assemble … --out work` exits 0, writes `work/rig/parts.json` and `work/render/recomposite_error_rig.png`, and prints an `uncovered:` line; I expect uncovered error px of a few thousand, maybe under the 4,200 bar.
3. **Chose / turned down:** paste the plan unchanged; turned down adding the `nose` row now — the task asks only for a green check, and a pitch reading is not on the pass lines; I will add it only if propose or check needs it.
4. **Happened:** exit 0, 22 parts on an 832x1216 rig, `uncovered error px: 2059`, 605 holes, the largest 402 px between shoes and legwear. Under the 4,200 bar as hoped. One surprise I note but do not act on: `mouth` is a 141x99 box holding 42 opaque px.

## Entry 3

1. **Read:** README *The loop* (`propose --parts work/rig --source painting.png --out work` → proposal.json, basis.json, landmarks.png; "correct it, copy bones/meshes/regions/motion into config.json").
2. **Expect:** exit 0, `work/proposal.json` with `bones`, `meshes`, `regions`, `motion`, a LINT summary and `coverage` lines.
3. **Chose / turned down:** run propose without `--keypoints` — the figure stands front-on with arms at her sides, the case the screen-y rules are written for; turned down hand-writing keypoints (no estimator here, and the skill says never write a joint you did not get from one).
4. **Happened:** exit 0; 21 bone entries, 8 meshes, `0 LINT line(s) over 8 mesh(es) and the hip`, coverage 31 checked clean / 9 not checked (regions and explicit segments, each with its reason). landmarks.png shows the chains on the art: sleeves down the arms, three skirt chains, bangs and two side locks; legwear is a region on hip. As expected.

## Entry 4

1. **Read:** README *The loop* last step; AUTHORING §4 step 9; TASK.md's exact build command; the overlay `work/render/landmarks.png`.
2. **Expect:** `rig-parts build` exits 0 with a `check: PASS` verdict and the three artifact paths; uncovered error px 2059 again.
3. **Chose / turned down:** copy `bones`, `meshes`, `regions`, `motion` from proposal.json uncorrected (overlay looks right, LINT clean); turned down adding `--loop` because the TASK's command has none and the grader builds without it.
4. **Happened:** exit 0 in 65 s: `check: PASS; 10 of 10 bar(s) measured, 0 skipped`, loop max |d| 0, seam mean 0.117, folds 0, `RECOMPOSITE_HOLES: REPORTED — … uncovered_error_px 2059`. As expected.

## Entry 5

1. **Read:** the prompt ("You may run `python3 grade.py runs/<your run>`").
2. **Expect:** four lines, all PASS (Built, Checked, Whole 2059 ≤ 4200, Does not fold 0).
3. **Chose / turned down:** grade now; turned down further tuning — nothing on the pass lines is near its bar.
4. **Happened:** `4 of 4 line(s)`: built, checked (every bar PASS, holes REPORTED), whole 2059 ≤ 4200, does_not_fold []. It also printed `clock: no started:/finished: lines` because the finished line is written after this run, as the prompt orders.

## At the end

- **Where I guessed:** `key` ("exam-01-build", authored, no source needed). `rig_scale` 0.5 is the examples' value, not derived for this painting — nothing told me how to pick another.
- **What I could not find:** why `mouth` assembles as a 141x99 box holding 42 opaque px; nothing downstream complained.
