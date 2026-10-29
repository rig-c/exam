"""Round 6 routing and provenance; no answer or calibrated measurements."""
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest
import tempfile
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
TASK = ROOT / 'tasks/03-correct'

class ActivationTests(unittest.TestCase):
    def test_draft_and_text_promoted_together(self):
        manifest = json.loads((TASK / 'edition.json').read_text())
        self.assertEqual(manifest['edition'], 'basic-round6')
        self.assertEqual(manifest['draft'], 'inputs/draft.json')
        self.assertEqual(hashlib.sha256((TASK / manifest['draft']).read_bytes()).hexdigest(), manifest['draft_sha256'])
        self.assertEqual((TASK / manifest['draft']).read_bytes(), (ROOT / 'next-repin/03-correct/inputs/draft.json').read_bytes())
        self.assertIn('inputs/draft.json', (TASK / 'TASK.md').read_text())
        self.assertIn('| **Still moves** | over the idle, the back hair travels at least 23 rig px against the head |',
                      (TASK / 'TASK.md').read_text())
        self.assertTrue((TASK / 'TASK-round5.md').is_file())
        expected = {str(p.relative_to(TASK / 'inputs')): hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in (TASK / 'inputs').rglob('*') if p.is_file() and p.name != 'draft.json'}
        self.assertEqual(manifest['source_sha256'], expected)
        pins = json.loads((ROOT / 'package.json').read_text())['devDependencies']
        self.assertEqual(manifest['packages'], pins)

    def test_grader_provenance_and_historical_absence(self):
        spec = importlib.util.spec_from_file_location('activation_grade', ROOT / 'grade.py')
        grade = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(grade)
        self.assertEqual(grade.task_edition('03-correct'), json.loads((TASK / 'edition.json').read_text()))
        self.assertIsNone(grade.task_edition('01-build'))
        self.assertEqual(grade.STILL_MOVES, 23)
        self.assertEqual(grade.KEPT_MESHES, 8)
        # Historical JSON stays readable without inventing a new edition for it.
        records = [json.loads(p.read_text()) for p in (ROOT / 'results').glob('*/2026-10-25-*/03-correct/result.json')]
        self.assertTrue(records)
        self.assertTrue(all('edition' not in r for r in records))
        self.assertIn('STILL_MOVES = 23        # task 03: minimum back-hair vertex travel relative to the head over the idle, at FPS',
                      (ROOT / 'grade.py').read_text())

    def test_changed_source_cannot_keep_sealed_provenance(self):
        spec = importlib.util.spec_from_file_location('seal_grade', ROOT / 'grade.py')
        grade = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(grade)
        with tempfile.TemporaryDirectory() as tmp:
            task = Path(tmp) / 'tasks/03-correct'
            (task / 'inputs').mkdir(parents=True)
            (task / 'inputs/draft.json').write_bytes(b'{}')
            (task / 'inputs/painting.png').write_bytes(b'original')
            manifest = {'edition': 'synthetic', 'draft': 'inputs/draft.json',
                        'draft_sha256': hashlib.sha256(b'{}').hexdigest(),
                        'source_sha256': {'painting.png': hashlib.sha256(b'original').hexdigest()}}
            (task / 'edition.json').write_text(json.dumps(manifest))
            with patch.object(grade, 'ROOT', tmp):
                self.assertEqual(grade.task_edition('03-correct'), manifest)
                (task / 'inputs/painting.png').write_bytes(b'changed')
                with self.assertRaisesRegex(ValueError, 'task edition input changed: inputs/painting.png'):
                    grade.task_edition('03-correct')
                (task / 'inputs/painting.png').write_bytes(b'original')
                (task / 'inputs/draft.json').write_bytes(b'{"changed":true}')
                with self.assertRaisesRegex(ValueError, 'task edition input changed: inputs/draft.json'):
                    grade.task_edition('03-correct')

if __name__ == '__main__': unittest.main()
