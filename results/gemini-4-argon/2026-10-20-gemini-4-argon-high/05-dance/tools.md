# What I missed in `@rig-c/parts` / `rig-c` — gemini-4-argon-high, 2026-10-20

## 1. Fast dry-run triangle count for `contour` + `regions` meshes
- **Task and journal entry where it bit:** 04-soft, entry 1
- **What I was trying to tell or change:** Estimate the total rig triangle count when replacing `topwear`'s uniform `grid: 31` mesh with a `contour` mesh and a refined `bust` circle region so the whole rig stays within `<= 700` triangles.
- **What I had to do instead:** Run a full `npx rig-parts build` with `contour.spacing: 24` and `regions[0].spacing: 14`, read `TEXTURE_STRETCH` (`triangles 722`, 22 over the `700` budget), edit `spacing` to `31` and `18`, and run a second full `npx rig-parts build` (`triangles 654`).
- **What would have answered in one step:** A `npx rig-parts rig --config config.json --dry-run` (or `rig-parts mesh-stats`) flag that triangulates configured meshes against existing `parts/` masks and prints per-slot vertex and triangle counts plus the total triangle count in under a second without running `[assemble]` or `[check]`.

## 2. Minimal `rigc-motion/1` schema snippet under `motion.animations_from` in `AUTHORING.md`
- **Task and journal entry where it bit:** 05-dance, entry 1
- **What I was trying to tell or change:** Write a standalone `dance.json` animation file referenced by `config.motion.animations_from`.
- **What I had to do instead:** Run `npx rig-parts build`, hit `[assemble] FAIL CONFIG_FIELD_PRESENT: config.motion.animations_from (.../dance.json).spec — is absent and required`, read `tasks/04-soft/hop.json` and `02-move/animations.json` to check the exact `"spec": "rigc-motion/1"` header and `tracks` array format, and rewrite `dance.json`.
- **What would have answered in one step:** A 15-line example in `AUTHORING.md` where `motion.animations_from` is documented, showing the required top-level `"spec": "rigc-motion/1"` field and `"tracks": [{ "bone": "...", "property": "rotate|translatex|translatey", "keys": [{ "t": 0, "v": [0] }] }]` structure.

## 3. Anatomical sleeve joint placement (`0.54` elbow, `0.20` wrist) in `rig-parts propose`
- **Task and journal entry where it bit:** 05-dance, entry 1
- **What I was trying to tell or change:** Place the interior joints of `sleeve_r` and `sleeve_l` at the anatomical elbow (~0.54 of part height from bottom) and wrist (~0.20) so upper-arm (`0.62..0.92`) and forearm (`0.22..0.46`) bands stay straight when the arm bends.
- **What I had to do instead:** Inspect `out/check/idle_frames/idle/geometry.json` and `landmarks.png` from task 04 to find the rest `y` bounds of `handwear_r` and `handwear_l` and manually calculate the rig coordinates corresponding to `0.54` and `0.20` height above the lowest vertex (`[330, 424]`, `[282, 561]` and `[553, 416]`, `[612, 550]`).
- **What would have answered in one step:** Having `rig-parts propose` place 3-link sleeve chain joints at `0.54` and `0.20` height fractions instead of uniform `1/3` intervals (which fall inside the `0.62..0.72` upper-arm and `0.30..0.38` forearm measurement bands), or printing each part's rest `y` span and normalized joint heights in `out/propose/landmarks.json`.
