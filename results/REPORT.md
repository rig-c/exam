# The proctor's report — the first sittings, 2026-10-12 and 13

Written by the proctor, by hand, from the runs in this directory. [README.md](README.md) is the generated
table; this page says what the table cannot: which rows count as what, what the journals found, and what
the exam itself got wrong. Versions: `@rig-c/parts` 1.11.0, `rig-c` 2.47.0.

## Which runs count

Seven runs, every one of them passing every line (4 of 4, 7 of 7, 5 of 5), each regraded by the proctor
from the files it handed in and found the same as its own report. They are not seven models.

| run | what it is | counts as |
| --- | --- | --- |
| `haiku` | Claude Haiku, as a sub-agent of the proctor's session, by design, with no other context | an independent sitting |
| `gemini-3.8-flash` | Gemini 3.8 Flash, itself, in the session it was started in | an independent sitting |
| `gpt-6.1-sol-20261013` | Sol 6.1, as a sub-agent of a Sol 6.1 session | an independent sitting — the one that is this model end to end |
| `gpt-6.1-sol` | Sol 6.1, as a sub-agent of a `gpt-6-astra` session | an independent sitting of Sol 6.1, briefed by another model |
| `gpt-6-sol` | `gpt-6-sol`, as a sub-agent of a `gpt-5.6-sol` session; whether that name is Sol 6.1 is not established | an independent sitting of a model the proctor cannot name |
| `codex-direct` | `gpt-6-astra` itself, repeating in the session that had seen its sub-agent's answers | **void** as a sitting; kept as a specimen |
| the run named `gpt-6-astra` | `gpt-5.6-sol` itself, repeating in the session that had seen its sub-agent's report | **void** as a sitting; kept as a specimen |

So the models that have sat this exam are three — Claude Haiku, Gemini 3.8 Flash and Sol 6.1 — and each
passed every line of all three tasks. `gpt-6-astra` and `gpt-5.6-sol` have no independent sitting, and none
is planned for this round: what the exam asks is whether an inexpensive model passes, and the three
that sat it are each the lighter tier of its vendor's range — Haiku and Flash by their vendors' own
naming, Sol by the account of the person who runs it (it is the tier his sessions hand execution to,
under a larger model that directs).

| independent sitting | minutes for the three tasks | task 03's correction |
| --- | --- | --- |
| `gpt-6-sol` | 14.1 | both chains' amplitudes cut to a quarter |
| `gpt-6.1-sol-20261013` | 14.2 | the sign of one chain |
| `gpt-6.1-sol` | 15.3 | the sign of one chain |
| `gemini-3.8-flash` | 20.0 | the sign of one chain |
| `haiku` | 21.0 | the sign of one chain |

Minutes are read off each examinee's own clone (its creation to each task's last `result.json`), except
`haiku`'s, which the proctor's harness measured. The time each run arrived says nothing: the one that
started first arrived second and took longest but one.

## What the journals found in the tools

Every item was checked against the installed packages before it was filed.

| found by | what | where it went |
| --- | --- | --- |
| `haiku`, 01 | `assemble --propose-plan` left seven layers out of the plan and printed `notes: []` | [parts#308](https://github.com/rig-c/parts/issues/308) — every unplanned layer is now named with its reason (`@rig-c/parts` 1.12.0) |
| `haiku`, `gpt-6.1-sol`, `gpt-6-sol`, `gemini-3.8-flash`, 02 | the recipe for strands that trail points at example files the package does not ship; values were chosen by hand or taken from `rig-c`'s source | parts#308 — the recipe carries a worked constraint (1.12.0) |
| every sitting, 03 | the proposal drafts two back-hair chains with opposed amplitudes on one mass, lints nothing, and then fails its own check | [parts#314](https://github.com/rig-c/parts/issues/314) — `propose` now names the pair, the edge and both remedies with their measured figures, one step before the build |
| `haiku`, `gemini-3.8-flash`, 03 | `CHECK_TEXTURE_STRETCH` names the vertices and not the bones they hang on; two examinees decoded `rig.json` by hand | parts#314 — the line names each vertex's bones and chains |
| `gemini-3.8-flash`, 02 | the named-animation recipe never says which way a positive `rotate` turns a bone; it read `rig-c`'s source to find out | [parts#317](https://github.com/rig-c/parts/issues/317), open |
| `haiku`, 03 | one part's `drift` in `assemble`'s table has no scale; "a seated figure needs `--keypoints`" reads wider than it is | parts#314 — `drift` prints its share, the sentence is narrowed |

The proctor ran the new lint on task 03's painting from the pull request's source: it stops the drafted
config with one line that states the cause two solvers had to diagnose, and offers exactly the two
corrections they had each taken.

## What the journals found in this exam

- **"You" was never defined.** The prompt said "you are sitting an exam". Three sessions carried a
  standing instruction to hand execution to sub-agents, read the exam as execution, and handed it on.
  The models did what their instructions said; the prompt had not said who was being examined. It does now.
- **A model asked for its own name gives the name it was told.** One session ran `gpt-5.6-sol`, carried
  instructions written for another model's persona, believed it was that model, and named its run for it.
  Another named itself a version it was not. The person starting the run now fills the name in, and the
  results table has a column for who did the work, apart from the name a run came in under.
- **A repeat in a session that has seen an answer is not a sitting.** Two sessions sat the exam again
  themselves after their sub-agents had. Both passed every line in half the time, and both runs are void.
- **Two traces showed it before anyone was asked.** An expectation, written before the first build, that
  already names the part that will fail; and hand-chosen numbers that match another run's where no
  document supplies them (the same ±0.15 / 0.35 / 0.6, the same four bones). Both examinees, asked
  afterwards, listed the same things. The first had said so in its journal unprompted. The proctor now
  reads every run for both.
- **The marker was the wrong word.** `SURPRISE:` is ordinary English and the grader counted it where it
  was not a marker; it also undersold what it was for. It is `WTF?:` now, and the grader reads both.
- **No run carried a clock.** The prompt now asks for a `started:` and a `finished:` line per task.
- **Task 03's `Kept` line is too weak.** It refuses a part made rigid, and it passed a correction that
  turned the part's motion down to a quarter. The next round reads how far the part still moves.
- **Tasks 01 and 02 are easy.** A proposal pasted uncorrected passes task 01. That is a result — the
  documented loop is enough for a small model — and it is also why the journals for those tasks are thin.

## What stands

Three models, the lighter tier of three vendors' ranges, built a rig that passes its check from
one painting and the installed documents, in fourteen to twenty-one minutes, including a draft that had
to be diagnosed and corrected. Five sittings produced three issues on the tools, two of them fixed and
released within the day. Nothing above says how a model not in the table would do.
