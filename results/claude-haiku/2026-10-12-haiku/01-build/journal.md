# Journal — haiku, 01-build, 2026-10-12

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry 1

1. **Read:** README.md rules 3–4 (journal before acting, transcript) and tasks/01-build/TASK.md; the journal template is JOURNAL.md.
2. **Expect:** a run directory that the grader will read `journal.md` from. The directory itself is the only thing to create before the journal can exist.
3. **Chose / turned down:** created runs/2026-10-12-haiku-01-build and wrote this journal into it. Turned down writing the journal outside the run, because grade.py reads journal.md from the run directory.
4. **Happened:** directory created (empty), journal written here. Nothing else changed yet. The mkdir was done just before this file existed, so its line 1–3 were not written first; no output from it.

## Entry 2

1. **Read:** README.md rule 2 ("`npm ci` installs them; use those and no others") and the root package.json (devDependencies `@rig-c/parts` 1.11.0, `rig-c` 2.47.0).
2. **Expect:** `npm ci` in the exam root exits 0 and creates node_modules/@rig-c/parts (1.11.0) and node_modules/rig-c (2.47.0), with bin links under node_modules/.bin.
3. **Chose / turned down:** `npm ci` from the lockfile. Turned down `npm install`, which may rewrite package-lock.json and can move versions.
4. **Happened:** exit 0, `found 0 vulnerabilities`; @rig-c/parts 1.11.0 and rig-c 2.47.0 installed, as pinned.

## Entry 3

1. **Read:** node_modules/@rig-c/parts/README.md "The loop, for an agent" and docs/AUTHORING.md §4 "The command order" (steps 0–2 are given: See-through is external and tasks/01-build/inputs already holds both layer runs and seethrough.json, whose head_box is [616, 32, 1132, 548]).
2. **Expect:** an `inputs` symlink in the run directory pointing at ../../tasks/01-build/inputs, so commands can use `inputs/...` paths without copying 19 MB. Nothing is written into the shared inputs as long as every later command writes to `out/` or `work/` (I will not run `rig-parts inputs --out inputs`, because it would write st_input_*.png into the shared folder).
3. **Chose / turned down:** symlink, over copying the inputs (19 MB, pointless) and over writing outputs into inputs. I also turn down running `rig-parts inputs` at all: the head box already exists in seethrough.json and the build does not read st_input files.
4. **Happened:** symlink created and resolves (inputs/painting.png, inputs/layers/full, inputs/layers/head, seethrough.json visible).

## Entry 4

1. **Read:** AUTHORING §4 "The command order", the loader table: `layers` step 6 (`assemble --propose-plan`) requires `key`, `seethrough`, `assemble.rig_scale`, with `seethrough.head_box`. Also `rig-parts layers inputs/layers/full` (29 layers, 0 WARN) and head (0 WARN).
2. **Expect:** after writing config.json with those three fields only, `assemble --propose-plan` prints a `plan` list (`[part, run, tag]` in draw order) and `extend_below_crop`, plus notes, and exits 0.
3. **Chose / turned down:** write `key` = "exam-haiku-01", `seethrough` from seethrough.json (resolution 1024, steps 30, seed 42, offload true, head_box [616,32,1132,548]), `assemble.rig_scale` 0.5 (the 1664x2432 painting makes an 832x1216 rig, AUTHORING §3). Turned down adding the `generation` block: it is recorded for the ComfyUI adapter and no CPU stage reads it.
4. **Happened:** config.json written (3 fields). `assemble --propose-plan` exit 0: a 22-part plan (hair_back, handwear, legwear, shoes, neck, bottomwear, topwear, hairpin, ears, face, mouth, eyewhites, irides, lashes, brows, hair_front), extend_below_crop with 2 entries, notes []. As expected, nose, eyewear, earwear, objects, tail, wings and neckwear are not in the plan and nothing names them.

## Entry 5

1. **Read:** work/plan.txt (the `assemble --propose-plan` output, exit 0, notes []). AUTHORING §4 step 6: "paste `plan` and `extend_below_crop` into `config.assemble`".
2. **Expect:** config.json gains `assemble.plan` (22 entries) and `assemble.extend_below_crop` (2 entries: hair_front, hair_back). The plan has no `nose`, `eyewear`, `earwear`, `objects`, `tail`, `wings`, `neckwear` line and the notes are empty, so I expect the assemble step to show holes where those pixels are.
3. **Chose / turned down:** paste the proposed plan unchanged (the plan is not mine to edit at this step, and assemble will name any hole). Turned down adding `nose` through `assemble.patches` now: a hole is only known after assemble runs.
4. **Happened:** config.json now has assemble.plan (22 entries) and extend_below_crop (2); the file parses and nothing else changed. As expected.

