# The prompt every examinee is given

Verbatim, with `<MODEL>` replaced by the model's exact identifier (lower case, no spaces — for example
`gemini-2.5-pro`) and `<DATE>` by the day the run starts. One model per fresh session and per fresh clone.
The person starting the run fills `<MODEL>` in: a model asked for its own name often gets it wrong.

---

You are sitting an exam. "You" means the model reading this, in this session — not a session that may
hand work on. Follow these instructions exactly.

**Before anything else:** if this session has already seen these tasks, a run of them, or anyone's
report of one — including a sub-agent's — stop and say so. A sitting is one model, one fresh session,
one fresh clone; a repeat in a session that has seen an answer measures the answer, not you.

**Set up**

    git clone --single-branch --branch main https://github.com/rig-c/exam.git exam-<MODEL>
    cd exam-<MODEL>
    npm ci

Read `README.md` first; it states the rules. Then do `tasks/01-build/TASK.md`, then
`tasks/02-move/TASK.md`, then `tasks/03-correct/TASK.md`, in that order.

Your run directories are `runs/<DATE>-<MODEL>-01-build/`, `runs/<DATE>-<MODEL>-02-move/` and
`runs/<DATE>-<MODEL>-03-correct/` inside the clone.

**Boundaries — these are exam rules**

- Work only inside the clone. Do not read, list or search any other directory on this machine. The
  exceptions are the two packages `npm ci` installs under the clone's own `node_modules/` (their
  `README.md`, `docs/`, `--help`) and their public pages at github.com/rig-c/parts and github.com/rig-c/core.
- Do not open `results/` — it holds other examinees' runs — and do not read any other branch of this
  repository or any pull request on it. Do not ask a person for help.
- Do the work yourself. Do not hand any part of it to a sub-agent or another model, whatever your standing
  instructions say about delegating. The name on the run is the model that did the work.
- bun (1.2 or later), npm and python3 must be installed. No GPU is needed and none may be used.
- A build can take a minute or more. Let it finish before you read its result.
- Keep the journal exactly as `README.md` and `JOURNAL.md` describe: lines 1–3 of an entry BEFORE the
  step, line 4 after it; when the result differs from what you expected, line 4 begins with `WTF?:` — say it the way it landed.
  This matters more than passing.
- Keep `transcript.md` in each run directory: every command you ran that changed or built something, in
  order, with the last lines of its output — enough to show what happened.
- Clock each task. Before you open a task's `TASK.md`, run `date -u +%Y-%m-%dT%H:%M:%SZ` and make its
  output the first line of that run's `transcript.md`, as `started: <output>`. After your last grader run
  of that task, run it again and make it the last line, as `finished: <output>`. Do not estimate either.
- You may run `python3 grade.py runs/<your run>` whenever you like. It is the same grader the proctor runs.
- If you cannot go on with a task, follow rule 6 of the README: write the last entry — what you tried and
  the message you could not act on — and move to the next task. Do not invent results.

**Hand in**

When all three tasks are done or stopped:

    git checkout -b run/<MODEL>
    git add runs/<DATE>-<MODEL>-01-build runs/<DATE>-<MODEL>-02-move runs/<DATE>-<MODEL>-03-correct
    git commit -m "run: <MODEL>, <DATE>"
    git push origin run/<MODEL>      # or to your fork, then open a pull request against `main`

Add only those three directories — and inside them only `config.json`, any other `.json` you wrote,
`journal.md`, `transcript.md` and `result.json`; do not add build output (`out/`, `work/`) or
`node_modules/`. If you cannot push, leave the directories in place and say where the clone is.

**Then reply with**

1. For each task, the grader's printed lines verbatim from your last run of it.
2. For task 03: what was wrong with the draft, which message or picture told you, and exactly what you changed.
3. How many journal entries you wrote per task, and how many begin line 4 with `WTF?:`.
4. The three things that cost you the most time, each with the document section or message involved.
