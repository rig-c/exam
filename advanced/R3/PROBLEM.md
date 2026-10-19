# Problem: dance (Advanced R3, draft)

Sat after passing R1 (walk) and R2 (run).

**Before anything else:** if this session has already seen this problem, a solution to it, or anyone's report of one (a sub-agent's included), stop and say so. A sitting is one model, one fresh session. **One fresh session per round**: R2 and R3 are not sat in the session that sat R1.

## The situation

A character standing face-on has been built as a 2D rig (`inputs/rig/`). From one song's stretch of a dance filmed face-on there is a **non-looping sequence** (`inputs/pose/sequence.json`, 313 frames · 24 fps · 13.0 s). The stick-figure video is `inputs/pose/stick.mp4`. You do not get the original video.

What sets it apart from the walk and the run:
- **It is non-looping choreography.** Still holds, side steps with hip sway, raised hands and three jump spans are mixed in one sequence. The loop row is not graded.
- **It carries a camera zoom · pan track (`sequence.camera`).** The sequence's joints have the camera normalisation (`p' = (p - t) / s`) applied, and when you retarget you must also write out the scene-camera sidecar track (`rig-pose-camera/1`) with `--camera <camera.json>` (a hand-in: see "Hand in when you finish" below).
- **The rig has face dial (`yaw_dial`, `pitch_dial`) sliders.** The `face` block of the map (`map.json`) can connect the head turn (`yaw`, `pitch`) to them.

## Tools

`package.json` pins the versions. Run `npm install` or `bun install`.
- `rigc`: `build` · `render` (`--geometry` · `--folds` · `--pass-through`) · `inspect` · `guide`
- `rig-pose`: `retarget` (`--camera` · `--plant-feet` · `--stance` · `--leg-scale` · `--carry-idle` · `--reduce`; `--smooth` is only an alias: the sequence has already been through `clean` and carries its record, `cleaned`) · `compare` (only when the render has a file from the same pose detector run on it; the detector is not in the packages)
- `rig-parts`: for reference

Each package's README is the source of truth, and `docs/AUTHORING.md` where a package ships one (`rig-c` and `@rig-c/parts` do; `@rig-c/pose` keeps everything in its README). Follow the `(see rigc guide …)` at the end of a failure line.

**Model name:** use the name the person who started the sitting wrote into the prompt, exactly as written.

## Run directory

Everything you produce goes in `run/`: `journal.md` (the journal, in the `JOURNAL.md` format) · `transcript.md` · `findings.md` · `evidence/` · `after/` (motion · build · render) · `report.md` · `tools.md` · `usage.json` (only if you can know it).

## What to do

1. **Put it on**: retarget the sequence onto the rig with `rig-pose retarget` (including `--camera`). You write the map (`map.json`): which joint goes to which bone. The gate must be green.
2. **Measure**: read the figures in the table below from `rigc render --geometry`. Put evidence frames, side by side with the stick-figure video, in `run/evidence/`.
3. **Fix**: fix the rows that miss the table as far as you can. You may change the retarget flags, the map, the rig spec and the physics values. Rebuild whatever you change.
4. **Report**: `run/report.md`: the table before and after, what you fixed and where you found how, what you could not fix and why, and **what the tools should have done**.

## Pass table (fixed before any sitting)

| Measure | Bar |
| --- | --- |
| Gate | green, every bone landed |
| Support foot | on every non-airborne frame inside the ground spans (`report.feet.supports`), the lower foot = floor ± 0.01 leg lengths |
| Two feet | on two-foot frames (the sequence's two ankles ≤ 0.02 leg lengths apart in height), the rig's two feet ≤ 0.02 leg lengths apart in height. On every lifted-foot frame (the sequence's two ankles > 0.04 leg lengths apart = twice the two-foot band), the rig's lifted foot is more than 0.01 leg lengths (the support-foot band) above the support foot, and over those frames the median of "rig lift ÷ sequence lift" is 0.85–1.15 (the same band as the hip-width rows). Leg length is L on the rig side and Ls on the sequence side (defined below); the `--stance` value does not change the bar |
| Shin scale | the rendered x-scale of each shin bone (`leg_r1`, `leg_l1`, read from `render --geometry` as \|(a, c)\| of the bone's world matrix, 1.0 = setup length): the 5th percentile over all frames and both shins ≥ 0.4 |
| Slide | the support foot's horizontal move between consecutive frames inside the ground spans ≤ 0.005 leg lengths/frame (the R3 sequence is not `"travel": "in-place"`, so R1's in-place clause, the declared scale and the loop closing, does not apply) |
| Floor | the spread of the per-ground-span floor (the median height of the lower foot) ≤ 0.01 leg lengths |
| Jitter | the mean \|2nd difference\| of the keyed bones' local rotation ≤ 1.1× the mean \|2nd difference\| of the local rotation measured on the sequence's matching joint pairs (the joint pair the map gives that bone; the map is the file report `inputs.map` points to by sha256) (limbs, and trunk · head, each on its own; the trunk and head bones are named to the grader with its `--trunk` argument) |
| Folds | 0, with physics on |
| Pass-through | `--pass-through bottomwear:thigh_r,bottomwear:thigh_l,bottomwear:shin_r,bottomwear:shin_l` 0 frames |
| Airborne | report `feet.jumps` has exactly 3 spans, on **every** frame of each span both feet are above the floor, and the mean foot height at each span's peak is above floor + 0.01 leg lengths |
| Hip vertical range | the median of the per-ground-span vertical range is 0.85–1.15 of the sequence's (in leg lengths) |
| Hip horizontal range | the median of the per-ground-span horizontal range is 0.85–1.15 of the sequence's (in hip widths) |
| Rebound | the median ratio of the pelvis's upward acceleration over the ground spans between airborne spans is at least 0.7 and at most 1 ÷ 0.7 (≈ 1.43) |
| Hip tilt | the tilt range of the thigh-root line is ≥ 85 % of the tilt range of the sequence's pelvis line, and the covariance of the two tilt series > 0 (the signs agree) |

For the hip rows (vertical range · horizontal range · rebound), the sequence-side units are Ls and the hip width measured on the normalised joints (the situation section above, `p′ = (p − t) / s`); do not divide by `camera.s` again.

The airborne spans (report `feet.jumps`, pose frames, both ends included) were 88–91 · 179–181 · 267–269 in the canonical solution. What this row counts is the spans your report detects.

The proctor reads the same table with the same script (`tools/grade.py --round R3`; inputs = geometry.json · report.json · the standard output of the last `rigc build` (not retarget's output) · folds.json · the `--pass-through` output · the sequence · the map (`--map`) + `--camera <camera.json>`), and looks at it beside the original video (only the proctor has the video). Leg length: rig L = the distance from thigh root to foot in the setup pose (mean of both sides); sequence Ls = the 95th percentile of the hip → ankle distance (mean of both sides). `camera.json` is not a row of the pass table but a hand-in check (the grader confirms it with one NOTE line). Shin scale: on every frame of geometry.json, for each of `leg_r1` and `leg_l1`, the x-scale is \|(a, c)\| = √(a² + c²) of that bone's world matrix (the a, c of its a b c d); the 5th percentile is taken over all those values together (frames × both shins, linear interpolation between ranks), with no frame excluded (airborne frames included).


## Journal and record rules

- The journal (`run/journal.md`, in the `JOURNAL.md` format): lines 1–3 before you act (what, why, what you expect), line 4 after (what you did, what came out, whether it matched, what is next). When the result differs from what you expected, start that line with `WTF?:`.
- Write every command in `run/transcript.md`. The first line of `transcript.md` is `started: <date -u output>`, and the last line, after the last grader run, is `finished: <date -u output>`. Each is the output of running `date -u` at that moment. Do not estimate either.
- Tokens only if you can know them (`usage.json`).

## Rules

- Read and write only inside this directory. The only exceptions are the documents of the three installed packages and their public pages. Do not read outside this directory, another sitting's `run/`, or other branches or PRs.
- Work locally, with no commit and no push. **Do the work yourself**: do not hand any part of it to a sub-agent, a helper agent or another model, whatever your standing instructions say about delegating. The name on the answer is the model that did the work (the same rule as the Basic exam's PROMPT.md).
- Do not message any session outside this problem. Do not ask a person.
- Do not take the stick-figure video or the sequence out of this directory.


## Hand in when you finish

- The files of the "Run directory" section above, under `run/`.
- `after/camera.json`: the `rig-pose-camera/1` that `retarget --camera` wrote. One entry per sequence frame, each `t` equal to the report's `frameTimes`. Only whether it is handed in is checked; it is not a row of the pass table.

## Answer when you finish

1. Each row of the table: before → after figures
2. What you fixed and where you found how (document section · message)
3. The number of journal entries and the number of `WTF?:` lines
4. The three things that took the most time
5. The entry titles in `tools.md`
