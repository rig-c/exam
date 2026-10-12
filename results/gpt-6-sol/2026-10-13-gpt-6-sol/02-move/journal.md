# Journal — gpt-6-sol, 02-move, 2026-10-13

## Entry 1

1. **Read:** `tasks/02-move/TASK.md` Given: start from my task 01 config, which graded four of four lines.
2. **Expect:** The new run receives an identical, parseable `config.json` before adding the wave and physics.
3. **Chose / turned down:** Copy only my 01 config as the baseline; turned down starting from a package example because its painting differs.
4. **Happened:** `config.json` was copied byte-for-byte from my graded 01 run and parses with the same 21 bone entries and 8 meshes.

## Entry 2

1. **Read:** `tasks/02-move/TASK.md` Do, `@rig-c/parts/docs/AUTHORING.md` Recipe: expressions and other named animations/Strands that trail, and `rig-c/docs/AUTHORING.md` §§3.5, 4.4–4.5. The right sleeve links are at `[357,254]`, `[342,381]`, `[306,507]` and tip `[242,637]` in rig coordinates.
2. **Expect:** `config.json` gains four physics constraints on the two hanging hair chains plus `motion.animations_from`; `animations.json` contains a 2-second wave raising the right sleeve by its root rotation and oscillating its tip.
3. **Chose / turned down:** Key the actual sleeve link bones and constrain actual hair links; turned down keying idle controls because the guide says those would interrupt the idle when layered.
4. **Happened:** Both JSON files parse; the config names `animations.json` and constraints `lock1`, `lock2`, `lock1_1`, `lock1_2`; the wave has 2 tracks over 2 seconds.

## Entry 3

1. **Read:** `tasks/02-move/TASK.md` Pass lines and `@rig-c/parts/docs/AUTHORING.md` §4 step 9: a build gates the authored constraints and the named animation.
2. **Expect:** `rig-parts build` exits 0, retains `check: PASS`, and reports four physics constraints plus the `wave` animation beside idle.
3. **Chose / turned down:** Build before grading to see named rig or motion refusals; turned down changing values without a measured failure.
4. **Happened:** Build exited 0, `check: PASS; 9 of 9`, reported 4 physics constraints, and gated the named `wave` animation; `uncovered_error_px` stayed 2059.

## Entry 4

1. **Read:** `grade.py` main: 02's grader renders idle and named animations with `--folds`, computes each animation's bone rise against the median, and requires 150 px.
2. **Expect:** Seven PASS lines, with four constrained hair bones, a 2-second wave rising at least 150 rig px, and no mesh folds.
3. **Chose / turned down:** Run the exact grader to measure the actual wave; turned down inferring rise or mesh quality from the build gate, which measures idle only.
4. **Happened:** Grader exited 0 with seven PASS lines: 4 physics bones, `wave` duration 2, rise 387.5 rig px, and no folding on idle or wave.

## At the end

- **Where I guessed:** The 2-second timing, −110° arm lift, ±15° hand oscillation, and the four physics tuning sets were authored without a task-specific source. A measured motion reference and strand response target would have replaced those choices.
- **What I could not find:** The package gave a recipe but no target pose for this painting; the grader supplied the quantitative rise and fold result.
