# What the tools were missing — claude-opus-5-5, 2026-10-25

## The figure's height before choosing `assemble.rig_scale`
- **I was trying to:** pick `assemble.rig_scale` for task 01 so the figure lands 1,100–1,200 rig px tall, as AUTHORING §3 (`assemble.rig_scale`) asks, before running `assemble`.
- **The tool gave me:** `rig-parts layers` prints most layers' box as the whole canvas — `legwear  body  0,0  1024,1024  1024x1024  51263` — so the table holds no figure height. The height first appears after assemble and propose, in propose's `note: mesh spacing: … H 1087 rig px the height of every part's box together`.
- **What would have helped:** `layers` printing each layer's alpha box (or one `figure: rows a..b of the run, ≈ N painting px` line), or `inputs` printing the rig_scale that puts the figure at ~1,150 rig px.
- **Cost:** a minute; I guessed 0.5 and propose confirmed it later.

## The squeeze LINT is the check's FAIL one step early, but `propose` exits 0
- **I was trying to:** know whether the draft would pass `check` (tasks 01 and 03).
- **The tool gave me:** `LINT hairback_r and hairback_l on mesh 'hair_back' squeeze it: … (max(ratio, 1/ratio) 15.572; <= 1.926544 is required, check's TEXTURE_STRETCH bar) … give both the same sign (then 1.046), or drop one chain` — and `propose --write-config` exited 0 and wrote those opposed amplitudes (`[-0.6, -1.4, -2.4]`) into the config anyway. On task 03 the build then failed with `FAIL  CHECK_TEXTURE_STRETCH: mesh "hair_back" … 15.338`.
- **What would have helped:** the proposer not writing a motion its own LINT knows fails a bar (draft both back-hair chains with the same sign, which the LINT already measures at 1.046), or `--write-config` saying on stderr `wrote motion with 1 LINT line; the build will fail TEXTURE_STRETCH`.
- **Cost:** about 2 minutes per task to read, flip and re-lint; one extra build on task 03 to confirm. Got there.

## The `drift` line on the seated painting gives no verdict
- **I was trying to:** decide whether task 03's plan order needed changing.
- **The tool gave me:** `drift: "bottomwear" refuses 21999 px of full:bottomwear … the painting is within 90 of "legwear" (21839 px at alpha >= 250, drawn behind "bottomwear")`.
- **What would have helped:** one clause saying what to do, or that nothing need be done: e.g. "the painting's own pixels are shown there; to move them with the legs, draw legwear in front of bottomwear in assemble.plan".
- **Cost:** a few minutes reading; left as is, nothing failed on it.

## Elbow and wrist signs on the mannequin
- **I was trying to:** bend each elbow and wrist the way a raised arm bends, in `dance`.
- **The tool gave me:** fixtures/mannequin/README *Signs*: "A positive `sleeve_r0` lowers the right arm and a positive `sleeve_l0` raises the left." — shoulders only.
- **What would have helped:** the same sentence for `sleeve_*1` and `hand_*` ("a negative `sleeve_r1` folds the right forearm up toward the head"), or `rig-parts` / `rigc` printing, per limb joint, which sign closes the joint.
- **Cost:** reasoned from the shoulder sign, checked by eye on the contact sheet; a few minutes.

## Straight legs at rest under the iks
- **I was trying to:** move `hip` in the dance without lifting the feet off their targets.
- **The tool gave me:** README: "Move or dip `hip` and the feet stay put." Nothing says the legs are fully straight at rest (root to ankle 488.0 px = thigh 242.7 + shin 245.3 on the right), so any rise or sideways shift of the hip leaves the ik short and the foot leaves its target.
- **What would have helped:** "both legs are straight in the setup pose: keep `hip` dipped by more than its sideways shift x 0.11 whenever it moves", or the build printing each two-bone ik's slack (`leg_r_ik: reach 488.0 of 488.0, slack 0.0 px`).
- **Cost:** computed by hand from the bone positions; ten minutes. Got there.

## Seam ghost at a knee bent inside its range
- **I was trying to:** keep the dance's joints closed on the reader `check` uses for `SEAM_OVER_MOTION`.
- **The tool gave me:** `SEAM_OVER_RANGE: PASS — 9 joint(s) bent to their declared range's ends and middle`, yet on the dance `seam "thigh_l" | "shin_l" opens on 49 of 49 frame(s) … ghost … 43 px … (37.00 × 10.00)` at a knee bend of about 30–36°, well inside `[-45, 45]`.
- **What would have helped:** `SEAM_OVER_RANGE`'s line printing each joint's figure on the `SEAM_OVER_MOTION` reader at the range ends, so a range that the motion reader opens inside is known before keying.
- **Cost:** one render and a rebuild with a shallower bounce (43 → 39 px only); left as a warning.

## `on_her_feet` drifts with the knee although the foot is a child of the shin
- **I was trying to:** keep each shin's end on its foot.
- **The tool gave me:** README: `foot_r` / `foot_l` (inherit `noRotationOrReflection`); nothing on what that does to the meeting point; the grader read `5.04 rig px … against <= 6.0` at my deepest bend.
- **What would have helped:** one sentence in the README's joint table: "the foot does not turn with the shin, so the shin's end moves off the foot by about N px per 10° of knee bend".
- **Cost:** one more build and grade with a shallower bounce (5.04 → 3.96).
