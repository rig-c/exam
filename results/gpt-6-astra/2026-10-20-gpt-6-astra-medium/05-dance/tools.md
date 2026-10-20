# Tool feedback

## Name the driving bones in fold diagnostics
- **I was trying to:** stop the new leg mesh folding in a planted dance without reducing the whole-body motion.
- **The tool gave me:** rig-parts check, ANIMATIONS_DO_NOT_FOLD: `"dance": mesh "legwear" (slot "legwear") folds on 40 frame(s) [1-5, 7-11, 13-17, 19-23, 25-29, 31-35, 37-41, 43-47] at 12 fps; worst frame 2 (t=0.1667s): 3 of 172 triangle(s) [63, 78, 79] in world box x [-30.80, 17.87] y [419.95, 517.43]`. This precisely locates the failure, but does not name the bones moving those vertices.
- **What would have helped:** include each failing triangle vertex's two largest bone weights, like the documented TEXTURE_STRETCH diagnostic, and name the IK constraints on those chains. I extracted weights from out/rig/rig.json myself and saw opposite leg chains pulling the inner leg lattice together.
- **Cost:** roughly a few minutes including the corrective full build. Resolved by moving the screen-right knee outward and changing that leg IK bend direction; final dance has no folds.
