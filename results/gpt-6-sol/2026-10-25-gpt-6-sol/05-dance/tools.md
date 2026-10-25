## Fresh output path for cloth proposal
- **I was trying to:** apply a `back hair` physics recipe to the task 02 config I had just copied.
- **The tool gave me:** `PROPOSE_WRITE_CONFIG_FRESH: ... exists; the config is written to a new file, never over the --cloth config or an earlier one`.
- **What would have helped:** The cloth recipe's command example should show distinct input and output config paths, then say to inspect and adopt the new file.
- **Cost:** About 5 seconds for the refusal and retry; I got there.

## Cloth ownership of a corrected idle track
- **I was trying to:** turn the back hair chains from idle keys into physics while preserving my task 01 hair correction.
- **The tool gave me:** `PROPOSE_WRITE_CONFIG_CONFLICT: config.motion.tracks[5] "hairback_l" ... the recipe's ... it holds amps [0.6,1.4,2.4] where the draft removes the entry`.
- **What would have helped:** The cloth recipe should say before the command that a corrected keyed track owned by the recipe must be removed from the input config when physics replaces that chain.
- **Cost:** About 10 seconds to interpret, remove the track, and retry; I got there.

## Contour coverage while reducing triangles
- **I was trying to:** keep a local soft topwear patch within the 700-triangle task budget.
- **The tool gave me:** `CONTOUR_COVERAGE: contour mesh "topwear" — 8 of 27280 art pixel(s) ... lie outside the mesh at tolerance 2 px and margin 1 px`.
- **What would have helped:** `mesh-stats` could report the smallest margin that covers this contour at the chosen tolerance, beside the refusal, so a budget iteration needs one fewer guess.
- **Cost:** About 10 seconds to raise margin to 2 and recount; I got there.
