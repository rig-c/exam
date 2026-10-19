# Journal — claude-opus-5-5, Advanced R2 (run), 2026-10-19

Model name: the prompt that started this sitting did not write a model identifier; `claude-opus-5-5` is the exact model ID this session's environment gives (see "Where I guessed").

## Entry 1

1. **Read:** PROMPT/the starting message, "Set up": "Run: npm install".
2. **Expect:** exit 0, rig-c 2.59.0, @rig-c/pose 0.31.1, @rig-c/parts 1.35.0 under node_modules.
3. **Chose / turned down:** npm install as told; bun install turned down (the prompt says npm).
4. **Happened:** exit 0, "found 0 vulnerabilities"; the three packages are there. (Lines 1–3 of this entry were written after the step: I ran it before opening the journal, as the set-up order put it before PROBLEM.md.) @rig-c/pose has no `docs/` folder, so its README is its only document (505 lines, some lines several KB long).

## Entry 2

1. **Read:** @rig-c/pose README "The map: `rig-pose-map/1`" (pelvis `"aim": ["leg_r0>leg_l0"]`, trunk with `reach: true`, head by eye line, arms `"free"` per the ⚠️ note, legs `"free"` per the dance-b note) and "The legs: foreshortening and planted feet" (`--leg-scale 0.8,1.05` the card's range, `--stance 0.07` the card's, `--plant-feet`, in-place loop closure). PROBLEM.md: render geometry at the sequence's rate (30 fps).
2. **Expect:** `run/map.json` written; `rig-pose retarget` exits 0 with gate green, every bone landing, FEET listing two jumps per cycle near 4–9 and 14–19; then `rigc build` exit 0 and `rigc render --fps 30 --geometry --folds --pass-through …` writes geometry.json/folds.json/pass-through.json; grader prints 14 rows, I expect several FAILs (hip vertical range: translate scale is torso-based, rig torso/leg proportion ≠ sequence's: rig 360/485 vs seq 202/399).
3. **Chose / turned down:** baseline with the README's own "card" settings and torso scale as the README example; turned down picking a leg-based scale up front, to measure first.
4. **Happened:** retarget exit 0, gate green, every bone lands (worst 0.16 of tolerance), FEET jumps 3–9 · 13–19 per cycle (within ±1 of the sheet). `rigc build --rig inputs/rig` then exited 1: WTF?: "cannot read …/inputs/rig: EISDIR" (`CE_COMPILE_JSON_READ_FAILED`) — `retarget --rig` takes a directory, `rigc build --rig` wants the rig.json file; nothing told me the two `--rig`s differ. Re-ran with `inputs/rig/rig.json`: exit 0; render exit 0. Grader: 8 PASS, 6 FAIL — two-feet (lift ratio 1.281), jitter trunk+head 1.387×, folds 16 frames (bottomwear), hip vertical 1.460, hip horizontal 1.712, rebound 1.929. Hip vertical 1.46 is exactly the SCALE (1.781) over the leg ratio (485/399 = 1.216), as I predicted. Next: a leg-proportioned translate scale.

## Entry 3

1. **Read:** README "The map": "`translate.scale` is one length measured on both … its median over the frames where both are good. Pick a long segment that does not foreshorten much." Grader baseline: hip vertical 1.460 = SCALE 1.781 ÷ (485/399).
2. **Expect:** with `scale` on the right leg (`r_hip→r_ankle` / `leg_r0→foot_r`) SCALE ≈ 485/median(hip→ankle) — the README's median, not the grader's p95, so ≈ 1.5 (FEET says the median leg is 303 px): hip vertical falls toward ~1.2, not into the band; horizontal still over. I expect this to show the scale's leverage, not to pass.
3. **Chose / turned down:** a leg segment, as the rows are in leg lengths; turned down editing the rig's proportions first (art and pass-through would move).
4. **Happened:** WTF?: SCALE 1.600 (rig 485.19 / pose median 303.15), as expected; grader 9 PASS / 5 FAIL — and folds went to 0 (16 before), which I did not expect: a lower scale moved the bottomwear off its folding frames. Hip vertical 1.324, horizontal 1.533, rebound 1.757 all fell ~in proportion to the scale; the two-feet lift ratio stayed 1.284, so it does not depend on the scale. Trunk+head jitter got worse (1.482). Reading: scale ∈ ~[1.03, 1.20] would put vertical, horizontal and rebound in band if they stay linear; lift needs something else (I suspect the 0.8 leg-scale floor holding a heel-kicked shin long, so the foot is drawn higher than the picture's).

## Entry 4

1. **Read:** my per-bone split of the trunk jitter (run/jitter_by_bone.py on try_leg's geometry): hip 1.000×, chest 2.197×, head 1.324×. README "The map": `reach` aims the chest "from where its origin is posed — the hip moved and turned"; without it the trunk is "parallel to the pose's". Translate scale: shoulder width (rig sleeve_r0→sleeve_l0 152 units, picture ≈141 px), a segment that does not foreshorten in a face-on run.
2. **Expect:** chest jitter ratio ≈ 1.0, so trunk+head ≈ (1.4+1.5+3.4)/(1.4+1.5+2.6) ≈ 1.1 — marginal, the head still over; SCALE ≈ 1.08: hip vertical ≈ 0.89, horizontal ≈ 1.03, rebound ≈ 1.19 if linear; lift ratio still ≈ 1.28 (FAIL); folds may come back.
3. **Chose / turned down:** shoulder width over hip width (hip width gives 1.018, just under the vertical band's 1.03 by my linear estimate); turned down a hand-tuned scale since the map takes only points.
4. **Happened:** WTF?: better than expected — 13 PASS / 1 FAIL. SCALE 1.0759; hip vertical 0.928, horizontal 1.059, rebound 1.257 (my linear estimates held), folds 0. Trunk+head jitter 1.000× with the head at 1.000× too: I expected the head to stay ~1.32×; its excess was not its own — the head is measured against the chest, and the reach-aimed chest was what moved. Only two-feet fails: lift ratio 1.294 (bar 0.85–1.15).

## Entry 5

1. **Read:** run/lift.py on try_v4: rig/seq lift per grounded frame 0.32, 1.20, 1.06 (left lifted, frames 0–2) and 1.41, 1.38, 1.61 (right lifted, 10–12). The retarget's LEG-SCALE lines: `leg_r1` "picture length ÷ straight 0.089 … 1.036", "110 frame(s) under 0.8, clamped (frames 5–15 …)"; in the picture on frame 10 the right ankle (452,684) is above its knee (460,741): a heel kicked up behind, the shin foreshortened to ~0.1 and pointing up. README "--leg-scale <min,max>": "clamped to [min, max]", bounds `0 < min ≤ 1 ≤ max`.
2. **Expect:** with `--leg-scale 0.05,1.05` the shin is keyed at its picture length, the lifted foot comes down to the picture's height: ratio median ≈ 1.0; risk: folds/pass-through from shins scaled to ~0.1 (SHEAR), and hip vertical/rebound move since the support leg can now shorten below 0.8 (asked 0.678 on the thigh).
3. **Chose / turned down:** lower the floor of the clamp; turned down editing `--stance` (the bar says it does not move the bar and no grounded frame is within 0.07) and turned down the map (the lift comes from the scale clamp).
4. **Happened:** Lift ratio 0.966 (per frame 0.95–1.00), as expected; folds 0 and pass-through 0 — the risk did not land; hip vertical/horizontal/rebound unchanged (0.928 / 1.059 / 1.257), which I had flagged as a risk and did not happen (the hip is set by the plant, and the support leg was not the clamped one on grounded frames). Grader: RESULT PASS (14/14). Next: look at the frames beside the stick video before believing it.

## Entry 6

1. **Read:** try_v5 retarget `SHEAR bone "foot_r": art sheared up to 78.08° … y axis 0.169 … 1.036 of setup`; evidence sheet run/evidence/sheet_v5_cycle2.png: on frames 48–52 the kicked-up foot is a squashed red blob at the knee. rig-c docs/AUTHORING.md `inherit` row: `normal · onlyTranslation · noRotationOrReflection · noScale · noScaleOrReflection`. README "--leg-scale": a bone under a `normal` child is "squashed along the shin: SHEAR reads both".
2. **Expect:** copy of the rig (run/rig_v6) with `foot_r`/`foot_l` `inherit: "onlyTranslation"` (they were `noRotationOrReflection`, which still takes the shin's scale/shear): SHEAR on the feet ≈ 0°, feet drawn whole; the foot's world position is the shin tip either way, so all 14 rows unchanged; folds stay 0.
3. **Chose / turned down:** `onlyTranslation` (no rotation, no scale) over `noScale` (that would let the foot turn with the shin, which the rig's author chose not to); turned down leaving it, since the proctor looks at the frames.
4. **Happened:** Feet SHEAR 0.00° both sides; sheet_v6_cycle2.png shows whole boots on the kicked-up legs; grader still 14/14 with every figure identical to try_v5 (foot positions are the shin tips, as expected). Kept as the final.

## At the end

- **Where I guessed:**
  - The model name `claude-opus-5-5`: the starting message had no `<MODEL>` filled in; I took the session environment's model ID. Needed: the name the person wrote.
  - `--trunk hip,chest,head` for the grader: my reading of "trunk and head bones"; the pelvis bone `hip` is keyed by the pelvis chain and I counted it as trunk. Needed: a sentence saying whether the pelvis bone is trunk or limb.
  - `--leg-scale 0.05,1.05`: 0.05 is a round value under the lowest asked scale (0.089); no document gives a floor for a run, only the walk card's 0.8,1.05.
  - `--stance 0.07`: the card's value; on this sequence it plants nothing (no grounded frame is within it), so it is inert.
  - Translate scale on shoulder width: chosen because the README's "a long segment that does not foreshorten much" plus the rows' units (leg lengths vertically, hip widths horizontally) left a window, and shoulder width fell in it; a leg segment would be the obvious reading and fails (its median is folded in a run).
- **What I could not find:**
  - Which length the translate scale should be when the rig's proportions differ from the subject's (rig torso/leg 0.74, subject 0.51): nothing says the hip rows depend on it.
  - Why `reach: true` (which the README recommends for a tilting pelvis) doubles the chest's rotation jitter, and when not to use it.
  - That `rigc build --rig` needs the rig.json file while `rig-pose retarget --rig` takes the directory.
