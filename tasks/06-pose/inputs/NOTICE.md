# Where task 06's inputs come from

## `toca.pose.json` — the dance

- **Source:** *Toca Toca*, a public dance challenge, as posted at
  https://www.youtube.com/shorts/HSug-0AAp3k — credited here by its URL. The dance and the video are their
  creators'; this repository claims nothing in them.
- **What is here:** joint positions only — for each of the video's 492 frames (30 frames a second, 1080 × 1920),
  the dancer's body-18 joints by name, each a position in the picture's pixels (y down), a state and the pose
  model's score. No frame, still, crop or sound of the video is in this repository, and none was used to make
  anything else in it.
- **How it was measured:** RTMPose whole-body (`rtmw-dw-x-l`, rtmlib's `balanced` mode) on onnxruntime, on the
  CPU. The 17 body joints keep their COCO names, renamed to body-18 (`left_*` → `l_*`, the subject's sides);
  `neck` is the midpoint of the shoulders, scored the lower of the two; a joint scored under 0.3 is
  `occluded` (none is, on this video). The dancer is, on each frame, the person whose body joints scored at
  least 0.3 (five or more) span the most height, because the video carries a small inset near its top with
  figures of its own: on every frame the person picked spans at least 958 px of the picture's 1920 and has no
  joint above y 532. The file is that measurement as it came out, written in the `rig-pose-sequence/1`
  format `@rig-c/pose` reads; no joint was moved by hand.

## `keypoints.json` — the painting's joints

Placed by hand on task 01's painting (`../../01-build/inputs/painting.png`), in its pixels. The elbow and
wrist heights are task 05's stated fractions of each arm part's height; the shoulders and hips, under the
sleeves and the skirt, are estimates and marked `occluded`. The painting and everything read off it are
this repository's, under its licence (`../../../LICENSE`).
