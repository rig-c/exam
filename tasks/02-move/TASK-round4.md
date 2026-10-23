# Task 02 — make her wave, and let her hair trail

> **Round 4's task 02**, kept for the runs filed on it, which sat Rounds 1 to 4's painting. Round 5 sets this task on a new
> painting: [`TASK.md`](TASK.md). The old painting and its layers left the tree with Round 5. To regrade a run filed on it,
> check out commit `f96b6b0` (its inputs, its grader and its pins), run `npm ci`, then `python3 grade.py runs/<run>`.

Do [task 01](../01-build/TASK.md) first; this one starts from a config that builds.

## Given

The same inputs as task 01 (`../01-build/inputs/`), and your own `config.json` from it.

## Do

1. **A wave.** Give the rig one animation beside its idle in which she waves: at least one second long,
   in which a bone rises at least 150 rig px more than the median of the bones does. What is measured is
   where the bones are, not the drawing: a wave that turns only the forearm can lift the hand a long way while
   no bone rises that far.
2. **Hair that trails.** Make the hair strands that hang free lag the head when it moves, on physics
   rather than keys — at least two bones.

The package's documents have a recipe for each. Nothing the package proposes does either for you.

## Hand in

`config.json`, the motion file it names, `journal.md`, and the transcript. Every `.json` file in your run
directory is copied beside the inputs before the build.

## Pass lines (written before any run)

Task 01's four, on this config, and:

| | line |
| --- | --- |
| **Trails** | the built rig holds physics constraints on at least two bones, and gates green |
| **Moves** | an animation other than `idle`, at least 1 s, in which some bone rises ≥ 150 rig px more than the median bone does |
| **Moves without folding** | `rigc render --folds` over that animation names no mesh |

A person looks at six frames of the wave for every run. Whether it *reads* as a wave is recorded beside
the machine's lines, and does not change them.
