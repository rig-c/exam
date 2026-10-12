# Task 06 — walk

The painting of task 01 and your rig for it. She faces you; make her walk toward you, on the spot.

## Given

Task 01's inputs (`../01-build/inputs/`). Nothing else: no keys, no pose, no reference clip.

One cycle is two steps and lasts exactly 1.0 s.

## Do

Give the rig one more animation, named `walk`: a loop of exactly 1.0 s in which she walks in place — one
foot leaves the ground, comes back, then the other.

A walk is not a matter of taste the way a dance is. Whoever walks does these, and each is a line below:

- the feet take turns, and the one on the ground stays where it is;
- the body's weight goes over the foot that is standing;
- the body comes down at each step — twice in a cycle;
- the arm opposite the lifted foot swings forward, the other back.

Seen from the front, a limb that swings toward you or away from you does not turn on the page: it gets
shorter and longer. What the rig can do about that is for you to find in the package's documents. One fact
about this painting, since you cannot see it: her skirt is drawn in front of her hands. An arm swinging
back goes in behind the skirt; an arm swinging forward comes out beside it.

As in task 05, the rig as task 04 left her cannot do this — her legs are one flat piece on the hip and
her shoes are one piece on the ground. Keep the rig light: at most 1,000 triangles.

## Hand in

`config.json`, the motion file it names (with `walk` in it), `journal.md`, and the transcript.

## Pass lines (written before any run)

Task 01's four (built, checked, whole, does not fold), and, on `walk` with the physics taken out, posed at
48 frames a second:

| | line |
| --- | --- |
| **Walk as timed** | the built rig holds an animation `walk` that lasts 1.0 s |
| **Closes** | no vertex in the last frame is more than 0.5 rig px from where it is in the first |
| **Steps** | each foot leaves the ground by at least 10 rig px |
| **One at a time** | the two feet are never both more than 2 rig px off the ground |
| **Stands** | each foot is on the ground for at least 0.40 of the cycle, and while it is, no vertex of it moves more than 2 rig px sideways |
| **Over the standing foot** | when a foot is at its highest, the middle of `topwear` is at least 4 rig px toward the other foot from its mean place |
| **Bobs twice** | the middle of `topwear` rises and falls at least 3 rig px, and at least half of that motion comes twice a cycle |
| **Arms opposite** | when a foot is at its highest, the hand on the other side is at least 15 rig px further out from the trunk than the hand on its own side — each measured against its own mean over the cycle |
| **Walk does not fold** | `rigc render --folds` over `walk`, with its physics, names no mesh |
| **Budget** | the build's `check` counts at most 1,000 triangles in the rig |

The feet are the two halves of the part the plan calls `shoes`, split at the widest gap between its
vertices in the first frame; a foot's height is its lowest vertex, and the ground is the lowest that
vertex gets. A hand is the lowest tenth of an arm part's vertices (`handwear_l`, `handwear_r`). A part
renamed, or left as a single flat piece with no vertices of its own to move, is not found or does not
step, and its lines fail.

No person judges this one.
