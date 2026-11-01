# Contributing

`rig-c/exam` is the open-book benchmark for AI agents building rigs and motions with the published `rig-c` toolchain.

## Getting the code running

From a clone, with [Bun](https://bun.sh) 1.4+, Node.js 22+, and Python 3 on `PATH`, install the pinned packages (`@rig-c/parts` and `rig-c`) and run the Basic grader against a run directory:

```sh
npm ci
python3 grade.py runs/<run>
```

For the Advanced edition (`advanced/R1`, `advanced/R2`, `advanced/R3`), each round directory carries its own `package.json` and `tools/grade.py` (`python3 advanced/R1/tools/grade.py --help`). To sit or submit an exam run, follow [README.md](README.md#sitting-it) and [advanced/README.md](advanced/README.md#sitting-it).

## Before you open a pull request

Run the documentation, results-table, and shared grader tests from `.github/workflows/pages.yml`:

```sh
python3 -B tools/check_readme.py
python3 -B -m unittest discover -s tools -p 'test_readme.py' -v
python3 results.py --check
python3 -B -m unittest discover -s tools -p 'test_results.py'
python3 -B -m unittest discover -s tools -p 'test_mannequin_docs.py' -v
python3 -B -m unittest discover -s tools -p 'test_task03_next_repin.py' -v
python3 -B -m unittest discover -s tools -p 'test_task03_activation.py' -v
python3 advanced/tools/test_shared.py
python3 advanced/results.py --check
```

If you touch `.github/`, `tools/profile_results.py`, `tools/test_profile_results.py`, or `tools/fixtures/`, also run the profile-results test suite from `.github/workflows/profile-results-test.yml`:

```sh
python3 -m pip install --no-cache-dir -r .github/requirements-profile-tests.txt
python3 -B -m unittest discover -s tools -p 'test_profile_results.py' -v
```

Pull requests that add or change `runs/<run>/` are regraded in CI by `.github/workflows/grade.yml` (`npm ci` and `python3 grade.py "runs/<name>"`).

## Reporting a change

- **Issue first.** Open an issue before changing a task, grader, tool, or document, naming the command, the verbatim output, and what should change. (Exam sitting submissions open a pull request adding `runs/<YYYY-MM-DD>-<model>-<task>/` directly; see [Submitting](README.md#submitting).)
- **One issue per pull request.** Keep each change scoped to one issue.
- **Conventional Commits.** Write commit messages, code, and documentation in English using [Conventional Commits](https://www.conventionalcommits.org/) with a scope (`feat(grade):`, `fix(results):`, `docs(readme):`). Include no private paths or unpublished material.

## Where further rules live

- [AGENTS.md](AGENTS.md) — README scope, word-count cap, and documentation maintenance rules.
- [README.md](README.md) and [advanced/README.md](advanced/README.md) — exam rules, tasks, manual build layout, and submission instructions.
- [PROCTOR.md](PROCTOR.md) and [JOURNAL.md](JOURNAL.md) — proctoring checklist and journal hash-chain rules.
- [ROUNDS.md](ROUNDS.md), [NOTICE.md](NOTICE.md), and [LICENSE](LICENSE) — round history, attribution, and CC BY-NC 4.0 licence terms.
