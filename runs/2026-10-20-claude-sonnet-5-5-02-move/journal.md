# Journal — claude-sonnet-5-5, 02-move, 2026-10-20

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry 1

1. **Read:** AUTHORING §3 'Recipe: expressions and other named animations' (motion.animations_from, key the free bones not the *_ctl, positive rotate is CCW so on sleeve_l raises toward image right/up) and its 'Strands that trail' (one physics constraint per link, rotate 1, inertia 0.8, strength 90 down by 0.35*i/(n-1), damping 0.85, mass 1, mix 1).
2. **Expect:** build exits 0, check PASS 10/10; 'beside the idle: 1 animation(s), wave'; ANIMATIONS_DO_NOT_FOLD names 0 folds if the arm raise does not turn a mesh triangle over (uncertain: a 95 degree swing of sleeve_l0 might fold the shoulder); loop line says 8 physics constraints left out.
3. **Chose / turned down:** wave.json keys sleeve_l0 +95 degrees then waves with sleeve_l1/l2 swinging, plus a small head tilt so the hair has a head motion to lag; constraints: 8 physics (lock0..3, lock1_0..3) copied from the demo shape. Turned down: using the _ctl bones (they carry the idle), turning bang chains into physics (they are fringe on the face; locks are the free-hanging strands), and an ik on the hand (needs --idle-keys direct, more machinery than needed).
4. **Happened:** build exit 0, check PASS 10 of 10, 'beside the idle: 1 animation(s), wave', physicsConstraints=8, ANIMATIONS_DO_NOT_FOLD 0 folding (idle, wave) with 8 physics constraints left out, loop physics line names the 8. As expected, no WTF; the 95 degree swing did not fold.

## Entry 2

1. **Read:** Task 02 pass lines (Trails, Moves: some bone rising >=150 rig px more than the median bone in a non-idle animation >= 1 s, Moves without folding); README Rules 6.
2. **Expect:** grader prints 7 PASS lines: task 01's four, trails (8 physics bones), moves (sleeve_l bones rise ~400+ px over median, wave 2.4 s), no folds.
3. **Chose / turned down:** Run the grader as the measurement. Turned down: rendering the six frames myself first, since the task's machine lines come from grade.py; I will still render the wave to look at it afterwards.
4. **Happened:** 7 of 7 PASS: trails 8 bones, moves wave 2.4 s rise 382.4 (bar 150), no folds. Matches expectation (I guessed 400+; 382.4). I then rendered the wave at 6 fps and looked at the contact sheet: the arm rises to about horizontal-and-above and the forearm sways. No WTF.

## At the end

- **Where I guessed:** Wave angles (+95 for sleeve_l0, +-22/+-14 for the forearm links), the head tilt (-6/5/-4), key times and the 2.4 s duration are my own numbers; I only knew from AUTHORING that +rotate on sleeve_l goes up and toward image right. Physics values are the demo's recipe numbers, not tuned for this hair; I did not render the hair to see it lag. I would have needed a measured line of how far a lock link trails, or a clip-level report of per-bone motion.
- **What I could not find:** How much the hair actually lags in this clip (no bar reads it; I did not measure); which of the two sleeve chains is the image's right (inferred from bone x positions, 507 vs 357, and the doc's demo note).
