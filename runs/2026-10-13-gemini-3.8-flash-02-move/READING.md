# The proctor's reading — gemini-3.8-flash, 02-move, 2026-10-13

Regraded from the handed-in files on a second checkout: 7 of 7, the same lines as the run's own
`result.json` and as the examinee's report.

**Does it read as a wave** (`wave_frames.jpg`, six frames): yes, and it is the clearest of the runs so
far — the upper arm lifts, the elbow bends, and the hand swings four times at the top. Nothing folds.

**What the journal caught.** Nothing marked; three entries, the thinnest journal of the runs. Two things
from the closing note and the report:

- The rotation angles were worked out "geometrically from bone lengths and angles", and the report says
  the longest step was establishing the coordinate convention — it read `rig-c`'s `src/transform.ts`
  ("World rotation in degrees, CCW, y up") to learn which way a positive key turns an arm. The recipe for
  a named animation in AUTHORING does not say which way positive is. Filed on the tool.
- The physics values came from `rig-c`'s `src/rig.ts` defaults — the examinee went to the compiler's
  source for what the parts guide pointed to an unshipped example for. Fixed in `@rig-c/parts` 1.12.0.

Physics is on two bones, one link of each side lock: the least that passes the line.
