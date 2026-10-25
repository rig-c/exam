# Journal

## Entry 1 (opened 2026-10-25T08:49:37Z)

1. **Read:** TASK 03 inputs; AUTHORING §4 propose-plan; recorded head_box
2. **Expect:** plan rows and extend_below_crop saved, exit 0
3. **Chose / turned down:** Initial config at documented rig_scale 0.5; derive plan from provided layers
4. **Happened** (2026-10-25T08:49:46Z): exit 0; config added assemble.plan and assemble.extend_below_crop from seated layers

## Entry 2 (opened 2026-10-25T08:49:49Z)

1. **Read:** AUTHORING §4 assemble, proposed seated plan
2. **Expect:** parts generated; uncovered_error_px below 3500; exit 0
3. **Chose / turned down:** Assemble current plan and measure coverage before rig proposal
4. **Happened** (2026-10-25T08:50:07Z): uncovered error px: 1726; drift bottomwear refuses 21999 px but coverage bar is under 3500; exit 0

## Entry 3 (opened 2026-10-25T08:50:11Z)

1. **Read:** AUTHORING §4 propose; seated pose warning says ratios may miss joints
2. **Expect:** proposal written with one or more LINT warnings revealing draft fault; exit 0
3. **Chose / turned down:** Draft from assembled parts without keypoints first to expose tool baseline; inspect basis and warnings
4. **Happened** (2026-10-25T08:50:20Z): exit 0; LINT hairback_r and hairback_l opposed amplitudes squeeze hair_back edge to 0.064 rest length, predicted same sign severity 1.046

## Entry 4 (opened 2026-10-25T08:50:25Z)

1. **Read:** propose LINT: opposed hairback tips 39px apart close triangle to 0.064; same sign predicted 1.046
2. **Expect:** build exit 0, check PASS, 8 meshes and uncovered 1726
3. **Chose / turned down:** Change hairback_l amps from negative to positive without lowering magnitude or making mesh rigid
4. **Happened** (2026-10-25T08:51:07Z): check: PASS; 11 of 11 bar(s) measured, 0 skipped; 8 mesh attachments and uncovered_error_px 1726

## Entry 5 (opened 2026-10-25T08:51:09Z)

1. **Read:** Task 03 six pass lines; corrected build PASS with eight meshes
2. **Expect:** grader prints six PASS including >=23 rig px back hair relative travel
3. **Chose / turned down:** Official grader rebuilds submitted config and measures still_moves rather than infer from amplitudes
4. **Happened** (2026-10-25T08:51:41Z): 6 of 6 line(s); 8 mesh(es) deformed and back hair travels 45.881 rig px against head

## At the end (2026-10-25T08:51:43Z)

- **Where I guessed:** key seated authored; rig_scale 0.5 from AUTHORING, head_box from inputs; tool proposed geometry and motion except changed hairback_l sign while preserving magnitude
- **What I could not find:** No blocking missing guidance: propose LINT named edge 37-117, 0.064 ratio, opposed amplitudes and same-sign fix
