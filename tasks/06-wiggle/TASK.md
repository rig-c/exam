# Task 06 — wiggle

The painting of task 01 and your rig for it. This time the dance is given to you, and the machine reads
all of it.

## Given

Task 01's inputs (`../01-build/inputs/`). Nothing else: no keys, no pose, no reference clip.

The music is 120 beats a minute. Eight beats are 4.0 seconds.

## Do

Give the rig one more animation, named `wiggle`: a loop of exactly 4.0 s in which she wiggles her hips.

- **The hips** go out to one side on each beat — left, right, left, right: four times each way in the
  loop, no more and no fewer — and they go far enough to see.
- **It is the hips that go**, not the whole of her: her shoulders stay nearly where they were, and her
  feet stay where they are.
- **Her arms** are held with the elbows bent a little, the forearms folded in toward her body, for the
  whole loop.
- **Her head** tilts from side to side in time with the hips.
- **Her skirt** swings — on physics, not on keys.

As in task 05, the rig as task 04 left her cannot do this: her legs are one flat piece on the hip and her
shoes are another on the ground, and nothing swings her skirt but the idle's keys. Keep the rig light: at
most 1,000 triangles.

## Hand in

`config.json`, the motion file it names (with `wiggle` in it), `journal.md`, and the transcript.

## Pass lines (written before any run)

Task 01's four (built, checked, whole, does not fold), and, on `wiggle` posed at 24 frames a second — with
the physics taken out except where a line says otherwise:

| | line |
| --- | --- |
| **Wiggle as timed** | the built rig holds an animation `wiggle` that lasts 4.0 s |
| **Closes** | no vertex in the last frame is more than 0.5 rig px from where it is in the first |
| **Four each way** | at least 0.7 of the sideways motion of the top of `bottomwear` comes four times a loop |
| **Hips go far** | the top of `bottomwear` travels at least 24 rig px from side to side |
| **Hips, not shoulders** | the top of `topwear` travels at most half as far, side to side, as the top of `bottomwear` |
| **Elbows in** | through the whole loop each forearm is folded in toward the body by 10 to 60 degrees more than at rest |
| **Head sways** | `face` tilts through at least 8 degrees, and at least 0.6 of that tilting comes four times a loop |
| **Skirt swings** | with its physics, the hem of `bottomwear` differs from the same build without them by at least 4 rig px at its furthest vertex, and by no more than half the part's height |
| **On her feet** | the end of each leg (`legwear`) stays within 6 rig px of where it meets `shoes`, and `shoes` does not move more than 2 rig px |
| **Wiggle does not fold** | `rigc render --folds` over `wiggle`, with its physics, names no mesh |
| **Budget** | the build's `check` counts at most 1,000 triangles in the rig |

How each is read, since you cannot see the figure:

- A part's *top*, *hem* and *end* are bands of its height at the rest pose: the top is the highest tenth
  of its vertices, the hem the lowest tenth, a leg's end the lowest 4 % — split into two legs at the widest
  gap between them, each leg's end taken at its middle.
- A forearm's fold is the angle at the elbow, read off three bands of an arm part (`handwear_l`,
  `handwear_r`) — the upper arm at 80 to 95 % of the part's height, the elbow at 58 to 70 %, the wrist at
  30 to 42 % — and counted toward the middle of `topwear`. It is compared with the same angle at rest.
- The head's tilt is the angle of one edge of `face`.
- "Four times a loop" is the share of a signal's variation carried by its fourth harmonic.

The part names are the ones the proposed plan gives; a part renamed, or left as a flat piece where a line
reads a band of its vertices, is not found and its line fails.

No person judges this one.
