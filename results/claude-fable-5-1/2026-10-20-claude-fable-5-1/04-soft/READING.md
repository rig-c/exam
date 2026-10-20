# The proctor's reading — claude-fable-5-1, 04-soft, 2026-10-20

Regraded: 9 of 9, the same lines — 692 triangles against 700; `topwear` differs from the build without
physics by 6.61 rig px at hop frame 14; 40 of 112 vertices move. 10.1 minutes.

**What it did.** The soft-region recipe: `topwear` from a grid to a contour mesh (spacing 31) with one circular
region (centre 446, 332; radius 30; spacing 12; band 16) on a new bone `chest_jiggle` under `chest`. The
physics values (inertia 0.25, strength 120, damping 0.92, x 0.5, y 1) and the band are the recipe's; the centre
is the shirt's own centre line, and the radius and spacings its own. One build, 8 triangles under the budget
on the first try.

**The chest at the landing** (`chest_landing.jpg`: with physics, without, and the difference ×4): one round
patch at the middle of the shirt moves, nothing else on the top comes loose.

**Journal.** Two entries, no `WTF?:`.
