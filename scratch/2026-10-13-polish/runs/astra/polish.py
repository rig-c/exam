import json,math,sys,copy
from pathlib import Path
out=Path('run/after');out.mkdir(exist_ok=True)
load=lambda p:json.loads(Path(p).read_text())
save=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
mode=sys.argv[1]
if mode=='init':
 for a,b in [('inputs/rig/rig.json','rig.json'),('inputs/dance/motion.json','motion.json'),('inputs/dance/map.json','map.json')]:save(out/b,load(a))
 print('Input rig/motion/map copied; original inputs untouched');sys.exit()
r=load(out/'rig.json');m=load(out/'motion.json');a=m['animations']['dance'];g=load('run/before-render/dance@24fps/geometry.json');measure=load('run/measurements-before.json');bones={b['name']:b for b in r['bones']}
track=lambda name,prop: next(t for t in a['tracks'] if t.get('bone')==name and t['property']==prop)
angle=lambda b:math.degrees(math.atan2(b['c'],b['a']))
wrap=lambda x:(x+180)%360-180
inv=lambda b,x,y:((b['d']*x-b['b']*y)/(b['a']*b['d']-b['b']*b['c']),(-b['c']*x+b['a']*y)/(b['a']*b['d']-b['b']*b['c']))
if mode=='arms':
 k=load('inputs/dance/map.json')['alternates'][0]
 changes={'upperarm_r_under':'K0_upperarm_r','forearm_r_back':'K0_forearm_r','upperarm_r':None,'forearm_r':None,'forearm_r_under':None,'upperarm_r_back':None}
 # Evaluate the existing attachment state, override frames 19..60, then compress equal runs.
 for slot,value in changes.items():
  t=next(t for t in a['tracks'] if t.get('slot')==slot and t['property']=='attachment');old=t['keys'];state=next(s['attachment'] for s in r['slots'] if s['name']==slot);new=[]
  for n in range(313):
   matches=[q for q in old if q['t']<=n/24+1e-7];v=matches[-1]['v'] if matches else state
   if 19<=n<=60:v=value
   if not new or new[-1]['v']!=v:new.append({'t':0 if n==0 else (n-.5)/24,'v':v})
  t['keys']=new
 for n in range(19,61):
  fb={b['name']:b for b in g['frames'][n]['bones']};parent=angle(fb[bones['sleeve_r0']['parent']]);targets={}
  for name in ['sleeve_r0','sleeve_r1']:
   drawn=k['drawn'][name];target=drawn+max(-5,min(5,wrap(angle(fb[name])-drawn)));targets[name]=target
   tr=track(name,'rotate');tr['keys'][n]['v']=[round(wrap(target-parent-bones[name].get('rotation',0)),6)];parent=target
 save(out/'arm-repair.json',{'frames':[19,60],'slots':changes,'drawn':k['drawn'],'turn':[-5,5],'method':'manual motion override; map.json retained as original retarget provenance, not a regeneration recipe'})
 print('42 frames: right K0 arm behind body, world art-turn clamped to +/-5 degrees; left arm and torso set unchanged')
