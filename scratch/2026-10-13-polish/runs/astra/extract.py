import subprocess
from PIL import Image,ImageDraw
from pathlib import Path
out=Path('run/evidence');samples=[0,18,24,30,33,48,60,72,80,84,90,96,108,120,138,144,156,168,174,180,186,192,204,216,228,240,252,264,270,275,288,300,312]
for n in samples:
 subprocess.run(['ffmpeg','-y','-v','error','-i','inputs/dance/clip-audio.mp4','-vf',f'select=eq(n\\,{n})','-frames:v','1',str(out/f'before-f{n:03}.png')],check=True)
# Exact reference head samples at each sixth input frame, not fps resampling.
subprocess.run(['ffmpeg','-y','-v','error','-i','inputs/reference/ref1080.mp4','-vf','select=not(mod(n\\,6)),crop=420:420:350:330,scale=168:168','-fps_mode','vfr',str(out/'head-%03d.png')],check=True)
paths=sorted(out.glob('head-[0-9][0-9][0-9].png')); sheet=Image.new('RGB',(8*168,7*192),'#dddddd');draw=ImageDraw.Draw(sheet)
for i,p in enumerate(paths):
 x=i%8*168;y=i//8*192;sheet.paste(Image.open(p),(x,y));draw.text((x+3,y+170),f'f{i*6} t={i/4:.2f}',fill='black')
sheet.save(out/'head-exact.png')
# Exact compared samples grouped temporally, all body units visible.
for group,ns in [('arms',samples[1:12]+[168,174,180,186,270,275]),('body',[0,80,84,90,96,168,174,180,264,270]),('legs',[0,72,96,144,168,180,192,216,264,288]),('clothes',[96,108,120,138,156,192,204,216,228,240])]:
 sheet=Image.new('RGB',(648*3,504*((len(ns)+2)//3)),'#dddddd');d=ImageDraw.Draw(sheet)
 for i,n in enumerate(ns):
  x=i%3*648;y=i//3*504;sheet.paste(Image.open(out/f'before-f{n:03}.png'),(x,y));d.text((x+4,y+482),f'f{n} t={n/24:.3f}',fill='black')
 sheet.save(out/f'{group}-before.png')
print(f'Extracted {len(samples)} paired evidence frames, {len(paths)} exact head frames and 4 unit sheets')
