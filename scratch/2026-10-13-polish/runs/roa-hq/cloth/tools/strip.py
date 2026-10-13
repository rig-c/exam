"""usage: strip.py out.png frame,frame,... dirA[,dirB...]  -- video | each render dir, skirt band crop"""
import sys
from PIL import Image, ImageDraw
out=sys.argv[1]; fr=[int(x) for x in sys.argv[2].split(',')]; dirs=sys.argv[3].split(',')
P='<scratch>/dancer-2026-10-13/polish1_cloth'
rows=[]
for i in fr:
    v=Image.open(f'{P}/look/ref/r{i+1:04d}.png').convert('RGB')      # 540x960
    v=v.crop((60,330,480,690)).resize((420,360))
    ims=[v]
    for d in dirs:
        r=Image.open(f'{d}/render/dance@24fps/f{i:04d}.png').convert('RGB')  # 628x800
        ims.append(r.crop((104,300,524,660)))
    row=Image.new('RGB',(420*len(ims),360),'white')
    for k,im in enumerate(ims): row.paste(im,(420*k,0))
    ImageDraw.Draw(row).text((5,5),f'f{i} t={i/24:.2f}s',fill=(255,0,0))
    rows.append(row)
W=Image.new('RGB',(rows[0].width,360*len(rows)),'white')
for k,r in enumerate(rows): W.paste(r,(0,360*k))
W.save(out)
