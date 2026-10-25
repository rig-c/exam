# Journal

## Entry 1 (opened 2026-10-25T11:30:14Z)

1. **Read:** parts README 'The loop, for an agent' step 3 and AUTHORING §4 step 3: rig-parts layers <dir> prints every layer's box, opaque px, depth; WARN lines for implausible layers
2. **Expect:** exit 0; one line per layer of the full run (29 tags in parts/), several empty ones (neckwear/tail/wings/objects/eyewear ~60-70 px) and maybe a WARN; the union of figure boxes ~ near full 1024 height of the padded square
3. **Chose / turned down:** read the full run's layers to judge the figure's height for rig_scale before anything else; turned down going straight to --propose-plan because rig_scale must be chosen first (AUTHORING §3 'Keep the figure about 1,100 to 1,200 rig px tall')
4. **Happened** (2026-10-25T11:30:27Z): WTF?: exit 0 and '0 WARN line(s)', but most layers print their box as '0,0       1024,1024' (the whole canvas: 'legwear 0,0 1024,1024 ... 51263'), so the layers table does not give the figure's height I wanted for rig_scale; only the arm layers have tight boxes. I'll keep rig_scale 0.5 (2432 px painting -> 1216 rig, figure nearly full height) and read propose's 'mesh spacing' H later

## Entry 2 (opened 2026-10-25T11:30:36Z)

1. **Read:** AUTHORING §4 step 6: 'assemble --propose-plan --source … --full … --head … --config config.json --write-config config.json saves assemble.plan and assemble.extend_below_crop'; read its notes
2. **Expect:** exit 0; a plan of ~20 rows printed as JSON on stdout, changes listed on stderr, notes naming neckwear/tail/wings/objects/eyewear/earwear as empty and nose never planned; config.json gains assemble.plan and extend_below_crop
3. **Chose / turned down:** use --write-config on the config (the documented save form) instead of hand-copying the plan; head_box kept as given in inputs/seethrough.json rather than re-proposed, since the head run was already cut at that box
4. **Happened** (2026-10-25T11:31:00Z): as expected: exit 0, 'added assemble.plan' and 'added assemble.extend_below_crop'; 22 plan rows, hair_front and hair_back continued from the full run, notes name neckwear/tail/wings/objects/eyewear/earwear empty and 'the proposer never plans nose'. Only surprise: headwear (hairpin) taken from the full run ('head run 526 rig px < 0.8 x full run 1516')

## Entry 3 (opened 2026-10-25T11:31:06Z)

1. **Read:** AUTHORING §4 step 7: 'rig-parts assemble … --out work — read its uncovered hole and uncovered: lines and look at work/render/recomposite_error_rig.png'; TASK.md Whole line: uncovered_error_px <= 3,700
2. **Expect:** exit 0; work/rig/parts.json and parts/ written, 22 parts; an 'uncovered:' line with uncovered error px somewhere in the low thousands, maybe a few 'uncovered hole N:' lines (e.g. between the arms and the skirt)
3. **Chose / turned down:** run assemble alone first (not build) so I can read the holes before bones exist; turned down adding the nose row now: nothing in TASK 01 needs the head pitch
4. **Happened** (2026-10-25T11:31:35Z): as expected: exit 0, '22 part(s) on a 832x1216 rig', 'uncovered error px: 1812' (under the 3,700 bar), largest hole 94 px between hair_front/hair_back/topwear; 29 px 'no layer', the rest on a layer below covered alpha — no patch needed

## Entry 4 (opened 2026-10-25T11:31:42Z)

