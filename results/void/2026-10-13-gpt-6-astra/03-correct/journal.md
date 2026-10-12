# Journal — gpt-6-astra, 03-correct, 2026-10-13

## Entry 1

1. **Read:** `tasks/03-correct/TASK.md` Given/Do, `inputs/seethrough.json`, and the two `rig-parts layers` reports: both runs contain 29 nonempty layers and 0 WARN lines; the recorded head box is `[538,158,1100,720]`.
2. **Expect:** The minimal config with those recorded fields and `rig_scale: 0.5` will satisfy the plan proposer's loader and let it derive the seated painting's plan.
3. **Chose / turned down:** I will begin from stage-owned fields only. I turned down reusing Task 01's plan or rig because Task 03 is a new seated painting whose measured geometry differs.
4. **Happened:** The minimal Task 03 config was written with only the recorded input fields and authored scale.

## Entry 2

1. **Read:** `AUTHORING.md` §4 step 6 and both layer reports, which show no plausibility warning requiring an authored exclusion.
2. **Expect:** `assemble --propose-plan` will exit 0 and return a plan and any full-run extensions needed for the head parts.
3. **Chose / turned down:** I will accept the tool's measured plan proposal as the starting draft. I turned down manually transplanting the standing painting's plan because draw order and usable run can differ here.
4. **Happened:** It exited 0 with 22 parts, two hair extensions, and one actionable note: the head-run headwear has only 5 rig px against 2,146 in the full run, so the proposal takes `hairpin` from the full run behind the face.

## Entry 3

1. **Read:** Entry 2's JSON and `AUTHORING.md` §4 step 6, which says to paste `plan` and `extend_below_crop` into `assemble` and act on its notes.
2. **Expect:** Copying this proposal exactly, including full-run `hairpin`, will let assemble write all 22 parts and quantify uncovered pixels for the seated painting.
3. **Chose / turned down:** I will keep the proposed full-run hairpin because its note supplies the measured 5-versus-2,146-pixel reason. I turned down using the nearly empty head-run layer.
4. **Happened:** The full proposed plan and two extension records were added to `config.json`.

## Entry 4

1. **Read:** `AUTHORING.md` §4 step 7 and §5 assemble diagnostics: uncovered error pixels and largest hole boxes decide whether the plan needs a painting patch before rigging.
2. **Expect:** Assemble will exit 0 and report uncovered error pixels; I expect the correctly selected full-run hairpin and hair extensions to keep the total within Task 03's 3,500 bar.
3. **Chose / turned down:** I will assemble and read numeric holes before touching the plan. I turned down pre-emptive patches because no uncovered body has yet been observed.
4. **Happened:** It exited 0 with `uncovered error px: 1726`, below the 3,500 bar; the largest hole is 154 px between shoes and legwear, so no painting patch is justified.

## Entry 5

1. **Read:** `AUTHORING.md` §4 step 7: propose writes the draft rig and the `landmarks.png` picture; Task 03 warns that this proposal will not pass and requires deciding from messages and pictures.
2. **Expect:** Propose will exit 0 and lint its own placement, but the later build will expose the intended failing check. The landmarks picture should show which chains share each deforming mesh if a motion failure names one.
3. **Chose / turned down:** I will generate the proposal unchanged and preserve it as the diagnostic baseline. I turned down correcting from the task's warning alone because it does not name the failed invariant.
4. **Happened:** Propose exited 0 with 22 bone entries, 8 meshes, and `0 LINT line(s)`. `work/render/landmarks.png` shows the broad `hair_back` mesh driven by two long, diverging three-link chains (`hairback_r` and `hairback_l`), while all eight proposed meshes remain present.

## Entry 6

1. **Read:** `AUTHORING.md` §4 step 7 and `work/proposal.json`: copy exactly `bones`, `meshes`, `regions`, and `motion` to establish the draft Task 03 says will fail.
2. **Expect:** The mechanical merge will preserve the assembled plan and produce a full config that lints, allowing the build's own failing message to identify the correction target.
3. **Chose / turned down:** I will copy all four operational proposal fields unchanged. I turned down reducing the visually long hair chains now because the landmarks picture alone does not state that their geometry or motion violates a bar.
4. **Happened:** The merge exited 0 and the config now contains the unedited proposed bones, eight meshes, regions, and idle motion.

## Entry 7

