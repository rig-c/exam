started: 2026-10-20T13:51:20Z

$ python3 grade.py runs/2026-10-20-gemini-3.8-flash-medium-05-dance
FAIL  built: "rig-parts build exit 1"
FAIL  checked: "the build wrote no check.json"
FAIL  whole: "the build wrote no check.json"
FAIL  does_not_fold: "the build wrote no check.json"

$ python3 grade.py runs/2026-10-20-gemini-3.8-flash-medium-05-dance
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 2059 against <= 4200"
PASS  does_not_fold: []
PASS  budget: "828 triangles against <= 1000"
PASS  dance_as_timed: "`dance` lasts 4 s against 4.0"
PASS  closes: "the last frame is 0.0 rig px from the first at its furthest vertex, against <= 0.5 (keys only, physics out)"
PASS  both_hands: "`handwear_l` travels 507.4 rig px and `handwear_r` 500.8 at their furthest vertex, measured from the middle of `topwear`, each against >= 100.0"
PASS  whole_body: "the vertex of `topwear` that travels least travels 32.6 rig px, measured from the middle of `shoes`, against >= 15.0"
FAIL  arms_bend_at_the_joints: "along its own length an upper arm or a forearm bends at most 9.2 degrees more than at rest, against <= 8.0"
PASS  on_her_feet: "the end of a leg (`legwear`) gets 2.72 rig px from where it meets `shoes`, against <= 6.0"
PASS  keeps_time: "1.0 of the variation in how fast she moves repeats every two beats, against >= 0.5"
PASS  soft_in_the_dance: "`topwear` differs from the same build without its physics by 5.482 rig px at dance frame 36, against 3.0 to 15.0"
PASS  dance_does_not_fold: []

$ python3 grade.py runs/2026-10-20-gemini-3.8-flash-medium-05-dance
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 2059 against <= 4200"
PASS  does_not_fold: []
PASS  budget: "828 triangles against <= 1000"
PASS  dance_as_timed: "`dance` lasts 4 s against 4.0"
PASS  closes: "the last frame is 0.0 rig px from the first at its furthest vertex, against <= 0.5 (keys only, physics out)"
PASS  both_hands: "`handwear_l` travels 305.0 rig px and `handwear_r` 302.8 at their furthest vertex, measured from the middle of `topwear`, each against >= 100.0"
PASS  whole_body: "the vertex of `topwear` that travels least travels 32.6 rig px, measured from the middle of `shoes`, against >= 15.0"
PASS  arms_bend_at_the_joints: "along its own length an upper arm or a forearm bends at most 5.3 degrees more than at rest, against <= 8.0"
PASS  on_her_feet: "the end of a leg (`legwear`) gets 2.72 rig px from where it meets `shoes`, against <= 6.0"
PASS  keeps_time: "1.0 of the variation in how fast she moves repeats every two beats, against >= 0.5"
PASS  soft_in_the_dance: "`topwear` differs from the same build without its physics by 5.482 rig px at dance frame 36, against 3.0 to 15.0"
PASS  dance_does_not_fold: []
finished: 2026-10-20T14:01:42Z
