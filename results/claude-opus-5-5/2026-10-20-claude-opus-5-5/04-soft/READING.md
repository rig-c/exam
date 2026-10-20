# The proctor's reading — claude-opus-5-5, 04-soft, 2026-10-20

Regraded: 9 of 9, the same lines — 683 triangles against 700; `hop` as given; `topwear` differs from the
same build without physics by 6.61 rig px at hop frame 14; 34 of 112 `topwear` vertices move. 10.4 minutes by
the run's own lines.

**What it did.** `topwear` turned into a contour mesh (tolerance 1.5, spacing 31) with a circular region of
radius 28 at (436, 318) bound to a new `chest_jiggle` bone on `chest`, spacing 12, band 16, and a physics
constraint with the values of AUTHORING *Recipe: a soft region* (inertia 0.25, strength 120, damping 0.92).
It rendered `hop` with physics on before grading.

**Journal.** Three entries, no `WTF?:`. Its guesses were close: 150–200 topwear triangles (179), 5–8 px (6.61),
about 37 % of the vertices (30 %).

**The transcript.** Commands and their last lines, the Python step that wrote `config.json` excepted.

`chest_landing.jpg`: hop frame 14 at 30 fps (the grader's frame) with physics, without, and their difference
×4. Most of the difference is the side locks' physics from task 02; the chest's is a small patch below the
collar.
