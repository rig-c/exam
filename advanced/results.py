#!/usr/bin/env python3
"""Write the Advanced edition's results pages from advanced/results/.

    python3 advanced/results.py           write advanced/results/README.md and the block between
                                          advanced/README.md's results markers
    python3 advanced/results.py --check   exit 1 if either would change (nothing is written)
    python3 advanced/results.py --profile print the short table the organisation's front page carries

advanced/results/<model>/<date>-<round>/ is one sitting of one round: <model> is the model that did
the work, exactly as the person who started the session named it; <date> is the UTC day of the run's
own `started:` line. In it: the files the run handed in, `result.txt` (the proctor's regrade, the
verdict of record) and `who.json` (the proctor's record: who did the work, where, the clock, the 0.21
shin-scale figure, what was noted). Nothing in either page is typed by hand.
"""
import json, os, re, sys
from datetime import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
ROUNDS = ['R1', 'R2', 'R3']
WHAT = {'R1': 'walk', 'R2': 'run', 'R3': 'dance'}
START, END = '<!-- results:start', '<!-- results:end -->'
SHIN_BAR = 0.4  # the 0.21 row: the 5th percentile of the shins' rendered x-scale >= 0.4 (each PROBLEM.md, "Shin scale")

def table_rows(rnd):
    """The rows of a round's fixed pass table, read from its PROBLEM.md."""
    text = open(os.path.join(ROOT, rnd, 'PROBLEM.md'), encoding='utf-8').read()
    body = text.split('## Pass table', 1)[1].split('\n## ', 1)[0]
    rows = [l for l in body.splitlines() if l.startswith('| ')]
    return [l.split('|')[1].strip() for l in rows[1:] if not set(l) <= set('|- ')]

def grade(path):
    """result.txt: the per-row verdicts and the RESULT line."""
    text = open(path, encoding='utf-8').read()
    rows = {m.group(2): m.group(1) for m in re.finditer(r'^(PASS|FAIL|SKIP)\s+(\S+)\s', text, re.M)}
    m = re.search(r'^RESULT (PASS|FAIL) \((\d+) pass, (\d+) fail, (\d+) skip of (\d+) rows\)', text, re.M)
    if not m: sys.exit(f'{path}: no RESULT line')
    verdict, passed, failed, skipped, of = m.group(1), *map(int, m.groups()[1:])
    if passed + failed + skipped != of or len(rows) != of: sys.exit(f'{path}: the RESULT line and the rows disagree')
    return {'verdict': verdict, 'passed': passed, 'of': of, 'rows': rows}

def count(path, pattern):
    if not os.path.exists(path): return None
    return len(re.findall(pattern, open(path, encoding='utf-8', errors='replace').read(), re.M))

def sittings():
    out = []
    base = os.path.join(ROOT, 'results')
    for model in sorted(os.listdir(base)):
        if not os.path.isdir(os.path.join(base, model)): continue
        for run in sorted(os.listdir(os.path.join(base, model))):
            d = os.path.join(base, model, run)
            m = re.match(r'(\d{4}-\d{2}-\d{2})-(R[123])$', run)
            if not os.path.isdir(d) or not m: continue
            who = json.load(open(os.path.join(d, 'who.json'), encoding='utf-8'))
            t0, t1 = (datetime.strptime(who[k], '%Y-%m-%dT%H:%M:%SZ') for k in ('started', 'finished'))
            p05 = who.get('shin_scale_p05')
            out.append({'model': model, 'day': m.group(1), 'round': m.group(2), 'path': f'results/{model}/{run}', 'who': who,
                        'grade': grade(os.path.join(d, 'result.txt')), 'minutes': (t1 - t0).total_seconds() / 60,
                        'shin': None if p05 is None else ('PASS' if p05 >= SHIN_BAR else 'FAIL', p05),
                        'entries': count(os.path.join(d, 'journal.md'), r'^## Entry [0-9]'),
                        'wtf': count(os.path.join(d, 'journal.md'), r'WTF\?:'),
                        'tools': count(os.path.join(d, 'tools.md'), r'^## ')})
    return out

