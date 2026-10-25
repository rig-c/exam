"""Fixture documentation contracts: Euclidean geometry, no poser or grader execution."""
import datetime
import json
import math
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / 'fixtures/mannequin'


def up(point):
    return point[0], -point[1]


def turn(point, degrees):
    a = math.radians(degrees)
    x, y = point
    return x * math.cos(a) - y * math.sin(a), x * math.sin(a) + y * math.cos(a)


def triangle_reaches(first, second, distance):
    return abs(first - second) <= distance <= first + second


def table(text, header):
    """Read one small Markdown table, without depending on surrounding line wrapping."""
    body = text.split(header + '\n', 1)[1].split('\n\n', 1)[0]
    return [[cell.strip().strip('`') for cell in line.strip('|').split('|')]
            for line in body.splitlines()[1:] if line.startswith('|')]


class MannequinDocsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = json.loads((FIXTURE / 'config.json').read_text())
        cls.bones = {b.get('chain', b.get('name')): b for b in cls.config['bones']}
        cls.hip = up(cls.bones['hip']['at'])
        cls.readme = (FIXTURE / 'README.md').read_text()
        cls.task = (ROOT / 'tasks/05-dance/TASK.md').read_text()
        cls.legs = {}
        for side in ('r', 'l'):
            chain = cls.bones['leg_' + side]
            joint, knee = map(up, chain['points'])
            target = up(cls.bones['foot_' + side + '_tgt']['at'])
            # Independently measure segments from the authored fixture points.
            # The writer's documented precision is six places for the child
            # offset and three for its length. No IK solution is duplicated.
            cls.legs[side] = (joint, target, round(math.dist(joint, knee), 6),
                              round(math.dist(knee, up(chain['tip'])), 3))

    def reachable(self, side, x=0, y=0, angle=0, wrong_pivot=False):
        joint, target, first, second = self.legs[side]
        offset = (0, 0) if wrong_pivot else tuple(a - b for a, b in zip(joint, self.hip))
        dx, dy = turn(offset, angle)
        moved = self.hip[0] + x + dx, self.hip[1] + y + dy
        return triangle_reaches(first, second, math.dist(moved, target))

    def ceiling(self, side, x):
        joint, target, first, second = self.legs[side]
        qx, qy = (a - b for a, b in zip(target, joint))
        return qy + math.sqrt((first + second) ** 2 - (qx - x) ** 2)

    def test_reach_assumptions_and_joint_offsets(self):
        self.assertEqual(self.bones['hip']['parent'], 'root')
        self.assertEqual(self.hip, (414, -623))
        for side, offset, q in [('r', (-40, 0), (-54, -485)), ('l', (40, 0), (53, -485))]:
            joint, target, _, _ = self.legs[side]
            self.assertEqual(tuple(a - b for a, b in zip(joint, self.hip)), offset)
            self.assertEqual(tuple(a - b for a, b in zip(target, joint)), q)
            self.assertEqual(self.bones['leg_' + side]['parent'], 'hip')
            self.assertEqual(self.bones['foot_' + side + '_tgt']['parent'], 'root')
            ik = next(c for c in self.config['constraints'] if c['name'] == 'leg_' + side + '_ik')
            self.assertEqual(ik['bones'], ['leg_' + side + '0', 'leg_' + side + '1'])
            self.assertEqual(ik['mix'], 1)
            self.assertEqual(ik.get('softness', 0), 0)
            self.assertFalse(ik.get('stretch', False))

    def test_documented_lengths_from_fixture_points(self):
        rows = table(self.readme, '| side | first link | second link | outer reach | inner reach |')
        self.assertEqual([r[0] for r in rows], ['right', 'left'])
        for row, side in zip(rows, ('r', 'l')):
            _, _, first, second = self.legs[side]
            for value, expected in zip(map(float, row[1:]), (first, second, first + second, abs(first - second))):
                self.assertAlmostEqual(value, expected, delta=1e-6)

    def test_documented_translation_bounds(self):
        rows = table(self.readme, '| hip x shift | greatest hip y shift near setup |')
        self.assertEqual([float(r[0]) for r in rows], [0, 10, -10])
        for x, y in rows:
            self.assertAlmostEqual(float(y), min(self.ceiling(s, float(x)) for s in self.legs), delta=1e-3)
        limits = [self.legs[s] for s in self.legs]
        lower = max(t[0] - j[0] - math.sqrt((a + b) ** 2 - (t[1] - j[1]) ** 2) for j, t, a, b in limits)
        upper = min(t[0] - j[0] + math.sqrt((a + b) ** 2 - (t[1] - j[1]) ** 2) for j, t, a, b in limits)
        lo, hi = map(float, re.search(r'\[(-?\d+\.\d+), (-?\d+\.\d+)\]', self.readme).groups())
        self.assertAlmostEqual(lo, lower, delta=1e-3)
        self.assertAlmostEqual(hi, upper, delta=1e-3)

    def test_normal_setup_and_dips(self):
        for x, y in [(0, 0), (0, -1), (10, -2), (-10, -2)]:
            with self.subTest(x=x, y=y):
                self.assertTrue(all(self.reachable(s, x, y) for s in self.legs))

    def test_defects_distinguish_both_legs_and_wrong_pivot(self):
        self.assertFalse(any(self.reachable(s, 0, 1) for s in self.legs))
        self.assertFalse(self.reachable('r', 10, 0))
        self.assertTrue(self.reachable('l', 10, 0))
        self.assertTrue(self.reachable('r', -10, 0))
        self.assertFalse(self.reachable('l', -10, 0))
        self.assertFalse(any(self.reachable(s, wrong_pivot=True) for s in self.legs))

    def test_outer_edges_and_tiny_positive_slack(self):
        for side, (joint, target, first, second) in self.legs.items():
            edge = self.ceiling(side, 0)
            self.assertGreater(edge, 0)
            self.assertLess(edge, 0.03)
            self.assertAlmostEqual(math.dist((joint[0], joint[1] + edge), target), first + second, places=9)
            self.assertTrue(self.reachable(side, 0, edge - 1e-3))
            self.assertFalse(self.reachable(side, 0, edge + 1e-3))

    def test_unequal_link_inner_and_outer_edges(self):
        # Exact synthetic lengths isolate annulus inclusion, independent of the fixture.
        for distance, expected in [(1.999, False), (2, True), (2.001, True), (4, True), (4.001, False)]:
            self.assertEqual(triangle_reaches(3, 1, distance), expected)

    def test_hip_rotation_moves_the_two_origins(self):
        self.assertTrue(self.reachable('r', angle=5))
        self.assertFalse(self.reachable('l', angle=5))
        self.assertFalse(self.reachable('r', angle=-5))
        self.assertTrue(self.reachable('l', angle=-5))
        self.assertIn('(R(theta)-I)b_s', self.readme)

    def test_local_setup_signs_and_relative_rotation(self):
        rows = table(self.readme, '| bone | local setup rotation (degrees) | a positive rotation delta |')
        documented = {r[0]: float(r[1]) for r in rows}
        for side in ('r', 'l'):
            chain = self.bones['sleeve_' + side]
            shoulder, elbow = map(up, chain['points'])
            wrist = up(chain['tip'])
            upper = math.degrees(math.atan2(elbow[1] - shoulder[1], elbow[0] - shoulder[0]))
            fore = math.degrees(math.atan2(wrist[1] - elbow[1], wrist[0] - elbow[0]))
            self.assertAlmostEqual(documented['sleeve_' + side + '1'], fore - upper, delta=1e-6)
            self.assertAlmostEqual(documented['hand_' + side], -fore, delta=1e-6)
            # Relative zero keeps the rest frame; absolute zero would lose it.
            self.assertNotAlmostEqual(documented['hand_' + side], 0)
            self.assertAlmostEqual(fore + documented['hand_' + side] + 90, 90, delta=1e-6)
        x, y = turn((1, 0), 90)
        self.assertAlmostEqual(x, 0)
        self.assertAlmostEqual(y, 1)
        self.assertAlmostEqual(up((x, y))[1], -1)  # opposite screen-y direction
        self.assertIn('add to the local setup rotation', self.readme)

    def test_timing_is_bound_to_seven_public_command_intervals(self):
        timing = self.task.split('## Timing\n', 1)[1].split('## Pass lines\n', 1)[0]
        # Provenance inputs belong to this repository test, not the examinee's
        # TASK links. Sparse sitting clones need not contain results/ at all.
        sources = {'claude-haiku-5-5': [3], 'claude-sonnet-5-5': [2, 3],
                   'claude-opus-5-5': [3, 5], 'claude-fable-5-1': [3, 5]}
        elapsed = []
        for model, steps in sources.items():
            path = ROOT / 'results' / model / ('2026-10-25-' + model) / '05-dance/transcript.md'
            text = path.read_text()
            for step in steps:
                block = next(b for b in text.split('## Step ')[1:] if b.startswith(str(step) + ' ('))
                argv = json.loads(re.search(r'^- argv: (.+)$', block, re.M)[1])
                self.assertEqual(argv[:2], ['python3', 'grade.py'])
                dates = [datetime.datetime.fromisoformat(re.search(r'^- ' + k + r': (.+)$', block, re.M)[1])
                         for k in ('start', 'end')]
                elapsed.append((dates[1] - dates[0]).total_seconds())
        self.assertEqual((len(elapsed), min(elapsed), max(elapsed)), (7, 106, 197))
        self.assertIn('seven command\nintervals of 106–197 seconds', timing)
        self.assertIn('historical shared-host observations', timing)
        self.assertEqual(re.findall(r'\]\(([^)]+)\)', timing),
                         ['https://github.com/rig-c/exam/issues/58#issuecomment-6398236249'])
        self.assertNotIn('results/', timing)
        self.assertIn("does not expand the exam's permitted reading", timing)

    def test_ankle_reading_is_a_height_band_not_a_vertex_count(self):
        self.assertIn('vertices in the lowest 4% of its height in **frame 0**', self.readme)
        self.assertNotIn('lowest 4% of its vertices', self.readme)

    def test_pages_ci_runs_the_documentation_contract(self):
        workflow = (ROOT / '.github/workflows/pages.yml').read_text()
        self.assertIn("python3 -B -m unittest discover -s tools -p 'test_mannequin_docs.py' -v", workflow)


if __name__ == '__main__':
    unittest.main()
