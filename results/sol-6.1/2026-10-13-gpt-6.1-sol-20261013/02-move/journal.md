# Journal — gpt-6.1-sol (MODEL gpt-6.1-sol-20261013), 02-move, 2026-10-13

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

Run: gpt-6.1-sol-20261013, 02-move, 2026-10-13

## Entry 1
1. **Read:** Task02; parts AUTHORING §3 named-animation recipe and strands-that-trail; rig-c AUTHORING §3.5 physics and appendix defaults; task01 own config
2. **Expect:** config and wave.json written: 1.8s arm lift/wave, eight hair-link physics constraints, no idle keys on those links; no folds expected because sleeve is one rigid weighted mesh.
3. **Chose / turned down:** Bind image-right sleeve rigidly to shoulder and turn 110° then oscillate 95–115°; reject articulated elbow on a single painting because recipe reports tearing at overhead waves. Choose stiffness from documented soft recipe; remove hair keys instead of double-driving them.
4. **Happened:** Exit 0; wave and physics config written. Named numeric choices remain authored and need validation.

## Entry 2
1. **Read:** Task02 trusted pass lines and task01 grader
2. **Expect:** Grader prints 7 of 7; all idle bars green, >=150px relative rise, eight physics bones and no folded mesh.
3. **Chose / turned down:** Run grader first as full rebuild plus both idle/wave folds, rather than duplicated manual build.
4. **Happened:** Exit 0; grader 7 of 7. Full per-line output in transcript.

## Entry 3
1. **Read:** JOURNAL end; Task02 grader 7/7; own idle geometry; AUTHORING recipe limits
2. **Expect:** End notes record authored wave/physics settings and measured small relative head lag.
3. **Chose / turned down:** Record naturalness boundary and missing packaged examples instead of treating numeric rise as human acceptance.

## End notes
- **Where I guessed:** 1.8s duration and 0/110/95/115-degree shoulder wave timeline are authored choices, validated as 417.6px relative rise and zero folds. The sleeve segment endpoints were copied from own proposed shoulder/tip, but single-shoulder binding is authored to avoid the documented elbow-tearing limitation. Eight hair constraints use rotate=1; inertia=.25, strength=120, damping=.92, mass=1, mix=1 are transferred from the documented soft-region recipe and validated on this idle.
- **What I could not find:** AUTHORING references examples/demo/README.md and animations.json, but these paths are absent from the installed package. Used the documented recipe instead. No human reading of six wave frames was performed. The grader measures rise and folds, not whether the gesture reads naturally. Physics roots move relative to head by -0.05894..0.10061 degrees (lock0) and -0.05709..0.08619 (lock1_0), from own idle geometry; the slow idle creates small lag, as the recipe explains.
4. **Happened:** Exit 0; end notes written. Machine grader: 7 of 7.
