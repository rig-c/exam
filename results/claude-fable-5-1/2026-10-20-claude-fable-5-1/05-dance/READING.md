# The proctor's reading — claude-fable-5-1, 05-dance, 2026-10-20

Regraded: 14 of 14, the same lines — 884 triangles; the loop closes at 0.0 rig px; hands 404.6 and 401.0;
the trunk's least-travelling vertex 24.5; arms bend at most 4.3° along their length; the legs stay 0.18 rig
px from the shoes; 1.0 of the speed variation repeats every two beats; soft 3.486 rig px, 0.486 above its
floor. 9.6 minutes by the run's own lines.

**What it added.** A bone `feet` under the root at the ankles, and `legwear` turned from a region on `hip`
into a grid mesh with two explicit segments, one across the thighs on `hip` and one across the ankles on
`feet` — the legs shear with the hip while their bottoms stay on the shoes; there are no knees. The two
sleeve chains' interior joints were moved onto the elbow (0.54) and wrist (0.20) heights the task gives:
the new heights are exactly those ratios of each arm part's box, and the x is interpolated along the
proposed chain. The dance is eight tracks with hand-computed `curve` easing on every key: a hip dip on each
beat, a hip sway, chest and head counter-rotation, and both arms flapping up and out at the shoulder and
elbow, mirrored.

**First try.** One build, one grade, green. It read the grader's source before planning the dance and says
so in its journal (allowed: the grader is in the clone).

**Journal.** Three entries, no `WTF?:`.

**tools.md**, seven items; each gives what it tried, what the package said, what would have helped and the
cost.

**The dance, judged.** Scored blind by a person on 2026-10-21, as clip E of eight (A to H), without knowing whose it was: **9 out of 10**, one mark for the whole clip. The judge's only words on it: "oh, this one reads as a dance". `dance.mp4` is the clip the judge saw: `dance` three times round, 12 s at 24 fps, physics running throughout, one fixed viewport, a click on each beat. `dance_frames.jpg` is twelve frames of its first loop, every third of a second, labelled by time only. The score changes no line.
