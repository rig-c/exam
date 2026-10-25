"""Check the examinee summary without displaying filed results, even on failure."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import warnings


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('exam_results', ROOT / 'results.py')
results = importlib.util.module_from_spec(spec)
spec.loader.exec_module(results)


class SummaryTests(unittest.TestCase):
    def test_only_independent_sittings_are_counted(self):
        records = [{'who': {'counts': count}, 'tasks': {}}
                   for count in ('independent', 'independent, fresh', 'assisted', 'void', '')]
        self.assertTrue(results.readme_block(records) ==
                        '**2 independent sitting(s) so far.**\n\n[Full results](results/README.md).',
                        'summary must contain only the sitting count and full-results link')

    def test_empty_sittings(self):
        self.assertTrue(results.readme_block([]) ==
                        '**0 independent sitting(s) so far.**\n\n[Full results](results/README.md).',
                        'empty summary must retain a zero count and link')

    def test_task_and_identity_details_cannot_enter_summary(self):
        record = {'who': {'counts': 'independent', 'model': 'synthetic-model'},
                  'name': 'synthetic-run', 'tasks': {'synthetic-task': {
                      'passed': 0, 'of': 1, 'lines': {'synthetic-private-line': {'pass': False}}}}}
        summary = results.readme_block([record])
        self.assertTrue(summary == results.readme_block([{'who': record['who']}]),
                        'summary must not depend on task cells, scores or identities')


class FixtureTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'tasks/01-build').mkdir(parents=True)
        run = self.root / 'results/synthetic/2000-01-01-synthetic'
        (run / '01-build').mkdir(parents=True)
        (run / 'who.json').write_text(json.dumps({'counts': 'independent', 'model': 'synthetic'}))
        (run / '01-build/result.json').write_text(json.dumps({
            'passed': 0, 'of': 1, 'lines': {'synthetic-private-line': {'pass': False}},
            'versions': {}, 'minutes': 1}))
        (self.root / 'results.py').write_bytes((ROOT / 'results.py').read_bytes())
        self.before = ('before\n<!-- results:start — generated; do not edit -->\n'
                       'obsolete\n<!-- results:end -->\nafter\n')
        (self.root / 'README.md').write_text(self.before)

    def command(self, *args):
        return subprocess.run([sys.executable, '-B', str(self.root / 'results.py'), *args],
                              cwd=self.root, capture_output=True)

    def test_generate_check_preserves_markers_and_surroundings(self):
        stale = self.command('--check')
        self.assertTrue(stale.returncode == 1, 'stale fixture must fail check')
        self.assertTrue((self.root / 'README.md').read_text() == self.before,
                        'check must not write')
        self.assertTrue(self.command().returncode == 0, 'generation must succeed')
        readme = (self.root / 'README.md').read_text()
        self.assertTrue(readme == self.before.replace('obsolete', results.readme_block([
            {'who': {'counts': 'independent'}}])), 'generation must replace only the marker body')
        self.assertTrue(self.command('--check').returncode == 0, 'generated pages must be current')
        page = (self.root / 'results/README.md').read_bytes()
        self.assertTrue(b'synthetic-private-line' in page and b'| model that did the work |' in page,
                        'full results must retain cells and failure details')
        self.assertTrue('synthetic-private-line' not in readme, 'summary must not reveal grade names')
        self.assertTrue(self.command().returncode == 0, 'regeneration must succeed')
        self.assertTrue((self.root / 'results/README.md').read_bytes() == page,
                        'regeneration must preserve full-table bytes')

    def test_reembedded_old_table_is_rejected_and_repaired(self):
        self.assertTrue(self.command().returncode == 0, 'fixture generation must succeed')
        with patch.object(results, 'ROOT', str(self.root)), patch.object(results, 'TASKS', ['01-build']):
            with warnings.catch_warnings():
                warnings.simplefilter('ignore', ResourceWarning)
                old_table = '\n'.join(results.tables(results.runs(), '', False))
        readme = self.root / 'README.md'
        clean = readme.read_bytes()
        readme.write_text(self.before.replace('obsolete', old_table))
        planted = readme.read_bytes()
        self.assertTrue(self.command('--check').returncode == 1, 'old-table plant must fail check')
        self.assertTrue(readme.read_bytes() == planted, 'failed check must preserve planted input')
        self.assertTrue(self.command().returncode == 0, 'generator must remove the old-table plant')
        self.assertTrue(readme.read_bytes() == clean, 'repair must restore the summary exactly')
        self.assertTrue(self.command('--check').returncode == 0, 'repaired pages must be current')


class FiledResultsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', ResourceWarning)
            cls.records = results.runs()

    def test_no_filed_grade_name_anywhere_in_readme(self):
        names = {name for run in self.records for task in run['tasks'].values()
                 for name in task.get('lines', {})}
        readme = (ROOT / 'README.md').read_text()
        self.assertTrue(bool(names), 'grade-name control must not be vacuous')
        self.assertTrue(not any(name in readme for name in names),
                        'README contains a filed grade name (details deliberately withheld)')

    def test_full_results_page_is_preserved_and_current(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', ResourceWarning)
            expected = results.results_page(self.records).encode()
        self.assertTrue((ROOT / 'results/README.md').read_bytes() == expected,
                        'full results page must remain exactly generated')

    def test_check_is_current_without_writing(self):
        paths = [ROOT / 'README.md', ROOT / 'results/README.md']
        before = [(p.read_bytes(), p.stat().st_mtime_ns) for p in paths]
        with warnings.catch_warnings(), patch.object(sys, 'argv', ['results.py', '--check']):
            warnings.simplefilter('ignore', ResourceWarning)
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                try:
                    results.main()
                except SystemExit:
                    self.fail('filed pages are stale (details deliberately withheld)')
        self.assertTrue(before == [(p.read_bytes(), p.stat().st_mtime_ns) for p in paths],
                        'check must preserve page bytes and timestamps')


if __name__ == '__main__':
    unittest.main()
