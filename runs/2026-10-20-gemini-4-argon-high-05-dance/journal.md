# Journal — gemini-4-argon-high — 05-dance — 2026-10-20

Rule: lines 1–3 are written BEFORE the command or edit; line 4 AFTER. If line 4 differs from line 2, begin line 4 with `WTF?:` and say how.

---

## Entry 1 — Author `config.json` and `dance.json` for the 4.0 s 120-BPM dance and run `rig-parts build`

1. **Read:** `tasks/05-dance/TASK.md`, `AUTHORING.md`, `src/rig.ts`, `src/motion.ts`, `runs/2026-10-20-gemini-4-argon-high-04-soft/config.json`, and `runs/2026-10-20-gemini-4-argon-high-04-soft/out/check/idle_frames/idle/geometry.json`.
2. **Expect:** Moving `sleeve_r` and `sleeve_l` interior joints to the anatomical elbow (~0.54 of arm height from bottom: `[330, 424]` on `handwear_r` and `[553, 416]` on `handwear_l`) and wrist (~0.20 of arm height: `[282, 561]` and `[612, 550]`) with `segments: ["sleeve_r"]` / `["sleeve_l"]` and `r: 4, exponent: 4` keeps upper-arm (`0.62..0.92`) and forearm (`0.22..0.46`) bands rigid along their own bones (`kink <= 8.0°`); meshing `legwear` (`grid: 31, r: 6, exponent: 3`) with upper thigh segments on `hip` and lower shin/ankle segments on `root` keeps total triangles `<= 1000` and ankles within `<= 6.0` rig px of `shoes`; and authoring a 4.0 s `dance` animation in `dance.json` as four identical 1.0 s (two-beat) cycles with beats at every 0.5 s (`hip` sway `x: ±10, y: -6..+2`, `chest` bounce `y: -4..+3`, and shoulder/elbow swings of `32°`/`20°`) will build cleanly (`exit 0`) and pass all 8 `rig-parts check` bars.
3. **Chose / turned down:** Chose anatomical elbow/wrist placement on `sleeve_r`/`sleeve_l`, `legwear` mesh skinned between `hip` thighs and `root` shins/ankles, `bust_phys` (`x: 0.8, y: 1.0, inertia: 0.35, strength: 120, damping: 0.92`) on `chest_jiggle`, and a 4-cycle symmetric 2-beat loop in `dance.json`; turned down keeping the 1/3-spaced sleeve chains from `01-build` (whose joints sit inside the `0.62..0.72` upper-arm and `0.30..0.38` forearm bands) or keeping `legwear` as a rigid `hip` region (which drags the ankles off `shoes` whenever `hip` moves).
4. **Happened:** WTF?: `rig-parts build` exited 1 at `[assemble]` with `FAIL CONFIG_FIELD_PRESENT: config.motion.animations_from (.../dance.json).spec — is absent and required`, because `dance.json` omitted the top-level `"spec"` header field required by the `animations_from` schema validator.

---

## Entry 2 — Rewrite `dance.json` in `rigc-motion/1` format (`spec`, `tracks` array with `bone`/`property`/`keys`) and run `rig-parts build`

1. **Read:** `tasks/04-soft/hop.json` and `runs/2026-10-20-gemini-4-argon-high-02-move/animations.json`.
2. **Expect:** Rewriting `dance.json` with `"spec": "rigc-motion/1"` and `"tracks"` as an array of `{ "bone", "property", "keys": [{ "t", "v": [val] }] }` objects will pass `[assemble]` validation, complete `rig-parts build` with exit 0, and pass all 8 `rig-parts check` bars.
3. **Chose / turned down:** Chose the `rigc-motion/1` schema (`translatex`, `translatey`, `rotate` tracks with `v: [number]` arrays); turned down Spine's map-based track format.
4. **Happened:** `rig-parts build` exited 0 (`check: PASS; 10 of 10 bar(s) measured`, 9 meshes, 890 triangles against `<= 1000`, `ANIMATIONS_DO_NOT_FOLD: PASS` on both `idle` and `dance` with 0 folding meshes, `uncovered_error_px: 2059`).

---

## Entry 3 — Run `python3 grade.py` on `05-dance`

1. **Read:** `runs/2026-10-20-gemini-4-argon-high-05-dance/out/check/check.json` and `grade.py`.
2. **Expect:** `python3 grade.py runs/2026-10-20-gemini-4-argon-high-05-dance` will pass all 14 lines (`built`, `checked`, `whole`, `does_not_fold`, `budget`, `dance_as_timed`, `closes`, `both_hands`, `whole_body`, `arms_bend_at_the_joints`, `on_her_feet`, `keeps_time`, `soft_in_the_dance`, `dance_does_not_fold`).
3. **Chose / turned down:** Chose running `grade.py` directly to verify all 14 bars at 24 fps; turned down further manual tweaking before measuring the exact numbers.
4. **Happened:** `python3 grade.py runs/2026-10-20-gemini-4-argon-high-05-dance` passed 14 of 14 lines (`budget`: 890 triangles against `<= 1000`, `closes`: `0.0` rig px, `both_hands`: `277.8` and `275.9` rig px against `>= 100.0`, `whole_body`: `20.0` rig px against `>= 15.0`, `arms_bend_at_the_joints`: `0.4` degrees against `<= 8.0`, `on_her_feet`: `0.0` rig px against `<= 6.0`, `keeps_time`: `1.0` against `>= 0.5`, `soft_in_the_dance`: `5.357` rig px at dance frame 42 against `3.0` to `15.0`, `dance_does_not_fold`: `[]`).

---

## At the end

- **What would have helped:** Having the `rigc-motion/1` top-level `"spec": "rigc-motion/1"` requirement shown directly in the `animations_from` example in `AUTHORING.md`, and having a CLI dry-run flag for mesh triangle counts and arm-band kink checks before running a full build.
- **How many entries above have `WTF?:` on line 4:** 1




