## rig --rig argument differs between retarget and build
- **I was trying to:** build the retargeted motion with `rigc build` using the same `--rig` I gave `rig-pose retarget`.
- **The tool gave me:** `rigc compile error: cannot read .../inputs/rig: EISDIR: illegal operation on a directory, read (see rigc guide CE_COMPILE_JSON_READ_FAILED)`
- **What would have helped:** the error saying "--rig takes rig.json, not a directory (inputs/rig/rig.json exists there)", or rigc build accepting the directory like retarget does.
- **Cost:** about 3 minutes; got there.

## No link from the card's --stance / --leg-scale values to the lift they flatten
- **I was trying to:** get the lifted foot to the sequence's lift height after the card values left median rig/sequence lift at 0.616–0.676.
- **The tool gave me:** `STANCE lifted: free foot r frames 0–10 ... the pose's height kept` and `LEG-SCALE ... 77 frame(s) under 0.8, clamped (frames 0–9, ... asked 0.451–0.786)`; the README/help say `0.8,1.05 is the card's range` and `0.07 is the card's`.
- **What would have helped:** a retarget line comparing each foot's lift in the rig with the picture's per support span, naming the clamp that caused the shortfall.
- **Cost:** about 25 minutes (two wrong tries, including changing the translate scale); got there.

## reach: true on a trunk raised jitter with no hint
- **I was trying to:** keep the chest from drifting off the shoulders, as the README recommends for a trunk bone.
- **The tool gave me:** README: "`reach: true` ... Without it, a tilted pelvis carries the chest's origin sideways"; nothing in retarget output about the trunk's jitter.
- **What would have helped:** a retarget line with the keyed trunk/head jitter against the pose's, or a README note that reach is only for a pelvis that turns.
- **Cost:** about 10 minutes of trial (found by dropping it); got there.

## Retarget output is too long to read the verdict
- **I was trying to:** read what changed between two retarget runs.
- **The tool gave me:** about 100 lines per run (dozens of STANCE, IDLE-DROPPED, FEET blend lines), and `rigc`/`rig-pose` help pages of 300+ lines that the terminal tool persisted to files.
- **What would have helped:** a `--summary` option printing one line per measure (gate, feet, lift, jitter), or a grouped count for repeated per-cycle lines.
- **Cost:** about 10 minutes of paging; got there.
