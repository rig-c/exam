## A soft region's triangle cost is only visible after a build
- **I was trying to:** make task 04's chest soft with a contour mesh and keep the whole figure under 700 triangles.
- **The tool gave me:** the recipe in AUTHORING §3 ("A `contour` ... region", fragment with `"spacing": 6, "band": 16`) and the contour section's "the contour mesh used more vertices than the lattice at the same spacing". Nothing prints the triangles a given `spacing` will cost; I read them from `out/rig/mesh_report.json` after a full build (topwear went 86 -> 215, total 719).
- **What would have helped:** a sentence next to the recipe fragment saying roughly what its numbers cost (triangles for a circle of radius r plus band at spacing s), or `propose --from-config` / `mesh-draft` printing the triangle count per mesh without a build.
- **Cost:** two extra builds (about 5 minutes); got there.

## Nothing says how to keep feet planted under a moving hip
- **I was trying to:** task 05, make the legs follow the hip while the ankles stay on the shoes. The task says "what a figure needs ... is for you to work out".
- **The tool gave me:** `regions.legwear` = `hip` (a rigid region) from the proposal, and AUTHORING §3 `meshes.<part>` / `segments` (explicit `[bone, from, to]` lines weighting a vertex by distance). No document mentions a bone parented to `root` that a mesh segment can name, or a part weighted to two different bones top and bottom.
- **What would have helped:** one line in §3 (`segments`) such as "a segment may name a bone that is not under the others, for example a static bone under `root`; the part stretches between them", and the note that a part must then be removed from `regions`.
- **Cost:** about five minutes of reasoning; it built and passed first time, but I did not know a segment on a root-level bone was allowed until it ran.

## Which chain is which side of the image
- **I was trying to:** raise the image's right hand (task 02) and pick the free-hanging hair strands for physics.
- **The tool gave me:** chains named `sleeve_l`, `sleeve_r`, `lock`, `lock1_` in `proposal.json`, and the doc's sign note "`sleeve_l0`, the sleeve on the image's right" which is measured on `demo`, not on my painting.
- **What would have helped:** a `note:` line in `propose` naming for each sleeve chain which side of the image it is on and which sign of `rotate` lifts it, and for the hair chains which ones hang free of the face (the ones `propose` would call "locks").
- **Cost:** about two minutes, inferred from the chains' x positions (sleeve_l starts at x 507, sleeve_r at 357); confirmed only by rendering the wave.
