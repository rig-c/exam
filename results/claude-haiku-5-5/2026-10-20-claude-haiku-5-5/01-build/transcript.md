started: 2026-10-20T13:19:09Z
$ git clone --single-branch --branch main --filter=blob:none --sparse https://github.com/rig-c/exam.git exam-claude-haiku-5-5 && git sparse-checkout set --no-cone '/*' '!/results/' '!/advanced/' && npm ci
  (clone of the exam repo, sparse; npm ci: "added 5 packages ... found 0 vulnerabilities")
$ ln -s ../../tasks/01-build/inputs inputs        # run directory now sees the task inputs without copying them
$ rig-parts inputs --source inputs/painting.png --config config.json --out work/inputs
  exit 0; "st_input_full.png 2432x2432: the painting at x 384, white either side (384 + 384 px)"
  (config.json at this point: key, seethrough {resolution 1024, steps 30, seed 42, offload true}, assemble.rig_scale 0.5)
$ rig-parts layers inputs/layers/full      > work/layers_full.txt   exit 0; 29 layers, 0 WARN
$ rig-parts layers inputs/layers/head      > work/layers_head.txt   exit 0; 29 layers, 0 WARN
$ rig-parts propose --head-box --full inputs/layers/full --canvas 1664x2432 > work/propose_head.log
  exit 0; "head_box [616, 32, 1132, 548], 516x516"
  (config.json: seethrough.head_box = [616, 32, 1132, 548] added)
$ rig-parts inputs --source inputs/painting.png --config config.json --out work/inputs
  exit 0; "st_input_head.png 516x516: seethrough.head_box [616, 32, 1132, 548]"
$ rig-parts assemble --propose-plan --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --config config.json > work/plan.log
  exit 0; 22-row plan, extend_below_crop for hair_front and hair_back, 7 notes (empty layers + nose)
  (config.json: assemble.plan and assemble.extend_below_crop pasted from plan.log)
$ rig-parts assemble --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --config config.json --out work > work/assemble1.log
  exit 0; "pixels: opaque 285469 = visible 222651 + occluded 62818 (22.0%); taken from the painting 180998 (63.4%)"
  "recomposite vs source: mean |d|=1.13, within 8: 97.8%, error px > 40: 6275, uncovered error px: 2059"
  "uncovered holes (8-connected): 605, the largest 5 listed"; "uncovered hole 1: 402 px at 405,1073 39x25 (between "shoes" 58 px, "legwear" 43 px)"
$ rig-parts propose --parts work/rig --source inputs/painting.png --out work > work/propose1.log
  exit 0; "0 LINT line(s) over 8 mesh(es) and the hip"; "coverage: 40 bone(s) — 31 checked and clean, 0 checked with a LINT line, 9 not checked"
  (config.json: bones, meshes, regions, motion copied from work/proposal.json)
$ rig-parts propose --parts work/rig --source inputs/painting.png --out work --from-config config.json > work/lint1.log
  exit 0; "0 LINT line(s) over 8 mesh(es) and the hip"
$ rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out
  exit 0 in 1m06s real; "check: PASS; 10 of 10 bar(s) measured, 0 skipped"; "53 assertions: 26 measured (26 passed, 0 failed), 27 skipped, 0 not in profile "spine-html""
  "build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from"
  "pack: skeleton.png 382x1962, 22 region(s), 90.3% covered"; "ANIMATIONS_DO_NOT_FOLD: PASS — 1 animation(s) ... 0 folding mesh(es)"
  "RECOMPOSITE_HOLES: REPORTED — error_px 6275; uncovered_error_px 2059; hole_count 605; largest px 402, box 405,1073 39x25"
$ python3 grade.py runs/2026-10-20-claude-haiku-5-5-01-build
  exit 0; PASS built, checked (all bars PASS, RECOMPOSITE_HOLES REPORTED), whole (2059 <= 4200), does_not_fold ([]); 4 of 4 lines
$ python3 grade.py runs/2026-10-20-claude-haiku-5-5-01-build   (final grader run, lines printed above in the grader log)
finished: 2026-10-20T13:31:46Z
