# DRAFT tool feedback disposition

These are proposals only; no upstream issue, tool fix or source-input repair was performed.

## DRAFT F1 — point from an image subdirectory to the parts manifest root

Task 04 journal entry 3 and tools.md report `PARTS_FILE_PRESENT` after `mesh-stats --parts out_04/parts`. The diagnosis that build deleted the intermediate is not supported. Independent output retains `out/parts.json`; the image directory is `out/parts/`. On the unchanged independently rebuilt config, the wrong directory exits 1 with `PARTS_FILE_PRESENT`; `--parts out` exits 0 and reports `mesh-stats: total 690 triangles over 8 mesh(es)`. `readRigInputs` reads `<partsDir>/parts.json` and `<partsDir>/parts/*.png`; AUTHORING line 1891 already names the assemble output root. Proposal: when the supplied directory is the images child and its parent holds parts.json, name that exact parent in the refusal. This is diagnostic guidance, not a missing config-only estimator or a cleanup defect.

## DRAFT F2 — make cloth-track reconciliation concrete

Task 02 journal entry 1: `WTF?: propose --cloth failed with PROPOSE_WRITE_CONFIG_CONFLICT on motion.tracks[5] hairback_l because our earlier manual sign edit conflicted with cloth removing that track`. Subsequent entries remove/reconcile the affected keyed hair tracks and the proposal succeeds. The refusal protects authored content; the feedback's “unrecoverable” characterization is not supported. Proposal: document a minimal keyed-track-to-physics reconciliation example and point to the named conflicting entry. No automatic force/overwrite behavior is endorsed.

## Not proposed — fallback cap resolution

Task 05 journal entry 1 and tools.md report `ASSEMBLE_LIMB_CAP_PRESENT` when fixture cap paths were interpreted relative to the run config. That is the stated rule: the refusal explicitly requires a PNG relative to the config's directory, and the grader copies the fixture's named caps into its isolated work directory. Record the friction and the remedy (copy the named assets or use the fixture-aware grader); this sitting does not establish a need for silent alternate-base lookup.

## Deferred exam-rules proposal

The source-reading-scope and last-grader/finish lifecycle gaps are reserved for one combined proposal after the non-Codex wave, per the proctor ruling. No new card execution is started here.
