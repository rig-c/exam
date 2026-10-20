# Journal — claude-fable-5-1, 01-build, 2026-10-20

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry <n>

1. **Read:** which document, section or message this step rests on (path and heading, or the message quoted).
2. **Expect:** what the step will produce, concretely — an exit code, a file, a number, a line of output.
3. **Chose / turned down:** what you are about to do, and the alternative you considered and why not.
4. **Happened:** what the step actually produced. If it differs from line 2, begin the line with
   `WTF?:` and say in one sentence what you now think you misread — or that nothing told you. Say it
   the way it landed. Politeness is not graded here; a line that understates the surprise hides it.

## At the end

- **Where I guessed:** every value you wrote without a source (a number, a name), and what you would
  have needed to read to not guess.
- **What I could not find:** questions you had that no document or message answered.

---

## Entry 1

1. **Read:** `@rig-c/parts` README *The loop, for an agent* and `docs/AUTHORING.md` §4 table (loader `layers`: `inputs`, `assemble --propose-plan` require `key`, `seethrough`, `assemble.rig_scale`; `--propose-plan` also needs `seethrough.head_box`). §3 says `assemble.rig_scale` is authored, "0.5 in both examples (a 1664x2432 painting makes an 832x1216 rig)". `inputs/seethrough.json` gives resolution 1024, steps 30, seed 42, offload true, head_box [616, 32, 1132, 548]. `rig-parts layers` on both runs printed 0 WARN lines, 29 layers each.
2. **Expect:** writing `config.json` with `key`, `seethrough` (copied from seethrough.json) and `assemble.rig_scale: 0.5`, then `rig-parts assemble --propose-plan --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --config config.json` exits 0 and prints a `plan` list (part, run, tag) with `extend_below_crop` and notes naming the unplanned tiny layers (neckwear, tail, wings, objects, eyewear ~70 px) and `nose`.
3. **Chose / turned down:** rig_scale 0.5 because the painting is exactly the size the guide quotes for it (1664x2432); turned down 1.0 (no document gives a reason to double the rig against the examples). Skipped `propose --head-box` since the task hands the head box in `seethrough.json` and says the head run was made with it.
4. **Happened:** exit 0. A 23-row plan (hair_back from the head run, handwear_l/r, legwear, shoes, neck, bottomwear, topwear, hairpin, ears, face, mouth, eyewhites, irises, lashes, brows, hair_front), `extend_below_crop` for hair_front and hair_back from the full run, and seven notes: neckwear/tail/wings/objects/eyewear/earwear below the 150 px floor, and `nose` never planned. As expected.

## Entry 2

1. **Read:** AUTHORING §4 step 6–7: paste `plan` and `extend_below_crop` into `config.assemble`, then `rig-parts assemble … --out work` and read its `uncovered hole` lines. The `assemble` loader requires `key`, `seethrough` (+head_box), `assemble.rig_scale`, `assemble.plan`. I am not adding the `nose` row: the note says it only feeds `propose`'s `head pitch:` note, and the examples' recomposite moved by ≤2 px with it.
2. **Expect:** exit 0, `work/rig/parts.json` and `work/rig/parts/*.png`, a `pixels:` line, and some `uncovered hole N:` lines — a few hundred px each; a total under the task's 4,200 bar would be good but I have no figure to predict from.
3. **Chose / turned down:** the plan as proposed, unedited; turned down adding the nose row (no bar reads it) and `--seam silhouette` / `--project visible` (the skill names them as alternatives for white garments and thin parts; the default is the reference rule and I have no reading yet that says it is needed).
4. **Happened:** exit 0, 22 parts on an 832x1216 rig. `pixels: opaque 285469 = visible 222651 + occluded 62818 (22.0%); taken from the painting 180998 (63.4%); visible but not projected 41664 (14.6%)`. `recomposite vs source: … uncovered error px: 2059`, 605 holes, the largest 402 px at 405,1073 39x25 between shoes and legwear. 2059 is under the task's 4,200 bar, so no patch is needed. As expected in kind; the size I had no figure for.

## Entry 3

