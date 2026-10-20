# Journal — claude-fable-5-1, 02-move, 2026-10-20

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

---

## Entry 1

1. **Read:** `@rig-c/parts` docs/AUTHORING.md §3 *Recipe: expressions and other named animations* — `motion.animations_from` names a `rigc-motion/1` file beside the config, keys are `{bone, property, keys:[{t, v:[…]}]}`, a positive `rotate` "swings a hanging arm toward the image's right and up", demo's `wave` raises the image's right arm with `sleeve_l0` at +48; and *Strands that trail* — one `physics` constraint per link on the link bone (not `_ctl`), `rotate: 1`, inertia 0.8, strength 90 falling by 1 − 0.35·i/(n−1), damping 0.85, mass 1, mix 1. §3 `constraints` row: entries in rig-c's shape, bones resolved by name. The public page github.com/rig-c/parts `examples/demo/animations.json`: `wave` 2.21 s, sleeve_l0 0→48 (0.35 s) hold to 1.71 →0, sleeve_l1 0→20, sleeve_l2 ±10 wagging 0.52–1.54 s. rig-c AUTHORING §1.2/R6: a key may carry `ease` or `curve`; the parts loader refuses an `easings` table in the file, and `out/rig/motion.json` holds only `shut` and `open`.
   Geometry from my task-01 config: sleeve_l0 [507,250]→[536,374] (127 px), sleeve_l1 →[585,497] (132 px), sleeve_l2 →tip [648,624]. Rotating sleeve_l0 +60 and sleeve_l1 +30 (CCW, y up) puts sleeve_l2's origin about 259 rig px higher than at rest (shoulder→elbow angle −77°→−17°, elbow→wrist −68°→+22°); +48/+20 would give about 186.
2. **Expect:** `wave.json` (duration 2.2 s: sleeve_l0 0→60 at 0.4 s, hold to 1.7, →0 at 2.2; sleeve_l1 0→30 same; sleeve_l2 wags +12/−12 three times between 0.5 and 1.6 s) plus 8 physics constraints on `lock0..3` and `lock1_0..3`; `rig-parts build` exits 0, prints `[rig] animations beside the idle, from …/wave.json as written: wave`, `ANIMATIONS_DO_NOT_FOLD: PASS — 2 animation(s) … 8 physics constraint(s) left out`, a `loop physics:` line naming 8 constraints, `check: PASS; 10 of 10`. The risk I see: the shoulder of `handwear_l` folding under a 60° turn — the demo stopped at 48 and the guide says an arm raised overhead tore demo's elbow (stretch 5.327, not a fold).
3. **Chose / turned down:** the image's right arm (`sleeve_l`, as demo); linear keys, no `ease` (the only named easings are the blink's `shut`/`open`, and a `curve` needs absolute control points I would be guessing); physics on the two side locks (`lock`, `lock1_`, 4 links each — the hair that "hangs free") and not on the bang chains (they frame the face and the task says hanging strands) nor `bun` (a single bone with a tip; the guide says a single bone with no `length` takes x/y instead and I did not want to find out which rule a tipped bone falls under on this build). Turned down keying `sleeve_l0_ctl` (the guide says key the bones the idle leaves alone).
4. **Happened:** exit 0, `build: PASS`, `check: PASS; 10 of 10 bar(s) measured, 0 skipped` — but in 4m03s, three times task 01's build; nothing said the physics or the second animation would cost that (WTF-adjacent, but the result is the one expected). `[rig] animations beside the idle, from …/wave.json as written: wave`; `loop physics: 8 physics constraint(s) left out of the loop's frames, reported, not judged`; `ANIMATIONS_DO_NOT_FOLD: PASS — 2 animation(s) … its 8 physics constraint(s) left out (idle, wave): 0 folding mesh(es)`; TEXTURE_STRETCH severity 1.115 (idle, hair_front triangle 68). No fold at the shoulder at 60°.

## Entry 2

1. **Read:** TASK.md pass lines: Trails (physics on ≥2 bones), Moves (an animation ≥1 s whose best bone rises ≥150 rig px over the median bone), Moves without folding; `grade.py` `rise()` reads bone `worldY` per frame from `rigc render --geometry`.
2. **Expect:** `python3 grade.py` prints 7 PASS lines: task 01's four, `trails: 8 bone(s)`, `moves` with rise about 250 (my estimate 259 for sleeve_l2's origin; the wrist's own tip is not a bone) on `wave` 2.2 s, `moves_without_folding: []`.
3. **Chose / turned down:** grade now; turned down rendering the wave myself first — the grader's folds render is the same reading and writes the frames I can look at afterwards.
4. **Happened:** `7 of 7 line(s)`: trails 8 bones, `moves: {"animation": "wave", "duration": 2.2, "rise": 259.1, "folds": []}` — 259.1 against my 259 estimate — and `moves_without_folding: []`. As expected on the lines. But I looked at the grader's `folds_wave/wave/contact.png`: the arm goes straight out to the side with the forearm nearly horizontal, which reads as pointing, not waving. WTF?: the lines are green and the picture is not a wave — the guide's demo values (48/20) are for a figure whose arms already hang away from the body; nothing in the recipe says the elbow has to bend past the shoulder's turn for the forearm to stand up, and no bar reads it.

## Entry 3

1. **Read:** the same recipe; my own geometry: forearm angle = −68° + (sleeve_l0 key) + (sleeve_l1 key). For the forearm to stand up (about +57°) with the upper arm out at −27°: sleeve_l0 +50, sleeve_l1 +75. Wrist then sits about (185, +53) from the shoulder, so sleeve_l2's origin rises about 300 rig px.
2. **Expect:** the rebuild exits 0 with `ANIMATIONS_DO_NOT_FOLD: PASS`; the risk is a fold at the elbow of `handwear_l` under a 75° bend of a 31 px lattice — if it folds, the FAIL line names the mesh and I back the elbow down. Grader: `rise` about 300, still 7 of 7.
3. **Chose / turned down:** bend the elbow (sleeve_l1) rather than raise the whole arm overhead (the guide says an arm raised overhead tore demo's elbow, stretch 5.327); turned down leaving the passing-but-not-a-wave clip as it was.
4. **Happened:** exit 0, `ANIMATIONS_DO_NOT_FOLD: PASS — 2 animation(s) … 0 folding mesh(es)`, `check: PASS; 10 of 10`, `build: PASS` in 2m36s. No fold at the elbow. As expected.

## Entry 4

1. **Read:** TASK.md pass lines, as in entry 2.
2. **Expect:** 7 of 7, `rise` about 300 on `wave`, no folds; the contact sheet shows the forearm standing up beside the head.
3. **Chose / turned down:** grade once more; nothing else changed.
4. **Happened:** `7 of 7 line(s)`, `moves: {"animation": "wave", "duration": 2.2, "rise": 300.2, "folds": []}`. The contact sheet now shows the forearm standing up beside the head and wagging. As expected.

## At the end

- **Where I guessed:** the wave's angles (50, 75, ±12) and timing (2.2 s, hold 0.4–1.7 s) — derived from my own geometry and the demo's clip, not from any rule; the physics values are the recipe's verbatim (inertia 0.8, strength 90 tapering to 58.5, damping 0.85). Which strands count as "hanging free" (I took the two side locks and left the bangs and the bun).
- **What I could not find:** a sentence saying how a keyed arm reads — the recipe measures where a key moves the hand but says nothing about what makes it a wave rather than a point; whether a tipped single bone (`bun`) takes a `rotate` physics drive or needs `x`/`y`; why this build took 4 minutes where task 01's took 77 s.
