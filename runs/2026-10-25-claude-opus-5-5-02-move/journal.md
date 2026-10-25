# Journal

## Entry 1 (opened 2026-10-25T11:34:59Z)

1. **Read:** AUTHORING §3 'Recipe: expressions and other named animations' (motion.animations_from, spec rigc-motion/1, keys on head/chest not *_ctl) and its 'Strands that trail' (one physics constraint per link, rotate 1, inertia 0.8, strength root*(1-0.35 i/(n-1)), damping 0.85); TASK 02's reference gesture: head 8°, chest 3°, chest lowered 6 rig px = 35.0 px
2. **Expect:** exit 0; '[rig] animations beside the idle, from …/animations.json as written: lean'; gate rig-play green with physicsConstraints=14; ANIMATIONS_DO_NOT_FOLD reads idle and lean, 0 folding; CLOTH_SETTLES now measured (maybe a warning); check PASS
3. **Chose / turned down:** config.json = task 01's plus animations_from and 14 physics constraints on hairback_r/l (3 links) and lock/lock1_ (4 links, the side locks that hang free); animations.json 'lean' 2.0 s: head rotate 8, chest rotate 3, chest translatey -6, eased in 0.6 s, held, out by 2.0 s. Turned down keying a sleeve: the TASK warns a limb swung past the painting shows the background
4. **Happened** (2026-10-25T11:36:08Z): as expected: exit 0, 'physicsConstraints=14', '1 animation(s), lean — built and gated by rigc with the rig', ANIMATIONS_DO_NOT_FOLD '(idle, lean): 0 folding mesh(es)', 'check: PASS; 11 of 11 bar(s) measured'. SEAM_OVER_MOTION SKIPs ('no neighbour pair is declared'), so the Holds-together line is not read by the build: I must read it with rigc render --seam myself

## Entry 2 (opened 2026-10-25T11:36:15Z)

1. **Read:** TASK 02 Holds together: 'topwear with each upper arm … Read with rigc render --seam, a frame opening when its gap or its ghost holds more cells than its box is long'; rigc render --help: '--seam <slot>:<slot>' writes seam.json per frame, '--geometry' writes skinned vertices
2. **Expect:** exit 0; one seam line per pair, topwear:handwear_l and topwear:handwear_r: zero or a few cells of gap during the chest lean (sleeves ride chest, topwear rides chest and hip, so a 3° lean may stretch a little); geometry.json for the lean frames from which I compute face travel ~35 px
3. **Chose / turned down:** render only the lean animation at 12 fps with --seam for both arm pairs and --geometry in one call; turned down rendering idle too (the line reads the gesture only)
4. **Happened** (2026-10-25T11:36:30Z): partly as expected: exit 0, '2 of 2 pair(s) open' by rigc's own count, but each is tiny against the TASK's floor: topwear|handwear_l 'max 3 px — no gap' in a box '(10.00 × 4.00)', topwear|handwear_r 'ghost … 8 px' in a box '(19.00 × 119.00)' and a 1 px gap — under 'more cells than its box is long' on both

## Entry 3 (opened 2026-10-25T11:36:44Z)

1. **Read:** TASK 02 Gestures line: 'face's furthest vertex travels at least 22 rig px measured from the middle of bottomwear'; reference: head 8°, chest 3°, lowered 6 = 35.0 (with idle travel 9.1)
2. **Expect:** max about 25-35 rig px (my lean is the reference's keys without the idle under it, measured from frame 0), at a held frame 8-16
3. **Chose / turned down:** my own script (scratchpad facetravel.py) over the render's geometry.json: per frame, every face vertex relative to bottomwear's box centre, distance from frame 0, max; turned down measuring against the setup pose since frame 0 of lean is the setup plus physics
4. **Happened** (2026-10-25T11:36:51Z): as expected: 'max 32.54 rig px at frame 8 of 25', above the 22 bar with margin

## Entry 4 (opened 2026-10-25T11:36:51Z)

1. **Read:** PROMPT: python3 grade.py runs/<run>; TASK 02 pass lines (task 01's four plus Trails, Gestures, Holds together, Gesture without folding)
2. **Expect:** exit 0; 8 of 8 lines PASS: trails (14 physics constraints), gestures about 32 px on lean, holds together (no pair over its floor), no fold; journal intact 3 entries+1, 0 WTF
3. **Chose / turned down:** grade now; turned down widening the lean, since 32.5 already clears 22 and a bigger chest turn widens the arm seams
4. **Happened** (2026-10-25T11:38:11Z): as expected: '8 of 8 line(s)', gestures '32.5 rig px … against >= 22', holds_together '0 frames open on every pair, every pair read'

## At the end (2026-10-25T11:38:11Z)

- **Where I guessed:** Gesture amounts (head 8°, chest 3°, translatey -6) copied from the TASK's reference gesture; timing (0.6 s in, hold to 1.4 s, out by 2.0 s) and the eased curve handles are mine. Physics values are the recipe's (inertia 0.8, strength 90 softened down the chain, damping 0.85); choosing lock/lock1_ as the strands that 'hang free' was read off the bone names and positions, not a picture.
- **What I could not find:** Whether TASK's 'middle of bottomwear' means the box centre or the vertex mean; I took the box centre and the grader's figure (32.5) matched mine.
