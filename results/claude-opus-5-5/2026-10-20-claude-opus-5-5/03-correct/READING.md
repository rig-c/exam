# The proctor's reading — claude-opus-5-5, 03-correct, 2026-10-20

Regraded: 6 of 6, the same lines — eight meshes kept, the back hair travels 45.881 rig px over the idle.
9.1 minutes by the run's own lines.

**What was wrong and what it changed.** The proposal keys the two back-hair chains with opposed amplitudes
(`hairback_r` [0.6, 1.4, 2.4], `hairback_l` [−0.6, −1.4, −2.4]), so they swing into each other and crush
`hair_back`. `propose` printed one LINT line naming the edge, the ratio and the remedy ("give both the same
sign (then 1.046)"); it checked the chains on `landmarks.png`, set `hairback_l`'s amplitudes to
[0.6, 1.4, 2.4] with a note, got `0 LINT line(s)` from `propose --from-config`, and built once: hair_back's
worst stretch 1.045. That is the only change from the proposal (the proctor compared the two files).

The proctor built the draft as proposed: `check` fails `TEXTURE_STRETCH` on `hair_back` triangle 167, edge
37–117 at 0.065 of its rest length at idle frame 22 — the message the LINT line anticipates.

**Journal.** Six entries, no `WTF?:`; every result was the one expected.

**The transcript.** Commands and their last lines, the Python step that wrote `config.json` excepted.

`idle_frames.jpg`: five idle frames of the run handed in.
