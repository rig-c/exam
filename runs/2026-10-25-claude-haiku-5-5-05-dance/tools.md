## The two write-config commands disagree about which file to write
- **I was trying to:** write the proposal's text into a config from `assemble --propose-plan` and from `propose --cloth`, and keep my own config unchanged.
- **The tool gave me:** for `propose --cloth`: `FAIL  PROPOSE_WRITE_CONFIG_FRESH: … exists; the config is written to a new file, never over the --cloth config or an earlier one`. For `assemble --propose-plan` with a new file: `FAIL  USAGE: --write-config must name the same file as --config for assemble --propose-plan`.
- **What would have helped:** one sentence in AUTHORING §4 step 6 and in the cloth recipe, next to the command: "`assemble --propose-plan` writes the same file it reads; `propose --cloth` writes a new one". The fresh-file rule is only in the guide's refusal text.
- **Cost:** about 3 minutes across tasks 02 and 03. Got there in the end by writing the same file in one case and a new file in the other.

## A propose LINT fix becomes a hand edit under the cloth recipe
- **I was trying to:** keep the sign fix I had made on `hairback_l` (the LINT's "give both the same sign") when adding the cloth recipe for back hair in task 02.
- **The tool gave me:** `FAIL  PROPOSE_WRITE_CONFIG_CONFLICT: config.motion.tracks[5] "hairback_l" — motion.tracks entry "hairback_l" is the recipe's, and it was changed by hand: it holds amps [0.6,1.4,2.4] where the draft removes the entry … take the draft by removing the hand edit`.
- **What would have helped:** a note in the LINT section that a sign or amplitude fix on a chain the cloth recipe will replace is itself a hand edit to remove, or that the cloth recipe should go in before the LINT fix.
- **Cost:** about 2 minutes: one refused write, one edit to remove the track, one more write.

## `chains` for back hair: per side or in total?
- **I was trying to:** set the back hair's tree count with `cloth.back hair.chains`.
- **The tool gave me:** with `chains: 2`, `LINT hairback_r0_, hairback_r1_ on mesh 'hair_back' (side r): 2 tree(s) for 1 visible hair mass(es)`. The recipe table reads "tree k of `chains` owns the cell k/N .. (k+1)/N of the art's width", which reads as a total, while the optional `back hair` paragraph says "per side".
- **What would have helped:** one line stating whether `chains` is the count per side for `back hair` (the paragraph suggests so) or the total, with the same meaning for `front hair`.
- **Cost:** about 2 minutes; one more write to correct it to 1.

## The build's check does not see a gesture's seams
- **I was trying to:** pass the grader's "Holds together" line for the gesture (task 02, a head turn and chest lean).
- **The tool gave me:** build reported `[check]   SEAM_OVER_MOTION: SKIP — no neighbour pair is declared: parts.json holds no limb segment below a joint (config.limbs) and no --requirements seam names two parts`, and the build was green. Only the grader then said `"holds_together": {"opens": {"topwear|handwear_l": {"frames": 13, "max_px": 40}}`. The pair and frames were in `seam_gesture/seam.json`, with no cause given.
- **What would have helped:** build's check reading the seams of every animation it has (not only the idle and declared pairs), or a line saying "a non-idle animation exists and no seam is declared", and a pointer to where `rigc render --seam` writes its pictures.
- **Cost:** about 6 minutes to find the cause by removing one track at a time (two grader runs), before the sign and amplitude choice cleared it.

## Drift on a layer the inputs give wrong: no config-only fix
- **I was trying to:** get the thigh region right, where the painting's colour matches one layer but the pixels sit in the layer drawn over it.
- **The tool gave me:** `drift: "bottomwear" refuses 21999 px of full:bottomwear (its colour more than 90 off the painting, max channel) … the painting is within 90 of "legwear" (21839 px at alpha >= 250, drawn behind "bottomwear")`. Changing the draw order moved the drift to the other layer (`"legwear" refuses 5574 px`).
- **What would have helped:** where the fix in AUTHORING §5 is "move the pixels in the layer PNG" and the inputs are fixed, a config-only route stated for this case: an `assemble.cuts` polygon with `under_fill`, or when draw order is the lever, how to choose between the two orders.
- **Cost:** about 4 minutes. Left the drift in place (5,574 px refused) because neither order was clean and the checks pass; the reading is in the journal.

## The fixture's build runs from its own folder, and the config names files beside it
- **I was trying to:** build the fixture's config from a run directory, not from its folder.
- **The tool gave me:** the fixture README's build line, `From this folder, on the pinned tools: rig-parts build --config config.json …`, and `config.json` naming `caps/arm_r_elbow.png` and eight more cap images relative to the config's own directory.
- **What would have helped:** a note that the config's `caps/` paths resolve beside the config, so a build from another folder needs `caps/` copied next to it. I copied `caps/` without testing whether the build finds them elsewhere.
- **Cost:** about 1 minute; I copied the folder and did not test the other route.

## The grader on the dance runs past the 120-second tool limit
- **I was trying to:** run `python3 grade.py runs/<run>` on task 05.
- **The tool gave me:** the shell command "did not complete within its 120s timeout and was moved to the background". The README and the grader's header say nothing about its run time.
- **What would have helped:** the expected run time for the mannequin dance in the README's "Sitting it" section, so a run is planned for a background shell.
- **Cost:** about 2 minutes of waiting; no failure.

## No guide from spacing to triangle count for a contour region
- **I was trying to:** fit a physics patch (contour topwear plus a bust region) under the 700-triangle budget.
- **The tool gave me:** `mesh-stats: total 933 triangles over 8 mesh(es)` at the recipe's own region spacing, then 849, 785, 771, and 671 after changes to the region spacing (8, 10, 16) and the outline spacing (18, 26, 34). AUTHORING's recipe says "count them before the first build" and gives no table of spacing against count.
- **What would have helped:** a short table in the recipe of how the outline's spacing and the region's spacing change the triangle count, or the budget's share each mesh takes on a figure of this size.
- **Cost:** about 3 minutes and five `mesh-stats` runs; each run was quick, so the cost was in the trials.
