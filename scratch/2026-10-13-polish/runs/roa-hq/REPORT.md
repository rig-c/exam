# The commanding session's own polish pass (Roa, rig HQ)

This is not a sitting. The HQ session that built the rig had already seen everything, so it could not sit the task. This folder is its own first polish pass on the same demo, kept for comparison with the two sittings. Its conditions differ from theirs:

- It started from the **owner's pass-1 findings**, not from its own search. The owner named three: the skirt passes through the legs; in the low-hands span an arm is drawn under the jacket and the hand shapes are gone; the skirt only tilts.
- It worked as a commander: the HQ session (Opus 5.5) and two Opus 5.5 sub-agents, one per unit (arms, cloth), run in parallel. Wall clock: about 19 min (arms) and 49 min (cloth).
- `POLISH.md` is the checklist the pass used.

The figures below are the sub-agents' measurements as reported to HQ. HQ looked at the before/after pictures; those set video frames beside the rig, so they are not in this repository.

## Arms unit (`arms/`)

- **Layer.** Both pieces of the left arm in the low-hands set (K2) had been placed behind the jacket, because the assembly script's place table was written by hand and never measured. In that span the whole arm vanished, and only a cuff showed below the hem. Two slots were added in front of the jacket and skirt, behind the right arm, and the K2 attachment keys moved to them; no bone key changed. The upper-arm piece was trimmed to what the painting shows as sleeve: the arm layer runs under the jacket's front panel, and drawn in front it left a ghost of the badge.
- **Hands.** The two hands had not been cut through. The split by distance to the skeleton extended a forearm past the wrist and put **93 %** of both hands' skin on one forearm. They were re-split along the painted boundary (1436 / 470 px).
- **Result.** Only frames 183–261 changed. Gates were green: rig-c 2.51.1 core build, and spine-core round trip `A00_ROUNDTRIP_PARSE` passed.
- **Found, not fixed.** The video's low-hands span is crossed wrists with two fists, not a clasp, so K2 itself should be repainted. A set's upper arm held at its ±20° limit sits over the chest. The behind-the-back set leaves a dashed seam line beside the skirt.

## Cloth unit (`cloth/`)

- **Through the legs.** On the dance, the skirt hem was inside the thigh outline on **41 of 313 frames → 0**, and 0 on all 30 animations. An earlier stiff "cone" tune made it worse (85).
- **Shape change.** Five radial chains replaced three. Their first links follow one shared swing bone (independent springs crossed the middle chains). The outer chains are held off the thighs by an IK-aimed frame, a world copy and a transform clamp: not past rest inwards, up to 60° outwards. Spine physics has no colliders, so this is a stand-in. Cost: bones 57 → 91, constraints 12 → 36. It runs live in any motion.
- **Against the reference skirt** (lag / swing / overshoot per span; bands fixed before measuring): 6 of 6 in band, from 5 of 6. Fold-free with physics on, at 24 and 30 fps, on every animation.
- **Not reached.** The fine ripple of the pleated hem: a deform applies to every vertex, so "only the hem ripples" cannot be written. This became rig-c/core#1413.

## What the comparison showed

The owner's eye found the two largest faults: the skirt through the legs, and the arm under the jacket. Neither sitting found them. Both sittings found what neither the owner nor this pass looked at: blinks and foot planting. One of them also split the shins' folding bridge, and one added breathing and hair sway. The owner's verdict afterwards: the limit is the retarget itself (the pelvis's U-shaped bounce is missing), and getting the pose right is worth more than any post-correction. That is rig-c/pose#47.
