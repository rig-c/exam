# The proctor's report — the first Advanced sittings, 2026-10-18

Written by the proctor, by hand, from the sittings in this directory. [README.md](README.md) is the generated
table; this page says what it cannot: how the sittings were run, what was regraded, what was recorded
against whom, and what the journals found. Versions: `rig-c` 2.59.0, `@rig-c/pose` 0.31.1, `@rig-c/parts` 1.35.0.

## How they were run

Five models, three rounds each, fifteen sittings. Every round was a fresh session started in a fresh copy of
that round's package, made by the packager from the edition's source and holding nothing else. The person
starting the session named the model and pasted the prompt verbatim; nobody answered during a sitting.

- The three `claude-*` models ran in Claude Code desktop; `gemini-3.8-flash-medium` and `gemini-4-argon-high`
  in Antigravity Desktop, where the prompt was delivered as a message into the session and the first message
  carried a header the delivery adds above it.
- `claude-haiku-5-5` sat the rounds one after another. `claude-sonnet-5-5` sat R1, then R2 and R3 in two
  sessions at once. The other three sat all three rounds in three sessions at once. Each round's
  `PROBLEM.md` says it follows the one before; no sitting was held to that, and each is graded on its own.
- No sitting handed in a `usage.json`, so no tokens are recorded.

**The edition they sat was 0.20, in two states.** The first nine sittings (`claude-haiku-5-5`,
`claude-sonnet-5-5`, `claude-opus-5-5`) sat it as first packaged. Before the last six, three text defects
those nine had exposed were fixed — `PROBLEM.md` said every package ships `docs/AUTHORING.md`, which
`@rig-c/pose` does not; R2's sentence about its table read as two tables; the grader's `--feet` and `--cycle`
had no help — and the prompt gained the sentence that a journal written after the fact disqualifies a
sitting. No bar moved. 0.21 is that fixed 0.20 with one row added.

## What the proctor regraded

Every sitting was regraded from the files it handed in, with the round's own `tools/grade.py` on edition 0.20.
That regrade is `result.txt` in each directory and is the verdict of record; a sitting's own grading and its
report are not. One cell of fifteen failed: `claude-haiku-5-5` R2, 8 of 14.

Then 0.21's new row was run, read only, on each sitting's own render geometry: the 5th percentile of the
shins' rendered x-scale, bar 0.4. Thirteen sittings read 0.5 or more and would have passed it; two —
`claude-opus-5-5` R2 and `gemini-3.8-flash-medium` R2 — read 0.106 and would have made 14 of 15. That is a
what-if column, not a verdict: the 0.20 results stand.

## What was recorded against five sittings

None of these voids a sitting, and none changes a verdict. Each is in the sitting's `who.json`.

| sitting | what | why it is not void |
| --- | --- | --- |
| `claude-haiku-5-5` R2 | stopped after three attempts, 2 min 23 s on its clock, with six rows failing | stopping is an answer; it is graded as it stands |
| `claude-sonnet-5-5` R2 | said in its closing reply that line 4 of entries 1 and 3 was written after the fact, for more than one step at once | the rule that disqualifies such a journal was written after this sitting, because of it, and applies to the sittings after it |
| `gemini-3.8-flash-medium` R1 | read the installed `@rig-c/pose` package's source, which the prompt's list of exceptions does not name | it is the public source of a package the round installs |
| `gemini-3.8-flash-medium` R2 | quoted the `@rig-c/pose` README three times, under three section names; none of the sentences and none of the names is in the README at 0.31.1 | the quotes are in the report, not in the files the grader reads; they are recorded so that no reader takes them for the package's |
| `gemini-4-argon-high` R3 | `tools.md` is not in the form the prompt gives (no `## <title>` entries) | `tools.md` is read for the tools, not graded |

## What the journals found in the tools

Every item was read against the installed packages before it was filed. The one most sittings ran into on
their own: `rigc build` refuses the rig's directory with `EISDIR` where `retarget` takes it — seven of the
fifteen sittings, four of the five models, say so.

