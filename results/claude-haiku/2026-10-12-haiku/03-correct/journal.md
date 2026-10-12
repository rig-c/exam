# Journal — haiku, 03-correct, 2026-10-12

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

1. **Read:** README.md "Rules" 2–3 and "Submitting"; tasks/03-correct/TASK.md "Do" and "Pass lines"; package.json pins `@rig-c/parts` 1.11.0 and `rig-c` 2.47.0; inputs/generation.json and pose_seated.json (crossed ankles, one hand on cheek, other at side, seated, feet ~y 1080).
2. **Expect:** `npm ci` installs the two pinned packages into node_modules/ with no error; I should then find `rig-parts` and `rigc` bins and their `--help` and docs inside node_modules/.
3. **Chose / turned down:** run `npm ci` (exact lock, pinned versions) rather than `npm install` (could move the lock). Turned down reading grade.py's source; I will use only its printed output.
4. **Happened:** `npm ci` exit 0, "added 5 packages", 0 vulnerabilities. Nothing surprising.

## Entry 2

1. **Read:** AUTHORING.md §4 (the loader table: `layers` row needs `key`, `seethrough`, `assemble.rig_scale`) and §3 `seethrough.head_box`; inputs/seethrough.json (resolution 1024, head_box [538,158,1100,720]); `rig-parts propose --head-box` printed the same box with "no shift", so the given head layers match the box I already have.
2. **Expect:** a minimal config.json with `key`, `seethrough` (the seethrough.json values) and `assemble.rig_scale` 0.5 is accepted by the `assemble --propose-plan` loader (it needs only those), and the plan prints in step 3.
3. **Chose / turned down:** write config.json with only the fields the step reads, per §4 ("config holds only what the step reads"). Turned down copying `examples/*` configs: the task says this painting's config must be my own, and the example configs do not fit this figure.
4. **Happened:** config.json written (the three fields only). Nothing surprising yet; the file is a pre-step plan line filled after the step.

## Entry 3

1. **Read:** `assemble --propose-plan` output (plan.txt in scratchpad, exit 0): 21 planned parts, `extend_below_crop` for hair_front and hair_back, one note on `headwear` (kept full-run). AUTHORING §4 step 6 says paste `plan` and `extend_below_crop` into `config.assemble`, and read the notes.
2. **Expect:** after pasting, `assemble --out work` builds parts; the uncovered-hole lines will show whether the plan leaves painting unheld (the full-run layers the plan does not take: objects, wings, tail, neckwear, earwear, eyewear, nose are not planned).
3. **Chose / turned down:** paste the proposal verbatim (not hand-edited) for step 7; turned down adding `assemble.patches` before I see a hole.
4. **Happened:** exit 0, 22 parts, `uncovered_error_px` line reads 1726 (444 holes). The surprise is in the table, not the exit code: `bottomwear` shows `drift=21999` and `unproj=27513` with `src=38750/60740`, far above every other part. I had not expected a drift count that large on any part.


## Entry 4

1. **Read:** `assemble` stdout (assemble1.txt): `bottomwear` row `drift=21999 seam=22338`, and `fringe pushed back: "bottomwear" 393 px` at §5 *The fringe push-back*; AUTHORING §4 step 7 says look at `recomposite_error_rig.png` and then run `propose --parts`.
2. **Expect:** `propose` writes `work/proposal.json`, `work/basis.json` and `work/render/landmarks.png`, and prints a LINT line for the seated figure (hip not below chest, sleeves from shoulders) because the standing-figure ratios do not fit the pose.
3. **Chose / turned down:** run `propose` now (step 7) rather than edit the parts by hand; turned down `pose_seated.json` as `--keypoints`: its points are the 832x1216 control skeleton (the latent size, not the 1664x2432 painting), and §3 says a control skeleton is not where the joints ended up.
4. **Happened:** exit 0, "wrote proposal.json (22 bone entries, 8 meshes)". Coverage: 45 bones, 37 checked and clean, 0 LINT. The picture (landmarks.png, which I read directly) shows a seated figure with the hip at the waist and the chest/neck chain fine; the skirt chains are the bottom of the skirt, not the legs. My expectation of a LINT line for the seated pose was wrong: the hip rule places it, LINT found nothing.


## Entry 5

