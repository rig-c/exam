# Journal — gpt-6-astra, 01-build, 2026-10-13

## Entry 1

1. **Read:** `tasks/01-build/TASK.md` Given/Do and `node_modules/@rig-c/parts/docs/AUTHORING.md` §3 fields `key`, `seethrough.*`, `assemble.rig_scale`; `inputs/seethrough.json` records resolution 1024 and head box `[616,32,1132,548]`.
2. **Expect:** Writing the initial `config.json` with the recorded See-through fields and `rig_scale: 0.5` will give `assemble --propose-plan` every field its `layers` loader requires; the next command should exit 0 and print a proposed plan.
3. **Chose / turned down:** I will start from only the fields this stage reads. I turned down inventing the plan, bones, meshes, regions or motion because AUTHORING §4 says those are proposed by later commands.
4. **Happened:** The file was written with exactly those recorded and authored fields.

## Entry 2

1. **Read:** `AUTHORING.md` §4 step 6 and the `rig-parts layers` output: both runs have 29 nonempty layers and 0 WARN lines.
2. **Expect:** `assemble --propose-plan` will exit 0 and print a plan plus `extend_below_crop` that can be pasted into `config.assemble`.
3. **Chose / turned down:** I will ask the tool for the plan from the supplied full/head runs. I turned down manually pairing tags because the command owns this proposal and uses the recorded head box.
4. **Happened:** It exited 0 and proposed 22 parts, two `extend_below_crop` entries for `hair_front` and `hair_back`, and no notes.

## Entry 3

1. **Read:** The `assemble --propose-plan` JSON from Entry 2 and `AUTHORING.md` §4 step 6, which says to paste `plan` and `extend_below_crop` into `config.assemble`.
2. **Expect:** Adding the proposal verbatim will make the config valid for the assemble loader; the following assemble command should be able to write parts under `work/`.
3. **Chose / turned down:** I will copy the proposal exactly. I turned down changing `hair_back` to the full run because this proposal explicitly extends its head part from the full layer and emitted no warning asking for a plan edit.
4. **Happened:** The 22-row plan and both extension records were added verbatim.

## Entry 4

1. **Read:** `AUTHORING.md` §4 step 7 and §5 `assemble`: assemble writes parts plus recomposite counts; uncovered red pixels cannot be repaired by later rig stages.
2. **Expect:** Assemble will exit 0, write `work/rig/parts.json` and images, and report uncovered error pixels small enough to understand whether a patch is needed.
3. **Chose / turned down:** I will assemble into the run's `work/` directory and inspect its numeric hole lines. I turned down adding a painting patch before observing a concrete uncovered body.
4. **Happened:** It exited 0, wrote 22 parts, and reported `uncovered error px: 2059`; the largest hole is 402 px between shoes and legwear. That is already below Task 01's 4,200 bar, so no patch is needed.

## Entry 5

1. **Read:** `AUTHORING.md` §4 step 7: after assemble, `propose --parts` writes `proposal.json`, `basis.json`, and landmarks; its bones, meshes, regions and motion are copied into the config.
2. **Expect:** Propose will exit 0, produce those JSON/PNG files, and print no LINT line because the draft should place its own chains on the measured part art.
3. **Chose / turned down:** I will propose from the assembled `work/rig` parts. I turned down authoring a skeleton from the painting dimensions because the package has measured masks and explicit role rules.
4. **Happened:** It exited 0, wrote 21 bone entries and 8 meshes, printed `0 LINT line(s)`, and classified 31 bones checked clean with 9 not checked for stated role/segment reasons.

## Entry 6

1. **Read:** `AUTHORING.md` §4 step 7 and `work/proposal.json`; the document says to copy `bones`, `meshes`, `regions`, and `motion` into the config.
2. **Expect:** Mechanically merging those four proposal fields will preserve the existing input/assemble fields and produce a full config accepted by `propose --from-config`.
3. **Chose / turned down:** I will use a JSON merge that selects exactly those four fields. I turned down copying `notes`, because the full loader does not require them and the task asks for operational inputs, not the proposal's narrative.
4. **Happened:** The merge exited 0 and replaced the config with its original fields plus the four selected proposal fields.

## Entry 7

1. **Read:** `AUTHORING.md` §4 step 8: redraw the config's current bones with `propose --from-config` and repeat until it prints no LINT lines.
2. **Expect:** The command will exit 0 and print 0 LINT lines because the proposal was copied without geometric edits.
3. **Chose / turned down:** I will lint the exact full config before the expensive build. I turned down skipping to build because this stage gives a narrower, faster refusal for copied structure errors.
4. **Happened:** It exited 0 and printed `0 LINT line(s)` with the same 31 checked-clean and 9 explicitly not-checked coverage classifications.

## Entry 8

1. **Read:** `tasks/01-build/TASK.md` Do/Pass lines and `AUTHORING.md` §4 step 9: build assembles, rigs and checks the corrected config; Task 01 requires exit 0, check PASS, uncovered error at most 4,200, and no idle fold.
2. **Expect:** The build will exit 0, end in `build: PASS`, retain `uncovered error px: 2059`, and write the checked skeleton; because the unedited proposal linted clean, I expect no check refusal.
3. **Chose / turned down:** I will run the exact task build command without `--loop`, since the task does not request loop artifacts. I turned down changing motion amplitudes before a gate names a failing object and measured bar.
4. **Happened:** The build exited 0 as expected: `check: PASS`, `uncovered_error_px 2059`, `TEXTURE_STRETCH: PASS`, and `build: PASS`; it wrote the packed skeleton artifacts.

## Entry 9

1. **Read:** `README.md` Results/Submitting and the prompt: `python3 grade.py runs/<run>` is the proctor's grader and writes `result.json`.
2. **Expect:** The grader will rebuild from `config.json` and print four PASS lines followed by `4 of 4 line(s)` with zero `WTF?:` entries.
3. **Chose / turned down:** I will run the grader now and trust only its rebuild. I turned down inferring a grade solely from the earlier `out/` because README says outputs are not trusted.
4. **Happened:** SURPRISE: All four pass lines were present, but the grader also printed `clock: no started:/finished: lines in transcript.md`, a transcript convention neither `README.md` nor `JOURNAL.md` described.

## At the end

- **Where I guessed:** `assemble.rig_scale: 0.5` was authored from the guide's two-example convention rather than proposed from this painting; a task-specific scale rule or proposer would remove that choice. No later geometry values were guessed: the plan and rig fields came from package proposals.
- **What I could not find:** No document states whether run-directory initialization itself must be journaled before the journal exists; I treated creating the directory and blank journal as setup and recorded it in the transcript.
