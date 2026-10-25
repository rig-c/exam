# Proctor reading — gpt-5.6-sol, 03-correct

Filed from `7c3535564fd7a2c9dc3e3a653d1dd5789c1fc042` on source parent `0643977fb2adb99eb91fc48cceb166b1b587b3bf`. Only submitted inputs are trusted.

Independent regrade on @rig-c/parts 1.60.0 and rig-c 2.67.2: **6 of 6**.

```text
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "STRESS_OFF_CHAIN": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 1726 against <= 3500"
PASS  does_not_fold: []
PASS  kept: "8 mesh(es) deformed against >= 8"
PASS  still_moves: "the back hair travels 45.881 rig px against the head over the idle, against >= 23"
journal: chain intact, 3 entries, 0 WTF
```

Three identical sheets inspected. Seated figure stays in frame, hair sweeps across the idle and the blink is visible; no gross inversion visible at contact-sheet scale. Eight deforming meshes retained and measured hair motion is 45.881 rig px. Same-sign repair follows the proposer diagnostic, not a reduction of motion.

Pictures and the [render receipt](render-receipt.json) bind the retained sheets to normalized commands and ordered frame hashes. Grader exit 0 is process completion; the individual lines above are the machine verdict.

Planner/proposer calls that rendered landmarks and measured lint were not wrapped in entries; the chain is intact; the task is counted; the omission is recorded. No unwrapped grader execution was observed.

Clock: 2026-10-25T09:51:03Z to 2026-10-25T09:54:22Z, 199 seconds by the unedited transcript. The clock includes stopped attempts where present.
