# Journal — claude-sonnet-5-5, 05-dance, 2026-10-20

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry 1

1. **Read:** TASK.md 05 (legs 'one flat piece that hangs from the hip', shoes on the ground; arms bend at elbow/wrist only; pass lines), AUTHORING §3 meshes.<part> (grid + explicit [bone, from, to] segments, every plan part is a mesh or a region), recipe 'expressions and other named animations' (key free bones, not *_ctl; animations_from), my own task 02/04 experience (hop file, hip is not idle-keyed).
2. **Expect:** A build from task 04's config with: legwear turned from a region on hip into a grid mesh weighted to hip at the top and to two new static foot bones (parent root) at the bottom, so a hip move stretches the legs while the ankles stay where the shoes are; animations.json holding hop exactly as given plus a 4.0 s dance sampled at 24 fps from sines of period 1.0 s and 0.5 s (hip bounce on each beat plus sway, chest and head lean, the two shoulders pumping in opposition); the build exits 0 with the legwear mesh adding ~200 triangles to 667. Not known yet: whether the shoulders' rigid swing passes the 8 degree bend line, and whether the bust's soft displacement stays in 3-15.
3. **Chose / turned down:** Weights from hip/foot segments rather than a leg bone chain with an ik (an ik needs --idle-keys direct and a target bone: much more machinery) and rather than keeping legwear a region (then the feet leave the legs, the exact fault the task names). Dance made only of period-1.0 s and 0.5 s sines so 'keeps time' (variation repeating every two beats) holds by construction. Turned down: keying elbows (no elbow bone exists; the 8 degree bar says bending elsewhere fails, so the arms swing whole from the shoulder).
4. **Happened:** build exit 0, check PASS 10 of 10, 'beside the idle: 2 animation(s), hop, dance', ANIMATIONS_DO_NOT_FOLD 0 over idle/hop/dance, triangles 859 (legwear added about 190). As predicted; the open questions (arm bend, soft range) are not answered by check.

## Entry 2

1. **Read:** Task 05 pass lines (dance as timed, closes, both hands, arms bend at joints, whole body, on her feet, keeps time, soft in dance, no folds, budget 1000).
2. **Expect:** Likely passes: closes, as timed, feet, budget, folds, keeps time, whole body, hands. Uncertain: arms bend (shoulder swing up to 65 degrees with chest blending), soft (bust spring under a 2 Hz 16 px bounce could exceed 15 or be under 3).
3. **Chose / turned down:** Run the grader to read the lines, then tune only what it names.
4. **Happened:** 14 of 14 PASS on the first grader run: arms bend at most 2.0 degrees (bar 8), soft_in_the_dance 4.82 px (3-15), whole_body 23.0 (>=15), both hands 423.8 / 421.5, on_her_feet 0.0, keeps_time 1.0, budget 859. My open worries (arm bend, soft range) were both fine; no WTF. I then rendered the dance and looked at frame 0: one arm out, the other low, legs stretched with the feet on the shoes.

## At the end

- **Where I guessed:** Every dance amplitude and phase (hip bounce 16, sway 12, chest -5, head 6, shoulders 35+-30), the foot-bone positions (read off the painting by eye: ankle pixels in the 1368-wide display scaled by 0.61), the leg segment endpoints and the grid 36 were my own numbers; the bust physics is task 04's unchanged. I would have needed a way to read a bone position off the part picture, and a printed arm-bend figure per band before the grader.
- **What I could not find:** Whether a mesh may name a bone parented to root in its segments (I assumed so; it built), and how the weights fall off between two segments (I used the 1/(d+r)^2 sentence from §3 and did not verify the knee blend by eye beyond one frame).
