"""Named plants exercise the real README check on disposable synthetic files."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from check_readme import ROOT, WORD_CAP


class ReadmeCheckTests(unittest.TestCase):
    def check(self, text, refusal=None):
        with tempfile.TemporaryDirectory(prefix='readme-plant-') as tmp:
            path = Path(tmp) / 'README.md'
            path.write_text(text, encoding='utf-8')
            result = subprocess.run(
                [sys.executable, '-B', str(ROOT / 'tools/check_readme.py'), str(path)],
                capture_output=True, text=True)
            self.assertEqual(result.returncode, 1 if refusal else 0, result.stdout + result.stderr)
            self.assertIn(refusal or 'README_OK', result.stdout)
            self.assertEqual(path.read_text(encoding='utf-8'), text, 'check must not write')
            if refusal:
                print(f'PLANT {self._testMethodName}: exit={result.returncode}; '
                      f'{result.stdout.strip()}')

    def test_normal_rules_and_prose_date(self):
        self.check('# Exam\n\n## Rules\n\nRuling, 2026-10-25: keep a journal.\n')

    def test_exact_word_cap_is_allowed(self):
        self.check('word ' * WORD_CAP)

    def test_plant_word_cap_plus_one(self):
        self.check('word ' * (WORD_CAP + 1), 'README_WORD_CAP')

    def test_plant_unlisted_h2(self):
        self.check('# Exam\n\n## Version history\n', 'README_HEADING')

    def test_plant_indented_h2_with_closing_hashes(self):
        self.check('   ## Version history ##\n', 'README_HEADING')

    def test_plant_empty_h2(self):
        self.check('##\n', 'README_HEADING')

    def test_plant_measured_on(self):
        self.check('Measured on 2026-10-30: 100 bytes.\n', 'README_DATED_PHRASE')

    def test_plant_read_on_wrapped(self):
        self.check('Read on\n2026-10-30: 100 bytes.\n', 'README_DATED_PHRASE')

    def test_plant_measured_phrase_inside_fence(self):
        self.check('```text\nmeasured on 2026-10-30\n```\n', 'README_DATED_PHRASE')

    def test_plant_table_date(self):
        self.check('| host | date |\n| --- | --- |\n| sample | 2026-10-30 |\n',
                   'README_TABLE_DATE')

    def test_plant_table_date_without_outer_pipes(self):
        self.check('host | date\n--- | ---\nsample | 2026-10-30\n', 'README_TABLE_DATE')

    def test_fenced_examples_are_not_headings_or_tables(self):
        self.check('## Layout ##\n\n```md\n## Example\n'
                   '| date | 2026-10-30 |\n```\n'
                   '~~~md\n## Example\n~~~\n### Manual build from clone root\n')

    def test_repository_readme_and_round_history_stub(self):
        self.check((ROOT / 'README.md').read_text(encoding='utf-8'))
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        stub = readme.split('## What is in a round\n', 1)[1].split('\n## ', 1)[0]
        self.assertIn('https://github.com/rig-c/exam/blob/main/ROUNDS.md#what-is-in-a-round', stub)
        self.assertIn('## What is in a round\n', (ROOT / 'ROUNDS.md').read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
