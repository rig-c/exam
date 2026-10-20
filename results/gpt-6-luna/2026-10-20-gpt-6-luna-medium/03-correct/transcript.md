started: 2026-10-20T12:31:49Z

`rig-parts inputs --source tasks/03-correct/inputs/painting.png --config tasks/03-correct/config.json --out tasks/03-correct/inputs`
  wrote `st_input_full.png` 2432x2432 and `st_input_head.png` 562x562.
`rig-parts assemble --source tasks/03-correct/inputs/painting.png --full tasks/03-correct/inputs/layers/full --head tasks/03-correct/inputs/layers/head --config tasks/03-correct/config.json --out tasks/03-correct/work`
  assembled 23 parts; recomposite mean |d| 1.09; uncovered_error_px 1726; wrote recomposite and 23 part PNGs.

`rig-parts propose --parts tasks/03-correct/work/rig --source tasks/03-correct/inputs/painting.png --out tasks/03-correct/work`
  wrote proposal.json (22 bone entries, 8 meshes); `LINT hairback_r and hairback_l on mesh 'hair_back' ... edge ... closes to 0.064 times its rest length ... severity 15.572; <= 1.926544 required`; same signs predicted 1.046.
  recomposite uncovered_error_px from assemble: 1726.

`python3` copied proposal specs to config and changed only `motion.tracks[hairback_l].amps` from `[-0.6, -1.4, -2.4]` to `[0.6, 1.4, 2.4]` — no stdout.
`rig-parts build --config tasks/03-correct/config.json --source tasks/03-correct/inputs/painting.png --full tasks/03-correct/inputs/layers/full --head tasks/03-correct/inputs/layers/head --out tasks/03-correct/out`
  rig-c gate: 53 assertions, 25 measured, 25 passed, 0 failed; check: PASS; 10 of 10 bar(s) measured, 0 skipped.
  `ANIMATIONS_DO_NOT_FOLD: PASS` — 0 folding mesh(es); build PASS, packed skeleton 513x1384, 23 regions, 93.9% covered.

`python3 grade.py runs/2026-10-20-gpt-6-luna-medium-03-correct`
  PASS  built: "rig-parts build exit 0"
  PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
  PASS  whole: "uncovered_error_px 1726 against <= 3500"
  PASS  does_not_fold: []
  PASS  kept: "8 mesh(es) deformed against >= 8"
  PASS  still_moves: "the back hair travels 45.881 rig px against the head over the idle, against >= 23"
  6 of 6 line(s); journal present, 0 entry(ies) whose line 4 begins WTF?:
finished: 2026-10-20T12:33:58Z
