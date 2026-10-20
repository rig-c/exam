# Journal — claude-opus-5-5, 02-move, 2026-10-20

## Entry 1

1. **Read:** AUTHORING §3 *Recipe: expressions and other named animations* — `motion.animations_from`, rigc-motion/1 shape, "Which way a key moves a bone" (positive `rotate` swings a hanging arm toward the image's right and up; demo's `wave` raises the image's right arm with `sleeve_l0` at +48), "Key the bones the idle leaves alone" (the idle keys `<chain><i>_ctl` and `head_ctl`, so `sleeve_l0` and `head` are free), and *Strands that trail* (one `physics` constraint per link on the link bone, `rotate: 1`, inertia 0.8, strength 90 × (1 − 0.35·i/(n−1)), damping 0.85, mass 1, mix 1). My task-01 config: chains `lock` (4 links, image-left side lock) and `lock1_` (4 links, image-right side lock), arm chain `sleeve_l` from [507,250] with the hand bone `sleeve_l2` at [585,497].
2. **Expect:** `build` exits 0, `[rig] animations beside the idle … : wave`, `check: PASS; 10 of 10`, a `loop physics:` line naming 8 constraints, ANIMATIONS_DO_NOT_FOLD reading 2 animations with 0 folding meshes. By my own arithmetic `sleeve_l0` at +110° lifts `sleeve_l2`'s origin about 400 rig px.
3. **Chose / turned down:** `animations.json` with `wave` (2.0 s): `sleeve_l0` rotate 0 → +110 by 0.4 s, held to 1.6 s, back to 0 at 2.0 s; `sleeve_l1` swinging ±25 four times between 0.4 and 1.6 s (the wave at the elbow); `head` rotate −4/+4 so the locks have something to trail. Physics on all 8 lock links with the recipe's values verbatim. Turned down demo's +48 (my arithmetic gives only ~140 px rise for the hand origin, under the 150 bar) and turned down physics on the bangs (they lie on the face; the task says strands that hang free).
4. **Happened:** exit 0; `animations beside the idle … : wave`, `physicsConstraints=8`, `loop physics:` names all eight, `ANIMATIONS_DO_NOT_FOLD: PASS — 2 animation(s) … its 8 physics constraint(s) left out (idle, wave): 0 folding mesh(es)`, `check: PASS; 10 of 10`. As expected — except that I had not expected the fold reading to leave physics out of the wave too; noted, not a surprise worth a WTF.

## Entry 2

1. **Read:** `rigc render --help` (`--animation`, `--folds`, `--geometry`, `--fps`, `--max`).
2. **Expect:** frames of `wave` under `work/wave/` (24 at 12 fps over 2 s + 1), a folds.json with no mesh, and a frame at ~1 s showing the image-right arm raised above the head.
3. **Chose / turned down:** render `wave` with physics on (the default render) so I see the locks trail and folds with them; turned down trusting the check line alone, since check left physics out.
4. **Happened:** 25 frames, `0 of 8 mesh(es) fold` with physics on. The contact sheet shows the image-right arm swinging up past horizontal and the hand above the head at frame 10, then back down; the elbow wave is small at this size. The puffed sleeve lifts with the arm and a little of the shoulder line opens beside it — visible, not judged by any bar.

## Entry 3

1. **Read:** the prompt (grade.py), TASK.md's pass lines (Trails ≥ 2 physics bones, Moves ≥ 150 rig px over the median bone, ≥ 1 s, no folds).
2. **Expect:** 7 of 7 PASS; the rise somewhere around 300–400 rig px.
3. **Chose / turned down:** grade as is; turned down tuning the arm further before seeing a number.
4. **Happened:** `7 of 7 line(s)`: trails 8 bones, moves `wave` 2 s rise 433.3, no folds. Rise a little above my 300–400 guess (the bone measured is presumably further out the arm than `sleeve_l2`'s origin).

## At the end

- **Where I guessed:** the wave's angles (+110 at the shoulder, ±20 at the elbow) and timings — my own arithmetic from the bone positions; the physics values are the recipe's verbatim (demo's twin tail), not tuned for these shorter side locks.
- **What I could not find:** what the hair actually does in the wave — no bar reads physics trailing, and the fold reading in `check` left physics out.