elif mode=='legs':
 mesh=r['skins']['default']['shins']['shins'];bad={x['triangle'] for x in measure['crossLegTriangles'] if x['maxAlpha']==0};old=mesh['triangles'];mesh['triangles']=[v for i in range(len(old)//3) if i not in bad for v in old[3*i:3*i+3]]
 p=load('inputs/reference/pose.json');factor=load('inputs/dance/report.json')['scale']['factor'];ankles=[sum(f['people'][0]['joints'][k]['at'][1] for k in ['r_ankle','l_ankle'])/2 for f in p['frames']]
 floor=min(measure['feet'][0]['soles'].values());keys=[];rows=[];windows=[(85,94),(175,184),(265,275)]
 for n in range(313):
  lift=0
  for l,u in windows:
   if l<n<u:
    level=ankles[l]+(ankles[u]-ankles[l])*(n-l)/(u-l);lift=max(0,(level-ankles[n])*factor)
  dy=floor+lift-min(measure['feet'][n]['soles'].values());keys.append({'t':n/24,'v':[round(dy,6)]});rows.append({'frame':n,'rootY':dy,'targetMinSole':floor+lift,'jumpLift':lift})
 a['tracks'].append({'bone':'root','property':'translatey','keys':keys});save(out/'contact-targets.json',{'floor':floor,'airborneWindows':windows,'frames':rows,'limitation':'minimum sole only; no full 2-foot IK or horizontal locking'})
 print('Removed only fully transparent cross-leg triangles',sorted(bad));print('Minimum-sole floor',floor,'jump peaks',[max(row['jumpLift'] for row in rows[l:u+1]) for l,u in windows])
elif mode=='clothes':
 rows=measure['skirt'];rest=next(x for x in g['rest'] if x['slot']=='bottomwear');setup={b['name']:b for b in g['setup']['bones']};h=setup['hip'];local=[inv(h,rest['vertices'][i]-h['worldX'],rest['vertices'][i+1]-h['worldY']) for i in range(0,len(rest['vertices']),2)];xmin=min(v[0] for v in local);xmax=max(v[0] for v in local);ymin=min(v[1] for v in local);ymax=max(v[1] for v in local);width=xmax-xmin;cx=(xmin+xmax)/2
 base=rows[:19];avg=lambda xs:sum(xs)/len(xs);bw=avg([x['width'] for x in base]);bc=avg([(x['left']+x['right'])/2-x['hip'][0] for x in base]);bt=avg([x['leftBottom']-x['rightBottom'] for x in base]);mesh=r['skins']['default']['bottomwear']['bottomwear'];keys=[];controls=[]
 for n in range(313):
  window=rows[max(0,n-2):min(313,n+3)];fade=max(0,min(1,(n-86)/10,(269-n)/8))
  ratio=max(.85,min(1.5,avg([q['width'] for q in window])/bw));dx=(avg([(q['left']+q['right'])/2-q['hip'][0] for q in window])-bc)*width/bw;dx=max(-width*.3,min(width*.3,dx));tilt=(avg([q['leftBottom']-q['rightBottom'] for q in window])-bt)*width/bw
  fb={b['name']:b for b in g['frames'][n]['bones']};hip=fb['hip'];vals=[]
  for (xx,yy),influences in zip(local,mesh['weights']):
   f=max(0,min(1,(ymax-yy)/(ymax-ymin)))**2
   lx=(dx+(xx-cx)*(ratio-1))*f*fade;ly=tilt*(xx-cx)/width*f*fade
   wx=hip['a']*lx+hip['b']*ly;wy=hip['c']*lx+hip['d']*ly
   for w in influences:
    u,v=inv(fb[w['bone']],wx,wy);vals.extend([round(u,6),round(v,6)])
  keys.append({'t':n/24,'offset':0,'vertices':vals});controls.append({'frame':n,'fade':fade,'hemDx':dx*fade,'widthRatio':1+(ratio-1)*fade,'tilt':tilt*fade})
 a.setdefault('deform',[]).append({'slot':'bottomwear','attachment':'bottomwear','keys':keys});save(out/'skirt-controls.json',{'referenceBaselineWidth':bw,'rigRestWidth':width,'controls':controls,'heuristics':{'blackThreshold':68,'quantiles':[.02,.98],'smoothFrames':5,'fadeIn':[86,96],'fadeOut':[261,269],'widthRatioBounds':[.85,1.5],'maxShearFraction':.3,'falloff':'squared distance below waistband'}})
 print('313 deform keys; waistband pinned; measured width/shear/hem tilt, existing physics unchanged; max dx',max(abs(q['hemDx']) for q in controls),'width ratio',max(q['widthRatio'] for q in controls))
elif mode=='head':
 # Observed closures, interpolated edges explicitly editorial rather than detected landmarks.
 phases=[(16,18,19,22),(135,138,149,153),(172,174,175,179),(231,234,235,239),(256,258,259,263)]
 keys=[{'t':0,'v':[1]}]
 for start,closed,end,opened in phases:keys.extend([{'t':start/24,'v':[1],'ease':'shut'},{'t':closed/24,'v':[.12]},{'t':end/24,'v':[.12],'ease':'open'},{'t':opened/24,'v':[1]}])
 keys.append({'t':13,'v':[1]});a['tracks'].append({'group':'eyes','property':'scaley','keys':keys});save(out/'blink-timing.json',{'frames':phases,'source':'visual reference closures, edge interpolation editorial; min scale 0.12 from inputs/rig/motion.json idle'})
 print('5 observed closure intervals; eyes group scaley 1 -> 0.12 -> 1')
else:raise ValueError(mode)
save(out/'rig.json',r);save(out/'motion.json',m)
