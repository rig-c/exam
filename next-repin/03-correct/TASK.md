# Task 03 — correct a supplied draft

This is a candidate for a future edition. It is not the current task.

## Given

- `inputs/draft.json` — the static draft supplied for this task.
- The task's painting, full and head layers, and See-through metadata. Until activation, these are
  the unchanged files in `tasks/03-correct/inputs/` at the repository root.

## Do

Write a `config.json` from the supplied draft for this painting. The draft can pass the package's
build and check while failing the exam's requirements. Decide what needs correcting from the
configuration, the tool's pictures and measurements, and the requirements below. Record what you
used to decide in the journal. A fresh proposal does not replace the supplied draft as this task's input.

Build from your configuration alone:

    rig-parts build --config config.json --source inputs/painting.png \
      --full inputs/layers/full --head inputs/layers/head --out out

## Hand in

`config.json`, `journal.md`, and the transcript.

## Pass lines

| | line |
| --- | --- |
| **Built** | the command above exits 0 on this edition's pinned versions |
| **Checked** | the build's `check` says PASS |
| **Whole** | `uncovered_error_px` is at most 3,500 |
| **Does not fold** | `rigc render --folds` over the idle names no mesh |
| **Kept** | at least eight meshes still deform |
| **Still moves** | over the idle, the back hair travels at least 23 rig px against the head |

The independent travel reading is the furthest any back-hair vertex gets from its first-frame
position, measured relative to the head bone's origin, at 12 fps over the idle. It is the existing
`grade.py` travel reading. A person also looks at five idle frames and what the journal says was wrong;
that reading is recorded beside the machine's and does not change it.
