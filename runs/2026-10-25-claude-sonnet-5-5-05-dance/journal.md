# Journal

## Entry 1 (opened 2026-10-25T11:49:44Z)

1. **Read:** fixtures/mannequin/README.md ('The joints' table: bones, signs, ranges; 'Feet are planted by the rig'); tasks/05-dance/TASK.md pass lines; AUTHORING §3 recipe 'expressions and other named animations' for animations_from and the sign convention (rotate CCW positive)
2. **Expect:** build exits 0, check PASS with FEET_STAY_LEVEL measured (10 of 14 bar(s)), dance 4.0 s built beside idle, ANIMATIONS_DO_NOT_FOLD PASS (shoulders and hips have no seam bar, so folds are the risk)
3. **Chose / turned down:** one animation 'dance' of 4 s in animations.json (hand-written by a python generator, sine keys every 1/16 s so every curve repeats each 1.0 s = two beats; bones keyed: hip translatey (dip 24 px on each beat, y up so negative lowers; the iks keep ankles planted) and hip rotate, chest rotate, neck/head rotate, sleeve_l0/r0 as alternating arm pumps (+ raises left, - raises right per README signs), elbows sleeve_l1/r1, wrists hand_l/r). Not keying ik mix: planted feet are the point. Turned down hip translatex (would pull ankles out of reach of the nearly straight legs)
4. **Happened** (2026-10-25T11:50:48Z): exit=0; "check: PASS; 10 of 14 bar(s) measured, 4 skipped" with FEET_STAY_LEVEL: PASS; "ANIMATIONS_DO_NOT_FOLD: PASS"; one unpredicted extra: "SEAM_OVER_MOTION: WARN — 9 declared pair(s) in 2 animation(s) (idle, dance) ... 2 warning(s), never a bar".

## Entry 2 (opened 2026-10-25T11:50:48Z)

1. **Read:** TASK.md 05 pass lines; build.log SEAM_OVER_MOTION WARN (not a bar)
2. **Expect:** grader: built, checked, whole, does_not_fold, dance_as_timed, closes, both_hands, whole_body, on_its_feet PASS; keeps_time probably PASS (all motion at period 1 s or 0.5 s); arms SKIP
3. **Chose / turned down:** grade now, then look at the seam warnings separately (turned down fixing the warning first: it is not a bar)
4. **Happened** (2026-10-25T11:53:35Z): WTF?: FAIL  on_her_feet: "the end of a leg (`shin_l`, `shin_r`) gets 8.32 rig px from where it meets `foot_l`, `foot_r`, against <= 6.0" — I expected the planted iks to hold the ankles whatever the hip did. Now I think the legs are nearly straight at rest (thigh 243 + shin 245 vs 488 px to the ankle), so at hip translatey 0 plus hip rotate the ankle target is out of the ik chain's reach and the shin lags. Everything else passed: both_hands 542.7/550.2, whole_body 25.4, keeps_time 1.0, closes 0.0.

## Entry 3 (opened 2026-10-25T11:53:35Z)

1. **Read:** my WTF just above; fixtures/mannequin/README.md 'Feet are planted by the rig' (move or dip hip and the feet stay put; thigh+shin length vs ankle distance computed from the config's bone points)
2. **Expect:** with hip translatey held between -10 and -34 (never at rest height) the iks always reach, on_her_feet passes (<= 6 px) and the rest still pass: 11 of 11 lines
3. **Chose / turned down:** re-key hip translatey as -22 - 12 cos(4 pi t) (hand edit of the generator output); keep hip rotate +-3; turned down dropping the hip rotate (try the cheaper change first)
4. **Happened** (2026-10-25T11:56:59Z): exit 0; "11 of 11 line(s), 3 skipped"; on_her_feet: "the end of a leg (`shin_l`, `shin_r`) gets 5.1 rig px from where it meets `foot_l`, `foot_r`, against <= 6.0" — passes but 5.1 is not far from 6, so my reach theory was only part of it.

## At the end (2026-10-25T11:56:59Z)

- **Where I guessed:** every amplitude and phase (arm +-30 deg about 35, elbows 0-34, head 7, chest 5, hip rotate 3, hip dip -10..-34 px) was chosen by feel, no document gave values for a dance; the 24 px / 34 px dip limit came from my arithmetic on thigh+shin length, not from a document
- **What I could not find:** No document says how far the planted legs can stretch; no line before the grader said the shin lags when hip rises (SEAM_OVER_MOTION WARN named 2 warnings and I did not read which pairs).