def by_model(ss):
    models = {}
    for s in ss: models.setdefault(s['model'], {})[s['round']] = s
    return models

def cell(s, prefix, full):
    if s is None: return '—'
    g = s['grade']; failed = [k for k, v in g['rows'].items() if v != 'PASS']
    c = f"[{g['passed']} / {g['of']}]({prefix}{s['path']}/)"
    return c + (' — not: ' + ', '.join(failed) if failed and full else (' FAIL' if failed else ''))

def native(s): return s['who'].get('edition') == '0.21'   # graded on 0.21: the shin-scale row is in result.txt itself

def whatif(s):
    if s is None or s['shin'] is None: return '—'
    v, p = s['shin']; g = s['grade']
    if native(s): return f"{'**FAIL**' if v == 'FAIL' else 'PASS'} {p:.3f}, graded on 0.21"
    total = g['passed'] + (v == 'PASS')
    return f"{'**FAIL**' if v == 'FAIL' else 'PASS'} {p:.3f} → {total} / {g['of'] + 1}"

def mins(rr): return ' · '.join('—' if rr.get(r) is None else f"{rr[r]['minutes']:.1f}" for r in ROUNDS)

def journal(rr):
    return ' · '.join('—' if rr.get(r) is None else f"{rr[r]['entries']} / {rr[r]['wtf']} / {'—' if rr[r]['tools'] is None else rr[r]['tools']}" for r in ROUNDS)

def tables(ss, prefix, full):
    models = by_model(ss); rows = {r: len(table_rows(r)) for r in ROUNDS}
    graded = sorted({s['grade']['of'] for s in ss if s['round'] == 'R1'})
    failed = sum(s['grade']['verdict'] == 'FAIL' for s in ss)
    ind = sum(s['who'].get('counts') == 'independent' for s in ss)
    on21 = sum(native(s) for s in ss)
    L = [f"**{len(ss)} sitting(s) of {len(models)} model(s), {ind} of them independent**, {len(ss) - on21} graded on edition 0.20 and {on21} on 0.21; each cell the rows passed "
         f"of the rows graded, linking to the sitting. {failed} of the {len(ss)} failed. The shin-scale column is edition 0.21's one new row "
         f"(the 5th percentile of the shins' rendered x-scale ≥ {SHIN_BAR}): for a 0.20 sitting a what-if, run on its own render, with the "
         f"total it would have made; for a 0.21 sitting the row as graded, already in its cell (R1 · R2 · R3 tables are {rows['R1']} · {rows['R2']} · {rows['R3']} rows on 0.21).", '']
    head = ['model that did the work', 'host'] + [f'{r} {WHAT[r]}' for r in ROUNDS] + ['0.21 shin scale (what-if on 0.20): R1 · R2 · R3', 'minutes, R1 · R2 · R3']
    if full: head += ['journal entries / of them WTF?: / tools.md entries, R1 · R2 · R3', 'clock (UTC), R1 · R2 · R3']
    L += ['| ' + ' | '.join(head) + ' |', '| ' + ' | '.join('---' for _ in head) + ' |']
    for model, rr in sorted(models.items()):
        host = next(iter(rr.values()))['who'].get('host', '?')
        if full: host += ' — ' + next(iter(rr.values()))['who'].get('how', '')
        row = [f'`{model}`', host] + [cell(rr.get(r), prefix, full) for r in ROUNDS] + ['<br>'.join(whatif(rr.get(r)) for r in ROUNDS) if full else ' · '.join(whatif(rr.get(r)) for r in ROUNDS), mins(rr)]
        if full: row += [journal(rr), ' · '.join('—' if rr.get(r) is None else f"{rr[r]['who']['started'][11:16]}–{rr[r]['who']['finished'][11:16]}" for r in ROUNDS)]
        L.append('| ' + ' | '.join(row) + ' |')
    noted = [s for s in ss if s['who'].get('notes')]
    if noted:
        L += ['', f'What the proctor recorded against {len(noted)} sitting(s) — none of it changes a verdict:', '', '| sitting | recorded |', '| --- | --- |']
        for s in sorted(noted, key=lambda s: (s['round'], s['model'])):
            L.append(f"| [`{s['model']}` {s['round']}]({prefix}{s['path']}/) | {'; '.join(s['who']['notes'])} |")
    if full:
        L += ['', 'Files a sitting directory does not carry as handed in:', '', '| sitting | file |', '| --- | --- |']
        for s in sorted(ss, key=lambda s: (s['round'], s['model'])):
            L.append(f"| [`{s['model']}` {s['round']}]({prefix}{s['path']}/) | {'; '.join(s['who'].get('files', [])) or '—'} |")
    return L

