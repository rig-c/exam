#!/usr/bin/env python3
"""Grade one run: rebuild from the files it hands in, on the pinned versions, and write result.json.

    python3 grade.py runs/<date>-<model>-<task>

The run directory names its task by its last component (…-01-build, …-04-soft). Nothing the run pasted is
read: the config (and any file it names) is copied beside the task's inputs into .grade/<run>/, built
there, and every line below is read off what that build wrote. Needs npm, bun and python3; installs the
pinned packages into ./node_modules on first use.
"""
import datetime, json, os, re, shutil, statistics, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
BIN = os.path.join(ROOT, 'node_modules', '.bin')
UNCOVERED_LINE = {'01-build': 4200, '02-move': 4200, '03-correct': 3500, '04-soft': 4200, '05-dance': 4200, '06-wiggle': 4200}   # rig px; about twice what the proposed plan leaves (2,059; 1,726)
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

WIGGLE = {'seconds': 4.0, 'fps': 24, 'swings': 4, 'closes': 0.5, 'count': 0.7, 'far': 24.0, 'shoulders': 0.5, 'elbow': (10.0, 60.0),
          'head': 8.0, 'head_in_time': 0.6, 'skirt': (4.0, 0.5), 'ankle': 6.0, 'feet': 2.0, 'budget': 1000}
                        # task 06: 8 beats, the hips out to a side on each — four times each way; the share of the hips' sideways
                        # motion that comes at that count; rig px they travel side to side; the shoulders' travel as a share of
                        # theirs; degrees each forearm is folded in toward the body, more than at rest; degrees the head
                        # tilts and the share of it at the hips' count; rig px the hem swings on physics, at least, and at most as a share of the part's height; the legs at the feet,
                        # the feet on the ground; triangles

def band(rest, lo, hi):
    """Indices of a part's vertices between two fractions of its height at the rest pose, measured from its bottom (y up)."""
    ys = rest[1::2]; a, b = min(ys), max(ys)
    return [i for i, y in enumerate(ys) if a + lo * (b - a) <= y <= a + hi * (b - a)]

