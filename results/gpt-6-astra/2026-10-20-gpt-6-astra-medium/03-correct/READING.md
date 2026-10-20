# The proctor's reading — gpt-6-astra-medium, 03-correct, 2026-10-20

Regraded: 6 of 6, the same lines (8 meshes deformed; the back hair travels 45.881 rig px against 23). 3.7 minutes.

**What it found wrong, and from what.** `propose`'s own LINT: `hairback_r` and `hairback_l` carry opposed
amplitudes on one mass of back hair, triangle 167's edge 37–117 closes to 0.064 of its rest length, and the
same sign gives 1.046. It flipped `hairback_l`'s amplitudes to positive, kept their size, and graded. It never
built the draft — the lint named the failure one step before the build, which is what parts#314 put there.
The expectation that names the edge was written after the lint printed it, not before.

**The idle** (`idle_frames.jpg`, five frames): whole, nothing tears. The proctor built the draft as proposed
for comparison: it fails `CHECK_TEXTURE_STRETCH` on that same edge (0.065 at idle frame 22), and at that
frame the back hair on the image's right is visibly pinched up; in the run handed in it hangs.

**Journal.** Seven entries, no `WTF?:` — the lint had told it what would happen.
