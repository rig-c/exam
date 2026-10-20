started: 2026-10-20T12:30:06Z

Copied task 01 config into the run; added `motion.animations_from: wave.json` and 8 `physics` constraints on `lock0..3` and `lock1_0..3` — no stdout.
Wrote `wave.json` with a 1.6-second `wave` animation, raising `sleeve_l0` and oscillating `sleeve_l2` — no stdout.

`python3 grade.py runs/2026-10-20-gpt-6-luna-medium-02-move`
  PASS  built: "rig-parts build exit 0"
  PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
  PASS  whole: "uncovered_error_px 2059 against <= 4200"
  PASS  does_not_fold: []
  PASS  trails: "8 bone(s) on a physics constraint: lock0, lock1, lock1_0, lock1_1, lock1_2, lock1_3, lock2, lock3"
  PASS  moves: {"animation": "wave", "duration": 1.6, "rise": 280.9, "folds": []}
  PASS  moves_without_folding: []
  7 of 7 line(s); journal present, 0 entry(ies) whose line 4 begins WTF?:
finished: 2026-10-20T12:31:44Z
