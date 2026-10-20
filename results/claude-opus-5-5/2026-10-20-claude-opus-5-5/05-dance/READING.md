# The proctor's reading — claude-opus-5-5, 05-dance, 2026-10-20

Regraded: 14 of 14, the same lines — 919 triangles; the loop closes at 0.0 rig px; hands 199.7 and 199.9;
the trunk's least-travelling vertex 26.1; arms bend at most 5.3° along their length; the legs stay 0.0 rig
px from the shoes; 1.0 of the speed variation repeats every two beats; soft 5.026 rig px. 32.0 minutes by the
run's own lines, passing at the third grade.

**What it added.** `legwear` turned from a region on the hip into a lattice mesh pulled by a thigh segment on
the hip per leg and a shin bone per leg parented to the root, from the leg/shoe junction to the knee, with a
sharper weight falloff (`exponent` 4). No IK: it turned the documented two-bone leg down because both legs are
nearly straight at rest and a bob would throw the knees sideways. The arm chains were moved to the elbow
(0.54) and wrist (0.20) heights the task gives, at row centres it measured on the arm parts. The dance is nine
tracks sampled every 1/16 s from sines of period 1 s and 0.5 s: a hip dip on each beat, a hip sway with a
tilt, a chest counter-turn, a head turn, the arms pumping in turn at shoulder and elbow. The side-lock physics
was made calmer and stiffer and the chest spring softer.

**The way there.** The first grade read 12 of 14 (the trunk travelled 11.0, the chest 2.04 px); the second
13 of 14 (arms bent 10.1° along their length). Between them a sharper falloff folded `wave` at the shoulder,
and its own renders with physics on found the side locks folding `hair_front` in the dance, which `check`
does not read. It wrote a script to read the arm bend itself; for three rebuilds that script read a stale
12 fps render (`render --fps 24` writes to another folder), one journal conclusion rests on that, and the
journal corrects it. `rule: "heat"` bent the arms about 1° but folded the elbow; it went back to `exponent`
4 with a smaller elbow swing.

**The journal, and an edit after the last grade.** Fifteen entries. As written before the last grader run,
one line 4 began `WTF?:` (entry 11) — the grader's count then was 1. Four more carried `WTF?:` in the middle
of the line (entries 5, 6, 9, 13) and three recorded a different result without it (1, 7, 12). After the
last grade it moved the marker to the start in four lines, added it in three, changed one phrase ("And WTF?:"
to "And — worse —"), wrote entry 15's line 4 and an end note that says so. The regrade counts 7 (entry 1's
label is "Happened (lint step):", which the grader's pattern does not match; the examinee counted 8). The
end note says the marker was "moved" in entry 1; there it was added.

**The ruling.** The table publishes this task's count as **1**, the count as written: the rule is that line 4 *begins* `WTF?:`, the count measures how a result landed, and six of the seven did not land that way. The edit was made because the count was low, and it is disclosed; the entries keep their value as evidence, so the journal is not voided, and nothing else in the sitting is touched by it. `result.json` keeps the regrade's 7.

**tools.md**, eight items: `--parts` after a build points elsewhere than after `assemble`; `render --fps`
changes the output folder without `--help` saying so; `check` reads folds with physics left out; no reading
of how far a limb bends between its joints; the distance rule's weights leak across a bend and sharper
weights fold sooner; planted feet are described for keypoints and for rig-c, not for a rig-parts figure; a
contour mesh's triangle count is known only after a build; the animations file refuses `easings`.

**The transcript.** Commands and their last lines (22 recorded); the Python steps that wrote `config.json`
and `animations.json` are not in it.

**The dance, judged.** Scored blind by a person on 2026-10-21, as clip F of eight (A to H), without knowing whose it was: **3 out of 10**, one mark for the whole clip. `dance.mp4` is the clip the judge saw: `dance` three times round, 12 s at 24 fps, physics running throughout, one fixed viewport, a click on each beat. `dance_frames.jpg` is twelve frames of its first loop, every third of a second, labelled by time only. The score changes no line.
