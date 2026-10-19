## Arm elbow refused as a joint limit
- **I was trying to:** get retarget to run with the sequence's arms on the rig.
- **The tool gave me:** `FAIL  POSE_BEND_ONE_WAY: chain "arm_r" hinge r_elbow, frame 200 … so the angle must stay ≤ 0` (226 problems, nothing written).
- **What would have helped:** a line in that message pointing to `"bend": "free"` for front-facing hinges, as the README says.
- **Cost:** about 5 minutes; found it in the pose README map section.

## Knee refused for an undeclared bend side
- **I was trying to:** get the leg chains through the gate.
- **The tool gave me:** `FAIL  MAP_BEND_SIDE: chain "leg_r" — the hinge at r_knee is straight at rest (inner angle 0.179°) … state "bend": "ccw", "cw" or "free"`.
- **What would have helped:** the message naming which of the three values is right for a knee on a front view, not only that one must be stated.
- **Cost:** about 3 minutes; chose `free`, following the elbow note.

## rigc build rejects the rig directory
- **I was trying to:** run the gate on the rig (`rigc build --rig inputs/rig`) as I had with retarget.
- **The tool gave me:** `rigc compile error: cannot read …/inputs/rig: EISDIR: illegal operation on a directory, read (see rigc guide CE_COMPILE_JSON_READ_FAILED)`.
- **What would have helped:** either accepting the directory as retarget does, or the message naming `rig.json`.
- **Cost:** about 4 minutes; the guide reference did not cover this case, I found it by trying the file.

## Trunk jitter has no cause shown
- **I was trying to:** bring the trunk+head jitter row under 1.1.
- **The tool gave me:** `trunk+head 1.390x sequence (0.999 vs 0.719 deg/f^2, chest,head)`, with no reason.
- **What would have helped:** a pointer from the jitter figure to the chain or option producing it.
- **Cost:** about 15 minutes of variants before removing `reach` from the trunk chain fixed it.

## Stance default pins lifted feet
- **I was trying to:** keep the two-feet lift between 0.85 and 1.15.
- **The tool gave me:** the card's default `--stance 0.07` and the help text saying it plants "a free ankle within this many leg lengths"; with it the lift ratio was 0.616.
- **What would have helped:** a note that 0.07 can pin lifts above the grader's 0.04 threshold on this kind of sequence, or a suggested value.
- **Cost:** about 10 minutes; resolved by setting 0.03.
