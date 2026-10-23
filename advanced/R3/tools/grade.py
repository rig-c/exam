#!/usr/bin/env python3
"""Grade an Advanced R1 (walk), R2 (run) or R3 (dance) attempt against its PROBLEM.md pass table.

usage:
  python3 grade.py --round R1|R2|R3 --geometry <geometry.json> --sequence <sequence.json>
                   --report <report.json> --build <build stdout> --cycle <frames>
                   [--folds <folds.json>] [--passthrough <pass-through.json or render stdout>]
                   [--map <map.json>] [--camera <camera.json>]
                   [--feet <left>,<right>] [--hip <bone>] [--trunk <bone>,<bone>,...]
                   [--jumps a-b,c-d] [--person <id>] [--airborne <airborne.json>]

Inputs, and where each comes from:
  --geometry     `rigc render --geometry`: geometry.json of the animation being graded
  --sequence     the round's inputs/pose/sequence.json (rig-pose-sequence/1)
  --report       `rig-pose retarget --report`: report.json (rig-pose-report/1)
  --build        the stdout of the final `rigc build` (not the retarget's stdout) — the gate line
  --folds        `rigc render --folds`: folds.json. The JSON, not the printed lines: a mesh that
                 never folds prints no line, so the text cannot tell "read, clean" from "not read".
  --passthrough  `rigc render --pass-through <cloth>:<leg>`: pass-through.json, or the render's stdout
  --map          the map the retarget read. It must be the file the report's `inputs.map` names by
                 sha256; without the flag the report's own `inputs.map.path` is tried (relative to the
                 working directory, then to the report's directory). The jitter row reads its joint
                 pairs from it.
  --camera       R3: `retarget --camera`'s camera.json. A submission check printed as a NOTE, not a row.
  --cycle        frames per cycle of the sequence (R1: 32, R2: 20)
  --feet         the foot bones the map puts the sequence's l_ankle and r_ankle on, in that order
                 (the subject's left first). Default foot_l,foot_r
  --hip          the bone the map translates, the legs hang from it. Default hip
  --trunk        the trunk and head bones, held to the trunk bar of the jitter row; every other
                 bone the retarget keys is held to the limb bar
  --jumps        override for the airborne spans (pose frames, inclusive); by default they are the
                 report's feet.jumps. A run that uses it says so.
  --airborne     R2: the airborne spans the proctor read from the source video for one cycle, the
                 round's inputs/pose/airborne.json; by default the airborne.json beside --sequence.
                 A span outside --cycle, or a file read for another cycle, refuses the row by name.

Prints one line per row of the round's table — R1: 10 rows, R2: R1's 10 and R2's 5, R3: 14 — each
PASS, FAIL or SKIP with its figure and its bar, then a RESULT line. A row whose input is absent
prints SKIP naming what is missing; it never passes on nothing. Exit 0 = every row PASS, 1 = a row
FAILs, 2 = no FAIL but a row could not be measured (SKIP), or the command line is malformed.

Units. A leg length is the rig's setup-pose distance from each thigh root to its foot bone, the
mean of the two sides (the thigh root is the child of --hip on the path down to the foot), read
from geometry.json's `setup.bones`. The sequence's leg length is each side's 95th-percentile
picture distance hip -> ankle over the frames (its straight length), the mean of the two sides:
the rig's leg length is a straight leg, so the sequence's is too. A hip width is the setup
distance between the two thigh roots (rig) and the median picture distance l_hip -> r_hip
(sequence). Sequence distances are read from the joints as the sequence carries them; where the
sequence has a camera track its joints are already normalised (p' = (p - t) / s), so nothing is
divided by camera.s again. The pelvis rows read the rig's thigh roots' midpoint against the
sequence's mid_hip (the midpoint of l_hip and r_hip). Per-frame figures are per frame of the
sequence; the geometry has to be rendered at the sequence's rate for any row that reads both side
by side.
"""
import argparse
import hashlib
import json
import math
import os
import re
import statistics
import sys

# The bars, as the PROBLEM tables state them.
BAR_FLOOR_BAND = 0.01      # support foot: lower foot = floor +/- 0.01 leg lengths
BAR_TWO_FEET = 0.02        # two feet: height difference <= 0.02 leg lengths on two-foot frames
LIFT_FLOOR = 2 * BAR_TWO_FEET  # a lifted frame: the sequence's ankles differ by more than twice the two-foot band
BAR_LIFT_RATIO = (0.85, 1.15)  # two feet: median rig lift / sequence lift on lifted frames (the hip-width band)
BAR_SHIN_SCALE = 0.4       # shin scale: 5th percentile of the shins' rendered x-scale over all frames and both shins >= 0.4
SHIN_BONES = ('leg_r1', 'leg_l1')  # the shin bones the shin-scale row reads
BAR_SLIDE = 0.005          # slide: support foot horizontal move <= 0.005 leg lengths per frame
BAR_JITTER_RATIO = 1.1     # jitter: mean |2nd difference| of rotation ÷ sequence's <= 1.1 (limbs, trunk+head)
BAR_LOOP = 1.0             # loop: first vs last cycle, degrees
BAR_LOOP_POS = 0.01        # loop: first vs last cycle, --hip and foot world position, leg lengths (the support-foot band)
BAR_HIP_RATIO = (0.85, 1.15)  # hip vertical and horizontal width, against the sequence
BAR_REBOUND = (0.7, 1 / 0.7)  # rebound ratio, two-sided: 0.7 .. 1/0.7 (about 1.43)
BAR_TILT = 0.85            # hip tilt range, share of the sequence's
BAR_JUMP_SPANS_R3 = 3      # R3 (dance): exact number of airborne jump spans in the sequence
BAR_AIR_MATCH = 1          # R2: each detected airborne span within the printed span +/- 1 frame
# R2: the airborne spans the proctor read from the source video before the exam are not in this
# file. They are the round's package file inputs/pose/airborne.json (the one beside --sequence;
# --airborne names another), with the cycle they were read for, and the row is refused by name when
# a span lies outside --cycle (exam#11). R2_AIR_REFERENCE stays None; an in-process caller may set
# it to one cycle's spans in place of the file, and they are held to --cycle the same way.
R2_AIR_REFERENCE = None

GEOMETRY_SPEC = 'rigc-geometry/1'
REPORT_SPEC = 'rig-pose-report/1'
SEQUENCE_SPECS = ('rig-pose-sequence/1', 'rig-c-pose-frames/0')
FOLDS_SPEC = 'rigc-folds/1'
PASS_SPEC = 'rigc-pass-through/1'
CAMERA_SPEC = 'rig-pose-camera/1'
MAP_SPEC = 'rig-pose-map/1'


# --- shared with the other edition's grader (exam#11) ---
# Every edition's tools/grade.py carries this block byte for byte; advanced/tools/test_shared.py
# extracts it from each grader and checks it. Change it in every grader at once, or not at all.
import json as _shared_json


def meets(value, op, bar):
    """True when value op bar. op is '<=', '<', '>=', '>', or 'in' with bar = (lo, hi), both ends
    included. Every measured real figure is held to its bar here and nowhere else. The comparison is
    exact, as the PROBLEM tables state the bars: exam#11 measured no tolerance that covers a float
    render error at a bar without also passing a boundary control. A value that prints as its bar
    shows its full precision instead (shown). Integer counts and empty-list conditions do not come here."""
    if op == 'in':
        lo, hi = bar
        return lo <= value <= hi
    if op == '<=':
        return value <= bar
    if op == '<':
        return value < bar
    if op == '>=':
        return value >= bar
    if op == '>':
        return value > bar
    raise ValueError(f'meets: op {op!r} is not <=, <, >=, > or in')


def shown(value, spec, bars):
    """value formatted with spec (as the row prints it). When that text is the text of one of the
    row's bars at the same spec, the value lies within the printed rounding of the bar, and the
    value the comparison saw follows in full: 0.400 (0.3999993). Otherwise the text alone."""
    text = format(value, spec)
    if any(text == format(b, spec) for b in bars):
        return f'{text} ({float(value)!r})'
    return text


AIRBORNE_SPEC = 'advanced-airborne-reference/1'


