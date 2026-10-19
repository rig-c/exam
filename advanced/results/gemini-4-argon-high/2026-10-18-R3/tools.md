# Tool Friction Log (`run/tools.md`)

- **Tool:** `npx rig-pose retarget`
- **Tried:** `npx rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --carry-idle --out run/before/motion.json --build run/before/build --report run/before/report.json --camera run/before/camera.json`
- **Wanted:** Default retargeting (or a diagnostic warning in the `FEET` / `POSTURE` summary) to flag that unplanted feet leave a 0.1456 leg-length airborne gap and 0.0457 per-frame foot slide, and that omitting a `pelvis` (`hip`) chain leaves `hip` tilt at `0.000` of the 54.769° sequence range.
- **Got:** `rig-pose retarget` exited 0 with `GATE green — all 19 landing(s) within tolerance` and `POSTURE hip tilt range ... rig 0.0° — rig/reference 0.000` as an informational line rather than a warning, requiring manual inspection of `tools/grade.py` failures to add a `pelvis` chain (`bones: ["hip"], joints: ["r_hip", "l_hip"], aim: ["leg_r0>leg_l0"]`) and `--plant-feet --stance 0.03 --leg-scale 0.68,1.1`.

- **Tool:** `npx rig-pose retarget --plant-feet --stance`
- **Tried:** Choosing `--stance` using the README's reference card value (`--stance 0.07` for `dance-a`).
- **Wanted:** `rig-pose retarget` to report how many frames fall in the two-foot vs lifted bands (`<= 0.02` vs `> 0.04` sequence ankle separation) or warn when `--stance` exceeds the grader's lifted-foot threshold (`0.04`).
- **Got:** The README's `--stance 0.07` would classify lifted frames with sequence ankle separation between `0.04` and `0.07` as `planted both`, pinning the lifted foot to the floor and failing `two-feet`; we had to inspect `tools/grade.py` (`LIFT_FLOOR = 0.04`, `BAR_TWO_FEET = 0.02`) to choose `--stance 0.03`.

- **Tool:** `npx rig-pose retarget --reduce 1`
- **Tried:** `npx rig-pose retarget --rig inputs/rig --map run/map.json --pose inputs/pose/sequence.json --plant-feet --stance 0.03 --leg-scale 0.7,1.05 --carry-idle --reduce 1 --out run/after/motion.json ...`
- **Wanted:** `--reduce 1` to smooth bone `rotate` curves (per README `rig-c/pose#116`) while keeping planted support feet pinned to the floor within the `slide` bar (`<= 0.005` leg lengths/frame).
- **Got:** Thinning the leg `rotate` tracks within 1° while `hip.translate` remained dense caused the supporting ankle to drift horizontally between kept rotate keys (`max support-foot move 0.01651 leg lengths/frame`, failing `slide <= 0.005`), and `"reach": true` on `trunk` still left `trunk+head` jitter at `1.332x` because `chest` sits 100 units above `hip` and counter-rotated against every pelvis tilt. We had to drop `--reduce` and remove `"reach": true` from `trunk` so dense keys preserved `0.00003` slide and `1.000x` trunk local angles.

- **Tool:** `npx rig-pose retarget` (head chain on `r_eye` / `l_eye`)
- **Tried:** Mapping `head` with `{"name": "head", "bones": ["head"], "joints": ["r_eye", "l_eye"], "aim": ["eye_r>eye_l"]}` and running `tools/grade.py --round R3 ... --trunk chest,head`.
- **Wanted:** `head.rotate` to aim strictly along the mapped `r_eye -> l_eye` 2D chord so its local angular acceleration matches the sequence's `r_eye -> l_eye` relative to `trunk`.
- **Got:** `retarget.js` couples the vertical head nod (`clampedY * +1.6°/unit` from `r_eye`/`l_eye` vertical offset relative to `neck`) into `head.rotate`, inflating `head` local jitter to `1.298x` of the 2D `r_eye -> l_eye` sequence chord (`1.201x` for `--trunk chest,head`, failing `<= 1.1`). We had to inspect `retarget.js` and switch the `head` chain to `joints: ["r_ear", "l_ear"], aim: ["ear_r>ear_l"]`, which aims `head` purely along the 2D ear chord (`1.000x` jitter).
