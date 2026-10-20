# The proctor's reading — gemini-3.8-flash-medium, 04-soft, 2026-10-20

Regraded: 9 of 9, the same lines — 636 triangles against 700; `topwear` differs from the build without
physics by 6.61 rig px at hop frame 14; 14 of 114 vertices move. 7.0 minutes.

**What it did.** The soft-region recipe: `topwear` on a contour mesh with one circular region on a new bone
`chest_jiggle`, placed at the chest bone's own position (446, 325) with the recipe's radius 28 and band 16.
The physics values (inertia 0.25, strength 120, damping 0.92) are the recipe's. It set the region's spacing
to 12 rather than the recipe's 6 (the grader's comment says 6 costs 920 triangles here) and the contour to
24, and the first build came to 742 triangles: `budget` failed, everything else passed. It coarsened the
contour to 30, the region to 18 and the skirt grid from 31 to 34, and the second build passed.

**The chest at the landing** (`chest_landing.jpg`: with physics, without, and the difference ×4): one round
patch on the middle of the shirt, over the placket and the tie's knot, moves; nothing else on the top does.

**Journal.** Five entries, one `WTF?:` (the 742 triangles), written as soon as the grader printed it.

**tools.md** (handed in with 05) says the recipe's region spacing 6 produced the 742 triangles. It did not:
the session never built spacing 6; the 742 came from its own spacing 12 and contour 24, as its journal here says.
