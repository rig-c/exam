import json,math,statistics,subprocess
from pathlib import Path
from PIL import Image
load=lambda x:json.loads(Path(x).read_text());ref=load('run/measurements-before.json')['skirt'];results={};geos={}
for label,root in [('before','run/before-render'),('after','run/after/render')]:
 g=load(root+'/dance@24fps/geometry.json');geos[label]=g;v=g['viewport'];widths=[]
 for n,f in enumerate(g['frames']):
  a=next(a for a in f['attachments'] if a['slot']=='bottomwear');xs=a['vertices'][::2];ys=a['vertices'][1::2];x0=max(0,int((min(xs)-v['x'])*v['scale']));x1=min(v['pixelWidth'],math.ceil((max(xs)-v['x'])*v['scale'])+1);y0=max(0,int((v['y']+v['height']-max(ys))*v['scale']));y1=min(v['pixelHeight'],math.ceil((v['y']+v['height']-min(ys))*v['scale'])+1);im=Image.open(root+f'/dance@24fps/f{n:04}.png').convert('RGB');px=im.load();dark=sorted(x for y in range(y0,y1) for x in range(x0,x1) if max(px[x,y])<68);widths.append(dark[int(.98*(len(dark)-1))]-dark[int(.02*(len(dark)-1))])
 base=statistics.mean(widths[:19]);rb=statistics.mean(q['width'] for q in ref[:19]);err=[abs(widths[n]/base-ref[n]['width']/rb) for n in range(96,265)];results[label]={'baselineBlackWidth':base,'meanNormalizedWidthError':statistics.mean(err),'maxNormalizedWidthError':max(err),'widths':widths}
k=load('inputs/dance/map.json')['alternates'][0];turns={}
for name in ['sleeve_r0','sleeve_r1']:
 ds=[]
 for n in range(19,61):
  b=next(b for b in geos['after']['frames'][n]['bones'] if b['name']==name);ds.append((math.degrees(math.atan2(b['c'],b['a']))-k['drawn'][name]+180)%360-180)
 turns[name]=[min(ds),max(ds)]
 assert max(abs(x) for x in ds)<5.001
results['K0RightArtTurnDegrees']=turns
# Verify exact blink bone scale against the inherited head matrix, not just authored JSON.
eyes=[]
for n in [0,18,138,174,234,258,288]:
 bones={b['name']:b for b in geos['after']['frames'][n]['bones']};eye=bones['eye_r'];head=bones['head'];det=lambda b:b['a']*b['d']-b['b']*b['c'];eyes.append({'frame':n,'relativeAreaScale':det(eye)/det(head)})
results['eyes']=eyes
for label in ['before','after']:
 folds=load(('run/before-render' if label=='before' else 'run/after/render')+'/dance@24fps/folds.json');results[label]['foldReport']=folds
Path('run/after/verification.json').write_text(json.dumps(results,indent=2)+'\n');print({k: {a:b for a,b in v.items() if a not in ['widths','foldReport']} if k in ['before','after'] else v for k,v in results.items()})
