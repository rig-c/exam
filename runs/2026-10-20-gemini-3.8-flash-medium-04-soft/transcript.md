started: 2026-10-20T13:41:33Z

$ python3 grade.py runs/2026-10-20-gemini-3.8-flash-medium-04-soft
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 2059 against <= 4200"
PASS  does_not_fold: []
FAIL  budget: "742 triangles against <= 700"
PASS  hop_as_given: "the built rig holds `hop` exactly as tasks/04-soft/hop.json gives it"
PASS  soft: "`topwear` differs from the same build without its physics by 6.61 rig px at hop frame 14, against 3.0 to 15.0"
PASS  a_patch: "38 of 155 `topwear` vertices move over 0.5 rig px, against >= 8 and <= 80 %"
PASS  hop_does_not_fold: []

$ python3 grade.py runs/2026-10-20-gemini-3.8-flash-medium-04-soft
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 2059 against <= 4200"
PASS  does_not_fold: []
PASS  budget: "636 triangles against <= 700"
PASS  hop_as_given: "the built rig holds `hop` exactly as tasks/04-soft/hop.json gives it"
PASS  soft: "`topwear` differs from the same build without its physics by 6.61 rig px at hop frame 14, against 3.0 to 15.0"
PASS  a_patch: "14 of 114 `topwear` vertices move over 0.5 rig px, against >= 8 and <= 80 %"
PASS  hop_does_not_fold: []
finished: 2026-10-20T13:48:30Z
