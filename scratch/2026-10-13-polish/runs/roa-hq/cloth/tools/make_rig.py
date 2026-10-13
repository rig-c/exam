"""Rewrite the dancer's skirt in a copy of the k0 rig spec: N radial chains (a fan along the
pleats), a rigc `segments` mesh over them, physics on every link, and per-chain clamps --
the outer chains' clamp measured against the thigh ("leg stop"), the inner ones a static cap.

usage: make_rig.py <config.json> <out rig dir> [--copy-images]

Everything else in the k0 spec (bones, slots, the five arm/topwear sets, the other meshes,
foot_level) is carried through unchanged; the motion is pose6/k0's, with the idle's tiny
hem sway copied onto the new middle chains.

Part pixels -> world: x = px - 109, y = 756 - py (read off the k0 build's rest geometry:
a least-squares fit of the authored mesh's uvs to its setup vertices, residual < 1e-6);
the hip sits at world (0, 673), i.e. part px (109, 83).
"""
import json, math, sys, os, shutil, copy

D = '<scratch>/dancer-2026-10-13'
K0 = f'{D}/k0/rig'
MOTION = f'{D}/polish1_cloth/src/motion_pose6_k0.json'
HIP_Y = 673.0
PX2W = lambda px, py: (px - 109.0, 756.0 - py)

cfg = json.load(open(sys.argv[1]))
out = sys.argv[2]
os.makedirs(out, exist_ok=True)
rig = json.load(open(f'{K0}/rig.json'))

names = cfg['chains']                    # screen left -> right, e.g. ["r","rm","c","lm","l"]
n = len(names)
root_py, tip_py = cfg['rootPy'], cfg['tipPy']
rx0, rx1 = cfg['rootPx']                 # outermost roots, part px
tx0, tx1 = cfg['tipPx']                  # outermost tips, part px
links = cfg['links']                     # per-link physics: [{inertia,strength,damping,mass,mix}, ...]
nl = len(links)

# --- drop the old skirt bones / constraints / detached entries ---------------------------
is_skirt = lambda nm: nm.startswith('skirt_')
rig['bones'] = [b for b in rig['bones'] if not is_skirt(b['name'])]
old_cons = rig['constraints']
keep = [c for c in old_cons if not (c['name'].startswith('skirt_'))]
rig['invariants']['detached'] = [d for d in rig['invariants']['detached']
                                 if not (is_skirt(d['notUnder']) or is_skirt(d['bone']))]

B = {b['name']: b for b in rig['bones']}

bones, cons, detached, chains_for_mesh, late = [], [], [], [], []
drv = cfg.get('driver')
if drv:
    # one pendulum for the whole skirt: hangs from the waist centre, and every chain's first
    # link takes its swing (times that chain's scale) instead of running its own spring --
    # so a hip roll cannot kick two chains in opposite directions into each other
    wy = round(PX2W(109, root_py)[1] - HIP_Y, 3)
    bones.append(dict(name='skirt_swing', parent='hip', length=drv['length'], rotation=-90, x=0, y=wy))
    cons.append(dict(type='physics', name='skirt_swing_phys', bone='skirt_swing', rotate=1,
                     inertia=drv['inertia'], strength=drv['strength'], damping=drv['damping'],
                     mass=drv.get('mass', 1), mix=drv['mix']))
