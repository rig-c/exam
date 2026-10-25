# Stopped before setup: inherited host memory

The host supplied actual prior-exam summary text before the first tool call.
This is an exposure disclosure, not an inference of deliberate answer access.
The original session stopped before setup; HQ acknowledged the STOP and ended
this sitting. It is retained here and does not count as independent. The active
retake is a separate session and is outside this record.

The entire frozen original log is JSONL lines 1-44. Its developer message at
line 8, `payload.content[1].text`, serializes the summary body itself, including
prior-exam results and grader-related topics. This is distinct from a generic
memory instruction or a tool reading the full memory registry. `who.json`
records two relevant short quotes, their reconstructed-summary line numbers,
the source record, and separate hashes for the log and summary.

The summary version SHA-256 is `2633958c5f2fa0110bd3453d9fa822888bc211931653fbffb9aed7dd8122d356`.
It covers the UTF-8 JSON-decoded text beginning after the begin marker's one
separating LF and ending immediately before the end marker. Markers are
excluded, the existing final LF is preserved, and no Unicode or line-ending
normalization is applied. This reconstructs serialized text, not the original
memory file's bytes. The summary does not establish that the earlier reports
concern these exact five tasks.

Both `turn_context.model` records, lines 11 and 37, identify `gpt-6-astra`.
Exactly two tool calls were observed: line 20 reads the bridge skill, and
line 25 sends the STOP report. The assistant states STOP at line 31; HQ accepts
it at line 38; the final acknowledgment is at line 41. In this complete frozen
log, no exam setup, clone/install, exam build, or task-file read call occurred.
Receiving the canonical exam prompt is not a task-file read.

There are zero tasks started, zero tasks submitted, and zero result files.
No grade, score, task duration, journal entry, or dance judgment is fabricated.
No dedicated memory-registry read or additional answer-source access was
observed in the two serialized tool-call inputs. That bounded observation does
not erase inherited memory exposure or establish absolute independence. This
session is ended and must not be reused as a fresh sitting.
