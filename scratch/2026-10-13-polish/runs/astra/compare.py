import json,math,subprocess
from pathlib import Path
from PIL import Image,ImageDraw
load=lambda x:json.loads(Path(x).read_text());bg=load('run/before-render/dance@24fps/geometry.json');ag=load('run/after/render/dance@24fps/geometry.json');bm=load('run/before-render/frames.json');am=load('run/after/render/frames.json')
bv=bm['viewport'];av=am['viewport'];left=min(bv['x'],av['x']);right=max(bv['x']+bv['width'],av['x']+av['width']);bottom=min(bv['y'],av['y']);top=max(bv['y']+bv['height'],av['y']+av['height']);scale=min(378/(right-left),480/(top-bottom));cx=(left+right)/2;cy=(top+bottom)/2;left=cx-189/scale;top=cy+240/scale
# Image output pixel -> world -> original source pixels.
def reframe(path,v):
 im=Image.open(path).convert('RGB');s=v['scale'];return im.transform((378,480),Image.Transform.AFFINE,(s/scale,0,(left-v['x'])*s,0,s/scale,(v['y']+v['height']-top)*s),Image.Resampling.BICUBIC,fillcolor=(232,232,232))
raw=subprocess.run(['ffmpeg','-v','error','-i','inputs/dance/clip-audio.mp4','-frames:v','313','-vf','crop=270:480:0:0','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True,check=True).stdout
out=Path('run/after/composite');out.mkdir(exist_ok=True);e=Path('run/evidence');selected=[0,18,24,30,33,48,60,80,84,90,96,108,120,138,144,156,168,174,180,186,192,204,216,228,234,240,258,264,270,275,288,300,312];floor=load('run/after/contact-targets.json');rows=[]
for n in range(313):
 ref=Image.frombytes('RGB',(270,480),raw[n*270*480*3:(n+1)*270*480*3]);after=reframe(f'run/after/render/dance@24fps/f{n:04}.png',av);im=Image.new('RGB',(648,480));im.paste(ref);im.paste(after,(270,0));im.save(out/f'f{n:04}.png')
 if n in selected:
  before=reframe(f'run/before-render/dance@24fps/f{n:04}.png',bv);pair=Image.new('RGB',(1026,504),(232,232,232));pair.paste(ref);pair.paste(before,(270,0));pair.paste(after,(648,0));d=ImageDraw.Draw(pair);d.text((5,484),f'f{n}  t={n/24:.3f}  REFERENCE',fill='black');d.text((275,484),'BEFORE (common world viewport)',fill='black');d.text((653,484),'AFTER',fill='black');pair.save(e/f'compare-f{n:03}.png')
 def soles(g):return {a['slot']:min(a['vertices'][1::2]) for a in g['frames'][n]['attachments'] if a['slot'] in ['shoe_r','shoe_l']}
 b=soles(bg);a=soles(ag);rows.append({'frame':n,'before':b,'after':a,'target':floor['frames'][n]['targetMinSole'],'error':min(a.values())-floor['frames'][n]['targetMinSole']})
summary={'groundMinSoleMaxError':max(abs(x['error']) for x in rows),'maxOtherFootClearance':max(max(x['after'].values())-min(x['after'].values()) for x in rows),'supportBeforeRange':None,'supportAfterRange':None,'viewport':{'left':left,'top':top,'scale':scale},'frames':rows}
support=[n for n,t in enumerate(floor['frames']) if t['jumpLift']==0]
for label in ['before','after']:
 vals=[min(rows[n][label].values()) for n in support];summary['support'+label.title()+'Range']=[min(vals),max(vals),max(vals)-min(vals)]
Path('run/after/comparison-metrics.json').write_text(json.dumps(summary,indent=2)+'\n')
for label,ns in [('key',[18,30,90,96,138,168,180,192,216,258,270,288]),('arms',[18,24,30,33,48,60]),('clothes',[96,120,138,168,192,216]),('legs',[0,84,90,96,180,192])]:
 sheet=Image.new('RGB',(1026,504*len(ns)),(232,232,232))
 for i,n in enumerate(ns):sheet.paste(Image.open(e/f'compare-f{n:03}.png'),(0,i*504))
 sheet.save(e/f'compare-{label}.png')
print({k:v for k,v in summary.items() if k!='frames'});print('313 paired composite PNGs and aligned before/after evidence written')