for k, nm in enumerate(names):
    f = k / (n - 1)
    rpx = rx0 + f * (rx1 - rx0); tpx = tx0 + f * (tx1 - tx0)
    rw = PX2W(rpx, root_py); tw = PX2W(tpx, tip_py)
    dx, dy = tw[0] - rw[0], tw[1] - rw[1]
    L = math.hypot(dx, dy); ang = math.degrees(math.atan2(dy, dx)); ll = round(L / nl, 3)
    rx, ry = round(rw[0], 3), round(rw[1] - HIP_Y, 3)
    stop = cfg['stops'].get(nm)
    pre = f'skirt_{nm}'
    if stop:


        # the stop frame: aims (one-bone IK) from the chain root at a point fixed on the thigh --
        # its outer edge at the hem corner's height at rest -- so the clamp's bound is "the hem
        # corner's direction reaches the thigh edge", whatever the leg and the hip do
        cw = stop['touchWorld']
        aRC = math.degrees(math.atan2(cw[1] - rw[1], cw[0] - rw[0]))
        d0 = ang - aRC
        late.append(dict(name=f'{pre}_touch', parent=stop['leg'], x=stop['touchLocal'][0], y=stop['touchLocal'][1]))
        bones.append(dict(name=f'{pre}_stop', parent='hip', length=ll, rotation=round(aRC, 6), x=rx, y=ry))
    bones.append(dict(name=f'{pre}0_ctl', parent='hip', length=ll, rotation=round(ang, 6), x=rx, y=ry))
    bones.append(dict(name=f'{pre}0', parent=f'{pre}0_ctl', length=ll, rotation=0, x=0, y=0))
    if stop:
        bones.append(dict(name=f'{pre}0_rel', parent=f'{pre}_stop', length=ll, rotation=round(d0, 6), x=0, y=0))
        bones.append(dict(name=f'{pre}0_d', parent=f'{pre}_stop', length=ll, rotation=round(d0, 6), x=0, y=0))
    else:
        bones.append(dict(name=f'{pre}0_d', parent=f'{pre}0_ctl', length=ll, rotation=0, x=0, y=0))
    parent = f'{pre}0_d'
    lc = cfg.get('linkClamp')
    for i in range(1, nl):
        bones.append(dict(name=f'{pre}{i}_ctl', parent=parent, length=ll, rotation=0, x=ll, y=0))
        bones.append(dict(name=f'{pre}{i}', parent=f'{pre}{i}_ctl', length=ll, rotation=0, x=0, y=0))
        if lc:
            # the drawn link: the physics link's bend off its parent, clamped (no whip past it)
            bones.append(dict(name=f'{pre}{i}_d', parent=f'{pre}{i}_ctl', length=ll, rotation=0, x=0, y=0))
            parent = f'{pre}{i}_d'
        else:
            parent = f'{pre}{i}'
    chains_for_mesh.append([f'{pre}0_d'] + [f'{pre}{i}' + ('_d' if lc else '') for i in range(1, nl)])

    def phys(bn, p):
        return dict(type='physics', name=f'{bn}_phys', bone=bn, rotate=1,
                    inertia=p['inertia'], strength=p['strength'], damping=p['damping'],
                    mass=p.get('mass', 1), mix=p['mix'])
    if stop:
        cons.append(dict(type='ik', name=f'{pre}_stop_aim', bones=[f'{pre}_stop'], target=f'{pre}_touch', mix=1))
        detached.append(dict(bone=f'{pre}_touch', notUnder=f'{pre}_stop', why=f'"{pre}_touch" is the target of "{pre}_stop_aim", which turns "{pre}_stop"'))
    if drv:
        cons.append(dict(type='transform', name=f'{pre}0_swing', source='skirt_swing', bones=[f'{pre}0'],
                         localSource=True, localTarget=True, additive=True,
                         properties=dict(rotate=dict(offset=-90, to=dict(rotate=dict(scale=drv['scale'][k])))),
                         mixRotate=1))
        detached.append(dict(bone='skirt_swing', notUnder=f'{pre}0', why=f'"skirt_swing" is the source of "{pre}0_swing"'))
    else:
        cons.append(phys(f'{pre}0', links[0]))
    if stop:
        # inward is + for a screen-left chain (CCW turns a down-pointing link toward the body)
        inward = 1 if stop['side'] == 'left' else -1
        bound = d0 + inward * (stop['alpha'] - stop.get('margin', 0))
        far = d0 - inward * stop['flare']
        lo, hi = round(min(bound, far), 4), round(max(bound, far), 4)
        print(f'  {pre}: chain {ang:.2f}, aim {aRC:.2f}, d0 {d0:.2f}, clamp [{lo}, {hi}]')
    else:
        lo, hi = cfg['cap']
    if stop:
        cons.append(dict(type='transform', name=f'{pre}0_rel_copy', source=f'{pre}0', bones=[f'{pre}0_rel'],
                         properties=dict(rotate=dict(to=dict(rotate={}))), mixRotate=1))
        detached.append(dict(bone=f'{pre}0', notUnder=f'{pre}0_rel', why=f'"{pre}0" is the source of "{pre}0_rel_copy"'))
        src = f'{pre}0_rel'
    else:
        src = f'{pre}0'
    cons.append(dict(type='transform', name=f'{pre}0_clamp', source=src, bones=[f'{pre}0_d'],
                     localSource=True, localTarget=True, clamp=True,
                     properties=dict(rotate=dict(offset=lo, to=dict(rotate=dict(offset=lo, max=hi, scale=1)))),
                     mixRotate=1))
    detached.append(dict(bone=src, notUnder=f'{pre}0_d', why=f'"{src}" is the source of "{pre}0_clamp"'))
    for i in range(1, nl):
        lp = dict(links[i])
        if cfg.get('linkStrengthScale'):
            # per-chain spring differences: neighbouring hem tips stop moving in lockstep
            lp['strength'] = round(lp['strength'] * cfg['linkStrengthScale'][k], 3)
        cons.append(phys(f'{pre}{i}', lp))
        if lc:
            if stop:
                inward = 1 if stop['side'] == 'left' else -1
                a, b = inward * lc['stopInward'], -inward * lc['stopOutward']
                l1, h1 = min(a, b), max(a, b)
            else:
                l1, h1 = -lc['inner'], lc['inner']
            cons.append(dict(type='transform', name=f'{pre}{i}_clamp', source=f'{pre}{i}', bones=[f'{pre}{i}_d'],
                             localSource=True, localTarget=True, clamp=True,
                             properties=dict(rotate=dict(offset=l1, to=dict(rotate=dict(offset=l1, max=h1, scale=1)))),
                             mixRotate=1))
            detached.append(dict(bone=f'{pre}{i}', notUnder=f'{pre}{i}_d', why=f'"{pre}{i}" is the source of "{pre}{i}_clamp"'))

