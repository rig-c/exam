# Transcript — haiku, 01-build, 2026-10-12

Commands that changed or built something, in order, with the last lines of their output.

## T1 mkdir runs/2026-10-12-haiku-01-build
- `mkdir -p runs/2026-10-12-haiku-01-build` (no output; directory created)
- `npm ci` in exam root (installs pinned packages into node_modules)
- `ln -s ../../tasks/01-build/inputs inputs` (symlink so inputs/ paths resolve)
- wrote config.json (key, seethrough, assemble.rig_scale)
- pasted plan + extend_below_crop from work/plan.txt into config.json (python)
- rig-parts assemble --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --config config.json --out work
- rig-parts propose --parts work/rig --source inputs/painting.png --out work > work/propose.log
- copied bones, meshes, regions, motion from work/proposal.json into config.json (python)
- rig-parts propose --parts work/rig --source inputs/painting.png --out work/lint --from-config config.json
- rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out > work/build1.log
- (build result recorded; exit code 144 on the foreground call, build completed in background, log work/build1.log)

## T2 rig-parts build (task 01 command), background-waited
- `rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out > work/build1.log`
  - the foreground call reported `Exit code 144` with only the first log line; the process (pid 53527) kept running and finished (background wait returned 0)
  - last lines of work/build1.log: `[check] check: PASS; 9 of 9 bar(s) measured, 0 skipped` / `build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from` / `  pack: skeleton.png 382x1962, 22 region(s), 90.3% covered, padding 2, page edges free, shape polygon`
  - out/check/check.json: PASS true, RECOMPOSITE_HOLES uncovered_error_px 2059
- rigc render --candidate out/check/build --animation idle --fps 12 --folds --geometry --out work/folds_idle > work/folds_idle.log
- rigc render ... --folds: 0 of 8 mesh(es) fold (work/folds_idle/idle/folds.json)
- cd exam && python3 grade.py runs/2026-10-12-haiku-01-build (background, log to work/grade1.out)
- grader: `python3 grade.py runs/2026-10-12-haiku-01-build` → output in work/grade1.out:
  - PASS built: "rig-parts build exit 0"
  - PASS checked: six bars PASS, RECOMPOSITE_HOLES REPORTED
  - PASS whole: "uncovered_error_px 2059 against <= 4200"
  - PASS does_not_fold: []
  - "4 of 4 line(s); journal present, 2 SURPRISE line(s); log .grade/2026-10-12-haiku-01-build/grade.log"
