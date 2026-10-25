# Proctor reading — gpt-5.6-luna, 02-move

Filed from `c6c945cdc3513040317fd31ea8360db28ad1d788` on source parent `564d526676c1234c13b9cc5902b3435eff19e00f`. Only submitted inputs are trusted.

Independent regrade on @rig-c/parts 1.60.0 and rig-c 2.67.2: **7 of 8**.

```text
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "STRESS_OFF_CHAIN": "PASS", "CLOTH_SETTLES": "CLEAR", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 1812 against <= 3700"
PASS  does_not_fold: []
PASS  trails: "6 bone(s) on a physics constraint: hairback_l0, hairback_l1, hairback_l2, hairback_r0, hairback_r1, hairback_r2"
PASS  gestures: "`gesture`: `face` travels 32.8 rig px at its furthest vertex, measured from the middle of `bottomwear`, against >= 22"
FAIL  holds_together: {"opens": {"topwear|handwear_l": {"frames": 15, "max_px": 40}}, "not_read": [], "against": "0 frames open on every pair, every pair read"}
PASS  gesture_without_folding: []
journal: chain intact, 2 entries, 0 WTF
```

Five sheets inspected. Head and chest turn and lift through the middle of the gesture, then return; the figure remains visible. No gross mesh inversion at contact-sheet scale, but that scale cannot certify the armhole seam. Exact seam reading fails topwear|handwear_l:15 open frames, max40 px. The frozen answer retains the failed chest motion; no repair or human mark was added.

Pictures and the [render receipt](render-receipt.json) bind the retained sheets to normalized commands and ordered frame hashes. Grader exit 0 is process completion; the individual lines above are the machine verdict.

The frozen `gesture` still keys chest rotation +3° and chest translate-y +6. The journal promises to remove chest rotation, but the frozen answer contains no such repair. Build check passes while the grader reads `topwear|handwear_l` open for 15 frames, maximum 40 px. The omission of a `WTF?:` prefix is preserved; no surprise is added retroactively.

Clock: 2026-10-25T10:03:28Z to 2026-10-25T10:06:32Z, 184 seconds by the unedited transcript. The clock includes stopped attempts where present.
