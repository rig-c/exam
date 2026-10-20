# Findings — gpt-6.1-sol, R3

The baseline map used pelvis rotation, reach:true on chest, eye-line head roll, all four free-bend limbs and both face dials. No planting/scaling was enabled. It passed 7/14 rows.

Planting plus leg scaling solved support/floor/slide and restored hip range and rebound. A 0.02 stance left a 0.0224 two-foot error; 0.03 closed it while retaining all 35 lifted-foot frames. Both --reduce 2 and --reduce 1 disturbed support contact. The final candidate keeps dense keys, changes trunk reach to direct direction aiming, and changes head roll from eyes to ears. Face yaw/pitch remain mapped. The provided rig and physics values were not edited. The sequence was never altered or cleaned again.

Final numeric result: 14/14 PASS, no SKIP. Camera sidecar: rig-pose-camera/1, 313 entries, time difference 0. The three detected flights remain 88–91, 179–181, 267–269. Physics remains enabled, with no folds or pass-through in all 313 rendered frames.

The final map has different head reference pairs than the baseline: its trunk+head jitter denominator is 1.597 rather than 1.660 deg/frame². This is a declared semantic change, not a claim that the original eye-line motion was preserved. Ear scores never fall below 0.836; their roll differs from eye roll by median 1.303° and max 4.105°. Direct trunk aiming gives up the shoulder endpoint correction. Render evidence supports broad gesture correspondence; no detector comparison was run, and the unavailable original film was not assessed.

## Procedural disclosure

The journal has a protocol defect: entry 4 began while entry 3 was still running. Entry 3's result was appended at its actual completion, under the already-open entry 4, leaving two line-4 records there. All pre-action lines were written before their respective actions, but the required serial entry/result protocol was not followed. The original order is preserved. Do not treat the numerical grader PASS as proof of a valid exam sitting; under the prompt's strict journal rule this defect disqualifies the sitting.

The host required reading agent-bridge SKILL.md before using that skill. This one skill read was outside the exam directory, and is disclosed in transcript.md. No other sitting, answer, branch, PR, or external model was consulted. No subagent, browser, Git command, commit or push was used. Final bridge submission is the proctor-requested exception to no messaging.

No usage.json: the tools expose no actual per-session fresh/cached/output token counts. No estimate was made.
