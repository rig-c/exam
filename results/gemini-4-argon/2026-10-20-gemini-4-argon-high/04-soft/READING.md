# The proctor's reading — gemini-4-argon-high, 04-soft, 2026-10-20

Regraded: 9 of 9, the same lines: 654 triangles against 700; `topwear` differs from the build without
physics by 6.61 rig px at hop frame 14; 14 of 111 vertices move. 13.1 minutes.

**What it did.** The soft-region recipe: `topwear` on a contour mesh (spacing 31, the grid size the proposal
gave it) with one circular region on a new bone `chest_jiggle`, placed at the chest bone's own position
(446, 325), with the recipe's radius 28 and band 16. The physics values (inertia 0.25, strength 120, damping
0.92) are the recipe's. It worked out that the other meshes already take 504 triangles, set the region's
spacing to 12 rather than the recipe's 6 (the grader's comment says 6 costs 920 here), and the first build
came to 718 triangles, 18 over. It raised the region's spacing to 18 and the second build passed.

**The chest at the landing** (`chest_landing.jpg`: with physics, without, and the difference ×4): one round
patch in the middle of the shirt, over the placket and the end of the tie, moves; nothing else on the top does.

**Journal.** Three entries, one `WTF?:` (the 718 triangles), written as soon as the build printed it. The
end of the journal swaps the form's two closing questions for two of its own.

**tools.md** (handed in with 05) tells this task's story differently: a first build at contour spacing 24
and region spacing 14 giving 722 triangles, then both spacings changed to 31 and 18. No such build ran.
The first build was 31 and 12 for 718, only the region's spacing was changed, and 722 is task 03's
triangle count.
