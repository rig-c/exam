# Journal

## Entry 1 (opened 2026-10-25T11:49:47Z)

1. **Read:** fixtures/mannequin/README 'The joints' (bones: hip, chest, head, sleeve_*0 shoulder, sleeve_*1 elbow ±45, hand_* wrist ±45; 'Move or dip hip and the feet stay put' — iks leg_*_ik on foot_*_tgt under root; 'A positive sleeve_r0 lowers the right arm and a positive sleeve_l0 raises the left'); TASK 05: 4.0 s at 120 bpm; AUTHORING recipe for animations_from (spec rigc-motion/1, last key at duration)
2. **Expect:** exit 0; '[rig] animations beside the idle … as written: dance'; 'check: PASS; 10 of 14 bar(s) measured, 4 skipped' (FEET_STAY_LEVEL now measured, as the TASK says); ANIMATIONS_DO_NOT_FOLD reads idle and dance with 0 folding
3. **Chose / turned down:** config.json = the fixture's with motion.animations_from 'dance.json'; dance.json written by my generator (scratchpad make_dance.py): keys every 1/24 s from functions periodic in 4 s — hip bounce low on every beat (y -6..-20, never above rest, because both legs are straight at rest: root-to-ankle 488.0 px = thigh+shin), hip sway x ±12 and rotate ±3 over two beats, chest ±5 and head ±8 counter-swing, arms pumping alternately on beats 1 and 2 (shoulder up to 43°, elbow 38°, wrist 20° plus a ±8 flick each beat), arm reach swelling over the 8-beat phrase. Built in work/fx beside a symlink to the fixture's caps/. Turned down keying the legs with ik mix 0: the iks already plant the feet
4. **Happened** (2026-10-25T11:50:54Z): as expected on the bars: 'check: PASS; 10 of 14 bar(s) measured, 4 skipped', FEET_STAY_LEVEL PASS on (idle, dance), '(idle, dance): 0 folding mesh(es)'; not expected: 'SEAM_OVER_MOTION: WARN — 9 declared pair(s) … 5 warning(s), never a bar' — some joints open during the dance

## Entry 2 (opened 2026-10-25T11:51:08Z)

1. **Read:** check.json SEAM_OVER_MOTION rows for dance: 'thigh_l|shin_l … opens [0, 12, 24, 36, 48] max_px 43', neck|head up to 9, right wrist 6, elbows 3-4 (warnings, never a bar)
2. **Expect:** exit 0; frames at 512 px; at f0000 the left knee (image right) bent ~36° by my t=0 pose (dip 20 + hip sway +12 toward that leg + hip rotate -3 all shorten it at once) shows a gap or ghost at the knee ball; the other knee clean
3. **Chose / turned down:** render dance at 12 fps --max 512 with --seam on the left knee only and look at f0000 and f0006; turned down changing the motion before seeing what the 43 px is
4. **Happened** (2026-10-25T11:51:23Z): WTF?: not only at the beats — 'opens on 49 of 49 frame(s)', a ghost on every frame ('ghost on 49 frame(s) [0-48], worst frame 0 … 43 px … (37.00 × 10.00)'), so the left knee shows its ghost whenever it bends at all, not just at my deepest pose; the knee's ±45 range (README) did not tell me the strict reader opens well inside it

## Entry 3 (opened 2026-10-25T11:51:36Z)

