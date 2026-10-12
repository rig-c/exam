# Journal — gpt-6.1-sol (MODEL gpt-6.1-sol-20261013), 01-build, 2026-10-13

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
1. **Read:** README.md Rules 2 and 3; Task 01 Given; package.json pinned dependencies.
2. **Expect:** npm ci exits 0 and installs @rig-c/parts 1.11.0 and rig-c 2.47.0.
3. **Chose / turned down:** Install pinned dependencies with npm ci; turned down newer packages because exam requires pinned versions.
4. **Happened:** npm ci exited 0; added 5 packages, audited 6, found 0 vulnerabilities.

## Entry 2
1. **Read:** JOURNAL.md entry format; README Rules 3–4; AUTHORING §4 layers-loader requirements; task inputs/seethrough.json.
2. **Expect:** A local recording helper and minimal config.json with exact recorded head box, resolution and authored rig_scale 0.5.
3. **Chose / turned down:** Create record.py to write expectations before each subprocess and raw output afterward; use supplied head box instead of proposing a different crop for already generated head layers.
4. **Happened:** record.py and the minimal config.json were written; exact supplied seethrough fields copied, rig_scale 0.5 authored from guide examples.

## Entry 3
1. **Read:** AUTHORING §4 step 6 and task supplied seethrough.json
2. **Expect:** Exit 0; JSON plan, extend_below_crop and notes printed.
3. **Chose / turned down:** Propose plan from supplied layers; reject example config because painting differs.
4. **Happened:** Exit 0. Printed plan and notes; transcript retains full JSON.

## Entry 4
1. **Read:** AUTHORING §4 step 6; Entry 3 proposed JSON (notes empty)
2. **Expect:** Config receives exact proposed plan and extend_below_crop.
3. **Chose / turned down:** Copy proposal only; no unsupported plan edits.
4. **Happened:** Exit 0; proposed plan copied.

## Entry 5
1. **Read:** AUTHORING §4 step 7 and §5 assemble
2. **Expect:** Exit 0; work/rig parts and recomposite produced; uncovered counts printed.
3. **Chose / turned down:** Assemble proposed plan, inspect numeric holes before bones.
4. **Happened:** Exit 0; assembled parts. Numeric recomposite findings recorded in transcript.

## Entry 6
1. **Read:** AUTHORING §4 step 7, assembled 2059 uncovered px below task bar
2. **Expect:** Exit 0; proposal.json and basis.json; LINT and coverage lines.
3. **Chose / turned down:** Draft from measured parts, retaining proposed rules before changing bones.
4. **Happened:** Exit 0; draft and basis written, coverage in transcript.

## Entry 7
1. **Read:** AUTHORING §4 steps 7–9, proposal 0 LINT, 31 checked/9 not checked
2. **Expect:** Full config exact proposal copied; subsequent build will evaluate bars LINT cannot.
3. **Chose / turned down:** Copy untouched proposal to establish empirical baseline; no speculative adjustments.
4. **Happened:** Exit 0; four rig sections copied.

## Entry 8
1. **Read:** AUTHORING §4 step 9; proposal clean LINT; README warns demo TIP_OVER_ROOT may fail
2. **Expect:** Build exits 0 and check PASS; uncovered remains 2059; inspect each bar for actual draft validity.
3. **Chose / turned down:** Build unchanged draft to evaluate movement instead of treating LINT as completion.
4. **Happened:** Exit 0; full build raw findings in transcript.

## Entry 9
1. **Read:** Task 01 pass lines; grade.py rebuilds and renders --folds
2. **Expect:** Grader prints 4 of 4; built/checked/whole/no folds pass.
3. **Chose / turned down:** Run trusted grader instead of accepting pasted output.
4. **Happened:** Exit 0; grader raw printed lines in transcript.

## Entry 10
1. **Read:** JOURNAL.md At the end; grader Entry 9 printed 4 of 4
2. **Expect:** End notes identify authored/ratio values and missing guarantees.
3. **Chose / turned down:** Close journal honestly after verified grader; do not claim human visual acceptance.

## End notes
- **Where I guessed:** key exam-01 is authored. rig_scale 0.5 follows AUTHORING §3 examples rather than a task mandate. All bone, mesh and motion numeric values were copied from this painting’s proposal; basis.json explicitly names its ratio guesses. No hand coordinate edits.
- **What I could not find:** No documented success guarantee for this unseen painting; LINT covers 31 of 40 bones, so nine remain unverified by its checks. The full check and folds grader passed; human contact-sheet reading is separate and was not requested/performed.
4. **Happened:** Exit 0; end notes written. Final machine grader: 4 of 4.
