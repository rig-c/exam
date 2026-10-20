# The proctor's reading — gpt-6-luna-medium, 05-dance, 2026-10-20

Regraded from the handed-in files on a second checkout: 5 of 14, the same lines as the run's own
`result.json`. Clock 9.2 min. Stopped and handed in as stopped.

| line | regrade |
| --- | --- |
| built | FAIL — `rig-parts build exit 1` |
| checked | FAIL — `CHECK_SEAM_WITHIN_BAR` (the only bar not met; 10 of 10 measured) |
| whole | PASS — uncovered_error_px 2059 against <= 4200 |
| does not fold | PASS |
| budget | PASS — 898 triangles against <= 1000 |
| dance as timed | PASS — 4 s |
| closes, both hands, whole body, arms bend at the joints, on her feet, keeps time, soft in the dance | FAIL — not measured: the build without its physics did not build |
| dance does not fold | PASS |

**What the run did.** It found the right idea in the documents: two two-bone leg chains under the hip, foot
targets on a ground bone, IK from each shin to its foot, and `legwear` turned into a mesh weighted to
the new bones. The first build's seam check refused the legs (`legwear`, 20,499 px, and 38 triangles
inverted at the setup pose). The run diagnosed that as bone positions written in rig coordinates where
the spec reads them as parent-local, rewrote the new leg bones and foot targets as parent-local (the
thighs now start at `[0, 0]`), and graded again.

**What the regrade found, against what the run says.** The run's last report says the leg seam was
fixed by that rewrite and that only the physics-free comparison build failed, on a `(no art) / (no art)`
seam. The regrade reads otherwise: the run's **own** build fails the same `CHECK_SEAM_WITHIN_BAR`, with the
same numbers as the comparison build, because physics has nothing to do with it. Its four seam pairs:

| pair | px over 40 |
| --- | --- |
| (no art) / (no art) | 17,095 |
| `legwear` / (no art) | 16,821 |
| `legwear` / `bottomwear` | 262 |
| `legwear` / `shoes` | 58 |

`seam_legwear.png` shows why: at the setup pose both legs are drawn far up and to the left of the figure,
turned on their side, and the place where her legs are painted is empty. The rewrite reduced the leg's
own mismatch (20,499 to 16,821 px) and did not put the legs back. The `(no art) / (no art)` pair is
the same legs seen from the other side — a mismatch where the flat composite has no part either.

The diagnosis itself runs the wrong way, by the run's own config: every bone the proposal wrote is in
rig coordinates — `chest` rests at `[446, 325]` under `hip` at `[446, 425]` — and so were the first
build's legs. Rewritten as offsets, the thighs start at `[0, 0]`, which is the top left of the rig, and that
is where the picture draws them. What made the first build's legs miss is not established here.

**The dance** (`dance_frames.jpg`, one frame a beat; `dance_first_second.jpg`, one every 4 frames): with
the legs off in the corner, the figure is a trunk floating over two shoes. Within that, the arms swing out
and back on a one-second phrase and the trunk sways a little. Read off the build with its physics, for
information and not as lines: the hands travel 391 and 318 rig px; the trunk's least-travelling vertex 8.2
rig px against the 15 the line asks; the leg ends get 40.6 rig px from the shoes against 6; the phrase
repeats every two beats exactly. A judged clip is rendered separately and carries no name.

**What the journal caught.** Two entries; one marked:

- `WTF?: initial grader run was combined with the config write without a separate pre-run journal entry; grader reported `CHECK_SEAM_WITHIN_BAR`, 20,499 px mismatch for `legwear`, and 38 setup-inverted triangles.`

Entry 1's line 4 was left as `pending`, and the rewrite in entry 2 has no line 4 of its own: what the
second build said is in the transcript only. The transcript, in turn, does not list the first grader run.

**The stop.** As handed in (`transcript.md`): physics-free comparison build failed `CHECK_SEAM_WITHIN_BAR`
on `(no art)/(no art)`, so closes, hands, whole body, arm bends, feet, timing, and soft-dance metrics were
not measured. The first half of that is true; the build it names is not the only one that failed.

**`tools.md`**, three entries, checked against the installed packages:

1. *`node_modules/@rig-c/parts/docs/MOTION.md` … is absent from the installed package.* True of
   `@rig-c/parts`, but the document ships — in `rig-c`, at `node_modules/rig-c/docs/MOTION.md`, which is
   the package whose README links it. The examinee looked in the wrong package. That the two packages'
   documents link each other without saying which package a path is in is worth a line on the tools.
2. *`rig-parts assemble --help` is not supported.* True: `FAIL USAGE: assemble does not take "--help"`.
3. *`@esotericsoftware/spine-core` … is not installed … this missing package limited the comparison
   build path.* The first half is true: it is a devDependency of both packages, so `npm ci` does not
   install it, and the tools say so. The second half is not: both builds ran rig-c's core check with all
   ten bars measured, and both failed on the legs' placement. The examinee read the two `package.json`
   files and installed nothing (rule 2 kept).

**Who sat it.** The same session as tasks 01–04. A context compaction happened during this task
(the session's replies to the commander were in Hebrew until then and in Korean after it); the model,
its settings and its permissions did not change.

**The dance, judged.** Scored blind by a person on 2026-10-21, as clip B of eight (A to H), without knowing whose it was: **0 out of 10**, one mark for the whole clip. `dance.mp4` is the clip the judge saw: `dance` three times round, 12 s at 24 fps, physics running throughout, one fixed viewport, a click on each beat. `dance_frames.jpg` and `dance_first_second.jpg` are the proctor's frames above, not the clip's. The score changes no line.