1. **Read:** TASK 05 pass lines (Dance as timed, Closes, Both hands >= 100, Whole body >= 15 from the feet' middle, On its feet <= 6, Keeps time >= half the speed variation on a two-beat period, no fold); contact sheet of dance viewed: the figure bounces, sways and pumps the arms, feet fixed
2. **Expect:** all machine lines PASS (arms SKIP as TASK says): closes ~0 px (boundary key = first key), hands well over 100 (shoulder 36-43° on a ~330 px arm), topwear travel ~25-30, shins on the feet (feet are children of the shins), keeps time high since every track but the arm-reach envelope repeats every 1 s
3. **Chose / turned down:** grade before polishing the knee ghost, which is a warning and no bar; the grader builds the run dir's config.json + dance.json on the fixture itself
4. **Happened** (2026-10-25T11:54:46Z): WTF?: every line passes ('11 of 11 line(s), 3 skipped', keeps_time '0.922', whole_body '31.8 rig px', hands 440.5/459.7) but on_her_feet is close to its bar — 'the end of a leg (shin_l, shin_r) gets 5.04 rig px from where it meets foot_l, foot_r, against <= 6.0' — where I expected ~0 because the feet are children of the shins; I now think the foot, inheriting no rotation (README: 'inherit noRotationOrReflection'), stays level while the shin turns, so the meeting point drifts with the knee bend

## Entry 4 (opened 2026-10-25T11:54:55Z)

1. **Read:** grade: on_her_feet 5.04 of 6.0 at my deepest knee bend; check.json: left knee ghost 43 px at the beat (SEAM_OVER_MOTION warning); README Known limits: knees hold at <= 6 px on the strict reader at ±45 — but the dance's knee is bent by the ik, not keyed
2. **Expect:** exit 0, check PASS 10 of 14; thigh_l|shin_l ghost smaller than 43 px (still on most frames, the leg is never straight now); fewer than 5 SEAM_OVER_MOTION warnings or the same 5 with smaller max px
3. **Chose / turned down:** shallower bounce (hip y -5..-14, was -6..-20), sway ±10 (was ±12), hip rotate ±2 (was ±3): the knee bends ~30° at most instead of ~36°, still never straight (min dip 5 > 1.1 sway + 1.4 rotate lengthening). Turned down keying ik mix 0 to pose the legs by hand: more to get wrong, and the iks are what plants the feet
4. **Happened** (2026-10-25T11:56:47Z): partly: 'check: PASS; 10 of 14 bar(s) measured', still '5 warning(s)'; from check.json the left knee eased only a little (43 -> 39 px, still 5 frames, the beats), neck 9 -> 7 px over 8 frames, right wrist 6 -> 8 px. The knee ghost looks structural (it opens on whichever frame bends it most); I keep this bounce

## Entry 5 (opened 2026-10-25T11:56:47Z)

1. **Read:** grade.py, after the shallower bounce
2. **Expect:** 11 of 11 PASS again; on_her_feet under 5.04 (about 4), whole_body lower than 31.8 (about 26), keeps_time still ~0.9
3. **Chose / turned down:** grade this version as the hand-in candidate; turned down further cutting the bounce: it is the beat the judge has to see
4. **Happened** (2026-10-25T11:58:44Z): WTF?: all pass ('11 of 11 line(s), 3 skipped', on_her_feet down to '3.96 rig px', keeps_time '0.928') but whole_body fell far more than I reckoned: 'the vertex of topwear that travels least travels 17.2 rig px' (was 31.8) for a sway cut only 12 -> 10 and a bounce 14 -> 9 deep; the least-travelling vertex must sit where the chest's counter-rotation cancels the hip's shift, so the margin to 15 is thin. Kept: it passes, and the deeper bounce cost the knees

## At the end (2026-10-25T11:58:45Z)

- **Where I guessed:** Every amplitude in dance.json is mine: bounce depth, sway ±10, hip ±2°, chest ±5°, head ±8°, shoulder 36° x (0.8-1.2), elbow 38°, wrist 20° and an 8° flick; the phrase envelope over 4 s. Signs from the README's 'Signs' sentence (positive sleeve_r0 lowers the right arm, positive sleeve_l0 raises the left); the elbow's bend sign by reasoning (same sign as the raise), confirmed only by eye on the contact sheet.
- **What I could not find:** Which way each elbow/wrist sign bends relative to the body (the README gives the shoulders only); whether the strict seam reader's knee ghost on a bent ik leg should be avoided or is expected; how the feet's 'noRotationOrReflection' moves the shin-foot meeting point (on_her_feet read 5.04 at a 36° knee).
