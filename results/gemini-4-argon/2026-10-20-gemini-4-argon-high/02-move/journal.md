# Journal — gemini-4-argon-high, 02-move, 2026-10-20

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry 1

1. **Read:** `tasks/02-move/TASK.md` and `node_modules/@rig-c/parts/docs/AUTHORING.md` §3 (`motion.animations_from`, `constraints`, and *Recipe: expressions and other named animations*, lines 1132–1224).
2. **Expect:** Writing `animations.json` with a 2.0 s `wave` animation (keying `sleeve_l0` `rotate` up to +42 deg, `sleeve_l1` `rotate` up to +35 deg, `sleeve_l2` `rotate` between -10 and +18 deg, and `head` `rotate` to -5 deg) and writing `config.json` (task 01's config plus `motion.animations_from: "animations.json"` and 8 `physics` constraints on `lock0..lock3` and `lock1_0..lock1_3` with `rotate: 1`, `inertia: 0.8`, `damping: 0.85`, `strength` 90.0, 79.5, 69.0, 58.5), then running `npx rig-parts build` will exit 0 with `check: PASS; 10 of 10 bar(s) measured` and `ANIMATIONS_DO_NOT_FOLD: PASS` over both `idle` and `wave`.
3. **Chose / turned down:** Chose to distribute the lift across `sleeve_l0` (+38..+42 deg) and `sleeve_l1` (+18..+35 deg) so `sleeve_l2`'s origin rises ~178 rig px (above the 150 rig px requirement) while avoiding shoulder/elbow triangle folds, and chose all 8 hanging hair lock bones (`lock0..lock3`, `lock1_0..lock1_3`) for physics constraints using the `1 - 0.35 * i / (n - 1)` strength decay from `AUTHORING.md` §3; turned down putting a large single angle on `sleeve_l0` alone to avoid tearing or folding the shoulder mesh.
4. **Happened:** Exited 0 with `ANIMATIONS_DO_NOT_FOLD: PASS — 2 animation(s) read by rigc render --folds at 12 fps, its 8 physics constraint(s) left out (idle, wave): 0 folding mesh(es)` and `check: PASS; 10 of 10 bar(s) measured, 0 skipped`.

## Entry 2

1. **Read:** `tasks/02-move/TASK.md` (Pass lines: Task 01's four, plus Trails, Moves, Moves without folding) and `grade.py`.
2. **Expect:** Running `python3 grade.py runs/2026-10-20-gemini-4-argon-high-02-move` will exit 0, print 7 PASS lines (`7 of 7 line(s)`), with `trails` showing 8 bones on physics constraints and `moves` showing `wave` rising ~178 rig px (>= 150) with `[]` folds.
3. **Chose / turned down:** Chose to run `grade.py` directly on the green build; turned down adjusting `wave` angles further since the calculated rise (~178 rig px) exceeds 150 rig px with 0 folding meshes.
4. **Happened:** Exited 0, printed `7 of 7 line(s)` (`trails`: 8 bones on physics constraints; `moves`: `{"animation": "wave", "duration": 2, "rise": 178.0, "folds": []}`; `moves_without_folding`: `[]`), and wrote `result.json`.

## At the end

- **Where I guessed:** The `wave` keyframe angles (`sleeve_l0` +38..+42 deg, `sleeve_l1` +18..+35 deg, `sleeve_l2` -10..+18 deg, `head` -3..-5 deg) were chosen by calculating the trigonometry of `sleeve_l0` (`length` 127.3 px, rest world angle -76.8 deg) and `sleeve_l1` (`length` 132.4 px, rest world angle -68.3 deg) to achieve a 178.0 rig px rise without folding the shoulder or elbow mesh. The physics parameters (`inertia: 0.8`, `strength: 90.0` decayed by `1 - 0.35 * i / (n - 1)`, `damping: 0.85`, `mass: 1`, `mix: 1`) were taken from the `demo` example recipe in `AUTHORING.md` §3.
- **What I could not find:** Nothing; `AUTHORING.md` §3 had both the `animations_from` recipe (including the `sleeve_l0` sign convention) and the `physics` strand recipe.


