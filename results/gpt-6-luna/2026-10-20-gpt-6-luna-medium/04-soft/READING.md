# The proctor's reading — gpt-6-luna-medium, 04-soft, 2026-10-20

Regraded from the handed-in files on a second checkout: 9 of 9, the same lines — 662 triangles,
`topwear` 6.61 rig px off its physics-free twin, 8 of 115 vertices moving. Clock 7.0 min.

**What the journal caught.** Six entries, five marked — four distinct surprises, all one search for the
triangle budget:

- `WTF?: grader found 816 triangles, over the 700 budget; the other 8 lines passed, with 6.61 px soft motion and 44/192 vertices moving.` (entries 1 and 2 carry this same line; entry 1's line 4 was filled in with the grader's result rather than with what writing the config did)
- `WTF?: 16 px spacing reduced the rig from 816 to 762 triangles, still 62 over budget; patch readings remained within range.`
- `WTF?: region spacing 26 px reduced the total to 732 triangles, still 32 above budget; soft motion remained 6.61 px with 14 patch vertices.`
- `WTF?: the rig fell to 662 triangles, but only 7 vertices moved over 0.5 px, one short of the patch minimum; soft displacement stayed 6.61 px.`

The run ends one vertex over the patch floor, found by trial: the documents say coarser spacing means
fewer triangles, and nothing said how many triangles a spacing would cost before building it. That is
the tool question in these lines.
