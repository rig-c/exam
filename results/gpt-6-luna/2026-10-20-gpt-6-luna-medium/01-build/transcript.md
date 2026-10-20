started: 2026-10-20T12:21:03Z

Setup: `git clone --single-branch --branch main --filter=blob:none --sparse https://github.com/rig-c/exam.git exam-gpt-6-luna-medium` — `Cloning into 'exam-gpt-6-luna-medium'...`
Setup: `git sparse-checkout set --no-cone '/*' '!/results/' '!/advanced/'` — completed silently.
Setup: `npm ci` — added 5 packages; 0 vulnerabilities.

`cat > tasks/01-build/config.json` + `rig-parts inputs --source tasks/01-build/inputs/painting.png --config tasks/01-build/config.json --out tasks/01-build/inputs`
  rig-parts inputs: painting.png (1664x2432) -> inputs
  st_input_full.png 2432x2432: painting at x 384, white either side (384 + 384 px)
  st_input_head.png 516x516: seethrough.head_box [616, 32, 1132, 548]

`python3` updated `tasks/01-build/config.json` with the proposed plan, nose row, and continuations — no stdout.

`rig-parts assemble --source tasks/01-build/inputs/painting.png --full tasks/01-build/inputs/layers/full --head tasks/01-build/inputs/layers/head --config tasks/01-build/config.json --out tasks/01-build/work`
  recomposite: mean |d|=1.13; within 8: 97.8%; error px > 40: 6276; uncovered error px: 2059
  holes: 605; wrote work/rig/parts.json, 23 part PNGs, recomposite images.

Journal update attempted from `tasks/01-build` with repo-root-relative paths — `FileNotFoundError: runs/2026-10-20-gpt-6-luna-medium-01-build/journal.md`; shell continued.
`../../node_modules/.bin/rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out`
  `check: PASS; 10 of 10 bar(s) measured, 0 skipped`; `ANIMATIONS_DO_NOT_FOLD: PASS` — 0 folding mesh(es).
  build: PASS; packed skeleton 382x1962, 23 regions, 90.4% covered.

`rig-parts propose --parts tasks/01-build/work/rig --source tasks/01-build/inputs/painting.png --out tasks/01-build/work`
  wrote proposal.json (21 bone entries, 8 meshes), landmarks.png (+_head), basis.json; head pitch note: 0.357 (frontal 0.474..0.630).

`python3 grade.py runs/2026-10-20-gpt-6-luna-medium-01-build`
  PASS  built: "rig-parts build exit 0"
  PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
  PASS  whole: "uncovered_error_px 2059 against <= 4200"
  PASS  does_not_fold: []
  4 of 4 line(s); journal present, 0 entry(ies) whose line 4 begins WTF?:

`python3 grade.py runs/2026-10-20-gpt-6-luna-medium-01-build`
  PASS  built: "rig-parts build exit 0"
  PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
  PASS  whole: "uncovered_error_px 2059 against <= 4200"
  PASS  does_not_fold: []
  4 of 4 line(s); journal present, 2 entry(ies) whose line 4 begins WTF?:
finished: 2026-10-20T12:29:57Z

`python3 grade.py runs/2026-10-20-gpt-6-luna-medium-01-build`
  PASS  built: "rig-parts build exit 0"
  PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
  PASS  whole: "uncovered_error_px 2059 against <= 4200"
  PASS  does_not_fold: []
  4 of 4 line(s); journal present, 2 entry(ies) whose line 4 begins WTF?:
finished: 2026-10-20T12:30:17Z
