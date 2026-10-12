# Journal — gpt-6.1-sol, 01-build, 2026-10-13

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry <n>

1. **Read:** which document, section or message this step rests on (path and heading, or the message quoted).
2. **Expect:** what the step will produce, concretely — an exit code, a file, a number, a line of output.
3. **Chose / turned down:** what you are about to do, and the alternative you considered and why not.
4. **Happened:** what the step actually produced. If it differs from line 2, begin the line with
   `SURPRISE:` and say in one sentence what you now think you misread — or that nothing told you.

## At the end

- **Where I guessed:** every value you wrote without a source (a number, a name), and what you would
  have needed to read to not guess.
- **What I could not find:** questions you had that no document or message answered.

## Entry 1

1. **Read:** README.md §Rules 2 and §Layout; JOURNAL.md.
2. **Expect:** npm ci exits 0 and installs @rig-c/parts 1.11.0 and rig-c 2.47.0 into this clone; no GPU.
3. **Chose / turned down:** Use npm ci as required, rather than installing latest versions; bootstrap this run directory and journal as the place to record setup.
4. **Happened:** npm ci exited 0: added 5 packages, audited 6 packages in 1s; found 0 vulnerabilities.

## Entry 2

1. **Read:** @rig-c/parts docs/AUTHORING.md §3 coordinates and §4 layers-loader row; task01 inputs/seethrough.json.
2. **Expect:** Create a minimal config with the recorded head box and rig_scale 0.5, plus a local journal/transcript command runner.
3. **Chose / turned down:** Use the recorded crop, not a newly proposed crop that would mismatch the supplied head decomposition; choose documented example scale 0.5 and use a recorder rather than manually reconstruct output later.
4. **Happened:** Created config.json with rig_scale 0.5 and recorded head box [616,32,1132,548]; record.py writes pre-step lines and captures command, output, exit and duration.

## Entry 3

1. **Read:** parts AUTHORING §4 step6
2. **Expect:** exit0; plan/extend_below_crop/notes JSON draft
3. **Chose / turned down:** propose plan from supplied decompositions instead of example config
4. **Happened:** Plan proposal exit0 after 28.03s; produced plan, two extend_below_crop entries and notes [].

## Entry 4

1. **Read:** parts AUTHORING §4 steps6–7; plan.json notes []
2. **Expect:** config now includes proposed plan and extension; assemble exits0 and prints recomposite/uncovered figures
3. **Chose / turned down:** copy proposed plan; retain supplied scale instead of modifying assembly before measuring
4. **Happened:** assemble exit0, 22 parts; uncovered_error_px2059 within task bar4200; largest hole402px at405,1073 39x25 between shoes/legwear; no patch needed to meet stated whole bar.

## Entry 5

1. **Read:** parts AUTHORING §4 step7
2. **Expect:** proposal.json/basis.json and overlays; no LINT expected for standing figure
3. **Chose / turned down:** draft from measured assembled parts instead of choosing bones from examples
4. **Happened:** propose exit0: 21 bone entries expanding to40bones,8meshes,0LINT; basis says32mask/7ratio/1derived.9bones not checked are named in transcript; lash_l crease may blink, but no clear split row.

## Entry 6

1. **Read:** parts AUTHORING §4 steps7–9; proposal0LINT; task01 pass bars; grade.py
2. **Expect:** copy four draft sections; grader builds0,checkPASS,whole≤4200,no folding meshes; four lines pass
3. **Chose / turned down:** use standing proposal as draft against grader rather than invent correction absent a failure
4. **Happened:** grader exit0,4of4 lines PASS; check all6judgement barsPASS,uncovered2059,noidlefolds.

## At the end — answers

- **Where I guessed:** key exam01 is an authored label. rig_scale0.5 chosen from documented examples, not inferred from this painting. No other numeric value manually invented: crop/settings copied task inputs; plan and all rig/motion values are tool proposals. Ratio-derived bones are recorded by basis.json; green check/folds test them only against stated bars.
- **What I could not find:** no unanswered blocker. Package notes state9bones unverified by LINT, so0LINT is not proof those bones fit visually.
- **Three largest time costs:** grader rebuild+idlefolds39.76s (AUTHORING §4 step9 / grade.py); propose-plan28.03s (AUTHORING §4 step6); assemble26.16s (AUTHORING §4 step7).
