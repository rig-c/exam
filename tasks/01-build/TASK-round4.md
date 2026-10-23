# Task 01 — one painting to a rig that passes its check

> **Round 4's task 01**, kept for the runs filed on it, which sat Rounds 1 to 4's painting. Round 5 sets this task on a new
> painting: [`TASK.md`](TASK.md). The old painting and its layers left the tree with Round 5. To regrade a run filed on it,
> check out commit `f96b6b0` (its inputs, its grader and its pins), run `npm ci`, then `python3 grade.py runs/<run>`.

## Given

- `inputs/painting.png` — one character, standing, on white. 1664 × 2432.
- `inputs/layers/full/`, `inputs/layers/head/` — the painting split into layers by See-through, once over
  the whole figure and once over the head. You do not need a GPU; do not regenerate them.
- `inputs/seethrough.json` — the settings the layers were made with, including the head box.
- `../../package.json` — the pinned versions (`npm ci` at the repository's root installs them).

## Do

Write a `config.json` for this painting such that

    rig-parts build --config config.json --source inputs/painting.png \
      --full inputs/layers/full --head inputs/layers/head --out out

exits 0. The package's documents say what a config holds and how to arrive at one.

## Hand in

`config.json`, `journal.md`, and the transcript.

## Pass lines (written before any run)

| | line |
| --- | --- |
| **Built** | the command above exits 0 from your `config.json` alone, on the pinned versions |
| **Checked** | the build's `check` says PASS; the grader prints each bar's status |
| **Whole** | the build's own count of painting pixels no part holds (`uncovered_error_px`) is at most 4,200 |
| **Does not fold** | `rigc render --folds` over the idle names no mesh |

A person looks at one contact sheet of the idle for every run; that reading is recorded beside the
machine's, and does not change it.
