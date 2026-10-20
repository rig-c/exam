# Tools: what I was missing

## The journal's line 4 has no defined form for a result that matched
- **I was trying to:** write line 4 of an entry when the step did what I expected.
- **The tool gave me:** JOURNAL.md says "line 4 begins with `WTF?:` when the result differs" and gives no form for a match. The grader counts entries "whose line 4 begins `WTF?:`". Writing `4. WTF?: no` looked like a surprise to me, and `4. **Happened:**` does not match the grader's count either.
- **What would have helped:** one sentence in JOURNAL.md saying whether a numbered prefix counts as "begins", and what line 4 should say when nothing differed.
- **Cost:** about 15 minutes; I had to re-number and re-mark three journals after writing them out of order.

## The journal's entry order is easy to break
- **I was trying to:** keep entries 1 to n in order with line 4 right after line 3.
- **The tool gave me:** JOURNAL.md ends with "## At the end", and its template entry sits above that. I appended entries after the template, and a split on "## At the end" moved one entry's text into a temporary file.
- **What would have helped:** a journal file that is empty of template text, or a `journal` command that appends a numbered entry and fills line 4 separately.
- **Cost:** about 10 minutes on task 01 to recover Entry 1; about 10 more on task 05 where line 4 of several entries landed under the wrong entry.

## Reading AUTHORING.md with the reading tool
- **I was trying to:** read the §4 command order and the §3 config fields of `@rig-c/parts` `docs/AUTHORING.md`.
- **The tool gave me:** the file is 323 KB with very long lines, and every read over about 40 KB was saved to a file I had to read in pieces; I also did not want to read the saved copies, since they sit outside the clone.
- **What would have helped:** a table of contents with byte offsets, or `docs/` split into one page per section.
- **Cost:** about 15 minutes of byte slicing (`grep -b` plus `tail -c`) to get to §4.

## `animations_from` is resolved beside the config file, and the refusal does not say so
- **I was trying to:** build a no-physics twin of the task 04 rig from `work/config_nophys.json`.
- **The tool gave me:** `FAIL  CONFIG_FILE_PRESENT: config.motion.animations_from — names …/runs/…/work/animations.json`. The path was right, and the file was not there; the docs say to write the file "beside the config".
- **What would have helped:** "relative to the config file's folder" in the refusal, or a copy of the twin's motion file made by the tool.
- **Cost:** about 3 minutes; I copied the file.

## Which pose file goes to `--keypoints` on a seated figure
- **I was trying to:** give `propose --keypoints` the joints of a seated figure, using the `pose_seated.json` the task supplied.
- **The tool gave me:** AUTHORING §3 *A posed figure* asks for `spine-parts-keypoints/1` in painting px, while `pose_seated.json` is a control pose (`width 832`, `height 1216`, 18 named `points`, a `generation.control.skeleton` file). Nothing in the tool says which of the two a file is until you pass it.
- **What would have helped:** a `propose --keypoints` refusal that names the format it found (`KEYPOINTS_SPACE_STATED` fires only on a bad space), or one sentence next to the example file in the task.
- **Cost:** about 8 minutes deciding not to pass it.

## Contour mesh and two islands: which bones take a bridge's vertices
- **I was trying to:** give the two legs of `legwear` a contour mesh, so no vertex sits in the gap between them.
- **The tool gave me:** `FAIL  CONTOUR_ONE_ISLAND … its art is 2 separate 4-connected islands … one island is required`. `bridges: true` then built, with the legs' bones blended across the bridge (the weights summary lists four bones per vertex).
- **What would have helped:** AUTHORING §3 saying which bones a bridge's vertices take, or a bridge option that does not blend two chains.
- **Cost:** about 40 minutes across three builds; the line I was trying to pass (`On her feet`) still fails at 21.5 rig px.

## Geometry JSON layout and the "travel" definitions
- **I was trying to:** measure the pass lines on the rendered `dance`.
- **The tool gave me:** `rigc render --geometry` says "every slot's region or mesh vertices in world units", but not the layout of `attachments[].vertices` (flat x, y pairs), and the task says "travel is the diagonal of the box a vertex's path fills", while "furthest vertex … measured from the middle of topwear" and "measured from the middle of shoes" do not say what the reference point is for each vertex.
- **What would have helped:** one example of a geometry frame in the README of `rigc render`, and the reference point written into each line.
- **Cost:** about 15 minutes to read the layout and settle the reading; I wrote my own measure script (`work/measure_dance.py`).

## Which frames the soft line samples
- **I was trying to:** check the `Soft` line on `hop` myself before handing in.
- **The tool gave me:** my own furthest-vertex figure on `hop` was 6.305 rig px, and the grader printed 6.61 "at hop frame 14". The task does not say which frames or fps the grader samples.
- **What would have helped:** the sampling (fps and frame range) in the task's pass line.
- **Cost:** about 5 minutes; both figures are inside the 3 to 15 band, so it changed no decision.
