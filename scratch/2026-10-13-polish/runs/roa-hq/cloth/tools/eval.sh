#!/bin/bash
# usage: eval.sh <variant dir>   (holds rig/ and build/) -> render/, raw.json, numbers line, xing.json
set -e
V=$1; P=<scratch>/dancer-2026-10-13/polish1_cloth
R=<scratch>/dancer-2026-10-13/skirt/tools/pkg/node_modules/.bin/rigc
T=<scratch>/dancer-2026-10-13/skirt/tools
cd $V
$R render --candidate build --animation dance --fps 24 --max ${MAX:-800} --geometry --folds --out render > render.out 2>&1
G=render/dance@24fps/geometry.json
python3 $T/rig_measure.py $G raw.json > /dev/null
(cd $T && python3 report.py $V/raw.json 0.1505) > numbers.out
python3 $P/tools/xing.py $G rig/images xing.json > xing.out
python3 - <<PY
import json
n=json.loads(open('numbers.out').read().splitlines()[0]); v=json.loads(open('numbers.out').read().splitlines()[1])
x=json.load(open('xing.json'))['summary']
fo=json.load(open('render/dance@24fps/folds.json'))
bw=[m for m in fo.get('meshes',fo if isinstance(fo,list) else []) if (m.get('slot') if isinstance(m,dict) else None)=='bottomwear'] if isinstance(fo,dict) else []
print('$V'.split('/')[-1], 'A lag %.2f sw %.2f ov %.3f | B lag %.2f sw %.2f ov %.3f | %d/6'%(n['A']['lag'],n['A']['swingRatio'],n['A']['overshoot'],n['B']['lag'],n['B']['swingRatio'],n['B']['overshoot'],sum(a=='PASS' for a in v.values())),
 '| xing %d deep %d max %.0f (A %d, B %d)'%(x['crossing'],x['deep'],x['maxDepth'],x['byWindow']['A']['crossing'],x['byWindow']['B']['crossing']))
PY
grep "folds " render.out | cut -c1-220 || true