def spans_outside(spans, cycle, source):
    """None when every span (a, b) lies in one cycle of `cycle` frames (0 <= a <= b < cycle);
    otherwise the refusal, naming the source and the first span that does not."""
    if not (isinstance(cycle, int) and cycle > 0):
        return f'{source}: the spans are cycle-relative and --cycle is {cycle!r}'
    for a, b in spans:
        if not (0 <= a <= b < cycle):
            return f'{source}: span {a}-{b} lies outside the declared --cycle {cycle} (cycle frames 0-{cycle - 1})'
    return None


def airborne_reference(path, cycle):
    """(spans, None) or (None, refusal). The round's airborne spans for one cycle, as the file at
    path holds them ({spec, cycle, spans: [[a, b], ...]}, pose frames, both ends included). Refused
    by name when a span lies outside --cycle or the file was read for another cycle."""
    try:
        with open(path, encoding='utf-8') as fh:
            doc = _shared_json.load(fh)
    except OSError:
        return None, f'{path} is not on disk: the airborne spans are the round\'s package file inputs/pose/airborne.json'
    except ValueError as e:
        return None, f'{path} is not JSON ({e})'
    if not isinstance(doc, dict) or doc.get('spec') != AIRBORNE_SPEC:
        return None, f'{path}: spec is not {AIRBORNE_SPEC}'
    raw, declared = doc.get('spans'), doc.get('cycle')
    if (not isinstance(raw, list) or not raw
            or not all(isinstance(s, list) and len(s) == 2 and all(type(v) is int for v in s) for s in raw)):
        return None, f'{path}: spans is not a list of [first, last] pose frames'
    spans = [tuple(s) for s in raw]
    why = spans_outside(spans, cycle, path)
    if why:
        return None, why
    if declared != cycle:
        return None, f'{path}: the spans were read for a {declared!r}-frame cycle, --cycle is {cycle}'
    return spans, None
# --- end shared ---


class Skip(Exception):
    """A row that cannot be measured: the reason names the missing input or the missing data."""


def wrap(deg):
    return (deg + 180.0) % 360.0 - 180.0


def median(xs):
    return statistics.median(xs)


def percentile(xs, q):
    """Linear interpolation between closest ranks."""
    v = sorted(xs)
    k = (len(v) - 1) * q
    lo = math.floor(k)
    hi = min(lo + 1, len(v) - 1)
    return v[lo] + (v[hi] - v[lo]) * (k - lo)


# ---------------------------------------------------------------- inputs

def load_json(path, flag):
    """(document, None) or (None, reason)."""
    if path is None:
        return None, f'{flag} not given'
    if not os.path.isfile(path):
        return None, f'{flag} {path} is not on disk'
    try:
        with open(path, encoding='utf-8') as fh:
            return json.load(fh), None
    except (ValueError, OSError) as e:
        return None, f'{flag} {path} is not JSON ({e})'


def load_text(path, flag):
    if path is None:
        return None, f'{flag} not given'
    if not os.path.isfile(path):
        return None, f'{flag} {path} is not on disk'
    with open(path, encoding='utf-8', errors='replace') as fh:
        return fh.read(), None


class Geometry:
    def __init__(self, doc, path):
        if not isinstance(doc, dict) or doc.get('spec') != GEOMETRY_SPEC:
            raise ValueError(f'{path}: spec is {doc.get("spec") if isinstance(doc, dict) else type(doc).__name__!r}, not {GEOMETRY_SPEC}')
        self.path = path
        self.animation = doc.get('animation')
        self.fps = float(doc['fps'])
        self.parent = {b['name']: b['parent'] for b in doc['bones']}
        # The setup pose's bones. `rest` is NOT a bone list: it is every attachment's rest
        # geometry ({slot, attachment, kind, vertices, triangles}); the bones are in `setup.bones`.
        setup = doc.get('setup')
        if not isinstance(setup, dict) or not isinstance(setup.get('bones'), list):
            raise ValueError(f'{path}: no setup.bones — the setup pose is read from there')
        self.setup = {b['name']: b for b in setup['bones']}
        self.frames = [{b['name']: b for b in f['bones']} for f in doc['frames']]
        self.times = [float(f['time']) for f in doc['frames']]

    def has(self, name):
        return name in self.parent


class Sequence:
    def __init__(self, doc, path, person):
        if not isinstance(doc, dict) or doc.get('spec') not in SEQUENCE_SPECS:
            raise ValueError(f'{path}: spec is {doc.get("spec") if isinstance(doc, dict) else "?"}, not rig-pose-sequence/1')
        self.path = path
        self.frames = doc['frames']
        self.times = [float(f['t']) for f in self.frames]
        self.has_camera = 'camera' in doc
        self.camera = doc.get('camera')
        self.in_place = doc.get('travel') == 'in-place'
        self.measured_hips = bool(((doc.get('cleaned') or {}).get('params') or {}).get('hipsInferred', {}).get('by') == 'measured')
        dts = [b - a for a, b in zip(self.times, self.times[1:])]
        self.fps = 1.0 / median(dts) if dts else None
        self.person = person

    def joint(self, i, name, allow_inferred=True):
        if name == 'mid_hip':
            l, r = self.joint(i, 'l_hip', allow_inferred), self.joint(i, 'r_hip', allow_inferred)
            return [(l[0] + r[0]) / 2, (l[1] + r[1]) / 2] if l and r else None
        if name == 'mid_shoulder':
            l, r = self.joint(i, 'l_shoulder', allow_inferred), self.joint(i, 'r_shoulder', allow_inferred)
            return [(l[0] + r[0]) / 2, (l[1] + r[1]) / 2] if l and r else None
        people = self.frames[i].get('people') or []
        p = None
        if self.person is None:
            p = people[0] if people else None
        else:
            p = next((q for q in people if q.get('id') == self.person), None)
        if p is None:
            return None
        j = (p.get('joints') or {}).get(name)
        if not j or 'at' not in j or j.get('state') in ('missing',):
            return None
        if not allow_inferred and j.get('state') == 'inferred':
            return None
        return j['at']


class Ctx:
    pass


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b''):
            h.update(chunk)
    return h.hexdigest()


def load_map(a, rep, rep_why):
    """(map, None) or (None, reason). The map is the file the report's inputs.map names by sha256."""
    if rep is None:
        return None, f'the map is the one the report names: {rep_why}'
    ref = (rep.get('inputs') or {}).get('map') if isinstance(rep.get('inputs'), dict) else None
    if not isinstance(ref, dict) or not ref.get('sha256'):
        return None, '--report has no inputs.map.sha256 (rig-pose 0.30 or later writes it)'
    tried = []
    if a.map is not None:
        tried.append(a.map)
    elif ref.get('path'):
        tried.append(ref['path'])
        if a.report:
            tried.append(os.path.join(os.path.dirname(os.path.abspath(a.report)), ref['path']))
    found = next((p for p in tried if os.path.isfile(p)), None)
    if found is None:
        return None, f'--map not given and the report\'s inputs.map.path {ref.get("path")!r} is not on disk' if a.map is None else f'--map {a.map} is not on disk'
    digest = sha256_of(found)
    if digest != ref['sha256']:
        return None, f'--map {found}: sha256 {digest[:12]}… is not the report\'s inputs.map {ref["sha256"][:12]}…'
    doc, why = load_json(found, '--map')
    if doc is None:
        return None, why
    if not isinstance(doc, dict) or doc.get('spec') != MAP_SPEC or not isinstance(doc.get('chains'), list):
        return None, f'--map {found}: spec is not {MAP_SPEC}'
    return doc, None


def camera_submission(path, seq, rep):
    """R3's after/camera.json: present, rig-pose-camera/1, one entry per sequence frame, each t the report's frameTimes."""
    if path is None:
        return 'camera submission: --camera not given (R3 asks for after/camera.json; a submission check, not a row)'
    doc, why = load_json(path, '--camera')
    if doc is None:
        return f'camera submission: MISSING — {why}'
    if not isinstance(doc, dict) or doc.get('spec') != CAMERA_SPEC or not isinstance(doc.get('frames'), list):
        return f'camera submission: WRONG — --camera {path}: spec is not {CAMERA_SPEC}'
    n = len(doc['frames'])
    if seq is not None and n != len(seq.frames):
        return f'camera submission: WRONG — {n} entries, the sequence has {len(seq.frames)} frames'
    times = (rep or {}).get('frameTimes')
    if isinstance(times, list) and len(times) == n:
        off = max(abs(float(f.get('t', 0.0)) - float(t)) for f, t in zip(doc['frames'], times))
        if off > 1e-3:
            return f'camera submission: WRONG — an entry\'s t is {off:.4f} s from the report\'s frameTimes'
        return f'camera submission: present, {CAMERA_SPEC}, {n} entries, t = report frameTimes (max difference {off:.6f} s)'
    return f'camera submission: present, {CAMERA_SPEC}, {n} entries (the report carries no frameTimes to hold t against)'


