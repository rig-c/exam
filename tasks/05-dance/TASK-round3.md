# Task 05 — dance

> **Round 3's task 05**, kept for the runs filed on it (on `@rig-c/parts` 1.15.0 and `rig-c` 2.47.1). Round 4
> sets task 05 on the wooden mannequin: [`TASK.md`](TASK.md). To regrade a Round 3 run, check out those
> versions and run `python3 grade.py runs/<run> --fixture none`. Its painting left the tree with Round 5; check out
> commit `f96b6b0` for it.

The painting of task 01, and your rig for it from task 04 — soft chest and all.

## Given

Task 01's inputs (`../01-build/inputs/`). Nothing else: no keys, no pose, no reference clip.

The music is 120 beats a minute. Eight beats are 4.0 seconds.

## Do

Give the rig one more animation, named `dance`: a loop of exactly 4.0 s in which she dances — to that
beat, with her whole body, on her own two feet.

Use the bones the rig has, and add what it lacks. As task 04 left her, her legs are one flat piece that
hangs from the hip and her shoes are another that sits on the ground: move the hip and the two come
apart. What a figure needs so that her feet stay under her while the rest of her moves is for you to work
out from the package's documents; nothing in them is called a dance.

Keep the rig light: the whole figure in at most 1,000 triangles.

## Hand in

`config.json`, the motion file it names (with `dance` in it), `journal.md`, and the transcript.

## Pass lines (written before any run)

The machine reads only whether the dance holds together. Task 01's four (built, checked, whole, does not
fold), and, on `dance`, posed at 24 frames a second:

| | line |
| --- | --- |
| **Dance as timed** | the built rig holds an animation `dance` that lasts 4.0 s |
| **Closes** | with the physics taken out, no vertex in the last frame is more than 0.5 rig px from where it is in the first |
| **Both hands** | `handwear_l` and `handwear_r` each travel at least 100 rig px at their furthest vertex, measured from the middle of `topwear` |
| **Arms bend at the joints** | along its own length, neither an upper arm nor a forearm bends more than 8 degrees more than at rest |
| **Whole body** | every vertex of `topwear` travels at least 15 rig px, measured from the middle of `shoes` — the trunk goes somewhere, and not by sliding the figure along the floor |
| **On her feet** | the bottom of `legwear` stays within 6 rig px of where it meets `shoes` |
| **Keeps time** | read how fast the figure moves from each frame to the next, round the loop: at least half of the variation in that repeats every two beats |
| **Soft in the dance** | `topwear` differs from the same build without its physics by 3 to 15 rig px at its furthest vertex — task 04's line, on this motion |
| **Dance does not fold** | `rigc render --folds` over `dance` names no mesh |
| **Budget** | the build's `check` counts at most 1,000 triangles in the rig |

Travel is the diagonal of the box a vertex's path fills over the loop.

An arm bends at its elbow and its wrist and nowhere else. An arm part (`handwear_l`, `handwear_r`) runs
from the shoulder, under the sleeve, to the fingertips; by height above the part's lowest point at rest,
**her elbow is at about 0.54 and her wrist at about 0.20** — you cannot see that, so it is given. The upper arm is read
in three bands, 0.62 to 0.72, 0.72 to 0.82 and 0.82 to 0.92, the forearm in three, 0.22 to 0.30, 0.30 to
0.38 and 0.38 to 0.46, each at its middle (each must hold a vertex); a bend along a bone's own length is
the angle at its middle band, compared with the same reading at rest. The part names are the ones the
proposed plan gives; a part renamed, or made something other than what the plan made it, is not found and
its line fails.

## And a judge

Whether it is a dance is not something these lines can read, and they do not try. For every run that is
filed, the proctor renders `dance` with its physics as a clip — three times round, with a click on each
beat — and a person scores it without knowing whose it is: the clips carry letters, and the names are put
back after the scores are in. The score is recorded beside the machine's lines and does not change them.

The judge is asked three things, each out of 5: does it read as a dance; is it on the beat; does she stay
in one piece and on the ground.
