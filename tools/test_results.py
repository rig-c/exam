"""Check the examinee summary without displaying filed results, even on failure."""
import contextlib
import importlib.util
import io
import json
import os
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
                      'passed': 0, 'of': 1, 'lines': {'synthetic_private_line': {'pass': False}}}}}
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
            'passed': 0, 'of': 1, 'lines': {'synthetic_private_line': {'pass': False}},
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
        self.assertTrue(b'synthetic_private_line' in page and b'| model that did the work |' in page,
                        'full results must retain cells and failure details')
        self.assertTrue('synthetic_private_line' not in readme, 'summary must not reveal grade names')
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

    def test_readme_summary_and_identifier_boundary(self):
        # Single-word grade names can coincide with ordinary English prose.
        names = {name for run in self.records for task in run['tasks'].values()
                 for name in task.get('lines', {}) if '_' in name}
        readme = (ROOT / 'README.md').read_bytes()
        self.assertTrue(bool(self.records), 'sitting control must not be vacuous')
        count = sum(run['who'].get('counts', '').startswith('independent')
                    for run in self.records)
        self.assertTrue(count > 0, 'independent sitting control must not be vacuous')
        self.assertTrue(bool(names), 'identifier control must not be vacuous')
        self.assertTrue(not any(name.encode() in readme for name in names),
                        'README contains a filed identifier (details deliberately withheld)')
        start, end = results.START.encode(), results.END.encode()
        self.assertTrue(readme.count(start) == 1 and readme.count(end) == 1,
                        'README must have exactly one generated region')
        a = readme.index(start)
        a_end = readme.index(b'-->', a) + 3
        b = readme.index(end, a_end)
        expected = (f'\n**{count} independent sitting(s) so far.**\n\n'
                    '[Full results](results/README.md).\n').encode()
        self.assertTrue(readme[a_end:b] == expected,
                        'README region must equal only the sitting summary and link')

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


