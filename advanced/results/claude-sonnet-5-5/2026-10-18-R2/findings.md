# Findings
- Foot is not mappable as a 3rd leg bone (body-18 has no toe): chain needs bones+1 joints. Leg chains = thigh+shin only; foot inherits.
- translate.scale drives hip travel: trunk pair (1.78) over-travels hip (vertical 1.46x, horizontal 1.71x). Shoulder pair (1.08) fits both bars.
- `reach` uses that same scale: with 1.08 it gave trunk jitter 3.6x and hair_front folds (155 frames). Plain aim `neck` gives 1.000x and 0 folds.
- Lifted-foot ratio is set by the --leg-scale minimum: 0.8 -> 1.29, 0.6 -> 1.175, 0.5 and 0.4 pass.
- Dropping --stance, or max 1.3, breaks airborne/hip-vertical.
