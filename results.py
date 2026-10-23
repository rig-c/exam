#!/usr/bin/env python3
"""Write the results pages from results/.

    python3 results.py           write results/README.md and the block between README.md's results markers
    python3 results.py --check   exit 1 if either would change (nothing is written)
    python3 results.py --profile print the short table the organisation's front page carries

results/<model>/<date>-<name>/ is one run: <model> is the model that did the work, as the proctor
established it; <date>-<name> is the day and the name the run was submitted under. In it, one directory
per task (the files handed in, the proctor's regraded result.json, READING.md, pictures) and who.json,
the proctor's record: who did the work and how, what the run counts as, the minutes read and from where.
results/void/ holds runs that are kept and not counted. Nothing in either page is typed by hand.
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TASKS = sorted(t for t in os.listdir(os.path.join(ROOT, 'tasks')) if os.path.isdir(os.path.join(ROOT, 'tasks', t)))
START, END = '<!-- results:start', '<!-- results:end -->'

def runs():
    out = []
    base = os.path.join(ROOT, 'results')
    for group in sorted(os.listdir(base)):
        if not os.path.isdir(os.path.join(base, group)): continue
        for run in sorted(os.listdir(os.path.join(base, group))):
            d = os.path.join(base, group, run)
            m = re.match(r'(\d{4}-\d{2}-\d{2})-(.+)$', run)
            if not os.path.isdir(d) or not m: continue
            who = json.load(open(os.path.join(d, 'who.json'))) if os.path.exists(os.path.join(d, 'who.json')) else {}
            tasks = {}
            for t in TASKS:
                p = os.path.join(d, t, 'result.json')
                if os.path.exists(p): tasks[t] = json.load(open(p))
            out.append({'group': group, 'run': run, 'day': m.group(1), 'name': m.group(2), 'who': who, 'tasks': tasks, 'path': f'results/{group}/{run}'})
    return sorted(out, key=lambda r: (r['day'], r['group'], r['name']))

def counted(r): return r['who'].get('counts', '').startswith('independent')

def cell(r, t, prefix):
    res = r['tasks'].get(t)
    if res is None: return '—'
    failed = [k for k, v in res['lines'].items() if not v['pass']]
    return f"[{res['passed']} / {res['of']}]({prefix}{r['path']}/{t}/)" + (' — not: ' + ', '.join(failed) if failed else '')

def minutes(r):
    own = [res.get('minutes') for res in r['tasks'].values()]
    if own and all(m is not None for m in own): return f'{sum(own):g}', "the run's own clock"
    m = r['who'].get('minutes')
    return ('—', '') if m is None else (f'{m:g}', r['who'].get('minutes_read_from', ''))

def k(n): return f'{n / 1000:.0f}k' if n < 1e6 else f'{n / 1e6:.1f}M'

def tokens(r, full):
    """What the run spent. The proctor's reading (who.json) first; else what the run reported itself, said to be so."""
    t = r['who'].get('tokens'); src = r['who'].get('tokens_read_from', '')
    if t is None:
        rep = [res.get('usage_reported') for res in r['tasks'].values() if res.get('usage_reported')]
        if not rep: return '—'
        t = {key: sum(u.get(key, 0) for u in rep) for key in ('input_fresh', 'input_cached', 'output', 'total') if any(key in u for u in rep)}; src = 'the run\'s own report'
    if 'output' in t and 'input_fresh' in t:
        s = f"{k(t['input_fresh'] + t['output'])} ({k(t['input_fresh'])} fresh in, {k(t['output'])} out; {k(t.get('input_cached', 0))} cached in)" if full else k(t['input_fresh'] + t['output'])
    else: s = k(t.get('total', 0)) + ' in all'
    return s + (f' — {src}' if full and src else '')

def judge(r, full):
    """What the person who judged the dance blind gave it (who.json `judge`). TASK.md asks for three marks out of 5
    (`dance`, `beat`, `whole`); a judge who gave one mark for the whole clip instead is recorded as given (`score`, `of`)."""
    j = r['who'].get('judge')
    if not j: return '—'
    if 'score' in j:
        return f"{j['score']} / {j['of']}" + (f" (one mark for the whole clip; judged as clip {j.get('letter', '?')})" if full else '')
    marks = [j.get(k) for k in ('dance', 'beat', 'whole')]
    s = f"{sum(marks)} / 15"
    return s + (f" (a dance {marks[0]}, on the beat {marks[1]}, in one piece {marks[2]}; judged as clip {j.get('letter', '?')})" if full else '')

