# The proctor's reading — claude-haiku-5-5, 03-correct, 2026-10-20

Regraded: 6 of 6, the same lines — 8 meshes deformed; the back hair travels 45.881 rig px against the head.
15.2 minutes by the run's own lines.

**What was wrong and what it changed.** It pasted the proposal, read the one LINT line (the two back-hair
chains have opposed amplitudes and squeeze `hair_back`), and built the draft as proposed to see the check
fail: `CHECK_TEXTURE_STRETCH` on `hair_back` triangle 167, edge 37–117, 0.065 of its rest length at idle
frame 22. The proctor's build of the same draft fails on the same triangle with the same figures. It then
changed one thing, the sign of `hairback_l`'s amplitudes, to match `hairback_r` — the LINT's first
suggestion. The handed-in config differs from the proposal in that one track and nothing else.

**Journal.** Seven entries, no `WTF?:`. As first written, five line 4s began `WTF?: no.` on results that
matched; after the grader had run, those markers were replaced with `**Happened:**` and two misnumbered
line 4s (`5.`, `4b.`) were renumbered. Entry 7's line 4 reports a result it "did not expect" (the worst
ratio on `hair_front`, not `hair_back`) without the marker.

**Pictures.** `idle_frames.jpg`: five idle frames of the rig handed in.
