import json,sys,numpy as np
from PIL import Image
sys.path.insert(0,sys.path[0])
import xing
g=json.load(open(sys.argv[1])); imgs=sys.argv[2]; fi=int(sys.argv[3]); out=sys.argv[4]
rest={r['slot']:r for r in g['rest']}
f=g['frames'][fi]; at={a['slot']:a for a in f['attachments']}
A=lambda s: np.asarray(Image.open(f"{imgs}/{rest[s]['attachment']}.png").convert('RGBA'))[...,3]
sk=xing.raster(at['bottomwear']['vertices'],rest['bottomwear']['uvs'],rest['bottomwear']['triangles'],A('bottomwear'))
tr=xing.raster(at['thigh_r']['vertices'],xing.REGION_UV,rest['thigh_r']['triangles'],A('thigh_r'))
tl=xing.raster(at['thigh_l']['vertices'],xing.REGION_UV,rest['thigh_l']['triangles'],A('thigh_l'))
img=np.full((xing.H,xing.W,3),255,np.uint8)
img[tr|tl]=(230,120,120); img[sk]=(60,60,140); img[sk&(tr|tl)]=(120,60,160)
L=xing.side(sk,tr,True); R=xing.side(sk,tl,False)
for s in (L,R):
    x=int(s['cornerX']-xing.X0); y=int(s['cornerY']-xing.Y0); img[max(0,y-3):y+4,max(0,x-3):x+4]=(0,200,0)
im=Image.fromarray(img[::-1]).crop((50,150,550,550)).resize((1000,800),Image.NEAREST); im.save(out); print(L,R)
