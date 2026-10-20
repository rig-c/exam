started: 2026-10-20T13:45:09Z
$ ln -s ../../tasks/03-correct/inputs inputs ; python3: config.json = key, seethrough (resolution 1024, steps 30, seed 42, offload true), assemble.rig_scale 0.5
$ rig-parts inputs --source inputs/painting.png --config config.json --out work/inputs   exit 0; st_input_full.png 2432x2432
$ rig-parts layers inputs/layers/full > work/layers_full.txt   exit 0; 0 WARN
$ rig-parts propose --head-box --full inputs/layers/full --canvas 1664x2432 > work/propose_head.log   exit 0; head_box [538, 158, 1100, 720]
$ rig-parts inputs ... (config.json: seethrough.head_box added)   exit 0; st_input_head.png 562x562
$ rig-parts assemble --propose-plan ... > work/plan.log   exit 0; 22 rows; (config: plan and extend_below_crop pasted)
$ rig-parts assemble --source ... --out work > work/assemble1.log   exit 0; uncovered error px 1726; 444 holes; largest 154 px
$ rig-parts propose --parts work/rig --source inputs/painting.png --out work > work/propose1.log   exit 0; 1 LINT line: hairback_r / hairback_l squeeze hair_back (0.064 times rest length)
$ rig-parts build ... --out out > work/build_draft.log   exit code not captured in the call (the log ends "build: stopped at check"); CHECK_TEXTURE_STRETCH: mesh "hair_back" triangle 167, ratio 0.065; "check: FAIL — 1 bar(s) not met"
  (config.json: bones, meshes, regions, motion copied from proposal.json as proposed; then hairback_l motion amps set to [0.6, 1.4, 2.4] (same sign as hairback_r))
$ rig-parts propose --parts work/rig --source inputs/painting.png --out work --from-config config.json > work/lint2.log   exit 0; 0 LINT line(s)
$ rig-parts build --config config.json --source inputs/painting.png --full inputs/layers/full --head inputs/layers/head --out out > work/build_fixed.log   exit 0; "check: PASS; 10 of 10 bar(s) measured, 0 skipped"; "build: PASS"; TEXTURE_STRETCH PASS (worst 0.888, hair_front)
finished: 2026-10-20T14:00:20Z
