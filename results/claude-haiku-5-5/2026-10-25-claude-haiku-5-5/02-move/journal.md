# Journal

## Entry 1 (opened 2026-10-25T11:36:53Z)

1. **Read:** TASK.md 02 'Do' 1 (a gesture beside the idle, at least 1 s, nothing comes apart) and 2 (hair strands on physics, at least two bones); Pass lines: Trails, Gestures (22 rig px), Holds together, Gesture without folding. AUTHORING.md 'Recipe: cloth and hair that answer the world' (§3 cloth block: per-tag chains/links/wind/gravity). Config: runs/…-02-move/config.json copied from the task 01 config and edited by hand: key exam-02-move; cloth block for 'back hair' and 'front hair'; motion.animations_from 'animations.json'. Step 1 only assembles, with the task 01 plan.
2. **Expect:** exit 0; 22 parts, uncovered_error_px 1812 as task 01 (the plan and painting are unchanged)
3. **Chose / turned down:** Assemble into runs/…-02-move/work to get a fresh work/rig for the cloth proposal. Turned down: reusing task 01's work/rig from another run dir, since the proposal writes work/ beside it.
4. **Happened** (2026-10-25T11:37:48Z): exit 0; it wrote "wrote runs/2026-10-25-claude-haiku-5-5-02-move/work/rig/parts.json, 22 PNG(s)" and the uncovered lines matched task 01 ("uncovered hole 2: 54 px at 447,68" and "no layer ... 29 px in 10 component(s)"). Expected 22 parts and 1812 uncovered: the uncovered_error_px number itself was not in my tail. Note: I piped this run through tail, so only its last six lines reached the terminal; the captured output is in .journal/step-1.out.

## Entry 2 (opened 2026-10-25T11:37:50Z)

