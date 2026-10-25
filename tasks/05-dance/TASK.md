# Task 05 — dance, on the mannequin

> **Round 4's task 05** (issue #10). Round 3 set this task on the painted figure of tasks 01–04; that text is
> kept as [`TASK-round3.md`](TASK-round3.md), for the runs filed on it. This task is graded on the fixture
> [`fixture.json`](fixture.json) names: `python3 grade.py runs/<run>` reads it, and the part names its lines read
> are in `../../fixtures/mannequin/grade-roles.json`.

A wooden artist's mannequin, already rigged: `../../fixtures/mannequin/`. Its README names every joint, its
range, the bone that turns it, and how the feet are held.

## Given

The fixture, as it is in the repository: the painting and its layers, the ball-joint caps, and `config.json`
with the rig and an idle. Nothing else: no keys, no pose, no reference clip.

The rig builds as given, on the versions the root `package.json` pins (`@rig-c/parts` 1.60.0, `rig-c` 2.67.2):

    rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out

and ends `check: PASS; 9 of 14 bar(s) measured, 5 skipped (BLINK_NO_HOLE, TIP_OVER_ROOT, TEXTURE_STRETCH,
FEET_STAY_LEVEL, STRESS_OFF_CHAIN)`. That is the idle-only check; with a `dance` that poses the legs,
`FEET_STAY_LEVEL` is also measured and the check ends `check: PASS; 10 of 14 bar(s) measured, 4 skipped` —
both counts describe passing builds. Two iks aim the ankles at fixed targets under `root`; hip movement
must stay within the fixture's [planted-leg reach](../../fixtures/mannequin/README.md#planted-leg-reach).
The targets staying fixed does not guarantee drawing contact. There are no legs to construct.

The music is 120 beats a minute. Eight beats are 4.0 seconds.

## Do

Give the rig one more animation, named `dance`: a loop of exactly 4.0 s in which the mannequin dances — to that
beat, with its whole body, on its own two feet.

Use the bones the rig has. Do not add bones, parts, meshes or physics; the rig is not what is being asked for.

## Hand in

`config.json` (the fixture's, with `dance` added), the motion file it names if you move the motion out of it,
`journal.md`, and the transcript.

## Timing

This grader rebuilds and samples the rig. A tool's 120-second wait can end before the grader does: one
recorded invocation was moved to the background at that limit and completed successfully afterward.
The [timing audit](https://github.com/rig-c/exam/issues/58#issuecomment-6398236249) records **seven command
intervals of 106–197 seconds** on 2026-10-25. These are historical shared-host observations, not an expected
runtime range for every machine or run. The grader itself does not impose a 120-second subprocess timeout.
The audit citation is provenance only; it does not expand the exam's permitted reading.

Use the host's supported longer wait or background-completion mechanism. Read the **same invocation's**
completed output and result before closing its journal entry and finishing the task clock. A wait ending
does not mean the grader failed; do not launch a duplicate while it is still running.

## Pass lines

The machine reads only whether the dance holds together. Task 01's four (built, checked, whole, does not fold),
and, on `dance`, posed at 24 frames a second:

| | line |
| --- | --- |
| **Dance as timed** | the built rig holds an animation `dance` that lasts 4.0 s |
| **Closes** | no vertex in the last frame is more than 0.5 rig px from where it is in the first |
| **Both hands** | `hand_l` and `hand_r` each travel at least 100 rig px at their furthest vertex, measured from the middle of `topwear` |
| **Arms bend at the joints** | along its own length, neither an upper arm nor a forearm bends more than 8 degrees more than at rest |
| **Whole body** | every vertex of `topwear` travels at least 15 rig px, measured from the middle of the feet — the trunk goes somewhere, and not by sliding the figure along the floor |
| **On its feet** | the bottom of each shin stays within 6 rig px of where it meets its foot |
| **Keeps time** | read how fast the figure moves from each frame to the next, round the loop: at least half of the variation in that repeats every two beats |
| **Dance does not fold** | `rigc render --folds` over `dance` names no mesh |

Travel is the diagonal of the box a vertex's path fills over the loop. Task 05's `budget` and
`soft_in_the_dance` lines, and task 04's hop, are not read here: there is no mesh or physics to author.

The arm and leg lines name this rig's parts (`upperarm_*`, `forearm_*`, `hand_*`, `shin_*`, `foot_*`) where
`TASK.md` names the painted figure's. Every arm part here is rigid on one bone and turns only at a joint that
declares its range, so **Arms bend at the joints** has nothing to read: the grader reports it SKIP, with that
reason, and does not count it. Keying the elbows or wrists does not change that SKIP: on this rig the line
has nothing to read, whatever is keyed. `budget` and `soft_in_the_dance` are reported SKIP the same way.

## And a judge

The dance is judged, not the leg construction. For every run that is filed, the proctor renders `dance` as a
clip — three times round, with a click on each beat — and a person scores it without knowing whose it is: the
clips carry letters, and the names are put back after the scores are in.

The judge gives one mark out of 10, recorded in its own column beside the machine's lines: 5 for whether the
joints move as a body's joints do, 5 for whether it reads as a dance on the beat.
