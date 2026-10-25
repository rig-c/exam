## Clone-local executable is not on PATH
- **I was trying to:** Run the documented `rig-parts propose` command through the required journal runner.
- **The tool gave me:** `journal.py: could not start rig-parts: [Errno 2] No such file or directory: 'rig-parts'`.
- **What would have helped:** State that journal-run commands need `./node_modules/.bin/rig-parts` (or make that path available).
- **Cost:** About two minutes; I found the clone-local executable and continued.

## Lint command needs an output directory
- **I was trying to:** Recheck the edited configuration with `propose --from-config`, as AUTHORING section 4 step 8 directs.
- **The tool gave me:** `FAIL USAGE: propose needs --out <dir> (see rig-parts guide USAGE)`.
- **What would have helped:** Include the required `--out` argument in section 4 step 8's command form.
- **Cost:** About one minute; I reran it with the existing work directory.
