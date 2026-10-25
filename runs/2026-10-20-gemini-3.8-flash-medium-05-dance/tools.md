## Contour mesh region spacing triangle cost not documented in recipe
- **I was trying to:** Author a soft region in `topwear` using a `contour` mesh with a circular `bust` region under a triangle budget of 700.
- **The tool gave me:** Following the recipe in `node_modules/@rig-c/parts/docs/AUTHORING.md` §3 ("Recipe: a soft region driven by physics") which specified region `spacing: 6`, the rig built with 742 triangles and failed the grader: `FAIL  budget: "742 triangles against <= 700"`.
- **What would have helped:** A note in `AUTHORING.md` §3 beside the recipe stating the triangle cost of region `spacing: 6` (e.g. "adding ~300+ triangles on a typical circular patch; for tight triangle budgets, increase region spacing to 12–18"), or a `rig-parts mesh` command reporting estimated triangle count for a contour region configuration without running full build.
- **Cost:** Roughly 3 minutes to diagnose the triangle breakdown, relax contour spacing to 30 and region spacing to 18 (and bottomwear grid to 34), and re-grade. Got there in the end (636 triangles).

## Motion spec lacks loop/period helper for non-idle animations
- **I was trying to:** Author a periodic 4.0-second dance animation repeating a 1.0-second (2-beat) motif across 4 cycles.
- **The tool gave me:** `rigc compile error: /var/folders/.../motion.json: animation "dance" bone "sleeve_l0" rotate: key times must strictly increase (at t=1)`.
- **What would have helped:** Either native support in `rigc-motion/1` for track looping/periods (analogous to the `period` and `cycles` properties supported in idle motion tracks), or an explicit warning in `docs/MOTION.md` noting that procedural repetition must drop cycle boundary keys `t == period` to avoid duplicate timestamps.
- **Cost:** Roughly 2 minutes to inspect `grade.log`, fix the key generator to strictly order timestamps, and rebuild. Got there in the end.

## Skinning blend kink limit vs joint rotation not documented for arm bands
- **I was trying to:** Animate expressive arm swings during dance meeting `both_hands >= 100` rig px travel while keeping limb straightness `arms_bend_at_the_joints <= 8.0` degrees.
- **The tool gave me:** `FAIL  arms_bend_at_the_joints: "along its own length an upper arm or a forearm bends at most 9.2 degrees more than at rest, against <= 8.0"` when swinging `sleeve_*0` by 55 degrees and `sleeve_*1` by 30 degrees.
- **What would have helped:** In `AUTHORING.md` §3/§4 under arm motion and weight binds, guidance on how elbow weighting influences adjacent bands and the safe relative rotation limit (e.g., "relative elbow bend over 30° creates ~9° vertex kink in the adjacent lower upper-arm band; keep individual link turns <= 35°").
- **Cost:** Roughly 3 minutes to moderate arm rotation angles from ±55/±30 to ±32/±16 degrees and re-grade. Got there in the end (5.3 degrees, 305 px hand travel).
