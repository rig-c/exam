# rig-c exam

An open-book exam for AI agents: build a rig from one painting with the published rig-c tools, and
write down what you expected before each step.

The tools are written for agents that cannot see what they build. This repository measures whether that
holds for an agent that has never seen the tools: the only help is what ships in the packages. Where an
examinee says *WTF?* — where what it expected and what happened differ — a document or a message is
missing something, and that line of the journal is what the exam is for.

## Rules

1. **Open book, closed neighbours.** You may read anything inside the two pinned packages once installed
   (`README.md`, `docs/`, `--help`, the examples they ship) and anything on their public repository pages.
   You may not read another examinee's run, and you may not ask a person. The runs are public, on the
   `runs` branch, because the results are; a run by an examinee that read them measures nothing, and its
   journal usually shows it.
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

## Results

[RESULTS.md on the `runs` branch](https://github.com/rig-c/exam/blob/runs/RESULTS.md): one row per
examinee, generated from the regraded runs, each cell linking to the journal and the proctor's reading.

## Sitting it

[`PROMPT.md`](PROMPT.md) is the prompt every examinee is given, verbatim — paste it into a coding agent
(one that can run commands and read and write files) with the model's name filled in. One model, one
fresh session, one fresh clone.

## Submitting

`main` holds the exam and no runs. Make `runs/<YYYY-MM-DD>-<model>-<task>/` for each task you sat
(`<task>` is the task's directory name, for example `2026-10-13-somemodel-01-build`), commit only those
directories on a branch of your fork, and open a pull request against the `runs` branch.

Anyone may sit it with any model, in any coding agent. The pull request's form asks which model, which
agent, and whether a person stepped in; a run with help is still worth having, labelled as one. A workflow
regrades the run on the pull request and prints its lines in the job's summary.

`python3 grade.py runs/<run>` writes `result.json`; you may run it as often as you like — it is the same
grader, and what you learn from it belongs in the journal like any other step. The proctor regrades every
run from the files it hands in before it is merged, looks at the pictures, and adds a `READING.md`: what
the journal caught, checked against the packages, and which of it was filed on the tools. A run's own
`result.json` is not trusted, and neither is its report.

## What is in a round

Round 1: `@rig-c/parts` 1.11.0, `rig-c` 2.47.0, tasks 01 and 02 on one painting. Round 2, on the same
versions: task 03, on a second painting of the same character, where the tool's draft does not pass as
proposed. Both paintings were generated for this exam (each task's `inputs/generation.json` records how)
and neither is one of the packages' examples: their configs do not fit.

## Licence

CC BY-NC 4.0, held by rig-c, covering the tasks, the painting and its layers, the grader and the runs:
free to use, share and adapt with credit, not for commercial use — see `LICENSE`. `NOTICE.md` names the
checkpoint the painting was generated with, See-through, and the tools the grader runs, and says what
submitting a run means.
