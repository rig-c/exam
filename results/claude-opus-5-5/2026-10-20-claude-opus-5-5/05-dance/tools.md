# What the tools were missing — claude-opus-5-5, 2026-10-20

## `--parts` after a build points somewhere else than after `assemble`
- **I was trying to:** LINT my edited config (`propose --from-config`) against the parts my task-04 build had written.
- **The tool gave me:** `FAIL  PARTS_FILE_PRESENT: ../…-04-soft/out/rig/parts.json — no such file`. The README's loop passes `--parts work/rig` (after `assemble --out work`), so I passed `out/rig`; a build writes `parts.json` at `out/`, not `out/rig/`.
- **What would have helped:** the refusal naming where else a `parts.json` sits: "a `build --out <dir>` writes it at `<dir>/parts.json`; `assemble --out <dir>` at `<dir>/rig/parts.json`".
- **Cost:** a minute; got there.

## `render --fps` changes the output folder without saying so in `--help`
- **I was trying to:** read the dance's posed geometry after each rebuild, to measure how far the arms bend between joints.
- **The tool gave me:** `--out <dir>  directory to write the frame series into (default render/)`. At `--fps 12` the frames land in `<out>/dance/`, at `--fps 24` in `<out>/dance@24fps/` (printed on the run line, but not in the help). My script kept reading the old 12 fps folder for three rebuilds.
- **What would have helped:** one sentence in `--help` for `--out`: "each animation is written to `<out>/<name>/` at the default 12 fps and to `<out>/<name>@<fps>fps/` otherwise"; or a refusal/warning when `--out` already holds a series of the same animation at another rate.
- **Cost:** about 15 minutes and one wrong conclusion in my journal (entry 11); found it in the end.

## `check` reads animations for folds with physics left out, so a physics fold is unreported
- **I was trying to:** know that the dance did not fold.
- **The tool gave me:** `ANIMATIONS_DO_NOT_FOLD: PASS — 4 animation(s) read by rigc render --folds at 12 fps, its 9 physics constraint(s) left out (idle, wave, hop, dance): 0 folding mesh(es)` — while `rigc render --animation dance --folds` (physics on) said `"dance": mesh "hair_front" … folds on 3 frame(s) [19, 31, 43]` (the side locks' physics squeezing the fringe).
- **What would have helped:** a second, REPORTED line from `check` reading each animation with its physics on (with a lead-in, as `--loop --lead-in` does), or one sentence in AUTHORING §7 saying "physics folds are not read; run `rigc render --folds` on each clip".
- **Cost:** two rebuilds (about 5 minutes) to tune the lock springs; got there because I rendered by hand.

## No reading of how much a limb bends between its joints
- **I was trying to:** keep the arms bending only at the elbow and wrist (the task's 0.54 / 0.20).
- **The tool gave me:** nothing that reads it — `TEXTURE_STRETCH` reads stretch on the idle, folds read turned triangles; the 10.1° bend inside the forearm was only visible to the grader and to a script I wrote over `geometry.json`.
- **What would have helped:** a `--requirements` kind that holds a chain link's own art straight: "the vertices bound mostly to `sleeve_r1` stay within N° of a rigid turn over animation X" — the requirements file already has a joint range and a mesh stretch; this is the missing neighbour.
- **Cost:** about 25 minutes (four rebuilds); got there.

## The distance rule's weights leak across a bend; nothing says so, and the fix trades against folds
- **I was trying to:** make the forearm turn as one piece.
- **The tool gave me:** AUTHORING §3 `exponent`: "a larger one hands each vertex more fully to its nearest bone"; `rule: "heat"`. Measured: exponent 4 → 6.9° bend (small moves), 5 → 10.1° (bigger moves), 6 folded `wave` at the shoulder (`… mesh "handwear_l" … folds on 15 frame(s) [5-19] … triangle(s) [2]`, between the chest stub and the upper arm); heat read ~1° but folded the elbow at 70°.
- **What would have helped:** a sentence by the `exponent` and `rule` rows that a lattice corner on the inside of a bend is near both bones, so straight-line distance hands it to the wrong one; and that sharper weights (higher exponent, heat) fold the crease earlier — with the measured trade on the examples, as *Which mode comes out smaller* gives one for triangles.
- **Cost:** the larger part of task 05's time; ended on exponent 4 with a smaller elbow pump.

## Keeping the feet planted: the documents describe it for keypoints and for rig-c, not for a rig-parts figure
- **I was trying to:** move the hip without the legs leaving the shoes (task 05's starting point: legs a region on `hip`, shoes a region on `root`).
- **The tool gave me:** AUTHORING §3's `leg_<s>` row (a leg chain only via `propose --keypoints`, "No idle track … whether the legs move is the scene's"), and rig-c RIGGING §9.1 (IK target under root) and §7's note that a two-bone solve "throws the knee sideways".
- **What would have helped:** a recipe beside *Expressions* and *A soft region*: "Planted feet — shoes on `root`, the legs a mesh weighted between the hip and bones on root (or an IK leg to targets on root when the legs are bent enough to fold); a near-straight leg will swing its knee sideways under IK". I worked out the root-shin blend from the `segments` row.
- **Cost:** about 20 minutes of reading and arithmetic; got there.

## A contour mesh's triangle count is known only after a full build
- **I was trying to:** fit a soft-chest contour mesh under task 04's 700 triangles.
- **The tool gave me:** the `[rig] mesh topwear v= 112 t= 179 …` line, printed one minute into `build`; AUTHORING *A contour mesh* says the outline "at tolerance 1 is dense" without a way to count it first.
- **What would have helped:** `rig-parts mesh --config … --parts … --part topwear` (or `rig --dry-run`) printing the mesh line alone in a second or two.
- **Cost:** none in the end — the first guess fit with 17 to spare — but only by luck.

## The animations file refuses `easings`, so smooth motion needs dense linear keys
- **I was trying to:** write a smooth 4 s loop.
- **The tool gave me:** the `motion.animations_from` row: "any other key — rig-c's `easings` … (`CONFIG_KEY_KNOWN`)"; only `shut` and `open` may be named.
- **What would have helped:** either `easings` passed through, or the idle's own sine shape (`{bone, prop, amp, period, phase}`) accepted in an animation beside the idle — a dance is exactly periodic tracks.
- **Cost:** a few minutes; I sampled each track every 1/16 s (65 keys).
