## `propose --write-config` writes amplitudes its own `--from-config` then LINTs
- **I was trying to:** go from `propose --parts … --write-config config.json` to a config that builds (tasks 01 and 03).
- **The tool gave me:** the proposal pasted into `config.json`, and on the same run `LINT hairback_r and hairback_l on mesh 'hair_back' squeeze it … their amplitudes are opposed (hairback_r [0.6, 1.4, 2.4], hairback_l [-0.6, -1.4, -2.4]) … give both the same sign (then 1.051), or drop one chain`. It appeared on both paintings, with `closes to 0.064 times its rest length` on the seated one.
- **What would have helped:** the proposer not drafting a pair it lints, or the LINT line saying which config key to edit (`motion.tracks[<n>].amps` of the track whose `chain` is `hairback_l`). I found the track by grep.
- **Cost:** about 2 minutes each time; got there.

## `--from-config` refuses `--full`/`--head`, and the README loop does not say why
- **I was trying to:** re-run LINT after editing the config, with the same flags as the `propose --parts` line before it.
- **The tool gave me:** `FAIL  USAGE: --full and --head draft the turn control while proposing; --from-config proposes nothing`.
- **What would have helped:** a note on the README loop's `--from-config` line (the second `propose --parts` line, "# -> LINT lines; exit 1 while any remain") that the flags differ from the line above it: `--full`/`--head` only on the drafting call.
- **Cost:** one wasted step (journal entry 5 of task 01); my pipe through `grep` also made `journal.py run` report exit 0 for it.

## `mesh-stats` does not take `--help`, and the soft-region recipe's numbers go over a 700-triangle budget
- **I was trying to:** copy the recipe fragment in AUTHORING §3 *Recipe: a soft region driven by physics* (`"spacing": 18 … "spacing": 6, "band": 16`) for task 04 and fit 700 triangles.
- **The tool gave me:** `mesh-stats: topwear — contour 192 vertices, 329 triangles` / `total 853 triangles over 8 mesh(es)` for spacing 24 and a circle of r 40; `rig-parts mesh-stats --help` gives `FAIL  USAGE: mesh-stats does not take "--help"`. Raising tolerance alone then gave `FAIL  CONTOUR_COVERAGE … 8 of 27280 art pixel(s) … lie outside the mesh at tolerance 2 px and margin 1 px`.
- **What would have helped:** a line in the recipe giving the triangle cost of the fragment's numbers next to the `reference-sample` figures (it quotes 568 triangles for `topwear` but not what changing `spacing` does), and `mesh-stats --help` printing its two flags.
- **Cost:** three `mesh-stats` runs, about 10 seconds each, plus working out tolerance/margin by trial; got there (638 triangles).

## No build line shows a seam opening during a gesture
- **I was trying to:** make an animation (task 02) in which "nothing comes apart", keyed on the bones the recipe says are free (`head`, `chest`).
- **The tool gave me:** `build: PASS`, `ANIMATIONS_DO_NOT_FOLD: PASS`, and `SEAM_OVER_MOTION: SKIP — no neighbour pair is declared: parts.json holds no limb segment below a joint (config.limbs) and no --requirements seam names two parts`. The grader then failed `holds_together: {"topwear|handwear_l": {"frames": 12, "max_px": 35}}`.
- **What would have helped:** in the *Recipe: expressions and other named animations* section, under "Key the bones the idle leaves alone", a sentence that a `chest` translate or large rotate opens `topwear` against `handwear_*` (the chest is in the topwear mesh blended with `hip`; the sleeve is rigid to it), and the command to check it: `rigc render --candidate out/check/build --animation <name> --seam topwear:handwear_l,topwear:handwear_r`. I found the command only by reading `grade.py`'s `holds_together()`.
- **Cost:** about 6 minutes (one probe build with the animation split by component, one seam script, two more grades); got there by dropping the chest translate and lowering the chest turn to ±2°.

## Nothing says how far the planted legs can stretch
- **I was trying to:** bounce the hip on the beat in task 05 with the two leg iks holding the feet.
- **The tool gave me:** the README's "Move or dip `hip` and the feet stay put", then (grader) `FAIL on_her_feet: the end of a leg (shin_l, shin_r) gets 8.32 rig px from where it meets foot_l, foot_r, against <= 6.0` with a bounce that touched the rest height. The build's own `FEET_STAY_LEVEL: PASS` and `SEAM_OVER_MOTION: WARN — … 2 warning(s)` named nothing about it.
- **What would have helped:** in the mannequin README's *Feet are planted* paragraph, "the legs are almost straight at rest (thigh 243 + shin 245 rig px against 488 to the ankle): `hip` can dip but not rise or move sideways without the ankles coming off their targets", and the `SEAM_OVER_MOTION` WARN line naming its pairs on the build line. After the fix it still reads 5.1 against 6.0 and I do not know which key causes the rest.
- **Cost:** about 4 minutes and one regrade; got there.

## The task's command is written for the inputs' directory, the run lives elsewhere
- **I was trying to:** run `rig-parts build --config config.json --source inputs/painting.png …` from a run directory that must end in the task name.
- **The tool gave me:** `TASK.md` command lines with relative `inputs/…` and `out`, and `README.md` saying only that the grader copies the config beside the inputs.
- **What would have helped:** one sentence in the README's *Layout* saying where to build a run (for example: from the clone's root, with the inputs at `tasks/<task>/inputs/` and `--out runs/<run>/out`), and, for task 05, that `caps/` must sit beside the config in the run directory for the config's relative `cap` paths (the grader copies them; my own builds needed `cp -r fixtures/mannequin/caps`).
- **Cost:** a few minutes of working out the layout from `grade.py`; got there.
