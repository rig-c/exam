# What the tools were missing — claude-fable-5-1, 2026-10-20

## A chain's tip ratio cannot be predicted before the build
- **I was trying to:** decide, before task 01's first build, whether the proposed skirt chains would pass `TIP_OVER_ROOT`, since the README says demo's pasted proposal failed it.
- **The tool gave me:** `@rig-c/parts` README, *What you get*: "the two outer skirt chains were moved out to 0.8 of the skirt's half-width (the proposal's, within 90 px of the centre of a skirt 449 px wide, swung it about its middle and failed `TIP_OVER_ROOT`, 0.442 against 1.4725; moved, 2.425)". My chains were 35–37 px from the centre of a 347 px skirt and passed at 3.673.
- **What would have helped:** the rule itself beside the anecdote — what the ratio is a ratio of, and one sentence on what moves it (chain root distance from the mesh's root line, link count, amplitude) — or a `propose` note that reads it off the draft the way the squeeze LINT reads `TEXTURE_STRETCH`.
- **Cost:** a wrong expectation (I wrote down a likely failure) and nothing else; about five minutes of reading. Got there.

## The recipe says where a key moves a hand, not what makes it read as a wave
- **I was trying to:** key a wave on `sleeve_l` (task 02) from the recipe's numbers.
- **The tool gave me:** AUTHORING §3 *Recipe: expressions and other named animations*: "`sleeve_l0` … at +30 moved its hand bone `sleeve_l2` 43.9 px right and 27.6 px up … so `demo`'s `wave` raises the image's right arm with `sleeve_l0` at +48". With sleeve_l0 +60 / sleeve_l1 +30 the grader read a rise of 259 and no fold, and the contact sheet showed an arm pointing straight sideways.
- **What would have helped:** one sentence that the forearm's world angle is the sum of the shoulder's and the elbow's keys, and that a wave wants the forearm past vertical — or the demo's `wave` keys in the installed package rather than only on the repository page.
- **Cost:** one extra build-and-grade round, about 6 minutes. Got there (sleeve_l0 +50, sleeve_l1 +75, rise 300).

## A build with physics and a second animation takes three times as long, unannounced
- **I was trying to:** wait the right length of time for task 02's build.
- **The tool gave me:** AUTHORING §4 step 9: "How long it takes is §8 (the two reference examples, 12.7 s and 27.5 s wall clock on one machine)". Task 01's build took 77 s; task 02's, with 8 physics constraints and `wave`, 4m03s; the same config rebuilt 2m36s; task 05's with two extra animations 1m25s.
- **What would have helped:** a line at the start of `check` saying how many renders it is about to run (idle, each animation, folds, with and without physics) so a long build is not read as a hung one.
- **Cost:** no wrong action, but I had to decide to keep waiting without a figure. Got there.

## The triangle count of a contour mesh is only known after the build
- **I was trying to:** fit task 04's soft `topwear` under 700 triangles.
- **The tool gave me:** `CONTOUR_BUDGET` ("more vertices than `budget` … coarser `spacing` or region `spacing`") and the `[rig] mesh topwear v= 112 t= 188 … contour tol=2 margin=2 spacing=31 … region bust->chest_jiggle reaches 52 (26 whole)` line, after the whole build. `mesh-draft` drafts lattice entries only and names a contour entry as `NOT COMPARED`.
- **What would have helped:** a dry mesh count — `rig --dry` or a `mesh-draft` that reports a declared contour entry's vertices and triangles without building the rig — so the region spacing can be chosen against the budget in seconds instead of a 2–3 minute build per try.
- **Cost:** one guess that landed at 692 of 700 on the first try; a second try would have been another 3 minutes. Got there.

## No easing can be named from an `animations_from` file
- **I was trying to:** ease the dance's keys (task 05) so the speed rises and falls on the beat.
- **The tool gave me:** AUTHORING §3 `motion.animations_from`: the loader refuses "any other key — rig-c's `easings`, `groups`, … which would be read and not written (`CONFIG_KEY_KNOWN`)" and the file "may name … the easings `shut` and `open` … when the blink writes them"; rig-c's R6: "`curve` is the escape hatch: the absolute `(time, value)` control points, verbatim".
- **What would have helped:** a general easing the rig stage always writes into `motion.json` (an `ease` named `smooth`, say) that a file may name, or an `easings` table admitted from the file and written through — so a clip does not need four hand-computed numbers on every key.
- **Cost:** a small generator script instead of named easings; about ten minutes. Got there (keeps time 1.0).

## A leg that stays on its foot has no recipe
- **I was trying to:** make the hip move while the legs' bottoms stay on the shoes (task 05).
- **The tool gave me:** `propose`'s note `legwear (full:legwear): no rule -> region on hip`, and AUTHORING §3 *A posed figure*: a `leg` chain is drafted on `legwear` only through a `--keypoints` file with three joints per leg — nothing for a figure with no keypoints, and nothing on weighting a part between a moving bone and the ground by hand.
- **What would have helped:** a recipe beside the soft-region one — "a part held at both ends": a config bone under `root` and two explicit segments on the part — or a `propose` rule that drafts the legs as a mesh bound to `hip` and a ground bone when the figure stands.
- **Cost:** worked out from the segment-weighting paragraph; one build. Got there (0.18 rig px).

## The proposer's sleeve joints are not the elbow
- **I was trying to:** key the elbow for the dance without bending the upper arm inside its own band (task 05).
- **The tool gave me:** `proposal.json`: `sleeve_l` points [[507,250],[536,374],[585,497]], and `basis.json` with `mask` as the basis — the middle joint sits at 0.65 of the part's height where the task says the elbow is at 0.54; `propose`'s note `handwear is two blobs: one sleeve chain per mesh, chest only at the shoulder` says nothing about what the joints stand for.
- **What would have helped:** the note saying how the two interior joints of a sleeve chain are placed (thirds of the part? the art's width minima?) and that they are not joints of the arm unless given by `--keypoints`.
- **Cost:** read off the task instead; the joints were moved by hand and the lint stayed clean. About ten minutes. Got there (4.3° against 8).