1. **Read:** AUTHORING §4 step 7: 'rig-parts propose --parts work/rig --source inputs/painting.png --out work --write-config config.json' saves bones, meshes, regions, motion and proposed_rig_scale; coverage lines per bone; error map looked at: red only as thin fringes at the hair and hairpin
2. **Expect:** exit 0; work/proposal.json, basis.json, render/landmarks.png; config gains bones/meshes/regions/motion/proposed_rig_scale; a 'mesh spacing' note with H about 1,080 (figure from y~50 to ~1135 on the error map); maybe some LINT lines
3. **Chose / turned down:** plain propose with --write-config; turned down --keypoints (no pose file is given for this painting and the figure is a plain front stand) and --cloth (task 01 asks only for a passing build)
4. **Happened** (2026-10-25T11:31:53Z): exit 0, 'H 1087 rig px' as guessed; config gained bones/meshes/regions/motion/proposed_rig_scale; one LINT I did not expect: 'hairback_r and hairback_l on mesh 'hair_back' squeeze it' (2.455 > 1.926544), fix offered: 'give both the same sign (then 1.051), or drop one chain'

## Entry 5 (opened 2026-10-25T11:32:00Z)

1. **Read:** propose LINT: 'their amplitudes are opposed (hairback_r [0.6, 1.4, 2.4], hairback_l [-0.6, -1.4, -2.4]) … give both the same sign (then 1.051)'; AUTHORING §4 step 8: re-run propose --from-config until it prints no LINT line (exit 0)
2. **Expect:** exit 0, '0 LINT line(s)' — the squeeze reading drops to about 1.051 as the LINT predicted
3. **Chose / turned down:** edited config.json by hand: hairback_l amps flipped to [0.6, 1.4, 2.4] (same sign as hairback_r); turned down dropping one chain, which leaves half the back hair stiff
4. **Happened** (2026-10-25T11:32:18Z): as expected: exit 0, '0 LINT line(s) over 8 mesh(es) and the hip'; 39 checked and clean, 8 not checked (regions and control). (My first python edit missed the hairback_l amps silently — fixed with sed at lines 718-720 before this step ran.)

## Entry 6 (opened 2026-10-25T11:32:18Z)

1. **Read:** TASK.md 01 Do: 'rig-parts build --config config.json --source inputs/painting.png --full … --head … --out out exits 0'; AUTHORING §4 step 9; TASK pass lines: check PASS, uncovered_error_px <= 3,700, render --folds names no mesh (and parts README: since 1.14.0 check reads every animation for folds)
2. **Expect:** exit 0 in about 15-30 s; last lines 'build: PASS — the packed atlas is the artifact' and the pack line; out/check/check.json with uncovered error px 1812 as assemble printed
3. **Chose / turned down:** the exact build command of the TASK, without --loop (the loop encodings are not graded and cost time); turned down adding nose/patches: nothing failed that they would fix
4. **Happened** (2026-10-25T11:33:15Z): as expected: exit 0, 'check: PASS; 11 of 11 bar(s) measured, 0 skipped', 'build: PASS — the packed atlas is the artifact', ANIMATIONS_DO_NOT_FOLD 0 folding mesh(es), uncovered_error_px 1812; build took ~52 s

## Entry 7 (opened 2026-10-25T11:33:15Z)

1. **Read:** README rule 6 and PROMPT: 'python3 grade.py runs/<your run>' rebuilds from config.json on the pinned versions and prints each line
2. **Expect:** exit 0; Built, Checked, Whole (1812 <= 3,700) and Does not fold all PASS; journal chain intact, 6 entries, 1 WTF
3. **Chose / turned down:** grade now; turned down further tuning: nothing on the pass lines is near its bar
4. **Happened** (2026-10-25T11:34:27Z): as expected: '4 of 4 line(s)', 'uncovered_error_px 1812 against <= 3700', 'journal: chain intact, 7 entries, 1 WTF'; the 'clock: no started:/finished: lines' line is because finish has not run yet

## At the end (2026-10-25T11:34:27Z)

- **Where I guessed:** assemble.rig_scale 0.5: chosen before any figure height was printed (layers prints whole-canvas boxes); propose's later 'H 1087 rig px' confirmed it in range. hairback_l amps sign flip: taken from the LINT's own suggestion, not a source on how the back hair should move.
- **What I could not find:** The layers table did not give the figure's height for choosing rig_scale before assemble; nothing said beforehand whether 0.5 would land in the 1,100-1,200 band.