1. **Read:** `AUTHORING.md` §4 step 8: lint the config's own bones before build; LINT checks placement, not the idle's texture-stretch bar.
2. **Expect:** `propose --from-config` will exit 0 with no LINT because the proposal was copied unchanged, confirming that Task 03's intended failure lies later than placement lint.
3. **Chose / turned down:** I will run the narrow config lint before the build. I turned down treating the earlier proposal lint as sufficient because this command reads the handed-in config itself.
4. **Happened:** It exited 0 with `0 LINT line(s)`, confirming the copied config's geometry placement passes the proposer's checks.

## Entry 8

1. **Read:** `tasks/03-correct/TASK.md` says the proposal does not pass its own check and the failing message/picture must drive the correction; `AUTHORING.md` §6 says every refusal names the object, found value and required value.
2. **Expect:** The exact task build will exit nonzero and print one or more failing check lines naming the specific mesh/motion measurement to correct; it should still assemble at `uncovered_error_px 1726`.
3. **Chose / turned down:** I will build the unedited draft once as required diagnostic evidence. I turned down speculative bone or amplitude edits before seeing the gate's named failure.
4. **Happened:** It exited 1 as expected. `CHECK_TEXTURE_STRETCH` named `hair_back` triangle 167, edge 37-117, idle frame 22: ratio 0.065, severity 15.338 against the required maximum 1.926544; its remedy says amplitudes may be too large down a chain or blended bones may move against each other.

## Entry 9

1. **Read:** The failed build's exact `CHECK_TEXTURE_STRETCH` message and `work/render/landmarks.png`: the picture shows one broad `hair_back` mesh weighted to two long chains on opposite sides, while the config gives those chains mirrored amplitudes `±[0.6,1.4,2.4]`. The message says the failing edge is squeezed as weighted bones move against each other.
2. **Expect:** Reducing only both `hairback_*` amplitude arrays to one quarter, `±[0.15,0.35,0.6]`, will keep the mesh deforming but bring the worst ratio inside 1.926544; all eight meshes remain meshes and every unrelated bar should remain unchanged.
3. **Chose / turned down:** I will symmetrically reduce those six amplitude values and change no bones, mesh, or part type. I turned down making `hair_back` rigid because Task 03 requires keeping at least eight deforming meshes, and turned down moving chain geometry because placement lint and the landmarks picture put both chains on their intended hair art.
4. **Happened:** Only the two hair-back amplitude arrays changed, from `±[0.6,1.4,2.4]` to `±[0.15,0.35,0.6]`; the eight mesh definitions and all chain geometry remain intact.

## Entry 10

1. **Read:** Entry 8's failure and Entry 9's scoped correction; Task 03 requires a green rebuild while preserving eight deforming meshes.
2. **Expect:** Rebuild will exit 0, print `TEXTURE_STRETCH: PASS` for 8 meshes with severity below 1.926544, retain `uncovered_error_px 1726`, and end `build: PASS`.
3. **Chose / turned down:** I will rerun the exact task build after the one scoped correction. I turned down further reductions until this measured result shows whether they are needed.
4. **Happened:** It exited 0 and ended `build: PASS`; `TEXTURE_STRETCH` now reports 8 meshes, severity 1.303, and the same edge ratio improved from 0.065 to 0.768, while uncovered error remains 1726.

## Entry 11

1. **Read:** `README.md` Results and Task 03 pass lines: the grader rebuilds from the handed-in config, checks folds, and counts meshes that still deform.
2. **Expect:** The grader will print five PASS lines, including `whole` at 1726, no folds, and at least 8 kept meshes.
3. **Chose / turned down:** I will run the proctor-equivalent grader now. I turned down any further quality tuning because the correction has a large measured margin and the experiment's required scope is satisfied.
4. **Happened:** SURPRISE: All five lines passed, including 8 deforming meshes and no folds, but the grader again added the undocumented `clock: no started:/finished: lines in transcript.md` diagnostic.

## At the end

- **Where I guessed:** `rig_scale: 0.5` follows the guide's examples. The quarter-scale hair-back amplitudes are an authored correction chosen from the 15.338 severity and opposing-chain picture; the package gives the failure ceiling and remedy class but no amplitude solver.
- **What I could not find:** No message maps a failing mesh edge back to the exact contributing bone weights. The build names the edge and gives the two likely mechanisms; the landmarks picture supplies the two-chain layout needed to choose the amplitude fix.
