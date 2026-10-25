"""Targeted profile splice/count/workflow contracts; never runs Git or writes remotely."""
from pathlib import Path
import subprocess
import sys
import tempfile
import textwrap
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import warnings

import profile_results as profile
import yaml


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / 'tools/fixtures/profile-before-summary.md'
SCRATCH = Path(tempfile.gettempdir())


class SpliceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.before = FIXTURE.read_bytes()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', ResourceWarning)  # unchanged upstream readers use open()
            cls.basic, cls.advanced, cls.counts = profile.generated()
        cls.after = profile.splice(cls.before, cls.basic, cls.advanced, cls.counts)

    def splice(self, data):
        return profile.splice(data, self.basic, self.advanced, self.counts)

    def test_both_tables_equal_the_real_clis_including_final_newline(self):
        for name, script in (('exam', 'results.py'), ('exam-advanced', 'advanced/results.py')):
            with self.subTest(name=name):
                r = profile.region(self.after, name)
                actual = subprocess.check_output([sys.executable, '-B', str(ROOT / script), '--profile'])
                self.assertEqual(self.after[r[1]:r[2]], actual)

    def test_live_legacy_paragraphs_migrate_without_losing_editorial_content(self):
        self.assertEqual(self.after.count(b'<!-- exam-summary:start'), 1)
        self.assertEqual(self.after.count(b'<!-- exam-summary:end'), 1)
        self.assertNotIn(b'Eleven models have sat it', self.after)
        self.assertNotIn(b'Six models have sat all three rounds', self.after)
        # Everything before the first table and after the last is byte preserved.
        a, b = profile.region(self.before, 'exam'), profile.region(self.after, 'exam')
        self.assertEqual(self.before[:a[1]], self.after[:b[1]])
        a, b = profile.region(self.before, 'exam-advanced'), profile.region(self.after, 'exam-advanced')
        self.assertEqual(self.before[a[2]:], self.after[b[2]:])
        # These two prose fragments share paragraphs with the retired sentences.
        cta = self.before.split(b'**Sit it with yours:**', 1)[1].split(b'\n\n', 1)[0]
        intro = self.before.split(b'**Advanced.**', 1)[1].split(b' Six models', 1)[0]
        self.assertIn(b'**Sit it with yours:**' + cta, self.after)
        self.assertIn(b'**Advanced.**' + intro, self.after)

    def test_previous_profile_before_manual_sync_is_supported(self):
        old = self.before.replace(
            b"Eleven models have sat it, from each vendor's lighter tier to its heaviest; nine passed every line, "
            b'and the two that missed one are on the page with the line they missed.',
            b"Every line passed, and the three models named are each their vendor's lighter tier.",
        ).replace(b'Six models have sat all three rounds', b'Five models have sat all three rounds')
        self.assertNotIn(b'Every line passed,', self.splice(old))

    def test_wrapped_legacy_paragraphs(self):
        data = self.before.decode()
        paragraphs = data.split('\n\n')
        data = '\n\n'.join(textwrap.fill(p, width=67) if p.startswith(('Eleven models', '**Advanced.**'))
                           else p for p in paragraphs).encode()
        result = self.splice(data)
        self.assertNotIn(b'Eleven models', result)
        self.assertIn(b'**Sit it with', result)
        self.assertEqual(self.splice(result), result)

    def test_extra_prose_in_the_same_paragraph_is_preserved(self):
        extra = b'An editorial sentence the automation does not own. '
        data = self.before.replace(b'Eleven models', extra + b'Eleven models')
        data = data.replace(b'Six models', extra + b'Six models')
        result = self.splice(data)
        self.assertEqual(result.count(extra), 2)

    def test_unknown_or_duplicate_legacy_prose_is_refused(self):
        for data in (
            self.before.replace(b'Eleven models have sat it', b'Unrecognised counts here'),
            self.before.replace(b'Six models have sat all three rounds', b'Unrecognised rounds here'),
            self.before.replace(b'Eleven models', b'Eleven models', 1).replace(
                b'<!-- exam-advanced:start',
                b"Every line passed, and the three models named are each their vendor's lighter tier. "
                b'**Sit it with yours:** duplicate\n<!-- exam-advanced:start'),
        ):
            with self.subTest(data=data[:30]):
                with self.assertRaises(profile.ProfileError):
                    self.splice(data)

    def test_missing_duplicate_and_reversed_markers_refuse(self):
        for name in ('exam', 'exam-advanced', 'exam-summary'):
            for kind in ('start', 'end'):
                token = f'<!-- {name}:{kind}'.encode()
                for data in (self.after.replace(token, b'<!-- removed', 1),
                             self.after + b'\n' + token + b' -->\n'):
                    with self.subTest(name=name, kind=kind):
                        with self.assertRaises(profile.ProfileError):
                            self.splice(data)
            data = self.after.replace(f'{name}:start'.encode(), b'SWAP', 1)
            data = data.replace(f'{name}:end'.encode(), f'{name}:start'.encode(), 1)
            data = data.replace(b'SWAP', f'{name}:end'.encode(), 1)
            with self.assertRaises(profile.ProfileError):
                self.splice(data)

    def test_inline_malformed_and_overlapping_pairs_refuse(self):
        cases = [self.after.replace(b'<!-- exam:end -->', b'inline <!-- exam:end -->'),
                 self.after.replace(b'<!-- exam:end -->', b'<!-- exam:end'),
                 self.after.replace(b'<!-- exam:end -->\n', b'') + b'\n<!-- exam:end -->\n']
        for data in cases:
            with self.subTest(data=data[-30:]):
                with self.assertRaises(profile.ProfileError):
                    self.splice(data)

    def test_crlf_and_unicode_outside_blocks_are_preserved(self):
        data = self.before.replace(b'\n', b'\r\n')
        result = self.splice(data)
        a, b = profile.region(data, 'exam'), profile.region(result, 'exam')
        self.assertEqual(data[:a[1]], result[:b[1]])
        self.assertEqual(result[b[1]:b[2]], self.basic)  # the CLI emits LF
        self.assertEqual(self.splice(result), result)

    def test_changing_counts_or_tables_changes_only_owned_blocks(self):
        new = profile.splice(self.after, self.basic + b'\n', self.advanced, b'changed summary\n')
        self.assertIn(b'changed summary\n<!-- exam-summary:end', new)
        # Replacing them again exactly restores the prior README.
        self.assertEqual(self.splice(new), self.after)

    def test_update_noop_never_writes_and_invalid_input_is_atomic(self):
        with tempfile.TemporaryDirectory(dir=SCRATCH) as tmp:
            path = Path(tmp) / 'README.md'
            path.write_bytes(self.after)
            with patch.object(profile, 'generated', return_value=(self.basic, self.advanced, self.counts)):
                with patch.object(Path, 'write_bytes', side_effect=AssertionError('unexpected write')):
                    self.assertFalse(profile.update(path))
                bad = self.before.replace(b'<!-- exam:end -->', b'')
                path.write_bytes(bad)
                with self.assertRaises(profile.ProfileError):
                    profile.update(path)
                self.assertEqual(path.read_bytes(), bad)


class CountTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.basic_reader = profile.generator(ROOT / 'results.py')
        cls.advanced_reader = profile.generator(ROOT / 'advanced/results.py')

    def counts(self, basic=(), advanced=()):
        b = SimpleNamespace(runs=lambda: basic, counted=self.basic_reader.counted)
        a = SimpleNamespace(sittings=lambda: advanced, by_model=self.advanced_reader.by_model,
                            ROUNDS=self.advanced_reader.ROUNDS)
        return profile.summary(b, a).decode()

    def run_record(self, group, passed=1, of=1, counts='independent', **task):
        return dict(group=group, who=dict(counts=counts, short='same display name'),
                    tasks={'01-build': dict(passed=passed, of=of, **task)})

    def sitting(self, model, rnd, status='PASS', shin=('PASS', 0.5)):
        return dict(model=model, round=rnd, shin=shin,
                    grade=dict(passed=int(status == 'PASS'), of=1, rows={'row': status}))

    def test_basic_group_identity_counted_prefix_and_all_sittings(self):
        records = [self.run_record('a'), self.run_record('a', counts='independent, fresh'),
                   self.run_record('b'), self.run_record('b', passed=0),
                   self.run_record('void', counts='void'), self.run_record('assisted', counts='assisted')]
        s = self.counts(basic=records)
        self.assertIn('Basic:** 2 models, 1 passed every graded line', s)
        self.assertIn('(4 sittings)', s)

    def test_basic_empty_and_zero_denominator_do_not_pass(self):
        empty = self.run_record('empty'); empty['tasks'] = {}
        s = self.counts(basic=[empty, self.run_record('zero', passed=0, of=0)])
        self.assertIn('Basic:** 2 models, 0 passed', s)
        self.assertIn('Basic:** 0 models, 0 passed', self.counts())

    def test_basic_separate_round5_painting_still_has_graded_lines(self):
        record = self.run_record('new-painting', passed=0, painting=self.basic_reader.NEW_PAINTING)
        self.assertIn('Basic:** 1 models, 0 passed', self.counts(basic=[record]))

    def test_advanced_uses_selected_sittings_complete_rounds_and_ignores_whatif(self):
        ss = [self.sitting('a', r, shin=('FAIL', 0.1)) for r in ('R1', 'R2', 'R3')]
        ss += [self.sitting('b', 'R1'), self.sitting('b', 'R2', 'SKIP')]
        # by_model replaces the earlier failed R1 with the later passing R1.
        ss.insert(0, self.sitting('a', 'R1', 'FAIL'))
        s = self.counts(advanced=ss)
        self.assertIn('Advanced:** 2 models, 1 with all three rounds; 1 passed', s)
        self.assertIn('1 of 5 displayed round cells did not pass every row', s)

    def test_advanced_fail_and_skip_prevent_all_round_pass(self):
        for status in ('FAIL', 'SKIP'):
            ss = [self.sitting('a', r, status if r == 'R2' else 'PASS') for r in ('R1', 'R2', 'R3')]
            s = self.counts(advanced=ss)
            self.assertIn('1 with all three rounds; 0 passed', s)
            self.assertIn('1 of 3 displayed round cells', s)


