# The proctor's reading — gemini-3.8-flash, 03-correct, 2026-10-13

Regraded from the handed-in files on a second checkout: 5 of 5, the same lines as the run's own
`result.json` and as the examinee's report. The idle (`idle_frames.jpg`) is whole.

**What it found wrong, and from what.** From the `CHECK_TEXTURE_STRETCH` line and AUTHORING §6: one
back-hair mesh carrying two chains whose amplitudes are opposed. The report adds that it read
`rig.json`'s weight arrays to find which bones the three vertices hang on — the same hand-decoding the
first examinee did, and the step `@rig-c/parts` now prints in the message (rig-c/parts#314).

**What it changed.** `hairback_l`'s amplitudes to `hairback_r`'s sign, magnitudes kept; severity 15.338 →
1.045. The same correction as the first examinee's, and the one that keeps the drafted motion whole.

**What the journal caught.** One line marked (entry 6): the draft failing. The first build of the draft
was the grader's own, not the task's command.

**Journal discipline.** Eight entries, correct in form.

**How long.** No clock in the run. The four runs of this night were started together, and the person who started them said so at 15:28:06 UTC; this run's commit is 17 minutes after that. Since they were started before he said so, all three tasks took at least that long — an estimate, not a measurement.
