# The proctor's reading — gpt-6-astra-medium, 01-build, 2026-10-20

Regraded from the handed-in files on a fresh clone of the submitted branch: 4 of 4, the same lines as the
examinee's own run (uncovered 2,059 against 4,200). 2.1 minutes by the run's own `started:` / `finished:` lines.

**What it did.** The documented loop, unchanged: `assemble --propose-plan`, the plan pasted, `assemble`,
`propose`, the four proposal fields pasted, one build through the grader. Nothing corrected, nothing guessed
but the `key` label and `rig_scale` 0.5, which it names as the examples' value.

**Journal.** Seven entries, no `WTF?:` — nothing differed from what it expected. Its "What I could not find"
is "nothing blocking".

**The transcript.** Four commands with their output are recorded raw; the three Python steps that wrote
`config.json` (the partial config, pasting the plan, pasting the proposal) are recorded as one-line
summaries, not as the code that ran. The examinee says so itself in its hand-in. The proctor compared each
summary with the session log: each says what the code did. Rule 4 asks for the raw record; for these three
steps it is not met.

**The clock line.** The grader printed `clock: no started:/finished: lines` during the sitting because the
examinee ran it before writing `finished:`, as the task order has it. Both lines are in the transcript now
and the regrade reads them.

**Who sat it.** `gpt-6-astra` itself, in a Codex Desktop thread opened by the proctor through agent-bridge; the
prompt arrived as a peer message. No sub-agent, no change of model in the thread.
