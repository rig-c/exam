# Problem: run (Advanced R2, draft)

Sat after passing R1 (walk).

**Before anything else:** if this session has already seen this problem, a solution to it, or anyone's report of one (a sub-agent's included), stop and say so. A sitting is one model, one fresh session. **One fresh session per round**: R2 and R3 are not sat in the session that sat R1.

## The situation

The same rig as R1 (`inputs/rig/`). The same person, filmed by the same camera, gives **a sequence made by repeating one running cycle** (`inputs/pose/sequence.json`, 200 frames · 30 fps · 6.7 s: right foot down → left foot down → right foot down is one cycle, 20 frames, ×10). The stick-figure video is `inputs/pose/stick.mp4`. You do not get the video.

What sets a run apart from a walk: every stride has an **airborne span** with both feet off the floor, the pelvis sinks on landing and springs back, and the pelvis tilts left and right in turn. The rig is 2D and face-on, so the knee cannot bend toward the camera; the leg length (`--leg-scale`) does that job.

## Tools

`package.json` pins the versions. Run `npm install` or `bun install`.
- `rigc`: `build` · `render` (`--geometry` · `--folds` · `--pass-through`) · `inspect` · `guide`
- `rig-pose`: `retarget` (`--plant-feet` · `--stance` · `--leg-scale` · `--carry-idle` · `--reduce`; `--smooth` is only an alias: the sequence has already been through `clean` and carries its record, `cleaned`) · `compare` (only when the render has a file from the same pose detector run on it; the detector is not in the packages)
- `rig-parts`: for reference

Each package's README is the source of truth, and `docs/AUTHORING.md` where a package ships one (`rig-c` and `@rig-c/parts` do; `@rig-c/pose` keeps everything in its README). Follow the `(see rigc guide …)` at the end of a failure line.

**Model name:** use the name the person who started the sitting wrote into the prompt, exactly as written.

## Run directory

Everything you produce goes in `run/`: `journal.md` (the journal, in the `JOURNAL.md` format) · `transcript.md` · `findings.md` · `evidence/` · `after/` (motion · build · render) · `report.md` · `tools.md` · `usage.json` (only if you can know it).

## What to do

1. **Put it on**: retarget the sequence onto the rig with `rig-pose retarget`. You write the map (`map.json`): which joint goes to which bone. The gate must be green.
2. **Measure**: read the figures in the table below from `rigc render --geometry`. Put evidence frames, side by side with the stick-figure video, in `run/evidence/`.
3. **Fix**: fix the rows that miss the table as far as you can. You may change the retarget flags, the map, the rig spec and the physics values. Rebuild whatever you change.
4. **Report**: `run/report.md`: the table before and after, what you fixed and where you found how, what you could not fix and why, and **what the tools should have done**.

## Pass table (fixed before any sitting)

Every row of R1 plus the R2 rows: the table below lists R1's ten rows first (Gate … Loop) and R2's five after them; leg length L · Ls is defined as in R1, in the grading paragraph below.

