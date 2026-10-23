# Journal — <model>, <task>, <date>

One entry per step. Every command that builds, renders, measures or grades is a step: a build, a
render, a measurement, a grader run. A file you write by hand (a config, written with an editor) is not a
step by itself: name it in line 3 of the step that first uses it. The four set-up lines in `PROMPT.md`
need no entry.

Keep the journal only with `tools/journal.py` (`python3 tools/journal.py --help`), in the task's run
directory (`--run runs/<date>-<model>-<task>`); it numbers the entries, stamps them and writes the run's
`journal.md` and `transcript.md`. For every step, three calls, each a command of its own:

    python3 tools/journal.py --run runs/<run> open --read "…" --expect "…" --chose "…"   lines 1–3, before the step
    python3 tools/journal.py --run runs/<run> run -- <the step's command>                the step
    python3 tools/journal.py --run runs/<run> close --happened "…"                       line 4, after you read its output

Line 4 quotes at least 12 characters of what the step printed (`--help` says how it is matched), or begins
with `WTF?:`. `start` comes before you open the task's `TASK.md`, `finish` after its last grader run. Do
not write or edit `journal.md`, `transcript.md` or `.journal/` by hand: a journal whose chain `python3
tools/journal.py --run runs/<run> verify` does not print as intact, or that the tool did not write, is
`journal: not kept`, and the task is disqualified.

## Entry <n>

1. **Read:** which document, section or message this step rests on (path and heading, or the message quoted).
2. **Expect:** what the step will produce, concretely — an exit code, a file, a number, a line of output.
3. **Chose / turned down:** what you are about to do, and the alternative you considered and why not.
4. **Happened:** what the step actually produced. If it differs from line 2, begin the line with
   `WTF?:` and say in one sentence what you now think you misread — or that nothing told you. Say it
   the way it landed. Politeness is not graded here; a line that understates the surprise hides it.
   The grader counts a line 4 that begins `WTF?:` (`tools/journal.py` writes it as
   `4. **Happened** (<time>): WTF?: …`); a `WTF?:` anywhere else in the line is not counted.

## At the end

Written with `python3 tools/journal.py --run runs/<run> end --guessed "…" --missing "…"`:

- **Where I guessed:** every value you wrote without a source (a number, a name), and what you would
  have needed to read to not guess.
- **What I could not find:** questions you had that no document or message answered.
