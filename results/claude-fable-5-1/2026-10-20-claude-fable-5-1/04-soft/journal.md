# Journal — claude-fable-5-1, 04-soft, 2026-10-20

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

1. **Read:** AUTHORING §3 *Recipe: a soft region driven by physics* — a config bone under `chest` (`chest_jiggle`), `topwear` moved from `grid` to `contour` with one circle region on that bone (`spacing` inside, `band` across which the weight falls), and a `physics` constraint `x: 0.5, y: 1, inertia 0.25, strength 120, damping 0.92, mass 1, mix 1` — the values tuned for reference-sample's `hop`, whose keys (hip down 5, up 24, landing −6 at 0.45 s) are exactly `tasks/04-soft/hop.json`'s; on it the bust moved at most 6.702 rig px at 30 fps. Its *Limits*: "the region's `band` caps the displacement" (PR #187's inertia 0.5/strength 100 gave 9.85 px and tore the band past 1.926544). *A contour mesh*: outline at tolerance 1 is dense and "used more vertices than the lattice at the same spacing"; `CONTOUR_BUDGET`, `CONTOUR_ONE_ISLAND` (`stray`). grade.py's `BUDGET` comment: the recipe's own region spacing (6) copied gives 920 triangles here, against 700. Task 01's build: 590 triangles, `topwear` lattice 58 v / 86 t at grid 31, part box 350,210 171x218; the bust on `parts/topwear.png` sits about rig (446, 332), the chest bone at [446, 325]. TASK.md: `hop` must be carried exactly as given (`motion.animations_from`, the recipe for named animations).
2. **Expect:** from task 01's config + `hop.json` as `animations_from` + `chest_jiggle` at [446, 332] + `topwear` as `contour {tolerance 2, margin 2, spacing 31, stray 4, regions: [bust circle cx 446 cy 332 r 30, bone chest_jiggle, spacing 12, band 16]}` + the physics constraint: `build` exits 0, the `[rig] mesh topwear` line prints a contour mesh of roughly 100–180 triangles (total under 700), `check: PASS; 10 of 10`, `loop physics: 1 physics constraint(s) left out`, `ANIMATIONS_DO_NOT_FOLD` reads idle and hop with 0 folds. On `hop` the bust should move about 5–8 rig px (the recipe's 6.7).
3. **Chose / turned down:** region spacing 12 and tolerance/margin 2 instead of the recipe's 6 / 1 / 1 — the recipe's spacing is what the grader's comment says blows the budget, and a coarser outline costs fewer vertices; task 01's config rather than task 02's (fewer physics constraints and no wave means a shorter build and a cleaner with/without comparison; the task allows either); the recipe's physics values unchanged (tuned on the same hop). Turned down `auto` (its reduction is held to a declared bend and §3 says it is not always smaller) and a polygon region (a circle is what the recipe measured).
4. **Happened:** exit 0, `build: PASS`, `check: PASS; 10 of 10` in 2m38s. `mesh topwear v= 112 t= 188 hull= 34 contour tol=2 margin=2 spacing=31 … region bust->chest_jiggle reaches 52 (26 whole)`; `TEXTURE_STRETCH … triangles 692` — 8 under the budget, closer than I expected (I had said roughly 100–180 for topwear; the outline's 34 hull vertices plus the region's 52 made 188). `loop physics: 1 physics constraint(s) left out — "bust_phys"`; `ANIMATIONS_DO_NOT_FOLD: PASS — 2 animation(s) … (idle, hop): 0 folding mesh(es)`. Within expectation on every line but the margin to the budget.

## Entry 2

1. **Read:** TASK.md's nine pass lines; grade.py builds `config_without_physics.json` beside mine, poses both on `hop` at 30 fps and reads `difference(a, b, 'topwear')` (3–15 rig px; ≥ 8 vertices and ≤ 80 % over 0.5 px), `hop_as_given` compares duration and tracks as values, budget ≤ 700.
2. **Expect:** 9 of 9: soft about 5–8 rig px near the landing (frame 13–15 of 30), a patch of roughly 20–50 of 112 vertices, 692 triangles, hop as given, no folds.
3. **Chose / turned down:** grade once; turned down trimming the budget margin first (692 passes; a coarser region would also shrink the patch the bar reads).
4. **Happened:** `9 of 9 line(s)`: `soft: topwear differs … by 6.61 rig px at hop frame 14, against 3.0 to 15.0`; `a_patch: 40 of 112 topwear vertices move over 0.5 rig px`; `budget: 692 triangles against <= 700`; hop as given; no folds. As expected (6.61 against the recipe's 6.702 on its own hop).

## At the end

- **Where I guessed:** the circle's centre (446, 332) and radius 30 — read off `parts/topwear.png` by eye against the part's box, no measurement names the bust; `tolerance 2, margin 2`, region `spacing 12`, `band 16` — chosen to land under 700 triangles, with only the §3 survey ("the smallest margin that covered every art pixel was … 1.5 at [tolerance] 2") and the recipe's band as guides; `stray 4` from the examples' settings.
- **What I could not find:** how many triangles a contour mesh will cost before building it — the mesh line prints the count after the fact, and `mesh-draft` only drafts lattices; a figure for how far the patch moves per unit of `strength`/`inertia` other than the two worked points the recipe gives.
