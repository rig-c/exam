# Proctor reading — gpt-5.6-sol, 02-move

Filed from `7c3535564fd7a2c9dc3e3a653d1dd5789c1fc042` on source parent `0643977fb2adb99eb91fc48cceb166b1b587b3bf`. Only submitted inputs are trusted.

Independent regrade on @rig-c/parts 1.60.0 and rig-c 2.67.2: **8 of 8**.

```text
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "STRESS_OFF_CHAIN": "PASS", "CLOTH_SETTLES": "CLEAR", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 1812 against <= 3700"
PASS  does_not_fold: []
PASS  trails: "6 bone(s) on a physics constraint: hairback_l0, hairback_l1, hairback_l2, hairback_r0, hairback_r1, hairback_r2"
PASS  gestures: "`gesture`: `face` travels 32.5 rig px at its furthest vertex, measured from the middle of `bottomwear`, against >= 22"
PASS  holds_together: {"opens": {}, "not_read": [], "against": "0 frames open on every pair, every pair read"}
PASS  gesture_without_folding: []
journal: chain intact, 4 entries, 1 WTF
```

Five sheets inspected. Gesture leans and turns the head toward image-right then returns, while the lower body and arms remain in the painted pose. Full silhouette remains visible, no gross mesh inversion; seam oracle reads all named pairs with zero open frames. Idle differences between build-check and independent renderer retained as distinct sheets.

Pictures and the [render receipt](render-receipt.json) bind the retained sheets to normalized commands and ordered frame hashes. Grader exit 0 is process completion; the individual lines above are the machine verdict.

Clock: 2026-10-25T09:46:03Z to 2026-10-25T09:51:01Z, 298 seconds by the unedited transcript. The clock includes stopped attempts where present.
