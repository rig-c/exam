# Proctor checklist — Basic exam

These checks complement the examinee's [rules](README.md#rules) and [journal](JOURNAL.md). They do not
change the machine bars, repair a hand-in or require a new host collector.

- **Before the first examinee call:** check the host evidence actually available for injected context
  and record its provenance, point in time, coverage and finding (observed content categories, or
  unavailable/partial). Keep raw private context and private persona names out of the public record.
  File presence or absence does not establish injection; a final prompt snapshot alone does not
  establish what was injected before the first call. If the host API or first-call evidence is
  unavailable, record that gap explicitly rather than claiming a clean context.
- **Preserve the evidence:** retain the original hand-in and available native command trace with
  source identifiers and hashes. Record which time span and command bodies the host exposes and which
  it does not. Public redactions are views, not byte-identical chain verification inputs.
- **Cross-check actual grader invocations:** read native command/tool-call records and compare each
  actual grader execution with the journal entry and transcript. Record an event reference, task,
  invocation time (or known ordering), matching entry or its absence, and separate flags for
  **outside-entry**, **before-start** and **after-finish**. Check shell wrappers' executed commands;
  an outer shell or script name alone may not establish what it executed. An entry wrapping a grader
  can still be outside the task clock: report the coverage and clock findings separately.
- **State coverage:** report the number of actual invocations and how many matched an entry only for
  the trace portion inspected. If command bodies, script contents or relevant time spans are missing,
  mark the finding unavailable/partial and identify the gap. A journal-only `transcript.md` contains
  only commands journal.py ran; an intact chain cannot reveal an unrecorded shell command. Do not turn
  missing evidence into “no omissions.”
- **Apply the 2026-10-25 ruling:** an outside-entry grader is an omission to record and does not alone
  disqualify an intact tool-written chain. A grader before start or after finish also means the literal
  task clock is incomplete. Keep the submitted clock, result, journal and historical disposition as
  they are; record the omission and timing limit separately. Broken or absent chains retain the
  existing rule. From the next sitting after this ruling, reading the clone's `grade.py` source is
  explicitly allowed: the exam measures packages and documentation sufficiency, with bars stated in
  `TASK.md`. Preserve historical source-read facts and their original dispositions; do not void them
  retroactively.

## Coverage controls

These are examples for reading evidence, not a command parser. `runs/example` stands for the task run.

| Observed evidence | Finding |
| --- | --- |
| `journal.py run -- python3 grade.py runs/example`, with matching step/entry and execution evidence | Wrapped grader; compare its time with start and finish as well. |
| `python3 grade.py runs/example`, with execution evidence and no matching entry | Direct outside-entry grader; record the omission. |
| `sh -c 'python3 grade.py runs/example'`, with evidence that the shell executed it | Actual grader inside a shell wrapper; match the outer journal step if one exists, otherwise record outside-entry. |
| An actual grader before start or after finish, whether wrapped or direct | Flag the clock boundary separately; retain the literal clock and disclose incompleteness. |
| `cat grade.py`, `printf '%s' 'python3 grade.py runs/example'`, or grader text in captured output | Source read or text mention, not a grader invocation. Text such as `grade.py` in a `python3 -c` string argument alone is not execution evidence. |
| A script/wrapper whose executed contents are unavailable, or a command after a shell condition whose outcome is unknown | Execution is unestablished; record the evidence gap, not an actual invocation or a clean finding. |
| Only the journal/transcript, or a native trace missing the relevant interval | Coverage unavailable/partial; the chain result remains a separate finding. |
