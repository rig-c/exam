# Journal — claude-opus-5-5, Advanced R3 (dance), 2026-10-19

(Model name: the prompt this session was given did not fill a `<MODEL>` value; I use the session's model id, claude-opus-5-5.)

## Entry 1

1. **Read:** @rig-c/pose README "The map: `rig-pose-map/1`" (chains, `aim` "a>b" for pelvis/head, `reach: true` trunk, bend ⚠️ "for front-facing material, arms go `"free"` … Leave legs `"free"`"), "What it does" (`face` dials), rig.json (bones hip, chest, head, sleeve_*, leg_*, foot_*, yaw_dial/pitch_dial sliders ±30/±25).
2. **Expect:** `run/map.json` written; first retarget (plain, `--camera`, no plant) exits 0, gate green, every bone lands; it writes motion, build, report, camera.json.
3. **Chose / turned down:** pelvis chain on `hip` (r_hip→l_hip, aim `leg_r0>leg_l0`) so the hip tilt row has a turning thigh-root line; trunk `chest` with `reach` to `sleeve_r0+sleeve_l0`; head by eye line; arms/legs `free`. translate scale mid_hip→neck vs rig hip→neck. Face yaw/pitch on the dials with the sliders' own ranges. Turned down: mapping `neck` bone — the pose's neck joint is the shoulders' midpoint, not a neck segment.
4. **Happened:** exit 0. Gate green (52 assertions, 24 measured, 0 failed), all 13 angle landings + hip origin within tolerance; `FEET` read 5 supports, 3 jumps 88–91 · 179–181 · 267–269 (the canonical spans) without `--plant-feet`; posed build: lowest ankle vertical range 0.142 leg lengths, worst support drift 0.105 — so support/slide/floor will fail until feet are planted. POSTURE tilt 1.000. Matched. Next: build + render geometry for the before table.

## Entry 2

1. **Read:** grade.py docstring ("--build the stdout of the final `rigc build`", "render with --fps 24"), `rigc --help` (render `--geometry`, `--folds`, `--pass-through`).
2. **Expect:** `rigc build` exits 0 with a "N assertions: … (… 0 failed)" line; `rigc render --animation dance --fps 24 --geometry --folds --pass-through …` writes geometry.json, folds.json, a pass-through reading; grader prints 13 rows, several FAIL (support foot, slide, floor).
3. **Chose / turned down:** build from inputs/rig + the retarget's motion.json into run/before/; turned down grading the retarget's own `--build` dir (the grader wants a separate build's stdout).
4. **Happened:** WTF?: the first `rigc build --rig inputs/rig` died with `EISDIR … (see rigc guide CE_COMPILE_JSON_READ_FAILED)` — retarget takes a rig directory, rigc build wants the rig.json file; rerun with `inputs/rig/rig.json` exited 0 (52 assertions, 0 failed). Render wrote geometry/folds/pass-through. Grader: 6 pass, 7 fail — support foot 0.0741, two feet 0.0873 / lift 0.217, slide 0.0223, floor 0.0547, jitter limbs 1.160 / trunk+head 1.664, hip vertical 0.265, rebound 0.647. Expected the feet rows to fail; did NOT expect jitter to fail on a straight per-frame retarget, least of all trunk+head at 1.66×. Next: find which bone drives the jitter.

## Entry 3

1. **Read:** my per-bone breakdown of grade.py's jitter row (scratch script calling its own functions on run/before): hip 1.000, legs 1.000, forearms 1.000, but chest 2.03×, head 2.28×, upper arms 1.7–1.9× — every child of `chest`. README map bullet: `reach: true` aims the trunk "from where its origin is posed — the hip moved and turned"; grade.py `row_jitter` compares the bone's local angle with the map pair's angle less its keyed parent's pair.
2. **Expect:** without `reach`, chest's world angle is the mid_hip→mid_shoulder angle exactly, so chest/upper-arm/head local angles equal the sequence's local ones and trunk+head jitter drops to ≈1.0–1.2× (head may keep extra from the face pitch coupling); limbs ≈1.0×.
3. **Chose / turned down:** drop `reach` from the trunk chain (aim stays the shoulders' midpoint). Turned down: moving chest_ctl's origin onto the hip pivot in the rig spec — bigger change, and the README itself says reach is what pulls the trunk off the pose's angle; try the map first.
4. **Happened:** jitter now limbs 1.000×, trunk+head 1.060× — PASS, as expected (head keeps a little from the face coupling/eye line vs chest). Cost: POSTURE sway rig/reference went 0.959 → 1.268 (the trunk no longer reaches the shoulders over a tilted pelvis). Feet rows unchanged. Next: plant the feet.

## Entry 4

1. **Read:** README "The legs: foreshortening and planted feet": `--leg-scale` ("0.8,1.05 is the card's range"), `--plant-feet` (one floor #85, jumps release the plant), `--stance` ("0.07 is the card's").
2. **Expect:** support foot, slide and floor rows drop under 0.01 / 0.005 / 0.01; two-foot frames ≤ 0.02 with stance; hip vertical rises toward 1.0 because the legs foreshorten instead of the feet lifting; jumps still 3.
3. **Chose / turned down:** all three at the documented card values in one run. Turned down: adding them one at a time — the README presents them as one configuration measured on `dance-a`.
4. **Happened:** 12 of 13 PASS: support foot 0.0000, slide 0.00003, floor 0.0000, hip vertical 1.049, rebound 1.334, airborne 3 spans (min peak 0.0245). WTF?: two feet FAILS the other way — all 35 lifted frames have the rig's lifted foot planted (lift −0.0000, median ratio −0.000). The card's `--stance 0.07` plants anything within 0.07 leg lengths, but the table calls a frame lifted past 0.04 Ls; nothing in the README warned that 0.07 is wider than the grader's lift band — and STANCE's leg length is FEET's median hip→ankle (608–613 px), not the grader's 95th-percentile Ls (722 px).

## Entry 5

1. **Read:** README `--stance` bullet ("tolerance is a distance … in the free side's leg length — the leg length `FEET` uses"; hysteresis "planted again only under 0.8 of it"; a change "takes effect only when its condition holds for 0.1 s"); report.feet.legLength r 608.6 / l 613.1 px; my listing of the sequence's ankle gap: the 35 lifted frames are 278–312 only (0.049–0.069 in FEET's leg length), two-foot frames ≤ 0.0237 in FEET's leg length; frames 272–277 run 0.030–0.047.
2. **Expect:** `--stance 0.03`: two-foot frames stay planted (≤ 0.0237 < 0.03, and 0.8 × 0.03 = 0.024 still above them), 272 onwards leaves the stance (0.0301 > 0.03 and stays over it for > 0.1 s), so 278–312 keep the pose's lift; two-feet row passes with a median lift ratio near 1 (the leg-scaled leg reproduces the picture's height). Other rows unchanged.
3. **Chose / turned down:** 0.03, converted from the grader's bands into FEET's leg length. Turned down 0.04 (the table's number) — in FEET's units 0.04 Ls is 0.047, and frame 278 (0.049) would be planted for the 0.1 s the state change needs.
4. **Happened:** 13 of 13 PASS. Two feet: two-foot max 0.0000, lifted 0 of 35 planted (lowest lift 0.0390 at 278), median lift ratio 0.933. Every other row identical to entry 4. Matched. Next: copy v4 into run/after, make evidence frames beside the stick video.

## Entry 6

1. **Read:** PROBLEM.md "Run directory" (`after/` motion · build · render; `after/camera.json`), "Measure" (evidence frames side by side with the stick video); `rigc render --help` (`--max`, `--viewport-from`).
2. **Expect:** run/after holds v4's motion.json, report.json, camera.json, build/, build.stdout, render/; a grade of run/after prints the same 13 PASS; run/evidence gets 7 PNGs (stick | before | after) at frames 20, 89, 150, 180, 230, 268, 295.
3. **Chose / turned down:** copy v4 rather than re-run (same bytes); extra renders at `--max 640` on one shared viewport for the pictures only (geometry stays the 24 fps render). Turned down re-running the whole pipeline into after/ — identical inputs.
4. **Happened:** WTF?: the first composite command failed — this ffmpeg has no `drawtext` filter ("No such filter: 'drawtext'"); dropped the label and put frame + column order in the file names; 7 PNGs written. (Also the transcript wrapper choked on parentheses in my cp line; the copy ran, I noted it by hand.) Looking at the pictures: after-frames 150 and 295 stand on one floor with both soles level and the lifted foot lifted at 295; before-150 floats one shoe. But at 295 the after render shows the knee art pulled apart (thigh/shin seams visible under the shin's scalex) — a visual cost of `--leg-scale` the table does not read.

## Entry 7

1. **Read:** my own report.md draft against run/v3/retarget.stdout (full `grep '^  STANCE'`).
2. **Expect:** the v3 STANCE lines list only planted-both runs and never the 272–312 lifted foot, as my report claims.
3. **Chose / turned down:** re-read the raw output before keeping a "the tool did not say" claim, rather than trusting the earlier `grep … | head` view.
4. **Happened:** WTF?: v3 DID print `STANCE planted both: free foot r frames 272–312 … up to 0.0687 leg lengths … within the tolerance 0.07`. My earlier pipeline (`grep … | head -30`) had cut it off and I read one line as the whole. Report bullet struck through and corrected, left in place.

## At the end

- **Where I guessed:** the model name (the prompt's `<MODEL>` was not filled; I used the session's model id). `--stance 0.03` is derived, not read: the table's bands converted into FEET's leg length from `feet.legLength` and the sequence's ankle gaps. `--trunk hip,chest,head` for the grader: I counted the pelvis bone as trunk; PROBLEM.md names "trunk · head" without listing bones. The evidence frame numbers (20, 89, 150, 180, 230, 268, 295) are my picks.
- **What I could not find:** a stated leg-length unit for `--stance` in px; whether `--trunk` should include the pelvis bone; any figure in the docs for how much `reach` adds to the trunk's jitter.
