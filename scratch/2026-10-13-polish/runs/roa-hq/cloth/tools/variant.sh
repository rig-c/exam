#!/bin/bash
# usage: variant.sh <name> <python expr editing dict c, from cfg/v2.json>
set -e
P=<scratch>/dancer-2026-10-13/polish1_cloth; cd $P
N=$1; shift
python3 -c "
import json; c=json.load(open('cfg/${BASE:-v2}.json'))
$1
json.dump(c,open('cfg/$N.json','w'),indent=1)"
python3 tools/make_rig.py cfg/$N.json sw/$N/rig --copy-images > /dev/null
cd sw/$N && ../../../skirt/tools/pkg/node_modules/.bin/rigc build --rig rig/rig.json --motion rig/motion.json --out build > build.out 2>&1 || { echo "$N BUILD FAILED"; grep -v "^  \.\.\|PROF\|SKIP\|PASS" build.out | head -5; exit 1; }
grep -q "0 failed" build.out || { echo "$N GATE RED"; grep FAIL build.out | head; }
$P/tools/eval.sh $P/sw/$N | head -1
grep 'mesh "bottomwear"' render.out | cut -c1-200 || true
