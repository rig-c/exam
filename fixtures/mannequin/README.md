# Wooden mannequin — exam fixture

A rig of a wooden artist's mannequin painting (SDXL base 1.0 + 4x-AnimeSharp upscale, frontal, legs apart,
1664×2432), made for a task whose subject is the motion, not the rig: every joint a dance needs is already
in it, with fixed ankle targets and the reach limits below. Everything here was made for this exam; see *Licence*.

## What is in the folder

| path | what |
| --- | --- |
| `inputs/painting.png` | the painting, 1664×2432, pure white background; `inputs/SHA256` holds its hash |
| `inputs/generation.json` | how the painting was made: checkpoint, sampler, seed, prompts, pose control, the background step |
| `inputs/pose.json` | the pose control the painting was drawn from (832×1216 latent px) |
| `inputs/layers/full/`, `inputs/layers/head/` | the layered input the build reads (See-through, ComfyUI wrapper form) |
| `inputs/keypoints.json` | the 13 body joints the rig was proposed from (`spine-parts-keypoints/1`, painting px) |
| `caps/*.png` | the ball joints' upper halves, one per limb joint (painted for this rig) |
| `config.json` | the rig-parts config: bones, limbs, ranges, iks and the idle |

The build is not shipped: it is made from these files, the same way `grade.py` builds every run. From this
folder, on the pinned tools:

    rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out

It exits 0 and its check line is:

```
[check] check: PASS; 9 of 14 bar(s) measured, 5 skipped (BLINK_NO_HOLE, TIP_OVER_ROOT, TEXTURE_STRETCH, FEET_STAY_LEVEL, STRESS_OFF_CHAIN); 0 warning(s) (SEAM_OVER_MOTION, not a bar)
```

The rig is in `out/rig/rig.json` and `out/rig/motion.json`, the gated Spine data in
`out/check/build/skeleton.{json,atlas,png}`.

**Tools.** Built with `@rig-c/parts` 1.49.1 and the `rig-c` it installs, 2.64.1 (`@rig-c/core` 2.64.1), and
measured again on the versions the root `package.json` pins for Round 4 (`@rig-c/parts` 1.58.0, `rig-c`
2.67.2): the same exit and the same check line. Rig px = painting px × 0.5 (832×1216).

## The joints

Every piece is rigid on one bone (weight 1); a bend is a rotation at a joint. Each joint below a limb segment
declares `range [-45, 45]`, and `check`'s `SEAM_OVER_RANGE` poses it at -45, 0 and +45.

| joint | bone that turns | parent | range | pivot (rig px, r / l) |
| --- | --- | --- | --- | --- |
| waist (breath only) | `chest` | `hip` | none declared | 416, 456 |
| neck (head on the neck ball) | `head` | `neck` (rigid on `chest`) | [-45, 45] | 417, 205 |
| shoulder | `sleeve_r0` / `sleeve_l0` | `chest` | none declared | 326, 286 / 505, 285 |
| elbow | `sleeve_r1` / `sleeve_l1` | upper arm | [-45, 45] | 253, 424 / 578, 423 |
| wrist | `hand_r` / `hand_l` | forearm | [-45, 45] | 165, 547 / 661, 546 |
| hip | `leg_r0` / `leg_l0` | `hip` | none declared | 374, 623 / 454, 623 |
| knee | `leg_r1` / `leg_l1` | thigh | [-45, 45] | 345, 864 / 483, 866 |
| ankle | `foot_r` / `foot_l` (inherit `noRotationOrReflection`) | shin | [-45, 45] | 320, 1108 / 507, 1108 |

`_r` is the mannequin's right, which is image left. The parts on those bones are `headpiece`, `neckpiece`,
`topwear` (chest), `pelvis`, `upperarm_*`, `forearm_*`, `hand_*`, `thigh_*`, `shin_*` and `foot_*`.

**Feet are planted by the rig.** `foot_r_tgt` and `foot_l_tgt` are bones under `root` at the ankles. Two iks,
`leg_r_ik` and `leg_l_ik`, run over `[leg_*0, leg_*1]` at mix 1, and both knees bend outward. The targets stay
put; the legs can reach them only within their available length. To pose a leg by hand, key the ik's mix to 0 in the animation
(`"ik": [{"constraint": "leg_r_ik", "keys": [{"t": 0, "mix": 0}]}]`).

### Planted-leg reach

Near setup, with no hip rotation, the hip can rise only about **0.02 rig px** and move sideways only about
**0.2 rig px** before one leg straightens. Sideways travel beyond that tiny slack needs a dip: a **10 rig px**
sideways shift needs about **1.2 rig px** of lowering. The knees are nearly straight at rest, with a little
positive slack, not exactly zero. These are geometric limits, not a dance recipe or a guarantee of drawing contact.

The source is [config.json](config.json), whose bone positions are already in rig px. The hip bone is at
`(414,623)` in image coordinates; the right and left hip joints are offset from it by `b_r=(-40,0)` and
`b_l=(40,0)`. Use y-up coordinates for animation: positive `translatey` raises the hip. With unchanged root,
unit scales, fixed targets, IK mix 1, softness 0 and no stretch, the target offsets from those joints are
`q_r=(-54,-485)` and `q_l=(53,-485)`.

The pinned parts 1.60.0 writer rounds local offsets/angles to six decimals and bone lengths to three.
The core 2.67.2 two-bone IK uses the distance to the child's origin as its first link, not the rounded
parent `length` field. The resulting approximate lengths are:

| side | first link | second link | outer reach | inner reach |
| --- | --- | --- | --- | --- |
| right | 242.738542 | 245.277 | 488.015542 | 2.538458 |
| left | 244.724335 | 243.187 | 487.911335 | 1.537335 |