1. **Read:** AUTHORING §4 step 7: `rig-parts propose --parts work/rig --source inputs/painting.png --out work` → `work/proposal.json`, `basis.json`, `landmarks.png`, per-bone `coverage` lines and `note:` lines; then copy `bones`, `meshes`, `regions`, `motion` into the config.
2. **Expect:** exit 0, a proposal with a `hip`/`chest`/`neck`/`head` spine, sleeve chains for the two handwear parts, chains for hair_back/hair_front/bottomwear, grid meshes at spacing round(1216/37)=33 px, an idle of 3.3333333333333335 s with a blink, and a `head pitch: not read: no part tagged nose` note.
3. **Chose / turned down:** default `--grid-rule figure`; turned down `--grid-rule part` (the figure rule is the default and §3 says the part rule is the reference's, used for the oracle examples only) and `--keypoints` (she is standing, front-facing — README says the screen-y rules fit that).
4. **Happened:** exit 0, 21 bone entries (hip/chest/neck/head, 5 face bones, `bun`, bang_r/c/l 2-link chains, `lock`/`lock1_` 4-link chains, hairpin, sleeve_r/l and skirt_r/c/l 3-link chains = 40 bones), 8 grid meshes at spacing 31 (round(1160/37) — I had said 33 from the full 1216 canvas; the note says H is the parts' boxes' height, 1160), 14 regions (legwear on hip, shoes on root), idle 3.3333333333333335 s with blink at t=2.3, 0 LINT lines, 31 bones checked clean, 9 not checked (controls/regions/explicit segments), and `head pitch: not read: no part tagged nose` as expected. I looked at `work/render/landmarks.png`: the chains sit on the sleeves, the side locks and the skirt. Within expectation but for the spacing figure.

## Entry 4

1. **Read:** AUTHORING §4 step 7–8: copy `bones`, `meshes`, `regions`, `motion` from `work/proposal.json` into the config, then `propose … --from-config config.json` until it prints no LINT line (exit 0). The proposal already printed 0 LINT lines.
2. **Expect:** after pasting, `rig-parts propose --parts work/rig --source inputs/painting.png --out work --from-config config.json` exits 0 with `0 LINT line(s)`.
3. **Chose / turned down:** paste the proposal unchanged. The `hair_front` note says the bang chains are a template and to "move the chains onto the locks" — I turned that down for now: no bar reads it, and I cannot verify a lock's path better than the proposer from the picture at this size; I will correct only what a FAIL line names.
4. **Happened:** exit 0, `0 LINT line(s) over 8 mesh(es) and the hip`, wrote `work/render/landmarks_config.png`. As expected.

## Entry 5

1. **Read:** TASK.md *Do* (the exact build command) and AUTHORING §4 step 9; README *The loop* says to read `out/check/check.json`, every FAIL names what has to change. README *What you get* says the demo's proposal pasted uncorrected failed `CHECK_TIP_OVER_ROOT` on `bottomwear` because the two outer skirt chains sat within 90 px of the centre of a 449 px skirt. Here skirt_r/skirt_l roots are 37 and 35 px from hip's x on a 347 px wide skirt.
2. **Expect:** the build runs assemble, rig and check; I expect exit 0 and `build: PASS` with a pack line and three artifact paths, but there is a real chance of `CHECK_TIP_OVER_ROOT` on `bottomwear` as on demo, since the skirt chains are as close to the centre as the demo's were. It should take about a minute.
3. **Chose / turned down:** the exact TASK.md command, no `--loop` (the task does not ask for the APNG and the grader runs the command as given); turned down pre-emptively moving the skirt chains outward — a correction with no FAIL line behind it is a guess.
4. **Happened:** WTF?: exit 0, `check: PASS; 10 of 10 bar(s) measured, 0 skipped`, `build: PASS` in 1m17s — `TIP_OVER_ROOT: PASS` with bottomwear at ratio 3.673 against the floor 1.4725, so the demo's failure did not repeat; the README's "within 90 px of the centre" reading was not a rule I could carry to this skirt, and nothing told me what makes a chain's tip ratio high enough until the bar printed it. Pack `skeleton.png 382x1962, 22 region(s), 90.3% covered`; loop `max |d| 0`; seam `mean |d| 0.117`; `TEXTURE_STRETCH` worst hair_front triangle 68 (vertices 56|30|28, edge 30|28, frame 3) ratio 1.084 against ceiling 1.926544; `ANIMATIONS_DO_NOT_FOLD: PASS — 0 folding mesh(es)`.

## Entry 6

1. **Read:** README rule 6 and the prompt: `python3 grade.py runs/<run>` rebuilds from `config.json` alone and prints the four pass lines of TASK.md (Built, Checked, Whole ≤ 4,200, Does not fold).
2. **Expect:** PASS on all four: `rig-parts build exit 0`, every bar PASS, `uncovered_error_px 2059 against <= 4200`, folds `[]`; `4 of 4 line(s)`; it writes `result.json` here.
3. **Chose / turned down:** run it once now; turned down skipping it (the grader is the proctor's reading and the only one that counts).
4. **Happened:** `4 of 4 line(s)`: built exit 0, every bar PASS (RECOMPOSITE_HOLES REPORTED), `uncovered_error_px 2059 against <= 4200`, `does_not_fold: []`. As expected. (Its `clock:` line says no finished: yet — that line is written after this.)

## At the end

- **Where I guessed:** `assemble.rig_scale: 0.5` — taken from §3's example figure for this exact painting size rather than from any rule that says what the scale should be; `key` is a free name. Everything else was copied from a command's output.
- **What I could not find:** what makes `TIP_OVER_ROOT` pass or fail before the build runs — the README gives the demo's failure as "within 90 px of the centre of a skirt 449 px wide" but no rule to apply to another skirt. Whether the `hair_front` note ("move the chains onto the locks") needs acting on when no bar reads it.
