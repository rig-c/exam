import json,math
from pathlib import Path
p=Path('run/after/motion.json');m=json.loads(p.read_text());g=json.loads(Path('run/before-render/dance@24fps/geometry.json').read_text());r=json.loads(Path('run/after/rig.json').read_text());b={x['name']:x for x in r['bones']};t={x['bone']:x for x in m['animations']['dance']['tracks'] if x.get('property')=='rotate' and 'bone'in x};wrap=lambda x:(x+180)%360-180
for n in range(19,61):
 f={x['name']:x for x in g['frames'][n]['bones']};c=f[b['sleeve_r0']['parent']];upper=math.degrees(math.atan2(c['c'],c['a']))+b['sleeve_r0']['rotation']+t['sleeve_r0']['keys'][n]['v'][0];old=upper+b['sleeve_r1']['rotation']+t['sleeve_r1']['keys'][n]['v'][0];mix=min(1,(n-18)/4,(61-n)/4);target=old+wrap(-45.93-old)*mix;t['sleeve_r1']['keys'][n]['v']=[round(wrap(target-upper-b['sleeve_r1']['rotation']),6)]
p.write_text(json.dumps(m,indent=2)+'\n');print('K0 right forearm: inward within existing [-5,+5] art limits; four-frame ramps')
