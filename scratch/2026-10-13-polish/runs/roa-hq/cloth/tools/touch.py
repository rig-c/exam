"""Rest-pose hem corners and the thigh contact points beside them, in world and leg-local units.
usage: touch.py <geometry.json> <images>"""
import json,sys,math,numpy as np
from PIL import Image
sys.path.insert(0,sys.path[0]); import xing
g=json.load(open(sys.argv[1])); imgs=sys.argv[2]
rest={r['slot']:r for r in g['rest']}
A=lambda s: np.asarray(Image.open(f"{imgs}/{rest[s]['attachment']}.png").convert('RGBA'))[...,3]
sk=xing.raster(rest['bottomwear']['vertices'],rest['bottomwear']['uvs'],rest['bottomwear']['triangles'],A('bottomwear'))
SB={b['name']:b for b in g['setup']['bones']}
out={}
for side,thn,leg,left in (('r','thigh_r','leg_r0',True),('l','thigh_l','leg_l0',False)):
    th=xing.raster(rest[thn]['vertices'],xing.REGION_UV,rest[thn]['triangles'],A(thn))
    s=xing.side(sk,th,left)
    r=int(s['cornerY']-xing.Y0); c=np.nonzero(th[r])[0]
    tx=(c.min() if left else c.max())+xing.X0+0.5
    C=(tx, s['cornerY']+0.5); K=(s['cornerX']+0.5, s['cornerY']+0.5)
    b=SB[leg]; ang=math.atan2(b['c'],b['a'])
    dx,dy=C[0]-b['worldX'],C[1]-b['worldY']
    lx=math.cos(-ang)*dx-math.sin(-ang)*dy; ly=math.sin(-ang)*dx+math.cos(-ang)*dy
    out[side]=dict(corner=K,contact=C,gap=abs(C[0]-K[0]),legLocal=(round(lx,3),round(ly,3)))
print(json.dumps(out))