def build_ctx(a):
    c = Ctx()
    c.args = a
    c.notes = []
    c.round = a.round
    c.cycle = a.cycle

    g, why = load_json(a.geometry, '--geometry')
    c.geo, c.geo_why = None, why
    if g is not None:
        try:
            c.geo = Geometry(g, a.geometry)
        except (ValueError, KeyError, TypeError) as e:
            c.geo_why = f'--geometry {a.geometry}: {e}'

    s, why = load_json(a.sequence, '--sequence')
    c.seq, c.seq_why = None, why
    if s is not None:
        try:
            c.seq = Sequence(s, a.sequence, a.person)
        except (ValueError, KeyError, TypeError) as e:
            c.seq_why = f'--sequence {a.sequence}: {e}'

    r, why = load_json(a.report, '--report')
    c.rep, c.rep_why = None, why
    if r is not None:
        if not isinstance(r, dict) or r.get('spec') != REPORT_SPEC:
            c.rep_why = f'--report {a.report}: spec is not {REPORT_SPEC}'
        else:
            c.rep = r

    c.build, c.build_why = load_text(a.build, '--build')
    c.folds, c.folds_why = load_json(a.folds, '--folds')
    c.pt_text, c.pt_why = load_text(a.passthrough, '--passthrough')

    # R3's camera.json is a submission, not a row: retarget writes videoS = s * sequence.camera.s
    # itself, so a residual against the sequence measures nothing a candidate can move.
    if a.round == 'R3':
        c.notes.append(camera_submission(a.camera, c.seq, r if isinstance(r, dict) else None))

    c.map, c.map_why = load_map(a, c.rep, c.rep_why)

    feet = [x.strip() for x in a.feet.split(',')]
    c.feet_why = None
    if len(feet) != 2 or not all(feet):
        c.feet_why = f'--feet {a.feet!r} is not <left>,<right>'
        feet = [None, None]
    c.foot_l, c.foot_r = feet
    c.hip = a.hip
    c.trunk = [x.strip() for x in a.trunk.split(',') if x.strip()] if a.trunk else None

    # Report against sequence: the report's frame indices are the sequence's.
    if c.rep is not None and c.seq is not None and c.rep.get('frames') is not None and c.rep['frames'] != len(c.seq.frames):
        c.rep_frames_why = f'--report is for {c.rep["frames"]} frames, --sequence has {len(c.seq.frames)}'
    else:
        c.rep_frames_why = None

    # Pose-frame times: the sequence's, else the report's frames over its duration.
    c.pose_times, c.pose_fps = None, None
    if c.seq is not None:
        t0 = c.seq.times[0]
        c.pose_times = [t - t0 for t in c.seq.times]
        c.pose_fps = c.seq.fps
    elif c.rep is not None and c.rep.get('frames') and c.rep.get('duration'):
        n = int(c.rep['frames'])
        c.pose_fps = (n - 1) / float(c.rep['duration'])
        c.pose_times = [i / c.pose_fps for i in range(n)]
        c.notes.append(f'pose frame times from --report ({n} frames over {c.rep["duration"]} s): no --sequence')

    # Airborne spans.
    c.jumps, c.jumps_why = None, None
    if a.jumps is not None:
        try:
            c.jumps = [tuple(int(v) for v in s.split('-')) for s in a.jumps.split(',') if s.strip()]
            if any(len(j) != 2 or j[0] > j[1] for j in c.jumps):
                raise ValueError
        except ValueError:
            c.jumps, c.jumps_why = None, f'--jumps {a.jumps!r} is not a-b[,c-d...]'
        else:
            c.notes.append(f'airborne spans: --jumps OVERRIDE used ({a.jumps}); the report\'s feet.jumps were not read')
    elif c.rep is None:
        c.jumps_why = f'airborne spans are the report\'s feet.jumps: {c.rep_why}'
    elif c.rep_frames_why:
        c.jumps_why = c.rep_frames_why
    else:
        feet_rep = c.rep.get('feet')
        if not isinstance(feet_rep, dict) or not isinstance(feet_rep.get('jumps'), list):
            c.jumps_why = '--report has no feet.jumps (the map does not name both legs)'
        else:
            c.jumps = [tuple(j) for j in feet_rep['jumps']]
            c.notes.append(f'airborne spans: report feet.jumps, {len(c.jumps)} span(s)')
    c.air = set()
    if c.jumps:
        for x, y in c.jumps:
            c.air.update(range(x, y + 1))

    derive_rig(c)
    derive_alignment(c)
    derive_seq_units(c)
    return c


def derive_rig(c):
    """Thigh roots, leg length and hip width from the setup pose."""
    c.rig_why = None
    c.root_l = c.root_r = None
    c.L = c.hip_width = None
    if c.geo is None:
        c.rig_why = c.geo_why
        return
    if c.feet_why:
        c.rig_why = c.feet_why
        return
    g = c.geo
    for name, flag in ((c.foot_l, '--feet'), (c.foot_r, '--feet'), (c.hip, '--hip')):
        if not g.has(name):
            c.rig_why = f'{flag}: bone {name!r} is not in {g.path}'
            return

    def root_of(foot):
        b = foot
        while g.parent.get(b) is not None:
            if g.parent[b] == c.hip:
                return b
            b = g.parent[b]
        return None

    c.root_l, c.root_r = root_of(c.foot_l), root_of(c.foot_r)
    if c.root_l is None or c.root_r is None:
        c.rig_why = f'--hip {c.hip!r} is not an ancestor of both feet, so no thigh root is found'
        return
    s = g.setup

    def dist(p, q):
        return math.hypot(s[p]['worldX'] - s[q]['worldX'], s[p]['worldY'] - s[q]['worldY'])

    c.L = (dist(c.root_l, c.foot_l) + dist(c.root_r, c.foot_r)) / 2
    c.hip_width = dist(c.root_l, c.root_r)
    if c.L <= 0:
        c.rig_why = 'the setup pose\'s leg length is 0'
        c.L = None
    c.notes.append(f'rig leg length {c.L:.4f} units (setup pose, {c.root_l}->{c.foot_l}, {c.root_r}->{c.foot_r}); hip width {c.hip_width:.4f}')


def derive_alignment(c):
    """c.N pose frames aligned one to one with geometry frames, or c.align_why."""
    c.N, c.align_why = None, None
    if c.geo is None:
        c.align_why = c.geo_why
        return
    if c.pose_times is None:
        c.align_why = f'pose frame times need --sequence ({c.seq_why})'
        return
    if abs(c.geo.fps - c.pose_fps) > 1e-3 * c.pose_fps:
        c.align_why = f'geometry is at {c.geo.fps:g} fps, the sequence at {c.pose_fps:.4g}: render with --fps {round(c.pose_fps)}'
        return
    n = min(len(c.geo.times), len(c.pose_times))
    half = 0.5 / c.pose_fps
    for i in range(n):
        if abs(c.geo.times[i] - c.pose_times[i]) > half:
            c.align_why = f'geometry frame {i} is at t={c.geo.times[i]:.4f}s, pose frame {i} at {c.pose_times[i]:.4f}s'
            return
    c.N = n
    if len(c.geo.times) != len(c.pose_times):
        c.notes.append(f'geometry has {len(c.geo.times)} frames, the pose {len(c.pose_times)}: rows read the first {n}')


def derive_seq_units(c):
    """Ls and the hip width, from the joints as the sequence carries them (normalised already when it has a camera)."""
    c.Ls = c.seq_hip_width = None
    c.seq_units_why = None
    if c.seq is None:
        c.seq_units_why = c.seq_why
        return
    q = c.seq
    sides = []
    for hip, ankle in (('l_hip', 'l_ankle'), ('r_hip', 'r_ankle')):
        ds = []
        for i in range(len(q.frames)):
            p, a = q.joint(i, hip), q.joint(i, ankle)
            if p and a:
                ds.append(math.hypot(p[0] - a[0], p[1] - a[1]))
        if not ds:
            c.seq_units_why = f'the sequence never has both {hip} and {ankle}'
            return
        sides.append(percentile(ds, 0.95))
    c.Ls = sum(sides) / 2
    ws = []
    for i in range(len(q.frames)):
        l, r = q.joint(i, 'l_hip'), q.joint(i, 'r_hip')
        if l and r:
            ws.append(math.hypot(l[0] - r[0], l[1] - r[1]))
    c.seq_hip_width = median(ws) if ws else None
    c.notes.append(f'sequence leg length {c.Ls:.2f} (95th percentile hip->ankle, mean of sides, the sequence\'s own units)'
                   + ('; the sequence\'s joints are camera-normalised, not divided by camera.s again' if q.has_camera else '; the sequence carries no camera'))