class CliTests(unittest.TestCase):
    def command(self, *args):
        return subprocess.run([sys.executable, '-B', str(ROOT / 'tools/profile_results.py'), *map(str, args)],
                              cwd=ROOT, capture_output=True)

    def test_cli_updates_then_preserves_bytes_and_mtime_on_noop(self):
        with tempfile.TemporaryDirectory(dir=SCRATCH) as tmp:
            path = Path(tmp) / 'README.md'
            path.write_bytes(FIXTURE.read_bytes())
            first = self.command(path)
            self.assertEqual((first.returncode, first.stdout), (0, b'profile_results: updated\n'))
            frozen = path.read_bytes(), path.stat().st_mtime_ns
            second = self.command(path)
            self.assertEqual((second.returncode, second.stdout), (0, b'profile_results: unchanged\n'))
            self.assertEqual((path.read_bytes(), path.stat().st_mtime_ns), frozen)
            for name, script in (('exam', 'results.py'), ('exam-advanced', 'advanced/results.py')):
                r = profile.region(path.read_bytes(), name)
                expected = subprocess.check_output([sys.executable, '-B', str(ROOT / script), '--profile'])
                self.assertEqual(path.read_bytes()[r[1]:r[2]], expected)

    def test_cli_bad_marker_exits_one_without_writing(self):
        with tempfile.TemporaryDirectory(dir=SCRATCH) as tmp:
            path = Path(tmp) / 'README.md'
            bad = FIXTURE.read_bytes().replace(b'<!-- exam:end -->', b'')
            path.write_bytes(bad)
            result = self.command(path)
            self.assertEqual(result.returncode, 1)
            self.assertIn(b'need exactly one start then one end marker', result.stderr)
            self.assertEqual(path.read_bytes(), bad)

    def test_cli_requires_an_existing_destination(self):
        self.assertEqual(self.command().returncode, 2)
        with tempfile.TemporaryDirectory(dir=SCRATCH) as tmp:
            path = Path(tmp) / 'missing.md'
            result = self.command(path)
            self.assertEqual(result.returncode, 1)
            self.assertFalse(path.exists())

    def test_generator_failure_prevents_a_destination_write(self):
        with tempfile.TemporaryDirectory(dir=SCRATCH) as tmp:
            path = Path(tmp) / 'README.md'
            before = FIXTURE.read_bytes()
            path.write_bytes(before)
            failure = subprocess.CalledProcessError(7, ['results.py', '--profile'])
            with patch.object(profile, 'generated', side_effect=failure):
                with self.assertRaises(subprocess.CalledProcessError):
                    profile.update(path)
            self.assertEqual(path.read_bytes(), before)

    def test_exam_has_only_read_only_test_ci_and_no_refresh_secret(self):
        self.assertFalse((ROOT / '.github/workflows/profile-results.yml').exists())
        ci = yaml.load((ROOT / '.github/workflows/profile-results-test.yml').read_text(),
                       Loader=yaml.BaseLoader)
        self.assertEqual(ci['permissions'], {'contents': 'read'})
        self.assertEqual(set(ci['on']), {'push', 'pull_request'})
        self.assertNotIn('secrets.', str(ci))
        readme = (ROOT / '.github/README.md').read_text()
        self.assertNotIn('PROFILE_RESULTS_TOKEN', readme)
        self.assertIn('no additional secrets are needed', readme)
        self.assertIn('rig-c/.github', readme)


if __name__ == '__main__':
    unittest.main()
