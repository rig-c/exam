# Journal — gpt-6-luna-medium, 01-build, 2026-10-20

## Earlier attempts (recorded when the journal became writable)

- The first command targeting the clone run directory failed to start because I supplied a nonexistent working directory. A corrected command then copied the template and opened `tasks/01-build/TASK.md`.
- A later Python write of this journal failed with `PermissionError: [Errno 1] Operation not permitted`. No config write was attempted then.
- The report command failed with `Broker unavailable; start bridge.py serve for this socket`; `bridge.py serve` then failed on `[a path outside the clone, removed by the proctor]` with `Operation not permitted`.

## Entry 1

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §3–4; `tasks/01-build/inputs/seethrough.json`.
2. **Expect:** the base config with recorded See-through values and `rig_scale` will let `rig-parts inputs` write the padded full and head inputs.
3. **Chose / turned down:** use the task's existing painting/layers with the documented 0.5 rig scale; no generation step is needed.
4. **Happened:** config loaded; `inputs` wrote `st_input_full.png` at 2432x2432 (painting centered at x=384) and `st_input_head.png` at 516x516.

## Entry 2

1. **Read:** `rig-parts assemble --propose-plan` output, especially its `nose` note; `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 step 6.
2. **Expect:** adding the proposed plan, continuations, and recommended head-run nose row will let `assemble` produce parts with a recomposite error report.
3. **Chose / turned down:** use the proposed tags and order, and include the head-run nose because the tool says otherwise head pitch is not read.
4. **Happened:** config now contains the proposed 22 rows plus the recommended nose row, and both below-crop continuations.


## Entry 3

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 step 7; the proposed plan and continuation records.
2. **Expect:** `assemble` will write `work/rig`, parts, and a recomposite error report; any uncovered holes will be reported.
3. **Chose / turned down:** assemble the specified painting and layers into `tasks/01-build/work`; the plan is now explicit.
4. **Happened:** assembled 23 parts on 832x1216; recomposite reports `uncovered error px: 2059` (below the 4200 bar), and wrote parts plus error maps.


## Entry 4

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 step 7; the assembled `work/rig/parts.json` output.
2. **Expect:** `propose` will write proposal specs and landmark overlays for the assembled parts.
3. **Chose / turned down:** use the tool's measured proposal as a draft; no independent bones or meshes are invented.
4. **Happened:** `propose` wrote 21 bone entries, 8 meshes, `regions`, and `motion`, plus landmarks and notes; head pitch read 0.357 against the stated 0.474–0.630 frontal range.

## Entry 5

1. **Read:** `tasks/01-build/work/proposal.json` keys `bones`, `meshes`, `regions`, `motion`; its notes on the out-of-range head-pitch reading and lash reach.
2. **Expect:** copying the proposal's four spec sections into config will provide the full config required by `build`.
3. **Chose / turned down:** preserve the proposal unchanged for the first build so its gate output diagnoses any required correction.
4. **Happened:** config now contains the proposal’s 21 bone entries, 8 meshes, 15 regions, and 3 motion sections without hand-edits.


## Entry 6

1. **Read:** `tasks/01-build/TASK.md` pass lines; the build command in that task.
2. **Expect:** build exits 0 with PASS on all measured bars and no folded idle meshes.
3. **Chose / turned down:** ran the required build from `tasks/01-build`; intended to update this journal first.
4. **Happened:** WTF?: the journal update used repo-root-relative paths from the task directory and failed, but the shell continued into the build; I did not stop it.

## Entry 7

1. **Read:** `tasks/01-build/TASK.md` hand-in section; the completed build output.
2. **Expect:** copying config, journal and transcript into the run folder and running `grade.py` will print the task's final bar statuses and write `result.json`.
3. **Chose / turned down:** use the required grader and its pinned build inputs as the final result.
4. **Happened:** grader printed PASS for all 4 bars: built, checked, whole (2059 <= 4200), and does_not_fold (empty).


## Entry 8

1. **Read:** the first `python3 grade.py` output, `clock: no started:/finished: lines in transcript.md`.
2. **Expect:** copying the full transcript, which starts with the recorded UTC start, will satisfy the grader's start-clock check.
3. **Chose / turned down:** stage the run transcript and rerun the grader once; it is required to get a complete grading record.
4. **Happened:** WTF?: grader still reports the start/finish clock pair missing because only `started:` exists until the required post-grader timestamp is appended.


## Boundary incident

While staging the transcript I temporarily copied it to `/tmp/01-build-transcript.md`, outside the exam clone, then copied it back. This was my mistake; the temporary copy was not used as an input to any task.


## Entry 9

1. **Read:** the second grader output, which reported 0 WTF entries because the label did not match its line format.
2. **Expect:** changing two line-four labels to start `WTF?:` and using the exact `Entry 6` heading will let the grader count them.
3. **Chose / turned down:** correct the journal labels, then rerun the grader as a final record check.
4. **Happened:** grader printed PASS for all 4 bars and counted 2 journal entries whose line 4 begins `WTF?:`.
