# Journal

## Entry 1 (opened 2026-10-25T09:30:50Z)

1. **Read:** tasks/02-move/TASK.md and node_modules/@rig-c/parts/docs/AUTHORING.md §3 (Recipe: expressions and other named animations; Strands that trail)
2. **Expect:** Exit code 0, printing 'check: PASS' and 'build: PASS', with bow built beside idle, 14 physics constraints on hairback_r/l and lock/lock1_, and 0 folding meshes on idle and bow.
3. **Chose / turned down:** Wrote runs/2026-10-25-gemini-4-argon-high-02-move/config.json (replacing hairback_r, hairback_l, lock, lock1_ idle tracks with 14 physics constraints from the Strands that trail recipe, and referencing animations.json) and runs/2026-10-25-gemini-4-argon-high-02-move/animations.json (a 2.0 s 'bow' animation keying head rotate -8°, chest rotate -3°, chest translatey -6 px with no limbs keyed), then run rig-parts build.
4. **Happened** (2026-10-25T09:32:08Z): WTF?: assemble refused with FAIL CONFIG_KEY_KNOWN: config.motion.animations_from (.../animations.json).easings — is not a field here; known: spec, animations

## Entry 2 (opened 2026-10-25T09:33:59Z)

1. **Read:** Entry 1 build output: [assemble] FAIL CONFIG_KEY_KNOWN on animations.json.easings; AUTHORING.md §3 Recipe: expressions and other named animations and Strands that trail
2. **Expect:** rig-parts build exits 0 with check: PASS after removing easings/curve from animations.json and keeping the idle tracks alongside physics constraints
3. **Chose / turned down:** run rig-parts build on runs/2026-10-25-gemini-4-argon-high-02-move/config.json
4. **Happened** (2026-10-25T09:35:25Z): build exited 0 with check: PASS; 11 of 11 bar(s) measured, 0 skipped; 0 warning(s) and ANIMATIONS_DO_NOT_FOLD: PASS — 2 animation(s) read by rigc render --folds at 12 fps, with its 14 physics constraint(s) on and off (idle, bow): 0 folding mesh(es)

## Entry 3 (opened 2026-10-25T09:35:36Z)

1. **Read:** Entry 2 build output: check: PASS; 11 of 11 bar(s) measured; ANIMATIONS_DO_NOT_FOLD: PASS on idle and bow with 14 physics constraints
2. **Expect:** grade.py passes all 8 lines (built, checked, whole, does_not_fold, trails, gestures, holds_together, gesture_without_folding)
3. **Chose / turned down:** run python3 grade.py runs/2026-10-25-gemini-4-argon-high-02-move
4. **Happened** (2026-10-25T09:37:18Z): WTF?: 7 of 8 line(s) passed, but FAIL holds_together: {"opens": {"topwear|handwear_l": {"frames": 17, "max_px": 40}}, "not_read": [], "against": "0 frames open on every pair, every pair read"} because keying chest in bow moved handwear_l (100% under chest) against topwear (weighted across chest and hip)

## Entry 4 (opened 2026-10-25T09:37:53Z)

1. **Read:** Entry 3 grade.py output: FAIL holds_together on topwear|handwear_l (17 frames, max_px 40) when chest was keyed in bow
2. **Expect:** grade.py passes all 8 lines including holds_together (0 frames open) and gestures (>= 22 rig px) when bow keys neck and head instead of chest
3. **Chose / turned down:** run python3 grade.py runs/2026-10-25-gemini-4-argon-high-02-move
4. **Happened** (2026-10-25T09:39:04Z): grade.py passed 8 of 8 line(s) including gestures (:  travels 41.9 rig px at its furthest vertex, measured from the middle of , against >= 22) and holds_together: {"opens": {}, "not_read": [], "against": "0 frames open on every pair, every pair read"}

## At the end (2026-10-25T09:39:16Z)

- **Where I guessed:** whether animations_from accepts a top-level easings table like rigc's motion spec; and the neck/head rotation amplitudes (+2/-2 and +7/-7 degrees) needed to move face >= 22 rig px without keying chest
- **What I could not find:** CONFIG_KEY_KNOWN on animations_from only lists spec and animations after assemble runs; a note in the animations_from recipe of AUTHORING.md §3 stating that top-level easings are not part of the animations_from schema (or that check --seam-pairs topwear:handwear_l can be run on a named animation) would prevent both round trips