class JournalTests(unittest.TestCase):
    """Exercise the real journal CLI on copied code and synthetic executables only."""

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.scratch = Path(self.temp.name)
        self.clone = self.scratch / 'clone with spaces'
        self.script = self.clone / 'tools/journal.py'
        self.script.parent.mkdir(parents=True)
        self.script.write_bytes((ROOT / 'tools/journal.py').read_bytes())
        self.bin = self.clone / 'node_modules/.bin'
        self.inherited = self.scratch / 'inherited bin'
        self.inherited.mkdir()
        self.run_dir = self.scratch / 'run'
        self.env = dict(os.environ, PATH=str(self.inherited), EXAM_TEST_MARKER='synthetic-value')

    def command(self, *args, expected=0, cwd=None, env=None):
        result = subprocess.run([sys.executable, '-B', str(self.script), '--run', str(self.run_dir), *args],
                                cwd=cwd or self.clone, env=self.env if env is None else env,
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, expected, 'synthetic journal call failed: ' + result.stderr)
        return result

    def open_entry(self):
        self.command('start')
        self.command('open', '--read', 'synthetic instructions', '--expect', 'synthetic fixture output',
                     '--chose', 'run the fixture instead of a package build')

    def executable(self, directory, name='exam-probe', label='clone'):
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / name
        path.write_text(f'#!{sys.executable}\n'
                        'import json, os, sys\n'
                        f'print(json.dumps({{"label": {label!r}, "args": sys.argv[1:], '
                        '"marker": os.environ.get("EXAM_TEST_MARKER"), '
                        '"path": os.environ.get("PATH"), "cwd": os.getcwd()}))\n')
        path.chmod(0o700)
        return path

    def close_and_verify(self, output):
        self.command('close', '--happened', output.strip())
        self.command('end', '--guessed', 'none', '--missing', 'none')
        self.command('finish')
        result = self.command('verify')
        self.assertEqual(result.stdout, 'journal: chain intact, 1 entries, 0 WTF\n')

    def test_bare_clone_command_without_bin_on_inherited_path(self):
        self.executable(self.bin)
        self.open_entry()
        result = self.command('run', '--', 'exam-probe')
        actual = json.loads(result.stdout)
        self.assertEqual(actual['label'], 'clone')
        self.assertEqual(actual['path'], str(self.bin) + os.pathsep + str(self.inherited))
        self.assertEqual(actual['marker'], 'synthetic-value')
        self.close_and_verify(result.stdout)

    def test_clone_bin_precedes_inherited_namesake(self):
        self.executable(self.bin)
        self.executable(self.inherited, label='inherited')
        self.open_entry()
        self.assertEqual(json.loads(self.command('run', '--', 'exam-probe').stdout)['label'], 'clone')

    def test_absent_clone_bin_preserves_inherited_lookup(self):
        self.executable(self.inherited, label='inherited')
        self.assertFalse(self.bin.exists())
        self.open_entry()
        self.assertEqual(json.loads(self.command('run', '--', 'exam-probe').stdout)['label'], 'inherited')

    def test_unset_path_uses_system_default_after_clone_bin(self):
        self.executable(self.bin)
        env = self.env.copy()
        del env['PATH']
        self.open_entry()
        actual = json.loads(self.command('run', '--', 'exam-probe', env=env).stdout)
        self.assertEqual(actual['path'], str(self.bin) + os.pathsep + os.defpath)

    def test_explicit_empty_path_is_preserved_as_tail(self):
        self.executable(self.bin)
        self.open_entry()
        actual = json.loads(self.command('run', '--', 'exam-probe', env=dict(self.env, PATH='')).stdout)
        self.assertEqual(actual['path'], str(self.bin) + os.pathsep)

    def test_bin_is_anchored_to_clone_and_cwd_is_preserved(self):
        self.executable(self.bin)
        nested = self.clone / 'nested directory'
        self.executable(nested / 'node_modules/.bin', label='cwd-decoy')
        self.open_entry()
        actual = json.loads(self.command('run', '--', 'exam-probe', cwd=nested).stdout)
        self.assertEqual(actual['label'], 'clone')
        self.assertEqual(Path(actual['cwd']).resolve(), nested.resolve())

    def test_child_environment_is_a_copy_without_parent_mutation(self):
        spec = importlib.util.spec_from_file_location('synthetic_journal', self.script)
        journal = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(journal)
        with patch.dict(os.environ, {'PATH': 'synthetic-tail', 'EXAM_TEST_MARKER': 'synthetic-value'}, clear=True):
            before = dict(os.environ)
            child = journal.command_environment()
            self.assertEqual(dict(os.environ), before)
            self.assertEqual(child, dict(before, PATH=str(self.bin) + os.pathsep + 'synthetic-tail'))
            child['EXAM_TEST_MARKER'] = 'changed-child'
            self.assertEqual(dict(os.environ), before)

    def test_shell_metacharacters_and_spaces_are_literal_arguments(self):
        self.executable(self.bin)
        marker = self.scratch / 'must-not-exist'
        arguments = ['two words', '; touch ' + str(marker), '$(touch ' + str(marker) + ')',
                     'grade.py', 'python3 -c "print(123)"', '| cat', '> output']
        self.open_entry()
        result = self.command('run', '--', 'exam-probe', *arguments)
        self.assertEqual(json.loads(result.stdout)['args'], arguments)
        self.assertFalse(marker.exists())
        self.close_and_verify(result.stdout)

    def test_explicit_shell_works_with_child_path(self):
        self.executable(self.bin)
        self.open_entry()
        result = self.command('run', '--', '/bin/sh', '-c', 'exam-probe')
        self.assertEqual(json.loads(result.stdout)['label'], 'clone')
        self.close_and_verify(result.stdout)

    def test_missing_command_returns_127_and_keeps_a_valid_step(self):
        self.open_entry()
        result = self.command('run', '--', 'exam-missing-command', expected=127)
        self.assertIn('could not start exam-missing-command', result.stdout)
        self.close_and_verify(result.stdout)

    def test_nonzero_exit_is_preserved(self):
        self.open_entry()
        result = self.command('run', '--', sys.executable, '-c',
                              'print("synthetic fixture failed"); raise SystemExit(7)', expected=7)
        self.close_and_verify(result.stdout)
        recs = [json.loads(line) for line in (self.run_dir / '.journal/chain.jsonl').read_text().splitlines()]
        self.assertEqual(next(r['exit'] for r in recs if r['kind'] == 'step'), 7)

    def test_refused_run_does_not_execute(self):
        marker = self.scratch / 'must-not-exist'
        result = self.command('run', '--', sys.executable, '-c',
                              'from pathlib import Path; Path(' + repr(str(marker)) + ').touch()', expected=2)
        self.assertIn('no entry is open', result.stderr)
        self.assertFalse(marker.exists())

    def test_journal_transcript_and_step_output_tampering_is_rejected(self):
        self.open_entry()
        result = self.command('run', '--', sys.executable, '-c', 'print("synthetic fixture output")')
        self.close_and_verify(result.stdout)
        for name in ('journal.md', 'transcript.md', '.journal/step-1.out'):
            with self.subTest(file=name):
                path = self.run_dir / name
                original = path.read_bytes()
                try:
                    path.write_bytes(original + b'changed\n')
                    checked = self.command('verify', expected=1)
                    self.assertIn('first broken link', checked.stdout)
                finally:
                    path.write_bytes(original)
        self.command('verify')

    def test_no_chain_is_not_kept(self):
        self.assertEqual(self.command('verify', expected=1).stdout, 'journal: not kept (no chain)\n')

    def test_chain_does_not_claim_to_detect_an_unrecorded_grader(self):
        # Synthetic grade.py only prints; no exam result or real grader is touched.
        grader = self.clone / 'grade.py'
        grader.write_text('print("synthetic grader output")\n')
        direct = [sys.executable, '-B', str(grader)]
        subprocess.run(direct, check=True, capture_output=True)  # before start, no entry
        self.open_entry()
        result = self.command('run', '--', *direct)  # wrapped
        self.close_and_verify(result.stdout)
        subprocess.run(direct, check=True, capture_output=True)  # after finish, no entry
        checked = self.command('verify')
        self.assertEqual(checked.stdout, 'journal: chain intact, 1 entries, 0 WTF\n')
        transcript = (self.run_dir / 'transcript.md').read_text()
        self.assertEqual(transcript.count('- argv:'), 1)
        self.assertEqual(transcript.count('## Step '), 1)


if __name__ == '__main__':
    unittest.main()