# ---------------------------------------------------------------- shared readings

def need(cond, why):
    if not cond:
        raise Skip(why)


def need_rig(c):
    need(c.L is not None, c.rig_why)


def need_aligned(c):
    need(c.N is not None, c.align_why)


def need_air(c):
    need(c.jumps is not None, c.jumps_why)


def foot_y(c, i, foot):
    return c.geo.frames[i][foot]['worldY']


def foot_x(c, i, foot):
    return c.geo.frames[i][foot]['worldX']


def grounded(c):
    if c.round == 'R3' and c.args.jumps is None and c.rep is not None:
        supports = (c.rep.get('feet') or {}).get('supports')
        if supports:
            sup_frames = set()
            for sp in supports:
                a, b = sp.get('frames', (0, -1))
                sup_frames.update(range(a, b + 1))
            return [i for i in range(c.N) if i in sup_frames and i not in c.air]
    return [i for i in range(c.N) if i not in c.air]


def floor_reading(c):
    """The one floor value: the median of the lower foot's height over grounded frames."""
    need_rig(c)
    need_aligned(c)
    need_air(c)
    frames = grounded(c)
    need(frames, 'no grounded frame: every frame is inside an airborne span')
    lows = {i: min(foot_y(c, i, c.foot_l), foot_y(c, i, c.foot_r)) for i in frames}
    return median(lows.values()), lows


def full_cycles(c):
    need(c.cycle and c.cycle > 0, '--cycle not given')
    k = c.N // c.cycle
    return [(j * c.cycle, (j + 1) * c.cycle) for j in range(k)]


def keyed_bones(c):
    """The bones the retarget keys a rotation on: the report's angle landings (excluding face slider dials)."""
    need(c.rep is not None, f'the keyed bones are the report\'s landings: {c.rep_why}')
    face_dials = set()
    face_rep = c.rep.get('face')
    if isinstance(face_rep, dict):
        for axis in ('yaw', 'pitch'):
            sub = face_rep.get(axis)
            if isinstance(sub, dict) and sub.get('bone'):
                face_dials.add(sub['bone'])
    names = []
    for l in c.rep.get('landings') or []:
        if l.get('kind') == 'angle' and l.get('bone') not in names and l.get('bone') not in face_dials:
            names.append(l['bone'])
    need(names, '--report lists no angle landing')
    return names


def world_angle(b):
    return math.degrees(math.atan2(b['c'], b['a']))


def local_angle(c, frame, name):
    """The bone's rotation in its parent's axes: P^-1 C, so a rotate key's value up to a constant."""
    b = frame[name]
    p = c.geo.parent.get(name)
    if p is None or p not in frame:
        return world_angle(b)
    q = frame[p]
    det = q['a'] * q['d'] - q['b'] * q['c']
    if det == 0:
        return world_angle(b)
    la = (q['d'] * b['a'] - q['b'] * b['c']) / det
    lc = (-q['c'] * b['a'] + q['a'] * b['c']) / det
    return math.degrees(math.atan2(lc, la))


def mean_second_diff(series_list):
    vals = []
    for v in series_list:
        for i in range(1, len(v) - 1):
            vals.append(abs(wrap(v[i + 1] - v[i]) - wrap(v[i] - v[i - 1])))
    return statistics.mean(vals) if vals else None


def per_cycle_width(values, cycles):
    widths = [max(values[a:b]) - min(values[a:b]) for a, b in cycles]
    return median(widths)


def seq_mid_hip(c, i):
    l, r = c.seq.joint(i, 'l_hip'), c.seq.joint(i, 'r_hip')
    if not l or not r:
        return None
    return ((l[0] + r[0]) / 2, (l[1] + r[1]) / 2)


# ---------------------------------------------------------------- R1 rows

def row_gate(c):
    need(c.build is not None, c.build_why)
    text = c.build
    red = []
    for line in text.splitlines():
        s = line.strip()
        if re.match(r'^FAIL\s', s) or 'assertion(s) failed' in s or 'RIG_GATE' in s or 'POSE_LANDS' in s:
            red.append(s)
    summaries = re.findall(r'(\d+) assertions: (\d+) measured \((\d+) passed, (\d+) failed\)', text)
    if any(int(f) > 0 for *_, f in summaries):
        red.append(next(f'{n} assertions: {m} measured ({p} passed, {f} failed)' for n, m, p, f in summaries if int(f) > 0))
    if red:
        return False, f'build is red: {red[0][:160]}'
    need(summaries, f'--build {c.args.build}: no gate summary line ("N assertions: M measured (P passed, F failed)")')
    n, m, p, f = summaries[-1]
    need(c.rep is not None, f'build green ({n} assertions, {f} failed); the landings are read from the report: {c.rep_why}')
    lands = c.rep.get('landings') or []
    need(lands, '--report lists no landing')
    off = [l for l in lands if not meets(l['worst'], '<=', l['tolerance'])]
    if off:
        l = off[0]
        return False, f'build green; {len(off)} of {len(lands)} landing(s) past tolerance, first {l["bone"]} {l["kind"]} worst {shown(l["worst"], ".4g", (l["tolerance"],))} > {l["tolerance"]:.4g} at frame {l["frame"]}'
    share = max(l['worst'] / l['tolerance'] if l['tolerance'] else 0 for l in lands)
    return True, f'build green ({n} assertions: {m} measured, {f} failed); {len(lands)}/{len(lands)} landings within tolerance (worst at {share:.2f} of its tolerance)'


def row_support_foot(c):
    F, lows = floor_reading(c)
    worst = max(lows, key=lambda i: abs(lows[i] - F))
    dev = abs(lows[worst] - F) / c.L
    return meets(dev, '<=', BAR_FLOOR_BAND), f'max |lower foot - floor| {shown(dev, ".4f", (BAR_FLOOR_BAND,))} leg lengths at frame {worst} over {len(lows)} grounded frames (floor {F:.3f} units) [bar <= {BAR_FLOOR_BAND}]'


def row_two_feet(c):
    """Two-foot frames (sequence ankles within 0.02 Ls): rig feet within 0.02 L of each other.
    Lifted frames (sequence ankles more than 0.04 Ls apart): the rig lifts the foot the sequence lifts by
    more than the support-foot band, and the median rig lift / sequence lift is in the hip-width band.
    Frames between the two bands are not read. --stance does not move any bar."""
    need_rig(c)
    need_aligned(c)
    need_air(c)
    need(c.Ls is not None, c.seq_units_why)
    both, lifted = [], []
    for i in grounded(c):
        la, ra = c.seq.joint(i, 'l_ankle'), c.seq.joint(i, 'r_ankle')
        if not la or not ra:
            continue
        d_seq = (ra[1] - la[1]) / c.Ls          # > 0: left ankle above right (picture y is down)
        d_rig = (foot_y(c, i, c.foot_l) - foot_y(c, i, c.foot_r)) / c.L   # > 0: left foot above right
        if abs(d_seq) <= BAR_TWO_FEET:
            both.append((abs(d_rig), i))
        elif abs(d_seq) > LIFT_FLOOR:
            rig_lift = d_rig if d_seq > 0 else -d_rig   # the foot the sequence lifts, above the other
            lifted.append((rig_lift, abs(d_seq), i))
    need(both or lifted, 'no grounded frame with both ankles in the sequence')
    parts, ok = [], True
    if both:
        v, i = max(both)
        ok &= meets(v, '<=', BAR_TWO_FEET)
        parts.append(f'two-foot frames: max height difference {shown(v, ".4f", (BAR_TWO_FEET,))} leg lengths at frame {i} over {len(both)} [bar <= {BAR_TWO_FEET}]')
    else:
        parts.append('two-foot frames: none in the sequence')
    if lifted:
        planted = [(rl, i) for rl, _, i in lifted if meets(rl, '<=', BAR_FLOOR_BAND)]
        lo_lift, lo_i = min((rl, i) for rl, _, i in lifted)
        ratio = median([rl / sl for rl, sl, _ in lifted])
        lo, hi = BAR_LIFT_RATIO
        ok &= not planted and meets(ratio, 'in', (lo, hi))
        parts.append(f'lifted frames (sequence ankles > {LIFT_FLOOR:g} apart): {len(planted)} of {len(lifted)} with the lifted foot '
                     f'within {BAR_FLOOR_BAND} of the support foot (lowest lift {shown(lo_lift, ".4f", (BAR_FLOOR_BAND,))} at frame {lo_i}) [bar 0]; '
                     f'median rig/sequence lift {shown(ratio, ".3f", (lo, hi))} [bar {lo}-{hi}]')
    else:
        parts.append(f'lifted frames: none in the sequence (ankles > {LIFT_FLOOR:g} apart)')
    return ok, '; '.join(parts)


