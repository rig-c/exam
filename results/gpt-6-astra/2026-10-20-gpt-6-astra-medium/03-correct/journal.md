# Journal — gpt-6-astra-medium, 03-correct, 2026-10-20

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
1. **Read:** Task 03 supplied head box; AUTHORING §4 partial config
2. **Expect:** partial config written
3. **Chose / turned down:** Use this painting head box; retain documented 0.5 scale.
4. **Happened:** partial config written, exit 0.

## Entry 2
1. **Read:** AUTHORING §4 propose-plan
2. **Expect:** exit 0, seated painting layer plan
3. **Chose / turned down:** Measure plan anew; do not reuse standing-painting assignments.
4. **Happened:** 22 rows, two hair extensions; headwear taken from full run because head crop holds only 5 rig px.

## Entry 3
1. **Read:** Entry 2 plan JSON
2. **Expect:** plan and extensions copied into config
3. **Chose / turned down:** Use measured plan unchanged before observing geometry.
4. **Happened:** config updated successfully.

## Entry 4
1. **Read:** AUTHORING §4 assemble then propose
2. **Expect:** 22 parts assembled and uncovered holes measured
3. **Chose / turned down:** Assemble new painting masks rather than copying prior bones.
4. **Happened:** 22 parts, uncovered 1726 below 3500.

## Entry 5
1. **Read:** Task 03 draft warning; AUTHORING §4 propose
2. **Expect:** proposal and LINT diagnostics identifying the correction
3. **Chose / turned down:** Read the actual diagnostic instead of assuming which part is wrong.
4. **Happened:** one LINT: opposed hairback amplitudes squeeze triangle 167 edge 37-117 to 0.064 rest length (15.572 stretch); same sign predicted 1.046. Proposal still exits 0.

## Entry 6
1. **Read:** LINT hairback_r and hairback_l squeeze; same sign then 1.046
2. **Expect:** config with eight meshes, same amplitudes magnitude, hairback_l positive like hairback_r
3. **Chose / turned down:** Correct opposed signs only; reject dropping a chain or reducing amplitude because task requires preserving deformation and travel.
4. **Happened:** hairback_l amps changed [-0.6,-1.4,-2.4] to [0.6,1.4,2.4]; all eight mesh definitions retained.

## Entry 7
1. **Read:** LINT specific same-sign remedy; task 03 requirements
2. **Expect:** six pass lines, back hair still travels at least 23 px
3. **Chose / turned down:** Grade corrected config rather than wasting a build on already diagnosed squeeze.
4. **Happened:** six of six pass, eight deforming meshes, back hair travel 45.881 px.

- **Where I guessed:** only key label and documented scale choice; correction came directly from measured LINT.
- **What I could not find:** nothing; this diagnostic precisely supplied the repair.
