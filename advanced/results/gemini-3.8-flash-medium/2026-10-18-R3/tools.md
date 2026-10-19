# Tools Feedback

## rigc build directory rejection (EISDIR)
- **I was trying to:** Run `rigc build --rig inputs/rig` using the same directory argument format accepted by `rig-pose retarget --rig inputs/rig`.
- **The tool gave me:** `rigc compile error: cannot read inputs/rig: EISDIR: illegal operation on a directory, read (see rigc guide CE_COMPILE_JSON_READ_FAILED)`
- **What would have helped:** Consistent CLI argument resolution across toolchain packages where `rigc build --rig <dir>` automatically discovers `<dir>/rig.json`, or an error message explicitly stating "path is a directory; specify rig.json directly".
- **Cost:** ~5 minutes to consult `rigc build --help` and adjust arguments to `--rig inputs/rig/rig.json --images inputs/rig/images`; resolved on retry.

## Key reduction (--reduce) degrading planted foot stability
- **I was trying to:** Reduce rotational jitter using `--reduce 1` and `--reduce-hip 1` as recommended in the documentation for `dance-a`.
- **The tool gave me:** `Slide: max support-foot move 0.01651 leg lengths/frame (foot_r, frame 64->65) over 294 steps [bar <= 0.005]` and ankle landing tolerances widened to 11.8 units, causing support foot drift across blend boundaries.
- **What would have helped:** A CLI warning or note in the documentation that `--reduce-hip` and `--reduce` on supporting leg chains can override `--plant-feet` precision, or an option to lock planted leg chains to dense keys while reducing upper-body bones.
- **Cost:** ~10 minutes diagnosing per-frame bone coordinates around blend frames before omitting `--reduce-hip` and `--reduce`.

## Documented --stance recommendation exceeding lifted threshold
- **I was trying to:** Plant the free foot on two-foot frames using the card's documented value `--stance 0.07`.
- **The tool gave me:** `Two feet: lifted frames (sequence ankles > 0.04 apart): 35 of 35 with the lifted foot within 0.01 of the support foot [bar 0]; median rig/sequence lift 0.008 [bar 0.85-1.15]` — every single lifted dance frame was forcefully flattened to the floor.
- **What would have helped:** A note in documentation or `--help` cautioning that `--stance` must remain below the 0.04 leg-length threshold used to classify lifted frames, or an adaptive stance algorithm that respects intentional low-lift choreography.
- **Cost:** ~10 minutes inspecting sequence ankle height deltas to calculate a working threshold (0.035) between the landing gap (0.0296) and the minimum lifted height (0.0416).
