# Journal

## Entry 1 (opened 2026-10-25T09:12:29Z)

1. **Read:** Fixture README The joints/Feet are planted/Signs; task05 timing and thresholds; parts AUTHORING named animations
2. **Expect:** 4s groove passes11 measured lines: alternating arm reach >100, trunk travel>15, fixed ankle targets, closed loop and 1s speed pattern.
3. **Chose / turned down:** Fixture config unchanged except motion.animations_from. Author 24fps sampled sine keys on hip x+/-24 y-28..-8 roll+/-2; shoulder r-44..0/l0..44, elbow+/-30max, wrist+/-12, head+/-6. Period1s, bounce.5s, exact boundary. No IK/target changes or new rig objects.
4. **Happened** (2026-10-25T09:16:48Z): WTF?: All11 measured lines pass, but checked reports SEAM_OVER_MOTION WARN. Build log names thigh_l|shin_l17 frames max50px and neckpiece|headpiece9frames max6px despite ranged joints passing. Fixed IK targets also yield4.95px art-end distance, not zero. Contact sheet shows the intended alternating arm groove; retain the rig and disclose warnings.

## At the end (2026-10-25T09:16:48Z)

- **Where I guessed:** Dance amplitudes, sinusoidal phase offsets and 24fps sample density are my choreography choices; joint bones and signs from fixture README The joints and Signs; IK from Feet are planted. No constraints keyed.
- **What I could not find:** Why static SEAM_OVER_RANGE passes while played knee/neck seam warns; fixture Known limits notes nape/hip/shoulder boundaries but does not predict this knee warning.
