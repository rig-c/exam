# Proctor reading — gpt-5.6-sol, 04-soft

Filed from `7c3535564fd7a2c9dc3e3a653d1dd5789c1fc042` on source parent `0643977fb2adb99eb91fc48cceb166b1b587b3bf`. Only submitted inputs are trusted.

Independent regrade on @rig-c/parts 1.60.0 and rig-c 2.67.2: **9 of 9**.

```text
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "STRESS_OFF_CHAIN": "PASS", "CLOTH_SETTLES": "CLEAR", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 1812 against <= 3700"
PASS  does_not_fold: []
PASS  budget: "687 triangles against <= 700"
PASS  hop_as_given: "the built rig holds `hop` exactly as tasks/04-soft/hop.json gives it"
PASS  soft: "`topwear` differs from the same build without its physics by 6.61 rig px at hop frame 14, against 3.0 to 15.0"
PASS  a_patch: "23 of 109 `topwear` vertices move over 0.5 rig px, against >= 8 and <= 80 %"
PASS  hop_does_not_fold: []
journal: chain intact, 6 entries, 3 WTF
```

Seven sheets inspected: idle and hop, with and without physics. The hop body rises, lands and settles; no gross mesh inversion is visible at sheet scale. The two hop renders use exactly the same fixed viewport, confirmed in frames.json. Patch displacement is small at sheet scale; geometry measures 6.61 px at frame14, 23/109 vertices >0.5 px and 687 triangles. Continuous playback and human quality are not scored.

Pictures and the [render receipt](render-receipt.json) bind the retained sheets to normalized commands and ordered frame hashes. Grader exit 0 is process completion; the individual lines above are the machine verdict.

The authored patch center is [403,330]; r28/band16/physics come from the documented recipe. Mesh statistics progressed 919 → 727 → 687 triangles at region spacings 7 → 12 → 14. The initial `--parts work` failure does not establish that the documented `work/rig` path is invalid; that path was not tried in the recorded failed command.

Clock: 2026-10-25T09:54:24Z to 2026-10-25T09:58:53Z, 269 seconds by the unedited transcript. The clock includes stopped attempts where present.
