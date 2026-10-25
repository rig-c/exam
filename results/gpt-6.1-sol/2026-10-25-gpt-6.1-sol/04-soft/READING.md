# Proctor reading

Independent pinned-tool rebuild: 9 / 9; journal: chain intact, 3 entries, 0 WTF; 2.9 minutes from task transcript stamps.

The idle, hop and physics-free hop sheets were inspected. The patch uses 533 triangles, with 55 of 138 topwear vertices moving over 0.5 rig pixels and a 6.61 rig-pixel physics difference at frame 14. The same 6.61 in an earlier sitting is a measured response to common documented physics, not a shared handwritten answer. The authored patch center 427,332 differs from that earlier sitting.

| Line | Result | Read |
| --- | --- | --- |
| built | PASS | "rig-parts build exit 0" |
| checked | PASS | {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "STRESS_OFF_CHAIN": "PASS", "CLOTH_SETTLES": "CLEAR", "RECOMPOSITE_HOLES": "REPORTED"} |
| whole | PASS | "uncovered_error_px 1812 against <= 3700" |
| does_not_fold | PASS | [] |
| budget | PASS | "533 triangles against <= 700" |
| hop_as_given | PASS | "the built rig holds `hop` exactly as tasks/04-soft/hop.json gives it" |
| soft | PASS | "`topwear` differs from the same build without its physics by 6.61 rig px at hop frame 14, against 3.0 to 15.0" |
| a_patch | PASS | "55 of 138 `topwear` vertices move over 0.5 rig px, against >= 8 and <= 80 %" |
| hop_does_not_fold | PASS | [] |

Original journal, transcript and ledger retained unedited. Adjacent pictures and render receipts bind inspected frames, viewport and pinned commands. Source README and prompt match post-fix c014e3cf; that README embeds no prior-results table.

Session-log audit found no delegation or forbidden-answer fetch. Detailed failure expectations follow actual tool output; no identical authored dance was found among nine earlier filed definitions checked.
