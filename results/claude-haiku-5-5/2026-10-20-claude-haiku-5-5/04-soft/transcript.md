started: 2026-10-20T14:00:25Z
$ cp ../2026-10-20-claude-haiku-5-5-02-move/config.json config.json; animations.json = wave (from task 02) + hop (copied exactly from tasks/04-soft/hop.json)
$ rig-parts build ... --out out > work/build_base.log        exit 0; TEXTURE_STRETCH triangles 590
$ config: chest_jiggle bone under chest at (446,320); topwear grid 31 -> contour (spacing 31, region bust circle cx 446 cy 320 r 26 spacing 12 band 16); constraint bust_phys (x 0.5, y 1, inertia 0.25, strength 120, damping 0.92)
$ rig-parts build ... --out out > work/build_soft1.log       exit 0; triangles 708 (over the 700 budget)
$ config: contour spacing 36, region spacing 15
$ rig-parts build ... --out out > work/build_soft2.log       exit 0; check PASS; triangles 664
$ work/config_nophys.json (every constraint removed) + work/animations.json; rig-parts build --config work/config_nophys.json ... --out work/out_nophys > work/build_nophys.log
  first attempt exit 1 (CONFIG_FILE_PRESENT: animations_from relative to the config's folder); second attempt exit 0
$ rigc render --candidate out/check/build/skeleton.json --animation hop --fps 24 --geometry --folds --out work/hop_phys   exit 0; 0 of 8 mesh(es) fold
$ rigc render --candidate work/out_nophys/check/build/skeleton.json --animation hop --fps 24 --geometry --folds --out work/hop_nophys   exit 0; 0 of 8 mesh(es) fold
$ python3 work/measure_soft.py work/hop_phys/hop@24fps/geometry.json work/hop_nophys/hop@24fps/geometry.json
  furthest vertex difference 6.305 rig px; 20 of 116 topwear vertices differ by >0.5 px at some frame (17.2%)
$ python3 grade.py runs/2026-10-20-claude-haiku-5-5-04-soft   (9 of 9 lines, see grader log: soft 6.61 by the grader's own measure, budget 664)
finished: 2026-10-20T14:13:02Z