1. **Read:** AUTHORING §4 step 8 (copy `bones`, `meshes`, `regions`, `motion` from the proposal into the config; then `propose --from-config` for LINT); the proposal's `notes` (legwear got "no rule -> region on hip"); the landmarks picture, read with the Read tool.
2. **Expect:** the config with the draft pasted is loadable, `propose --from-config` prints 0 LINT lines and exits 0 (LINT is about bones vs art, not the check).
3. **Chose / turned down:** paste the draft unedited first, so the build shows what the tool proposes (the task says it does not pass as proposed; I need the failure before I correct anything). Turned down editing the bones by eye before the first build.
4. **Happened:** config.json now holds bones, meshes, regions, motion from the draft. `propose --from-config` exit 0, 0 LINT lines, 37 checked and clean, 8 not checked. Matches the expectation.


## Entry 6

1. **Read:** AUTHORING §4 step 9 (`build` = assemble, rig, check in one process; "every FAIL line names what has to change"); README "The loop, for an agent".
2. **Expect:** build stops at a FAIL in the check stage (not at the assemble stage, which passed); the FAIL names the bar and the value. I expect at least one of the seated-figure bars (TIP_OVER_ROOT for the skirt or a seam bar on bottomwear) to be red.
3. **Chose / turned down:** run the unedited draft build (the required first look). Turned down `--idle-keys direct` and `--loop` for now, since they add stages I cannot yet read.
4. **Happened:** exit 1 at check, 16 s. Assemble passed (uncovered error px 1726). rig: rigc build exit 0. check: 8 of 9 bars PASS-or-REPORTED, one FAIL: `CHECK_TEXTURE_STRETCH: mesh "hair_back" triangle 167 (vertices 115 37 117), edge 37-117, idle frame 22 ... 0.065 times its rest length (max(ratio, 1/ratio) 15.338); <= 1.926544`. The other mesh stretches are all under 1.13. I expected a TIP_OVER_ROOT or seam red; the only red is the back-hair mesh, which I had not expected.


## Entry 7

