# Journal

## Entry 1 (opened 2026-10-25T09:31:05Z)

1. **Read:** tasks/05-dance/TASK.md and fixtures/mannequin/README.md
2. **Expect:** rig-parts build exits 0 and produces mannequin rig with dance animation
3. **Chose / turned down:** building mannequin rig with authored dance.json animation
4. **Happened** (2026-10-25T09:31:30Z): build: stopped at assemble; no later stage ran

## Entry 2 (opened 2026-10-25T09:31:34Z)

1. **Read:** grade.py and tasks/05-dance/TASK.md
2. **Expect:** grade.py builds mannequin rig and measures dance lines
3. **Chose / turned down:** running grade.py to evaluate dance on fixture
4. **Happened** (2026-10-25T09:34:28Z): FAIL  both_hands: `hand_l` travels 155.6 rig px and `hand_r` 90.7 at their furthest vertex, measured from the middle of `topwear`, each against >= 100.0

## Entry 3 (opened 2026-10-25T09:34:43Z)

1. **Read:** tasks/05-dance/TASK.md (both_hands line >= 100 rig px)
2. **Expect:** both hands travel >= 100 rig px and grade.py passes all non-skipped lines
3. **Chose / turned down:** increasing arm joint rotations and adding wrist rotation in dance.json to satisfy both_hands travel
4. **Happened** (2026-10-25T09:37:49Z): 11 of 11 line(s), 3 skipped (budget, arms_bend_at_the_joints, soft_in_the_dance); journal present, 0 entry(ies) whose line 4 begins WTF?:;

## At the end (2026-10-25T09:37:54Z)

- **Where I guessed:** rotation direction synergy between shoulder, elbow and wrist for hand travel
- **What I could not find:** an interactive preview of motion curves or bone paths to visualize hand travel without full check loop
