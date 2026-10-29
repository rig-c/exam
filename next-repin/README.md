# Archived next-repin candidate

Activated for Basic Round 6 by issue #63: the live draft and task text are in
`tasks/03-correct/`, with hashes and pins in `edition.json`. This directory preserves the
original dormant candidate byte for byte; it remains inactive. The boundary below records
the promotion contract. Issue #63 explicitly excludes new sittings; fresh-sitting evaluation
is future evidence and is not claimed by this author maintenance.

## Original staging contract

This directory stages static candidate inputs for a future edition. It is not selected by the current
prompt, task registry or grader. It contains no reference solution or corrected control. These files
can be visible in a clone without granting permission to replace the current task.

## Candidate format

`03-correct/manifest.json` has spec `rig-exam-next-repin/1`. `active` must be `false`. `draft` and
`task_text` are paths relative to that manifest's directory. `draft_sha256` seals the exact bytes of
the JSON draft. `source_inputs` is relative to the repository root and names the unchanged painting
and layers; it is a source reference, not an instruction to regenerate a proposal. The draft is
self-contained: it names no external config-relative asset. `03-correct/TASK.md` states the future
input contract and the existing machine bars, without calibrated readings or a correction recipe.

The small regression suite checks the draft hash, required config sections, absence of external
asset references, exact candidate file inventory, source/text path closure, and absence of activation
links from the current prompt, task and grader. These are static checks, not proof
that a new package version accepts the candidate.

    python3 -B -m unittest discover -s tools -p 'test_task03_next_repin.py' -v

## Activation boundary

A future, separately approved repin must promote the static draft and task text together, record the
new edition and source input hashes, and revalidate the actual build/check and independent exam bars
on those exact proposed pins. The author must hold a private defective control and a private corrected
control; their command outputs must show that package checks alone do not distinguish acceptance.
Keep calibration, corrected configs, control recipes and reference output outside the examinee clone.
Do not rerun `propose` to overwrite the supplied draft at activation or during a sitting.

Promotion must replace the current task's failing-proposal description and its numeric hint, route
the new edition explicitly to the static input, and preserve historical grading inputs. Updating
package versions alone is not activation. Current `tasks/03-correct/`, `package.json`, lockfile,
`grade.py`, `PROMPT.md`, existing results and in-flight sittings are unchanged by this staging area.
The current clone excludes `results/` and `advanced/` only; this directory is not a private storage
boundary. Private author material must never be copied here. Future pin acceptance and a fresh
sitting are activation gates, not claims made by these dormant files.
