## Parent output directories are not created
- **I was trying to:** Write the first retarget motion and report into run/before/.
- **The tool gave me:** "FAIL  ARG_PATH: --out run/before/motion.json — directory run/before does not exist" and the matching --report failure.
- **What would have helped:** The Try it command could say, "Create the parent directories for --out and --report first; retarget does not create them."
- **Cost:** Roughly a minute including recording and retrying; resolved with mkdir.

## Translation calibration needs an anatomical recipe
- **I was trying to:** Match normalized pelvis travel on a rig whose torso-to-leg proportions differ from the subject's.
- **The tool gave me:** README §The map: "Pick a long segment that does not foreshorten much." The first SCALE line was "1.78104 rig units per picture px (rig 360.00 / pose median 202.13)".
- **What would have helped:** A documented leg-length calibration option or recipe, with the exact percentile definition and a separate horizontal gain, plus a warning when torso and leg calibration disagree substantially.
- **Cost:** Several minutes and two calibration retarget/build/render iterations; resolved with a measured marker plus a 0.95 empirical gain correction.

## Reported scale hides exact-boundary precision
- **I was trying to:** Keep every rendered shin scale at or above the 0.4 bar.
- **The tool gave me:** "world x axis 0.400 … 1.036" in SHEAR, and LEG-SCALE said scalex was keyed in [0.4, 1.2], while the exact rendered geometry's p5 failed the >=0.4 comparison.
- **What would have helped:** Print more digits on a clamped minimum, or explicitly state that the landing tolerance and serialized transform precision can place the measured value slightly below the requested minimum.
- **Cost:** One failed grading iteration and a small clamp-margin adjustment; resolved at 0.405. This was numeric precision, not a new motion error.