| Measure | Bar |
| --- | --- |
| Gate | green, every bone landed |
| Support foot | on every frame that is not airborne, the lower foot = floor ± 0.01 leg lengths |
| Two feet | on two-foot frames (the sequence's two ankles ≤ 0.02 leg lengths apart in height), the rig's two feet ≤ 0.02 leg lengths apart in height. On every lifted-foot frame (the sequence's two ankles > 0.04 leg lengths apart = twice the two-foot band), the rig's lifted foot is more than 0.01 leg lengths (the support-foot band) above the support foot, and over those frames the median of "rig lift ÷ sequence lift" is 0.85–1.15 (the same band as the hip-width rows). Leg length is L on the rig side and Ls on the sequence side (defined below); the `--stance` value does not change the bar |
| Shin scale | the rendered x-scale of each shin bone (`leg_r1`, `leg_l1`, read from `render --geometry` as \|(a, c)\| of the bone's world matrix, 1.0 = setup length): the 5th percentile over all frames and both shins ≥ 0.4 |
| Slide | the support foot's horizontal move ≤ 0.005 leg lengths/frame (if the sequence is `"travel": "in-place"`: the difference between the support foot's horizontal move and "the sequence's supporting ankle's horizontal move × the scale the report declares (`scale`, the SCALE line)", after removing the per-frame loop-closing move that report `feet.closure` records, ≤ 0.005 leg lengths/frame) |
| Floor | the spread of the per-cycle floor (the median height of the lower foot) ≤ 0.01 leg lengths |
| Jitter | the mean \|2nd difference\| of the keyed bones' local rotation (read from the render geometry) ≤ 1.1× the mean \|2nd difference\| of the local rotation measured on the sequence's matching joint pairs (the joint pair the map gives that bone; the map is the file report `inputs.map` points to by sha256) (limbs, and trunk · head, each on its own; the trunk and head bones are named to the grader with its `--trunk` argument) |
| Folds | 0, with physics on |
| Pass-through | `--pass-through bottomwear:thigh_r,bottomwear:thigh_l` 0 frames |
| Loop | between the first cycle and the last, the keyed bones' world angles differ by ≤ 1°, and the world positions of the `--hip` bone and both feet differ by ≤ 0.01 leg lengths (physics bones excluded: they start from the rest pose) |
| Airborne | report `feet.jumps` has exactly two spans per cycle, each span lies within ± 1 frame of the airborne frames written on this sheet (read by the proctor from the original video before any sitting), and on each of those frames both feet are above floor + 0.01 leg lengths |
| Hip vertical range | 0.85–1.15 of the sequence's (in leg lengths) |
| Hip horizontal range | 0.85–1.15 (in hip widths) |
| Rebound | the ratio by which the pelvis rises again after landing is at least 0.7 and at most 1 ÷ 0.7 (≈ 1.43) |
| Hip tilt | the tilt range of the thigh-root line is ≥ 85 % of the tilt range of the sequence's pelvis line, and the covariance of the two tilt series > 0 (the signs agree) |

Airborne frames (per cycle, pose frames, both ends included): **4–9 · 14–19**, read by the proctor from the original video before any sitting (the same values are in `R2_AIR_REFERENCE` in `tools/grade.py`). A cycle is 20 frames and repeats 10 times over the 200 frames of the sequence, so in sequence frames cycle k (counting from 0) has 4+20k–9+20k · 14+20k–19+20k.

Jitter and loop are already in the R1 rows of the table above (the same rows, not counted twice): jitter has the same ratio cap as R1 (≤ 1.1× the sequence); a run gets no extra allowance. Loop keeps both of R1's clauses, angle and position, as they are.

The proctor reads the same table with the same script (`tools/grade.py --round R2`; the inputs are the same as R1: geometry.json · report.json · the standard output of the last `rigc build` · folds.json · the `--pass-through` output · the sequence · the map), and looks at it beside the original video (only the proctor has the video). Pelvis = the midpoint of the thigh roots (not the hip bone's origin: when the hip tilts, the origin wobbles); rig leg length L = the distance from thigh root to foot in the setup pose (mean of both sides); sequence leg length Ls = the 95th percentile of the hip→ankle length in pixels (mean of both sides). Grounded frames = the frames outside the jump spans (report `feet.jumps`). Shin scale: on every frame of geometry.json, for each of `leg_r1` and `leg_l1`, the x-scale is \|(a, c)\| = √(a² + c²) of that bone's world matrix (the a, c of its a b c d); the 5th percentile is taken over all those values together (frames × both shins, linear interpolation between ranks), with no frame excluded (airborne frames included).


## Journal and record rules

- The journal (`run/journal.md`, in the `JOURNAL.md` format): lines 1–3 before you act (what, why, what you expect), line 4 after (what you did, what came out, whether it matched, what is next). When the result differs from what you expected, start that line with `WTF?:`.
- Write every command in `run/transcript.md`. The first line of `transcript.md` is `started: <date -u output>`, and the last line, after the last grader run, is `finished: <date -u output>`. Each is the output of running `date -u` at that moment. Do not estimate either.
- Tokens only if you can know them (`usage.json`).

## Rules

- Read and write only inside this directory. The only exceptions are the documents of the three installed packages and their public pages. Do not read outside this directory, another sitting's `run/`, or other branches or PRs.
- Work locally, with no commit and no push. **Do the work yourself**: do not hand any part of it to a sub-agent, a helper agent or another model, whatever your standing instructions say about delegating. The name on the answer is the model that did the work (the same rule as the Basic exam's PROMPT.md).
- Do not message any session outside this problem. Do not ask a person.
- Do not take the stick-figure video or the sequence out of this directory.

## Answer when you finish

1. Each row of the table: before → after figures
2. What you fixed and where you found how (document section · message)
3. The number of journal entries and the number of `WTF?:` lines
4. The three things that took the most time
5. The entry titles in `tools.md`