1. **Read:** the FAIL line (names mesh, triangle, edge, frame, the ratio and the bar); the `CHECK_TEXTURE_STRETCH` message says "the bones this mesh is weighted to move apart (amplitudes too large down a chain), or a vertex blends bones that move against each other"; AUTHORING §3 `meshes.<part>` (`segments`, `rule`, `influences`) and §7 TEXTURE_STRETCH (to read).
2. **Expect:** the squeeze is on the back-hair mesh, where the left and right chains (hairback_r, hairback_l, opposite-sign amplitudes) are weighted into the same triangles. I expect either the amplitude or the weighting to be the cause; I will read the bar text in §7 before choosing.
3. **Chose / turned down:** read §7 and the mesh_report/picture before editing (no edit yet). Turned down deleting the hair_back mesh (that would fail the Kept line); turned down lowering all amplitudes (would change other bars).
4. **Happened:** I read the bar text and §3 *The weight cut* and §7 TEXTURE_STRETCH (the doc's fold cases are weight steps at 2 px edges, not a 30 px lattice edge). `rigc render --folds` over the draft's idle (scratch dir, not the checkout) says "0 of 8 mesh(es) fold", so the Does-not-fold line already holds on the draft. Nothing I read so far names the cause on this lattice.


## Entry 8

1. **Read:** `rig.json` hair_back weights (out/rig): vertex 37 is 0.92 `hairback_r2` / 0.08 `hairback_l2`, vertices 115 and 117 are `hairback_l2`-dominant. The track list in config.json: `hairback_r` amps [0.6, 1.4, 2.4] and `hairback_l` amps [-0.6, -1.4, -2.4], same phase and lag. The bar message: "a vertex blends bones that move against each other". My reading of the sign: with a chain hanging down, a positive rotation moves its tip toward +x, so opposite-sign amplitudes on the two sides move both tips toward the centre at once, which closes the bottom edge that bridges them (the edge 37-117 spans them).
2. **Expect:** flipping the sign of the `hairback_l` amps (same sign as `hairback_r`, so both tips sway together) removes the closing motion: the 37-117 edge then translates instead of shortening, and TEXTURE_STRETCH on hair_back falls under 1.93. I expect `CHAIN_LAG` to still pass (same lag and phase, only the sign changes) and the other bars to be unchanged.
3. **Chose / turned down:** test it first in a scratch config and a scratch out dir (absolute paths, not the checkout), so the checkout's config only moves when the build says so. Turned down halving all back-hair amplitudes (it would weaken a motion the proposer drafted and changes every link) and turned down `influences: continuous` (the 0.92/0.08 split is not a 0.03 step, so the cut does not touch this edge).
4. **Happened:** scratch build (e1.json, output in scratchpad) exit 0, `build: PASS`. `check: PASS; 9 of 9 bar(s) measured`. TEXTURE_STRETCH now severity 1.126 (ceiling 1.926544), worst `hair_front` 1.114; hair_back max 1.045. CHAIN_LAG still PASS with the same amp values. Matches the expectation. The contact picture is too small to show the back hair, and the back-hair tips sit behind topwear and skirt, so the picture cannot show the change either way; I compared the top hair in frames 0, 12, 22, 32 of both builds (crops in scratchpad) and saw no visible break.


## Entry 9

1. **Read:** the PASS result above; the proposal's own sign pattern (`bang_r` and `bang_l` both +1, `lock` and `lock1_` both +0.8, `hairback_r` +0.6 and `hairback_l` -0.6): the back hair is the only hair chain pair that mirrors its sign, which is the one that closes; and `rigc render --folds` on the draft shows "0 of 8 mesh(es) fold", so the Does-not-fold line does not need the change.
2. **Expect:** after the edit the checkout's build exits 0, check 9 of 9 PASS, and `render --folds` still names no mesh.
3. **Chose / turned down:** change only the sign of `hairback_l` amps (magnitudes unchanged, so every chain keeps its designed motion size) — one value set, the fix the messages point at. Turned down halving amplitudes (weakens the sway for both sides) and turned down `rule: heat` / `influences` (the fold cases in §3 are weight steps at 2 px outline edges; this is a 30 px lattice edge whose ends move toward each other).
4. **Happened:** checkout build exit 0 (`build: PASS`), `check: PASS; 9 of 9`, TEXTURE_STRETCH 1.126. Same result as the scratch build. No SURPRISE.


## Entry 10

1. **Read:** the Pass lines in TASK.md (Does not fold, Whole, Kept); the proposal's eight drafted meshes (`mesh_report.json`: 8 rows).
2. **Expect:** `rigc render --folds` over the new build names no mesh (0 of 8); `out/parts.json` `recomposite` shows 1726 uncovered error px (≤ 3,500); the mesh report still lists 8 meshes.
3. **Chose / turned down:** run the fold reading on the build's own `out/check/build` (the packed artifact), into scratchpad. Turned down reading `grade.py` source to learn how the grader measures these; I will use only its printed lines.
4. **Happened:** `rigc render --folds` over the fixed build: "0 of 8 mesh(es) fold". `out/parts.json` recomposite: uncovered_error_px 1726 (≤ 3,500). `mesh_report.json` lists 8 meshes. Matches the expectation.


## Entry 11

1. **Read:** the five idle frames of the new build (f0000, f0010, f0020, f0030, f0040, out/check/idle_frames/idle), viewed as an image: the figure seated, hand on the knee, the other arm to the side, crossed ankles, no visible tear or fold in the hair, skirt or sleeves.
2. **Expect:** no file change; the picture is the human-facing reading the task asks for, and it should agree with the machine's PASS.
3. **Chose / turned down:** no further config edit. Turned down a keypoints file (`propose --keypoints`) built by eye from the painting: that would be a guess presented as a measurement, and the bars already pass.
4. **Happened:** I see the five frames as a plausible seated idle: breath, a head tilt, hair and skirt move, nothing folds or tears, the hand stays on the knee. Consistent with the machine's PASS. No SURPRISE.

## At the end

- **Where I guessed:** the choice of `hairback_l` amplitude sign as the cause rests on my reading of the chain geometry (a positive rotation moves a hanging tip toward +x) and not on a measurement of tip positions; the scratch build confirmed the effect. The proposal's leg region (`legwear`, no rule, placed on hip) and the hip height were accepted from the draft without a joint measurement. The `note` key I added inside the hairback_l track records the reason.
- **What I could not find:** whether the proposer intended the mirrored sign on the back hair, or copied the sleeves' convention. No document said which. Whether a keypoints file (`propose --keypoints`) would have placed the seated joints better: AUTHORING says a seated figure needs one, I had no observed joints (pose_seated.json is a control skeleton at latent size, which §3 says is not the observed pose), so I skipped it and the draft's rules passed LINT. Whether `bottomwear`'s high drift count (21999) in assemble matters: no bar reads it; I did not investigate.
- **Surprise tagging I missed:** entries 4 and 6 each had a result that differed from line 2, and I wrote it without the `SURPRISE:` prefix the form asks for. Entry 4 is the `bottomwear` drift count (21999) and the wrong expectation of a LINT line; entry 6 is the `hair_back` texture stretch that I did not expect. Entries 4 and 6 should have begun line 4 with `SURPRISE:`. I did not rewrite those lines after the fact.