def row_shin_scale(c):
    """The rendered x-scale of each shin bone, |(a, c)| of its world matrix (1.0 = setup length):
    the 5th percentile over all frames and both shins. A leg drawn shorter than 0.4 of its setup
    length on more than one frame in twenty is a leg that vanishes, whatever the feet rows read."""
    need(c.geo is not None, c.geo_why)
    missing = [n for n in SHIN_BONES if not c.geo.has(n)]
    need(not missing, f'--geometry has no shin bone {", ".join(missing)} (the row reads {", ".join(SHIN_BONES)})')
    xs = []
    for i, f in enumerate(c.geo.frames):
        for n in SHIN_BONES:
            b = f.get(n)
            need(b is not None, f'--geometry frame {i} carries no {n}')
            xs.append((math.hypot(b['a'], b['c']), i, n))
    need(xs, '--geometry has no frame')
    p05 = percentile([x for x, _, _ in xs], 0.05)
    lo, lo_i, lo_n = min(xs)
    return meets(p05, '>=', BAR_SHIN_SCALE), (f'5th percentile shin x-scale {shown(p05, ".3f", (BAR_SHIN_SCALE,))} over {len(c.geo.frames)} frames x {len(SHIN_BONES)} shins '
                                   f'({", ".join(SHIN_BONES)}; 1.0 = setup length); min {lo:.3f} at frame {lo_i} ({lo_n}) [bar >= {BAR_SHIN_SCALE}]')


def row_slide(c):
    need_rig(c)
    need_aligned(c)
    need_air(c)
    in_place = bool(c.seq is not None and c.seq.in_place)
    if in_place:
        # The report's declared scale (its SCALE line, rig units per picture px) is the scale the
        # retarget moves the supporting foot by; no other scale is tried in its place.
        need(c.rep is not None, f'travel in-place: the declared scale is read from --report: {c.rep_why}')
        sc = c.rep.get('scale')
        sf = sc.get('factor') if isinstance(sc, dict) else None
        need(isinstance(sf, (int, float)) and not isinstance(sf, bool) and math.isfinite(sf) and sf > 0,
             f'travel in-place: --report has no usable scale.factor (found {sc!r}); the row reads no other scale')
        # The loop closure (report feet.closure): the hip's x drift spread back over the frames, so
        # every frame moves the supporting foot by -drift / (frames - 1) on top of the scaled ankle.
        cl = (c.rep.get('feet') or {}).get('closure')
        if cl is None:
            per, cl_text = 0.0, 'feet.closure absent from the report: closure drift taken as 0'
        else:
            dr, nf = cl.get('drift'), cl.get('frames')
            need(isinstance(dr, (int, float)) and isinstance(nf, int) and nf > 1,
                 f'travel in-place: report feet.closure is not {{drift, frames > 1}} (found {cl!r})')
            per = -dr / (nf - 1)
            cl_text = f'closure {per:+.5f} units/frame removed (report feet.closure drift {dr:.2f} over {nf} frames)'
    supports = (c.rep.get('feet') or {}).get('supports') if c.rep is not None else None
    pairs = []
    if supports:
        for sp in supports:
            side = sp.get('side')
            a, b = sp.get('frames', (0, -1))
            s = c.foot_l if side == 'l' else c.foot_r
            ankle = 'l_ankle' if side == 'l' else 'r_ankle'
            for i in range(max(1, a + 1), min(b + 1, c.N)):
                if i in c.air or i - 1 in c.air:
                    continue
                pairs.append((i, s, ankle))
    else:
        for i in range(1, c.N):
            if i in c.air or i - 1 in c.air:
                continue
            is_l = foot_y(c, i - 1, c.foot_l) <= foot_y(c, i - 1, c.foot_r)
            s = c.foot_l if is_l else c.foot_r
            ankle = 'l_ankle' if is_l else 'r_ankle'
            pairs.append((i, s, ankle))
    if in_place:
        cand = []
        for i, s, ankle in pairs:
            a0, a1 = c.seq.joint(i - 1, ankle), c.seq.joint(i, ankle)
            if not a0 or not a1:
                continue
            dfx = foot_x(c, i, s) - foot_x(c, i - 1, s)
            dax = a1[0] - a0[0]
            cand.append((abs(dfx - per - dax * sf) / c.L, i, s))
        need(cand, 'no two consecutive grounded frames with sequence ankles')
        v, i, s = max(cand)
        return meets(v, '<=', BAR_SLIDE), (f'max |support-foot move - closure - sequence ankle move x report scale {sf:.5f}| {shown(v, ".5f", (BAR_SLIDE,))} leg lengths/frame ({s}, frame {i - 1}->{i}) '
                                f'over {len(cand)} steps (travel: in-place; {cl_text}) [bar <= {BAR_SLIDE}]')
    moves = []
    for i, s, _ in pairs:
        moves.append((abs(foot_x(c, i, s) - foot_x(c, i - 1, s)) / c.L, i, s))
    need(moves, 'no two consecutive grounded frames')
    v, i, s = max(moves)
    return meets(v, '<=', BAR_SLIDE), f'max support-foot move {shown(v, ".5f", (BAR_SLIDE,))} leg lengths/frame ({s}, frame {i - 1}->{i}) over {len(moves)} steps [bar <= {BAR_SLIDE}]'


def row_floor(c):
    F, lows = floor_reading(c)
    if c.round == 'R3' and not (c.cycle and c.cycle > 0):
        need(c.rep is not None, f'support spans are read from --report: {c.rep_why}')
        supports = (c.rep.get('feet') or {}).get('supports') or []
        need(len(supports) >= 2, f'--report has {len(supports)} support span(s): two are needed')
        floors = []
        for sp in supports:
            a, b = sp.get('frames', (0, -1))
            vals = [lows[i] for i in range(a, min(b + 1, c.N)) if i in lows]
            if vals:
                floors.append(median(vals))
        need(len(floors) >= 2, 'fewer than two support spans have a grounded frame')
        spread = (max(floors) - min(floors)) / c.L
        return meets(spread, '<=', BAR_FLOOR_BAND), (f'per-support-span floor spread {shown(spread, ".4f", (BAR_FLOOR_BAND,))} leg lengths over {len(floors)} spans '
                                          f'[bar <= {BAR_FLOOR_BAND}, the support-foot band: the table gives this row no number of its own]')
    cycles = full_cycles(c)
    need(len(cycles) >= 2, f'{c.N} frames hold {len(cycles)} full cycle(s) of {c.cycle}: two are needed')
    floors = []
    for a, b in cycles:
        vals = [lows[i] for i in range(a, b) if i in lows]
        if vals:
            floors.append(median(vals))
    need(len(floors) >= 2, 'fewer than two cycles have a grounded frame')
    spread = (max(floors) - min(floors)) / c.L
    return meets(spread, '<=', BAR_FLOOR_BAND), (f'per-cycle floor spread {shown(spread, ".4f", (BAR_FLOOR_BAND,))} leg lengths over {len(floors)} cycles '
                                      f'[bar <= {BAR_FLOOR_BAND}, the support-foot band: the table gives this row no number of its own]')


def _seq_seg_angles(c, j0, j1, n):
    out = []
    for i in range(n):
        p0, p1 = c.seq.joint(i, j0), c.seq.joint(i, j1)
        if not p0 or not p1 or (p0[0] == p1[0] and p0[1] == p1[1]):
            return None
        out.append(math.degrees(math.atan2(-(p1[1] - p0[1]), p1[0] - p0[0])))
    return out


