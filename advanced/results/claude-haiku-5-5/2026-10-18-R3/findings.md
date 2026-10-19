# Findings — dance (R3)

- Rig: inputs/rig (rig.json needs its motion.json beside it; rig.json alone is refused).
- Pelvis tilt: the translate-only map leaves hip rotation unkeyed (tilt 0.000). A one-bone `pelvis` chain (hip; l_hip→r_hip; aim leg_r0) keys it (1.000 of sequence).
- Stance planting (`--stance`) is the support/lift switch: 0.07 and 0.02 leave lift at 0.015/0 (two-feet fail on lift ratio); 0.035 satisfies both support and lift; no --stance fails support (0.041).
- `--reduce 0.5` adds a 0.0087 leg-length/frame slide on foot_r at frames 83→84; removing it brings slide to 0.00003.
- Knee bend guard: 566 POSE_BEND_ONE_WAY frames on leg_l l_knee (-0.1 to -6.4 deg). Resolved with `--bends clamp`, which straightens those frames; not checked against the video.
- Scores after: 13/13 PASS. Before: 9 pass / 4 fail (support-foot, two-feet, slide, hip-tilt).
