#!/usr/bin/env python3
"""Grade one run: rebuild from the files it hands in, on the pinned versions, and write result.json.

    python3 grade.py runs/<date>-<model>-<task> [--fixture <name>|none]

The run directory names its task by its last component (…-01-build, …-04-soft). Nothing the run pasted is
read: the config (and any file it names) is copied beside the task's inputs into .grade/<run>/, built
there, and every line below is read off what that build wrote. Needs npm, bun and python3; installs the
pinned packages into ./node_modules on first use.

A run set on a fixture (fixtures/<name>/: the one tasks/<task>/fixture.json names, or `--fixture <name>`;
`--fixture none` grades a task on its own inputs, as Round 3's task 05 was) is built on that fixture's inputs, with every
file its config.json names copied beside them, and its lines read the part names in fixtures/<name>/grade-roles.json
where the task's own lines name the painted figure's. A line the fixture's rig cannot discriminate is
reported SKIP with its reason: it is kept out of the lines counted, and listed in result.json under `skipped`.
"""
import datetime, json, os, re, shutil, statistics, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
BIN = os.path.join(ROOT, 'node_modules', '.bin')
UNCOVERED_LINE = {'01-build': 4200, '02-move': 4200, '03-correct': 3500, '04-soft': 4200, '05-dance': 4200}   # rig px; about twice what the proposed plan leaves (2,059; 1,726)
KEPT_MESHES = 8          # task 03: the meshes the proposal drafts on its painting
RISE_LINE = 150         # rig px a hand rises above the rest of the body, task 02
FPS = 12
STILL_MOVES = 23        # task 03: rig px the back hair travels against the head over the idle — half of what the draft's
                        # own amplitudes give once its two chains agree (45.9); the same amplitudes cut to a quarter give 17.5
SOFT = (3.0, 15.0)      # task 04: rig px the soft patch differs from the same build without its physics, on the hop
PATCH = (8, 0.80)       # task 04: at least 8 of the part's vertices move, and at most 80 % of them — a patch, not the garment
BUDGET = 700            # task 04: triangles in the whole rig; the recipe's own region spacing, copied, gives 920 here
DANCE = {'seconds': 4.0, 'fps': 24, 'closes': 0.5, 'hand': 100.0, 'body': 15.0, 'time': 0.5, 'ankle': 6.0, 'budget': 1000}
                        # task 05: 8 beats at 120 a minute; rig px a frame apart at the loop's ends; rig px each hand's part and every
                        # vertex of the trunk must travel; the share of the figure's changes of speed that repeat every two beats;
                        # rig px the bottom of the legs may leave the feet; triangles

def run(cmd, cwd, log):
    with open(log, 'a') as f:
        f.write('$ ' + ' '.join(cmd) + '\n'); f.flush()
        return subprocess.run(cmd, cwd=cwd, stdout=f, stderr=subprocess.STDOUT).returncode

def folds(work, animation, log):
    out = os.path.join(work, 'folds_' + animation)
    code = run([os.path.join(BIN, 'rigc'), 'render', '--candidate', 'out/check/build', '--animation', animation,
                '--fps', str(FPS), '--folds', '--geometry', '--out', out], work, log)
    if code != 0: return None, None
    d = os.path.join(out, animation)
    f = json.load(open(os.path.join(d, 'folds.json')))
    folding = [m['slot'] for m in f['meshes'] if m.get('frames')]
    return folding, json.load(open(os.path.join(d, 'geometry.json')))

def slot_vertices(frame):
    out = {}
    for a in frame['attachments']:
        v = a.get('vertices')
        if v: out[a['slot']] = v if not isinstance(v[0], list) else [c for p in v for c in p]
    return out

