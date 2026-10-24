"""Targeted profile splice/count/workflow contracts; never runs Git or writes remotely."""
import os
from pathlib import Path
import shlex
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
SCRATCH = ROOT / 'work/profile-tests'
SCRATCH.mkdir(parents=True, exist_ok=True)


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


class WorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflow = yaml.load((ROOT / '.github/workflows/profile-results.yml').read_text(),
                                 Loader=yaml.BaseLoader)
        cls.job = cls.workflow['jobs']['profile']
        cls.steps = cls.job['steps']

    def test_main_results_push_and_manual_dispatch_only(self):
        self.assertEqual(set(self.workflow['on']), {'push', 'workflow_dispatch'})
        self.assertEqual(self.workflow['on']['push'],
                         {'branches': ['main'], 'paths': ['results/**', 'advanced/results/**']})
        self.assertIn("github.ref == 'refs/heads/main'", self.job['if'])
        self.assertIn("github.repository == 'rig-c/exam'", self.job['if'])
        self.assertEqual(self.workflow['permissions'], {'contents': 'read'})
        self.assertEqual(self.workflow['concurrency'],
                         {'group': 'exam-profile-results', 'cancel-in-progress': 'false'})

    def test_checkouts_bind_source_sha_and_profile_only_pat(self):
        checkouts = [s['with'] for s in self.steps if s.get('uses', '').startswith('actions/checkout@')]
        self.assertEqual(len(checkouts), 2)
        source, target = checkouts
        self.assertEqual(source['ref'], '${{ github.sha }}')
        self.assertNotIn('token', source)
        self.assertEqual(target['repository'], 'rig-c/.github')
        self.assertEqual(target['ref'], 'main')
        self.assertEqual(target['token'], '${{ secrets.PROFILE_RESULTS_TOKEN }}')
        self.assertTrue(all(c['persist-credentials'] == 'false' for c in checkouts))
        guard = next(s for s in self.steps if s.get('name') == 'Require the profile token')
        self.assertIn('exit 1', guard['run'])
        self.assertNotIn('$PROFILE_TOKEN\n', guard['run'])

    def test_token_presence_check_fails_without_printing_a_token(self):
        guard = next(s for s in self.steps if s.get('name') == 'Require the profile token')
        env = dict(os.environ)
        for value, code in (('', 1), ('local-test-not-a-real-token', 0)):
            env['PROFILE_TOKEN'] = value
            result = subprocess.run(['bash', '-eu', '-c', guard['run']], env=env, capture_output=True)
            self.assertEqual(result.returncode, code)
            if value:
                self.assertEqual(result.stdout + result.stderr, b'')
            else:
                self.assertIn(b'Owner must provision PROFILE_RESULTS_TOKEN', result.stdout)

    def test_one_fixed_pr_branch_scoped_path_and_no_merge(self):
        actions = [s for s in self.steps if s.get('uses', '').startswith('peter-evans/create-pull-request@')]
        self.assertEqual(len(actions), 1)
        step = actions[0]; config = step['with']
        self.assertNotIn('if', step)  # let the action retire a PR whose diff disappeared
        self.assertEqual(config['branch'], 'codex/exam-profile-results')
        self.assertNotIn('branch-suffix', config)
        self.assertEqual(config['base'], 'main')
        self.assertEqual(config['path'], 'profile')
        self.assertEqual(config['add-paths'], 'profile/README.md')
        self.assertEqual(config['token'], '${{ secrets.PROFILE_RESULTS_TOKEN }}')
        self.assertEqual(config['delete-branch'], 'true')
        self.assertEqual(config['title'], 'docs(profile): exam tables at ${{ github.sha }}')
        self.assertIn('Co-Authored-By: Naru <342599188+fj-naru[bot]@users.noreply.github.com>',
                      config['commit-message'])
        self.assertFalse(any('merge' in s.get('run', '') for s in self.steps))
        self.assertEqual(len(step['uses'].split('@')[1].split()[0]), 40)

    def test_actual_generation_step_runs_locally_and_second_run_is_noop(self):
        step = next(s for s in self.steps if s.get('name') == 'Generate and splice both tables and counts')
        with tempfile.TemporaryDirectory(dir=SCRATCH) as tmp:
            base = Path(tmp)
            (base / 'exam').symlink_to(ROOT, target_is_directory=True)
            dest = base / 'profile/profile/README.md'
            dest.parent.mkdir(parents=True)
            dest.write_bytes(FIXTURE.read_bytes())
            command = shlex.split(step['run'])
            first = subprocess.run(command, cwd=base, capture_output=True, check=True)
            self.assertEqual(first.stdout, b'profile_results: updated\n')
            frozen = dest.read_bytes(), dest.stat().st_mtime_ns
            second = subprocess.run(command, cwd=base, capture_output=True, check=True)
            self.assertEqual(second.stdout, b'profile_results: unchanged\n')
            self.assertEqual((dest.read_bytes(), dest.stat().st_mtime_ns), frozen)
            for name, script in (('exam', 'results.py'), ('exam-advanced', 'advanced/results.py')):
                r = profile.region(dest.read_bytes(), name)
                expected = subprocess.check_output([sys.executable, '-B', str(ROOT / script), '--profile'])
                self.assertEqual(dest.read_bytes()[r[1]:r[2]], expected)


if __name__ == '__main__':
    unittest.main()
