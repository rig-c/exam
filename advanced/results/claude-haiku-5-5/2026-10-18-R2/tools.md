## rigc build without the right flags printed a long help text and exit 2
- **I was trying to:** build the retargeted motion into a skeleton (`rigc build --rig … --motion …`).
- **The tool gave me:** exit 2 and a page of text about `rigc pose`, `chainfit`, `skills install` and `cuts.json`; the only line about the arguments was "a cuts.json is { … }". The actual error (`--out <dir>` is needed for a plain build) was not on the screen.
- **What would have helped:** one line naming the missing flag, e.g. "build needs --out <dir> (or --cut)".
- **Cost:** about 3 minutes; I got there by reading `rigc build --help`.

## The PROBLEM says the R1 table is written out again, but it is not
- **I was trying to:** know the full R1 bars (leg length, jitter, pass-through) before retargeting.
- **The tool gave me:** PROBLEM.md line 37: "Every row of R1 (the R1 table is written out again here …) +", followed only by the R2 table.
- **What would have helped:** the R1 rows printed in the file, or a pointer to where they are.
- **Cost:** about 5 minutes reading `grade.py` to recover the R1 bars from the code.

## The retarget help gives tuning values without saying which ones apply to this clip
- **I was trying to:** pick `--stance`, `--flip`, `--short`, `--leg-scale` for a run.
- **The tool gave me:** the help strings "90 is the measured setting", "0.35 is the measured setting", "0.07 is the card's", "0.8,1.05 is the card's range" — without the clip or the test they came from.
- **What would have helped:** a short table of which setting was measured on which clip, and what it changes.
- **Cost:** about 10 minutes reading the 124 KB pose README; I still took the values on trust.

## The grader gives a figure but not the mechanism behind a miss
- **I was trying to:** understand why hip vertical (1.35–1.46) and hip horizontal (1.71) are high.
- **The tool gave me:** a single ratio with the rig and sequence ranges (`rig/sequence 1.349 (rig 0.1286, sequence 0.0954 leg lengths …)`).
- **What would have helped:** a per-frame or per-span breakdown of the rig's hip against the sequence's hip, so the cause (translate scale, plant-feet shift, or leg scale) can be seen.
- **Cost:** not resolved; I did not find a tool that splits the hip excursion by source.

## No video reference in my package
- **I was trying to:** put the evidence frames side by side with the stick-figure video.
- **The tool gave me:** PROBLEM.md says "You do not get the video." Only the render contact sheet can be compared.
- **What would have helped:** a version of the stick video I could compare frames against, or a note that the comparison is for the proctor only.
- **Cost:** the evidence file is one-sided; not resolved.
