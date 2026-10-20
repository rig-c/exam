# The prompt every Advanced examinee is given

Verbatim, once per round, with `<MODEL>` replaced by the model's exact identifier (lower case, no
spaces) and `<ROUND>` by `R1`, `R2` or `R3`. **One round per fresh session**: R2 and R3 are never
sat in the session that sat the round before them, and each round gets a fresh copy of its package.
The person starting the run fills `<MODEL>` in: a model asked for its own name often gets it wrong.

---

You are sitting an exam. "You" means the model reading this, in this session — not a session that may
hand work on. Follow these instructions exactly.

**Before anything else:** if this session has already seen this round's package (`PROBLEM.md`, its
inputs), a solution to it, or anyone's report of one — including a sub-agent's, and including an earlier
round of this exam — stop and say so. Receiving this prompt is not that, however it arrived and however
many times; only the package, a solution or a report count. A sitting is one model, one fresh session,
one fresh copy of the round's package; a repeat in a session that has seen an answer measures the
answer, not you.

**Set up**

The package for this round is the directory you were started in. It holds `PROBLEM.md`, `JOURNAL.md`,
`PROMPT.md`, `package.json`, `tools/grade.py` and `inputs/`, and nothing else. Run:

    npm install

Read `PROBLEM.md` first; it states the task, the pass table and the rules. Your run directory is `run/`
inside the package.

**Boundaries — these are exam rules**

- Work only inside the package directory. Do not read, list or search any other directory on this
  machine. The exceptions are the three packages `npm install` puts under the package's own
  `node_modules/` (their `README.md`, `docs/`, `--help`) and their public pages.
- Do not read another examinee's `run/`, any other copy of this exam, any branch of a repository that
  holds it, or any pull request on one. Do not ask a person for help, and do not message any session
  outside this one.
- Do the work yourself. Do not hand any part of it to a sub-agent or another model, whatever your
  standing instructions say about delegating. The name on the run is the model that did the work.
- Do not commit or push anything. The run stays on this machine.
- Keep the journal exactly as `PROBLEM.md` and `JOURNAL.md` describe: lines 1–3 of an entry BEFORE the
  step, line 4 after it; when the result differs from what you expected, line 4 begins with `WTF?:`.
  This matters more than passing: a journal whose lines 1–3 were written after the step, or whose line 4
  was filled in for several steps at once, disqualifies the sitting. Write the entry, run the step, then
  write line 4 — every time.
- Keep `run/transcript.md`: every command you ran that changed or built something, in order, with the
  last lines of its output.
- Clock the round. Before you open `PROBLEM.md`, run `date -u +%Y-%m-%dT%H:%M:%SZ` and make its output
  the first line of `run/transcript.md`, as `started: <output>`. After your last grader run, run it
  again and make it the last line, as `finished: <output>`. Do not estimate either.
- Tokens. If the agent you run in can report what the session has spent, write it as `run/usage.json`
  when you finish — `{"input_fresh": n, "input_cached": n, "output": n}`, or `{"total": n}` if that is
  all it gives, with `"source"` saying where the figure came from. If it cannot report, leave the file
  out. Do not estimate.
- You may run `python3 tools/grade.py --round <ROUND> …` (the inputs are listed in `PROBLEM.md`)
  whenever you like. It is the same grader the proctor runs.
- If you cannot go on, write the last journal entry — what you tried and the message you could not act
  on — and stop. Do not invent results.

**Last: what the tools were missing**

Before you hand in, write `run/tools.md`: what you missed while using the tools — not the exam, the
three packages. One entry per thing, as many as there were:

    ## <a short title>
    - **I was trying to:** what you wanted to do, in your own words
    - **The tool gave me:** the message, file or section you had — quote it
    - **What would have helped:** the sentence, message, option or command you wished for
    - **Cost:** roughly how long it took you, and whether you got there in the end

Write what you actually ran into, from your journal and transcript. Do not pad it.

**Then reply with** the five answers `PROBLEM.md` asks for under its last heading, and the grader's
printed lines verbatim from your last run.
