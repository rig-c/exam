# Journal

## Entry 1 (opened 2026-10-25T09:57:27Z)

1. **Read:** @rig-c/parts README.md, The loop for an agent; task inputs layers
2. **Expect:** layers metadata prints without refusal
3. **Chose / turned down:** inspect both supplied layer runs before drafting the plan
4. **Happened** (2026-10-25T09:57:31Z): WTF?: the journal could not start rig-parts: [Errno 2] No such file or directory: 'rig-parts'; I expected the npm binary on PATH and will use node_modules/.bin/rig-parts explicitly.

## Entry 2 (opened 2026-10-25T09:57:36Z)

1. **Read:** @rig-c/parts README.md, Commands: layers; supplied full decomposition
2. **Expect:** full layer metadata prints with no refusal
3. **Chose / turned down:** invoke the installed binary by explicit path after PATH lookup failed
4. **Happened** (2026-10-25T09:57:40Z): WTF?: LAYERS_INPUT_KIND says inputs/layers/full does not exist; I expected the supplied directory and will inspect the task input entries.

## Entry 3 (opened 2026-10-25T09:57:46Z)

1. **Read:** Task 01 Given: inputs live under tasks/01-build; @rig-c/parts layers command
2. **Expect:** full layer metadata prints
3. **Chose / turned down:** use the repository task input path explicitly; the previous relative path was from the wrong working directory
4. **Happened** (2026-10-25T09:57:51Z): full layers: 29 layer(s), 0 with none, 0 WARN line(s)

## Entry 4 (opened 2026-10-25T09:57:51Z)

1. **Read:** Task 01 supplied head decomposition; layers command output
2. **Expect:** head layer metadata prints without refusal
3. **Chose / turned down:** inspect head run separately before proposing its placement
4. **Happened** (2026-10-25T09:57:56Z): head layers: 29 layer(s), 0 with none, 0 WARN line(s)

## Entry 5 (opened 2026-10-25T09:58:04Z)

1. **Read:** @rig-c/parts README.md, propose --head-box; task canvas 1664x2432
2. **Expect:** head-box proposal writes seethrough.head_box into config.json
3. **Chose / turned down:** use the package proposal rather than authoring a crop box by hand
4. **Happened** (2026-10-25T09:58:08Z): WTF?: CONFIG_FIELD_TYPE says config.seethrough is absent; I expected head-box writing to accept only key and scale, so I will copy the supplied See-through settings into the config.

## Entry 6 (opened 2026-10-25T09:58:13Z)

1. **Read:** Task 01 supplied seethrough.json; CONFIG_FIELD_TYPE refusal from previous head-box attempt
2. **Expect:** head-box proposal writes or preserves valid head_box
3. **Chose / turned down:** rerun with the complete seethrough object
4. **Happened** (2026-10-25T09:58:18Z): head_box [584,69,1111,596], 527x527, inside painting with no shift

## Entry 7 (opened 2026-10-25T09:58:19Z)

1. **Read:** @rig-c/parts README.md, assemble --propose-plan; full and head layer metadata
2. **Expect:** assemble plan proposal prints and exits 0
3. **Chose / turned down:** let assemble derive the plan from both supplied decompositions
4. **Happened** (2026-10-25T09:58:40Z): plan proposed 22 rows and extend_below_crop for hair_front and hair_back; four tiny full-run layers plus nose were intentionally unplanned

## Entry 8 (opened 2026-10-25T09:58:51Z)

1. **Read:** @rig-c/parts README.md, assemble command order; derived plan in config.json
2. **Expect:** assemble writes work/rig and reports recomposite with bounded uncovered holes
3. **Chose / turned down:** assemble using the package-proposed plan
4. **Happened** (2026-10-25T09:58:54Z): WTF?: CONFIG_FIELD_TYPE requires extend_below_crop entries to be objects, not strings; I will preserve the proposed part/run/tag records.

## Entry 9 (opened 2026-10-25T09:58:59Z)

1. **Read:** Previous refusal CONFIG_FIELD_TYPE on extend_below_crop; proposal stdout gave object records
2. **Expect:** assemble writes work/rig and reports recomposite
3. **Chose / turned down:** rerun after correcting the documented field shape
4. **Happened** (2026-10-25T09:59:54Z): assemble exited 0; recomposite uncovered error px 1812, 672 holes, largest 94 px; wrote 22 parts

## Entry 10 (opened 2026-10-25T09:59:54Z)

1. **Read:** @rig-c/parts README.md, propose --parts; assembled work/rig
2. **Expect:** proposal writes bones, meshes, regions and motion into config
3. **Chose / turned down:** use the package proposal and its overlay/basis rather than authoring rig geometry
4. **Happened** (2026-10-25T10:00:09Z): proposal wrote config sections; 47 bones, 8 meshes; one LINT on opposed hairback chains

## Entry 11 (opened 2026-10-25T10:00:09Z)

1. **Read:** Task 01 pass lines; @rig-c/parts build command
2. **Expect:** build exits 0 and check reports PASS
3. **Chose / turned down:** run the pinned build from the submitted config
4. **Happened** (2026-10-25T10:01:08Z): WTF?: build stopped at check with CHECK_TEXTURE_STRETCH on hair_back (ratio 2.445 > 1.926544), despite gate green; I will correct the opposed chain signs named by propose.

## Entry 12 (opened 2026-10-25T10:01:16Z)

1. **Read:** Previous build CHECK_TEXTURE_STRETCH; propose named opposed hairback amplitudes and said same sign gives 1.051
2. **Expect:** corrected build exits 0 with check PASS
3. **Chose / turned down:** make the documented same-sign correction and rebuild
4. **Happened** (2026-10-25T10:02:04Z): corrected build exited 0; check: PASS, 11 of 11 bars measured, uncovered_error_px 1812

## Entry 13 (opened 2026-10-25T10:02:09Z)

1. **Read:** Task 01 does not fold pass line; rigc render --help --folds
2. **Expect:** folds render exits 0 and names no folded mesh
3. **Chose / turned down:** render the built candidate with the package's folds reader
4. **Happened** (2026-10-25T10:02:14Z): rendered idle 41 frames; folds.json says 0 of 8 mesh(es) fold

## Entry 14 (opened 2026-10-25T10:02:15Z)

1. **Read:** Task 01 pass lines; README grading rule
2. **Expect:** grader prints task 01 status lines and writes result.json
3. **Chose / turned down:** run the official local grader before finishing the task
4. **Happened** (2026-10-25T10:03:26Z): grader printed PASS built, checked, whole and does_not_fold; journal chain intact with 14 entries and 5 WTF

