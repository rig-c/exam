# The proctor's reading — claude-fable-5-1, 03-correct, 2026-10-20

Regraded: 6 of 6, the same lines (8 meshes deformed; the back hair travels 45.881 rig px against 23). 11.1 minutes.

**What it found wrong, and from what.** `propose`'s own LINT: `hairback_r` and `hairback_l` swing with opposed
amplitudes on one ponytail, triangle 167's edge 37–117 closes to 0.064 of its rest length, the same sign
gives 1.046. It flipped `hairback_l`'s amplitudes to positive, kept their size (with a `note` beside them),
and changed nothing else. It never built the draft. The expectation naming the fix was written after the lint
printed it.

**The idle** (`idle_frames.jpg`, five frames): whole, nothing tears. The proctor built the draft as proposed for
comparison: it fails `CHECK_TEXTURE_STRETCH` on that same edge (0.065 at idle frame 22); at that frame the
two renders differ only around the head and hair (133 pixels by more than 40 at 323×768).

**Journal.** Six entries, no `WTF?:` — the lint had told it what would happen.