def map_pairs(m):
    """bone -> (joint, joint) as the map gives it: a chain's k-th bone runs from its k-th joint to the next;
    a one-bone chain with two joints (pelvis, trunk, head) runs from the first to the second."""
    out = {}
    for ch in m.get('chains') or []:
        bones, joints = ch.get('bones') or [], ch.get('joints') or []
        for k, b in enumerate(bones):
            if k + 1 < len(joints):
                out[b] = (joints[k], joints[k + 1])
    return out


def row_jitter(c):
    need(c.geo is not None, c.geo_why)
    need(c.seq is not None, c.seq_why)
    need_aligned(c)
    keyed = keyed_bones(c)
    need(c.trunk is not None, '--trunk not given: name the trunk and head bones')
    need(c.map is not None, c.map_why)
    missing = [b for b in keyed if not c.geo.has(b)]
    need(not missing, f'keyed bone(s) {missing} not in the geometry')
    trunk = [b for b in keyed if b in c.trunk]
    limbs = [b for b in keyed if b not in c.trunk]
    need(trunk, f'--trunk {",".join(c.trunk)}: none of them is keyed (keyed: {",".join(keyed)})')
    need(limbs, 'every keyed bone is in --trunk: no limb')
    need(c.N >= 3, 'fewer than three aligned frames')
    pairs = map_pairs(c.map)
    unmapped = [b for b in keyed if b not in pairs]
    need(not unmapped, f'keyed bone(s) {unmapped} have no joint pair in the map')

    l_rig = {b: [local_angle(c, c.geo.frames[i], b) for i in range(c.N)] for b in keyed}
    w_seq = {}
    for b in keyed:
        j0, j1 = pairs[b]
        w_seq[b] = _seq_seg_angles(c, j0, j1, c.N)
        need(w_seq[b] is not None, f'the sequence lacks {j0} or {j1} (the map\'s pair for {b}) on a frame')

    # The sequence's local rotation: the bone's pair against the pair of its nearest keyed ancestor,
    # as the rig's local rotation is against its parent.
    keyed_set = set(keyed)
    l_seq = {}
    for b in keyed:
        p = c.geo.parent.get(b)
        while p is not None and p not in keyed_set:
            p = c.geo.parent.get(p)
        l_seq[b] = [wrap(w_seq[b][i] - w_seq[p][i]) for i in range(c.N)] if p is not None else w_seq[b]

    jl = mean_second_diff([l_rig[b] for b in limbs])
    jl_seq = mean_second_diff([l_seq[b] for b in limbs])
    jt = mean_second_diff([l_rig[b] for b in trunk])
    jt_seq = mean_second_diff([l_seq[b] for b in trunk])
    need(jl is not None and jt is not None and jl_seq and jt_seq, 'fewer than three frames with non-zero sequence motion')
    rl = jl / jl_seq
    rt = jt / jt_seq
    ok = meets(rl, '<=', BAR_JITTER_RATIO) and meets(rt, '<=', BAR_JITTER_RATIO)
    return ok, (f'limbs {shown(rl, ".3f", (BAR_JITTER_RATIO,))}x sequence ({jl:.3f} vs {jl_seq:.3f} deg/f^2, {len(limbs)} bones) [bar <= {BAR_JITTER_RATIO}], '
                f'trunk+head {shown(rt, ".3f", (BAR_JITTER_RATIO,))}x sequence ({jt:.3f} vs {jt_seq:.3f} deg/f^2, {",".join(trunk)}) [bar <= {BAR_JITTER_RATIO}]; '
                f'joint pairs from the map')


def row_folds(c):
    need(c.folds is not None, c.folds_why)
    d = c.folds
    need(isinstance(d, dict) and d.get('spec') == FOLDS_SPEC, f'--folds {c.args.folds}: spec is not {FOLDS_SPEC}')
    if c.geo is not None and d.get('animation') != c.geo.animation:
        raise Skip(f'--folds reads animation {d.get("animation")!r}, the geometry {c.geo.animation!r}')
    meshes = d.get('meshes') or []
    need(meshes, '--folds reads no mesh: nothing to measure')
    frames = set()
    worst = None
    for m in meshes:
        idx = [f['index'] for f in m.get('frames') or []]
        frames.update(idx)
        if idx and (worst is None or len(idx) > worst[1]):
            worst = (m.get('slot'), len(idx))
    if frames:
        return False, f'{len(frames)} frame(s) with a folded triangle, most in slot {worst[0]!r} ({worst[1]} frames) [bar 0]'
    return True, f'0 frames fold over {len(meshes)} mesh(es) [bar 0]'


PASS_SUMMARY = re.compile(r'(?:("[^"]*"|the setup pose): )?cloth "([^"]+)" over leg "([^"]+)" passes through on (\d+) of (\d+) frame\(s\) read')
PASS_NONE = re.compile(r'(?:("[^"]*"|the setup pose): )?cloth "([^"]+)" over leg "([^"]+)": (the two slots draw together on no frame|the cloth draws over the leg on 0 of)')


def row_pass_through(c):
    need(c.pt_text is not None, c.pt_why)
    pairs = []  # (cloth, leg, passes or None for nothing read, read, animation)
    try:
        d = json.loads(c.pt_text)
    except ValueError:
        d = None
    if isinstance(d, dict):
        need(d.get('spec') == PASS_SPEC, f'--passthrough {c.args.passthrough}: JSON whose spec is not {PASS_SPEC}')
        for p in d.get('pairs') or []:
            read = p.get('over', 0)
            pairs.append((p['cloth'], p['leg'], len(p.get('frames') or []) if read else None, read, d.get('animation')))
    else:
        for line in c.pt_text.splitlines():
            m = PASS_SUMMARY.search(line)
            if m:
                pairs.append((m.group(2), m.group(3), int(m.group(4)), int(m.group(5)), json.loads(m.group(1)) if m.group(1) and m.group(1).startswith('"') else None))
                continue
            m = PASS_NONE.search(line)
            if m:
                pairs.append((m.group(2), m.group(3), None, 0, json.loads(m.group(1)) if m.group(1) and m.group(1).startswith('"') else None))
    need(pairs, f'--passthrough {c.args.passthrough}: no pass-through reading in it')
    if c.geo is not None:
        other = [p for p in pairs if p[4] is not None and p[4] != c.geo.animation]
        need(not other, f'--passthrough reads animation {other[0][4]!r} if any, the geometry {c.geo.animation!r}' if other else '')
    through = [p for p in pairs if p[2]]
    if through:
        p = through[0]
        return False, f'cloth {p[0]!r} over leg {p[1]!r} passes through on {p[2]} of {p[3]} frames read [bar 0]'
    empty = [p for p in pairs if p[2] is None]
    need(not empty, f'cloth {empty[0][0]!r} over leg {empty[0][1]!r}: nothing read (the cloth draws over the leg on no frame)' if empty else '')
    return True, '; '.join(f'{p[0]}:{p[1]} 0 of {p[3]} frames' for p in pairs) + ' [bar 0]'


def row_loop(c):
    need_aligned(c)
    keyed = keyed_bones(c)
    missing = [b for b in keyed if not c.geo.has(b)]
    need(not missing, f'keyed bone(s) {missing} not in the geometry')
    need_rig(c)
    cycles = full_cycles(c)
    need(len(cycles) >= 2, f'{c.N} frames hold {len(cycles)} full cycle(s) of {c.cycle}: two are needed')
    last = cycles[-1][0]
    worst = (0.0, None, None)
    worst_p = (0.0, None, None)
    placed = [c.hip, c.foot_l, c.foot_r]
    for i in range(c.cycle):
        f0, f1 = c.geo.frames[i], c.geo.frames[last + i]
        for b in keyed:
            d = abs(wrap(world_angle(f0[b]) - world_angle(f1[b])))
            if d > worst[0]:
                worst = (d, b, i)
        for b in placed:
            d = math.hypot(f0[b]['worldX'] - f1[b]['worldX'], f0[b]['worldY'] - f1[b]['worldY']) / c.L
            if d > worst_p[0]:
                worst_p = (d, b, i)
    d, b, i = worst
    dp, bp, ip = worst_p
    where = f' ({b}, cycle frame {i})' if b else ''
    where_p = f' ({bp}, cycle frame {ip})' if bp else ''
    return meets(d, '<=', BAR_LOOP) and meets(dp, '<=', BAR_LOOP_POS), (
        f'cycle 1 vs cycle {len(cycles)}: max keyed-bone angle difference {shown(d, ".4f", (BAR_LOOP,))} deg{where} [bar <= {BAR_LOOP}], '
        f'max {"/".join(placed)} world position difference {shown(dp, ".4f", (BAR_LOOP_POS,))} leg lengths{where_p} [bar <= {BAR_LOOP_POS}]')


