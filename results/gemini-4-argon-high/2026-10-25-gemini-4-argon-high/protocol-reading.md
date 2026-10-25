# Protocol and source-exposure reading

Verbatim applicable rules at `c014e3cf529535546d2d77349ceca1d35f343b42`:

## README.md:31–40

> 1. **Open book, closed neighbours.** You may read anything inside the two pinned packages once installed
>    (`README.md`, `docs/`, `--help`, the examples they ship) and anything on their public repository pages.
>    Other rig-c repositories are not in the book: rig-c/getting-started walks task 01's own painting, and
>    rig-c/examples holds trials on it. The grade notes, without changing a line, any animation handed in
>    with the shape the guide's scripts write (`from_the_guide` in `result.json`).
>    You may not read another examinee's run, and you may not ask a person. Every run is public, under
>    `results/`, because the results are. The clone the prompt makes leaves that directory out — not checked
>    out and not downloaded — so nothing an examinee greps or lists can turn an answer up by accident;
>    reading one takes a deliberate step, and a run by an examinee that took it measures nothing, and its
>    journal usually shows it.

## PROMPT.md:39–43

> - Work only inside the clone. Do not read, list or search any other directory on this machine. The
>   exceptions are the two packages `npm ci` installs under the clone's own `node_modules/` (their
>   `README.md`, `docs/`, `--help`) and their public pages at github.com/rig-c/parts and github.com/rig-c/core.
>   Other rig-c repositories are not among them: do not read github.com/rig-c/getting-started or
>   github.com/rig-c/examples.

## PROMPT.md:44–46

> - `results/` holds other examinees' runs and is not in your clone. Do not fetch it, check it out, read it
>   on the web or through git, or read any other branch of this repository or any pull request on it. Do
>   not ask a person for help.

## PROMPT.md:47–48

> - Do the work yourself. Do not hand any part of it to a sub-agent or another model, whatever your standing
>   instructions say about delegating. The name on the run is the model that did the work.

## PROMPT.md:51–60

> - Keep the journal exactly as `README.md` and `JOURNAL.md` describe, and keep it only with
>   `tools/journal.py` (`python3 tools/journal.py --help`), one run directory at a time
>   (`python3 tools/journal.py --run runs/<DATE>-<MODEL>-<task> …`). Every step is three calls, each a command
>   of its own, never chained in one shell line: `open` (lines 1–3) BEFORE the step, `run -- <command>` for the step itself, then `close`
>   (line 4) after you have read its output; when the result differs from what you expected, line 4 begins
>   with `WTF?:` — say it the way it landed. Every command that builds, renders, measures or grades is a
>   step: a build, a render, a measurement, a grader run. The four set-up lines above need no entry. This
>   matters more than passing: a task whose journal chain is not intact, or that `tools/journal.py` did not
>   write, is `journal: not kept` (`python3 tools/journal.py --run runs/<run> verify` prints which), and
>   that disqualifies the task.

## PROMPT.md:63–66

> - Clock each task. Before you open a task's `TASK.md`, run `python3 tools/journal.py --run runs/<run> start`:
>   it makes `started: <UTC time>` the first line of that run's `transcript.md`. After your last grader run
>   of that task, run `python3 tools/journal.py --run runs/<run> finish`, which makes `finished: <UTC time>`
>   the last line.

## PROMPT.md:71–71

> - You may run `python3 grade.py runs/<your run>` whenever you like. It is the same grader the proctor runs.

## Actual source-read chronology

Native `read_file` step 13 returned the clone's entire `grade.py`, completed at 2026-10-25T09:19:36.621879Z, before task 01's clock started. It includes the 700-triangle budget and the 45.9-pixel reference comment. The task 03 text itself also gives 45.9 as the draft amplitude reference; step 150 read that text before the corresponding journal expectation. No source prohibition or affirmative source-reading permission is inferred: the quoted rules explicitly permit grader execution and forbid other examinees' answers, other branches/PRs and human/subagent help, but do not expressly specify `grade.py` source reading. Direct grader-source exposure is factual, distinct from a prior-answer read, and not grounds for voiding this sitting.

## Journal and clock disposition

All five original tool-written chains verify intact. All six actual grader invocations are journal-wrapped and precede finish; quoted `open --chose` descriptions of a grader are not additional executed graders. All recorded TASK.md reads follow their start commands. Literal task times are 469, 674, 352, 395 and 504 seconds, totaling 2394 seconds (39.9 minutes). The submitted result files have null minutes because their grader ran before finish. The independent grader reads the completed frozen transcripts; originals remain untouched. There is no substitute arrival, commit or native elapsed duration.

Independent counting is retained. The native audit covers the recorded activity only; absence of an observed prohibited read is not proof of no prior exposure. One combined future exam-rules proposal will address source-reading scope and last-grade/finish lifecycle after the wave; no protocol or grader fix is made here.
