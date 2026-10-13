import json,copy
from collections import Counter,defaultdict
from pathlib import Path
p=Path('run/after/rig.json');r=json.loads(p.read_text());orig=r['skins']['default']['shins']['shins'];tris=[orig['triangles'][i:i+3] for i in range(0,len(orig['triangles']),3)]
for suffix,bone in [('r','leg_r1'),('l','leg_l1')]:
 selected=[t for t in tris if all(orig['weights'][v][0]['bone']==bone for v in t)];used={v for t in selected for v in t};edges=Counter(tuple(sorted((t[i],t[(i+1)%3]))) for t in selected for i in range(3));adj=defaultdict(list)
 for (u,v),n in edges.items():
  if n==1:adj[u].append(v);adj[v].append(u)
 assert all(len(v)==2 for v in adj.values())
 boundary=[min(adj)];prev=None;cur=boundary[0]
 while True:
  nxt=next(v for v in sorted(adj[cur]) if v!=prev)
  if nxt==boundary[0]:break
  boundary.append(nxt);prev,cur=cur,nxt
 assert len(boundary)==len(adj)
 order=boundary+sorted(used-set(boundary));remap={v:i for i,v in enumerate(order)};a=copy.deepcopy(orig);a['uvs']=[x for v in order for x in orig['uvs'][2*v:2*v+2]];a['weights']=[orig['weights'][v] for v in order];a['triangles']=[remap[v] for t in selected for v in t];a['hull']=len(boundary)
 slot='shins' if suffix=='r' else 'shins_l';name='shins' if suffix=='r' else 'shins_l';r['skins']['default'][slot]={name:a}
 if suffix=='l':
  i=next(i for i,x in enumerate(r['slots']) if x['name']=='shins');r['slots'].insert(i+1,{'name':slot,'bone':bone,'attachment':name})
 print(slot,len(order),'vertices',len(boundary),'boundary',len(selected),'triangles')
r['invariants']['meshSlots']=13;p.write_text(json.dumps(r,indent=2)+'\n')
