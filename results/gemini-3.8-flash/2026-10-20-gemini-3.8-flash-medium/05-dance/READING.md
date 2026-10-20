# The proctor's reading — gemini-3.8-flash-medium, 05-dance, 2026-10-20

Regraded: 14 of 14, the same lines — 828 triangles; the loop closes at 0.0 rig px; hands 305.0 and 302.8;
the trunk's least-travelling vertex 32.6; arms bend at most 5.3° along their length; the legs stay 2.72 rig
px from the shoes; 1.0 of the speed variation repeats every two beats; soft 5.482 rig px. 10.4 minutes by
the run's own lines.

**What it added.** One bone, `feet`, parented to the root at the shoe line, and `legwear` turned from a region
into a grid mesh weighted to the hip at the top and to `feet` at the bottom. There are no leg chains, knees
or IK: the legs are one sheet stretched between a moving hip and a fixed floor. The dance is seven tracks on a
one-second motif repeated four times: the hip bobs twice a second and sways once, both arms swing out and back
in mirror, the head tilts.

**The two failures.** The first build was refused by the compiler: the generated keys repeated `t = 1` where
one cycle met the next. The second built and failed one line, the arms bending 9.2° against 8; it lowered the
swings from 55°/30° to 32°/16° and the third build passed. Both were recorded as `WTF?:` as they happened.

**tools.md**, three items: the triangle cost of the soft-region recipe (its premise is wrong — see 04's
reading), no loop helper for non-idle animations, and no guidance on how far an arm link can turn before its
mesh kinks. The hand-in cites the compiler's message to `docs/MOTION.md` §2 and `src/motion.ts`; the session
never opened either, and neither holds it. It is documented in rig-c's `AUTHORING.md`.

**The dance, judged.** Scored blind by a person on 2026-10-21, as clip C of eight (A to H), without knowing whose it was: **7 out of 10**, one mark for the whole clip. `dance.mp4` is the clip the judge saw: `dance` three times round, 12 s at 24 fps, physics running throughout, one fixed viewport, a click on each beat. `dance_frames.jpg` is twelve frames of its first loop, every third of a second, labelled by time only. The score changes no line.
