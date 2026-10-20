# The proctor's reading — claude-sonnet-5-5, 05-dance, 2026-10-20

Regraded: 14 of 14, the same lines — 859 triangles; the loop closes at 0.0 rig px; hands 423.8 and 421.5;
the trunk's least-travelling vertex 23.0; arms bend at most 2.0° along their length; the legs stay 0.0 rig
px from the shoes; 1.0 of the speed variation repeats every two beats; soft 4.82 rig px. 8.1 minutes by the
run's own lines, passing at the first grade.

**What it added.** Two fixed foot bones parented to the root, and `legwear` turned from a region on the hip
into a grid mesh whose segments weight its top to the hip and its bottom to the two foot bones, so the legs
stretch between a moving hip and planted feet. No leg chain, no knee, no IK. The dance is six tracks
sampled at 24 fps from sines of period 1 s and 0.5 s: a hip bounce on each beat, a hip sway, a chest lean, a
head tilt, and the two shoulders swinging in opposition; the arms swing whole from the shoulder and do not
bend at the elbow. It found no recipe for planted feet and says the weighting came from AUTHORING §3
(`meshes.<part>` and its `segments`).

**Journal.** Two entries, no `WTF?:`; both results were as expected.

**tools.md**, three items: a contour region's triangle cost is only seen after a build; nothing says a mesh
segment may name a bone under the root to plant a part; which chain is which side of the image.

**The dance, judged.** Scored blind by a person on 2026-10-21, as clip D of eight (A to H), without knowing whose it was: **6 out of 10**, one mark for the whole clip. `dance.mp4` is the clip the judge saw: `dance` three times round, 12 s at 24 fps, physics running throughout, one fixed viewport, a click on each beat. `dance_frames.jpg` is twelve frames of its first loop, every third of a second, labelled by time only. The score changes no line.
