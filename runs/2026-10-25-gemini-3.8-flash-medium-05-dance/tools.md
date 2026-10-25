# Tools Feedback

## mesh-stats requires existing intermediate parts directory
- **I was trying to:** Check and predict triangle counts for a contour mesh with custom region spacing before running a full build in Task 04 to fit under the 700 triangle budget.
- **The tool gave me:** `FAIL PARTS_FILE_PRESENT: out_04/parts/parts.json — no such file (see rig-parts guide PARTS_FILE_PRESENT)`
- **What would have helped:** A command or flag like `rig-parts mesh-stats --config <config.json> --candidate <build_dir>` or `mesh-stats` being able to derive part metrics directly from the config and source inputs or existing `out/check/build/` artifacts without requiring the ephemeral `parts/` intermediate directory.
- **Cost:** ~2.5 minutes; worked around by iteratively re-running `rig-parts build` and inspecting `out/check/check.json`'s `TEXTURE_STRETCH.triangles`.

## propose --cloth fails on modified motion tracks without overwrite option
- **I was trying to:** Apply the cloth recipe propose command on `back hair` after previously adjusting amplitude signs on hairback tracks.
- **The tool gave me:** `FAIL PROPOSE_WRITE_CONFIG_CONFLICT: config.motion.tracks[5] "hairback_l" — already in config.motion.tracks and not identical to what would be written`
- **What would have helped:** A `--force` or `--replace-tracks` flag in `propose --cloth` to automatically overwrite or drop conflicting legacy tracks rather than refusing with an unrecoverable conflict error.
- **Cost:** ~2 minutes; resolved by manually editing `config.json` to strip the conflicting manual tracks before re-running `propose --cloth`.

## assemble requires limb caps relative only to config directory
- **I was trying to:** Run `rig-parts build` on a run directory holding `config.json` referencing fixture limb caps (`caps/*.png`).
- **The tool gave me:** `FAIL ASSEMBLE_LIMB_CAP_PRESENT: config.limbs.arm_r.segments[1].cap (part "forearm_r") — names .../runs/.../caps/arm_r_elbow.png, which is no such file; a PNG of the cap, its path relative to the config's directory, is required`
- **What would have helped:** A `--caps <dir>` CLI option or base-asset resolution fallback so assets like joint caps can be shared across config iterations without having to duplicate image files into every run folder.
- **Cost:** ~1 minute; resolved because `grade.py` handles fixture asset copying into its isolated work directory.
