# Reading — 04-soft

Independent regrade: **9 / 9**, parts1.60.0 / rig-c2.67.2. Every machine line and applicable SKIP matches the private submitted selfgrade; the final transcript supplies the finished clock. The proctor did not repair the answer.

The patch placement and contour sampling are authored from the part image and documented recipe. Mesh-stats is used before the grade. The submitted triangle count reaches the budget exactly; no proctor tuning was performed.

Measured lines (the build/check also pass):

- **budget**: "700 triangles against <= 700".
- **hop_as_given**: "the built rig holds `hop` exactly as tasks/04-soft/hop.json gives it".
- **soft**: "`topwear` differs from the same build without its physics by 6.61 rig px at hop frame 14, against 3.0 to 15.0".
- **a_patch**: "36 of 106 `topwear` vertices move over 0.5 rig px, against >= 8 and <= 80 %".
- **hop_does_not_fold**: [].

The physics-on/off landing frame14 and every generated sheet were read. Small raster softness is not a substitute for the paired-geometry bar. A read-only source PNG comparison is retained privately; preview cropping appearances are not treated as produced-sheet clipping. No diagnostic rebuild/render/regrade was added.

Paired source sheets: [physics on](pictures/pose_out_check_build_hop-hop@30fps.png) / [physics off](pictures/pose_out_without_physics_check_build_hop-hop@30fps.png).

Journal: intact, 4 entries / 0 literal WTF markers. Clock: 240s (4min rounded by grader). All 7 generated sheets were read; ordered native frame digests/commands/viewports/pins are in the [render receipt](render-receipt.json). [Retained sheet](pictures/folds_idle-idle.png). Source, host/model/access boundaries and separate native grader invocation/clock flags are in [who.json](../who.json).
