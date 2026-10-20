# The proctor's reading — claude-sonnet-5-5, 03-correct, 2026-10-20

Regraded: 6 of 6, the same lines — uncovered 1,726 against 3,500; 8 meshes deformed; the back hair travels
45.881 rig px. 9.2 minutes by the run's own lines.

**What was wrong and how it found it.** `propose` printed one LINT line: the two back-hair chains squeeze
`hair_back` because their amplitudes have opposite signs, with the remedy (give both the same sign) and
the figure that would follow. It changed one thing, `hairback_l`'s amplitudes to `[0.6, 1.4, 2.4]`;
`propose --from-config` then printed no LINT and the build passed. It never built the draft and says so.
The proctor built the draft: `check` fails `TEXTURE_STRETCH` on `hair_back`, triangle 167, edge 37–117,
idle frame 22, the edge at 0.065 of its rest length — the same edge the LINT named. The config handed in
is the draft with exactly that one change.

**Journal.** Six entries, no `WTF?:`. Entry 3 expected the seated pose to break the hip, chest or sleeves;
the LINT was about the back hair, and line 4 says "my guess about the cause was wrong" — with no `WTF?:`.
By the rule (the result differed from what it expected) that line should have begun with `WTF?:`.

**The transcript.** The config-writing steps are summaries; builds, `propose` runs and grades are recorded
with their output.

`idle_frames.jpg`: five idle frames of the build handed in.