## Entry 6

1. **Read:** AUTHORING §4 step 7 ("`rig-parts assemble … --out work` — read its `uncovered hole` and `uncovered:` lines and look at `work/render/recomposite_error_rig.png`"), and README "The loop" (`assemble` writes work/rig; the holes are the thing no later gate can see).
2. **Expect:** exit 0 or 1 with named refusals; `uncovered hole N:` lines; `work/rig/parts.json` and `work/rig/parts/*.png`; `work/render/recomposite_error_rig.png`. The task pass line says the whole-build uncovered_error_px must be <= 4200 (grader's UNCOVERED_LINE, from the build's check.json, not this step). I expect a few holes near the nose and the outer clothes that the plan left out.
3. **Chose / turned down:** run assemble into `work/` (not into the shared inputs and not into `out/`, which the build owns). Turned down running `build` straight away, because the README asks for the holes to be read before the rig is authored.
4. **Happened:** SURPRISE: exit 0, but the count is 605 uncovered 8-connected holes (not "a few"); `uncovered error px` is 2059, which is under the 4,200 line. The largest, 402 px at 405,1073, lies between shoes and legwear, and none of the five largest is at the nose. The count is what I misread: I had guessed a handful, and nothing in AUTHORING §4 says how many holes to expect.

## Entry 7

1. **Read:** AUTHORING §4 step 7 (`propose --parts work/rig --source … --out work` writes proposal.json, basis.json and render/landmarks.png; copy bones, meshes, regions and motion into the config) and README "The loop" (`propose` is a draft, not part of build). I looked at work/render/recomposite_error_rig.png: the red is at the right ankle (about 405–440, 1073–1090 rig px) and a thin stripe beside the back hair at the left of the neck.
2. **Expect:** exit 0, `LINT` lines for chain links off their art (possibly none on the first proposal), one `coverage <bone>` line per bone, and files work/proposal.json, work/basis.json, work/render/landmarks.png, landmarks_head.png. The proposal will include `motion` with an idle and a blink (the figure has eyewhites).
3. **Chose / turned down:** propose without `--keypoints` (no keypoint file exists for this painting, and inventing joints would be a value the package does not have). Turned down `--compare` against a config with no bones yet.
4. **Happened:** exit 0. 21 bone entries (40 bones counting chain links), 8 meshes, 14 regions, idle motion 3.333 s with a blink. LINT: 0 lines. Coverage: 31 checked and clean, 9 not checked (neck is a control; the face and eye bones only bind regions, which no check reads). Notes flag: no nose part ("not read: no part tagged nose"), a template bang layout for hair_front, and a sash that is not drafted. As expected for the nose; the template-bang note is a judgment I must make, not a number.

## Entry 8

1. **Read:** AUTHORING §4 step 8 ("Copy `bones`, `meshes`, `regions` and `motion` into the config"; then `propose --from-config` to LINT, repeated until no LINT line) and §3 `bones`, `meshes`, `regions`, `motion` rows. work/proposal.json has top-level bones, meshes, regions, motion and notes; `notes` is not a config key and is not copied.
2. **Expect:** config.json with the four proposed sections and no change to them (the proposal is the draft; I am copying it unchanged first, to see what LINT says before I correct anything). The file loads and `propose --from-config` runs with 0 LINT lines, as the proposal's own LINT said.
3. **Chose / turned down:** copy unchanged. Turned down hand-correcting the bang chains or the nose before seeing a build, because the rule is to correct against the overlay (landmarks.png) only where a check or the picture says so, and I have not looked at landmarks.png yet. Turned down adding `constraints`: no task-01 line needs them.
4. **Happened:** config.json now holds bones, meshes, regions, motion from the proposal (python, one write). Loads with the keys key, seethrough, assemble, bones, meshes, regions, motion.

### Entry 9 (written after the fact; the rule was broken here)

I ran `propose --from-config config.json --out work/lint` right after entry 8's copy, and I wrote no entry before it. Its lines 1-3 are the ones in entry 8 step 8 of §4 (the LINT step after copying), which is the only reading I had for it. A rule-3 slip, recorded here rather than hidden.

1. **Read:** AUTHORING §4 step 8 (LINT after copying; "repeat until it prints no LINT line (exit 0)").
2. **Expect:** exit 0 and 0 LINT lines.
3. **Chose / turned down:** the lint run, as the step asks. Turned down skipping LINT and going to build.
4. **Happened:** exit 0, `0 LINT line(s) over 8 mesh(es) and the hip`, coverage 31 checked and clean, 9 not checked (the same as the proposal). Nothing to correct at this step; as expected.

