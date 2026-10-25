# Journal

## Entry 1 (opened 2026-10-25T08:47:03Z)

1. **Read:** AUTHORING cloth recipe and --write-config splice; task01 assembled parts
2. **Expect:** cloth proposer replaces back hair keyed chains with physics constraints on at least two bones; exit 0
3. **Chose / turned down:** Use documented back hair recipe with derived chains; retain all other parts and add named nod animation in animations.json
4. **Happened** (2026-10-25T08:47:08Z): WTF?: PROPOSE_WRITE_CONFIG_FRESH refuses writing over the --cloth config; use new output file then replace source config.

## Entry 2 (opened 2026-10-25T08:47:10Z)

1. **Read:** PROPOSE_WRITE_CONFIG_FRESH: existing output refused; AUTHORING cloth writes new file
2. **Expect:** new config-cloth.json receives physics constraints; exit 0
3. **Chose / turned down:** Write to fresh config-cloth.json and inspect result before copying it to submitted config.json
4. **Happened** (2026-10-25T08:47:16Z): WTF?: PROPOSE_WRITE_CONFIG_CONFLICT says my corrected hairback_l amps are a hand edit the cloth recipe would drop; remove that track before proposing.

## Entry 3 (opened 2026-10-25T08:47:21Z)

1. **Read:** PROPOSE_WRITE_CONFIG_CONFLICT directs removal of hand-edited hairback_l track
2. **Expect:** cloth proposal writes fresh config with physics constraints and no hairback keys; exit 0
3. **Chose / turned down:** Removed hairback_l idle track since cloth recipe owns those bones; retain rest of config
4. **Happened** (2026-10-25T08:47:33Z): exit 0; back hair drafts 6 constraint(s), physics on every link, no idle key; wrote config-cloth.json

## Entry 4 (opened 2026-10-25T08:47:38Z)

1. **Read:** Task 02 gesture/physics bars; cloth proposal six constraints and AUTHORING animations_from
2. **Expect:** build exits 0, check PASS, no fold across nod
3. **Chose / turned down:** Build copied cloth config with 2-second nod (head 8°, chest 3°, chest -6 y); defer render until gate results
4. **Happened** (2026-10-25T08:48:29Z): check: PASS; 11 of 11 bar(s) measured, 0 skipped; physicsConstraints=6, animations=2

## Entry 5 (opened 2026-10-25T08:48:31Z)

1. **Read:** Task 02 bars; build PASS physicsConstraints 6 and named nod
2. **Expect:** grader returns all seven lines PASS if nod remains within seam tolerance
3. **Chose / turned down:** Use official grader to measure face travel and seam/folds, then revise only if needed
4. **Happened** (2026-10-25T08:49:12Z): 8 of 8 line(s); nod face travels 32.5 rig px; holds_together opens {} not_read []

## At the end (2026-10-25T08:49:15Z)

- **Where I guessed:** Authored gesture head 8 degrees, chest 3 degrees, translatey -6 rig px; measured by grader 32.5 rig px and no seam opening. Cloth values wind 1..8 and gravity 4..24 came from AUTHORING fixture, not tuned for this art.
- **What I could not find:** The fresh-output and hand-edit ownership constraints were only clear from PROPOSE_WRITE_CONFIG_FRESH and PROPOSE_WRITE_CONFIG_CONFLICT refusals at runtime
