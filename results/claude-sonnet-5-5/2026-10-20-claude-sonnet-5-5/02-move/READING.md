# The proctor's reading — claude-sonnet-5-5, 02-move, 2026-10-20

Regraded: 7 of 7, the same lines — 8 bones on physics, `wave` 2.4 s with a rise of 382.4. 6.6 minutes by
the run's own lines.

**What it did.** Task 01's config, a `wave.json` beside it named by `motion.animations_from`, and eight
physics constraints on the two free hair strands (`lock0`–`lock3`, `lock1_0`–`lock1_3`). The physics
values are the documented strand recipe: root inertia 0.8, strength 90 tapering by 1 − 0.35·i/(n−1)
(90, 79.5, 69, 58.5), damping 0.85. The wave is its own: `sleeve_l0` raised to 95° and held, the forearm
and hand rocked ±22° and ±14°, a small head tilt. It worked out which sleeve is on the image's right from
the chains' x positions and confirmed it by rendering the wave and looking.

**Journal.** Two entries, no `WTF?:`; both results were as expected.

**The transcript.** The step that wrote the config and `wave.json` is a one-line summary; the files are
handed in. Paths inside the clone are shown as `<clone>`.

`wave_frames.jpg`: six frames of `wave`, rendered by the proctor from the regrade's build.
