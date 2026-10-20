# The proctor's reading — gemini-4-argon-high, 03-correct, 2026-10-20

Regraded: 6 of 6, the same lines (8 meshes deformed; the back hair travels 45.881 rig px against 23). 10.9 minutes.

**What it found wrong, and from what.** `propose`'s own LINT: `hairback_r` and `hairback_l` carry opposed
amplitudes on one mass of back hair, triangle 167's edge 37–117 closes to 0.064 of its rest length, and the
same sign gives 1.046. It flipped `hairback_l`'s amplitudes to positive, kept their size, checked with
`propose --from-config` (0 LINT lines), built (severity 1.045) and graded. It never built the draft; the lint
named the failure one step before the build. Every sitting this day made the same flip, which the lint itself
prints as the remedy.

**The idle** (`idle_frames.jpg`, five frames): whole, nothing tears. The proctor built the draft as proposed
for comparison: it fails `CHECK_TEXTURE_STRETCH` on the same edge (0.065 at idle frame 22). At this render
size the difference is a sliver of the back hair's outline beside the head; the defect is one small triangle.

**Journal.** Six entries, no `WTF?:`; the lint had told it what would happen. The transcript keeps the
commands' output in excerpt; the step that pasted the proposal and flipped the sign is not in it.
