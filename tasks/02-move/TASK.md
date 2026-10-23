# Task 02 — a gesture, and hair that trails

Do [task 01](../01-build/TASK.md) first; this one starts from a config that builds.

## Given

The same inputs as task 01 (`../01-build/inputs/`), and your own `config.json` from it.

## Do

1. **A gesture.** Give the rig one animation beside its idle in which she moves inside what was painted —
   a turn of the head, a lean, a lift of the shoulders — at least one second long, and in which nothing comes
   apart. This rig is a living illustration: nothing in it was painted from another angle, so a gesture that
   swings a limb past where the painting holds it shows the background where the limb was.
2. **Hair that trails.** Make the hair strands that hang free lag the head when it moves, on physics
   rather than keys — at least two bones.

The package's documents have a recipe for the hair. Nothing the package proposes does either for you.

## Hand in

`config.json`, the motion file it names, `journal.md`, and the transcript. Every `.json` file in your run
directory is copied beside the inputs before the build.

## Pass lines (written before any run)

Task 01's four, on this config, and:

| | line |
| --- | --- |
| **Trails** | the built rig holds physics constraints on at least two bones, and gates green |
| **Gestures** | an animation other than `idle`, at least 1 s, in which `face`'s furthest vertex travels at least 22 rig px measured from the middle of `bottomwear` |
| **Holds together** | over that animation at 12 fps, every pair of parts the grader names is read, and no frame opens on any of them: every limb joint the build's check declares, and `topwear` with each upper arm (the arm part, where the arm is not cut). Read with `rigc render --seam`, a frame opening when its gap or its ghost holds more cells than its box is long — the parts check's own floor for a seam over motion |
| **Gesture without folding** | `rigc render --folds` over that animation names no mesh |

The 22 is the idle's own travel of `face` on this painting (9.1 rig px) and half of what a reference gesture adds
to it (35.0: the head turned 8°, the chest leaned 3° and lowered 6 rig px, no limb keyed), rounded down.

The animation these lines read is the one, of those at least 1 s long, in which `face` travels furthest.

A person looks at six frames of the gesture for every run. Whether it *reads* as one is recorded beside the
machine's lines, and does not change them.
