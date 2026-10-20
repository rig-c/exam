# The proctor's reading — claude-opus-5-5, 01-build, 2026-10-20

Regraded from the handed-in files on a fresh clone of the submitted branch: 4 of 4, the same lines as the
examinee's own run (uncovered 2,059 against 4,200). 5.3 minutes by the run's own `started:` / `finished:` lines.

**What it did.** The documented loop, unchanged: `assemble --propose-plan`, the plan pasted, `assemble`,
`propose`, the proposal pasted, one build, the grader. Nothing corrected; the only values it chose are the
`key` label and `rig_scale` 0.5, which it took from the AUTHORING row that gives 0.5 for a painting of this size.

**Journal.** Five entries, no `WTF?:`. Entry 2 notes "one surprise I note but do not act on" (`mouth` is a
141×99 box holding 42 opaque px) without marking it; the result it expected was met.

**The transcript.** Every assembling, proposing, building and grading command is recorded with its last
lines. The three Python steps that wrote `config.json` (the partial config, the plan pasted, the proposal
pasted) are not in it; the handed-in `config.json` is their result. Paths inside the clone are shown here as
`<clone>`.

**Who sat it.** `claude-opus-5-5`, as a Claude Code subagent started by the proctor. No sub-agent of its own and no
change of model in the session.
