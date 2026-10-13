# Journal — Fable 5.1, dancing-rig polish (1회차), 2026-10-13

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry 1 — install the three packages

1. **Read:** PROBLEM.md §도구 — "`package.json`에 버전을 고정해 두었다. 이 폴더에서 `npm install` 또는 `bun install`을 실행한다."
2. **Expect:** exit 0, `node_modules/rig-c`, `node_modules/@rig-c/parts`, `node_modules/@rig-c/pose` present, `bunx rigc --help` prints usage.
3. **Chose / turned down:** `bun install` (faster, bun ≥1.2 is already the stated runtime). Turned down `npm install` only because bun is what rigc itself runs on.
4. **Happened:**
`bun install` exit 0, 6 packages (rig-c 2.51.1, @rig-c/parts 1.17.0, @rig-c/pose 0.6.0 + ag-psd, base64-js, pako). `bunx rigc --help` prints the usage table. As expected.

## Entry 2 — render the given build at 24 fps for frame-by-frame evidence

1. **Read:** `rigc render --help` — `--fps`, `--max`, `--geometry` ("per frame, every bone's world transform and every slot's region or mesh vertices"), `--folds`; PROBLEM.md §해야 할 것 1 asks for 영상 | 리그 side-by-side evidence frames per finding, and `inputs/dance/clip-audio.mp4` is only 480 px tall.
2. **Expect:** exit 0; `run/evidence/_work/render_before/` with 313 frame PNGs (13 s × 24 fps, +1 maybe), `frames.json`, `geometry.json`, a `poser` line saying `core` (skeleton.model.json is beside the pair). ≥ 1 min.
3. **Chose / turned down:** render myself at `--max 960 --fps 24 --geometry --folds` so I can measure (feet y, knee angles, skirt bone angles) rather than eyeball. Turned down cropping frames out of the given clip: too small, and no geometry.
4. **Happened:**
exit 0 (no error lines in the log); `run/evidence/_work/render_before/dance@24fps/` has 313 frames at 754×960, poser line: `rigc core — …/skeleton.model.json`. As expected.

## Entry 3 — baseline rebuild of the given rig + motion (to learn the build cost and confirm the gate is green before I touch anything)

1. **Read:** `rigc build --help` (`--rig`, `--motion`, `--out`, `--report`); `inputs/dance/run.txt` GATE line: "51 assertions: 19 measured (19 passed, 0 failed), 16 skipped, 16 not in profile 'spine'"; rig.json `"images": "images"` (relative to rig.json, so `inputs/rig/images`).
2. **Expect:** exit 0, same GATE figures as run.txt (19/0/16/16 + A00 SKIP naming spine-core since the install has no spine-core), `skeleton.json` byte-identical to `inputs/dance/build/skeleton.json` (A18 determinism — same inputs, same version 2.51.1), under 2 minutes.
3. **Chose / turned down:** build into `run/evidence/_work/build_baseline` with `--report`. Turned down skipping this: every later fix is judged against "did the gate stay green and did only the intended bytes move", and I need the baseline bytes from *this* install, not the ones shipped.
4. **Happened:**
`bun x rigc build` exit 0 in 11.1 s wall. WTF?: the gate line reads "52 assertions: 21 measured (21 passed, 0 failed), 17 skipped, 14 not in profile" where run.txt said 51/19/16/16 — run.txt's figures were printed by rig-pose's own run (an older rigc through @rig-c/pose, or a different entry); nothing told me the two entries count differently. Also not byte-identical: the shipped skeleton.json differs only in `skeleton.images` ("../build/" — it was written with `--copy-images`) and the atlas in its page paths; JSON-equal otherwise (checked by parsing both and erasing that one field). So determinism holds; my expectation about `--copy-images` was the miss.
   **Correction (same entry, minutes later):** "JSON-equal otherwise" above was wrong — I wrote it before the parse-and-compare printed. The parsed documents differ in 1,363 places, all of them the per-vertex bone order inside weighted mesh `vertices` arrays (bottomwear, shins, …): the same bones and weights, listed in a different order. That is what rig-c 2.51.1's own changelog entry (#1407, "a weighted attachment is written in one bone order") changes, so the shipped build came from an earlier rigc. Not a determinism break; a version difference I had no way to see from run.txt (it prints no rigc version).

