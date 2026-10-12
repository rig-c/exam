# Journal — gpt-6-sol, 01-build, 2026-10-13

## Entry 1

1. **Read:** `README.md` Rules 2–3 and `tasks/01-build/TASK.md` Given: pinned packages are installed by `npm ci` at the repository root.
2. **Expect:** `npm ci` exits 0 and installs `@rig-c/parts@1.11.0` and `rig-c@2.47.0` in this clone.
3. **Chose / turned down:** Run the pinned install; turned down any other package version because the exam fixes these versions.
4. **Happened:** `npm ci` exited 0, added 5 packages, and reported 0 vulnerabilities.

## Entry 2

1. **Read:** `tasks/01-build/TASK.md` Given, `inputs/seethrough.json`, and `@rig-c/parts/docs/AUTHORING.md` §3–4: the initial loader needs a key, See-through settings, and an authored rig scale.
2. **Expect:** A parseable `config.json` with the recorded 1024 resolution and `[616,32,1132,548]` head box, plus a 0.5 rig scale, ready for `assemble --propose-plan`.
3. **Chose / turned down:** Create the minimal staged config; turned down inventing a plan or bones before the tool measures the layers.
4. **Happened:** `config.json` now has the recorded See-through settings and the authored 0.5 rig scale; no plan or rig sections yet.

## Entry 3

1. **Read:** `@rig-c/parts/docs/AUTHORING.md` §4 step 6 and `rig-parts assemble --propose-plan` output: 22 planned parts, two hair extensions, and no notes.
2. **Expect:** `config.json` gains the proposed 22-item draw order and both `extend_below_crop` entries without altering their names or tags.
3. **Chose / turned down:** Copy the proposal as printed; turned down changing the hair source before `assemble` measures uncovered holes.
4. **Happened:** `config.json` now carries the 22 proposed parts and both hair extensions in the printed order.

## Entry 4

1. **Read:** `@rig-c/parts/docs/AUTHORING.md` §4 step 7 and §5 assemble: assembly reports uncovered painting pixels and holes before rig authoring.
2. **Expect:** `rig-parts assemble` exits 0, writes `work/rig/parts.json`, and reports an `uncovered error px` count near the documented examples' scale.
3. **Chose / turned down:** Assemble the proposed plan to inspect its measured holes; turned down speculative patches before seeing those measurements.
4. **Happened:** Assembly exited 0 and wrote 22 parts; `uncovered error px: 2059`, with the largest hole 402 px between shoes and legwear.

## Entry 5

1. **Read:** `@rig-c/parts/docs/AUTHORING.md` §4 step 7: `propose` reads assembled parts and writes config-shaped bones, meshes, regions, motion, landmarks, and basis.
2. **Expect:** `rig-parts propose` exits 0 and writes `work/proposal.json` and `work/basis.json`, with any geometry lint clearly named.
3. **Chose / turned down:** Generate a measured draft from `work/rig`; turned down hand-authoring bones before the proposer reports them.
4. **Happened:** Proposal exited 0, wrote 21 bone entries and 8 meshes plus basis and landmarks, and reported 0 LINT lines; it noted the skirt chains start close to hip center.

## Entry 6

1. **Read:** `@rig-c/parts/docs/AUTHORING.md` §4 step 7 and `work/proposal.json`: the full loader requires the four proposed rig sections.
2. **Expect:** `config.json` gains the proposal's `bones`, `meshes`, `regions`, and `motion` verbatim and remains valid JSON.
3. **Chose / turned down:** Copy the generated sections unchanged for a measured baseline; turned down moving skirt chains before seeing this painting's gate result.
4. **Happened:** `config.json` has all four proposal sections; JSON parsing shows 21 bone entries, 8 meshes, 14 regions, and motion keys `duration`, `tracks`, `blink`.

## Entry 7

1. **Read:** `tasks/01-build/TASK.md` Do and `@rig-c/parts/docs/AUTHORING.md` §4 step 9: build assembles, rigs, checks, and prints any failing bar.
2. **Expect:** The uncorrected proposed config either exits 0 with `check: PASS` or gives a named check failure to correct; its assembly should retain about 2059 uncovered error px.
3. **Chose / turned down:** Run the exact task build flags for a baseline; turned down adding optional loop encoding because the task's gate does not request it.
4. **Happened:** Build exited 0, `check: PASS; 9 of 9`, and assembly held `uncovered_error_px 2059`; the skirt `TIP_OVER_ROOT` ratio was 3.673, above 1.4725.

## Entry 8

1. **Read:** `README.md` Submitting and `grade.py` main/folds: the grader rebuilds handed-in JSON, renders idle with `--folds`, and writes `result.json`.
2. **Expect:** `python3 grade.py` prints four PASS lines for 01 and writes `result.json` with 4 of 4 lines passed.
3. **Chose / turned down:** Grade the handed-in config independently; turned down trusting the direct build for the fold bar it did not measure.
4. **Happened:** Grader exited 0, printed four PASS lines, `does_not_fold: []`, and wrote `result.json`.

## At the end

- **Where I guessed:** `key` was authored as `exam-01-build`; `assemble.rig_scale` was authored as 0.5 from the guide's two examples. A task-specific scale would have required a stated target size.
- **What I could not find:** Nothing prevented this task's four pass lines.
