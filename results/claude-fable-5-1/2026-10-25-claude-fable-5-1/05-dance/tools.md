# What the tools were missing — claude-fable-5-1, 2026-10-25

Entries from the five journals and transcripts, about `@rig-c/parts` 1.60.0 and `rig-c` 2.67.2.

## The `layers` table's box is the manifest's, not the art's
- **I was trying to:** read the standing figure's height off `rig-parts layers inputs/layers/full` before choosing `assemble.rig_scale` (AUTHORING §3 says to keep the figure about 1,100–1,200 rig px tall), task 01, entry 1.
- **The tool gave me:** a box column of `0,0 1024,1024 1024x1024` for every body layer — the wrapper manifest's box — so the table says nothing about where the art is; only `propose`'s `mesh spacing: grid 29 = round(H / 37), H 1087 rig px` note, three steps later, confirmed the scale.
- **What would have helped:** an alpha box (or the figure's rows top to bottom) in the `layers` table, or an `H` line from `assemble`, so `rig_scale` can be sized at step 3 instead of being guessed and confirmed at step 7. On task 03 I guessed the seated figure at ~900 rig px and it read 1107.
- **Cost:** about two minutes of reading on task 01, a wrong guess written in task 03's journal; got there through the later note both times.

## A keyed chest opens the top against the arm, and nothing read it before the grader
- **I was trying to:** give the rig a gesture (task 02) that leans the chest 2° and lowers it 4 px beside a head turn, from the expressions recipe's "Key the bones the idle leaves alone".
- **The tool gave me:** `check: PASS` with `SEAM_OVER_MOTION: SKIP — no neighbour pair is declared: parts.json holds no limb segment below a joint (config.limbs) and no --requirements seam names two parts`; the grader's own `rigc render --seam` then read `seam "topwear" | "handwear_l" opens on 18 of 25 frame(s) … no gap; ghost … worst frame 6 (t=0.5000s): 18 px` — the top's shoulder vertices are weighted partly to the hip segment while the arm rides the sleeve chain under `chest`, so the top lags the arm.
- **What would have helped:** either `SEAM_OVER_MOTION` reading `topwear` against each `handwear` part by default on a rig with no limbs (the pair every gesture that keys `chest` touches), or one sentence in the expressions recipe: a key on `chest` moves a sleeve-chain arm fully and a chest-and-hip-weighted top in part, so the shoulder opens; key `head` for a gesture that must hold, or declare the pair as a `seam` requirement.
- **Cost:** one extra build and grade (about 4 minutes) and the task's one WTF; got there by dropping the chest keys.

## What the soft-region recipe costs beside a budget
- **I was trying to:** copy the recipe's contour mesh with one bust region onto `topwear` under task 04's 700-triangle budget, at the background spacing the lattice had (29) and the region at spacing 10 instead of the recipe's 6.
- **The tool gave me:** `mesh-stats: topwear — contour 154 vertices, 253 triangles` and `mesh-stats: total 777 triangles over 8 mesh(es)` on the first count — the outline at tolerance 1 / margin 1 alone holds more vertices than the 61-vertex lattice it replaced; the recipe's "Read what it costs" points at `mesh-stats` and at the region's vertices, not at the outline.
- **What would have helped:** a line in the recipe (or in *A contour mesh*) saying what a tolerance-1 outline costs on a part of this size against its lattice, and that `tolerance`/`margin` 1.5 and a coarser background spacing are the first knobs for a budget; `mesh-stats` did the measuring in a second once I knew to turn them.
- **Cost:** one extra `mesh-stats` round (under a minute) and task 04's WTF; got there at 607 triangles.

## `animations_from` refuses rig-c's `easings`
- **I was trying to:** write task 05's dance in rig-c's own motion-spec shape, with one named easing (`"easings": {"smooth": [0.25, 0, 0.75, 1]}`, rig-c AUTHORING §1.2 and §4.5 "`ease` names an entry of `easings`") and `"ease": "smooth"` on each key.
- **The tool gave me:** `FAIL  CONFIG_KEY_KNOWN: config.motion.animations_from (…/dance.json).easings — is not a field here; known: spec, animations` — the parts loader admits only `spec` and `animations` in that file, so a key's `ease` has nothing to name; the expressions recipe's wave uses inline `curve` handles and says `curve` is rig-c's escape, but does not say `easings` is out.
- **What would have helped:** either the loader passing `easings` through to rigc as it passes `animations`, or one sentence in the recipe's bullet list: *`easings` is not read here — write each key's `curve` as absolute handles.*
- **Cost:** one refused build (about a minute) and a rewrite of every key's easing as `[t0 + 0.25·dt, v0, t0 + 0.75·dt, v1]`; got there on the next build.

## Where the shin's end is read, on a planted foot
- **I was trying to:** size the dance's hip dip so the mannequin's shins stay within task 05's 6 rig px of their feet (`on_her_feet`), from the fixture README's "Move or dip `hip` and the feet stay put".
- **The tool gave me:** `FEET_STAY_LEVEL: PASS — … each foot's drawing within ±10 degrees of its setup pose while a bone above it is turned` from `check`, and nothing about how far the shin's end moves against the foot; the grader then read 5.65 rig px at a 12 px dip (4.75 at 8 px).
- **What would have helped:** a figure from `check` or `rigc render` for a limb joint over an animation — how far the segment below the joint moves against the part under it, in rig px — the way `SEAM_OVER_RANGE` poses the declared joints; the README's "the declared joints hold … ≤ 6 px on that reader at ±45" names a reader `check` does not print.
- **Cost:** one extra build and grade (about 4 minutes) to add margin; got there.

## The squeeze LINT's remedy leaves the choice of chain to me
- **I was trying to:** correct the back-hair draft on tasks 01 and 03 from `LINT hairback_r and hairback_l on mesh 'hair_back' squeeze it … give both the same sign (then 1.046), or drop one chain`.
- **The tool gave me:** the figure for each remedy, which was enough to act on — but not whether a chain's amplitude sign has a meaning on its own (which way `+` swings each side), so I flipped `hairback_l` to match `hairback_r` without knowing whether the mirror choice would read differently to an eye.
- **What would have helped:** the LINT naming the direction each sign swings the tips (toward or away from the head's axis), or the proposer drafting the two chains with one sign in the first place, since 1.13.0 already reads the squeeze.
- **Cost:** none in time (one hand edit each time, both built green); a guess recorded in task 03's journal.
