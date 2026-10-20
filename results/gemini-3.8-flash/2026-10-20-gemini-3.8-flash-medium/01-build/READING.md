# The proctor's reading — gemini-3.8-flash-medium, 01-build, 2026-10-20

Regraded from the handed-in files on a fresh clone of the submitted branch: 4 of 4, the same lines as the
examinee's own run (uncovered 2,059 against 4,200). 5.2 minutes by the run's own `started:` / `finished:` lines.

**What it did.** The documented loop, unchanged: `assemble --propose-plan`, the plan pasted, `assemble`,
`propose`, the four proposal fields pasted, `propose --from-config` (0 LINT lines), one build through the
grader. Nothing corrected; `key` and `rig_scale` 0.5 are the only values it chose.

**Journal.** Eight entries, no `WTF?:`. The session log shows each entry's lines 1–3 written before its step
and line 4 after it, as the form asks.

**The transcript.** It is written by hand, not captured. Every output line in it is a line the command
really printed (the proctor matched each against the session log), but the outputs are excerpts — the
`assemble` block keeps 8 of the lines it printed, and the grader blocks drop the `clock:` and summary lines.
Not in it at all: `assemble --propose-plan`, the two writes of `config.json` and the step that pasted the
proposal into it, and every read. Rule 4 asks for the raw record; for those steps it is not met.

**Who sat it.** Gemini 3.8 Flash itself, in an Antigravity Desktop conversation opened by the proctor through
agent-bridge; the prompt arrived as a peer message. No sub-agent; the log carries one model throughout.
