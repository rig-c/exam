# Journal — gemini-3.8-flash-medium, 02-move, 2026-10-20

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry 1

1. **Read:** `tasks/02-move/TASK.md` (wave duration >= 1 s, rise >= 150 rig px) and `node_modules/@rig-c/parts/docs/AUTHORING.md` §3 (`motion.animations_from`).
2. **Expect:** `wave.json` holding a 2.0 s `wave` animation with keys raising `sleeve_l` links (`sleeve_l0`, `sleeve_l1`) and waving `sleeve_l2`.
3. **Chose / turned down:** Created `wave.json` with arm raise and wrist waving; turned down keying other bones to avoid fold risks on the torso.
4. **Happened:** Created `wave.json` with a 2.0 s `wave` animation.

## Entry 2

1. **Read:** `tasks/02-move/TASK.md` (Hair that trails on physics rather than keys, >= 2 bones) and `node_modules/@rig-c/parts/docs/AUTHORING.md` §3 (`constraints`, `Strands that trail`).
2. **Expect:** `config.json` written with 8 physics constraints on hair strands (`lock0..3`, `lock1_0..3`), `lock` and `lock1_` removed from `motion.tracks`, and `motion.animations_from: "wave.json"`.
3. **Chose / turned down:** Applied physics constraints to `lock` and `lock1_` chains using the softening formula from AUTHORING.md and removed their keyed tracks from idle; turned down keying them.
4. **Happened:** Created `config.json` with 8 hair physics constraints, removed `lock`/`lock1_` from idle tracks, and linked `wave.json`.

## Entry 3

1. **Read:** `grade.py` lines 297-309 and `tasks/02-move/TASK.md` Pass lines.
2. **Expect:** `python3 grade.py runs/2026-10-20-gemini-3.8-flash-medium-02-move` will pass all 7 lines (built, checked, whole, does_not_fold, trails, moves, moves_without_folding).
3. **Chose / turned down:** Running `grade.py` to evaluate the build with physics and wave animation.
4. **Happened:** python3 grade.py passed 7 of 7 lines (built, checked, whole, does_not_fold, trails, moves [rise 397.6], moves_without_folding).

## At the end

- **Where I guessed:** Wave rotation angles (90 deg on sleeve_l0, 45 deg on sleeve_l1, ±20 deg on sleeve_l2). Verified they provide sufficient rise (397.6 px > 150 px) without folding.
- **What I could not find:** None; the strand physics softening recipe and motion file conventions were well-described in AUTHORING.md §3 and §4.