## Entry 10

1. **Read:** README "The loop" last line and AUTHORING §4 step 9: `rig-parts build --config config.json --source … --full … --head … --out out` assembles, rigs and checks in one process and stops at the first refusal; the task's command is the same without `--loop`.
2. **Expect:** exit 0 on the first try is unlikely given that the proposal was never corrected, though LINT is clean. I expect either PASS with `out/check/check.json`, or a named FAIL line (exit 1) that says which bar and what to change. The uncovered number should match the assemble run (2059).
3. **Chose / turned down:** the task's exact command, without `--loop` (the task names none, and `--loop` is a different artifact). Turned down `--idle-keys direct`, which is only needed for a two-bone ik, and I have none.
4. **Happened:** the tool reported `Exit code 144` for the foreground call, and printed only the first log line. The build process was still running (pid 53527, `cli.ts build`); I waited on it in the background, and it exited 0. Its log ends `build: PASS` and `[check] check: PASS; 9 of 9 bar(s) measured, 0 skipped`. check.json: PASS true, uncovered_error_px 2059. Six bars PASS (BREATH_VISIBLE, BLINK_NO_HOLE, CHAIN_LAG, TIP_OVER_ROOT, STILL_REGIONS_DARK, TEXTURE_STRETCH) and RECOMPOSITE_HOLES REPORTED. SURPRISE: the 144 was not a build failure, but I misread the first line as the whole result; nothing in the README says a long build is backgrounded by the tool.

Also in the machine while the build ran: another process, `bun tools/auto_weightjump_survey.ts` (pid 49067, 100 % CPU, started 9:34 PM, not from this checkout), was running. I did not touch it.

## Entry 11

1. **Read:** the task's pass line "**Does not fold** — `rigc render --folds` over the idle names no mesh", and the grader's command (grade.py `folds()`: `rigc render --candidate out/check/build --animation idle --fps 12 --folds --geometry --out <dir>`, then folds.json `meshes[].frames`). I use the same command so my reading matches the grader's.
2. **Expect:** exit 0, a `folds.json` under the output with `meshes` where no mesh has `frames`, so the list of folding meshes is empty.
3. **Chose / turned down:** run the grader's exact command into work/, not a different `--fps`. Turned down reading the picture before the number: the number is the pass line, the picture is a separate reading.
4. **Happened:** exit 0. folds.json: `0 of 8 mesh(es) fold`, the folding list is empty. As expected. Pass line met.

## Entry 12

1. **Read:** README rule 5 and "Submitting" (`python3 grade.py runs/<run>` rebuilds from config.json and writes result.json; I may run it as often as I like); the task's pass lines.
2. **Expect:** the grader prints 4 lines (built, checked, whole, does_not_fold) all PASS, with the build taking several minutes, and writes result.json into the run directory.
3. **Chose / turned down:** run the grader now, once, before writing the rest. Turned down running it in a loop or changing the config to chase a bar, since all four are already green on my own runs.
4. **Happened:** the grader printed `PASS built`, `PASS checked` (all six bars PASS, RECOMPOSITE_HOLES REPORTED), `PASS whole` (`uncovered_error_px 2059 against <= 4200`), `PASS does_not_fold` (`[]`), `4 of 4 line(s); journal present, 2 SURPRISE line(s)`. Matches expectation. The grader's count of SURPRISE lines (2) equals the ones I wrote in entries 6 and 10.

## At the end

- **Where I guessed:** `key` = "exam-haiku-01" (any name; the examples use the directory name). The `head_box`, `resolution`, `steps`, `seed`, `offload` and `rig_scale` 0.5 are not guesses: they come from seethrough.json and from AUTHORING §3 (0.5 in both examples). Everything under `bones`, `meshes`, `regions`, `motion` is the proposal's unchanged, not my numbers. I did not write a value without a source.
- **What I could not find:** (1) whether assemble's plan is meant to include every See-through layer. Seven layers are not in the plan (nose, eyewear, earwear, objects, tail, wings, neckwear), and `assemble --propose-plan` printed `notes: []`, so nothing says why. AUTHORING §4 step 6 says a left-out layer is named in the notes, and these are not named. (2) How long a build takes and whether the tool backgrounds it: my foreground call returned `Exit code 144` while the build was still running, and no document says that a build takes minutes. (3) Whether 605 uncovered 8-connected holes (2,059 px) is normal for a plan that leaves seven layers out; the bar is on pixels (4,200), not holes, so I did not chase it.
- **Journal slips, recorded not hidden:** entry 9 was written after the fact (the lint run), and entry 4 and 5 had their results written into the wrong entries at first; I fixed both in the file.
