# Tool Evaluation & Critique

This document provides constructive critiques and concrete enhancement proposals for the toolchain (`rig-pose`, `rigc`, and `@rig-c/parts`) based on experience during the Advanced R2 run retargeting sitting.

---

## 1. `rig-pose retarget`: Motion Clamping & Proportion Diagnostics

### Current Pain Point
When retargeting dynamic athletic sequences (such as running) with significant foreshortening, `rig-pose retarget` applies default `--leg-scale` bounds (`0.8, 1.05`) designed for walking strides. In a running motion where the shin compresses along the Z-axis down to 8.6% of its rest length, the tool silently clamps bone lengths without warning. This caused:
1. Artificially high lifted-foot heights (violating `Two feet` ratio: 1.284).
2. Unwanted penetrations of the unshortened leg into skirt geometry, inducing mesh folds.

Furthermore, when the rig's anatomical proportions (leg-to-torso ratio) differ drastically from the human performer, default translation scaling using torso endpoints (`mid_hip` to `neck`) produces severe overshooting of hip translation trajectories (horizontal 1.745, vertical 1.525).

### Concrete Proposals
- **Adaptive Leg-Scale Analysis / Warning:** Inspect the sequence's 2D segment foreshortening distribution prior to retargeting. If the minimum measured segment length is lower than the configured `--leg-scale min`, output a warning:
  `Warning: sequence 'shin_r' contracts to 0.086 of rest length, but --leg-scale min is 0.800. Clamping will distort foot trajectories.`
- **Proportion-Aware Scale Mode:** Provide an `--aspect-mode` option (e.g., `--aspect-mode leg` or `--aspect-mode torso` or `--aspect-mode auto`). If `--aspect-mode leg` is selected, position translations are scaled by $L / Ls$ (rig leg length / sequence leg length) directly, avoiding the need for manual offset anchor hacks in `map.json`.

---

## 2. `rigc render`: Mesh Fold Spatial Localization & Intersecting Bone Pinpointing

### Current Pain Point
When running `rigc render --folds`, the report only indicates the mesh identifier and the list of frames where self-intersection or boundary folding occurred:
```
skirt_front: 16 frames (10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 30, 31, 32, 33, 34, 35)
```
It gives no information regarding:
1. Which specific triangles or vertex indices inverted or intersected.
2. Which skeleton bones or collider volumes exerted the displacement causing the fold.

During debugging, this obscurity led to an initial hypothesis that the skirt physics translation constraints were too loose, whereas the true root cause was the leg failing to foreshorten and punching through the skirt.

### Concrete Proposals
- **Detailed Fold Diagnostics:** Add a `--verbose-folds` flag to `rigc render` that logs:
  - The bounding box / vertex IDs of the fold region.
  - The closest skeletal bone or active physics particle influencing those vertices.
- **Visual Fold Heatmap:** Generate an optional overlay image or debug color pass highlighting folded triangles in red on the rendered output frames.

---

## 3. `@rig-c/parts`: Physics Joint Coordinate Visualization & Collision Limits

### Current Pain Point
In `@rig-c/parts` and rig definitions (`rig.json`), physics secondary motion (e.g., hair, skirt bones) uses spring-damper dynamics with angle and translation limits. However, there is no interactive or offline preview tool to visualize physics anchor joints, translation limit envelopes, or rest positions relative to adjacent bone envelopes.

When adjusting translation physics limits (`translate_x`, `translate_y`), developers have to guess how far the mesh vertices will deform under inertial acceleration during running landings.

### Concrete Proposals
- **`rigc inspect --physics`:** Add an inspection subcommand that prints the computed rest positions, bounding envelopes, and spring limits of all physics chains, along with their associated collision mesh boundaries.
- **Physics Boundary Clamp Verification:** Provide compile-time static verification in `rigc build` checking if physics chain maximum travel intersects base skeleton rest poses.

---

## 4. Developer Ergonomics: Unified Pipeline & Stricter Schema Validation

### Current Pain Point
The retargeting, compilation, and rendering steps require multiple manual invocations across distinct CLI tools (`rig-pose retarget` -> `rigc build` -> `rigc render` -> `python3 tools/grade.py`). In iterative development, missing an intermediate `build` step after tweaking `map.json` or `rig.json` leads to evaluating stale skeleton builds against new motion files.

### Concrete Proposals
- **Pipeline Runner (`rig-pose run` or `rigc test`):** A high-level orchestration subcommand that runs retargeting, compilation, and headless verification in one shot, caching unchanged stages based on content hashes.
- **Strict Configuration Schema Linting:** Enhance `rigc inspect` to validate `map.json` anchor expressions (e.g. `eye_l+skirt2_0`) and emit descriptive errors if bone names or offset expressions do not resolve to valid rig skeleton definitions.
