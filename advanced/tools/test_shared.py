#!/usr/bin/env python3
"""Check the block every edition's grader shares (exam#11), from the grader files themselves.

usage: python3 advanced/tools/test_shared.py [grade.py ...]
       (no argument: advanced/R1, R2 and R3 tools/grade.py beside this file)

For each file: extracts the lines between the shared-block markers, prints the block's sha256,
runs the cases below against that block alone (nothing else of the grader is loaded), and checks
that every file carries the same block. Exit 0 when every case passes on every file. Standard
library only.
"""
import hashlib
import json
import os
import sys
import tempfile

BEGIN = "# --- shared with the other edition's grader (exam#11) ---\n"
END = '# --- end shared ---\n'
HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT = [os.path.join(HERE, '..', r, 'tools', 'grade.py') for r in ('R1', 'R2', 'R3')]


def extract(path):
    with open(path, encoding='utf-8') as fh:
        text = fh.read()
    if text.count(BEGIN) != 1 or text.count(END) != 1:
        raise SystemExit(f'{path}: the shared-block markers are not there exactly once each')
    start = text.index(BEGIN)
    end = text.index(END, start) + len(END)
    return text[start:end]


def cases(ns, tmp):
    """(name, passed) for every shared case."""
    meets, shown, airborne_reference = ns['meets'], ns['shown'], ns['airborne_reference']
    out = []
    # exam#11: comparisons are exact (no tolerance: none separates float error from the boundary controls), so a
    # shin clamped at the bar that renders 0.3999993 does not meet >= 0.4; the print below shows why.
    out.append(('0.3999993 does not meet >= 0.4 (comparisons are exact)', not meets(0.3999993, '>=', 0.4)))
    # One printed-rounding step past each bar, on its wrong side, never meets it:
    # (value, op, bar, the row's printed spec).
    for v, op, bar, spec in [(0.399, '>=', 0.4, '.3f'),            # shin scale
                             (0.00501, '<=', 0.005, '.5f'),        # slide
                             (0.0101, '<=', 0.01, '.4f'),          # support foot, floor, loop position
                             (0.0201, '<=', 0.02, '.4f'),          # two feet
                             (1.101, '<=', 1.1, '.3f'),            # jitter
                             (1.0001, '<=', 1.0, '.4f'),           # loop angle
                             (0.849, '>=', 0.85, '.3f'),           # hip tilt
                             (0.0099, '>', 0.01, '.4f'),           # airborne foot height
                             (0.849, 'in', (0.85, 1.15), '.3f'),   # hip ranges, lift ratio
                             (1.151, 'in', (0.85, 1.15), '.3f'),
                             (0.699, 'in', (0.7, 1 / 0.7), '.3f'),  # rebound
                             (1.430, 'in', (0.7, 1 / 0.7), '.3f')]:
        out.append((f'{v} {op} {bar} one printed step ({spec}) past the bar does not meet it', not meets(v, op, bar)))
    for v, op, bar in [(0.4, '>=', 0.4), (0.005, '<=', 0.005), (0.85, 'in', (0.85, 1.15)), (1.15, 'in', (0.85, 1.15))]:
        out.append((f'{v} {op} {bar}: a value at its bar meets it', meets(v, op, bar)))
    # exam#7: the full figure is printed beside the rounded one exactly when the value prints as its bar.
    for v, spec, bars, want in [(0.3999993, '.3f', (0.4,), '0.400 (0.3999993)'),
                                (0.4004, '.3f', (0.4,), '0.400 (0.4004)'),
                                (0.399, '.3f', (0.4,), '0.399'),
                                (0.41, '.3f', (0.4,), '0.410'),
                                (0.0050004, '.5f', (0.005,), '0.00500 (0.0050004)'),
                                (0.00502, '.5f', (0.005,), '0.00502'),
                                (1.1499999, '.3f', (0.85, 1.15), '1.150 (1.1499999)'),
                                (1.0, '.3f', (0.85, 1.15), '1.000')]:
        got = shown(v, spec, bars)
        out.append((f'shown({v}, {spec!r}, {bars}) is {want!r} (got {got!r})', got == want))
    # exam#11 (1): spans for one cycle, read from the round's file, held to --cycle.
    path = os.path.join(tmp, 'airborne.json')
    with open(path, 'w', encoding='utf-8') as fh:
        json.dump({'spec': ns['AIRBORNE_SPEC'], 'cycle': 20, 'spans': [[4, 9], [14, 19]]}, fh)
    spans, why = airborne_reference(path, 20)
    out.append(('spans inside the declared --cycle 20 pass', spans == [(4, 9), (14, 19)] and why is None))
    spans, why = airborne_reference(path, 19)
    out.append((f'a span outside --cycle 19 is refused naming the file and the span ({why})',
                spans is None and why is not None and path in why and '14-19' in why))
    spans, why = airborne_reference(path, 21)
    out.append((f'a file read for another cycle is refused naming the file ({why})',
                spans is None and why is not None and path in why and '21' in why))
    missing = os.path.join(tmp, 'absent', 'airborne.json')
    spans, why = airborne_reference(missing, 20)
    out.append((f'an absent file is refused naming it ({why})', spans is None and why is not None and missing in why))
    out.append(('span 0-0 in a 1-frame cycle passes; -1-3 and 3-2 are refused',
                ns['spans_outside']([(0, 0)], 1, 's') is None and ns['spans_outside']([(-1, 3)], 20, 's') is not None
                and ns['spans_outside']([(3, 2)], 20, 's') is not None))
    return out


def main(argv):
    paths = argv or DEFAULT
    blocks, failed = {}, 0
    with tempfile.TemporaryDirectory() as tmp:
        for p in paths:
            block = extract(p)
            blocks[p] = block
            print(f'{hashlib.sha256(block.encode("utf-8")).hexdigest()}  shared block of {p}')
            ns = {}
            exec(compile(block, f'{p} (shared block)', 'exec'), ns)
            for name, ok in cases(ns, tmp):
                failed += not ok
                print(f'  {"ok  " if ok else "FAIL"} {name}')
    if len(set(blocks.values())) != 1:
        failed += 1
        print('FAIL the shared blocks differ between the files')
    else:
        print(f'ok   one shared block across {len(blocks)} file(s)')
    print('RESULT ' + ('PASS' if not failed else f'FAIL ({failed} case(s))'))
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
