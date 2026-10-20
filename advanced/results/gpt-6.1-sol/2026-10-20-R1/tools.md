## Separate ankle precision from smoothing
- **I was trying to:** reduce rotation jitter while keeping supporting ankles on their reference horizontal track.
- **The tool gave me:** README “Few keys”: “Each ankle is held to the plant's tolerance plus the most the reduction may move it”; --help offers “--reduce <deg>” and “--reduce-hip <units>”. At 0.5 the report allowed foot tolerance 4.727 units and measured 3.645 units error; slide failed at 0.01094 L/frame. At 0.2 slide passed but jitter failed.
- **What would have helped:** a per-chain reduction tolerance or an explicit --reduce-foot-error world-unit bound that constrains reduction independently of trunk smoothing, with the predicted endpoint tolerance printed before fitting.
- **Cost:** roughly several minutes across three corrected trials and renders; eventually solved using the map change and 0.25 degrees, without per-chain controls.

## Warn when reach starts away from its source joint
- **I was trying to:** follow mid_hip→mid_shoulder using a trunk bone whose rig origin is above the hip.
- **The tool gave me:** README “The map”: “Without it, a tilted pelvis carries the chest's origin sideways and the trunk, parallel to the pose's, misses the shoulders.” The retarget landed every bone, but the initial grader read trunk jitter 1.588x source. Its green landing messages did not warn that the mapped origin was displaced by 180 units.
- **What would have helped:** a mapping diagnostic stating source segment start versus rig aim origin, its offset, and “reach re-aims from this displaced origin; compare angular jitter with reach off.”
- **Cost:** roughly a few minutes of investigating jitter and trial reductions; solved for the table by disabling reach, with endpoint matching limitation disclosed.
