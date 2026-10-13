# Scratch: a polish task, drafted and sat twice (2026-10-13)

**Not part of the graded exam.** This is a draft of a possible future task, kept with the two sittings that tried it.

## The task

`problem/PROBLEM.md` (in Korean). A rigged character dances a reference dance that was retargeted from video joints with `@rig-c/pose`. The examinee compares the rig with the video one body unit at a time (head, arms, body, legs, cloth), finds what is wrong, classifies each finding (fix the rig / fix the motion / paint a new drawing / a tool should have done it), fixes what it can, and reports. The journal, transcript and `tools.md` rules are this exam's.

## What is not here

The task was sat with the reference video, its audio and a video | rig demo clip. **None of that footage is in this repository.** Neither are the sitters' evidence images or after-clips, which set video frames beside the rig. What remains is everything without a frame of the video in it:

- the joint positions measured from the video (`problem/inputs/reference/pose.json`);
- the rig, its five alternate drawing sets and the retargeted dance;
- each sitting's journal, transcript, findings, report, `tools.md` and its fixed rig and motion files.

Paths in the sittings' files that pointed at the problem folder are written as `<problem folder>`.

The dance is one performance of the *Zero Two* dance challenge, https://www.youtube.com/shorts/BGyjsZsWndA, credited by that URL. Who first choreographed it is not known to us, so no choreographer is named, and this repository claims no authorship of the movement. The joint data is under this repository's licence, CC BY-NC 4.0, so it may not be used commercially.

## The sittings

| sitting | model (as given by the person who started it) | sub-agents | wall clock |
| --- | --- | --- | --- |
| `runs/astra/` | GPT "Astra" | 0 | 19 min |
| `runs/fable/` | Fable 5.1 | 0 | 25 min (three classifier interruptions included) |
| `runs/roa-hq/` | the HQ session (Opus 5.5) that built the rig: **not a sitting**. It had seen everything and started from the owner's findings; see its REPORT.md | 2 (Opus 5.5, arms and cloth) | 19 / 49 min in parallel |

Both were started at the same time, in fresh sessions, each in its own copy of the problem folder, local only.

**What the two had in common.** Both found that the eyes never blink and that the supporting foot drifts off the floor, and both fixed those. Neither found the two largest faults a person found on the same demo: the skirt passing through the legs, and an arm drawn under the jacket in the low-hands span. Their after-clips differ from the given demo on about 5 % of rig pixels, and from each other on about 4 %. The motion under both came from the same retarget.

**What it taught.** The task measured careful touch-ups more than finding, and the ceiling was the retarget underneath. A version worth grading would pair the task with a measured gap report (rig-c/pose#38) and score how far the gap closes. What both sittings' `tools.md` named went to rig-c/pose#43 and rig-c/core#1414.
