# Task 03 — a draft that does not pass

A new painting: the same character, seated, one hand in her lap, her ankles crossed.

## Given

- `inputs/painting.png`, `inputs/layers/full/`, `inputs/layers/head/`, `inputs/seethrough.json` — as in
  task 01, for this painting.

## Do

Write a `config.json` for this painting such that

    rig-parts build --config config.json --source inputs/painting.png \
      --full inputs/layers/full --head inputs/layers/head --out out

exits 0.

On this painting, what the tool proposes does not pass its own check as proposed. Something has to be
corrected, and what, and how, is the task. The tool's messages and pictures are what you have to decide
from; say in the journal which of them you decided from.

## Hand in

`config.json`, `journal.md`, and the transcript.

## Pass lines (written before any run)

| | line |
| --- | --- |
| **Built** | the command above exits 0 from your `config.json` alone, on the pinned versions |
| **Checked** | the build's `check` says PASS; the grader prints each bar's status |
| **Whole** | the build's own count of painting pixels no part holds (`uncovered_error_px`) is at most 3,500 |
| **Does not fold** | `rigc render --folds` over the idle names no mesh |
| **Kept** | the build still deforms at least the eight meshes the proposal drafts — a part is not made to pass by being made rigid |

A person looks at five frames of the idle for every run and at what the journal says was wrong; that
reading is recorded beside the machine's, and does not change it.
