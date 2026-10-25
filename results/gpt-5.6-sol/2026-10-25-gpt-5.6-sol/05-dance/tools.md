## mesh-stats did not identify the directory shape it wanted
- **I was trying to:** count the soft-region triangles before building task 04, using the recipe's `rig-parts mesh-stats --config config.json --parts work/rig` form.
- **The tool gave me:** `FAIL  PARTS_FILE_PRESENT: runs/2026-10-25-gpt-5.6-sol-01-build/work/parts.json — no such file`.
- **What would have helped:** `--parts must name the assemble output root containing parts.json and parts/, not its rig/ subdirectory` in the help and recipe, or acceptance of the documented `work/rig` layout.
- **Cost:** about one minute; I followed the missing path in the refusal, retried with the task 01 build root, and got there in the end.

## No preflight for animation seam pairs
- **I was trying to:** make task 02's head-and-chest gesture stay closed at both armholes before running the full grader.
- **The tool gave me:** build said `SEAM_OVER_MOTION: SKIP — no neighbour pair is declared`, while the grader later reported `topwear|handwear_l` open on 10 frames.
- **What would have helped:** a `rig-parts check` option that takes ad-hoc part pairs for `SEAM_OVER_MOTION`, with an example for `topwear` against each upper arm in the named-animation recipe.
- **Cost:** about three minutes plus a rebuild and regrade; I changed the symmetric gesture to the documented one-direction turn and passed in the end.

## Moving a config needs an asset base
- **I was trying to:** build the mannequin fixture config from the required run directory after adding `dance.json`.
- **The tool gave me:** nine `ASSEMBLE_LIMB_CAP_PRESENT` lines resolving `caps/*.png` relative to the moved config's directory.
- **What would have helped:** a `--config-base <dir>` option, or a build message saying to preserve or link config-relative assets when copying a config for a run.
- **Cost:** about one minute; I linked the fixture's caps into the run directory and got there in the end.
