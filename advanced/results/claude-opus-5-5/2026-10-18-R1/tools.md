# What the tools were missing

## The eye-line head nod is not periodic, and cannot be turned off
- **I was trying to:** key the head from its eye line (the README's own example for a head) and keep a looped walk identical cycle to cycle.
- **The tool gave me:** README "What it does": "When a head chain carries the eye line (`r_eye → l_eye`) … keys a vertical `translate` nod channel … coupled in phase into … the head bone's `rotate` track (+1.6°/unit)". On a sequence whose 7 cycles are byte-identical, `head rotate` keys differed 1.38° between cycle 1 and 7 and the grader's loop row failed. No line of the retarget output mentioned the nod at all.
- **What would have helped:** a `NOD` line in the output with its range and the window it is read over, and a `--nod off` flag (or a map switch); better, read it wrapped on an `"in-place"` loop as `clean --loop` does.
- **Cost:** ~10 min (comparing keys cycle by cycle, then re-aiming the head at neck→nose). Got there, at the price of not using the eye line.

## `--stance` tolerance is in a different leg length than everything else
- **I was trying to:** plant both feet on two-foot frames without planting frames that are really lifted.
- **The tool gave me:** `--help`: "a free ankle within this many leg lengths (FEET's) …(… 0.07 is the card's)" and `FEET … leg length (median hip → ankle) r 392.8px, l 405.4px`, while LEG-SCALE's "straight length" is the 95th percentile. With 0.07, 42 of 168 lifted frames were planted.
- **What would have helped:** the STANCE line printing the tolerance in px per side ("0.07 = 27.5 / 28.4 px"), and one sentence in the README that 0.07 was measured on a dance, not a walk, where a lifted foot can be < 0.07 leg lengths up.
- **Cost:** ~10 min, one extra variant run. Got there (0.035).

## `--leg-scale`'s clamp floor hides the lift it withholds
- **I was trying to:** make the rig's lifted foot rise as far as the sequence's.
- **The tool gave me:** `LEG-SCALE … leg_r1 … 77 frame(s) under 0.8, clamped (frames 0–9, …) (0–9: asked 0.451–0.786 …)`. Clear about the scale; silent about the consequence (lift ratio 0.616).
- **What would have helped:** a figure for what the clamp did to the ankle ("ankle left 0.08 leg lengths below the asked height on 77 frames"), and guidance on how low a shin may go before the art reads wrong.
- **Cost:** ~5 min. Got there (0.45), though 0.45 squashes the shin art visibly.

## `reach: true` without a pelvis only adds error
- **I was trying to:** follow the README's trunk example (`"reach": true`).
- **The tool gave me:** "Without it, a tilted pelvis carries the chest's origin sideways" — nothing when there is no pelvis chain, and the run accepted it silently; limbs jitter 1.056× and trunk higher than needed.
- **What would have helped:** a note (or a warning line) that reach only helps when the translated bone also turns.
- **Cost:** ~2 min, found as a side effect of the head fix. Got there.

## Render does not say whether physics ran
- **I was trying to:** be sure the folds and pass-through readings were "with physics on" as the table asks.
- **The tool gave me:** `rigc render --help` documents `--environment` ("the wind and gravity the physics answers") but no line in the render output says physics was applied.
- **What would have helped:** a `physics: N constraint(s) stepped at 30 fps` line in the render output.
- **Cost:** ~2 min; I took the default as physics-on, unverified.
