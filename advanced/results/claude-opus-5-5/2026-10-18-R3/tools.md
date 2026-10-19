# What the tools were missing

## `rigc build` refuses the rig directory that `rig-pose retarget` takes
- **I was trying to:** build the retargeted motion with the same `--rig inputs/rig` I had just passed to `rig-pose retarget`.
- **The tool gave me:** `rigc compile error: cannot read …/inputs/rig: EISDIR: illegal operation on a directory, read (see rigc guide CE_COMPILE_JSON_READ_FAILED)`
- **What would have helped:** `rigc build --rig <dir>` reading `<dir>/rig.json` as retarget does, or the line saying "--rig is the rig.json file; inputs/rig/rig.json is there".
- **Cost:** a minute; got there by passing `inputs/rig/rig.json`.

## Nothing says `reach` turns the trunk off the pose's angle under a turning pelvis
- **I was trying to:** find why the jitter row failed on a plain per-frame retarget (trunk+head 1.664×, limbs 1.160×).
- **The tool gave me:** every `LAND` line within 0.002°, `POSTURE` tilt 1.000, sway 0.959. The README map bullet only says `reach` aims "from where its origin is posed — the hip moved and turned", which reads as a fix, not a cost.
- **What would have helped:** a retarget line when a `reach` trunk hangs from a bone a pelvis chain turns, e.g. "trunk reach: chest's aim departs from mid_hip→mid_shoulder by up to N° (mean |Δ²| M°/f²) because the pelvis tilt swings its origin; its children inherit it".
- **Cost:** about 10 minutes (a scratch script running grade.py's functions per bone); fixed by dropping `reach`, at the price of a 1.27× sway.

## `--stance` and `--leg-scale` use two different "leg lengths" under one name
- **I was trying to:** pick a `--stance` tolerance that plants the two-foot frames and leaves the lifted ones lifted.
- **The tool gave me:** `--help`: "a free ankle within this many leg lengths (FEET's) … 0.07 is the card's". The STANCE line: "within the tolerance 0.07 leg lengths", and two lines below, "its straight length (hip → ankle, its 95th percentile)". FEET's leg length turned out to be the median hip → ankle (608.6/613.1 px in `feet.legLength`), 15 % shorter than the 95th-percentile length (722.45).
- **What would have helped:** the STANCE line printing its unit in px and as a share of the straight length, or a `--stance` value that can be given in straight lengths.
- **Cost:** about 10 minutes and one failed run at 0.07 (all 35 lifted frames planted); 0.03, worked out by hand from the sequence, passed.

## The `CLEAN` line is one ~8,900-character line
- **I was trying to:** read the retarget's output for the lines that matter (FEET, STANCE, LEG-SCALE).
- **The tool gave me:** `CLEAN rig-pose-clean/1: legs 5, rest 7, … HOLD frames 0–81: held nose, … ; not held: …` on a single line, the whole hold record inlined.
- **What would have helped:** a one-line CLEAN summary (holds count, jitter before → after) with the per-joint record left to `--report`, or a `--quiet-clean`.
- **Cost:** a few minutes of scrolling, and it pushed me to `grep … | head`, which then hid the STANCE line I needed (journal entry 7).
