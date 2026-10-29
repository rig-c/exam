"""Static, inactive candidate inputs only; no solution or build calibration."""
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / 'next-repin' / '03-correct'


class NextRepinFixtureTests(unittest.TestCase):
    def test_static_draft_hash(self):
        manifest = json.loads((CANDIDATE / 'manifest.json').read_text())
        self.assertEqual(manifest['spec'], 'rig-exam-next-repin/1')
        self.assertIs(manifest['active'], False)
        self.assertEqual(manifest['draft'], 'inputs/draft.json')
        draft = CANDIDATE / manifest['draft']
        self.assertFalse(draft.is_symlink())
        self.assertEqual(hashlib.sha256(draft.read_bytes()).hexdigest(), manifest['draft_sha256'])

    def test_config_is_self_contained(self):
        config = json.loads((CANDIDATE / 'inputs' / 'draft.json').read_text())
        for key in ('key', 'seethrough', 'assemble', 'bones', 'meshes', 'regions', 'motion'):
            self.assertIn(key, config)
        self.assertNotIn('animations_from', config['motion'])
        # No external config-relative assets or generated proposal are needed.
        import sys
        sys.path.insert(0, str(ROOT))
        import grade
        self.assertEqual(grade.named_paths(config, str(CANDIDATE)), [])

    def test_inactive_linkage(self):
        manifest = json.loads((CANDIDATE / 'manifest.json').read_text())
        self.assertEqual(manifest['source_inputs'], 'tasks/03-correct/inputs')
        self.assertTrue((ROOT / manifest['source_inputs'] / 'painting.png').is_file())
        self.assertEqual(manifest['task_text'], 'TASK.md')
        self.assertTrue((CANDIDATE / manifest['task_text']).is_file())
        for name in ('grade.py', 'PROMPT.md', 'tasks/03-correct/TASK.md'):
            self.assertNotIn('next-repin/', (ROOT / name).read_text())
        self.assertFalse((ROOT / 'tasks/03-correct/fixture.json').exists())
        self.assertEqual((ROOT / 'tasks/03-correct/inputs/draft.json').read_bytes(),
                         (CANDIDATE / 'inputs/draft.json').read_bytes())

    def test_no_private_controls_in_candidate(self):
        self.assertEqual(sorted(str(p.relative_to(CANDIDATE)) for p in CANDIDATE.rglob('*') if p.is_file()),
                         ['TASK.md', 'inputs/draft.json', 'manifest.json'])


if __name__ == '__main__':
    unittest.main()
