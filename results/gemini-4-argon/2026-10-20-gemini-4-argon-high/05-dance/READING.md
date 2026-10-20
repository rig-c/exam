# The proctor's reading — gemini-4-argon-high, 05-dance, 2026-10-20

Regraded: 14 of 14, the same lines: 890 triangles; the loop closes at 0.0 rig px; hands 277.8 and 275.9;
the trunk's least-travelling vertex 20.0 against 15; arms bend at most 0.4° along their length; the legs
stay 0.0 rig px from the shoes; 1.0 of the speed variation repeats every two beats; soft 5.357 rig px.
28.6 minutes by the run's own lines.

**What it changed.** It moved the arm chains' middle joints onto the elbow and wrist heights the task gives
(0.54 and 0.20 of the arm part's height above its lowest point). The elbows come to the same pixels as
another sitting's, read off its own proposal by interpolation; the wrists it read off the landmark render.
It bound each arm mesh to its own chain only, with a steeper falloff. `legwear` went from a region into a
grid mesh with the thighs weighted to the hip and the shins to the root. The shins are fixed to the floor,
which is how the legs stay exactly on the shoes. There are no knees and no IK. The dance is nineteen tracks
on a one-second motif keyed every half beat (0.25 s) and repeated four times: the hips sway side to side and bob,
the chest and head tilt, the arms swing out and in at shoulder and elbow, one opening as the other closes, and the hair and skirt chains rock a little.

**The one failure.** The first build was refused: its `dance.json` had no `"spec"` header and keyed its
tracks in another shape. It rewrote the file in the `rigc-motion/1` shape it had used for 02 and the second
build passed; the grader passed it first time. Recorded as `WTF?:`.

**tools.md**, three items: no quick triangle count for a contour mesh with a region (its account of 04 is
wrong; see 04's reading); no example of the motion file's `spec` header beside `animations_from` in
`AUTHORING.md` (there is one, in the field's own row and in the expressions recipe, which it read during
02 and followed there); and a request that `propose` put the arm joints at elbow and wrist heights rather
than in thirds, which is fair.

**The dance, judged.** Scored blind by a person on 2026-10-21, as clip H of eight (A to H), without knowing whose it was: **3 out of 10**, one mark for the whole clip. `dance.mp4` is the clip the judge saw: `dance` three times round, 12 s at 24 fps, physics running throughout, one fixed viewport, a click on each beat. `dance_frames.jpg` is twelve frames of its first loop, every third of a second, labelled by time only. The score changes no line.
