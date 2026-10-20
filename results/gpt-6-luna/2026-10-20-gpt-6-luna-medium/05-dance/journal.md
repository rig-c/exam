# Journal — gpt-6-luna-medium, 05-dance, 2026-10-20

## Entry 1

1. **Read:** `tasks/05-dance/TASK.md`; `node_modules/rig-c/docs/RIGGING.md` §9.1–9.2; `rig-c/core` `gallery/walk/README.md` sections “The leg is two plates” and “The foot targets hang off ground”; task 04 config.
2. **Expect:** adding two two-bone leg chains, root-anchored foot targets and IK constraints will keep the feet connected to shoes while the hip and arms move; a 1-second repeated phrase will meet the eight-beat 4-second loop and triangle limit.
3. **Chose / turned down:** convert only `legwear` to a mesh weighted to the new thigh/shin bones; keep `shoes` on root, targets under `ground` under root, and preserve the chest physics and supplied hop.
4. **Happened:** pending.

## Entry 2

1. **Read:** `.grade/2026-10-20-gpt-6-luna-medium-05-dance/grade.log`, including the failed `CHECK_SEAM_WITHIN_BAR` detail.
2. **Expect:** the leg mesh is displaced in setup because the proposed chain origins were specified as parent-local coordinates but were entered as rig-space coordinates; correcting each joint to parent-local positions should restore the original leg silhouette and remove inverted setup triangles.
3. **Chose / turned down:** preserve the supplied art, shoe positions, and dance; adjust only the new leg bones and IK target placement to keep the hip-to-foot chains aligned with the painted legs.
4. **Happened:** WTF?: initial grader run was combined with the config write without a separate pre-run journal entry; grader reported `CHECK_SEAM_WITHIN_BAR`, 20,499 px mismatch for `legwear`, and 38 setup-inverted triangles.