1. **Read:** AUTHORING.md 'Recipe: cloth and hair that answer the world': propose --cloth drafts constraints and trees for the 'cloth' tags, and --write-config splices them into the config; without --cloth nothing changes. AUTHORING §4 step 7: propose --parts ... --write-config. Config: runs/…-02-move/config.json with the cloth block from entry 1 line 3 (back hair chains 2, links 3; front hair chains 1, links 3).
2. **Expect:** exit 0; writes constraints (physics on the trailing links) and replaces the back hair and front hair chains with trees; the spliced config holds at least two constraints
3. **Chose / turned down:** Run propose --cloth --write-config on the 02 config, with --out work. Turned down: writing constraints by hand, since the doc says the recipe drafts them and the splice keeps hand-added entries.
4. **Happened** (2026-10-25T11:38:00Z): WTF?: exit 1, not 0. Refused by PROPOSE_WRITE_CONFIG_FRESH: "the config is written to a new file, never over the --cloth config or an earlier one". I had pointed --write-config at the --cloth config itself, which I had not read as a rule (AUTHORING.md's splice section says the output is a new file). Nothing was written; I will write to work/config_cloth.json and copy it over config.json after I check it.

## Entry 3 (opened 2026-10-25T11:38:01Z)

1. **Read:** PROPOSE_WRITE_CONFIG_FRESH refusal in entry 2 close: --write-config must name a new file. AUTHORING 'The config written (issue #537)': the output is the --cloth config's text with the recipe spliced. Writing to runs/…-02-move/work/config_cloth.json; the copy to config.json comes after this check (a separate step).
2. **Expect:** exit 0; the new file work/config_cloth.json holds constraints for hair, and the back hair and front hair chains are trees
3. **Chose / turned down:** Write into work/config_cloth.json, a new path. Turned down: deleting config.json to satisfy the rule, since the file is my own work and the rule is about overwriting.
4. **Happened** (2026-10-25T11:38:41Z): WTF?: exit 1. Refused by PROPOSE_WRITE_CONFIG_CONFLICT: "motion.tracks[5] \"hairback_l\" is the recipe's, and it was changed by hand: it holds amps [0.6,1.4,2.4]". That is my task 01 sign fix, copied into this config; I had not expected the cloth recipe to treat it as a hand edit. The message says to take the draft by removing the hand edit, so I will remove that track entry in config.json (a hand edit, named in the next entry's line 3) and run the write again.

## Entry 4 (opened 2026-10-25T11:38:45Z)

1. **Read:** PROPOSE_WRITE_CONFIG_CONFLICT (entry 3 close): motion.tracks 'hairback_l' is the recipe's and was changed by hand; the message says take the draft by removing the hand edit. I removed the hairback_l track entry from runs/…-02-move/config.json (the hand edit; the recipe now drafts those hair links as physics). AUTHORING 'The config written (issue #537)': an entry equal to neither draft is refused; a removed hand edit is then the recipe's.
2. **Expect:** exit 0; writes work/config_cloth.json with constraints added and the back hair and front hair chains replaced by trees
3. **Chose / turned down:** Run the same propose --cloth write, to the new file work/config_cloth.json. Turned down: keeping the sign fix and forcing the write, since the splice would overwrite it and the recipe replaces that chain anyway.
4. **Happened** (2026-10-25T11:39:14Z): WTF?: exit 0, and it wrote work/config_cloth.json with constraints and trees, but it also printed "2 LINT line(s) over 8 mesh(es) and the hip": "LINT hairback_r0_, hairback_r1_ on mesh 'hair_back' (side r): 2 tree(s) for 1 visible hair mass(es)" and the same for the left side. I had set back hair chains 2 meaning two trees, and did not expect one visible hair mass per side. The note on the output also says the animations_from path resolves beside the written file, so the written config must sit beside config.json.

## Entry 5 (opened 2026-10-25T11:39:32Z)

1. **Read:** Entry 4 close: LINT '2 tree(s) for 1 visible hair mass' per side for back hair chains 2. AUTHORING recipe: 'trees' rule, 'chains' per side; the LINT message says draft one tree per visible hair mass. I hand-edited runs/…-02-move/config.json cloth 'back hair' chains 2 -> 1 (the input config, not yet spliced). Writing the new spliced config to a fresh path work/config_cloth_b.json (PROPOSE_WRITE_CONFIG_FRESH: never over an earlier one).
2. **Expect:** exit 0; no LINT for hair_back trees; the same constraints and track removals as entry 4 with one tree per side
3. **Chose / turned down:** Re-run the write from config.json to work/config_cloth_b.json, then copy it over config.json as the next step. Turned down: writing over work/config_cloth.json, which the tool refuses; and keeping two trees, since the lint names the fault.
4. **Happened** (2026-10-25T11:39:49Z): exit 0; it printed "0 LINT line(s) over 8 mesh(es) and the hip" and "coverage: 42 bone(s) — 35 checked and clean, 0 checked with a LINT line, 7 not checked", and wrote work/config_cloth_b.json. The LINT went away with one tree per side, which matched the line the tool gave me in entry 4. Next I will copy config_cloth_b.json over config.json so animations_from resolves beside it.

## Entry 6 (opened 2026-10-25T11:39:55Z)

1. **Read:** Copied work/config_cloth_b.json over runs/…-02-move/config.json (spliced by propose --cloth, entry 5), so config.json now holds the cloth block, 23 constraints, the trees, and motion.animations_from 'animations.json' beside it. AUTHORING §4 step 8: propose --from-config re-lints every chain link and exit 1 while a LINT remains.
2. **Expect:** exit 0 with 0 LINT lines and a coverage summary with the hair tree bones clean
3. **Chose / turned down:** Run propose --from-config with --out work. Turned down: building first, since step 8 is the doc's order and the build's own check would print the same LINT later.
4. **Happened** (2026-10-25T11:40:07Z): exit 0; it printed "0 LINT line(s) over 8 mesh(es) and the hip" and "coverage: 42 bone(s) — 35 checked and clean, 0 checked with a LINT line, 7 not checked". Expected 0 LINT; matched. The 7 not-checked bones are the same region-bound and control bones as task 01.

## Entry 7 (opened 2026-10-25T11:40:09Z)

1. **Read:** TASK.md 02 pass lines (Trails: physics on at least 2 bones and green; Gestures: animation other than idle, at least 1 s, face travel >= 22 rig px from bottomwear middle). AUTHORING §4 step 9: build (assemble, rig, check; the animations file is read by the rig stage). Config: runs/…-02-move/config.json (cloth spliced, animations_from 'animations.json' hand-written in run dir, read here for the first time).
2. **Expect:** exit 0; check: PASS with 11 of 11 bars; a gesture animation named 'gesture' listed beside idle; possible TEXTURE_STRETCH or CHAIN_LAG notes from the new hair chains
3. **Chose / turned down:** Run the exact task command, without --loop, to runs/…-02-move/out. Turned down: --loop, since the pass line is the task's own command.
4. **Happened** (2026-10-25T11:41:36Z): exit 0; "[check] check: PASS; 11 of 11 bar(s) measured, 0 skipped; 0 warning(s) (CLOTH_SETTLES, not a bar)" and "pages=22 regions=22 bones=61 slots=22 animations=2 ... physicsConstraints=23". Expected a gesture animation beside idle and physics on the hair; both appear ("animations beside the idle, from …/animations.json as written: gesture"). ANIMATIONS_DO_NOT_FOLD: "2 animation(s) read by rigc render --folds … 0 folding mesh(es)". The face travel and seam holds are not in this output; the grader reads them.

## Entry 8 (opened 2026-10-25T11:41:38Z)

1. **Read:** TASK.md 02 pass lines: Gestures = face furthest vertex travels >= 22 rig px from the middle of bottomwear over an animation other than idle, >= 1 s; Holds together = rigc render --seam over that animation at 12 fps; Gesture without folding = rigc render --folds names no mesh. Grader is the proctor's same grader (README rule 'You may run grade.py whenever you like').
2. **Expect:** PASS built; PASS checked (or REPORTED RECOMPOSITE_HOLES); whole 1812 <= 3700; does_not_fold []; Trails and Gestures lines possibly failing if the head-turn reads under 22 px, in which case I would scale the gesture
3. **Chose / turned down:** Run grade.py on the 02 run dir. Turned down: measuring face travel myself first, since the grader reads the same values and the journal is for grader results.
4. **Happened** (2026-10-25T11:43:49Z): WTF?: the grader printed "FAIL  holds_together: {\"opens\": {\"topwear|handwear_l\": {\"frames\": 13, \"max_px\": 40}}" while built, checked, whole, does_not_fold, trails and gestures passed ("gestures: \`gesture\`: \`face\` travels 33.5 rig px\"). I expected the gesture to hold; the seam ghost opens at the gesture's peak (frames 6 to 18 of seam.json, around t = 1 s) at the left arm and topwear. The count of opening frames printed 13 and the largest 40 px, against a box of 12 to 19 cells. I had not expected a torso lean and lowering to open the upper arm this much.

## Entry 9 (opened 2026-10-25T11:44:00Z)

1. **Read:** Entry 8 close: holds_together FAIL at topwear|handwear_l, seam ghost peak at gesture t ~1 s. Hypothesis (not a measurement): the chest translatey -6 is the part that moves the sleeve chain and the chest mesh apart, since topwear's hip segment does not move. I hand-edited runs/…-02-move/animations.json: removed the chest translatey track (keeps head rotate -8 and chest rotate -3). The gesture must still give face travel >= 22 px (TASK.md Gestures line).
2. **Expect:** holds_together PASS (no frames opening); gestures travel below the 33.5 of entry 8 but still at least 22; if gestures fails, the lean alone is not enough
3. **Chose / turned down:** Re-run the grader with the trimmed gesture. Turned down: a larger head turn to make up the travel, since that also moves the face on the seam pair and I would be changing two things at once.
4. **Happened** (2026-10-25T11:45:19Z): WTF?: the trimmed gesture is still not clean. holds_together: "{\"opens\": {\"topwear|handwear_l\": {\"frames\": 1, \"max_px\": 12}}"; the opening went from 13 frames and 40 px to 1 frame and 12 px, so removing the chest lowering was most of the cause but not all. gestures "travels 30.3 rig px", against the 22 bar. My expectation was a clean pass; the remaining one-frame opening was not in my expectation.

## Entry 10 (opened 2026-10-25T11:45:42Z)

1. **Read:** Entry 9 close: the chest lowering was most of the seam opening; one frame at 12 px remains with chest rotate -3. I hand-edited animations.json again: head rotate -8 -> -14 (to hold the 22 px face travel), chest rotate -3 -> -1 (the chest turn that moves the sleeve chain and topwear apart). TASK.md Gestures: face travel >= 22 rig px from the middle of bottomwear.
2. **Expect:** holds_together PASS (no frame opens); gestures >= 22 px (the head turn carries most of the travel); folds still 0
3. **Chose / turned down:** Re-run the grader. Turned down: keeping head -8 and dropping the chest turn altogether, since -1 keeps a lean the task names and the test is whether the small chest turn is clean.
4. **Happened** (2026-10-25T11:46:56Z): exit 0; grader printed "PASS  holds_together: {\"opens\": {}, \"not_read\": []" and "8 of 8 line(s)". Expected holds_together PASS and face travel >= 22. Holds and gestures passed; face travel was "35.1 rig px", more than my estimate of about 26, so the head turn did more than I had worked out. The journal chain is intact ("journal: chain intact, 10 entries, 5 WTF").

## At the end (2026-10-25T11:59:38Z)

- **Where I guessed:** Gesture numbers: head rotate -8 then -14 and chest -3 then -1, chosen by trial against the seam and the 22 px bar. Only the 22 px and 'at least 1 s' came from the task; the joint keys and the key times (0, 1, 2 s) are mine. I did not measure face travel before the first grader run; the grader's 33.5 and 35.1 are the only figures I have.
- **What I could not find:** Why the chest translatey (-6) opened the topwear|handwear_l seam: the grader names the pair and the frames, not the cause; I inferred it from removing one track at a time, not from the seam picture. The rigc render --seam picture itself I did not open.
