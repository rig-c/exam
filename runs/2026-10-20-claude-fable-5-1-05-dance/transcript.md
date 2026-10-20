started: 2026-10-20T14:03:23Z

$ cp ../2026-10-20-claude-fable-5-1-04-soft/config.json config.json; cp ../2026-10-20-claude-fable-5-1-04-soft/hop.json hop.json
$ python3 (sleeve_l points -> [[507,250],[553,416],[611,550]]; sleeve_r -> [[357,254],[330,424],[279,561]]; + bone feet under root at [416,1070]; regions.legwear removed; meshes.legwear grid 36 r 10 segments [hip across y 600], [feet across y 1070])
$ rig-parts propose --parts ../2026-10-20-claude-fable-5-1-01-build/work/rig --source inputs/painting.png --out work --from-config config.json
0 LINT line(s) over 9 mesh(es) and the hip
coverage: 42 bone(s) — 31 checked and clean, 0 checked with a LINT line, 11 not checked
exit 0

$ python3 (write dance.json = hop.json + animation dance: 4.0 s, eased curve keys — hip translatey 0/-12 every 0.5 s; hip translatex 0/+14/0/-14 over 2 s; chest rotate 0/-4/0/+4; head rotate 0/5/0/-5; sleeve_l0 0/30, sleeve_l1 0/45 every 1 s; sleeve_r0 0/-30, sleeve_r1 0/-45; motion.animations_from = dance.json); rm hop.json
$ rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out
[rig]   mesh legwear      v= 134 t= 192 hull= 74 grid=36 bones=2 infl max 2 mean 1.62 cover 1.00000 loop passes 1
[rig]   animations beside the idle, from /Users/firejune/Workspace/Firejune/exam-runs/claude-fable-5-1-basic/exam-claude-fable-5-1/runs/2026-10-20-claude-fable-5-1-05-dance/dance.json as written: hop, dance
[check]   loop physics: 1 physics constraint(s) left out of the loop's frames, reported, not judged — "bust_phys" on bone "chest_jiggle" (rig.json)
[check]   beside the idle: 2 animation(s), hop, dance — built and gated by rigc with the rig; ANIMATIONS_DO_NOT_FOLD reads each for folds, every other bar here reads the idle
[check]   TEXTURE_STRETCH: PASS — meshes 9; triangles 884; frames 41; severity 1.098; severity_ceiling 1.926544; worst slot topwear, triangle 128, vertices 53 | 97 | 54, edge 97 | 54, frame 11, ratio 1.098; max_ratio 1.098; min_ratio 0.92
[check]   ANIMATIONS_DO_NOT_FOLD: PASS — 3 animation(s) read by rigc render --folds at 12 fps, its 1 physics constraint(s) left out (idle, hop, dance): 0 folding mesh(es), 0 not declared in may_fold (<= 0)
build: PASS — the packed atlas is the artifact; parts/ and rig/ are the intermediates it was made from
  out/check/build/skeleton.json
  out/check/build/skeleton.atlas
  out/check/build/skeleton.png
exit 0 (real 1m25s)

$ python3 grade.py runs/2026-10-20-claude-fable-5-1-05-dance
PASS  built: "rig-parts build exit 0"
PASS  checked: {"BREATH_VISIBLE": "PASS", "BLINK_NO_HOLE": "PASS", "CHAIN_LAG": "PASS", "TIP_OVER_ROOT": "PASS", "STILL_REGIONS_DARK": "PASS", "TEXTURE_STRETCH": "PASS", "ANIMATIONS_DO_NOT_FOLD": "PASS", "RECOMPOSITE_HOLES": "REPORTED"}
PASS  whole: "uncovered_error_px 2059 against <= 4200"
PASS  does_not_fold: []
PASS  budget: "884 triangles against <= 1000"
PASS  dance_as_timed: "`dance` lasts 4 s against 4.0"
PASS  closes: "the last frame is 0.0 rig px from the first at its furthest vertex, against <= 0.5 (keys only, physics out)"
PASS  both_hands: "`handwear_l` travels 404.6 rig px and `handwear_r` 401.0 at their furthest vertex, measured from the middle of `topwear`, each against >= 100.0"
PASS  whole_body: "the vertex of `topwear` that travels least travels 24.5 rig px, measured from the middle of `shoes`, against >= 15.0"
PASS  arms_bend_at_the_joints: "along its own length an upper arm or a forearm bends at most 4.3 degrees more than at rest, against <= 8.0"
PASS  on_her_feet: "the end of a leg (`legwear`) gets 0.18 rig px from where it meets `shoes`, against <= 6.0"
PASS  keeps_time: "1.0 of the variation in how fast she moves repeats every two beats, against >= 0.5"
PASS  soft_in_the_dance: "`topwear` differs from the same build without its physics by 3.486 rig px at dance frame 22, against 3.0 to 15.0"
PASS  dance_does_not_fold: []
14 of 14 line(s); journal present, 0 entry(ies) whose line 4 begins WTF?:
finished: 2026-10-20T14:12:59Z