# bones: insert where the old skirt bones were (after hairpin), keeping the rest in order
idx = [b['name'] for b in rig['bones']].index('hairpin') + 1
rig['bones'] = rig['bones'][:idx] + bones + rig['bones'][idx:] + late
i0 = [c['name'] for c in keep].index('foot_level') + 1
rig['constraints'] = keep[:i0] + cons + keep[i0:]
rig['invariants']['detached'] += detached

# the mesh
bw = rig['skins']['default']['bottomwear']['bottomwear']
seg = dict(kind='segments', cell=cfg['cell'],
           bones=[dict(bone='hip', **{'from': cfg['waist'][0], 'to': cfg['waist'][1]})] + chains_for_mesh,
           falloff=cfg['falloff'], anchor=[109, 83])
rig['skins']['default']['bottomwear']['bottomwear'] = dict(type='mesh', image=bw['image'], generator=seg)
if 'meshTriangles' in cfg:
    rig['invariants']['meshTriangles'] = cfg['meshTriangles']

json.dump(rig, open(f'{out}/rig.json', 'w'), indent=1)

# motion: copy the idle hem sway of the nearest original chain onto each new chain name
m = json.load(open(MOTION))
src_of = cfg.get('idleFrom', {})
idle = m['animations']['idle']['tracks']
add = []
for nm in names:
    s = src_of.get(nm)
    if not s or s == nm: continue
    for t in idle:
        b = t.get('bone', '')
        if b.startswith(f'skirt_{s}') and b.endswith('_ctl'):
            i = b[len(f'skirt_{s}'):-4]
            if int(i) < nl:
                t2 = copy.deepcopy(t); t2['bone'] = f'skirt_{nm}{i}_ctl'; add.append(t2)
valid = {b['name'] for b in rig['bones']}
m['animations']['idle']['tracks'] = [t for t in idle if t.get('bone') is None or t['bone'] in valid] + add
json.dump(m, open(f'{out}/motion.json', 'w'), indent=1)
if '--copy-images' in sys.argv:
    if os.path.exists(f'{out}/images'): shutil.rmtree(f'{out}/images')
    shutil.copytree(f'{K0}/images', f'{out}/images')
print(f'{out}: {len(rig["bones"])} bones, {len(rig["constraints"])} constraints; chains',
      {nm: c for nm, c in zip(names, chains_for_mesh)})
