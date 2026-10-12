# Journal — gemini-3.8-flash, 02-move, 2026-10-13

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry 1

1. **Read:** `tasks/02-move/TASK.md` (Do 2: "Hair that trails") and `node_modules/@rig-c/parts/docs/AUTHORING.md` §3 ("Recipe: expressions and other named animations", "Strands that trail").
2. **Expect:** Create `runs/2026-10-13-gemini-3.8-flash-02-move/config.json` copied from task 01, adding physics constraints on `lock1` and `lock1_1` (driving `rotate`), and declare `motion.animations_from: "wave.json"`.
3. **Chose / turned down:** Chose adding physics constraints to hair chain links `lock1` and `lock1_1` driving `rotate`, and pointing `animations_from` to `wave.json`. Turned down zero-length bones (like bun) because `A23` prohibits rotate drive on zero-length bones.
4. **Happened:** Created `config.json` with two physics constraints on `lock1` and `lock1_1` and `motion.animations_from: "wave.json"` as expected.

## Entry 2

1. **Read:** `tasks/02-move/TASK.md` (Do 1: "A wave") and `node_modules/@rig-c/parts/docs/AUTHORING.md` §3 ("Recipe: expressions and other named animations").
2. **Expect:** Create `runs/2026-10-13-gemini-3.8-flash-02-move/wave.json` with animation `wave` of duration 1.5 s, keying `sleeve_l0`, `sleeve_l1`, and `sleeve_l2` to lift the arm >= 150 rig px and wave.
3. **Chose / turned down:** Chose keying `sleeve_l0` (70°), `sleeve_l1` (50°), and waving `sleeve_l2` (±20°) over 1.5 s. Turned down keying `sleeve_l0_ctl` or `*_ctl` controls because supplementary clips must key the bones directly as instructed in AUTHORING §3.
4. **Happened:** Created `wave.json` with animation `wave` (1.5 s) keying `sleeve_l0`, `sleeve_l1`, and `sleeve_l2` as expected.

## Entry 3

1. **Read:** `tasks/02-move/TASK.md` (Pass lines: Built, Checked, Whole, Does not fold, Trails, Moves, Moves without folding) and `grade.py`.
2. **Expect:** `python3 grade.py runs/2026-10-13-gemini-3.8-flash-02-move` passes 7 of 7 lines and writes `result.json`.
3. **Chose / turned down:** Chose running `python3 grade.py` to evaluate the rig, physics trails, and folding over the wave animation. Turned down running standalone build as the grader performs complete verification.
4. **Happened:** Grader passed 7 of 7 lines (`built`, `checked`, `whole`, `does_not_fold`, `trails` 2 bones, `moves` rise 335.8 >= 150, `moves_without_folding` []) and wrote `result.json` as expected.

## At the end

- **Where I guessed:** Keyframe rotation angles for the wave animation (`sleeve_l0` 70°, `sleeve_l1` 50°, `sleeve_l2` ±20°) were determined geometrically from bone lengths and angles rather than an existing clip file. Physics tuning parameters were taken directly from the default constants in `node_modules/rig-c/src/rig.ts`.
- **What I could not find:** None. The animation spec requirements and physics constraint specifications in `AUTHORING.md` and `rig.ts` were clear.





