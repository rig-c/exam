# Findings
- Retarget `--rig` takes the rig directory; `rigc build --rig` needs rig.json (EISDIR otherwise).
- `--stance 0.07` (card value) plants feet the Two-feet row wants lifted (bar threshold 0.04); 0.03 fixes that part.
- `--leg-scale` floor 0.8 clamps the shin on frames where the picture shin is 0.45 of straight (LEG-SCALE lines: frames 0-9, 31-41 ... asked 0.451-0.786); the lifted foot then sits low: median lift ratio 0.676. Floor 0.45 gives 0.913.
- `reach: true` on the trunk raised chest jitter to 1.39x sequence; without it 1.000x (hip is never rotated on this rig).
- Tried and reverted: translate.scale on the thigh (lift unchanged, jitter 2.2x).
- Not run: `rig-pose compare` (no detector output for the render).