## Entry 4 — physics trial 1: loosen the skirt springs (and give the back hair one)

1. **Read:** AUTHORING §4.6 — `inertia`, `strength`, `damping` ∈ [0,1] ("1 never decays"), `mass`, `mix`; §3.5 "A physics constraint's five components all default to 0" (so `rotate: 1` stays). Measured before (geometry.json of the given build): `skirt_c2 − hip` range 21.9° over the clip, 13.6° in the K1 sway (f95–175), 5.0° in jump 1 — with inertia 0.15 / strength 250 / damping 0.93 the hem barely leaves the hip's own tilt. The video's hem swings visibly to one side on every sway beat (sheet_before_04/05/08: f102, f111, f123, f204, f210).
2. **Expect:** gate green (same figures as entry 3); `skirt_c2 − hip` range in K1 ≥ 30° and over the clip ≥ 40°, no runaway (A23 would refuse damping > 1; I stay at 0.85); jump 1 range ≥ 15°.
3. **Chose / turned down:** skirt rows: inertia 0.5 / 0.6 / 0.7 (root → hem), strength 120 / 90 / 60, damping 0.85. Plus one new `physics` on `bun` (rotate 1, inertia 0.4, strength 150, damping 0.85) so the back hair follows the jumps. Turned down `wind`/`gravity` (the swing I want comes from the hip's motion, not a steady force) and turned down a `physics` timeline in the motion (a rest value is enough for a first reading). Render at 12 fps / 480 px for the measurement only — half the frames, same metric.
4. **Happened:**
build exit 0 (52/21/0/17/14), render exit 0 — but WTF?: `skirt_c2 − hip` range is **130.7°** over the clip (K1 87.8°, K2 130.7°, jump 1 20.3°), four times the 30–40° I asked for; the contact sheet shows the hem flung sideways past horizontal through the K2 sway (frames 104–119 of the 12 fps sheet). I read inertia as "how much it follows" and guessed a middle value; nothing in §4.6 gives a scale for what 0.5 vs 0.15 does to a 54-unit chain, so the first trial was a blind shot and it overshot. The 12 fps render also lands in `render_physA/dance/`, not `dance@12fps/` — the suffix is only added when `--fps` differs from the default 12 (unstated; read off the output line). Bun−head swing 15.8°: fine.

## Entry 5 — physics trial 2: back off toward the original

1. **Read:** entry 4's numbers: inertia 0.15 / strength 250 → 13.6° in K1; inertia 0.5–0.7 / strength 60–120 → 87.8°. The amplitude is roughly linear in inertia / strength, so the target ≈ 35° in K1 sits near inertia 0.3 with strength ~180.
2. **Expect:** gate green; K1 `skirt_c2 − hip` range 25–45°, full clip ≤ 60°, hem never past ±60° from the hip's down axis (i.e. c2−hip within [−150, −30]).
3. **Chose / turned down:** inertia 0.3 / 0.35 / 0.4, strength 200 / 170 / 140, damping 0.82 (a little less carry-over than 0.85 so the K2 whip settles between beats). Bun unchanged. Turned down keeping damping at 0.85: the K2 whip in trial 1 built up over consecutive beats, which is what damping governs.
4. **Happened:**
build exit 0 (52/21/0/17/14), render exit 0. `skirt_c2 − hip`: K1 41.0° (asked 25–45 ✓), full clip 64.6° (asked ≤ 60 — 4.6° over, from one K2 beat), span [−122.0, −57.5] (asked within [−150, −30] ✓), jump 1 24.0°, jump 2 30.1°. Close enough to the mark on the first correction; accepted as the rig fix. Linear-in-inertia/strength was a usable model.

## Entry 6 — motion post-process: plant the feet, add blinks and breath (run/after/post_motion.py → run/after/dance/motion.json)

1. **Read:** @rig-c/pose README "What 0.1.0 does not do: Plant feet beyond what the pose gives"; geometry.json of the given build — min(foot_r.y, foot_l.y) runs 100.1 … 186.9 units over the clip (rest ≈ 149) while the hip is the only translated bone; AUTHORING §4.4 (`group` + `scaley` for the eyes, `translatey` on `chest_ctl`), §4.5 (`t` strictly increasing, a key on the last sample = the duration's own value, `curve` times are absolute so a tiled idle key must shift them); the idle animation's own blink (`eyes` scaley 1 → 0.12 with eases `shut`/`open`, 0.31 s) and breath (`chest_ctl` translatey 0 … 5.02, 3.33 s period); the eye-crop sheet of the video (run/evidence/_work/eyes_sheet.png): eyes shut around f18–22, f144–155, f170–175, f256–259.
2. **Expect:** script exit 0; new dance has 3 more tracks (`eyes` scaley, `brows` translatey, `chest_ctl` translatey) + the hip translate y rewritten; build green with the same gate figures; in the rebuilt geometry min-foot-y = rest value ± 0.5 on every frame I mark grounded, and above it only on the three hops (≈ f86–93, f176–182, f266–273).
3. **Chose / turned down:** dy = restFootY − minFootY per frame, added to the hip's translate y; a frame is airborne when the pose's two ankles are both ≥ 25 px above their own 25-frame rolling median, and there I hold the last grounded dy so the hop height stays the pose's. Turned down smoothing dy (the per-frame keys already carry the pose's smoothing) and turned down planting *both* feet (only the lower one can be on the floor in a 2D rig). Blinks at the four video times; breath = idle's chest_ctl track tiled 4× and cut at 13 s.
4. **Happened:**
script exit 0, but WTF?: **airborne frames 0** — my 25 px threshold was a number I made up; the three hops lift the ankles only 10–28 px in the picture (rolling-median rise, 12-frame window: f88–90 r 17/25/12, l 17/16/11; f178–180 r 19/13/16, l 13/9/18; f267–269 r 16/27/28, l 19/17/15), three frames each. Nothing in the inputs gave the hop height; I should have read it off the pose before writing the threshold. Re-run with 8 px (both ankles) and the same window.
   Re-run: 15 airborne frames — f88–90, f178–180, f267–269 (the hops) plus f99–101 and f187–189 (a second, smaller bounce right after landing in the pose; kept, it is the pose's). Build exit 0 (52/21/0/17/14). In the rebuilt 24 fps geometry the lower foot sits at the rest height (152.8) on 298/313 frames and above it only on those 15 (max +28.4), never below. Skirt at 24 fps: c2−hip range 62.9° clip / 39.9° K1 (12 fps trial read 64.6 / 41.0 — the physics clock is the frame's, so the figure moves a little with the rate). As expected after the threshold fix.

## Entry 7 — retarget again with a `frames` window on K4 (map fix)

1. **Read:** pose README "A stopgap window: `frames`" — "it shows only inside those windows, and on them it is chosen over any set within tolerance that has no window"; run.txt SWITCH K4 frames 27–33 and END-ON sleeve_l0 frames 31–36; sheet_before_01: at f021–f026 the rig's left arm is drawn straight out sideways while the pose's upper arm is end-on (the hand is at the ear from ~f23), and at f034–f038 the base art comes back while the hand is still at the ear.
2. **Expect:** exit 0; SWITCH K4 frames 23–37 (or the README's sentence means tolerance still applies, in which case the line will still read 27–33 and I learn that); every other SWITCH span unchanged; gate green; landing lines unchanged.
3. **Chose / turned down:** `"frames": [[23, 37]]` on K4, same retarget flags as run.txt (min-score 0.3, smooth 7, flip 90, short 0.35, bends clamp), `--rig run/after/rig` (the tuned physics) so the gated build is the one I ship. Turned down a `turn` change or a wider switch tolerance: both would move every set, this moves one span.
4. **Happened:**
WTF?: exit 1 before any retarget — three refusals on the pose file itself: `POSE_SPEC` ("rig-c-pose-frames/0"; this reader reads "rig-pose-sequence/1"), `POSE_SPACE` (units "painting-px", must be "picture-px"), `POSE_KEYS` (a key "fps" the reader does not know). The shipped `dance/` was retargeted from this very file, so whatever produced it ran a reader that took the older spelling; the 0.6.0 I installed does not, and PROBLEM.md's table calls the file `rig-c-pose-frames/0` as if that were current. Nothing told me the two names differ. Fix: a converted copy (`run/after/dance/pose.seq.json`: spec + units renamed, `fps` dropped; frames untouched) and run again — a second entry, same expectation.

## Entry 7b — the same retarget on the converted pose copy

1. **Read:** the three FAIL lines above; README "The pose: rig-pose-sequence/1" (spec, space, width, height, source, frames — no fps).
2. **Expect:** as entry 7: exit 0, SWITCH K4 23–37 or unchanged 27–33, other spans unchanged, gate green.
3. **Chose / turned down:** rename only; turned down editing `inputs/` (read-only by the problem's own layout).
4. **Happened:**
WTF?: exit 1 again, `RIG_GATE_BASE` → rigc compile error `image "hair_back.png" is not on disk at run/after/rig/images/…`. `rig-pose` has no `--images` (rigc build does, and I had been leaning on it), so a rig.json copied out of its images directory cannot be retargeted unless its `images` field is re-pointed. Set `"images": "../../../inputs/rig/images"` in run/after/rig/rig.json (rigc resolves it relative to the rig file) and run again. Expectation unchanged.
exit 0, gate green (52/21/0/17/14), but WTF?: SWITCH K4 still reads **frames 27–33** — the `frames` window changed nothing. So the README's "it shows only inside those windows, and on them it is chosen over any set within tolerance that has no window" means the window *restricts* and *breaks ties*; it does not admit a frame outside the 25° tolerance. The sentence never says that outright. Every rotate/attachment key of the new file is identical to the shipped motion (checked track by track), so the rewrite bought nothing — and the file carries only `dance` (the earlier run's "animations: idle, pose_…, dance" line came from a run that had the base motion; mine found no `motion.json` to merge even though I copied one beside rig.json — not investigated further, I use the shipped motion as the base instead). The K4 timing goes into the post-process as a key edit.

## Entry 8 — K4 earlier by hand: shift the switch-on key to f23 and bridge the left-arm keys (post_motion.py, step 2)

1. **Read:** entry 7b; the attachment tracks in the shipped dance (`upperarm_l_under` etc. key K4 at t=1.104165 = halfway between f26 and f27, back at 1.395835); pose README "A switch onto frame i is keyed halfway between frames i−1 and i"; AUTHORING §4.5 stepped keys "write a time a little below T".
2. **Expect:** the five K4 slot keys at 1.104165 move to (22.5/24) = 0.9375 (and the matching base-art `null`/`topwear` keys at that time); sleeve_l0 / sleeve_l1 rotate keys on f23–26 replaced by a straight line from f22's value to f27's; build green; in the new render f023–f026 show the K4 drawing instead of the straight arm.
3. **Chose / turned down:** a linear bridge over four frames (the pose's upper arm is end-on there, its direction is noise anyway). Turned down moving the switch-off (f33→37): the base forearm reads acceptably at f34–38 in sheet_before_01, and the K4 art would be turned ~20° past its drawn angle by f36.
4. **Happened:**
script: "K4 keys moved 10 -> t=0.9375" (5 K4-on keys + 5 base-off keys shared the time). Build into run/after/build (`--copy-images`) exit 0, 52/21/0/17/14. Render exit 0, 313 frames. Visual check pending in the sheets (entry 9 reads it).

## Entry 9 — the after clip: run/after/clip-audio.mp4

1. **Read:** ffprobe of inputs/dance/clip-audio.mp4: 648×480, 24 fps, 313 frames, aac audio 13.03 s; PROBLEM.md "왼쪽 영상, 오른쪽 리그, 음악 0초 맞춤".
2. **Expect:** ffmpeg exit 0; a 648×480, 24 fps, 313-frame mp4 with the audio track starting at 0; left 270 px = the reference scaled, right 378 px = the after render scaled to 480 high (377) + 1 px pad.
3. **Chose / turned down:** build it from `render_after` frames and the reference directly (no labels), audio = `inputs/reference/audio.mp3` with `-shortest`. Turned down re-using the labelled pair frames: the label would be in the deliverable.
4. **Happened:**
WTF?: ffmpeg exit 234 — `pad=378:480` refused: "Padded dimensions cannot be smaller than input dimensions" — `scale=-1:480` on a 754×960 frame rounds the width up to 378 (even), so there was nothing to pad. Use `scale=378:480` (a 1-px stretch) instead. Not run yet: entry 8's sheet first.
   And entry 8's own result, read in sheet_after_01: WTF?: f024 still shows the arm straight out sideways — now it is the **K4 drawing** turned ~50° off its painted angle, because my linear bridge walks sleeve_l0 from f22 (hanging) to f27 (raised) *while the K4 art is already on*. The pose README said it in the `turn` paragraph ("a drawing reads right only near the angle it was painted at") and I bridged the bone instead of holding it. Blink and breath did land (eye scaleY 0.12 at f21–22, f150–155; chest_ctl rises 100.1 → 104.9 over a breath).

## Entry 10 — hold, don't bridge: f23–26 left-arm keys = f27's values

1. **Read:** the paragraph above; pose README `turn`: "While the set shows, the bone is held within it".
2. **Expect:** build green; f023–f026 show the K4 drawing at its painted angle (a one-frame snap of the arm between f22 and f23, which the reference's own motion blur at f24 makes acceptable); clip ffmpeg exit 0, 648×480, 313 frames.
3. **Chose / turned down:** hold = snap. Turned down widening the hold to f20: the pose's hand is still low at f20–22 and the base art is right there.
4. **Happened:**
build exit 0 (52/21/0/17/14), render exit 0, pair 313, clip ffmpeg exit 0 → 648×480, 24 fps, 313 frames, aac. sheet_after_01: f024 now shows the K4 drawing at its painted angle, the snap sits between f022 and f023. sheet_after_08: the hem swings against the hip on every K2 beat (f201, f204, f210). As expected.

## At the end

- **Where I guessed:** skirt physics values (inertia .3/.35/.4, strength 200/170/140, damping .82) — no document gives a scale, I measured twice; bun physics (inertia .4, strength 150, damping .85) — one shot, judged only by eye (bun−head swing 15.8°); the hop threshold (8 px rise of both ankles over a 12-frame rolling median) — read off the pose after the first guess (25 px) found nothing; blink times (0.78 / 6.05+0.3 hold / 7.15 / 10.70 s) — read from an eye-crop sheet of the video, ±2 frames; blink shape and breath amplitude — copied from the rig's own idle; the K4 hold span f23–26 — chosen from sheet_before_01.
- **What I could not find:** what `frames` on an alternate does when the frame is outside the switch tolerance (the README sentence reads both ways; measured: nothing); why rig-pose 0.6.0 refuses the spec string the inputs carry (`rig-c-pose-frames/0`) while the shipped run accepted it; why my retarget wrote only `dance` with a motion.json beside the rig; whether rigc's physics clock at 24 fps vs 12 fps should move a spring's range by 1.7° (it did; §4.6's clock note suggests why but gives no figure); the session's token usage (the harness shows none — no usage.json written).
