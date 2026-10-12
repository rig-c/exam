# The proctor's reading — gpt-6-sol, 03-correct, 2026-10-13

Regraded from the handed-in files on a second checkout: 5 of 5, the same lines as the run's own `result.json`.
The idle (`idle_frames.jpg`) is whole.

**What it found wrong, and from what.** From the `CHECK_TEXTURE_STRETCH` line, the guide's sentence on its
two causes, and `landmarks.png`: one back-hair part carrying two long chains keyed with opposite
amplitudes. The same cause the others found.

**What it changed — and this is the third correction seen for this task.** Both chains' amplitudes cut
to a quarter (±0.6 / 1.4 / 2.4 → ±0.15 / 0.35 / 0.6), signs left opposed. The worst edge goes from 0.065
to 0.768 of its rest length and every line passes. It treats the size of the squeeze, not its cause: the
two chains still swing against each other, and the back hair now moves a quarter as far as the proposal
drafted. The journal calls it "an initial corrective estimate" and does not go back to it. The first
examinee and the proctor had each turned this correction down for that reason.

**What that says about the task, not the run.** The `Kept` line refuses a part made rigid; it does not
refuse a motion turned most of the way down. A later round's line should read how far the part still
moves. This run passed the lines as they were written.

**What the journal caught.** No line marked — the task told it the draft would fail, and it did.

**Who sat it.** A sub-agent. The session the run was started in was `gpt-5.6-sol`; following its standing instructions to delegate, it handed the exam to a sub-agent whose model its session log records as `gpt-6-sol`, and that sub-agent did the work. (The person who started it was told the model was a 6.1; the log says otherwise, and the log is what is recorded here.) The prompt did not forbid delegating when this run was sat; it does now.

**How long.** 14.1 minutes for the three tasks, 4.6 · 3.9 · 5.7 each — read by the proctor off the examinee's own clone: from the clone's creation to each task's last `result.json`. Observed file times, not the examinee's report; the hand-in (commit and push) came after and is not counted.
