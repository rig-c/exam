# Rounds

## What is in a round

Rounds 1 and 2, on `@rig-c/parts` 1.11.0 and `rig-c` 2.47.0: tasks 01 and 02 on one painting, and task 03
on a second painting of the same character, where the tool's draft does not pass as proposed.

Round 3, on `@rig-c/parts` 1.15.0 and `rig-c` 2.47.1: task 04, a soft
chest under a triangle budget; task 05, a dance; and one more line on task 03. The tools changed between
the rounds because of what the first two found: on 1.13.0 `propose` names task 03's fault itself, one step
before the build, so a result on that task is a result on the versions beside it in the table. Since 1.14.0 `check` also reads every animation, the idle included, for folds, and fails a build where one folds — the line tasks 02, 04 and 05 grade is now one the tool reports first.

Tasks 01 to 04 can be passed by following a recipe the documents carry. In Round 3, task 05 had none: the
rig as the earlier tasks leave it could not do what was asked, and what it lacked had to be worked out. Its
machine lines read only whether the dance holds together — the loop closes, the feet stay under her, the
arms bend at their joints and nowhere else, the motion keeps the beat. Whether it is a dance is scored by a person from
a clip with a letter on it and no name, and that score sits beside the lines without changing them.

Round 4, on `@rig-c/parts` 1.58.0 and `rig-c` 2.67.2: tasks 01 to 04
unchanged, and task 05 set on a wooden mannequin that comes already rigged (`fixtures/mannequin/`), so the dance
is the work and the rig is not. On Round 3 the clocks showed that the time went into building legs that could
dance at all, five different ways. The painted figure's task 05 is kept as `tasks/05-dance/TASK-round3.md` for
the runs filed on it. On the new versions the tools' own documented path passes tasks 01 to 04. Between 1.15.0 and 1.58.0
`check` came to refuse an arm mesh weighted off its chain, which every Round 3 config carried from the 1.15.0 draft, so a
Round 3 config does not build on Round 4's versions; each row of the tables names the versions it was graded on.
Task 05's lines on the mannequin read the same things on its parts, except the arm line: every arm part is
rigid on one bone and turns only at a ranged joint, so that line is SKIP with its reason, as are the budget and
the soft line (no mesh, no physics to author). **Round 4's task 05: dry run sat 2026-10-23** (claude-haiku-5-5, 9.8 min, 11 of 11 lines): not filed as a result.

Round 5, on `@rig-c/parts` 1.60.0 and `rig-c` 2.67.2: tasks 01, 02 and 04 move to a new painting, because
the old one had become a walked example. rig-c/getting-started teaches the tools on it step by step, and
followed verbatim it handed in a task 02 that passed 7 of 7 lines (rig-c/exam#29). Task 02 also changes to suit Form 1:
its wave, a bone rising 150 rig px, asked a living illustration for a limb swing the painting does not hold,
and the grader could not see the tear that caused (the guide's own wave opened the shoulder by 4,922 px).
It now asks for a gesture inside what was painted, a head turn, a lean or a lift of the shoulders, read by
how far the face travels, with every limb joint and both armholes held to no opening at all. The new
painting was chosen by measurement, from four candidates (rig-c/exam#29): on the documented path, a rigid elbow cut on a
bare arm opens at a 30° turn, so no gesture that bends a cut joint can hold, and that was filed on the tools
(rig-c/parts#687). The old painting's task texts are kept as `TASK-round4.md` beside each task, and its cells
are tabled apart from the new painting's, never ranked with them. Tasks 03 and 05 are unchanged.

A walk and a hip wiggle were each set as a sixth task on this painting and withdrawn before anyone sat
them: seen from the front, with her feet apart and her arms at her sides, neither reads as what it is. A
walk belongs on a figure seen from the side, and that is the next painting.

A later sixth task, motion from a pose (a public dance's joints put on this painting with `@rig-c/pose`), was
published and withdrawn the same day, before anyone sat it (commit 9188c1b, reverted). It measured the tool
rather than the examinee: the examinee's part was a map and a few flags, the reference solve passed every
line in about two minutes, one line was answered by the package's own README, and the ceiling was what a
turning bone cannot draw. The part of that work that does measure an agent is the polish that follows,
comparing the rig with the video and closing the gap, and it returns as a task once that gap can be measured.

Round 6, on `@rig-c/parts` 1.73.1 and `rig-c` 2.80.0: task 03 now starts from the static
[`inputs/draft.json`](tasks/03-correct/inputs/draft.json), with its edition, exact draft hash and unchanged
source input hashes in [`edition.json`](tasks/03-correct/edition.json). The draft can pass the package
check while failing an independent exam line. Its [task text](tasks/03-correct/TASK.md) replaces the
old failing-proposal description and correction hint; [`TASK-round5.md`](tasks/03-correct/TASK-round5.md)
preserves that text byte for byte. Existing results with no task edition field remain historical
proposal-task records on their recorded versions; they are not results on the new static draft.
New task 03 grader output records `edition` and `task_input` provenance. The other Basic tasks keep
their existing inputs and bars. This repin is author validation, not a new sitting.

The package name stays `rig-c`: the tasks and grader invoke its `rigc` binary and the grader records
its installed package version under that literal name. Advanced's current round packages use the
same core and parts pins, with `@rig-c/pose` 1.5.2; recorded sittings keep their original versions.

Every painting was generated for this exam (each task's `inputs/generation.json` records how). None is
one of the packages' examples, nor walked by any public guide: their configs do not fit. A guide walks its own
painting, never an exam's input.

