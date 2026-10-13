"""Crossing count: frames where the skirt's side edge lies inside the thigh outline.

usage: xing.py <geometry.json> <images dir> <out.json> [skirt slot names, comma-separated]

Everything is read in world units off `rigc render --geometry` (posed vertices + rest uvs)
and the part PNGs' alpha, rasterised on a 1-unit world grid -- no rendered pixels are read.

Per frame and per side (screen-left = thigh_r, screen-right = thigh_l):
  corner  = the skirt silhouette's outermost texel on that side, in the lower half of the
            skirt's height that frame (the hem's side corner);
  pen(y)  = how far the thigh's outer edge sticks out past the skirt's outer edge on row y,
            for rows from the corner up to the skirt's top (rows below the corner are under
            the hem, where a visible thigh is correct);
  depth   = max pen(y) (units; > 0 means the thigh shows beside the skirt = the skirt edge is
            inside the thigh outline);  area = sum of positive pen over rows (units^2).
A frame is a crossing when depth > 1 unit on either side ("deep" when > 4 units).
"""
import json, sys, numpy as np
from PIL import Image

X0, X1, Y0, Y1 = -300, 300, 250, 900   # world box, 1 unit per cell
W, H = X1 - X0, Y1 - Y0

def raster(verts, uvs, tris, alpha):
    """alpha-tested coverage of a textured triangle list on the world grid."""
    m = np.zeros((H, W), bool)
    ah, aw = alpha.shape
    V = np.asarray(verts).reshape(-1, 2); U = np.asarray(uvs).reshape(-1, 2)
    T = np.asarray(tris).reshape(-1, 3)
    for a, b, c in T:
        p = V[[a, b, c]]
        x0 = int(np.floor(p[:, 0].min())) ; x1 = int(np.ceil(p[:, 0].max()))
        y0 = int(np.floor(p[:, 1].min())) ; y1 = int(np.ceil(p[:, 1].max()))
        x0 = max(x0, X0); x1 = min(x1, X1 - 1); y0 = max(y0, Y0); y1 = min(y1, Y1 - 1)
        if x1 < x0 or y1 < y0: continue
        gx, gy = np.meshgrid(np.arange(x0, x1 + 1) + 0.5, np.arange(y0, y1 + 1) + 0.5)
        (ax, ay), (bx, by), (cx, cy) = p
        d = (by - cy) * (ax - cx) + (cx - bx) * (ay - cy)
        if abs(d) < 1e-9: continue
        l1 = ((by - cy) * (gx - cx) + (cx - bx) * (gy - cy)) / d
        l2 = ((cy - ay) * (gx - cx) + (ax - cx) * (gy - cy)) / d
        l3 = 1 - l1 - l2
        ins = (l1 >= -1e-6) & (l2 >= -1e-6) & (l3 >= -1e-6)
        if not ins.any(): continue
        uv = l1[..., None] * U[a] + l2[..., None] * U[b] + l3[..., None] * U[c]
        tx = np.clip((uv[..., 0] * aw).astype(int), 0, aw - 1)
        ty = np.clip((uv[..., 1] * ah).astype(int), 0, ah - 1)
        hit = ins & (alpha[ty, tx] > 127)
        yy, xx = np.nonzero(hit)
        m[yy + y0 - Y0, xx + x0 - X0] = True
    return m

REGION_UV = [0, 1, 0, 0, 1, 0, 1, 1]   # BL, UL, UR, BR (rigc geometry's region order)

def side(sk, th, left):
    rows = np.nonzero(sk.any(1))[0]
    if len(rows) == 0: return None
    top, bot = rows.max(), rows.min()
    low = rows[rows <= bot + 0.5 * (top - bot)]
    xs = np.arange(W)
    def edge(m, r):
        c = np.nonzero(m[r])[0]
        if len(c) == 0: return None
        return c.min() if left else c.max()
    best = None
    for r in low:
        e = edge(sk, r)
        if best is None or (e < best[1] if left else e > best[1]): best = (r, e)
    cr, ce = best
    pens = []
    for r in range(cr, top + 1):
        e = edge(sk, r); t = edge(th, r)
        if e is None or t is None: continue
        pens.append((e - t) if left else (t - e))
    pens = np.array(pens) if pens else np.array([0.0])
    return dict(cornerX=float(ce + X0), cornerY=float(cr + Y0), depth=float(pens.max()),
                area=float(np.clip(pens, 0, None).sum()))

def main():
    g = json.load(open(sys.argv[1])); imgs = sys.argv[2]; out = sys.argv[3]
    skirt_slots = sys.argv[4].split(',') if len(sys.argv) > 4 else ['bottomwear']
    rest = {r['slot']: r for r in g['rest']}
    alpha = {}
    def A(slot):
        if slot not in alpha:
            alpha[slot] = np.asarray(Image.open(f"{imgs}/{rest[slot]['attachment']}.png").convert('RGBA'))[..., 3]
        return alpha[slot]
    res = []
    for f in g['frames']:
        at = {a['slot']: a for a in f['attachments']}
        sk = np.zeros((H, W), bool)
        for s in skirt_slots:
            if s in at:
                sk |= raster(at[s]['vertices'], rest[s]['uvs'], rest[s]['triangles'], A(s))
        th = {}
        for s in ('thigh_r', 'thigh_l'):
            th[s] = raster(at[s]['vertices'], REGION_UV, rest[s]['triangles'], A(s))
        L = side(sk, th['thigh_r'], True); R = side(sk, th['thigh_l'], False)
        res.append(dict(i=f['index'], t=f['time'], L=L, R=R))
    depth = np.array([max(r['L']['depth'], r['R']['depth']) for r in res])
    summ = dict(frames=len(res), crossing=int((depth > 1).sum()), deep=int((depth > 4).sum()),
                maxDepth=float(depth.max()), worstFrame=int(np.argmax(depth)),
                sumArea=float(sum(r['L']['area'] + r['R']['area'] for r in res)),
                byWindow={})
    for n, (t0, t1) in {'A': (3.9, 7.4), 'B': (7.6, 11.1), 'all': (0, 99)}.items():
        sel = [k for k, r in enumerate(res) if t0 <= r['t'] < t1]
        d = depth[sel]
        summ['byWindow'][n] = dict(frames=len(sel), crossing=int((d > 1).sum()), deep=int((d > 4).sum()), maxDepth=round(float(d.max()), 2) if len(d) else None)
    json.dump(dict(summary=summ, frames=res), open(out, 'w'))
    print(json.dumps(summ))

if __name__ == '__main__':
    main()
