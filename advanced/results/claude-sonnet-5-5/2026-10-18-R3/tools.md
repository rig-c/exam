# What the tools were missing

## Which stance value the lifted-foot band wants
- **I was trying to:** keep the free foot lifted on frames where the dancer lifts it, while planting it otherwise.
- **The tool gave me:** `--stance <leg lengths> … (default: off; 0.07 is the card's, rig-c/pose#60)` in `rig-pose retarget --help`.
- **What would have helped:** one line saying that frames with the free ankle within the value are planted, so a value above the lifted threshold of the material you grade (0.04 here) flattens lifted feet; or a `STANCE` report line listing how many frames of the reference were lifted vs planted.
- **Cost:** about one run (3 min); got there.

## `--reduce` moves planted ankles
- **I was trying to:** cut rotation jitter.
- **The tool gave me:** `--reduce <deg>` help text; the ankle tolerance is described only as "plus the most the reduced bones above it may move it by" (README).
- **What would have helped:** a printed line at the end of the run: "ankle drift allowed: X units = Y leg lengths/frame", so I could tell before grading that 1° exceeds a 0.005 slide bar.
- **Cost:** three runs of about 2 min each (reduce is slow); did not get a pass from it, solved another way.

## Per-bone jitter, and what `reach` does to it
- **I was trying to:** find which bone made the trunk jitter 1.66x.
- **The tool gave me:** `LAND` lines (all fine) and the grader's single ratio per group.
- **What would have helped:** a `JITTER` line in retarget's output: per bone, the keyed local rotation's mean second difference against the pose pair's; and a sentence under `reach` that its aim is not the pair's angle and so adds jitter.
- **Cost:** about 10 min writing perbone.py against the grader's functions; got there.

## Which bone is the ankle for the grader
- **I was trying to:** pass `--feet` to the grader.
- **The tool gave me:** `--feet` default `foot_l,foot_r` and no description in `--help`.
- **What would have helped:** a note that the listed bone's origin must be the ankle (leg_*1 origins are knees). I passed leg_r1,leg_l1 first and read a false 0.17 floor error.
- **Cost:** about 3 min; got there.

## Relative paths and timeouts in the pipeline
- **I was trying to:** run retarget, build, render, grade in one go.
- **The tool gave me:** `rig-pose retarget` re-renders folds internally when `--reduce` is on; runs took over 120 s with no progress line.
- **What would have helped:** a progress line (frame x of 313 / "rigc render --folds" started).
- **Cost:** one backgrounded command and a wait of about 5 min total.
