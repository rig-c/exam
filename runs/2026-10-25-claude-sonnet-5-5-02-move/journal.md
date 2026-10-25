# Journal

## Entry 1 (opened 2026-10-25T11:33:51Z)

1. **Read:** AUTHORING §3 'Recipe: expressions and other named animations' (animations_from, key head/chest not *_ctl) and 'Strands that trail' (physics per link, demo values inertia 0.8 strength 90 damping 0.85)
2. **Expect:** build exit 0 with the look animation built and gated, 20 physics constraints (hairback_r/l, lock, lock1_ chains), ANIMATIONS_DO_NOT_FOLD PASS or a fold/stretch FAIL I will read
3. **Chose / turned down:** animations.json (look: head +-10, chest +-3, chest translatey -6, 2.4 s, hand-written) and constraints written into config.json by a python snippet (hand edit); build task 02 straight rather than lint first; turned down keying the rig's 'turn' control (moves every part by depth, risks seams)
4. **Happened** (2026-10-25T11:35:11Z): exit=0; "build: PASS"; ANIMATIONS_DO_NOT_FOLD: PASS — 2 animation(s) ... with its 14 physics constraint(s) on and off (idle, look): 0 folding mesh(es). 14 constraints, not the 20 I wrote in my expectation (3+3+4+4=14, my arithmetic slip).

## Entry 2 (opened 2026-10-25T11:35:11Z)

1. **Read:** TASK.md pass lines; README 'python3 grade.py runs/<run>'
2. **Expect:** grader: built, checked, whole, does_not_fold PASS plus trails PASS, gestures PASS if face travel >= 22 (head 10deg + chest 3deg + 6px drop: estimate 30+), holds_together uncertain, gesture_no_fold PASS
3. **Chose / turned down:** run the grader on the run dir; no tuning before seeing numbers
4. **Happened** (2026-10-25T11:36:32Z): WTF?: FAIL  holds_together: {"opens": {"topwear|handwear_l": {"frames": 12, "max_px": 35}}} — I expected the chest lean/drop to carry the sleeves with it; instead 12 frames open a 35 px gap between topwear and handwear_l (not handwear_r). gestures PASS (66.3 px vs 22), the other lines pass.

## Entry 3 (opened 2026-10-25T11:36:49Z)

1. **Read:** grade output FAIL holds_together topwear|handwear_l 12 frames 35 px; grade.py holds_together() source; rigc render --help --seam
2. **Expect:** building a probe rig with four single-component animations (head only, chest rotate only, chest translate only, head+chest rotate) then seam-rendering each will show which key opens topwear|handwear_l; I expect the chest translatey -6 (topwear is blended to hip, sleeve rides chest fully)
3. **Chose / turned down:** build a probe copy under run/probe (not handed in) with animations split by component; turned down guessing a fix and re-grading (each grade costs ~75 s and says nothing about the cause)
4. **Happened** (2026-10-25T11:38:06Z): exit=0; probe build wrote runs/2026-10-25-claude-sonnet-5-5-02-move/probe/out/check/build/skeleton.json as expected.

## Entry 4 (opened 2026-10-25T11:38:06Z)

1. **Read:** rigc render --seam (help); grade.py holds_together() pair and floor rule
2. **Expect:** seam.json per probe animation: p_trans (chest translatey) opens topwear|handwear_l; p_head and p_rot show none
3. **Chose / turned down:** one script running rigc render --seam topwear:handwear_l,topwear:handwear_r for each p_* animation and applying the grader's floor rule (px > max box side / cell); a python script I wrote inline in sh -c
4. **Happened** (2026-10-25T11:38:39Z): As predicted: "p_trans topwear handwear_l read frames open 18 max_px 20" while p_head, p_rot and p_headrot read "frames open 0 max_px 0" for both pairs. The chest translatey opens the pair.

## Entry 5 (opened 2026-10-25T11:38:40Z)

1. **Read:** probe result: only chest translatey opens topwear|handwear_l
2. **Expect:** grade: 8 of 8 lines pass; face travel falls from 66.3 to roughly 35-45 rig px, still >= 22; holds_together empty
3. **Chose / turned down:** drop the chest translatey track from animations.json (hand edit) and raise head to +-12 and chest to +-4 deg; turned down keeping a smaller translate (it opens by construction: topwear blends to hip, sleeve rides chest)
4. **Happened** (2026-10-25T11:40:10Z): WTF?: removing the translate did not clear it: FAIL holds_together {"topwear|handwear_l": {"frames": 6, "max_px": 16}} — fewer frames, but my probe said chest rotate 3 deg opened nothing, so the 4 deg (or head 12) I raised it to is over the edge. Face travel 82.6 px, far above 22.

## Entry 6 (opened 2026-10-25T11:40:10Z)

1. **Read:** previous grade: 6 frames open at chest +-4; probe: chest +-3 with head +-10 opened none
2. **Expect:** holds_together passes with chest +-2 and head +-12; face travel ~70-80 px; 8 of 8
3. **Chose / turned down:** lower chest rotate to +-2 (hand edit), keep head +-12; turned down dropping the chest rotate altogether (a lean is one of the gestures the task names)
4. **Happened** (2026-10-25T11:41:43Z): exit 0; "8 of 8 line(s)"; holds_together: {"opens": {}, ...}; gestures 66.4 rig px; chest +-2 deg with head +-12 deg opens nothing.

## At the end (2026-10-25T11:41:43Z)

- **Where I guessed:** gesture angles (head 12, chest 2) and the physics values (inertia 0.8/0.7, strength 90, damping 0.85) came from the demo recipe/trial, not from a measurement of this painting; the 22 px bar was given
- **What I could not find:** Nothing said the chest translate would open the topwear/handwear pair (the doc's 'Key the bones the idle leaves alone' rule gives no seam warning).
