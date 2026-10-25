# What we missed

### `propose` drafts opposed amplitudes on shared back-hair masses that fail its own squeeze LINT

- **Package**: `@rig-c/parts` (`rig-parts propose`)
- **Where it hit**: task `01`, entry `3` in `journal.md`, and task `03`, entry `3` in `journal.md`
- **What we had to do instead**: On both paintings `propose --parts --write-config` drafted `"hairback_r"` with `"amps": [0.6, 1.4, 2.4]` and `"hairback_l"` with `"amps": [-0.6, -1.4, -2.4]` on the single `"hair_back"` mesh (tips 55.0 px apart in task 01, 39.0 px apart in task 03), and in the same run emitted a `LINT` line reporting that the opposed signs squeeze triangle 135 (ratio 2.455 in task 01) or triangle 167 (ratio 15.572 in task 03) past `TEXTURE_STRETCH`'s `<= 1.926544` ceiling. We edited `config.json` by hand to set `hairback_l`'s `amps` to `[0.6, 1.4, 2.4]` and re-ran `propose --from-config` in task `01` entry `4` and task `03` entry `4`.
- **What would have helped**: When `propose` places two back-hair chains on the same `hair_back` mesh close enough to trigger its own pair-squeeze check, drafting same-sign `amps` directly would avoid writing a config that fails the squeeze LINT in the same invocation.

### `motion.animations_from` rejects `rigc`'s top-level `easings` table

- **Package**: `@rig-c/parts` (`assemble` config loader for `motion.animations_from` and `docs/AUTHORING.md` §3 *Recipe: expressions and other named animations*)
- **Where it hit**: task `02`, entry `1` in `journal.md`
- **What we had to do instead**: Following `node_modules/rig-c/README.md` (which documents `rigc`'s motion format with a top-level `"easings"` map and named `"curve"` references) and `AUTHORING.md` §3 ("Name a file in rig-c's motion-spec shape"), we included `"easings": { "sine": [0.37, 0, 0.63, 1] }` in `animations.json`. `rig-parts build` refused at `[assemble]` with `FAIL CONFIG_KEY_KNOWN: config.motion.animations_from (.../animations.json).easings — is not a field here; known: spec, animations`. We removed `"easings"` and `"curve": "sine"` from `animations.json` and re-ran `rig-parts build` in task `02` entry `2`.
- **What would have helped**: Either allowing `rigc`'s top-level `easings` object in `motion.animations_from` files (merging it into `rig/motion.json`), or stating in `AUTHORING.md` §3 (*Recipe: expressions and other named animations*) that `animations_from` accepts only `spec` and `animations` and requires inline 4-number Bézier `curve` arrays on keys rather than named `easings`.

### `check` skips torso-to-sleeve seam checks across animations beside `idle`

- **Package**: `@rig-c/parts` (`rig-parts check` / `rig-parts build`)
- **Where it hit**: task `02`, entry `2` and entry `3` in `journal.md`
- **What we had to do instead**: In task `02` entry `2`, `rig-parts build` passed 11 of 11 bars while skipping `SEAM_OVER_MOTION` (`no neighbour pair is declared`). In entry `3`, `grade.py` ran `rigc render --seam topwear:handwear_r --seam topwear:handwear_l` on `bow` and reported `FAIL holds_together: {"opens": {"topwear|handwear_l": {"frames": 17, "max_px": 40}}}` because keying `chest` moved `handwear_l` (100% under `chest` via `sleeve_l`) against `topwear` (shared between `chest` and `hip`). We updated `bow` in `animations.json` to key `neck` and `head` instead of `chest` and re-ran in entry `4`.
- **What would have helped**: Having `check` (or a `--seam-pairs` flag that also runs over animations beside `idle` in `animations_from`) evaluate default adjacent torso/sleeve pairs (`topwear:handwear_r`, `topwear:handwear_l`) across non-idle clips during `build`.

### `mesh-stats` omits per-region vertex counts on `contour` meshes

- **Package**: `@rig-c/parts` (`rig-parts mesh-stats`)
- **Where it hit**: task `04`, entry `1` and entry `2` in `journal.md`
- **What we had to do instead**: We used `rig-parts mesh-stats` to bring the rig's triangle count from 712 (entry `1`) down to 588 (entry `2`) before running a full build. Because `mesh-stats` prints only total vertices and triangles per mesh (`topwear — contour 83 vertices, 130 triangles`) and not the per-region reached counts (`g > 0` and `g = 1`) that `src/contour.ts` computes for `mesh_report.json`, we had to estimate the `bust` region's vertex share from its radius and spacing until the full build in entry `3` confirmed `21 of 83` vertices moved `> 0.5` rig px.
- **What would have helped**: Including each contour region's reached vertex count (`g > 0` and `g = 1`) in `rig-parts mesh-stats` output so patch size and vertex share can be verified alongside triangle budget before running `rig-parts build`.
