# The proctor's reading — claude-sonnet-5-5, 04-soft, 2026-10-20

Regraded: 9 of 9, the same lines — 667 triangles; `hop` as given; soft 6.61 rig px at hop frame 14; 32 of
104 `topwear` vertices move. 16.9 minutes by the run's own lines.

**What it did.** The documented soft-region recipe on task 01's config: a `chest_jiggle` bone under the
chest, `topwear` turned into a contour mesh with one circular region on that bone, and one physics
constraint with the recipe's values (inertia 0.25, strength 120, damping 0.92, x 0.5, y 1). Its own values:
the circle at (446, 322), radius 24, band 16 (the recipe's band), region spacing 10, outline spacing 30.

**The one miss.** The first build came to 719 triangles against 700. It graded anyway to read the other
lines (8 of 9, only the budget failing), coarsened the mesh to spacings 12 and 36, rebuilt (667) and
graded 9 of 9. Its entry 1 had turned down the recipe's spacing 6 because it would "blow the 700 budget",
and expected the total "near or over 700". Line 4 records 719 with "No WTF". The hedge covered both
outcomes, but the step's choice was made to land under the budget and it did not: the proctor reads that
line as one that should have been a `WTF?:`.

**The clock.** About 15 of the 16.9 minutes are two builds and two grader runs, each 3 to 4.7 minutes long
while other sittings were grading on the same machine (the regrade's grader takes 1.8 minutes on this task).

`chest_landing.jpg`: hop frame 14 at 30 fps (the grader's reported frame), with physics, without, and the
difference ×4 — one round patch at the chest, nothing else moves.
