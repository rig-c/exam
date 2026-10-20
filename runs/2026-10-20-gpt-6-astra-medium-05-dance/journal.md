# Journal — gpt-6-astra-medium, 05-dance, 2026-10-20

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
1. **Read:** Task 05 joint heights; parts AUTHORING §3 bones, meshes exponent, constraints and scene target; core AUTHORING §3.5 and A47 two-bone IK; task04 config.
2. **Expect:** author script for fixed ankle IK, sharper arm weighting at corrected joints, and 4-second beat loop retaining chest physics.
3. **Chose / turned down:** add two two-link legs targeting root-level feet, not slide rigid legwear with hip. Grid22 exponent6 arms to concentrate bends at joints; grid38 legs for budget. One-second repeated phrase, bob twice per second, alternated arms.
4. **Happened:** dance_setup.py written; no config mutation yet.

## Entry 2
1. **Read:** Entry 1 design and exact source in transcript
2. **Expect:** config.json and animations.json with fixed feet IK and periodic dance
3. **Chose / turned down:** Run recorded authoring script; retain task04 soft region and hop.
4. **Happened:** config and dance written, 2 chains, 2 IK and 9 tracks.

## Entry 3
1. **Read:** Task05 pass lines; first authored dance
2. **Expect:** build and 14 lines pass, though joint weighting and ankle residual need measurement
3. **Chose / turned down:** Measure the complete clip before tuning; no silent reduction of motion.
4. **Happened:** WTF?: Expected a viable first dance, but legwear folds on triangles 63,78,79; only 4/14 measured lines pass. Two nearly straight legs bend towards each other under the downward bob; the lattice between their inner edges inverts. Budget is 956, idle stays green. Full grader withholds seven measurements when the physics-free build folds.

## Entry 4
1. **Read:** grade.log fold box and triangle weights; dance contact sheet; IK bendPositive
2. **Expect:** outward screen-right knee keeps thighs from closing the inner leg lattice
3. **Chose / turned down:** Move leg_l knee from x475 to x490 and set its IK bendPositive false; preserve dance amplitudes and left leg.
4. **Happened:** knee moved and bend sign changed as planned.

## Entry 5
1. **Read:** Corrected leg bend direction
2. **Expect:** 14 pass lines; no inter-leg inversion
3. **Chose / turned down:** Rerun official grader after geometric correction.
4. **Happened:** all 14 pass; 956 triangles, hands 433.4/437.5 px, trunk minimum 40 px, arms 4 degrees, feet 2.35 px, soft 7.196 px, loop exact, time score 1.0. Contact sheet inspected: alternating arms and planted squat/sway. The grader counted zero surprises because my earlier line lacked the bold Happened label; text itself was recorded at the time.

## Entry 6
1. **Read:** grade.py lines313-315 parses 4. **Happened:** WTF?:; prior failed build diagnostic and journal; task requires tools.md.
2. **Expect:** preserve surprise text while correcting its label; tools.md records one actual tool omission; journals gain proper model/task titles.
3. **Chose / turned down:** fix the formatting transparently, not pretend there was no surprise. No padding of tool feedback.
4. **Happened:** preserved surprise text with parseable label, titles filled, tools.md written with one issue.

- **Where I guessed:** leg joint positions visually estimated; arm elbow/wrist y from task ratios, x from painting and prior chain. Grid22/38, r4, exponent6 and all dance amplitudes/phases are authored choices. Outward knee correction follows the observed inversion.
- **What I could not find:** fold messages do not report driving bone weights; extracted them from rig.json. No token usage API with fresh/cached/output session totals was available, so usage.json omitted.

## Entry 7
1. **Read:** Final input unchanged; journal surprise label repaired
2. **Expect:** 14 pass lines and one correctly counted WTF entry
3. **Chose / turned down:** One final grader run to verify the submitted record agrees with its printed surprise count.
4. **Happened:** final grader again passed all 14 lines and counted 1 WTF entry.
