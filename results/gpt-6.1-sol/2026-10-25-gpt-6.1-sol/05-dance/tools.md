## Predicting a seam-safe torso gesture
- **I was trying to:** Make a small head turn and chest lean on the painted figure without opening the armhole.
- **The tool gave me:** AUTHORING, "A raised arm moves its `handwear` part only": "the `topwear` part on `chest` and `hip` alone". My first task02 grader returned `"topwear|handwear_l": {"frames": 12, "max_px": 35}` even though the gesture keyed no limb.
- **What would have helped:** A seam-motion preflight that names the shared boundary whose weights disagree under a proposed chest key, or a sentence that even a small torso lean can separate a chest-carried sleeve from a chest/hip-blended top. The named-animation recipe explains a raised arm, but I needed the torso case.
- **Cost:** Roughly two minutes for another build/grade and narrowing the gesture. Head-only rotation passed all eight lines, travelling 33.9 rig px.

## Explaining static-range PASS versus played-seam WARN
- **I was trying to:** Dance on the fixture using its documented ranged joints and planted-foot IKs.
- **The tool gave me:** The package build printed `SEAM_OVER_RANGE: PASS` and then `WARN seam "thigh_l|shin_l" opens on 17 frame(s)` with `max 50 px in "dance"`; it also named `neckpiece|headpiece`, nine frames, max 6 px. The final check remained PASS, with SEAM_OVER_MOTION explicitly "never a bar". Fixture README, The joints, says each declared joint is read at -45, 0, +45, but that is a different reading from the played seams.
- **What would have helped:** The warning naming the posed joint angle and whether cap coverage, IK pose, or the seam reader explains the difference from the static test, plus a direct command to render that warning frame at the joint. Static range acceptance alone did not tell me what to change in choreography.
- **Cost:** Roughly four minutes for the dance grade and inspection of its log/contact sheet. All eleven measured lines passed, but I retained and disclosed both seam warnings; I did not change the supplied rig or claim those seams were clean.
