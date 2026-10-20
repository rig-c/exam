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
| `gemini-3.8-flash`, 02 | the named-animation recipe never says which way a positive `rotate` turns a bone; it read `rig-c`'s source to find out | [parts#317](https://github.com/rig-c/parts/issues/317) — the recipe says it: counter-clockwise positive, y up, with a measured arm (1.13.1) |
| `haiku`, 03 | one part's `drift` in `assemble`'s table has no scale; "a seated figure needs `--keypoints`" reads wider than it is | parts#314 — `drift` prints its share, the sentence is narrowed |
| every sitting, 01 | `assemble.rig_scale` was copied from the examples (0.5); the guide does not say what the value trades | [parts#345](https://github.com/rig-c/parts/issues/345), open |
| `gpt-6.1-sol`, 02 | a wave that passes the grader read on the examinee's own contact sheet as an arm raised sideways; the worked `wave` is not in the package | parts#345, open |
| `gpt-6.1-sol` ×2, `codex-direct`, 02 | strand physics lags a fraction of a degree under the idle alone; the answer is in another recipe's *Limits* | parts#345, open |
| `haiku`, 02 | arm art painted into `topwear` stays with the torso when the arm rises | parts#345, open |

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

## 2026-10-20 — eight sittings of the five-task round

Eight models from three families sat all five tasks on `@rig-c/parts` 1.15.0 and `rig-c` 2.47.1, each in a fresh
session, each regraded by the proctor from the files it handed in. Every regrade agrees with the run's own grader
lines; where a run's report says something its files do not, the run's `READING.md` says so beside it.

| model | lines passed, of 40 | task 05 | minutes | the dance, judged (clip) |
| --- | --- | --- | --- | --- |
| `claude-fable-5-1` | 40 | 14 / 14 | 52.9 | 9 / 10 (E) |
| `gemini-3.8-flash` | 40 | 14 / 14 | 31.1 | 7 / 10 (C) |
| `claude-sonnet-5-5` | 40 | 14 / 14 | 53.6 | 6 / 10 (D) |
| `claude-haiku-5-5` | 39 | 13 / 14 — not `on_her_feet` | 70.3 | 5 / 10 (G) |
| `gpt-6-astra` | 40 | 14 / 14 | 33.1 | 4 / 10 (A) |
| `claude-opus-5-5` | 40 | 14 / 14 | 64 | 3 / 10 (F) |
| `gemini-4-argon-high` | 40 | 14 / 14 | 71.3 | 3 / 10 (H) |
| `gpt-6-luna` | 31 | 5 / 14 — the build failed | 29.1 | 0 / 10 (B) |

Minutes are the runs' own `started:` / `finished:` lines summed over the five tasks.

### Which runs count, and the proctor's rulings

All eight are independent sittings: one model, in the session it was started in, with no sub-agent of its own.
Three rulings touch what the table shows; none changes a line.

| sitting | what was found | ruling |
| --- | --- | --- |
| `claude-opus-5-5`, task 05 | after its last grade counted one `WTF?:`, the run moved the marker to the start of line 4 in four entries and added it to three more, and said so at the journal's end; the regrade of the edited file counts 7 | the count is **published as 1**, the count as written, with a footnote in the table. The rule is that line 4 *begins* `WTF?:`; six of the seven did not land that way, and the edit was made because the count was low. Not voided: the words are the run's own, written in time, and the edit is disclosed. `result.json` keeps the regrade's 7 |
| `claude-haiku-5-5`, task 01 | five line 4s written in one step after the task's grade, and a sixth after it too | **task 01's journal is not credited** (README rule 3: an entry written after the fact is worth nothing here); lines 1–3 stand, the build lines are the grader's, and the sitting counts. Marker moves in tasks 04 and 05 are recorded, not voided |
| `gpt-6-luna`, task 05 | the build failed its seam check and the run stopped; its report says the failure was fixed and only a comparison build failed | **5 / 14, counted as graded.** A stop is an answer. The report's claim is contradicted in the task's `READING.md`, with the regrade's figures |
| all four Claude sittings | they ran as sub-agents of the proctor's own session, whose host delivers its standing instruction files with every sub-agent | recorded in each `who.json` (`host_context`); the files carry one-line notes about the exam and no task content, value or answer, and no examinee opened them. Not a void — but see the caveat below |

Two smaller things are recorded and not ruled on. `gpt-6-astra` relabelled one line 4 of task 05 after reading the
grader's counting pattern; only the label changed, the sentence is as first written. `claude-sonnet-5-5` left two
results that differed from their expectation unmarked; the table keeps the grader's count.

### What the journals found in the tools

Thirty-six `tools.md` items across the eight sittings, all on task 05, grouped where they say the same thing.
Every item was read against the installed packages; four did not hold up and are marked.

| what | sittings |
| --- | --- |
| a contour or region mesh's triangle count is known only after a full build | 5 — fable, opus, sonnet, flash, argon (flash's figure in its first item is contradicted by its own config; argon's first item names a build that did not happen) |
| nothing says how to keep a leg on its foot under a moving hip on a `rig-parts` figure | 3 — fable, opus, sonnet |
| the proposer's sleeve joints are not at the elbow and wrist the task gives | 2 — fable, argon |
| no easing can be named in an `animations_from` file, so smooth motion needs a hand-written `curve` or dense linear keys | 2 — fable, opus |
| the weights of a distance-blended arm leak across a bend, and nothing says how far a joint may turn before it kinks | 2 — opus, flash |
| `animations_from`: the file's schema is not shown beside the field (argon; contradicted — the guide has it), and the path is resolved beside the config without the refusal saying so (haiku) | 2 |
| a fold is located by triangle and not by the bones that drive it | 1 — astra |
| `check` reads animations for folds with physics left out | 1 — opus |
| `render --fps` writes to another folder without `--help` saying so | 1 — opus |
| `--parts` after a build points somewhere else than after `assemble` | 1 — opus |
| no reading of how far a limb bends between its joints; the geometry file's layout and the "travel" readings are not described | 2 — opus, haiku |
| a chain's tip ratio cannot be predicted before the build | 1 — fable |
| the recipe says where a key moves a hand, not what makes it read as a wave | 1 — fable |
| a build with physics and a second animation takes three times as long, unannounced | 1 — fable |
| which chain is which side of the image | 1 — sonnet |
| no loop or period helper for an animation other than the idle | 1 — flash |
| which pose file goes to `--keypoints` on a seated figure | 1 — haiku |
| which bones take the vertices of a contour's bridge between two islands | 1 — haiku |
| which frames the soft line samples | 1 — haiku |
| reading `AUTHORING.md` with the reading tool | 1 — haiku |
| `assemble --help` is refused | 1 — luna |
| `MOTION.md` is missing (luna; contradicted — it ships in `rig-c`, the package whose README links it) | 1 |
| `spine-core` is not installed (luna; true, and a devDependency of both packages — its "this limited the comparison build" is contradicted) | 1 |
| the journal's line 4 has no form for a result that matched; its entry order is easy to break | 2 items — haiku (about the exam, not the tools) |

### What the machine lines cannot see

Task 05's fourteen lines read whether a dance holds together: the loop closes, the hands and the trunk travel, the
arms bend at their joints, she stays on her feet, the motion keeps the beat. They do not read whether it is a dance.
For that the proctor rendered each run's `dance` as a clip — three times round, physics running, one fixed viewport,
a click on each beat — lettered A to H with no name, and one person judged all eight in one sitting before the
letters were matched to models. The clip and the score are in each run's `05-dance/`.

| model | task 05 lines | the dance, judged |
| --- | --- | --- |
| `claude-fable-5-1` | 14 / 14 | 9 |
| `gemini-3.8-flash` | 14 / 14 | 7 |
| `claude-sonnet-5-5` | 14 / 14 | 6 |
| `claude-haiku-5-5` | 13 / 14 | 5 |
| `gpt-6-astra` | 14 / 14 | 4 |
| `claude-opus-5-5` | 14 / 14 | 3 |
| `gemini-4-argon-high` | 14 / 14 | 3 |
| `gpt-6-luna` | 5 / 14 (the build failed) | 0 |

The judge used one mark out of 10 for the whole clip, not the three marks out of 5 that TASK.md describes, and
gave the rubric in one line (translated): half the mark is whether the joints read as a human's, half is the dance
itself; most of them read as flailing, and one understood the beat.

The six runs that passed every line were scored from 3 to 9. The one that missed a line scored in the middle of
them, and the one whose build failed scored 0. Passing the lines is what a run needs to be judged at all; it says
almost nothing about the score.

Two observations, each one sitting per model and one judge, so neither is a finding about the models:

- **The largest model of each family scored below the middle one.** `gpt-6-astra` 4, `claude-opus-5-5` 3 and
  `gemini-4-argon-high` 3, against `gemini-3.8-flash` 7 and `claude-sonnet-5-5` 6.
- **The highest score is the one run that eased its keys.** `claude-fable-5-1` gave every key of all eight of its
  dance tracks a `curve` (72 of 72 keys that are not a track's last), and its journal plans the phrase in beats: a
  dip on every beat, the arms on a two-beat cycle, the sway over four. The other seven runs keyed linear values
  only, from 9 to 97 keys a track.

**A caveat on the four Claude sittings.** They ran as sub-agents of the proctor's own session, and that host
delivers its standing instruction files with every sub-agent it starts: the operator's general instructions, the
core repository's guide, and an index of notes whose exam lines are one-line pointers about editions and proctoring,
with no task content. No examinee opened them, and each `who.json` records them. They did show in one hand-in's
language and in three commits' co-author lines. The next edition runs the Claude sittings outside that context.

What this day filed on the exam and the tools:

| issue | what |
| --- | --- |
| [exam#4](https://github.com/rig-c/exam/issues/4) | line 4 is written after the output is read; a line composed in the step's own shell is a forecast |
| [exam#5](https://github.com/rig-c/exam/issues/5) | Advanced: a layer-order row, the rig's draw order against the sequence's derived depth order |
| [exam#6](https://github.com/rig-c/exam/issues/6) | the grader counts `4. **Happened:** WTF?:` while JOURNAL.md says "begin the line with `WTF?:`"; two sittings wrote `4. WTF?:` and were counted 0 |
| [pose#281](https://github.com/rig-c/pose/issues/281) | derived depth per segment in the sequence, drawn on the stick figure, so draw order can be read and graded |
