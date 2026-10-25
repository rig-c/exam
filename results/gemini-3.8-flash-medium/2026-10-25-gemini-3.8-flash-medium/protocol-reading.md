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

Native `read_file` steps 42, 44, 46 and 48 returned `grade.py` lines 1–150, 151–320, 321–450 and 451–490, completed at 09:00:26.610778, 09:00:30.118825, 09:00:33.792845 and 09:00:36.843864 UTC. Step 42 returned `BUDGET = 700` at line 32. The read precedes the first full build; later task 04 tuning also consulted grader output/source.

The rules explicitly permit running the grader and explicitly forbid other examinees' answers, the excluded results, other branches/PRs and human/subagent help. Direct reading of the clone's `grade.py` source is not explicitly named as permitted or forbidden in these excerpts. Its source exposure is therefore recorded without inventing a ban or an affirmative source-reading permission. It is not, by itself, a prior-answer read or grounds for voiding this sitting. The 700-triangle cap is also explicit in task 04.

## Journal and clock disposition

All five original tool-written chains verify intact. Each transcript nevertheless finished before one later unjournalled grader call; the per-task UTC start/end table is in `clock-audit.json`. The proctor ruling retains independent counting because these are coverage/finish-order gaps, not a broken/not-kept chain. Findings are preserved in `who.json.journal_rulings`, not silently erased. The exact literal total is 2009 seconds (33.483333… minutes, 33.5 to one decimal), excluding the later graders. It is not a compliant complete-task benchmark duration. The original grader's per-task rounded metadata is preserved; adding already-rounded inputs is not the exact measured total.

One combined future exam-rules proposal will address the source-reading scope and last-grade/finish lifecycle after this wave. No protocol or grader fix is made here.
