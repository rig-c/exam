## rig.json alone refused without motion spec
- **I was trying to:** retarget onto inputs/rig/rig.json directly.
- **The tool gave me:** "FAIL RIG_GATE_BASE: … rig.json with no motion spec is red under rigc build --profile spine" and "rig constraint "yaw": applies animation "turn", which the motion spec does not declare".
- **What would have helped:** a hint in the error: "pass --rig inputs/rig (the directory) so motion.json beside it is read".
- **Cost:** about 3 minutes; got there by switching to the directory form.

## 566 POSE_BEND_ONE_WAY frames with no summary
- **I was trying to:** find out whether the leg_l knee bend is a real fault or noise.
- **The tool gave me:** 566 lines "FAIL POSE_BEND_ONE_WAY: chain "leg_l" hinge l_knee, frame 49 … inner angle -1.6°; it bends counter-clockwise (+) at rest (1.4°)…" — one per frame.
- **What would have helped:** a one-line summary: count, worst angle, frame range, and what --bends clamp changes.
- **Cost:** about 10 minutes reading the log; got there with --bends clamp.

## --report not produced by default
- **I was trying to:** feed grade.py its report.json.
- **The tool gave me:** report-less retarget output; grade.py: "--report <report.json> … retarget --report". The first grader attempt without --report printed SKIP lines.
- **What would have helped:** retarget writing report.json next to motion.json, or a printed hint "for grade.py, add --report <file>".
- **Cost:** about 5 minutes (re-ran retarget with --report).

## Floor row SKIP with --cycle 313
- **I was trying to:** get the grader's floor row for R3.
- **The tool gave me:** "SKIP floor … 313 frames hold 1 full cycle(s) of 313: two are needed".
- **What would have helped:** grade.py --help saying that for R3 the floor and hip rows use the report's support spans only when --cycle is omitted.
- **Cost:** about 5 minutes; found the logic in grade.py row_floor and dropped --cycle.

## Overwrote the baseline report
- **I was trying to:** test a variant without losing the baseline report.
- **The tool gave me:** retarget writes --report to the path I gave, with no versioning; my variant run overwrote run/after/report.json.
- **What would have helped:** a default per-run directory or a warning when --report already exists.
- **Cost:** about 5 minutes; baseline grade already saved to run/evidence/grade_before.txt, so only the grading script needed a per-run path.

## --stance and --reduce interact on slide
- **I was trying to:** keep support and lift rows green and fix slide.
- **The tool gave me:** each flag's help on its own; no note that --reduce adds slide error after --stance planting.
- **What would have helped:** a line in retarget --help: "--reduce re-keys the planted leg after --plant-feet/--stance; check the slide row after changing it".
- **Cost:** about 15 minutes of sweeps.
