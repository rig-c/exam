## CHECK_TIP_OVER_ROOT did not narrow the remaining fix
- **I was trying to:** make `bottomwear` satisfy the tip-over-root check after removing the chest and hip segments the refusal named.
- **The tool gave me:** `the art in its lower half travels 11.466 rig px and in its upper half 19.981 rig px (ratio 0.574); a ratio >= 1.4725 is required ... the chain's amplitudes do not grow toward the tip, or the mesh is not weighted to the chain ... grow the chain's amplitudes toward the tip`.
- **What would have helped:** a reading of how the mesh's vertex weights and each chain link's travel contribute to the two halves, plus a concrete next adjustment when increasing the amplitudes scales both readings but leaves the ratio at 0.574.
- **Cost:** about 5 minutes; I did not get the bar to pass.

## Build needs fixture cap files beside the config
- **I was trying to:** build the mannequin from a run-local copy of its config.
- **The tool gave me:** `ASSEMBLE_LIMB_CAP_PRESENT ... names .../runs/2026-10-25-gpt-6-luna-05-dance/caps/arm_r_elbow.png, which is no such file; a PNG of the cap, its path relative to the config's directory, is required` (the same refusal named all nine caps).
- **What would have helped:** a build option to resolve fixture-relative asset paths from the fixture root, or a preflight listing every config-relative file before starting the build.
- **Cost:** about 5 seconds; I copied `fixtures/mannequin/caps/` beside the run config and the build passed.
