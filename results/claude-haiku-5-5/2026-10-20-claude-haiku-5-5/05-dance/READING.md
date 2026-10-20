# The proctor's reading — claude-haiku-5-5, 05-dance, 2026-10-20

Regraded: 13 of 14, the same lines. **`on_her_feet` fails**: the end of a leg gets 20.62 rig px from where
it meets `shoes`, against 6.0. The rest pass — 958 triangles against 1,000; the loop closes at 0.0 rig px;
hands 661.7 and 459.3; the trunk's least-travelling vertex 18.1; arms bend at most 3.4° along their
length; 1.0 of the speed variation repeats every two beats; soft 4.415 rig px. 16.6 minutes by the run's
own lines.

**What it added.** Two leg chains under `hip` (`legA`, `legB`, thigh and shin), each held by a two-bone IK
to a fixed target under the root at the ankle (`footA`, `footB`); `legwear` turned from a region on `hip`
into a mesh bound to the two chains. The knees sit on the straight line from hip to target so the IK does
not move the setup pose (its first build failed the seam bar until it did that). The dance is eight
linear tracks keyed every 0.125 s: an 18 rig px hip bounce on every beat, hip, chest and head rotation, and
the arms swinging at shoulder and elbow. The sleeve joints were left where the proposer put them.

**Where it stopped.** The sock ends move with the hip. It moved the targets to the sock ends (no change),
tried a contour mesh (refused: the legs are two islands), a contour with `bridges: true` (built, no change)
and a smaller weight radius (no change), and stopped, saying it had not found what gives the sock-end
vertices the other leg's bones. Its journal and `tools.md` both name the missing sentence.

**Journal.** Eight entries; entry 1 has no line 4. Five line 4s begin `WTF?:` in the handed-in file. As
first written, two did (entries 2 and 8) and one did under a wrong number (entry 5, `7.`). After the
task's first grader run had started, the misnumbered line 4s (`5.` to `9.`) were renumbered, entry 6's
was changed from `**Happened:**` to `WTF?:`, and entry 7's mid-line marker was moved to the start. Entry 4
keeps a mid-line `WTF?:` that was not moved. The grader counts 0, for the numbering reason in 01's
reading.

**tools.md**, eight items. The first two are about the exam's journal form rather than the packages; the
other six name a package message or section.

**The dance, judged.** Scored blind by a person on 2026-10-21, as clip G of eight (A to H), without knowing whose it was: **5 out of 10**, one mark for the whole clip. `dance.mp4` is the clip the judge saw: `dance` three times round, 12 s at 24 fps, physics running throughout, one fixed viewport, a click on each beat. `dance_frames.jpg` is twelve frames of its first loop, every third of a second, labelled by time only. The score changes no line.