# ---------------------------------------------------------------- R2 / R3 rows

def row_airborne(c):
    F, _ = floor_reading(c)
    if c.round == 'R3':
        spans = [j for j in c.jumps if j[0] < c.N]
        ok = len(spans) == BAR_JUMP_SPANS_R3
        parts = [f'airborne spans {len(spans)} ({", ".join(f"{a}-{b}" for a, b in spans)}) [bar {BAR_JUMP_SPANS_R3}]']
        if not spans:
            return False, '; '.join(parts + ['no airborne span inside the geometry'])
        peaks = []
        grounded_on = []   # (low foot height above the floor, frame) on frames where a foot is not above it
        for a, b in spans:
            fs = [i for i in range(a, min(b + 1, c.N))]
            if not fs:
                continue
            for i in fs:   # every frame of the span: both feet above the floor
                low = (min(foot_y(c, i, c.foot_l), foot_y(c, i, c.foot_r)) - F) / c.L
                if not meets(low, '>', 0.0):
                    grounded_on.append((low, i))
            best_i = max(fs, key=lambda i: ((foot_y(c, i, c.foot_l) + foot_y(c, i, c.foot_r)) / 2 - F) / c.L)
            peak_mean = ((foot_y(c, best_i, c.foot_l) + foot_y(c, best_i, c.foot_r)) / 2 - F) / c.L
            peaks.append((peak_mean, best_i, f'{a}-{b}'))
        worst_peak, worst_i, worst_sp = min(peaks)
        ok &= not grounded_on and meets(worst_peak, '>', BAR_FLOOR_BAND)
        frames_n = sum(min(b + 1, c.N) - a for a, b in spans)
        parts.append(f'{len(grounded_on)} of {frames_n} span frame(s) with a foot not above the floor'
                     + (f' (first frame {min(grounded_on, key=lambda t: t[1])[1]})' if grounded_on else '') + ' [bar 0]')
        parts.append(f'min peak airborne foot height {shown(worst_peak, ".4f", (BAR_FLOOR_BAND,))} leg lengths above the floor at frame {worst_i} (span {worst_sp}) '
                     f'[bar > {BAR_FLOOR_BAND}: above the support-foot band]')
        return ok, '; '.join(parts)
    cycles = full_cycles(c)
    need(cycles, f'{c.N} frames hold no full cycle of {c.cycle}')
    printed, why = r2_air_reference(c)
    need(printed is not None, why)
    counts = [sum(1 for x, _ in c.jumps if a <= x < b) for a, b in cycles]
    ok = all(n == 2 for n in counts)
    # Each detected span within a printed span +/- BAR_AIR_MATCH frames (the printed spans repeat per cycle).
    ref = [(a + k * c.cycle, b + k * c.cycle) for k in range(len(cycles)) for a, b in printed]
    off = []
    for x, y in c.jumps:
        if x >= c.N:
            continue
        if not any(abs(x - a) <= BAR_AIR_MATCH and abs(y - b) <= BAR_AIR_MATCH for a, b in ref):
            off.append((x, y))
    ok &= not off
    lowest = None
    for i in sorted(c.air):
        if i >= c.N:
            continue
        h = (min(foot_y(c, i, c.foot_l), foot_y(c, i, c.foot_r)) - F) / c.L
        if lowest is None or h < lowest[0]:
            lowest = (h, i)
    parts = [f'airborne spans per cycle {counts} [bar 2 each]',
             f'{len(off)} detected span(s) off the printed spans {printed} +/- {BAR_AIR_MATCH}'
             + (f' (first {off[0][0]}-{off[0][1]})' if off else '') + ' [bar 0]']
    if lowest is None:
        ok = False
        parts.append('no airborne frame inside the geometry')
    else:
        ok &= meets(lowest[0], '>', BAR_FLOOR_BAND)
        parts.append(f'lowest foot on an airborne frame {shown(lowest[0], ".4f", (BAR_FLOOR_BAND,))} leg lengths above the floor at frame {lowest[1]} '
                     f'[bar > {BAR_FLOOR_BAND}: above the support-foot band]')
    return ok, '; '.join(parts)


def r2_air_reference(c):
    """(spans, None) or (None, refusal): R2's printed airborne spans for one cycle of --cycle frames."""
    if R2_AIR_REFERENCE is not None:
        why = spans_outside(R2_AIR_REFERENCE, c.cycle, 'R2_AIR_REFERENCE')
        return (None, why) if why else (list(R2_AIR_REFERENCE), None)
    path = getattr(c.args, 'airborne', None)
    if path is None:
        if c.args.sequence is None:
            return None, '--airborne not given and no --sequence: the airborne spans are the airborne.json beside the sequence'
        path = os.path.join(os.path.dirname(c.args.sequence), 'airborne.json')
    spans, why = airborne_reference(path, c.cycle)
    if spans is None and not os.path.isfile(path):
        why += ' (nor is R2_AIR_REFERENCE set in-process)'
    return spans, why


def hip_series(c):
    need_rig(c)
    need_aligned(c)
    need(c.Ls is not None, c.seq_units_why)
    idx, rig, seq = [], [], []
    for i in range(c.N):
        m = seq_mid_hip(c, i)
        if m is None:
            continue
        idx.append(i)
        # The sequence's mid_hip is the midpoint of its two hip joints, so the rig's is the
        # midpoint of its two thigh roots — not --hip's origin, which a hip tilt swings about.
        f = c.geo.frames[i]
        rig.append(((f[c.root_l]['worldX'] + f[c.root_r]['worldX']) / 2, (f[c.root_l]['worldY'] + f[c.root_r]['worldY']) / 2))
        seq.append(m)
    need(len(idx) == c.N, f'the sequence lacks a hip on {c.N - len(idx)} frame(s)')
    return rig, seq


def width_ratio(c, axis, rig_unit, seq_unit, label, unit_name):
    rig, seq = hip_series(c)
    if c.round == 'R3' and not (c.cycle and c.cycle > 0):
        need(c.rep is not None, f'support spans are read from --report: {c.rep_why}')
        supports = (c.rep.get('feet') or {}).get('supports') or []
        spans = [sp for sp in supports if sp.get('frames', (0, -1))[1] - sp.get('frames', (0, -1))[0] >= 5]
        need(spans, '--report has no support span of at least 5 frames')
        ls_ref, w_ref = c.Ls, c.seq_hip_width   # the sequence's own (camera-normalised) units
        wrs, wss = [], []
        for sp in spans:
            side = sp.get('side')
            a, b = sp.get('frames', (0, -1))
            b = min(b, c.N - 1)
            foot_b = c.foot_l if side == 'l' else c.foot_r
            ank_j = 'l_ankle' if side == 'l' else 'r_ankle'
            hip_j = 'l_hip' if side == 'l' else 'r_hip'
            rv, sv = [], []
            for i in range(a, b + 1):
                ank = c.seq.joint(i, ank_j)
                sh = c.seq.joint(i, hip_j)
                if not ank or not sh:
                    continue
                if axis == 1:
                    rv.append((rig[i][1] - foot_y(c, i, foot_b)) / rig_unit)
                    sv.append((ank[1] - seq[i][1]) / ls_ref)
                else:
                    rv.append((rig[i][0] - foot_x(c, i, foot_b)) / rig_unit)
                    leg_dx = (sh[0] - ank[0]) / ls_ref * (c.L / c.hip_width)
                    pel_dx = (seq[i][0] - sh[0]) / w_ref
                    sv.append(leg_dx + pel_dx)
            if len(rv) >= 2 and max(sv) - min(sv) > 1e-6:
                wrs.append(max(rv) - min(rv))
                wss.append(max(sv) - min(sv))
        need(wss, f'the sequence\'s hip has no {label} width over the support spans')
        ratios = [r / s for r, s in zip(wrs, wss)]
        ratio = median(ratios)
        wr, ws = median(wrs), median(wss)
        lo, hi = BAR_HIP_RATIO
        return meets(ratio, 'in', (lo, hi)), (f'rig/sequence {shown(ratio, ".3f", (lo, hi))} (rig {wr:.4f}, sequence {ws:.4f} {unit_name}, '
                                   f'median per-span width over {len(ratios)} spans) [bar {lo}-{hi}]')
    cycles = full_cycles(c)
    need(cycles, f'{c.N} frames hold no full cycle of {c.cycle}')
    sign = 1 if axis == 0 else -1  # picture y is down
    wr = per_cycle_width([p[axis] / rig_unit for p in rig], cycles)
    ws = per_cycle_width([sign * p[axis] / seq_unit for p in seq], cycles)
    need(ws > 0, f'the sequence\'s hip has no {label} width')
    ratio = wr / ws
    lo, hi = BAR_HIP_RATIO
    return meets(ratio, 'in', (lo, hi)), (f'rig/sequence {shown(ratio, ".3f", (lo, hi))} (rig {wr:.4f}, sequence {ws:.4f} {unit_name}, '
                               f'median per-cycle width over {len(cycles)} cycles) [bar {lo}-{hi}]')