def travel(geometry, slot, bone):
    """The furthest any vertex of a slot gets from where it was in the first frame, measured from a bone's origin."""
    base = None; best = 0.0
    for f in geometry['frames']:
        v = slot_vertices(f).get(slot); b = next((x for x in f['bones'] if x['name'] == bone), None)
        if v is None or b is None: return None
        rel = [(v[i] - b['worldX'], v[i + 1] - b['worldY']) for i in range(0, len(v), 2)]
        if base is None: base = rel; continue
        best = max(best, max(((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** 0.5 for p, q in zip(rel, base)))
    return round(best, 3)

def difference(a, b, slot):
    """Two builds of one rig posed on the same frames: the largest distance between a slot's matching vertices, and how many moved."""
    best = (0.0, None, 0, 0)
    for fa, fb in zip(a['frames'], b['frames']):
        x, y = slot_vertices(fa).get(slot), slot_vertices(fb).get(slot)
        if x is None or y is None or len(x) != len(y): return None
        d = [((x[i] - y[i]) ** 2 + (x[i + 1] - y[i + 1]) ** 2) ** 0.5 for i in range(0, len(x), 2)]
        if best[1] is None or max(d) > best[0]: best = (round(max(d), 3), fa['index'], sum(1 for k in d if k > 0.5), len(d))
    return best

def pose(work, build, animation, fps, log):
    out = os.path.join(work, 'pose_' + build.replace('/', '_') + '_' + animation)
    code = run([os.path.join(BIN, 'rigc'), 'render', '--candidate', build, '--animation', animation, '--fps', str(fps),
                '--max', '256', '--folds', '--geometry', '--out', out], work, log)
    if code != 0: return None, None
    d = next((os.path.join(out, n) for n in sorted(os.listdir(out)) if n.startswith(animation) and os.path.isdir(os.path.join(out, n))), None)
    if d is None: return None, None
    return json.load(open(os.path.join(d, 'geometry.json'))), [m['slot'] for m in json.load(open(os.path.join(d, 'folds.json')))['meshes'] if m.get('frames')]

def rise(geometry):
    """The largest rise of any bone's origin above its first-frame height, less the median bone's rise."""
    frames = geometry['frames']; first = {b['name']: b['worldY'] for b in frames[0]['bones']}
    best = 0.0
    for f in frames:
        d = [b['worldY'] - first[b['name']] for b in f['bones']]
        best = max(best, max(d) - statistics.median(d))
    return round(best, 1)

def band(rest, lo, hi):
    """Indices of a part's vertices between two fractions of its height at the rest pose, measured from its bottom (y up)."""
    ys = rest[1::2]; a, b = min(ys), max(ys)
    return [i for i, y in enumerate(ys) if a + lo * (b - a) <= y <= a + hi * (b - a)]

ARM = {'upper': ((0.82, 0.92), (0.72, 0.82), (0.62, 0.72)), 'fore': ((0.38, 0.46), (0.30, 0.38), (0.22, 0.30)), 'straight': 8.0}
                        # an arm part, shoulder to fingertips, by height above its lowest point at rest: on this painting the
                        # elbow is at about 0.54 and the wrist at about 0.20. Three bands of the upper arm and three of the forearm; degrees
                        # either may bend along its own length, against the same reading at rest. The bands keep clear of the elbow, where the
                        # skin blends from one bone to the next

def arm_read(rest, frames, slot, mid_x):
    """Per frame, for one arm part: degrees the forearm is turned toward the trunk's middle from the line of the upper arm,
    less the same at rest; and the largest bend along the upper arm or along the forearm themselves, less the same at
    rest. None when a band holds no vertex."""
    import math
    bands = {k: [band(rest[slot], lo, hi) for lo, hi in v] for k, v in ARM.items() if k != 'straight'}
    if any(not ii for v in bands.values() for ii in v): return None
    side = 1 if sum(rest[slot][0::2]) / (len(rest[slot]) // 2) < mid_x else -1   # an arm on the image's left: counter-clockwise is toward the middle
    def read(v):
        c = {k: [(sum(v[2 * i] for i in ii) / len(ii), sum(v[2 * i + 1] for i in ii) / len(ii)) for ii in b] for k, b in bands.items()}
        ang = lambda p, q: math.atan2(q[1] - p[1], q[0] - p[0])
        wrap = lambda d: (math.degrees(d) + 180) % 360 - 180
        elbow = side * wrap(ang(c['fore'][0], c['fore'][2]) - ang(c['upper'][0], c['upper'][2]))
        kink = {k: wrap(ang(c[k][1], c[k][2]) - ang(c[k][0], c[k][1])) for k in c}
        return elbow, kink
    e0, k0 = read(rest[slot]); out = []
    for f in frames:
        e, k = read(f[slot]); out.append((e - e0, max(abs(k[x] - k0[x]) for x in k)))
    return out

def paths(geometry, slot, against=None):
    """Per vertex of a slot, the diagonal of the box its path fills over the frames — measured from the centre of another slot when one is named."""
    xs = ys = None
    for f in geometry['frames']:
        sv = slot_vertices(f); v = sv.get(slot)
        if v is None: return None
        ox = oy = 0.0
        if against:
            o = sv.get(against)
            if o is None: return None
            ox, oy = sum(o[0::2]) / (len(o) // 2), sum(o[1::2]) / (len(o) // 2)
        if xs is None: xs = [[] for _ in range(len(v) // 2)]; ys = [[] for _ in range(len(v) // 2)]
        if len(v) // 2 != len(xs): return None
        for i in range(len(xs)): xs[i].append(v[2 * i] - ox); ys[i].append(v[2 * i + 1] - oy)
    return [((max(x) - min(x)) ** 2 + (max(y) - min(y)) ** 2) ** 0.5 for x, y in zip(xs, ys)]

def loop_gap(geometry):
    """The largest distance between a vertex in the first frame and the same vertex in the last."""
    a, b = slot_vertices(geometry['frames'][0]), slot_vertices(geometry['frames'][-1]); worst = 0.0
    for s in a:
        if s not in b or len(a[s]) != len(b[s]): return None
        worst = max([worst] + [((a[s][i] - b[s][i]) ** 2 + (a[s][i + 1] - b[s][i + 1]) ** 2) ** 0.5 for i in range(0, len(a[s]), 2)])
    return round(worst, 3)

def on_the_beat(geometry, frames_per_two_beats):
    """How fast the figure moves, frame to frame (the mean over every vertex), read round the loop: the share of that
    signal's variation carried by what repeats every two beats. 1 is a figure whose speed repeats exactly; noise gives
    about the reciprocal of the number of harmonics in play."""
    import cmath
    F = [slot_vertices(f) for f in geometry['frames']]; sp = []
    for k in range(1, len(F)):
        d = []
        for s in F[k]:
            a, b = F[k - 1].get(s), F[k][s]
            if a is None or len(a) != len(b): continue
            d += [((b[i] - a[i]) ** 2 + (b[i + 1] - a[i + 1]) ** 2) ** 0.5 for i in range(0, len(a), 2)]
        sp.append(sum(d) / len(d) if d else 0.0)
    n = len(sp)
    if n % frames_per_two_beats: return None
    cycles = n // frames_per_two_beats   # two-beat spans in the loop: a harmonic k repeats every two beats when k is a multiple of this
    power = [abs(sum(sp[t] * cmath.exp(-2j * cmath.pi * k * t / n) for t in range(n))) ** 2 for k in range(1, n // 2 + 1)]
    total = sum(power)
    if total <= 1e-9: return 0.0
    return round(sum(p for k, p in enumerate(power, 1) if k % cycles == 0) / total, 3)

def ankles(geometry, leg='legwear', foot='shoes', band_=0.04, legs=2):
    """How far the end of each leg gets from its foot. The leg part's vertices in the lowest 4 % of its height at the
    first frame are split into two legs at the widest gap in x (a part that holds one leg, legs=1, is not split); each
    leg's end is the middle of its vertices there, and it is held against the foot-part vertex nearest it in the first
    frame. The largest change in that offset over the frames — the middle, so that an ankle turning over a planted foot
    is not read as a leg leaving it."""
    F = [slot_vertices(f) for f in geometry['frames']]; a0, b0 = F[0].get(leg), F[0].get(foot)
    if a0 is None or b0 is None: return None
    P = [(a0[i], a0[i + 1]) for i in range(0, len(a0), 2)]; Q = [(b0[i], b0[i + 1]) for i in range(0, len(b0), 2)]
    lo, hi = min(p[1] for p in P), max(p[1] for p in P); cut = lo + band_ * (hi - lo)   # y up: the lowest band
    low = sorted((i for i, p in enumerate(P) if p[1] <= cut), key=lambda i: P[i][0])
    if not low: return None
    gap = max(range(1, len(low)), key=lambda k: P[low[k]][0] - P[low[k - 1]][0]) if len(low) > 1 and legs > 1 else 0
    ends = [e for e in (low[:gap], low[gap:]) if e]
    worst = 0.0
    for e in ends:
        cx, cy = sum(P[i][0] for i in e) / len(e), sum(P[i][1] for i in e) / len(e)
        j = min(range(len(Q)), key=lambda j: (Q[j][0] - cx) ** 2 + (Q[j][1] - cy) ** 2)
        for f in F:
            a, b = f.get(leg), f.get(foot)
            if a is None or b is None or len(a) != len(a0) or len(b) != len(b0): return None
            x, y = sum(a[2 * i] for i in e) / len(e), sum(a[2 * i + 1] for i in e) / len(e)
            worst = max(worst, (((x - b[2 * j]) - (cx - Q[j][0])) ** 2 + ((y - b[2 * j + 1]) - (cy - Q[j][1])) ** 2) ** 0.5)
    return round(worst, 2)

def without_physics(work, log):
    """The same config with every physics constraint taken out, built beside the first; its build directory, or None."""
    cfg = json.load(open(os.path.join(work, 'config.json')))
    still = dict(cfg); still['constraints'] = [k for k in cfg.get('constraints', []) if k.get('type') != 'physics']
    if not still['constraints']: del still['constraints']
    json.dump(still, open(os.path.join(work, 'config_without_physics.json'), 'w'))
    code = run([os.path.join(BIN, 'rig-parts'), 'build', '--config', 'config_without_physics.json', '--source', 'inputs/painting.png',
                '--full', 'inputs/layers/full', '--head', 'inputs/layers/head', '--out', 'out_without_physics'], work, log)
    return 'out_without_physics/check/build' if code == 0 else None

def clock(path):
    """Minutes between the transcript's `started:` first line and `finished:` last line — the run's own clock."""
    if not os.path.exists(path): return None
    lines = [l.strip() for l in open(path).read().splitlines() if l.strip()]
    if not lines: return None
    a = re.match(r'started:\s*(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)$', lines[0]); b = re.match(r'finished:\s*(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)$', lines[-1])
    if not a or not b: return None
    t = lambda s: datetime.datetime.strptime(s, '%Y-%m-%dT%H:%M:%SZ')
    d = (t(b.group(1)) - t(a.group(1))).total_seconds()
    return round(d / 60, 1) if d >= 0 else None

ROLES = {'05-dance': {'hands': ['handwear_l', 'handwear_r'], 'trunk': 'topwear', 'feet': ['shoes'],
                     'legs': [{'leg': 'legwear', 'foot': 'shoes', 'legs': 2}], 'arms': ['handwear_l', 'handwear_r'], 'not_read': {}}}
                        # the parts a task's lines read, by role, on the task's own painting; a fixture's grade-roles.json names its own

def roles(task, fixture):
    """The task's part roles: the fixture's map for this task where it has one, else the task's own names."""
    own = json.loads(json.dumps(ROLES.get(task, {})))
    p = os.path.join(fixture, 'grade-roles.json') if fixture else None
    if p and os.path.exists(p): own.update(json.load(open(p)).get(task, {}))
    return own

def named_paths(config, base):
    """Relative paths a config names that exist under base: every string anywhere in it, read as a path."""
    out = set()
    def walk(x):
        if isinstance(x, dict): [walk(v) for v in x.values()]
        elif isinstance(x, list): [walk(v) for v in x]
        elif isinstance(x, str) and x and not os.path.isabs(x):
            n = os.path.normpath(x)
            if not n.startswith('..') and n != '.' and os.path.exists(os.path.join(base, n)): out.add(n)
    walk(config)
    return sorted(out)

def rigid_arms(work, arms):
    """When every arm part is rigid (a region on one bone, no mesh) and every joint along the limbs that carry them
    declares a range: the reason the arm line reads nothing on this rig. Else None."""
    rig = json.load(open(os.path.join(work, 'out', 'rig', 'rig.json'))); cfg = json.load(open(os.path.join(work, 'config.json')))
    found = {}
    for skin in (rig.get('skins') or {}).values():
        for slot, atts in skin.items():
            if slot in arms: found.setdefault(slot, []).extend(atts.values())
    if set(found) != set(arms) or any(a.get('type', 'region') != 'region' for v in found.values() for a in v): return None
    joints = []
    for limb in (cfg.get('limbs') or {}).values():
        seg = limb.get('segments', [])
        if not any(x.get('part') in arms for x in seg): continue
        for x in seg[1:]:
            if not x.get('range'): return None
            j = f"{x.get('joint', x.get('part'))} {x['range']}"
            if j not in joints: joints.append(j)
    if not joints: return None
    return (f"not measured: every arm part ({', '.join('`' + a + '`' for a in arms)}) is rigid on one bone and turns only at a joint "
            f"that declares its range ({', '.join(joints)}); a rigid part cannot bend along its own length, so the line has nothing on this rig to tell apart")

def surprises(journal):
    """Entries whose fourth line begins with WTF?: (SURPRISE: in the form before 2026-10-13), as JOURNAL.md asks —
    after the `4.` and the template's optional `**Happened:**` label, so `4. WTF?:` counts as well as
    `4. **Happened:** WTF?:`; not the word wherever it appears."""
    return len(re.findall(r'^4\.\s*(?:\*\*Happened:\*\*\s*)?(?:WTF\?:|SURPRISE:)', journal, re.M))

def main():
    args = sys.argv[1:]; fx = None
    if '--fixture' in args:
        i = args.index('--fixture'); fx = args[i + 1] if i + 1 < len(args) else ''; del args[i:i + 2]
    rundir = os.path.abspath(args[0]); name = os.path.basename(rundir.rstrip('/'))
    task = next((t for t in sorted(os.listdir(os.path.join(ROOT, 'tasks'))) if name.endswith(t)), None)
    if task is None: sys.exit(f'{name}: the run directory must end with a task name, one of ' + ', '.join(sorted(os.listdir(os.path.join(ROOT, "tasks")))))
    own_fx = os.path.join(ROOT, 'tasks', task, 'fixture.json')   # a task set on a fixture names it; --fixture none grades on the task's own inputs
    if fx is None and os.path.exists(own_fx): fx = json.load(open(own_fx))['fixture']
    if fx == 'none': fx = None
    if fx is not None and not os.path.isfile(os.path.join(ROOT, 'fixtures', fx, 'config.json')): sys.exit(f'--fixture {fx}: no fixtures/{fx}/config.json')
    fixture = os.path.join(ROOT, 'fixtures', fx) if fx else None
    if not os.path.isdir(BIN) and subprocess.run(['npm', 'ci'], cwd=ROOT).returncode != 0: sys.exit('npm ci failed')
    work = os.path.join(ROOT, '.grade', name); shutil.rmtree(work, ignore_errors=True); os.makedirs(work)
    log = os.path.join(work, 'grade.log')
    for f in os.listdir(rundir):
        if f.endswith('.json') and f not in ('result.json', 'usage.json'): shutil.copy(os.path.join(rundir, f), work)
    own = os.path.join(ROOT, 'tasks', task, 'inputs')   # a task without a painting of its own is set on task 01's
    if fixture:   # a fixture's inputs, and every other file its config (or the run's) names — the ball caps, say — copied beside them
        os.symlink(os.path.join(fixture, 'inputs'), os.path.join(work, 'inputs'))
        given = [json.load(open(os.path.join(fixture, 'config.json')))] + ([json.load(open(os.path.join(work, 'config.json')))] if os.path.exists(os.path.join(work, 'config.json')) else [])
        for p in sorted({p for c in given for p in named_paths(c, fixture)}):
            src, dst = os.path.join(fixture, p), os.path.join(work, p)
            if os.path.lexists(dst) or p.split(os.sep)[0] == 'inputs': continue
            os.makedirs(os.path.dirname(dst) or work, exist_ok=True)
            shutil.copytree(src, dst) if os.path.isdir(src) else shutil.copy(src, dst)
    else:
        os.symlink(own if os.path.exists(os.path.join(own, 'painting.png')) else os.path.join(ROOT, 'tasks', '01-build', 'inputs'), os.path.join(work, 'inputs'))
    versions = {p: json.load(open(os.path.join(ROOT, 'node_modules', p, 'package.json')))['version'] for p in ('@rig-c/parts', 'rig-c')}
    res = {'run': name, 'task': task, 'versions': versions, 'lines': {}}
    if fx: res['fixture'] = fx
    R = roles(task, fixture)
    L = res['lines']
    if not os.path.exists(os.path.join(work, 'config.json')):
        L['built'] = {'pass': False, 'read': 'no config.json handed in'}
    else:
        code = run([os.path.join(BIN, 'rig-parts'), 'build', '--config', 'config.json', '--source', 'inputs/painting.png',
                    '--full', 'inputs/layers/full', '--head', 'inputs/layers/head', '--out', 'out'], work, log)
        L['built'] = {'pass': code == 0, 'read': f'rig-parts build exit {code}'}
    cj = os.path.join(work, 'out', 'check', 'check.json')
    if os.path.exists(cj):
        c = json.load(open(cj))
        bars = {k: v['status'] for k, v in c.items() if isinstance(v, dict) and 'status' in v}
        L['checked'] = {'pass': c.get('PASS') is True, 'read': bars}
        u = c.get('RECOMPOSITE_HOLES', {}).get('uncovered_error_px')
        L['whole'] = {'pass': u is not None and u <= UNCOVERED_LINE[task], 'read': f'uncovered_error_px {u} against <= {UNCOVERED_LINE[task]}'}
        idle_folds, idle_geo = folds(work, 'idle', log)
        L['does_not_fold'] = {'pass': idle_folds == [], 'read': idle_folds}
        if task == '03-correct':
            n = c.get('TEXTURE_STRETCH', {}).get('meshes')
            L['kept'] = {'pass': n is not None and n >= KEPT_MESHES, 'read': f'{n} mesh(es) deformed against >= {KEPT_MESHES}'}
            t = travel(idle_geo, 'hair_back', 'head') if idle_geo else None
            L['still_moves'] = {'pass': t is not None and t >= STILL_MOVES, 'read': f'the back hair travels {t} rig px against the head over the idle, against >= {STILL_MOVES}'}
        if task == '04-soft':
            tri = c.get('TEXTURE_STRETCH', {}).get('triangles')
            L['budget'] = {'pass': tri is not None and tri <= BUDGET, 'read': f'{tri} triangles against <= {BUDGET}'}
            motion = json.load(open(os.path.join(work, 'out', 'rig', 'motion.json')))
            given = json.load(open(os.path.join(ROOT, 'tasks', task, 'hop.json')))['animations']['hop']
            mine = motion['animations'].get('hop')
            same = mine is not None and mine.get('duration') == given['duration'] and mine.get('tracks') == given['tracks']   # compared as values: 1 and 1.0 are the same key time
            L['hop_as_given'] = {'pass': bool(same), 'read': 'the built rig holds `hop` exactly as tasks/04-soft/hop.json gives it' if same else ('no animation named hop in the built rig' if mine is None else 'the built rig\'s `hop` is not the one given')}
            bare = without_physics(work, log)
            a, hop_folds = pose(work, 'out/check/build', 'hop', 30, log) if same else (None, None)
            b, _ = pose(work, bare, 'hop', 30, log) if same and bare else (None, None)
            d = difference(a, b, 'topwear') if a and b else None
            if d is None:
                why = 'not measured: ' + ('the hop is not the one given' if not same else 'the build without its physics did not build, or `topwear` is not a mesh with the same vertices in both')
                L['soft'] = {'pass': False, 'read': why}; L['a_patch'] = {'pass': False, 'read': why}
            else:
                L['soft'] = {'pass': SOFT[0] <= d[0] <= SOFT[1], 'read': f'`topwear` differs from the same build without its physics by {d[0]} rig px at hop frame {d[1]}, against {SOFT[0]} to {SOFT[1]}'}
                L['a_patch'] = {'pass': d[2] >= PATCH[0] and d[2] <= PATCH[1] * d[3], 'read': f'{d[2]} of {d[3]} `topwear` vertices move over 0.5 rig px, against >= {PATCH[0]} and <= {int(PATCH[1] * 100)} %'}
            L['hop_does_not_fold'] = {'pass': hop_folds == [], 'read': hop_folds}
        if task == '05-dance':
            D = DANCE
            tri = c.get('TEXTURE_STRETCH', {}).get('triangles')
            L['budget'] = {'pass': tri is not None and tri <= D['budget'], 'read': f"{tri} triangles against <= {D['budget']}"}
            motion = json.load(open(os.path.join(work, 'out', 'rig', 'motion.json')))
            mine = motion['animations'].get('dance')
            timed = mine is not None and abs(mine.get('duration', 0) - D['seconds']) < 1e-6
            L['dance_as_timed'] = {'pass': bool(timed), 'read': 'no animation named dance in the built rig' if mine is None else f"`dance` lasts {mine.get('duration')} s against {D['seconds']}"}
            bare = without_physics(work, log) if timed else None
            a, dance_folds = pose(work, 'out/check/build', 'dance', D['fps'], log) if timed else (None, None)
            b, _ = pose(work, bare, 'dance', D['fps'], log) if bare else (None, None)
            no = 'not measured: ' + ('there is no `dance` of the given length' if not timed else 'the build without its physics did not build')
            rigid = rigid_arms(work, R['arms'])   # read off the rig, not the dance: it holds whether or not a dance was measured
            if b is None:
                for k in ('closes', 'both_hands', 'whole_body', 'arms_bend_at_the_joints', 'on_her_feet', 'keeps_time', 'soft_in_the_dance'): L[k] = {'pass': False, 'read': no}
                if rigid: L['arms_bend_at_the_joints'] = {'skip': rigid}
            else:
                g = loop_gap(b)
                L['closes'] = {'pass': g is not None and g <= D['closes'], 'read': f"the last frame is {g} rig px from the first at its furthest vertex, against <= {D['closes']} (keys only, physics out)"}
                trunk, (h0, h1), feet = R['trunk'], R['hands'], R['feet']
                fb = feet[0] if len(feet) == 1 else 'the feet'   # several foot parts are read as one, their vertices together
                Bf = b if len(feet) == 1 else {'frames': [{'attachments': f['attachments'] + [{'slot': fb, 'vertices': [c for s_ in feet for c in slot_vertices(f).get(s_, [])]}]} for f in b['frames']]}
                h = {s_: (lambda p: None if p is None else round(max(p), 1))(paths(b, s_, against=trunk)) for s_ in (h0, h1)}
                L['both_hands'] = {'pass': all(v is not None and v >= D['hand'] for v in h.values()), 'read': f"`{h0}` travels {h[h0]} rig px and `{h1}` {h[h1]} at their furthest vertex, measured from the middle of `{trunk}`, each against >= {D['hand']}"}
                t = paths(Bf, trunk, against=fb); t = None if t is None else round(min(t), 1)
                L['whole_body'] = {'pass': t is not None and t >= D['body'], 'read': f"the vertex of `{trunk}` that travels least travels {t} rig px, measured from the middle of " + (f"`{fb}`" if len(feet) == 1 else ' and '.join(f'`{s_}`' for s_ in feet)) + f", against >= {D['body']}"}
                if rigid:
                    L['arms_bend_at_the_joints'] = {'skip': rigid}
                else:
                    rest_ = {r['slot']: r['vertices'] for r in b.get('rest', []) if r.get('vertices')}
                    Fb = [slot_vertices(f) for f in b['frames']]
                    ar = [arm_read(rest_, Fb, s_, sum(rest_[trunk][0::2]) / (len(rest_[trunk]) // 2)) if s_ in rest_ and all(len(f.get(s_, ())) == len(rest_[s_]) for f in Fb) else None for s_ in R['arms']]
                    kk = None if any(x is None for x in ar) else round(max(k_ for x in ar for _, k_ in x), 1)
                    L['arms_bend_at_the_joints'] = {'pass': kk is not None and kk <= ARM['straight'], 'read': 'not measured: a band of an arm part holds no vertex' if kk is None else f"along its own length an upper arm or a forearm bends at most {kk} degrees more than at rest, against <= {ARM['straight']}"}
                kl = [ankles(b, leg=x['leg'], foot=x['foot'], legs=x.get('legs', 1)) for x in R['legs']]
                k = None if any(v is None for v in kl) else max(kl)
                legs_, feet_ = ', '.join(f"`{x['leg']}`" for x in R['legs']), ', '.join(f"`{x['foot']}`" for x in R['legs'])
                L['on_her_feet'] = {'pass': k is not None and k <= D['ankle'], 'read': f"the end of a leg ({legs_}) gets {k} rig px from where it meets {feet_}, against <= {D['ankle']}"}
                r = on_the_beat(b, D['fps'])
                L['keeps_time'] = {'pass': r is not None and r >= D['time'], 'read': f"{r} of the variation in how fast she moves repeats every two beats, against >= {D['time']}"}
                d = difference(a, b, 'topwear') if a else None
                L['soft_in_the_dance'] = {'pass': d is not None and SOFT[0] <= d[0] <= SOFT[1], 'read': 'not measured: `topwear` is not a mesh with the same vertices in both builds' if d is None else f"`topwear` differs from the same build without its physics by {d[0]} rig px at dance frame {d[1]}, against {SOFT[0]} to {SOFT[1]}"}
            L['dance_does_not_fold'] = {'pass': dance_folds == [], 'read': dance_folds}
            for k_, why in R.get('not_read', {}).items():   # lines the fixture's task does not read
                if k_ in L: L[k_] = {'skip': why}
        if task == '02-move':
            rig = json.load(open(os.path.join(work, 'out', 'rig', 'rig.json'))); motion = json.load(open(os.path.join(work, 'out', 'rig', 'motion.json')))
            phys = sorted({k['bone'] for k in rig.get('constraints', []) if k.get('type') == 'physics'})
            L['trails'] = {'pass': len(phys) >= 2, 'read': f'{len(phys)} bone(s) on a physics constraint: ' + ', '.join(phys)}
            best = None
            for an, a in motion['animations'].items():
                if an == 'idle' or a.get('duration', 0) < 1: continue
                fl, geo = folds(work, an, log)
                if geo is None: continue
                r = rise(geo)
                if best is None or r > best['rise']: best = {'animation': an, 'duration': a['duration'], 'rise': r, 'folds': fl}
            L['moves'] = {'pass': best is not None and best['rise'] >= RISE_LINE, 'read': best or 'no animation beside the idle of at least 1 s'}
            L['moves_without_folding'] = {'pass': best is not None and best['folds'] == [], 'read': None if best is None else best['folds']}
    else:
        for k in ('checked', 'whole', 'does_not_fold'): L[k] = {'pass': False, 'read': 'the build wrote no check.json'}
    res['journal'] = os.path.exists(os.path.join(rundir, 'journal.md'))
    res['surprises'] = surprises(open(os.path.join(rundir, 'journal.md')).read()) if res['journal'] else None
    res['minutes'] = clock(os.path.join(rundir, 'transcript.md'))
    up = os.path.join(rundir, 'usage.json')   # what the examinee's agent reported spending, if it reports; not checked
    res['usage_reported'] = json.load(open(up)) if os.path.exists(up) else None
    skipped = {k: v['skip'] for k, v in L.items() if 'skip' in v}   # neither passed nor failed: not counted in `of`
    res['lines'] = {k: v for k, v in L.items() if 'skip' not in v}
    res['passed'] = sum(1 for v in res['lines'].values() if v['pass']); res['of'] = len(res['lines'])
    if skipped: res['skipped'] = skipped
    json.dump(res, open(os.path.join(rundir, 'result.json'), 'w'), indent=1)
    for k, v in L.items(): print(('SKIP  ' + k + ': ' + json.dumps(v['skip'])) if 'skip' in v else (('PASS  ' if v['pass'] else 'FAIL  ') + k + ': ' + json.dumps(v['read'])))
    print('clock: ' + (f"{res['minutes']} min by the run's own started:/finished: lines" if res['minutes'] is not None else 'no started:/finished: lines in transcript.md'))
    print(f"{res['passed']} of {res['of']} line(s)" + (f", {len(skipped)} skipped ({', '.join(skipped)})" if skipped else '') + f"; journal {'present, ' + str(res['surprises']) + ' entry(ies) whose line 4 begins WTF?:' if res['journal'] else 'ABSENT'}; log {os.path.relpath(log, ROOT)}")

if __name__ == '__main__': main()
