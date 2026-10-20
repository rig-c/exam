# Journal — gpt-6-luna-medium, 02-move, 2026-10-20

## Entry 1

1. **Read:** `node_modules/@rig-c/parts/docs/AUTHORING.md` §4, “Recipe: expressions and other named animations” and “Strands that trail”; `node_modules/rig-c/docs/RIGGING.md` §6.
2. **Expect:** a 1.6-second wave clip and physics constraints on two long hair chains will build into the supplied rig and satisfy the wave and trailing bars.
3. **Chose / turned down:** animate the right-in-image sleeve chain `sleeve_l` (the guide's measured positive direction raises that arm), and add physics to both free hanging front locks `lock` and `lock1_`; use the recipe's per-link softened constraints.
4. **Happened:** config and `wave.json` were written as described; no stdout.


## Entry 2

1. **Read:** `tasks/02-move/TASK.md` pass lines; `node_modules/@rig-c/parts/docs/AUTHORING.md` §4 and the config and motion files.
2. **Expect:** grader will report task 01's 4 bars, at least two physics bones, a ≥1 s animation with ≥150 px rise relative to median, and no folded mesh in the wave.
3. **Chose / turned down:** run the official grader on the authored config; use its measurements to decide whether the wave amplitude needs adjustment.
4. **Happened:** grader passed all 7 lines; wave rise was 280.9 px over 1.6 s and 8 hair bones received physics constraints.