def journal(r):
    """Entries / the grader's WTF?: count, per task — or, where who.json `journal_rulings` holds the proctor's ruling on a
    task's journal, the figure the ruling publishes, marked; the ruling's reason is listed under the table."""
    out = []
    for t in TASKS:
        res = r['tasks'].get(t); p = os.path.join(ROOT, r['path'], t, 'journal.md')
        if res is None or not os.path.exists(p): out.append('—'); continue
        ruling = r['who'].get('journal_rulings', {}).get(t, {})
        c = f"{len(re.findall(r'^## Entry [0-9]', open(p).read(), re.M))} / {ruling.get('surprises', res.get('surprises'))}"
        if 'surprises' in ruling: c += ' (ruled)'
        if ruling.get('credit') == 'void': c += ' (not credited)'
        out.append(c)
    return ' · '.join(out)

def rulings(rs, prefix):
    rows = [(r, t, v) for r in rs if counted(r) for t, v in sorted(r['who'].get('journal_rulings', {}).items())]
    if not rows: return []
    L = ['', f'The proctor ruled on {len(rows)} task journal(s); the journal column shows the ruling, and `result.json` keeps the grader\'s count:', '',
         '| run | task | the grader\'s count | ruling |', '| --- | --- | --- | --- |']
    for r, t, v in rows:
        L.append(f"| [`{r['name']}`]({prefix}{r['path']}/{t}/), {r['day']} | {t} | {r['tasks'][t].get('surprises')} | {v['note']} |")
    return L

def versions(r):
    v = next(iter(r['tasks'].values()))['versions'] if r['tasks'] else {}
    return f"parts {v.get('@rig-c/parts', '?')}, rig-c {v.get('rig-c', '?')}"

def tables(rs, prefix, full):
    good = [r for r in rs if counted(r)]; rest = [r for r in rs if not counted(r)]
    lines = [f'**{len(good)} independent sitting(s) so far**, each cell the lines passed of the lines graded, linking to the run:', '']
    head = ['model that did the work', 'run, as submitted'] + TASKS + ['the dance, judged', 'minutes', 'tokens']
    if full: head += ['minutes read from', 'journal entries / of them WTF?, per task', 'versions']
    lines += ['| ' + ' | '.join(head) + ' |', '| ' + ' | '.join('---' for _ in head) + ' |']
    for r in good:
        m, src = minutes(r)
        row = [r['who'].get('model', f"`{r['name']}`") + (f" — {r['who']['how']}" if full and r['who'].get('how') else ''), f"[`{r['name']}`]({prefix}{r['path']}/), {r['day']}"] + [cell(r, t, prefix) for t in TASKS] + [judge(r, full), m, tokens(r, full)]
        if full: row += [src, journal(r), versions(r)]
        lines.append('| ' + ' | '.join(row) + ' |')
    if full: lines += rulings(good, prefix)
    if rest:
        lines += ['', f'Kept, and not counted — {len(rest)} run(s):', '', '| model that did the work | run, as submitted | lines passed | why it does not count |', '| --- | --- | --- | --- |']
        for r in rest:
            passed = ' · '.join(cell(r, t, prefix) for t in TASKS)
            lines.append(f"| {r['who'].get('model', '?')} | [`{r['name']}`]({prefix}{r['path']}/), {r['day']} | {passed} | {r['who'].get('counts', 'not yet read by the proctor')} |")
    return lines

def task05_text(rs):
    """Which task 05 text the filed rows sat, read off the versions each row's task 05 was graded on: Round 3's painted
    figure (tasks/05-dance/TASK-round3.md) on @rig-c/parts 1.15.0, Round 4's mannequin (tasks/05-dance/TASK.md) on 1.58.0."""
    n = {'TASK-round3.md': 0, 'TASK.md': 0}
    for r in rs:
        t = r['tasks'].get('05-dance')
        if t is None: continue
        n['TASK-round3.md' if t.get('versions', {}).get('@rig-c/parts') == '1.15.0' else 'TASK.md'] += 1
    r4 = f"{n['TASK.md']} on Round 4\'s, the mannequin (`tasks/05-dance/TASK.md`)" if n['TASK.md'] else "none yet on Round 4\'s, the mannequin (`tasks/05-dance/TASK.md`; dry run pending)"
    return f"Task 05 cells: {n['TASK-round3.md']} sat Round 3\'s text, the painted figure (`tasks/05-dance/TASK-round3.md`); {r4}."

