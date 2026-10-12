# The proctor's reading — haiku, 03-correct, 2026-10-12

Regraded from the handed-in files on a second checkout: 5 of 5, the same lines. About ten minutes.

**The idle** (`idle_frames.jpg`, five frames): whole; breath, head tilt, the blink closes on frame 29;
nothing tears. The back hair is behind the shoulder in every frame, so the picture cannot show the fix —
the examinee says the same.

**What it found wrong, and from what.** The draft's `hairback_r` and `hairback_l` carry mirrored
amplitudes on a back hair that is one mass; the bridging edge closes. Decided from the
`CHECK_TEXTURE_STRETCH` line, then from `rig.json`'s weights read by hand, then from the proposal's own
sign pattern on its other chain pairs. Fix: the sign of `hairback_l`'s amps, magnitudes kept — a
different correction from the proctor's (one chain dropped), and the gentler one.

**What the journal caught** (filed on the tool):

- The proposal lints clean and then fails its own check on a cause the proposer can compute.
- The FAIL line names vertices; which bones they hang on had to be decoded from `rig.json`.
- `drift=21999` on one part in `assemble`'s table: flagged, could not be judged, nothing says what is ordinary.
- "A seated figure needs `--keypoints`" — it declined to invent joints, and the draft passed without.

**Journal discipline.** Eleven entries. No fourth line begins `SURPRISE:` although entries 4 and 6 record
a result that differed from the expectation — the examinee says so itself at the end and did not rewrite
them. The form's own "At the end" text was left above the entries.