def row_hip_vertical(c):
    need_rig(c)
    return width_ratio(c, 1, c.L, c.Ls, 'vertical', 'leg lengths')


def row_hip_horizontal(c):
    need_rig(c)
    need(c.seq_hip_width, c.seq_units_why or 'the sequence never has both hips')
    need(c.hip_width and c.hip_width > 0, 'the rig\'s thigh roots coincide at setup: no hip width')
    return width_ratio(c, 0, c.hip_width, c.seq_hip_width, 'horizontal', 'hip widths')


def row_rebound(c):
    rig, seq = hip_series(c)
    need_air(c)
    hr = [p[1] / c.L for p in rig]
    hs = [-p[1] / c.Ls for p in seq]   # the sequence's own (camera-normalised) units
    spans = sorted(j for j in c.jumps if j[1] < c.N)
    windows = [(a[1] + 1, b[0] - 1) for a, b in zip(spans, spans[1:]) if b[0] - 1 >= a[1] + 1]
    need(windows, 'no stance window between two airborne spans')
    ratios = []
    for a, b in windows:
        js = [j for j in range(max(a, 1), min(b, c.N - 2) + 1)]
        if not js:
            continue
        acc_s = max(hs[j - 1] - 2 * hs[j] + hs[j + 1] for j in js)
        acc_r = max(hr[j - 1] - 2 * hr[j] + hr[j + 1] for j in js)
        if acc_s > 0:
            ratios.append(acc_r / acc_s)
    need(ratios, 'no stance window where the sequence\'s hip accelerates upward')
    v = median(ratios)
    lo, hi = BAR_REBOUND
    return meets(v, 'in', (lo, hi)), (f'median rig/sequence peak upward hip acceleration in the stance windows {shown(v, ".3f", (lo, hi))} '
                           f'over {len(ratios)} windows [bar {lo}-{hi:.2f}]')


def row_hip_tilt(c):
    need_rig(c)
    need_aligned(c)
    need(c.seq is not None, c.seq_why)
    allow_inf = bool(c.seq.measured_hips)
    rt, st = [], []
    left_out = 0
    for i in range(c.N):
        l, r = c.seq.joint(i, 'l_hip', allow_inferred=allow_inf), c.seq.joint(i, 'r_hip', allow_inferred=allow_inf)
        if not l or not r:
            left_out += 1
            continue
        st.append(math.degrees(math.atan2(-(l[1] - r[1]), l[0] - r[0])))
        f = c.geo.frames[i]
        rt.append(math.degrees(math.atan2(f[c.root_l]['worldY'] - f[c.root_r]['worldY'], f[c.root_l]['worldX'] - f[c.root_r]['worldX'])))
    need(len(st) >= 3, 'the hips are inferred or missing on every frame: no tilt to read')
    st = [wrap(v - st[0]) for v in st]
    rt = [wrap(v - rt[0]) for v in rt]
    rs, rr = max(st) - min(st), max(rt) - min(rt)
    need(rs > 0, 'the sequence\'s hip line does not tilt')
    ms, mr = statistics.mean(st), statistics.mean(rt)
    cov = sum((a - ms) * (b - mr) for a, b in zip(st, rt))
    share = rr / rs
    ok = meets(share, '>=', BAR_TILT) and meets(cov, '>', 0)
    note = f'; {left_out} frame(s) with an inferred hip left out' if left_out else ''
    return ok, (f'rig tilt range {rr:.3f} deg = {shown(share, ".3f", (BAR_TILT,))} of the sequence\'s {rs:.3f} [bar >= {BAR_TILT}], '
                f'sign {"agrees" if cov > 0 else "DISAGREES"} (covariance {cov:+.3g}){note}')


# ---------------------------------------------------------------- table

R1_ROWS = [
    ('gate', 'Gate', row_gate),
    ('support-foot', 'Support foot', row_support_foot),
    ('two-feet', 'Two feet', row_two_feet),
    ('shin-scale', 'Shin scale', row_shin_scale),
    ('slide', 'Slide', row_slide),
    ('floor', 'Floor', row_floor),
    ('jitter', 'Jitter', row_jitter),
    ('folds', 'Folds', row_folds),
    ('pass-through', 'Pass-through', row_pass_through),
    ('loop', 'Loop', row_loop),
]
R2_ROWS = [
    ('airborne', 'Airborne', row_airborne),
    ('hip-vertical', 'Hip vertical range', row_hip_vertical),
    ('hip-horizontal', 'Hip horizontal range', row_hip_horizontal),
    ('rebound', 'Rebound', row_rebound),
    ('hip-tilt', 'Hip tilt', row_hip_tilt),
]
R3_ROWS = R1_ROWS[:-1] + [
    ('airborne', 'Airborne', row_airborne),
    ('hip-vertical', 'Hip vertical range', row_hip_vertical),
    ('hip-horizontal', 'Hip horizontal range', row_hip_horizontal),
    ('rebound', 'Rebound', row_rebound),
    ('hip-tilt', 'Hip tilt', row_hip_tilt),
]


def grade(c):
    if c.round == 'R3':
        rows = R3_ROWS
    elif c.round == 'R2':
        rows = R1_ROWS + R2_ROWS
    else:
        rows = R1_ROWS
    out = []
    for key, label, fn in rows:
        try:
            ok, figure = fn(c)
            out.append(('PASS' if ok else 'FAIL', key, label, figure))
        except Skip as e:
            out.append(('SKIP', key, label, str(e) or 'not measured'))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description='Grade an Advanced R1/R2/R3 attempt against its pass table.')
    ap.add_argument('--round', choices=('R1', 'R2', 'R3'), default='R1')
    ap.add_argument('--geometry')
    ap.add_argument('--sequence')
    ap.add_argument('--report')
    ap.add_argument('--build')
    ap.add_argument('--folds')
    ap.add_argument('--passthrough')
    ap.add_argument('--camera')
    ap.add_argument('--map')
    ap.add_argument('--cycle', type=int, help='frames per cycle for the looped rounds (R1 32, R2 20); omit for R3, whose floor and hip rows read the report\'s support spans — passing the clip length makes them SKIP')
    ap.add_argument('--feet', default='foot_l,foot_r', help='the two bones whose ORIGIN is the ankle (default foot_l,foot_r; a shin bone\'s origin is the knee and reads a false floor error)')
    ap.add_argument('--hip', default='hip')
    ap.add_argument('--trunk')
    ap.add_argument('--jumps')
    ap.add_argument('--airborne', help='R2: the round\'s inputs/pose/airborne.json (default: the airborne.json beside --sequence)')
    ap.add_argument('--person')
    a = ap.parse_args(argv)
    c = build_ctx(a)
    print(f'grade {a.round}')
    for n in c.notes:
        print(f'NOTE  {n}')
    rows = grade(c)
    for status, key, label, figure in rows:
        print(f'{status:<5} {key:<15} {label}: {figure}')
    n_pass = sum(1 for r in rows if r[0] == 'PASS')
    n_fail = sum(1 for r in rows if r[0] == 'FAIL')
    n_skip = sum(1 for r in rows if r[0] == 'SKIP')
    verdict = 'FAIL' if n_fail else ('INCOMPLETE' if n_skip else 'PASS')
    print(f'RESULT {verdict} ({n_pass} pass, {n_fail} fail, {n_skip} skip of {len(rows)} rows)')
    return 1 if n_fail else (2 if n_skip else 0)


if __name__ == '__main__':
    sys.exit(main())
