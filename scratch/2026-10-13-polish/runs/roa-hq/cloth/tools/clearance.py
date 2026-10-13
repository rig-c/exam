"""Rest-pose clearance between the skirt's side edges and the thighs' outer edges, as the
inward rotation (degrees) of the skirt edge about a chain root that first touches the thigh.
usage: clearance.py <geometry.json> <images> <rootL_x,rootL_y> <rootR_x,rootR_y>   (world)"""
import json,sys,numpy as np
from PIL import Image
sys.path.insert(0,sys.path[0]); import xing
g=json.load(open(sys.argv[1])); imgs=sys.argv[2]
rest={r['slot']:r for r in g['rest']}
A=lambda s: np.asarray(Image.open(f"{imgs}/{rest[s]['attachment']}.png").convert('RGBA'))[...,3]
sk=xing.raster(rest['bottomwear']['vertices'],rest['bottomwear']['uvs'],rest['bottomwear']['triangles'],A('bottomwear'))
th={s:xing.raster(rest[s]['vertices'],xing.REGION_UV,rest[s]['triangles'],A(s)) for s in ('thigh_r','thigh_l')}
for side,root,thn,left in (('L',sys.argv[3],'thigh_r',True),('R',sys.argv[4],'thigh_l',False)):
    rx,ry=map(float,root.split(','))
    rows=np.nonzero(sk.any(1))[0]
    top,bot=rows.max(),rows.min(); low=rows[rows<=bot+0.5*(top-bot)]
    ex=lambda r:(np.nonzero(sk[r])[0].min() if left else np.nonzero(sk[r])[0].max())
    cr=min(low,key=lambda r: ex(r) if left else -ex(r)); rows=rows[rows>=cr]
    pts=[]
    for r in rows:
        c=np.nonzero(sk[r])[0]; pts.append(((c.min() if left else c.max())+xing.X0+0.5, r+xing.Y0+0.5))
    pts=np.array(pts)
    t=th[thn]
    def edge(y):
        r=int(np.floor(y-xing.Y0));
        if r<0 or r>=xing.H: return None
        c=np.nonzero(t[r])[0]
        if len(c)==0: return None
        return (c.min() if left else c.max())+xing.X0+0.5
    gaps=[(y,(edge(y)-x) if left else (x-edge(y))) for x,y in pts if edge(y) is not None]
    gy=min(gaps,key=lambda a:a[1])
    sgn=1 if left else -1   # inward rotation sign (CCW moves a left-side down-pointing edge right)
    hit=None
    for deg in np.arange(0,40,0.1):
        a=np.radians(sgn*deg); c,s=np.cos(a),np.sin(a)
        q=np.c_[rx+c*(pts[:,0]-rx)-s*(pts[:,1]-ry), ry+s*(pts[:,0]-rx)+c*(pts[:,1]-ry)]
        bad=False
        for x,y in q:
            e=edge(y)
            if e is None: continue
            if (left and x>e) or ((not left) and x<e): bad=True; break
        if bad: hit=deg; break
    print(side, 'min rest gap %.1f units at y %.1f'%(-gy[1] if left else -gy[1], gy[0]) if False else '', 'rest gaps (edge->thigh) min', round(min(a[1] for a in gaps),1), 'contact after inward rotation about root (%.1f,%.1f): %s deg'%(rx,ry,None if hit is None else round(hit,1)))
