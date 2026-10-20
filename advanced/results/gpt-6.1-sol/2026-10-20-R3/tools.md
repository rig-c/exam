## Reduction that preserves planted contact
- **I was trying to:** lower local rotation jitter without making planted feet slide.
- **The tool gave me:** README “Few keys”: “Each ankle is held to the plant's tolerance plus the most the reduction may move it”. With --reduce 2 the gate stayed green, but measured slide was 0.03690 leg lengths/frame; with 1 it was 0.01651, against 0.005.
- **What would have helped:** `--reduce-contact` that constrains support-foot positions and their consecutive-frame displacement, or an explicit warning that a green reduced retarget does not certify foot planting.
- **Cost:** roughly several minutes for two retarget/build/render/grade cycles. Got there by abandoning reduction, not by finding a contact-preserving reduction option.

## Reach compensation needs a local-motion reading
- **I was trying to:** aim the chest toward the shoulder target while staying within the local rotation jitter bar.
- **The tool gave me:** README map: “Without it, a tilted pelvis carries the chest's origin sideways and the trunk, parallel to the pose's, misses the shoulders.” This encouraged reach:true. Baseline chest local jitter measured 3.874 versus sequence 1.908 deg/frame², and upper-arm compensation also increased jitter.
- **What would have helped:** A POSTURE reading that separately reports the local jitter added by reach compensation and the shoulder endpoint error traded away when reach is disabled.
- **Cost:** roughly a few minutes including the read-only per-bone calculation and the last retarget cycle. Disabled reach; direct segment directions pass, but shoulder endpoint matching is no longer enforced.

## Optional eye-line nod coupling
- **I was trying to:** map head roll and face yaw/pitch faithfully without adding excessive local rotation curvature.
- **The tool gave me:** README “What it does”: the clamped nod is coupled into “the head bone's rotate track (`+1.6°/unit` ...)”. This is documented, but the CLI exposed no separate switch to disable this additional channel while keeping eye-line roll.
- **What would have helped:** `--head-nod off` or separate nod-to-rotate and nod-to-pitch gains, with the added local jitter printed.
- **Cost:** roughly a couple of minutes diagnosing the head contribution and checking ear confidence/angles. Used the observed ear line for head roll instead; the face dials remain mapped, but automatic eye-line translation/nod is omitted.
