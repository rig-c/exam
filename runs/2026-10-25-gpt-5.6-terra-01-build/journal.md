# Journal

## Entry 1 (opened 2026-10-25T09:50:09Z)

1. **Read:** AUTHORING.md §4 step 4: propose --head-box writes the head crop into an initial layers config.
2. **Expect:** The supplied full and head layer runs were made at 1024, so the proposer will add a square head_box in the 1664x2432 painting.
3. **Chose / turned down:** I wrote the minimal config.json with the documented key, seethrough resolution 1024, and rig_scale 0.5; I did not invent a plan or rig sections.
4. **Happened** (2026-10-25T09:50:13Z): WTF?: journal.py: could not start rig-parts: [Errno 2] No such file or directory: rig-parts; the package command was not on PATH.

## Entry 2 (opened 2026-10-25T09:50:17Z)

1. **Read:** The first command failed before it ran because journal.py does not add node_modules/.bin to PATH; npm ci installed the package under this clone.
2. **Expect:** Calling the package executable at ./node_modules/.bin/rig-parts will run the same documented propose command and add the head_box.
3. **Chose / turned down:** I use the clone-local executable rather than installing another version or changing PATH globally.
4. **Happened** (2026-10-25T09:50:23Z): WTF?: FAIL CONFIG_FIELD_PRESENT: config.seethrough.steps — is absent and required; the task input seethrough.json states steps, seed and offload too.

## Entry 3 (opened 2026-10-25T09:50:27Z)

1. **Read:** The refusal named the three omitted seethrough fields, and tasks/01-build/inputs/seethrough.json supplies steps 30, seed 42, offload true.
2. **Expect:** With the supplied complete See-through settings, propose --head-box will write the crop coordinates.
3. **Chose / turned down:** I copied only those three task-supplied settings into config.json and retained the given resolution.
4. **Happened** (2026-10-25T09:50:34Z): head_box [584, 69, 1111, 596], 527x527; config added seethrough.head_box.

## Entry 4 (opened 2026-10-25T09:50:37Z)

1. **Read:** AUTHORING.md §4 step 6: assemble --propose-plan combines the supplied full and head layers and writes the plan.
2. **Expect:** The supplied matching layer runs will yield a plan and perhaps notes for layers that are intentionally not planned.
3. **Chose / turned down:** I use the documented full/head inputs and write the plan into the same config.
4. **Happened** (2026-10-25T09:50:58Z): added assemble.plan; added assemble.extend_below_crop; the notes say nose is in no plan row and the package never plans it.

## Entry 5 (opened 2026-10-25T09:51:02Z)

1. **Read:** AUTHORING.md §4 step 7 says to assemble the proposed plan to work/ and then use those parts to draft bones, meshes, regions and idle motion.
2. **Expect:** Assembly will expose any uncovered holes and write the rig-space parts that propose needs.
3. **Chose / turned down:** I keep work under this task run directory and use the plan without adding the optional nose row.
4. **Happened** (2026-10-25T09:51:36Z): recomposite vs source: mean |d|=1.09, within 8: 97.6%, error px > 40: 7465, uncovered error px: 1812.

## Entry 6 (opened 2026-10-25T09:51:39Z)

1. **Read:** AUTHORING.md §4 step 7: propose --parts writes the drafted rig sections into config after the assembled parts are available.
2. **Expect:** The automatic proposal will add bones, meshes, regions and idle motion; it may report LINT that the next documented stage checks.
3. **Chose / turned down:** I use the assembled rig parts and the original painting, allowing the proposer to write only its documented sections.
4. **Happened** (2026-10-25T09:51:50Z): LINT hairback_r and hairback_l on mesh hair_back squeeze it; give both the same sign, or drop one chain.

## Entry 7 (opened 2026-10-25T09:51:56Z)

1. **Read:** The proposal LINT says the opposed hairback amplitudes squeeze a hair_back edge and specifies that both chains need the same sign.
2. **Expect:** Changing only hairback_l amplitudes from negative to positive will remove that LINT without moving any bone or mesh.
3. **Chose / turned down:** I retained both hair chains and made hairback_l amplitudes [0.6, 1.4, 2.4], the exact alternative the tool reported.
4. **Happened** (2026-10-25T09:52:02Z): WTF?: FAIL USAGE: propose needs --out <dir>; the §4 step 8 prose omitted the required output argument.

## Entry 8 (opened 2026-10-25T09:52:05Z)

1. **Read:** The rerun refusal says propose needs --out <dir>, and §4 step 7 demonstrates that work directory as the proposal output.
2. **Expect:** With --out work supplied, --from-config will lint the edited config and report no LINT if the amplitude correction holds.
3. **Chose / turned down:** I reuse the existing task-local work directory; this lint run does not rewrite config.json.
4. **Happened** (2026-10-25T09:52:17Z): 0 LINT line(s) over 8 mesh(es) and the hip; coverage: 47 bone(s) — 39 checked and clean, 0 checked with a LINT line.

## Entry 9 (opened 2026-10-25T09:52:20Z)

1. **Read:** TASK.md requires the documented build to exit 0, report check PASS, hold uncovered error <=3700, and render folds with no mesh; AUTHORING.md §4 step 9 says build gates the corrected config.
2. **Expect:** The documented draft plus the hair amplitude correction will build and the assembled source coverage was 1812 uncovered error px, below the task bar.
3. **Chose / turned down:** I request --loop so the idle fold check exists, write build output under this run only, and do not add unmeasured patches.
4. **Happened** (2026-10-25T09:53:17Z): rigc build --profile rig-play --pack --page-edges free --pack-shape polygon: exit 0; 24 measured (24 passed, 0 failed).

## Entry 10 (opened 2026-10-25T09:53:47Z)

1. **Read:** TASK.md requires rigc render --folds over idle to name no mesh; rigc render --help says --folds writes folds.json and prints one line per folding mesh.
2. **Expect:** The green corrected build will render idle without any mesh fold line.
3. **Chose / turned down:** I render the compiled check skeleton into task-local evidence rather than treating build PASS as fold evidence.
4. **Happened** (2026-10-25T09:53:53Z): idle 41 frame(s), 3.333s + contact.png + folds.json (0 of 8 mesh(es) fold).

## At the end (2026-10-25T09:53:53Z)

- **Where I guessed:** The documented proposal and its one LINT-directed amplitude repair are sufficient for this painting.
- **What I could not find:** The package did not explain in §4 step 8 that propose --from-config still requires --out.
