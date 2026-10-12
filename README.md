# rig-c exam

An open-book exam for AI agents: build a rig from one painting with the published rig-c tools, and
write down what you expected before each step.

The tools are written for agents that cannot see what they build. This repository measures whether that
holds for an agent that has never seen the tools: the only help is what ships in the packages. Where an
examinee is surprised — where what it expected and what happened differ — a document or a message is
missing something, and that line of the journal is what the exam is for.

## Rules

1. **Open book, closed neighbours.** You may read anything inside the two pinned packages once installed
   (`README.md`, `docs/`, `--help`, the examples they ship) and anything on their public repository pages.
   You may not read another examinee's run, and you may not ask a person.
2. **Pinned versions.** `package.json` at the root names the round's versions. `npm ci` installs them;
   use those and no others.
3. **Journal before you act.** Copy `JOURNAL.md` into your run. Before every command that changes
   something, write the entry's first three lines (what you read, what you expect, what you chose and
   what you turned down). After the command, write what happened. An entry written after the fact is
   worth nothing here; a wrong expectation written beforehand is the most useful line in the file.
4. **Submit the transcript.** The raw record of your session (commands and their output) goes in the run
   beside the journal. The two are compared.
5. **The grader rebuilds.** Only your inputs are trusted: `grade.py` builds from the files the task says
   you hand in, on the pinned versions. Outputs you paste are not read.
6. **Stopping is an answer.** If you cannot go on, write the last entry — what you tried, the message
   you could not act on — and submit. A run that stops honestly is graded as stopped, not discarded.

## Layout

    tasks/<task>/TASK.md        the problem, what you are given, what you hand in, the pass lines
    tasks/<task>/inputs/        the painting and its layers
    JOURNAL.md                  the journal's form
    grade.py                    the grader: python3 grade.py runs/<your run>
    runs/<date>-<model>-<task>/ one examinee's run (on the `runs` branch): journal.md, transcript, the
                                files handed in, result.json

## Submitting

`main` holds the exam and no runs, so a checkout of it shows you nobody's answers. Make
`runs/<YYYY-MM-DD>-<model>-<task>/` (`<task>` is the task's directory name, for example
`2026-10-13-somemodel-01-build`), put the run there, and open a pull request against the `runs` branch.
`python3 grade.py runs/<run>` writes `result.json`; you may run it yourself as often as you like — it is
the same grader, and what you learn from it belongs in the journal like any other step.

## What is in a round

Round 1: `@rig-c/parts` 1.11.0, `rig-c` 2.47.0, tasks 01 and 02 on one painting. The painting was
generated for this exam (`tasks/01-build/inputs/generation.json` records how) and is not one of the
packages' examples: their configs do not fit it.

## Licence

CC BY-NC 4.0, held by rig-c, covering the tasks, the painting and its layers, the grader and the runs:
free to use, share and adapt with credit, not for commercial use — see `LICENSE`. `NOTICE.md` names the
checkpoint the painting was generated with, See-through, and the tools the grader runs, and says what
submitting a run means.
