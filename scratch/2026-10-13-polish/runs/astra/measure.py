import json,subprocess,math,statistics
from PIL import Image
from pathlib import Path
p=json.load(open('inputs/reference/pose.json'));g=json.load(open('run/before-render/dance@24fps/geometry.json'));r=json.load(open('inputs/rig/rig.json'))
# Read full RGB reference into memory, all artifacts stay here.
x=subprocess.run(['ffmpeg','-v','error','-i','inputs/reference/ref1080.mp4','-frames:v','313','-vf','scale=270:480','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True,check=True).stdout
assert len(x)>=313*270*480*3
# Use reference scaled to 270x480 for pixel thresholding, connected skirt sample bounded by tracked hips/knees.
rows=[]
for n in range(313):
 im=Image.frombytes('RGB',(270,480),x[n*270*480*3:(n+1)*270*480*3]);pix=im.load();j=p['frames'][n]['people'][0]['joints'];hx=sum(j[k]['at'][0] for k in ['r_hip','l_hip'])/8;hy=sum(j[k]['at'][1] for k in ['r_hip','l_hip'])/8
 pts=[]
 for yy in range(max(0,int(hy)-40),min(480,int(hy)+49)):
  for xx in range(max(0,int(hx)-65),min(270,int(hx)+66)):
   q=pix[xx,yy]
   if max(q)<68:pts.append((xx,yy))
 if len(pts)<100:raise ValueError((n,len(pts)))
 xs=sorted(q[0] for q in pts);ys=sorted(q[1] for q in pts);lo=xs[int(len(xs)*.02)];hi=xs[int(len(xs)*.98)];cx=sum(xs)/len(xs)
 # Lowest dark silhouette on each side, excluding isolated antialias pixels.
 left=[yy for xx,yy in pts if xx<hx-8];right=[yy for xx,yy in pts if xx>hx+8]
 q95=lambda a: sorted(a)[int(.95*(len(a)-1))]
 rows.append({'frame':n,'time':n/24,'hip':[hx,hy],'left':lo,'right':hi,'center':cx,'width':hi-lo,'leftBottom':q95(left),'rightBottom':q95(right),'pixels':len(pts)})
 if n in [0,96,120,138,168,192,216,240]:
  from PIL import ImageDraw
  d=ImageDraw.Draw(im);d.rectangle((lo,hy-40,hi,hy+49),outline='red');d.line((cx,hy-40,cx,hy+49),fill='cyan',width=1);im.resize((540,960)).save(f'run/evidence/skirt-mask-f{n:03}.png')
feet=[]
for f in g['frames']:
 feet.append({'frame':f['index'],'soles':{a['slot']:min(a['vertices'][1::2]) for a in f['attachments'] if a['slot'] in ['shoe_r','shoe_l']}})
a=r['skins']['default']['shins']['shins'];im=Image.open('inputs/rig/images/shins.png').convert('RGBA');alpha=im.getchannel('A');bridges=[]
for i in range(len(a['triangles'])//3):
 ids=a['triangles'][i*3:i*3+3];bones={w['bone'] for k in ids for w in a['weights'][k]}
 if len(bones)>1:
  from PIL import ImageDraw
  mask=Image.new('L',im.size);d=ImageDraw.Draw(mask);d.polygon([(a['uvs'][2*k]*im.width,a['uvs'][2*k+1]*im.height) for k in ids],fill=255)
  vals=[aa for aa,bb in zip(alpha.getdata(),mask.getdata()) if bb]
  bridges.append({'triangle':i,'bones':sorted(bones),'maxAlpha':max(vals),'pixelsWithAlpha':sum(v>0 for v in vals)})
result={'skirt':rows,'feet':feet,'crossLegTriangles':bridges};Path('run/measurements-before.json').write_text(json.dumps(result,indent=2))
print('Cross leg triangles',bridges);print('Sole ranges',{s:[min(f['soles'][s] for f in feet),max(f['soles'][s] for f in feet)] for s in ['shoe_r','shoe_l']});print('Skirt sampled',rows[0],rows[138],rows[192])
