# Journal — gpt-6-astra-medium, 01-build, 2026-10-20

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry <n>

1. **Read:** which document, section or message this step rests on (path and heading, or the message quoted).
2. **Expect:** what the step will produce, concretely — an exit code, a file, a number, a line of output.
3. **Chose / turned down:** what you are about to do, and the alternative you considered and why not.
4. **Happened:** what the step actually produced. If it differs from line 2, begin the line with
   `WTF?:` and say in one sentence what you now think you misread — or that nothing told you. Say it
   the way it landed. Politeness is not graded here; a line that understates the surprise hides it.

## At the end

- **Where I guessed:** every value you wrote without a source (a number, a name), and what you would
  have needed to read to not guess.
- **What I could not find:** questions you had that no document or message answered.

## Entry 1
1. **Read:** AUTHORING §3 and §4; inputs/seethrough.json.
2. **Expect:** create a partial config at scale 0.5 and a command recorder; no rig yet.
3. **Chose / turned down:** use the supplied head box and documented example scale; no guessed bones. A recorder will preserve pre-step entries and command output.
4. **Happened:** created config.json and record.py as expected.

## Entry 2
1. **Read:** AUTHORING §4 step 6
2. **Expect:** exit 0; proposed assembly plan on stdout
3. **Chose / turned down:** Ask tool for plan instead of choosing layers blindly.
4. **Happened:** exit 0, 22 plan rows and two hair extensions; nose omission explicitly explained.

## Entry 3
1. **Read:** proposed plan from entry 2.
2. **Expect:** config gains exactly plan and extend_below_crop.
3. **Chose / turned down:** retain proposal; no reason yet to override its layers.
4. **Happened:** copied both fields.

## Entry 4
1. **Read:** AUTHORING §4 step 7
2. **Expect:** exit 0; parts and measured uncovered holes
3. **Chose / turned down:** Assemble before proposing bones; geometry needs actual masks.
4. **Happened:** exit 0, 22 parts; uncovered 2059, below task ceiling 4200.

## Entry 5
1. **Read:** AUTHORING §4 step 8; assembled masks
2. **Expect:** exit 0; proposal.json and basis.json with bone coverage
3. **Chose / turned down:** Use mask-derived draft before judging whether corrections are needed.
4. **Happened:** exit 0, proposal and basis written, zero LINT; 31 bones checked clean, 9 not checked.

## Entry 6
1. **Read:** proposal.json and zero LINT result; AUTHORING §4.
2. **Expect:** complete config with proposed bones, meshes, regions and motion.
3. **Chose / turned down:** preserve draft for first build; do not correct clean geometry without evidence.
4. **Happened:** copied four proposal fields into config.

## Entry 7
1. **Read:** Task 01 pass lines and README grader
2. **Expect:** built, checked, whole and no folds; proposal has no LINT and uncovered 2059
3. **Chose / turned down:** Use official grader, which builds and measures, instead of duplicating its build.
4. **Happened:** all four pass lines passed; grader clock absent because finished is recorded after the last grader, as instructed.

- **Where I guessed:** key exam is an authored label; scale 0.5 is the documented example choice. No manual geometry.
- **What I could not find:** nothing blocking task 01.