def results_page(rs):
    L = ['# Results', '', 'Generated by `results.py` from this directory. A run is filed under the model that did the work, as the',
         'proctor established it — which is not always the name it was submitted under — and keeps that name beside',
         'the day. Each run holds the files handed in, the proctor\'s regrade of them (`result.json`), its reading',
         '(`READING.md`) and `who.json`. [REPORT.md](REPORT.md) is the proctor\'s account, written by hand.', '',
         '**What the machine lines cannot see.** On 2026-10-20 six runs passed all fourteen of task 05\'s lines, and one person',
         'judging their clips blind scored them from 3 to 9 out of 10; the run that missed one line scored 5 and the one whose',
         'build failed 0. The lines read whether a dance holds together, not whether it is one.',
         '[The report](REPORT.md#what-the-machine-lines-cannot-see) has the scores, the judge\'s rubric, a caveat on how four of',
         'the sittings were run, and what the day filed on the exam and the tools.', '']
    L += [l.replace('](results/', '](') for l in tables(rs, '', True)]
    L += ['', 'Minutes are for the tasks sat, together: the run\'s own `started:` / `finished:` lines where it has them,',
          'otherwise what the proctor read and from where. Tokens are fresh input plus output, with the cached input a session',
          're-read on every turn beside them; a dash means nothing recorded them. The dance (task 05) is scored by a person from a clip that carries a letter and no name, on the scale the judge used (Round 3\'s TASK-round3.md asks for three marks out of 5; the 2026-10-20 clips got one mark out of 10, the scale Round 4\'s TASK.md states), and the score changes no line. Two rows with the same model are that model sitting the',
          'exam twice, not two models.', '', task05_text(rs), '',
          'A pass says the published documents were enough for that model on that painting. It says nothing about',
          'a model that is not in the table, and little about taste: whether a wave reads as a wave is in the reading.', '']
    return '\n'.join(L)

def readme_block(rs):
    L = tables(rs, '', False)
    L += ['', 'Minutes are for the tasks sat, together; tokens are fresh input plus output, cached input left out; the dance is judged by a person who does not know whose clip it is. [The full table](results/README.md) has who sat each run and how,',
          'the journals\' counts and the versions; [the proctor\'s report](results/REPORT.md) says what the journals found',
          'in the tools and in this exam.', '', task05_text(rs)]
    return '\n'.join(L)

def profile_block(rs):
    """A short table for the organisation's front page: one row per model that did the work, counted sittings only."""
    site = 'https://github.com/rig-c/exam/tree/main/'
    by = {}
    for r in rs:
        if counted(r): by.setdefault(r['group'], []).append(r)
    L = ['| model | sittings | lines passed, of lines graded | minutes for the tasks sat |', '| --- | --- | --- | --- |']
    for group, rr in sorted(by.items()):
        name = rr[0]['who'].get('short') or rr[0]['who'].get('model', group)
        passed = sum(res['passed'] for r in rr for res in r['tasks'].values()); of = sum(res['of'] for r in rr for res in r['tasks'].values())
        mins = sorted(float(minutes(r)[0]) for r in rr if minutes(r)[0] != '—')
        span = '—' if not mins else (f'{mins[0]:g}' if len(mins) == 1 else f'{mins[0]:g} to {mins[-1]:g}')
        L.append(f"| [{name}]({site}results/{group}/) | {len(rr)} | {passed} / {of} | {span} |")
    return '\n'.join(L)

def main():
    rs = runs()
    if '--profile' in sys.argv: print(profile_block(rs)); return
    page = results_page(rs)
    readme = open(os.path.join(ROOT, 'README.md')).read()
    a = readme.index(START); a_end = readme.index('-->', a) + 3; b = readme.index(END)
    new_readme = readme[:a_end] + '\n' + readme_block(rs) + '\n' + readme[b:]
    page_path = os.path.join(ROOT, 'results', 'README.md')
    old_page = open(page_path).read() if os.path.exists(page_path) else None
    if '--check' in sys.argv:
        stale = [n for n, same in (('results/README.md', old_page == page), ('README.md', readme == new_readme)) if not same]
        if stale: sys.exit('stale, run python3 results.py: ' + ', '.join(stale))
        print('results pages are current'); return
    open(page_path, 'w').write(page); open(os.path.join(ROOT, 'README.md'), 'w').write(new_readme)
    print(f'{len(rs)} run(s): {sum(counted(r) for r in rs)} counted; wrote results/README.md and the README block')

if __name__ == '__main__': main()
