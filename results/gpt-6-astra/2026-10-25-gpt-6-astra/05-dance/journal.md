# Journal

## Entry 1 (opened 2026-10-25T11:44:09Z)

1. **Read:** TASK05; fixture README The joints, Feet are planted, Signs, Known limits; parts named-animation recipe
2. **Expect:** 4s loop closes exactly, hand excursions over100, trunk over15, planted ankles remain fixed and repeated 1s groove meets 2-beat timing.
3. **Chose / turned down:** Fixture unchanged except animations_from. Authored hip x±18 and y -12..-28, chest±2, head±5, shoulders -40..4 / -4..40, elbows -38..-6 /6..38, wrists±12, sampled sinusoidal 1s phrase with half-second dip. IK mix1 and root foot targets untouched; no extra rig or physics.
4. **Happened** (2026-10-25T11:47:25Z): 11 of 11 line(s), 3 skipped; hands187.6/189.7, trunk31.8, foot gap4.71, timing1.0, closes0.0. Check passes with SEAM_OVER_MOTION WARN, to inspect visually before hand-in.

## At the end (2026-10-25T11:47:48Z)

- **Where I guessed:** Dance amplitudes and phases authored, not from reference animation: hip18px sideways and -20±8 vertically, chest2deg, head5deg phase-.2, shoulders22deg about ±18, elbows16deg about ±22 phase-.5, wrists12deg phase-.8. 16 samples/second chosen for smooth periodic motion. Fixture README supplies names, joint ranges and planted-foot IK. No constraint keys; both iks remain mix1. Contact sheet reviewed; four SEAM_OVER_MOTION warnings remain, largest left knee47px over33 frames at12fps, despite machine gates passing.
- **What I could not find:** Seam warning gives part/frame/pixel counts but not posed joint angle, making comparison with declared ranges indirect. Recorded in tools.md; no rig edits permitted or attempted.
