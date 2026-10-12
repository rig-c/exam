# Task 04 — soft

The painting of task 01, and a rig for it that builds — yours from task 02, or a new one.

## Given

- Task 01's inputs (`../01-build/inputs/`).
- `hop.json` — one animation, `hop`: a one-second jump, keyed on the bone the proposal names `hip`.

## Do

Make her chest soft: when she hops, a patch of her top should lag the body and catch up — moved by
physics, not by keys — and nothing else about the top should come loose.

Your rig must carry `hop` exactly as `hop.json` gives it (the same bone, property and keys), beside whatever
other animations it has. The grader builds your rig twice, once as you hand it in and once with every
physics constraint taken out, poses both on `hop`, and reads how far the part the plan calls `topwear`
differs between them.

And keep the rig light: the whole figure in at most 700 triangles.

The package's documents have a recipe for a soft region. Read what it costs before you copy it.

## Hand in

`config.json`, the motion file it names (with `hop` in it), `journal.md`, and the transcript.

## Pass lines (written before any run)

Task 01's four (built, checked, whole, does not fold), and:

| | line |
| --- | --- |
| **Hop as given** | the built rig holds `hop` exactly as `hop.json` gives it |
| **Soft** | on `hop`, `topwear` differs from the same build without its physics by 3 to 15 rig px at its furthest vertex — under 3 nothing is soft, over 15 it has come off |
| **A patch** | at least 8 of `topwear`'s vertices move over half a rig px, and at most 80 % of them — a patch, not the garment |
| **Hop does not fold** | `rigc render --folds` over `hop` names no mesh |
| **Budget** | the build's `check` counts at most 700 triangles in the rig |

A person looks at the chest with and without the physics, at the landing, for every run.
