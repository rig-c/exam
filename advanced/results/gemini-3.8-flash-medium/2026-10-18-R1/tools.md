# Tools Feedback

## Inconsistent directory resolution between rig-pose and rigc build
- **I was trying to:** Build the newly retargeted motion by passing the rig directory (`--rig inputs/rig`) to `rigc build`, exactly as accepted by `rig-pose retarget`.
- **The tool gave me:** `rigc compile error: cannot read inputs/rig: EISDIR: illegal operation on a directory, read (see rigc guide CE_COMPILE_JSON_READ_FAILED)`
- **What would have helped:** `rigc build` should auto-resolve a directory argument to `<dir>/rig.json` (just like `rig-pose retarget`), or display a friendly error: `--rig is a directory; did you mean inputs/rig/rig.json?`.
- **Cost:** ~2 minutes to realize the CLI discrepancy and rerun with the explicit file path; got there immediately.

## Implicit inPlace activation requirement on --plant-feet
- **I was trying to:** Understand why the head world rotation differed by 1.38° between cycle 1 and cycle 7 even though the input sequence joint coordinates were mathematically identical across cycles and declared `"travel": "in-place"`.
- **The tool gave me:** No diagnostic warning. In the source (`retarget.ts`), `const inPlace = plantOn && opts.travel === TRAVEL_IN_PLACE;` silently evaluated to `false` when `--plant-feet` was omitted, causing `maxNod = 0.02 * neckRestLen` to trigger a non-wrapping boundary-clipped sliding window that polluted `head.rotate`.
- **What would have helped:** A diagnostic log or warning: `sequence declares travel: in-place but --plant-feet is off; in-place loop processing and unconstrained head nod disabled`.
- **Cost:** ~10 minutes inspecting source code to find the coupling between `--plant-feet` and `inPlace`; got there in the end.

## Lack of measured foreshortening guidance for --leg-scale
- **I was trying to:** Lift the swing leg to pass the `two-feet` bar.
- **The tool gave me:** In README: `0.8,1.05 is the card's range, rig-c/pose#47`, but in a face-on stride the forward-swinging shin compresses down to 0.451 of its straight length.
- **What would have helped:** In `retarget`'s output or report, print the observed minimum segment length ratio: `LEG-SCALE observed r_shin min ratio 0.451 (below card range 0.8; consider --leg-scale 0.45,1.05)`.
- **Cost:** ~5 minutes writing a node script to inspect sequence joint distances; got there in the end.
