# Journal — gpt-6-astra, 02-move, 2026-10-13

## Entry 1

1. **Read:** `tasks/02-move/TASK.md` Given/Do and `AUTHORING.md` recipe “expressions and other named animations”: Task 02 starts from Task 01's green config and names a motion file through `motion.animations_from`.
2. **Expect:** Copying the passing config into this run will preserve Task 01's four bars and give a stable base for the new wave and physics fields.
3. **Chose / turned down:** I will copy my own Task 01 config, as the task explicitly directs. I turned down reproposing because it would add no information and could only change the known-green baseline.
4. **Happened:** The Task 01 config was copied byte for byte into this run.

## Entry 2

1. **Read:** `AUTHORING.md` recipes “expressions and other named animations” and “Strands that trail”; rig-c `AUTHORING.md` §4.4 says bone `rotate` keys are relative degrees, and physics rotate needs a nonzero-length bone.
2. **Expect:** A 2-second `wave` rotating `sleeve_r0` by 90° will lift its descendants more than 150 rig px, while alternating `sleeve_r2` by ±15° will read as a wave. Four rotate-physics constraints on the lower links of the two long hair chains should gate green and satisfy the two-bone trail bar.
3. **Chose / turned down:** I will key the free chain bones, not their generated `_ctl` controls, so the named clip can layer over idle. I will constrain links 1 and 2 of each long lock, leaving each root directly attached to the head. I turned down translating the whole arm by 150 px because that would detach the shoulder rather than articulate it.
4. **Happened:** The config now names `animations.json`, contains four physics constraints on `lock1`, `lock2`, `lock1_1`, and `lock1_2`, and the motion file contains the planned 2-second wave.

## Entry 3

1. **Read:** `tasks/02-move/TASK.md` pass lines and `AUTHORING.md` §4 step 9: build gates named animations and physics constraints with the rig, though its ordinary check bars measure idle.
2. **Expect:** Build will exit 0, name `wave` beside idle, show four physics constraints in the rig gate, and retain Task 01's green bars. I expect the animation itself to need the grader for rise and fold measurements.
3. **Chose / turned down:** I will build before grading to catch schema or rig-gate failures locally. I turned down adding more arm tracks because the first run should measure the simplest articulated gesture.
4. **Happened:** It exited 0, named `wave`, gated a rig with 2 animations and 4 physics constraints, retained all idle PASS bars, and ended `build: PASS`.

## Entry 4

1. **Read:** `README.md` Results and Task 02 pass lines: the grader rebuilds and uniquely measures trail count, wave duration/rise, and folds over the named animation.
2. **Expect:** The grader will print seven PASS lines: the four Task 01 lines plus trails on four bones, a 2-second wave with rise above 150, and no folds.
3. **Chose / turned down:** I will grade this first articulated draft. I turned down pre-emptive tuning because only the grader states the actual rise and folding result.
4. **Happened:** SURPRISE: All seven lines passed, including 202.0 rig px rise and no folds, but the grader again printed the undocumented `clock: no started:/finished: lines in transcript.md` diagnostic.

## At the end

- **Where I guessed:** The wave's 90° shoulder raise, ±15° wrist oscillation, key timing, and all four physics tuning sets are authored values. A packaged wave example for this exact skeleton or a motion preview metric before grading would remove those guesses.
- **What I could not find:** The package recipe explains structure and examples but gives no numeric wave values for the supplied painting; Task 02 deliberately leaves whether the gesture visually reads as a wave to the proctor.
