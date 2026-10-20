# Journal — claude-haiku-5-5, 02-move, 2026-10-20

## Entry 1

1. **Read:** TASK.md `Do` 1 (a wave, at least 1 s, a bone rising at least 150 rig px more than the median bone); AUTHORING §3 *Recipe: expressions and other named animations* (`motion.animations_from` names a file in rig-c's motion-spec shape `rigc-motion/1`; key the bones the idle leaves alone, such as `sleeve_l0` rather than `sleeve_l0_ctl`; a `rotate` key is CCW-positive in y-up, and on `demo` a positive key on the image-right sleeve raises the hand). Rig from task 01: `sleeve_l0` 127 rig px, `sleeve_l1` 132, `sleeve_l2` 142, so the hand chain is about 400 px long.
2. **Expect:** `build` exits 0 with an extra animation `wave` listed under `[rig]` and `ANIMATIONS_DO_NOT_FOLD` naming one animation. The hand should rise 100 to 200 rig px with `sleeve_l0` at about +100 degrees (estimate from arm length and rest angle, not measured yet).
3. **Chose / turned down:** a separate `animations.json` in the run directory (the recipe's door), keying `sleeve_l0` for the raise and `sleeve_l1` for the wave, one-shot, 2.4 s. Turned down: keying `sleeve_l0_ctl` or the idle's chain tracks (the idle owns those), and a 0.5 s clip (the task needs at least 1 s).
4. WTF?: `build` exit 0; `[rig] animations beside the idle … as written: wave`, `ANIMATIONS_DO_NOT_FOLD: PASS — 2 animation(s) read … 0 folding mesh(es)`. Then I measured the wave with `rigc render --candidate out/check/build/skeleton.json --animation wave --geometry --folds --out work/render_wave`: `0 of 8 mesh(es) fold`. The bone rise was 409.8 rig px (`sleeve_l2_ctl`, frame 17) above the median bone, against my estimate of 100 to 200. The contact sheet shows the arm lifted toward the image's right and the hand above the head around frames 7 and 8, but the sleeve reads as a thin streak in frames 3 to 6. I expected a hand, and the picture shows a stretched strip. That is what I wrote; I did not change the animation yet.

## Entry 2

1. **Read:** TASK.md `Do` 2 and the pass line `Trails` (physics constraints on at least two bones); AUTHORING §3 *Strands that trail* (one `physics` constraint per link on the link bone, `rotate: 1`, softened down the chain by `1 − 0.35·i/(n−1)`); the rig's bone names in `out/rig/rig.json` (`lock0`…`lock3`, `lock1_0`…`lock1_3`, the strands that hang free, 44 rig px links).
2. **Expect:** `build` exits 0, `physicsConstraints=8` in the check line, the loop's `loop physics:` line names the 8 bones, and `CHAIN_LAG` may move since the keyed `lock` and `lock1_` tracks are removed.
3. **Chose / turned down:** put the physics on the eight `lock` links and delete the two keyed `lock`/`lock1_` tracks, so the strands are driven by physics and not by keys (the task says "on physics rather than keys"). Turned down: leaving the keyed sway in place and adding physics on top (the strand would then be keyed, not free), and putting physics on the bang chains (they are a template, not free strands).
4. `build` exit 0: `physicsConstraints=8`, `CHAIN_LAG: PASS`, `check: PASS; 10 of 10 bar(s) measured, 0 skipped`, `loop physics: 8 physics constraint(s) left out … "lock0_phys" on bone "lock0"`. As I expected. Re-rendering the wave on the physics build: `0 of 8 mesh(es) fold` and the max rise over the median is still 409.85 rig px (`sleeve_l2_ctl`, frame 17). Nothing surprised me this time.

## At the end

- **Where I guessed:** the wave timings (0.5 s raise, 0.4 s wave) and the physics `inertia 0.8`, `damping 0.85`, root `strength 90` are my choices, copied from the recipe's `demo` values; the `1 − 0.35·i/(n−1)` softening is the recipe's rule. I did not tune them against a picture.
- **What I could not find:** whether the wave reads as a wave; the contact sheet shows the sleeve as a thin streak on frames 3 to 6, and I did not find a document that says how to avoid that for a sleeve raised 100 degrees.