| what | where it went |
| --- | --- |
| `build` refuses a directory `--rig` and a missing `--out` with `EISDIR` and the whole catalogue, not by name | [core#1466](https://github.com/rig-c/core/issues/1466) |
| `render` does not say whether physics ran | [core#1467](https://github.com/rig-c/core/issues/1467) |
| `render` writes `<animation>@<fps>fps/` when `--fps` is not the default, and the README does not say so | [core#1468](https://github.com/rig-c/core/issues/1468) |
| `reach` has a cost — the trunk's jitter — that nothing names | [pose#236](https://github.com/rig-c/pose/issues/236) |
| `--stance` and `--leg-scale` measure leg length in different units; the `--leg-scale` clamp does not say what it did to the free foot | [pose#237](https://github.com/rig-c/pose/issues/237) |
| `retarget`'s output is not readable at length: the `CLEAN` summary, per-frame refusals not collapsed | [pose#238](https://github.com/rig-c/pose/issues/238) |
| path refusals do not name the fix: a missing `--out` parent, a bare `rig.json`, the default `--report`, an overwrite | [pose#239](https://github.com/rig-c/pose/issues/239) |
| readings without their remedy: `SCALE` foreshortening, `SHEAR` inheritance, `--reduce` moving the ankle, `MAP_CHAIN_JOINTS` with a toe | [pose#240](https://github.com/rig-c/pose/issues/240) |
| the head nods, with no line saying so and no switch for it | [pose#241](https://github.com/rig-c/pose/issues/241) |
| a sequence's being in-place is read only under `--plant-feet`; two sittings found it in the source | [pose#242](https://github.com/rig-c/pose/issues/242) |
| `--sequence` and `--animation` are what an agent reaches for; the flags are `--pose` and `--name` | [pose#243](https://github.com/rig-c/pose/issues/243) |

## What the sittings found in this edition

- **The bars converge, except in R2.** In R1 and R3 the five sittings took different flags and maps, and no
  sitting's figure on any measured feature was under half or over twice the median of the five; in R3 all
  five read the same hip vertical range, 1.049. A table made of rows that converge measures whether a
  sitting gets there and little about how well: once there, everyone is the same. R2 is the round where the
  bars leave room, and it is where the sittings spread — the one failed cell, and two shin figures of 0.106
  against a median of 0.500.
- **Quality was read by the median across models, not by eye.** After all fifteen were in, each sitting's
  measurable features were set against the median of the five on the same round, and anything under half
  or over twice it was read. That caught two sittings in R2, each with a lifted shin drawn at about a tenth
  of its length and every row passed. A look at four frames had caught one of them and passed the other,
  because none of the four frames was a compressed one. The feature became 0.21's new row; nothing that
  needs an eye was made a row.
- **Stopping looks like failing.** The one failed cell is not a sitting that could not do R2 but one that
  stopped: three attempts in 2.4 minutes, against 8.7 to 20.3 minutes for the four that passed it.
- **A journal can be written afterwards and still look right.** One sitting said so itself; nothing in its
  files shows it. The prompt now says what it costs.
- **A quotation is not a source.** Three quotations in one report, each attributed to a README section by
  name, are in neither the README nor any section of it.

## 2026-10-20 — the first Codex sittings, on edition 0.21

One model, `gpt-6.1-sol`, sat R1, R2 and R3, each in a fresh Codex Desktop thread, on edition 0.21 itself: its
shin-scale row is graded, not a what-if. The proctor regraded each round from the files handed in with the round's
own `tools/grade.py`; every regrade equals the run's own grade line for line, and its `motion.json`, `report.json`
and geometry hash the same.

| round | rows | minutes | shin scale (5th percentile, bar 0.4) | journal entries / `WTF?:` |
| --- | --- | --- | --- | --- |
| R1 walk | 10 / 10 | 8.7 | 0.631 | 20 / 3 |
| R2 run | 15 / 15 | 8.1 | 0.405 | 26 / 6 |
| R3 dance | 14 / 14 | 8.5 | 0.757 | 17 / 2 |

No sub-agent, no model change and no outside session in any of the three; each thread's only outbound messages
went to the proctor over the channel the prompt came on. No sitting handed in a `usage.json`; the tokens the
proctor read from the host's log are in each `who.json`.

### The proctor's rulings

None changes a verdict; each is in the sitting's `who.json`.

| sitting | what was found | ruling |
| --- | --- | --- |
| R1 | before reading JOURNAL.md it wrote a transcript placeholder with a made-up start time and no journal entry before it, then declared the sitting terminated | **recorded.** The proctor answered that the slip is recorded rather than voiding; it resumed, and the slip is preserved in its run |
| R2 | before opening PROBLEM.md it read the messaging tool's own skill file outside the package, called that a boundary violation and stopped | **not exam material.** The boundary is about exam material; the channel's own tooling is not it. It was told to record the read and continue, and did. 31 s of its clock is that exchange |
| R2 | 8 of 26 line 4s were composed in the same shell call as their step, before its output was read; one of them was wrong and was rewritten in place, saying so | **record-only.** Neither disqualifier the prompt names occurred (lines 1–3 after the step; one line 4 for several steps). Filed as [exam#4](https://github.com/rig-c/exam/issues/4) |
| R2 | the rig spec was changed: one marker bone for the map's scale pair, and the skirt's physics softened; `--leg-scale 0.405` and a 0.95 gain sit on their bars by choice | **within the problem's "Fix?"**, which allows the flags, the map, the rig spec and the physics. The proctor's control with the original physics also passes 15 of 15 with no folds, so the softening is not what cleared the folds, as the run's report says it was |
| R3 | it declared its own sitting invalid: entry 4 was opened while entry 3's grade was still running, so entry 3's line 4 landed under entry 4 | **record-only.** Every entry's lines 1–3 came before its step and each line 4 came from its own step; the overlap carried no information, was disclosed mid-round, and the same habit is recorded, not voided, on R2. 14 of 17 line 4s were pre-written, which is exam#4 again |
| R3 | the same skill-file read as R2, in the first tool call | **not exam material**, as on R2; disclosed in its transcript and findings |

The R3 dance is not judged by a person; the Basic edition's dance scores of the same day are in
[the Basic report](../../results/REPORT.md#what-the-machine-lines-cannot-see).

### What the journals found in the tools

Eight `tools.md` items over the three rounds, none of them the same item twice; the two that recur are the same
trade seen from two rounds.

| what | rounds |
| --- | --- |
| `--reduce` trades ankle precision against smoothing with one tolerance; a reduction that keeps planted contact is wanted | R1 (*Separate ankle precision from smoothing*), R3 (*Reduction that preserves planted contact*) |
| `reach` starting away from its source joint is not warned about, and its local motion cannot be read | R1 (*Warn when reach starts away from its source joint*), R3 (*Reach compensation needs a local-motion reading*) |
| `retarget` does not create the parent directories of `--out` and `--report` | R2 |
| the map's translation scale needs an anatomical recipe | R2 |
| a reported scale rounded to three places hides a value just under the bar | R2 |
| the automatic eye-line nod should be optional | R3 |

The parent-directory refusal is the one the 2026-10-18 sittings filed as [pose#239](https://github.com/rig-c/pose/issues/239),
and the nod is [pose#241](https://github.com/rig-c/pose/issues/241); the reduction and reach items are new.
Also filed from this day: [exam#5](https://github.com/rig-c/exam/issues/5), a layer-order row, after
[pose#281](https://github.com/rig-c/pose/issues/281).
