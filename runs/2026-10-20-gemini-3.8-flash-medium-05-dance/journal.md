# Journal — gemini-3.8-flash-medium, 05-dance, 2026-10-20

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry 1

1. **Read:** `tasks/05-dance/TASK.md` (120 bpm, 4.0 s duration, hands >= 100 px, body >= 15 px, keeps time >= 0.5).
2. **Expect:** `dance.json` created with 4.0 s `dance` animation holding 1.0 s (2 beats) periodic tracks on `hip`, arms, and `head`.
3. **Chose / turned down:** Authored a 4.0 s dance looping every 1.0 s (2 beats) to maximize `keeps_time` power and ensure loop closure; turned down a non-rhythmic motion.
4. **Happened:** Created `dance.json` with 4.0 s dance animation containing 7 rhythmic tracks looping on a 1.0 s period.

## Entry 2

1. **Read:** `tasks/05-dance/TASK.md` ("legs are one flat piece that hangs from the hip and her shoes are another that sits on the ground: move the hip and the two come apart", "On her feet: stays within 6 rig px") and `node_modules/@rig-c/parts/docs/AUTHORING.md` §3 (target bones parented to `root`, mesh segments).
2. **Expect:** `config.json` authored with new `feet` bone under `root`, `legwear` converted from region to mesh bound between `hip` and `feet`, maintaining triangle budget <= 1000.
3. **Chose / turned down:** Added `feet` bone under `root` at ankle level and meshed `legwear` across `hip` and `feet` so leg bottoms stay pinned to `shoes`; turned down leaving `legwear` on `hip` which fails `on_her_feet`.
4. **Happened:** Created `config.json` with `feet` bone under `root`, `legwear` converted to mesh with `hip` and `feet` segments, and `dance.json` linked.

## Entry 3

1. **Read:** `grade.py` lines 264-296 and `tasks/05-dance/TASK.md` Pass lines.
2. **Expect:** `python3 grade.py runs/2026-10-20-gemini-3.8-flash-medium-05-dance` runs build and checks all dance pass lines.
3. **Chose / turned down:** Running `grade.py` to evaluate the dance animation and rig structure.
4. **Happened:** WTF?: Expected rig-parts build exit 0, but rigc failed compilation with "key times must strictly increase (at t=1)" on sleeve_l0 rotate because the pattern included t=1.0 which duplicated cycle 1's t=1.0 start.

## Entry 4

1. **Read:** `grade.log` line 63: `animation "dance" bone "sleeve_l0" rotate: key times must strictly increase (at t=1)`.
2. **Expect:** `dance.json` regenerated with strictly increasing key timestamps across all 7 tracks, closing at exactly t=4.0.
3. **Chose / turned down:** Removed redundant cycle boundary keys from the 1.0 s pattern definitions so times strictly increase; turned down non-periodic keys.
4. **Happened:** Regenerated `dance.json` with strictly increasing key times across all tracks, verified by programmatic monotonicity check.

## Entry 5

1. **Read:** `tasks/05-dance/TASK.md` Pass lines and `grade.py` lines 264-296.
2. **Expect:** `python3 grade.py runs/2026-10-20-gemini-3.8-flash-medium-05-dance` compiles cleanly and passes all dance grading criteria.
3. **Chose / turned down:** Running `grade.py` to grade the dance with non-overlapping keys.
4. **Happened:** WTF?: Expected all lines to pass, but arms_bend_at_the_joints failed with 9.2 degrees against <= 8.0 (1.2 degrees over) due to skinning blend kink at 55 deg / 30 deg arm swing, while all other 13 lines passed (both_hands 507 px, on_her_feet 2.72 px, keeps_time 1.0).

## Entry 6

1. **Read:** `grade.py` output (`arms_bend_at_the_joints: 9.2 deg vs <= 8.0 deg`) and `both_hands` reading (507 px vs >= 100 px required).
2. **Expect:** Lowering arm rotation angles (`sleeve_*0` to ±32 deg, `sleeve_*1` to ±16 deg) brings limb bending below 8.0 deg while still exceeding 100 px hand travel.
3. **Chose / turned down:** Moderated arm rotation angles in `dance.json`; turned down removing arm motion which would fail `both_hands`.
4. **Happened:** Updated `dance.json` with moderated arm rotations (`sleeve_*0`: ±32 deg, `sleeve_*1`: ±16 deg).

## Entry 7

1. **Read:** `tasks/05-dance/TASK.md` Pass lines and `grade.py` lines 264-296.
2. **Expect:** `python3 grade.py runs/2026-10-20-gemini-3.8-flash-medium-05-dance` passes all 14 lines cleanly.
3. **Chose / turned down:** Re-grading the moderated dance animation to verify all pass lines.
4. **Happened:** python3 grade.py passed all 14 of 14 lines (arms bend: 5.3 deg <= 8.0; hands: 305 px / 303 px; keeps_time: 1.0; on_her_feet: 2.72 px).

## At the end

- **Where I guessed:** Arm rotation limits (reduced from 55/30 to 32/16 deg) to prevent skinning blend kink at elbow while preserving > 100 px hand travel.
- **What I could not find:** Direct documentation predicting limb vertex bending angle threshold from joint rotation angles under dual-segment skinning.
