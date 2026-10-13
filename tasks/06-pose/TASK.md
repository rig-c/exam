# Task 06 — motion from a pose

The painting of task 01, and a rig for it that builds — yours from task 01, changed as you need. This time
the motion is not yours to key: it is a real dancer's, measured from a video, and it goes on with
`@rig-c/pose`.

## Given

- Task 01's inputs (`../01-build/inputs/`).
- `inputs/toca.pose.json` — the dance: a `rig-pose-sequence/1` file, 492 frames at 30 frames a second
  (16.37 s), one dancer seen from the front, her joints by name on every frame. Joint positions only: no
  picture, no sound. Where it comes from is in `inputs/NOTICE.md`.
- `inputs/keypoints.json` — where the painting's joints are, as `@rig-c/parts` reads them
  (`spine-parts-keypoints/1`). Her shoulders and hips are under her sleeves and her skirt; you cannot see
  them, so they are given.
- `@rig-c/pose`, at the version `../../package.json` pins, beside the two packages of the earlier tasks.

## Do

Make the rig take the dance. The grader builds your config as task 01 does, and then runs

    rig-pose retarget --rig out/rig --map map.json --pose <inputs/toca.pose.json> --out pose/motion.json \
      --name toca --build pose/build --report pose/report.json <your flags>

which must exit 0. A map says which bone carries which of the dancer's joints; the flags are yours to
choose. As task 01 left her, her arms hang on chains whose links are not at her elbows, and her legs are one
flat piece on the hip: no bone in her carries a knee. What a rig needs before a pose can move it, how a map
is written and which flags a sequence like this one calls for are in the packages' documents.

A bone turns; it does not get shorter. Where the dancer points a limb at the camera, a flat drawing turned
by its bones cannot follow her — that is a job for a second drawing of the limb, and not this task. What is
graded is that the bones follow her wherever they can, and that your run says where they cannot.

## Hand in

`config.json` (and any motion file it names), `map.json`, `retarget.json`, `journal.md`, and the transcript.
`retarget.json` holds the flags you chose for the command above, as `{"flags": ["--flag", "value", …]}`,
from `--min-score`, `--smooth`, `--flip`, `--short`, `--bends` and `--bend-tolerance`; the grader sets every
other. Every `.json` file in your run directory is copied beside the inputs before the build.

The grader runs the retarget itself. Your own report, build and render are yours to read; they are not
handed in.

## Pass lines (written before any run)

Task 01's four (built, checked, whole, does not fold), and:

| | line |
| --- | --- |
| **Retargeted** | the command above exits 0 with your `map.json` and your flags: the rig's gate is green with the dance in, and every bone the map names lands where the dancer's joints ask |
| **Limbs follow** | each of the eight limb bones misses the dancer's segment by at most 10 degrees on nine frames in ten |
| **Hips tilt** | the bone `hip` tilts over at least half the range the dancer's hip line does |
| **Hips travel** | the bone `hip` travels at least half as far as the dancer's hips do, at the rig's scale |
| **End-on reported** | the run's report lists, as end-on, the two spans in which this dancer points a limb at the camera — her right upper arm, frames 395 to 401, and her right shin, frames 365 to 370, each end within 3 frames — and at most 4 spans in all |
| **On her feet** | the end of each leg stays within 6 rig px of its shoe |

The dance is posed at 30 frames a second, the source's rate, from the retargeted build.

**The limb bones** are read by the names `rig-parts propose --keypoints` gives them: `sleeve_r0` (her right
upper arm, shoulder to elbow), `sleeve_r1` (her right forearm, elbow to wrist), `sleeve_l0`, `sleeve_l1`,
`leg_r0` (her right thigh, hip to knee), `leg_r1` (her right shin, knee to ankle), `leg_l0` and `leg_l1`;
`r` and `l` are her own sides. A bone renamed is not found, and its line fails. A bone's miss on a frame is
how far it has turned from the rig's setup pose, less how far the dancer's segment has turned from where
`keypoints.json` puts it on the painting. Nine frames in ten leaves room for the frames the package's own
flags hold or spread; a limb that stays where it is, or follows the other side's joints, misses by more than
10 degrees on more frames than that on this dance.

**The hips**: the tilt is the turn of the bone `hip` against the setup pose, and the dancer's is the angle of
the line from her right hip to her left; each is read as the range from its 5th to its 95th percentile over
the frames. The travel is the diagonal of the box the bone's origin fills, between the 5th and 95th
percentiles of each axis, and the dancer's is the same for the midpoint of her hips, scaled by her trunk
(neck to that midpoint, its median over the frames) against the painting's (the same two points in
`keypoints.json`, at the rig's scale).

**End-on**: the report is the one `--report` writes; a span is an entry of its `endOn` list, matched by the
two joints of its segment.

**On her feet**: the legs are every part whose name begins `legwear`, the shoes every part whose name begins
`shoe`. At the setup pose, the leg vertices in the lowest 4 % of their height are split into two legs at the
widest gap between them; each leg's end is the middle of its vertices there, and its shoe is the two shoe
vertices nearest it. The line reads how far the distance from the end to either of them changes over the
frames — a shoe that turns with its shin keeps it, a shoe left where it was painted does not.

A person looks at the dance beside the dancer's joints, drawn as a stick figure frame for frame, for every
run; that reading is recorded beside the machine's, and does not change it.