def harmonic(x, k):
    """The share of a looped signal's variation carried by its k-th harmonic."""
    import cmath
    n = len(x); m = sum(x) / n
    P = [abs(sum((x[t] - m) * cmath.exp(-2j * cmath.pi * j * t / n) for t in range(n))) ** 2 for j in range(1, n // 2 + 1)]
    return round(P[k - 1] / sum(P), 3) if sum(P) > 1e-9 and k <= len(P) else 0.0

def wiggle_read(geometry):
    """Readings of a hip wiggle off the posed vertices (y up), keys only. A part's bands are taken at the rest pose."""
    rest = {r['slot']: r['vertices'] for r in geometry.get('rest', []) if r.get('vertices')}
    rest = {k: (v if not isinstance(v[0], list) else [c for p in v for c in p]) for k, v in rest.items()}
    F = [slot_vertices(f) for f in geometry['frames']][:-1]; n = len(F)
    need = ('bottomwear', 'topwear', 'handwear_l', 'handwear_r', 'face', 'shoes')
    if n < 8 or any(s not in rest or any(len(f.get(s, ())) != len(rest[s]) for f in F) for s in need): return None
    mx = lambda v, ii: sum(v[2 * i] for i in ii) / len(ii)
    hip, sho = band(rest['bottomwear'], 0.9, 1.0), band(rest['topwear'], 0.9, 1.0)
    hx = [mx(f['bottomwear'], hip) for f in F]; sx = [mx(f['topwear'], sho) for f in F]
    R = {'hips': round(max(hx) - min(hx), 1), 'count': harmonic(hx, WIGGLE['swings']), 'shoulders': round(max(sx) - min(sx), 1)}
    mid = lambda v: sum(v[0::2]) / (len(v) // 2)
    import math
    def bend(v, slot):   # degrees the forearm is turned toward the trunk's middle, from the line of the upper arm
        c = lambda lo, hi: (lambda ii: (sum(v[2 * i] for i in ii) / len(ii), sum(v[2 * i + 1] for i in ii) / len(ii)))(band(rest[slot], lo, hi))
        up, el, wr = c(0.80, 0.95), c(0.58, 0.70), c(0.30, 0.42)
        d = math.degrees(math.atan2(wr[1] - el[1], wr[0] - el[0]) - math.atan2(el[1] - up[1], el[0] - up[0]))
        d = (d + 180) % 360 - 180
        return d if mx(rest[slot], list(range(len(rest[slot]) // 2))) < mid(rest['topwear']) else -d   # image-left arm: counter-clockwise is toward the middle
    R['elbow'] = {}
    for s_ in ('handwear_l', 'handwear_r'):
        b0 = bend(rest[s_], s_); bs = [bend(f[s_], s_) - b0 for f in F]
        R['elbow'][s_] = (round(min(bs), 1), round(max(bs), 1))
    ang = [math.degrees(math.atan2(f['face'][5] - f['face'][3], f['face'][4] - f['face'][2])) for f in F]   # one edge of the face's quad
    R['head'] = round(max(ang) - min(ang), 2); R['head_in_time'] = harmonic(ang, WIGGLE['swings'])
    sh = F[0]['shoes']
    R['feet'] = round(max(max(abs(f['shoes'][i] - sh[i]) for i in range(len(sh))) for f in F), 2)
    return R

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

def ankles(geometry, leg='legwear', foot='shoes', band_=0.04):
    """How far the end of each leg gets from its foot. The leg part's vertices in the lowest 4 % of its height at the
    first frame are split into two legs at the widest gap in x; each leg's end is the middle of its vertices there, and
    it is held against the foot-part vertex nearest it in the first frame. The largest change in that offset over the
    frames — the middle, so that an ankle turning over a planted foot is not read as a leg leaving it."""
    F = [slot_vertices(f) for f in geometry['frames']]; a0, b0 = F[0].get(leg), F[0].get(foot)
    if a0 is None or b0 is None: return None
    P = [(a0[i], a0[i + 1]) for i in range(0, len(a0), 2)]; Q = [(b0[i], b0[i + 1]) for i in range(0, len(b0), 2)]
    lo, hi = min(p[1] for p in P), max(p[1] for p in P); cut = lo + band_ * (hi - lo)   # y up: the lowest band
    low = sorted((i for i, p in enumerate(P) if p[1] <= cut), key=lambda i: P[i][0])
    if not low: return None
    gap = max(range(1, len(low)), key=lambda k: P[low[k]][0] - P[low[k - 1]][0]) if len(low) > 1 else 0
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

def main():
    rundir = os.path.abspath(sys.argv[1]); name = os.path.basename(rundir.rstrip('/'))
    task = next((t for t in sorted(os.listdir(os.path.join(ROOT, 'tasks'))) if name.endswith(t)), None)
    if task is None: sys.exit(f'{name}: the run directory must end with a task name, one of ' + ', '.join(sorted(os.listdir(os.path.join(ROOT, "tasks")))))
    if not os.path.isdir(BIN) and subprocess.run(['npm', 'ci'], cwd=ROOT).returncode != 0: sys.exit('npm ci failed')
    work = os.path.join(ROOT, '.grade', name); shutil.rmtree(work, ignore_errors=True); os.makedirs(work)
    log = os.path.join(work, 'grade.log')
    for f in os.listdir(rundir):
        if f.endswith('.json') and f not in ('result.json', 'usage.json'): shutil.copy(os.path.join(rundir, f), work)
    own = os.path.join(ROOT, 'tasks', task, 'inputs')   # a task without a painting of its own is set on task 01's
    os.symlink(own if os.path.exists(os.path.join(own, 'painting.png')) else os.path.join(ROOT, 'tasks', '01-build', 'inputs'), os.path.join(work, 'inputs'))
    versions = {p: json.load(open(os.path.join(ROOT, 'node_modules', p, 'package.json')))['version'] for p in ('@rig-c/parts', 'rig-c')}
    res = {'run': name, 'task': task, 'versions': versions, 'lines': {}}
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
            if b is None:
                for k in ('closes', 'both_hands', 'whole_body', 'on_her_feet', 'keeps_time', 'soft_in_the_dance'): L[k] = {'pass': False, 'read': no}
            else:
                g = loop_gap(b)
                L['closes'] = {'pass': g is not None and g <= D['closes'], 'read': f"the last frame is {g} rig px from the first at its furthest vertex, against <= {D['closes']} (keys only, physics out)"}
                h = {s_: (lambda p: None if p is None else round(max(p), 1))(paths(b, s_, against='topwear')) for s_ in ('handwear_l', 'handwear_r')}
                L['both_hands'] = {'pass': all(v is not None and v >= D['hand'] for v in h.values()), 'read': f"`handwear_l` travels {h['handwear_l']} rig px and `handwear_r` {h['handwear_r']} at their furthest vertex, measured from the middle of `topwear`, each against >= {D['hand']}"}
                t = paths(b, 'topwear', against='shoes'); t = None if t is None else round(min(t), 1)
                L['whole_body'] = {'pass': t is not None and t >= D['body'], 'read': f"the vertex of `topwear` that travels least travels {t} rig px, measured from the middle of `shoes`, against >= {D['body']}"}
                k = ankles(b)
                L['on_her_feet'] = {'pass': k is not None and k <= D['ankle'], 'read': f"the end of a leg (`legwear`) gets {k} rig px from where it meets `shoes`, against <= {D['ankle']}"}
                r = on_the_beat(b, D['fps'])
                L['keeps_time'] = {'pass': r is not None and r >= D['time'], 'read': f"{r} of the variation in how fast she moves repeats every two beats, against >= {D['time']}"}
                d = difference(a, b, 'topwear') if a else None
                L['soft_in_the_dance'] = {'pass': d is not None and SOFT[0] <= d[0] <= SOFT[1], 'read': 'not measured: `topwear` is not a mesh with the same vertices in both builds' if d is None else f"`topwear` differs from the same build without its physics by {d[0]} rig px at dance frame {d[1]}, against {SOFT[0]} to {SOFT[1]}"}
            L['dance_does_not_fold'] = {'pass': dance_folds == [], 'read': dance_folds}
        if task == '06-wiggle':
            W = WIGGLE
            tri = c.get('TEXTURE_STRETCH', {}).get('triangles')
            L['budget'] = {'pass': tri is not None and tri <= W['budget'], 'read': f"{tri} triangles against <= {W['budget']}"}
            motion = json.load(open(os.path.join(work, 'out', 'rig', 'motion.json')))
            mine = motion['animations'].get('wiggle')
            timed = mine is not None and abs(mine.get('duration', 0) - W['seconds']) < 1e-6
            L['wiggle_as_timed'] = {'pass': bool(timed), 'read': 'no animation named wiggle in the built rig' if mine is None else f"`wiggle` lasts {mine.get('duration')} s against {W['seconds']}"}
            bare = without_physics(work, log) if timed else None
            a, wig_folds = pose(work, 'out/check/build', 'wiggle', W['fps'], log) if timed else (None, None)
            b, _ = pose(work, bare, 'wiggle', W['fps'], log) if bare else (None, None)
            g = wiggle_read(b) if b else None
            no = 'not measured: ' + ('there is no `wiggle` of the given length' if not timed else 'the build without its physics did not build' if b is None else '`bottomwear`, `topwear`, `handwear_l`, `handwear_r`, `face` and `shoes` are not all there with vertices that keep their count')
            if g is None:
                for k in ('closes', 'four_each_way', 'hips_go_far', 'hips_not_shoulders', 'elbows_in', 'head_sways', 'skirt_swings', 'on_her_feet'): L[k] = {'pass': False, 'read': no}
            else:
                gp = loop_gap(b)
                L['closes'] = {'pass': gp is not None and gp <= W['closes'], 'read': f"the last frame is {gp} rig px from the first at its furthest vertex, against <= {W['closes']} (keys only, physics out)"}
                L['four_each_way'] = {'pass': g['count'] >= W['count'], 'read': f"{g['count']} of the hips' sideways motion comes {W['swings']} times a loop, against >= {W['count']}"}
                L['hips_go_far'] = {'pass': g['hips'] >= W['far'], 'read': f"the top of `bottomwear` travels {g['hips']} rig px side to side, against >= {W['far']}"}
                L['hips_not_shoulders'] = {'pass': g['hips'] > 0 and g['shoulders'] <= W['shoulders'] * g['hips'], 'read': f"the top of `topwear` travels {g['shoulders']} rig px side to side, against <= {W['shoulders']} of the hips' {g['hips']}"}
                lo_, hi_ = min(v[0] for v in g['elbow'].values()), max(v[1] for v in g['elbow'].values())
                L['elbows_in'] = {'pass': lo_ >= W['elbow'][0] and hi_ <= W['elbow'][1], 'read': f"through the loop each forearm is folded in toward the body by {lo_} to {hi_} degrees more than at rest, against {W['elbow'][0]} to {W['elbow'][1]}"}
                L['head_sways'] = {'pass': g['head'] >= W['head'] and g['head_in_time'] >= W['head_in_time'], 'read': f"`face` tilts through {g['head']} degrees, against >= {W['head']}, and {g['head_in_time']} of that comes at the hips' count, against >= {W['head_in_time']}"}
                hem = band({r['slot']: r['vertices'] for r in b.get('rest', []) if r.get('vertices')}['bottomwear'], 0.0, 0.1) if a else []
                d = None
                if a:
                    d = 0.0
                    for fa, fb in zip(a['frames'], b['frames']):
                        x, y = slot_vertices(fa).get('bottomwear'), slot_vertices(fb).get('bottomwear')
                        if x is None or y is None or len(x) != len(y): d = None; break
                        d = max([d] + [((x[2 * i] - y[2 * i]) ** 2 + (x[2 * i + 1] - y[2 * i + 1]) ** 2) ** 0.5 for i in hem])
                ys = {r['slot']: r['vertices'] for r in b.get('rest', []) if r.get('vertices')}['bottomwear'][1::2]; most = round(W['skirt'][1] * (max(ys) - min(ys)), 1)
                L['skirt_swings'] = {'pass': d is not None and W['skirt'][0] <= d <= most, 'read': 'not measured: `bottomwear` is not a mesh with the same vertices in both builds' if d is None else f"the hem of `bottomwear` differs from the same build without its physics by {round(d, 2)} rig px at its furthest vertex, against {W['skirt'][0]} to {most} (half the part's height)"}
                k = ankles(b)
                L['on_her_feet'] = {'pass': k is not None and k <= W['ankle'] and g['feet'] <= W['feet'], 'read': f"the end of a leg (`legwear`) gets {k} rig px from where it meets `shoes`, against <= {W['ankle']}; `shoes` moves {g['feet']} rig px, against <= {W['feet']}"}
            L['wiggle_does_not_fold'] = {'pass': wig_folds == [], 'read': wig_folds}
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
    # an entry's fourth line that begins with WTF?: (SURPRISE: in the form before 2026-10-13), as the form asks —
    # not the word wherever it appears
    res['surprises'] = len(re.findall(r'^4\.\s*\*\*Happened:\*\*\s*(?:WTF\?:|SURPRISE:)', open(os.path.join(rundir, 'journal.md')).read(), re.M)) if res['journal'] else None
    res['minutes'] = clock(os.path.join(rundir, 'transcript.md'))
    up = os.path.join(rundir, 'usage.json')   # what the examinee's agent reported spending, if it reports; not checked
    res['usage_reported'] = json.load(open(up)) if os.path.exists(up) else None
    res['passed'] = sum(1 for v in L.values() if v['pass']); res['of'] = len(L)
    json.dump(res, open(os.path.join(rundir, 'result.json'), 'w'), indent=1)
    for k, v in L.items(): print(('PASS  ' if v['pass'] else 'FAIL  ') + k + ': ' + json.dumps(v['read']))
    print('clock: ' + (f"{res['minutes']} min by the run's own started:/finished: lines" if res['minutes'] is not None else 'no started:/finished: lines in transcript.md'))
    print(f"{res['passed']} of {res['of']} line(s); journal {'present, ' + str(res['surprises']) + ' entry(ies) whose line 4 begins WTF?:' if res['journal'] else 'ABSENT'}; log {os.path.relpath(log, ROOT)}")

if __name__ == '__main__': main()
