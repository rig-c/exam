# Findings

The final command uses --leg-scale 0.4,1.2 --plant-feet --stance 0.02 --reduce 0.25 and run/map-parallel.json. The rig spec and physics values are unchanged. The pose sequence is unchanged.

Pose README “The map” supplies the chains, eye-line and pelvis aims, free hinges for front-facing motion and measured trunk scale. “The legs: foreshortening and planted feet” supplies segment scaling, one floor, in-place closure and stance. “Few keys: --reduce” supplies bounded reduction and explains why ankle error increases with angle tolerance. Trial 0.5 passed jitter but failed slide; 0.2 passed slide but failed jitter; 0.35 failed both. The trunk had reach:true despite its origin being 180 rig units above the translated hip. The map section states that without reach the trunk stays parallel to the reference. Turning reach off and using 0.25 passed both. This sacrifices shoulder endpoint matching to follow the measured trunk angle without an origin-offset re-aim.

The measured translation scale is 1.7707134152696318 rig units/source unit, from hip→neck / median mid_hip→neck. Rig L is 485.0928; source Ls is 426.70. The declared in-place closure drift is -224.73 units over 224 frames; grader removes +1.00778 units/frame. These are not travel-free visual fidelity claims.

All ten grader rows pass. Six synchronized evidence panels (0,8,16,24,77,205) were visually inspected in evidence/comparison.png. Each panel has separately fitted viewports: it is not a pixel comparison. Red lines are ankle-origin floor readings, not shoe-sole collision planes. The foot has one ankle bone; toe articulation and true sole contact were not added. Hair/skirt physics remain on with no new keyed physics bones. No detector is supplied, so rig-pose compare was not run and no detector-based or original-video similarity is claimed. Only the stick video and sequence were available.

The standalone build measured 21 assertions with zero failures; 17 assertions were skipped and 14 outside the spine profile. In particular A00_ROUNDTRIP_PARSE is skipped because the installed entry does not link spine-core. Grader itself reports zero skipped rows. No additional packages were installed to hide this distinction.

Initial setup broke prospective journaling and wrote a wrong placeholder timestamp. Those records are preserved verbatim in transcript.tmp, the journal and setup-history. Proctor message 0b4756d4-91df-45b2-92fe-d7d6348185f3 explicitly directed continuation and preservation. This report supersedes the premature termination claim, not the record of the slip.

Full before output: before/grade.txt. Final output: after/grade.txt. Trials retained in trial-1 through trial-3.
