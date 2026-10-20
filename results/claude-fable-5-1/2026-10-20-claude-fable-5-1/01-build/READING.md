# The proctor's reading — claude-fable-5-1, 01-build, 2026-10-20

Regraded from the handed-in files on a fresh clone of the submitted branch: 4 of 4, the same lines as the
examinee's own run (uncovered 2,059 against 4,200). 6.8 minutes by the run's own `started:` / `finished:` lines.

**What it did.** The documented loop, unchanged: `assemble --propose-plan`, the plan pasted, `assemble`,
`propose`, the proposal pasted, `propose --from-config` (0 LINT), one build, one grade. Nothing corrected;
`rig_scale` 0.5 and the `key` label are its only choices.

**Journal.** Six entries, one `WTF?:`, and it is a wrong expectation of the kind the exam asks for: it
expected the pasted proposal to fail `TIP_OVER_ROOT` on the skirt, as the package README says the demo's
did, and it passed at 3.673 against 1.4725. Its line 4 says the README's anecdote was not a rule it could
carry to this skirt.

**The transcript.** Commands and the last lines of their output, as the prompt asks; long outputs are cut
with `…` (ten places in this task) and the three Python steps that wrote `config.json` are one-line
summaries. The build lines were filtered out of the build's own log by `grep`, not retyped.

**Who sat it.** `claude-fable-5-1` itself, as a Claude Code subagent started by the proctor. No sub-agent of its own,
one model throughout.
