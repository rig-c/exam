# Findings
- Map with all chains `bend:"free"` and face dials landed first try; gate green, 0 folds, 0 pass-through, 3 jumps detected (88-91, 179-181, 267-269) in every configuration.
- `--stance` above 0.04 leg lengths flattens lifted feet; 0.03 passes two-feet.
- `--reduce` trades slide against jitter (1°: 0.0165 / 1.15x; 0.5°: 0.011 / 1.34x; 0.25°: pass / 1.49x); not usable here.
- Trunk `reach:true` doubles the chest's jitter against the grader's pair reference (3.87 vs 1.91 deg/f²); without it 1.0x.
- Camera sidecar after/camera.json: 313 entries, t = frameTimes.