def results_page(ss):
    L = ['# Advanced results', '', 'Generated by `advanced/results.py` from this directory. A sitting is one model, one fresh session, one round;',
         'each directory holds the files the run handed in, the proctor\'s regrade of them (`result.txt`, the verdict of record)',
         'and `who.json`. [REPORT.md](REPORT.md) is the proctor\'s account, written by hand.', '']
    L += [l.replace('](results/', '](') for l in tables(ss, '', True)]
    L += ['', 'Minutes are each round\'s own `started:` / `finished:` lines, from the transcript. No sitting handed in a `usage.json`,',
          'so no tokens are in the table; where the proctor read them from a host\'s log they are in that sitting\'s `who.json`. A what-if cell is the 0.21 row\'s verdict, the 5th percentile it read, and the total the sitting',
          'would have made with that row added; the verdict of record is the 0.20 one beside it. A cell that says "graded on 0.21" is that row as the sitting was graded.', '']
    return '\n'.join(L)

def readme_block(ss):
    L = tables(ss, '', False)
    L += ['', '[The full table](results/README.md) has how each model was run, the journals\' counts, the clocks and what each',
          'sitting directory leaves out; [the proctor\'s report](results/REPORT.md) says what the journals found in the tools and in this edition.']
    return '\n'.join(L)

def profile_block(ss):
    """A short table for the organisation's front page: one row per model, one cell per round."""
    site = 'https://github.com/rig-c/exam/tree/main/advanced/'
    L = ['| model | R1 walk | R2 run | R3 dance | 0.21 shin-scale row, what-if | minutes, R1 · R2 · R3 |', '| --- | --- | --- | --- | --- | --- |']
    for model, rr in sorted(by_model(ss).items()):
        cells = [cell(rr.get(r), site, False) for r in ROUNDS]
        fails = [f"{r} ({rr[r]['shin'][1]:.3f})" for r in ROUNDS if rr.get(r) and rr[r]['shin'] and rr[r]['shin'][0] == 'FAIL']
        shin = ('fails ' + ', '.join(fails)) if fails else f"passes all {sum(1 for r in ROUNDS if rr.get(r))}"
        L.append(f"| [`{model}`]({site}results/{model}/) | " + ' | '.join(cells) + f' | {shin} | {mins(rr)} |')
    return '\n'.join(L)

def main():
    ss = sittings()
    if '--profile' in sys.argv: print(profile_block(ss)); return
    page = results_page(ss)
    readme_path = os.path.join(ROOT, 'README.md')
    readme = open(readme_path, encoding='utf-8').read()
    a = readme.index(START); a_end = readme.index('-->', a) + 3; b = readme.index(END)
    new_readme = readme[:a_end] + '\n' + readme_block(ss) + '\n' + readme[b:]
    page_path = os.path.join(ROOT, 'results', 'README.md')
    old_page = open(page_path, encoding='utf-8').read() if os.path.exists(page_path) else None
    if '--check' in sys.argv:
        stale = [n for n, same in (('advanced/results/README.md', old_page == page), ('advanced/README.md', readme == new_readme)) if not same]
        if stale: sys.exit('stale, run python3 advanced/results.py: ' + ', '.join(stale))
        print('advanced results pages are current'); return
    open(page_path, 'w', encoding='utf-8').write(page); open(readme_path, 'w', encoding='utf-8').write(new_readme)
    print(f'{len(ss)} sitting(s) of {len(by_model(ss))} model(s); wrote advanced/results/README.md and the advanced/README.md block')

if __name__ == '__main__': main()
