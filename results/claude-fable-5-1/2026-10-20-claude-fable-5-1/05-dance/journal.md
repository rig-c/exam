# Journal — claude-fable-5-1, 05-dance, 2026-10-20

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

1. **Read:** TASK.md — the arm bands (elbow at 0.54 and wrist at 0.20 of the arm part's height above its lowest point; upper-arm bands 0.62–0.92, forearm 0.22–0.46) and "her legs are one flat piece that hangs from the hip and her shoes are another that sits on the ground". AUTHORING §3 `bones` (a chain's `points` are its joints, links turned along the chain), `meshes.<part>.segments` (`[bone, [x0,y0], [x1,y1]]` explicit segments; weights `1/(d+r)²`, at most 4 bones), `regions.<part>` (every part is exactly one of mesh or region), *A posed figure* (the keypoints route drafts `leg` chains on `legwear` — but through a keypoints file I do not have; by hand the same thing is a mesh with segments). My task-04 config: `sleeve_l` points [507,250],[536,374],[585,497] tip [648,624] over a part whose box is y 234–629 (395 tall) — its middle joint sits at 0.65 of the height, inside the upper-arm band 0.62–0.72, so an elbow key there would read as the upper arm bending; `sleeve_r` likewise ([342,381] at 0.65 of 238–642). `legwear` is `regions.legwear: "hip"`, box 204,555 368x524 (y to 1079); `shoes` a region on `root`.
2. **Expect:** (a) move each sleeve chain's two joints onto the given elbow and wrist heights along the arm's own line — `sleeve_l` [[507,250],[553,416],[611,550]] tip [648,624]; `sleeve_r` [[357,254],[330,424],[279,561]] tip [242,637]; (b) add `feet` `{parent: root, at: [416, 1070]}` and make `legwear` a `grid` mesh (36 px) with segments `["hip", [300,600],[590,600]]` (across the thighs) and `["feet", [290,1070],[560,1070]]` (across the ankles), removing it from `regions`; then `propose … --from-config` exits 0 with `0 LINT line(s)` and the mesh line later costs legwear about 150–200 triangles (692 + that < 1,000).
3. **Chose / turned down:** joints moved rather than new bones added (the part names and the chain's three links stay, and the task says the proposed joints are not where the elbow is); a `feet` bone under `root` rather than a segment on `root` itself (the guide says never to declare root; naming it in a segment is a reading I would be guessing at); a lattice for legwear rather than contour (the budget has room and nothing deforms it locally). Turned down leaving the sleeve chains as proposed (an elbow key would fail *Arms bend at the joints* by construction) and the `--keypoints` route (no keypoints file; the control pose given in task 03 is a different painting).
4. **Happened:** exit 0, `0 LINT line(s) over 9 mesh(es) and the hip`; every sleeve link `checked, clean — read by off-art`; `feet` not checked (an explicit segment's bone). As expected.

## Entry 2

1. **Read:** rig-c AUTHORING §1.2 and R6 (a key carries `ease` or `curve`; `curve` is four absolute `(time, value)` control points per channel; the last key carries neither); parts AUTHORING *Recipe: expressions* (key the bones the idle leaves alone — `chest`, `head`, chain links; `translatex`/`translatey` are in the parent's axes, y up; positive `rotate` swings an arm toward the image's right and up); TASK.md: 120 bpm, 4.0 s loop at 24 fps, *Keeps time* reads the frame-to-frame speed for what repeats every two beats (1 s), *Closes* needs the last frame on the first, *Soft in the dance* 3–15 rig px on `topwear` (task 04's hop of 24 px gave 6.61).
2. **Expect:** `dance.json`, every key eased with a `curve` [t0 + 0.35·Δt, v0, t1 − 0.35·Δt, v1] so the speed rises and falls each half-cycle: `hip` translatey 0 → −12 → 0 every 0.5 s (a dip on each beat); `hip` translatex 0 → +14 → 0 → −14 → 0 over 2 s; `chest` rotate ∓4 and `head` rotate ±5 over 2 s; `sleeve_l0` 0 → +30 → 0 and `sleeve_l1` 0 → +45 → 0 every 1 s, `sleeve_r0`/`sleeve_r1` the mirror (−30, −45). The build exits 0 with `animations beside the idle … hop, dance`, `ANIMATIONS_DO_NOT_FOLD` over 3 animations with 0 folds, total triangles about 850–900, `check: PASS`. Risks I see: the forearm's lowest band (0.22–0.30) sits 8 px above the wrist joint, so a forearm bend may read a few degrees there; and the bust spring under a 12 px dip every 0.5 s may read under 3 px.
3. **Chose / turned down:** elbow and shoulder keys only, no wrist key (a key on `sleeve_*2` would bend the forearm's lowest band against the others); a hip dip rather than a root bounce (the task says the shoes sit on the ground and the legs must stay on them; `root` would lift the shoes too); 1 s and 2 s cycles only, so every speed pattern repeats every two beats. Turned down linear keys (a constant-speed zigzag would leave the speed signal nearly flat) and named easings (only the blink's `shut`/`open` exist).
4. **Happened:** exit 0, `build: PASS`, `check: PASS; 10 of 10` in 1m25s. `mesh legwear v= 134 t= 192 … grid=36 bones=2` (I had said 150–200); `TEXTURE_STRETCH … meshes 9; triangles 884`; `animations beside the idle … hop, dance`; `ANIMATIONS_DO_NOT_FOLD: PASS — 3 animation(s) … (idle, hop, dance): 0 folding mesh(es)`. As expected.

## Entry 3

1. **Read:** TASK.md's fourteen pass lines and grade.py's readers: `loop_gap` on the no-physics build, `paths` for the hands (from topwear's middle) and the trunk (from shoes' middle), `arm_read` bands, `ankles` (lowest 4 % of legwear against the nearest shoes vertex, ≤ 6), `on_the_beat` (harmonics that are multiples of 96/24 = 4), `difference` on topwear 3–15, 24 fps.
2. **Expect:** closes within 0.5 (every track returns to its first value at 4.0); hands well over 100 (the fingertips swing about 200–400 px); whole body ≥ 15 (hip's box 28 × 12); arms bend ≤ 8°; on her feet ≤ 6 (the ankle vertices ride `feet` almost alone); keeps time ≥ 0.5; soft 3–15 — the one I am least sure of, the dip being half the hop's; no folds; 884 ≤ 1000. 14 of 14 if the soft line holds.
3. **Chose / turned down:** grade once and read; turned down raising the dip beforehand (a larger dip pulls the thighs further from the ankles and I have no figure for either side).
4. **Happened:** `14 of 14 line(s)`: closes 0.0; hands 404.6 / 401.0; whole body 24.5; arms bend at most 4.3°; on her feet 0.18 rig px; keeps time 1.0; `soft_in_the_dance … 3.486 rig px at dance frame 22, against 3.0 to 15.0` — the one I was unsure of, and it is 0.5 above the floor; no folds; 884 triangles. As expected, with the soft line closer than I would like. The grader's `dance@24fps/contact.png` shows the arms swinging out and up to the sides with the body swaying — a sway with arm flaps, on the beat.

## At the end

- **Where I guessed:** the new sleeve joints' x positions (interpolated along the proposed chain at the given heights — the heights are given, the x is mine); `feet` at [416, 1070] and the two legwear segment lines (y 600 across the thighs, y 1070 across the ankles) read off the part boxes; legwear `grid 36`, `r 10`; every dance amplitude and the 0.35 ease handle; the hip dip of 12 px (the soft line came out at 3.486, close to its floor, and I did not have a figure to size it by).
- **What I could not find:** a recipe for a leg that stays on its foot — the keypoints route drafts `leg` chains but only from a keypoints file I did not have, and nothing says how to weight a leg by hand; where the proposer's sleeve joints sit relative to the real elbow (the task gave 0.54; the proposal's middle joint was at 0.65 of the part and nothing in the proposal says what it rests on besides `basis.json`'s `mask`); an easing I could name from an `animations_from` file (the file refuses an `easings` table and only the blink's `shut`/`open` exist, so every eased key carries four hand-computed `curve` numbers).