For hip translation `t=(x,y)` and rotation `theta`, let `R(theta)` be the usual CCW rotation. **Both** legs
need `inner_s <= norm(q_s - t - (R(theta)-I)b_s) <= outer_s`. Rotation moves the two hip joints differently;
using only the hip bone's origin misses that offset. With no hip rotation:

```text
right: inner_r^2 <= (x+54)^2 + (y+485)^2 <= 488.015542^2
left:  inner_l^2 <= (x-53)^2 + (y+485)^2 <= 487.911335^2
```

Near setup, `y_max(x) = min_s(sqrt(outer_s^2 - (x-q_s.x)^2) - 485)` when both square roots exist.

| hip x shift | greatest hip y shift near setup |
| --- | --- |
| 0 | 0.018731 |
| 10 | -1.199246 |
| -10 | -1.173098 |

At `y=0`, the shared horizontal interval is approximately `[-0.220962, 0.167972]` rig px. These figures
describe the written geometry before runtime float32 rounding; they are not extra grading thresholds.

**What the ankle line reads.** `grade.py`'s `on_her_feet` uses attachment vertices, not the IK target or
shin bone tip. For each `shin_*`, it selects vertices in the lowest 4% of its height in **frame 0**, averages
their positions, and selects the nearest `foot_*` vertex in that frame. Keeping those indices, it measures
the largest change in their relative offset across the animation, rounded to two decimals. Each shin is
read separately. A reachable target does not guarantee that this drawing-based distance stays within
the task's existing six-pixel bar; a foot staying level is also a different reading.

### Signs

Rotation keys **add to the local setup rotation**. Positive is counter-clockwise in y-up coordinates;
image y goes down. A positive `sleeve_r0` lowers the right arm and a positive `sleeve_l0` raises the left.
With all other bones held at setup:

| bone | local setup rotation (degrees) | a positive rotation delta |
| --- | --- | --- |
| `sleeve_r1` | -7.703526 | turns the forearm CCW; its wrist initially moves image-right/down |
| `sleeve_l1` | 6.133157 | turns the forearm CCW; its wrist initially moves image-right/up |
| `hand_r` | 125.581718 | turns the hand frame CCW from its upright rest orientation |
| `hand_l` | 55.988651 | turns the hand frame CCW from its upright rest orientation |

The wrist setup rotations cancel the forearms' rest turns, so both hand frames have world rotation 0 at
setup. A positive wrist delta takes the frame's +x axis toward +y; negative reverses it. Parent motion
carries the frame with it. “Positive bends inward” is not a pose-independent rule for either joint.

**Idle.** A breath on `chest` (`translatey`, 9.28 px peak to peak), plus sways on `neck`, `head` and both sleeve
chains. It lasts 40 frames at 12 fps.

## Known limits

- **Shoulders and hips have no declared range and no ball.** A hip-ball layer was tried and taken out: the wedge
  between the flat pelvis and the thigh's dome lies outside any ball about the hip pivot. When those bones
  turn, a concave corner opens between the pieces. On a strict reader (pixels a 3 px closing fills inside a
  disc of 0.75 × the limb's width about the joint, minus the same at rest; bar ≤ 6 px) it is already over that
  bar at ±45 — up to 23 px at a shoulder and 26 px at a hip — and grows beyond it. No bar in `check` reads it,
  because no range is declared there.
- **The neck** reads 12 / 10 px at +45 / -45 on that same reader, while `SEAM_OVER_RANGE` passes the nape.
- **The declared joints hold.** Elbows, wrists, knees and ankles stay at ≤ 6 px on that reader at ±45.
- **No floor shadow.** The painting's negative prompt carries `contact shadow, cast shadow, floor`, and the
  background was then flattened to pure white, which takes any floor shadow with it.
- **No cloth, no hair, no mesh.** There is no physics constraint, so `CLOTH_SETTLES` skips.

## How it was made

1. **Painting.** `rig-parts comfy paint` with SDXL base 1.0 and the OpenPose control `inputs/pose.json`
   (strength 0.8, end 0.7), euler_ancestral/normal, 30 steps, cfg 6, latent 832×1216, seed 511005, upscaled to
   1664×2432 with 4x-AnimeSharp; the prompts are in `inputs/generation.json`. The background was then flattened to pure
   white by a flood from the border over neutral pixels.
2. **Layers.** See-through ran a full pass and a head pass (head box `[683, 170, 983, 470]`). The full pass put
   the whole figure in `topwear`, so the figure's pixels were re-sorted by polygon into `face`, `neck`,
   `handwear-r/-l`, `legwear`, `footwear` and `topwear`, with colour and alpha taken from the painting itself —
   the correction loop in rig-parts AUTHORING.
3. **Joints.** DWPose (no bbox detector) gave the joints; each was then moved by eye to the centre of its ball or
   seam.
4. **Proposal.** `propose --keypoints` drafted the bones and limbs. The edits: a rigid trunk (chest and pelvis,
   cut at the waist); a third arm segment, the hand; neck and head as a two-segment limb; ranges of ±45 on every
   limb joint; foot targets and iks; an idle without a hip key.
5. **Ball joints.** The painting's elbows, wrists, knees and ankles are hinge rings, so each got a painted
   wooden ball: the upper half is a limb cap image (`caps/`), the lower half fills the seam notch in the lower
   piece's layer without overwriting any painted pixel.

## Licence

The painting is a generated image: SDXL base 1.0, upscaled with 4x-AnimeSharp. The layers came from See-through
run on that painting, and the ball caps were drawn procedurally. No third-party artwork or asset is included.
The fixture is covered by this repository's licence, CC BY-NC 4.0, as the rest of the repository is
(`LICENSE`, `NOTICE.md`).
