## Foot bone in a leg chain
- **I was trying to:** map the foot bone with the ankle.
- **The tool gave me:** `MAP_CHAIN_JOINTS: chain "leg_r" has 3 bone(s) and 3 joint(s); bone k carries the segment from joint k to joint k+1, so it needs 4`
- **What would have helped:** a note that body-18 has no toe, so the last bone of a leg is the shin and the foot is left unkeyed.
- **Cost:** 2 minutes, got there.

## Output directory not created
- **I was trying to:** write `--out run/after/motion.json` on a fresh run dir.
- **The tool gave me:** `FAIL  ARG_PATH: --out run/after/motion.json — directory run/after does not exist`
- **What would have helped:** create it, or name the flag that does.
- **Cost:** 1 minute.

## rigc build rejects the rig directory
- **I was trying to:** rebuild with the same `--rig inputs/rig` retarget takes.
- **The tool gave me:** `cannot read .../inputs/rig: EISDIR: illegal operation on a directory (see rigc guide CE_COMPILE_JSON_READ_FAILED)`
- **What would have helped:** accept a directory holding rig.json, as retarget does.
- **Cost:** 2 minutes.

## Choosing the translate scale pair
- **I was trying to:** make hip travel match the sequence's in leg lengths and hip widths.
- **The tool gave me:** README: "Pick a long segment that does not foreshorten much." The trunk pair gave hip-vertical 1.460 and hip-horizontal 1.712.
- **What would have helped:** retarget printing the rig/pose ratio for trunk, leg and hip width so the pair can be picked; and a line that this scale also sizes `reach`.
- **Cost:** about 10 minutes, got there by arithmetic from the grader.

## reach breaks with a different scale
- **I was trying to:** keep the trunk on the shoulders after changing the scale.
- **The tool gave me:** nothing; trunk+head jitter 3.625x and 155 folds appeared silently.
- **What would have helped:** a POSTURE or warning line that the reach target is off in distance.
- **Cost:** about 8 minutes.

## Leg-scale minimum vs lift
- **I was trying to:** bring the lifted foot's height ratio (1.29) into 0.85–1.15.
- **The tool gave me:** `--leg-scale <min,max> ... (default: off; 0.8,1.05 is the card's range)`
- **What would have helped:** a sentence that the minimum limits how far the hip-side leg can shorten, so it sets the lifted foot's height.
- **Cost:** about 12 minutes of sweeping (0.8, 0.6, 0.5, 0.4), got there.
