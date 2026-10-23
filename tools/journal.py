#!/usr/bin/env python3
"""journal.py: the only writer of <run>/journal.md and <run>/transcript.md.

Every step of the task is three calls, in three separate turns:

  python3 tools/journal.py open --read TEXT --expect TEXT --chose TEXT   lines 1-3, before the step
  python3 tools/journal.py run -- COMMAND ARG...                         the step itself
  python3 tools/journal.py close --happened TEXT                         line 4, after you read the output

and the run is framed by four more:

  python3 tools/journal.py start           before you open the task's text (PROBLEM.md or TASK.md): `started: <UTC>`
  python3 tools/journal.py end --guessed TEXT --missing TEXT             the journal's "At the end" section
  python3 tools/journal.py finish          after your last grader run: transcript.md's last line, `finished: <UTC>`
  python3 tools/journal.py verify          prints whether the chain is intact

Every verb takes --run DIR, the run directory (default: run). Put it before or after the verb.

Rules the tool holds you to (a refused call writes nothing, runs nothing and exits 2):
  open    refused before `start`, while an entry is open (whether or not its step ran), after `end` or `finish`.
  run     refused with no open entry, and when the open entry already ran its step: one step per entry.
          A refused run does not execute the command.
  close   refused unless the open entry's step ran, and unless --happened quotes that step's output (below).
          A refused close leaves the entry open: read the output again and close it.
  end     refused while an entry is open, and a second time.
  finish  refused while an entry is open, and a second time.

The quote rule (close). --happened must contain at least one fragment of 12 or more characters that also
occurs in the step's captured output (.journal/step-<n>.out, stdout and stderr together). Before comparing,
both texts are normalised the same way: ANSI colour/escape sequences and carriage returns are removed, and
every run of whitespace (spaces, tabs, newlines) becomes one space. The comparison is exact otherwise: case,
digits and punctuation must match. So copy a fragment from the output, e.g.
  close --happened 'exit 0; it printed "gate: 0 errors, 2 warnings" -- the two warnings were not expected'
A --happened that begins with `WTF?:` passes through as written, without the quote check: use it when the
result differs from what you expected (that is what WTF?: is for), not to skip the quote.
A step whose whole output, normalised, is shorter than 12 characters cannot be quoted that way. For such a
step, quote its end stamp instead: `run` prints `journal.py: step <n> ended <UTC stamp>, exit <code>` when
the command finishes, and --happened must then contain that exact stamp (e.g. 2026-10-23T11:20:13Z) to the
second. Better still, make the step show what it made: run -- sh -c 'CMD && ls -l OUT'.

What a step is. Each command that builds, renders, measures or grades is a step and runs through `run`:
a build, a retarget, a render, a measurement script, a grader run, a script that writes evidence frames. A file you write by hand is not a step by itself: name it in line 3 of the step that first uses it.
For a pipeline or redirection, give the shell as the command: run -- sh -c 'a | b > out.txt'.
The command runs in the current directory, with its output shown live and saved; `run` exits with the
command's own exit code (127 if it could not be started, 128+N if a signal N ended it).

On disk, inside the run directory:
  journal.md          the entries, in the JOURNAL.md format, each part stamped in UTC
  transcript.md       `started:`, one record per step (argv, UTC start and end, exit code, last lines), `finished:`
  .journal/chain.jsonl   one line per block the tool wrote, in order: which file and entry it belongs to, its
                      kind, its length in bytes, the previous block's hash and its own hash:
                      sha256(previous hash + "\\n" + kind + " " + entry + " " + file + "\\n" + the block's exact bytes)
  .journal/step-<n>.out  entry n's captured output (its sha256 is in the step's transcript record)

What verify trusts. Only the chain ledger (.journal/chain.jsonl) and the step outputs it names. It reads
journal.md and transcript.md from the first byte, cuts each into the blocks the ledger lists, at the
lengths it lists, and recomputes every hash in order. The first block whose bytes, order or hash do not
match is the first broken link, so a hand edit, a deleted or reordered entry, a truncated or appended file,
or an edited step output shows there. It also checks each close's quote against its step output again.
It prints exactly one line:
  journal: chain intact, N entries, M WTF                      exit 0
  journal: first broken link at entry K (<why>)                exit 1   (K 0 = the started line)
  journal: not kept (no chain)                                 exit 1   (no ledger: not written by this tool)
The chain shows what was changed after the tool wrote it; it does not stop someone who rewrites the
ledger on purpose, and it cannot show that line 2 was a real expectation. Do not edit, move or delete
anything in the run directory's .journal/, journal.md or transcript.md by hand.
"""
import argparse
import fcntl
import hashlib
import json
import os
import re
import signal
import subprocess
import sys
import time

GENESIS = '0' * 64
QUOTE_MIN = 12
TAIL_LINES = 12
ANSI = re.compile(r'\x1b\[[0-?]*[ -/]*[@-~]|\x1b\][^\x07\x1b]*(?:\x07|\x1b\\)|\x1b[@-Z\\-_]')


class Refused(Exception):
    pass


def now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def normalise(text):
    return ' '.join(ANSI.sub('', text).replace('\r', '').split())


def quotes(happened, output):
    """True when `happened` holds a fragment of >= QUOTE_MIN characters that also occurs in `output`."""
    h, o = normalise(happened), normalise(output)
    return any(h[i:i + QUOTE_MIN] in o for i in range(len(h) - QUOTE_MIN + 1))


def block_hash(prev, kind, entry, fname, data):
    return hashlib.sha256(f'{prev}\n{kind} {entry} {fname}\n'.encode() + data).hexdigest()


def indent(text):
    """Keep a multi-line text inside its markdown list item."""
    return '\n   '.join(text.strip().splitlines()) if text.strip() else '(empty)'


class Journal:
    def __init__(self, run):
        self.run = run
        self.state = os.path.join(run, '.journal')
        self.ledger_path = os.path.join(self.state, 'chain.jsonl')

    def path(self, fname):
        return os.path.join(self.run, fname)

    def ledger(self):
        if not os.path.exists(self.ledger_path):
            return []
        with open(self.ledger_path) as f:
            return [json.loads(l) for l in f if l.strip()]

    # -- the state, replayed from the ledger -------------------------------------------------------
    def status(self, recs):
        st = {'started': False, 'finished': False, 'ended': False, 'entries': 0, 'open': None, 'ran': False}
        for r in recs:
            k = r['kind']
            if k == 'started':
                st['started'] = True
            elif k == 'open':
                st['entries'] = r['entry']; st['open'] = r['entry']; st['ran'] = False
            elif k == 'step':
                st['ran'] = True
            elif k == 'close':
                st['open'] = None; st['ran'] = False
            elif k == 'end':
                st['ended'] = True
            elif k == 'finished':
                st['finished'] = True
        return st

    def append(self, recs, fname, kind, entry, text, extra=None):
        data = text.encode()
        prev = recs[-1]['hash'] if recs else GENESIS
        rec = {'seq': len(recs) + 1, 'file': fname, 'entry': entry, 'kind': kind, 'at': now(),
               'length': len(data), 'prev': prev, 'hash': block_hash(prev, kind, entry, fname, data)}
        if extra:
            rec.update(extra)
        with open(self.path(fname), 'ab') as f:
            f.write(data)
        with open(self.ledger_path, 'a') as f:
            f.write(json.dumps(rec, sort_keys=True) + '\n')
        recs.append(rec)
        return rec

    def guard(self):
        line, code = verify(self.run)
        if code and 'not kept' not in line:
            print('journal.py: WARNING ' + line + ': the journal was changed by hand; this is recorded', file=sys.stderr)

    def step_out(self, n):
        return os.path.join(self.state, f'step-{n}.out')

    def recover(self, recs):
        """A `run` that was killed before it could write its record: write it now from what was captured."""
        st = self.status(recs)
        marker = os.path.join(self.state, 'running.json')
        if not os.path.exists(marker):
            return
        with open(marker) as f:
            m = json.load(f)
        try:
            os.kill(m['pid'], 0)
            alive = True
        except ProcessLookupError:
            alive = False
        except PermissionError:
            alive = True
        if alive:
            raise Refused(f'step {m["entry"]} is still running (journal.py pid {m["pid"]}); wait for it to finish')
        if st['open'] == m['entry'] and not st['ran']:
            self.write_step(recs, m['entry'], m['argv'], m['start'], now(), None)
        os.remove(marker)

    def write_step(self, recs, n, argv, start, end, code):
        out = self.step_out(n)
        raw = open(out, 'rb').read() if os.path.exists(out) else b''
        text = raw.decode('utf-8', 'replace')
        lines = ANSI.sub('', text).replace('\r', '').rstrip('\n').splitlines()[-TAIL_LINES:]
        tail = '\n'.join('    ' + l for l in lines) if lines else '    (no output)'
        shown = 'none: the run was interrupted before the command ended' if code is None else str(code)
        block = (f'\n## Step {n} (entry {n})\n\n'
                 f'- argv: {json.dumps(argv)}\n'
                 f'- start: {start}\n'
                 f'- end: {end}\n'
                 f'- exit: {shown}\n'
                 f'- output: .journal/step-{n}.out, {len(raw)} bytes, sha256 {hashlib.sha256(raw).hexdigest()}\n'
                 f'- last lines:\n\n{tail}\n')
        self.append(recs, 'transcript.md', 'step', n, block,
                    {'out': f'step-{n}.out', 'out_sha256': hashlib.sha256(raw).hexdigest(), 'exit': code, 'end': end})


def locked(fn):
    def wrapper(j, a):
        os.makedirs(j.state, exist_ok=True)
        with open(os.path.join(j.state, 'lock'), 'w') as lk:
            fcntl.flock(lk, fcntl.LOCK_EX)
            return fn(j, a)
    return wrapper


@locked
def cmd_start(j, a):
    recs = j.ledger()
    if recs:
        raise Refused('the run is already started; `start` is the first thing the journal records')
    for fname in ('journal.md', 'transcript.md'):
        if os.path.exists(j.path(fname)) and os.path.getsize(j.path(fname)):
            raise Refused(f'{j.path(fname)} already exists and was not written by journal.py; this tool writes it from the start')
    rec = j.append(recs, 'transcript.md', 'started', 0, f'started: {now()}\n')
    print(f'journal.py: started, {rec["at"]}')
    return 0


@locked
def cmd_open(j, a):
    recs = j.ledger(); j.guard(); j.recover(recs)
    st = j.status(recs)
    if not st['started']:
        raise Refused('the run is not started: run `journal.py start` first (it writes transcript.md\'s `started:` line)')
    if st['finished'] or st['ended']:
        raise Refused('the journal is closed (`end` or `finish` already ran); no entry can be opened after it')
    if st['open'] is not None:
        raise Refused(f'entry {st["open"]} is still open' + (': close it with `close --happened`' if st['ran'] else
                      ': its step has not run yet; run it with `run -- COMMAND`, then close it'))
    n = st['entries'] + 1
    stamp = now()
    head = '# Journal\n\n' if n == 1 else ''
    block = (f'{head}## Entry {n} (opened {stamp})\n\n'
             f'1. **Read:** {indent(a.read)}\n'
             f'2. **Expect:** {indent(a.expect)}\n'
             f'3. **Chose / turned down:** {indent(a.chose)}\n')
    j.append(recs, 'journal.md', 'open', n, block)
    print(f'journal.py: entry {n} open, {stamp}; next: run -- COMMAND')
    return 0


@locked
def cmd_run(j, a):
    recs = j.ledger(); j.guard(); j.recover(recs)
    st = j.status(recs)
    if not a.command:
        raise Refused('no command: give it after --, e.g. run -- npx rigc build ...')
    if st['open'] is None:
        raise Refused('no entry is open: write lines 1-3 with `open` first; the command was not run')
    if st['ran']:
        raise Refused(f'entry {st["open"]} already ran its step (one step per entry): close it, then open a new entry; the command was not run')
    n = st['open']
    out = j.step_out(n)
    start = now()
    marker = os.path.join(j.state, 'running.json')
    with open(marker, 'w') as f:
        json.dump({'pid': os.getpid(), 'entry': n, 'argv': a.command, 'start': start}, f)
    code = None
    with open(out, 'wb') as cap:
        try:
            p = subprocess.Popen(a.command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        except OSError as e:
            msg = f'journal.py: could not start {a.command[0]}: {e}\n'.encode()
            cap.write(msg); sys.stdout.buffer.write(msg); sys.stdout.flush()
            code = 127
        else:
            try:
                while True:
                    chunk = os.read(p.stdout.fileno(), 65536)
                    if not chunk:
                        break
                    cap.write(chunk); cap.flush()
                    sys.stdout.buffer.write(chunk); sys.stdout.flush()
            except KeyboardInterrupt:
                p.send_signal(signal.SIGINT)
            rc = p.wait()
            code = rc if rc >= 0 else 128 - rc
    end = now()
    j.write_step(recs, n, a.command, start, end, code)
    os.remove(marker)
    print(f'journal.py: step {n} ended {end}, exit {code}; next: read the output, then close --happened', file=sys.stderr)
    return code


@locked
def cmd_close(j, a):
    recs = j.ledger(); j.guard(); j.recover(recs)
    st = j.status(recs)
    if st['open'] is None:
        raise Refused('no entry is open')
    n = st['open']
    if not st['ran']:
        raise Refused(f'entry {n} has not run its step: run it with `run -- COMMAND`, read its output, then close')
    step = [r for r in recs if r['kind'] == 'step' and r['entry'] == n][-1]
    why = quote_problem(a.happened, j.step_out(n), step)
    if why:
        raise Refused(why + '; the entry stays open')
    stamp = now()
    j.append(recs, 'journal.md', 'close', n, f'4. **Happened** ({stamp}): {indent(a.happened)}\n\n')
    wtf = ' (WTF)' if a.happened.lstrip().startswith('WTF?:') else ''
    print(f'journal.py: entry {n} closed{wtf}, {stamp}')
    return 0


def quote_problem(happened, out_path, step):
    """None when the close passes the quote rule; otherwise why not."""
    if happened.lstrip().startswith('WTF?:'):
        return None
    out = open(out_path, 'rb').read().decode('utf-8', 'replace') if os.path.exists(out_path) else ''
    if len(normalise(out)) < QUOTE_MIN:
        if step['end'] in happened:
            return None
        return (f'the quote rule: this step printed fewer than {QUOTE_MIN} characters, so --happened must contain '
                f'its end stamp exactly ({step["end"]}), or begin with WTF?: if the result was not what you expected')
    if quotes(happened, out):
        return None
    return (f'the quote rule: --happened quotes no fragment of {QUOTE_MIN} or more characters of the step\'s '
            f'output ({out_path}); copy a piece of what the step printed into line 4, or begin it with WTF?: '
            f'if the result was not what you expected')


@locked
def cmd_end(j, a):
    recs = j.ledger(); j.guard(); j.recover(recs)
    st = j.status(recs)
    if not st['started']:
        raise Refused('the run is not started')
    if st['open'] is not None:
        raise Refused(f'entry {st["open"]} is still open: close it first')
    if st['ended']:
        raise Refused('`end` already ran')
    stamp = now()
    head = '# Journal\n\n' if st['entries'] == 0 else ''
    block = (f'{head}## At the end ({stamp})\n\n'
             f'- **Where I guessed:** {indent(a.guessed)}\n'
             f'- **What I could not find:** {indent(a.missing)}\n')
    j.append(recs, 'journal.md', 'end', st['entries'], block)
    print(f'journal.py: end written, {stamp}')
    return 0


@locked
def cmd_finish(j, a):
    recs = j.ledger(); j.guard(); j.recover(recs)
    st = j.status(recs)
    if not st['started']:
        raise Refused('the run is not started')
    if st['open'] is not None:
        raise Refused(f'entry {st["open"]} is still open: close it first')
    if st['finished']:
        raise Refused('`finish` already ran')
    rec = j.append(recs, 'transcript.md', 'finished', st['entries'], f'\nfinished: {now()}\n')
    print(f'journal.py: finished, {rec["at"]}')
    return 0


def verify(run):
    """(line, exit code). The one implementation of the chain check; the edition's grader calls it.
    A ledger whose records are not what journal.py writes reports a broken chain; it never raises."""
    try:
        return _verify(run)
    except (AttributeError, TypeError, KeyError, ValueError, IndexError) as e:
        return f'journal: first broken link (chain ledger malformed: {type(e).__name__})', 1


def _verify(run):
    j = Journal(run)
    try:
        recs = j.ledger()
    except (OSError, ValueError) as e:
        return f'journal: first broken link at entry 0 (chain ledger unreadable: {e})', 1
    if not recs:
        return 'journal: not kept (no chain)', 1
    data, pos = {}, {}
    for fname in ('journal.md', 'transcript.md'):
        p = j.path(fname)
        data[fname] = open(p, 'rb').read() if os.path.exists(p) else None
        pos[fname] = 0
    prev, entry, wtf, last_entry, st = GENESIS, 0, 0, 0, {'open': None, 'ran': False}
    for i, r in enumerate(recs):
        entry = r.get('entry', last_entry) if isinstance(r, dict) else last_entry
        if not isinstance(entry, int) or isinstance(entry, bool):
            entry = last_entry
        broken = lambda why: (f'journal: first broken link at entry {entry} ({why})', 1)
        if not (isinstance(r, dict) and isinstance(r.get('file'), str) and isinstance(r.get('kind'), str)
                and isinstance(r.get('length'), int) and not isinstance(r.get('length'), bool) and r['length'] >= 0
                and isinstance(r.get('hash'), str) and isinstance(r.get('prev'), str)):
            return broken(f'ledger line {i + 1} is malformed')
        fname, kind, length = r['file'], r['kind'], r['length']
        if r.get('seq') != i + 1 or r.get('prev') != prev:
            return broken(f'ledger line {i + 1} is out of order')
        if fname not in data:
            return broken(f'ledger line {i + 1} names an unknown file')
        if data[fname] is None:
            return broken(f'{fname} is missing')
        chunk = data[fname][pos[fname]:pos[fname] + length]
        h = block_hash(prev, kind, entry, fname, chunk)
        if len(chunk) != length or h != r.get('hash'):
            return broken(f'{fname} {kind} block at byte {pos[fname]} differs from what journal.py wrote')
        pos[fname] += length
        prev = h
        if kind == 'open':
            st = {'open': entry, 'ran': False}
            last_entry = entry
        elif kind == 'step':
            if st['open'] != entry or st['ran']:
                return broken('a step record with no open entry')
            out = j.step_out(entry)
            raw = open(out, 'rb').read() if os.path.exists(out) else None
            if raw is None or hashlib.sha256(raw).hexdigest() != r.get('out_sha256'):
                return broken(f'.journal/step-{entry}.out is missing or changed')
            st['ran'] = True
            st['step'] = r
        elif kind == 'close':
            if st['open'] != entry or not st['ran']:
                return broken('a line 4 with no step run')
            text = chunk.decode('utf-8', 'replace')
            happened = text.split('): ', 1)[1] if '): ' in text else text
            happened = '\n'.join(l[3:] if l.startswith('   ') else l for l in happened.rstrip('\n').split('\n'))
            if happened.lstrip().startswith('WTF?:'):
                wtf += 1
            elif quote_problem(happened, j.step_out(entry), st['step']):
                return broken('line 4 does not quote its step output')
            st = {'open': None, 'ran': False}
    for fname, d in data.items():
        if d is not None and len(d) > pos[fname]:
            entry = last_entry
            return f'journal: first broken link at entry {entry} ({fname} has {len(d) - pos[fname]} bytes journal.py did not write after its last block)', 1
    n = sum(1 for r in recs if r['kind'] == 'open')
    return f'journal: chain intact, {n} entries, {wtf} WTF', 0


def cmd_verify(j, a):
    line, code = verify(j.run)
    print(line)
    return code


def parser():
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument('--run', default=argparse.SUPPRESS, metavar='DIR', help='the run directory (default: run)')
    ap = argparse.ArgumentParser(prog='journal.py', description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--run', default='run', metavar='DIR', help='the run directory (default: run)')
    sub = ap.add_subparsers(dest='verb', metavar='VERB')
    sub.required = True
    p = sub.add_parser('start', parents=[common], help='write transcript.md\'s first line, `started: <UTC>`')
    p.set_defaults(fn=cmd_start)
    p = sub.add_parser('open', parents=[common], help='lines 1-3 of a new entry, before its step')
    p.add_argument('--read', required=True, metavar='TEXT', help='line 1: the document, section or message the step rests on')
    p.add_argument('--expect', required=True, metavar='TEXT', help='line 2: what the step will produce, concretely')
    p.add_argument('--chose', required=True, metavar='TEXT', help='line 3: what you are about to do, and the alternative you turned down and why')
    p.set_defaults(fn=cmd_open)
    p = sub.add_parser('run', parents=[common], help='run the open entry\'s one step: run -- COMMAND ARG...')
    p.add_argument('command', nargs=argparse.REMAINDER, help='the command and its arguments, after --')
    p.set_defaults(fn=cmd_run)
    p = sub.add_parser('close', parents=[common], help='line 4, after the step ran; must quote its output (see journal.py --help)')
    p.add_argument('--happened', required=True, metavar='TEXT', help='line 4: what the step produced, quoting >= 12 characters of its output, or beginning with WTF?:')
    p.set_defaults(fn=cmd_close)
    p = sub.add_parser('end', parents=[common], help='the journal\'s "At the end" section')
    p.add_argument('--guessed', required=True, metavar='TEXT', help='every value you wrote without a source, and what you would have needed to read')
    p.add_argument('--missing', required=True, metavar='TEXT', help='questions no document or message answered')
    p.set_defaults(fn=cmd_end)
    p = sub.add_parser('finish', parents=[common], help='write transcript.md\'s last line, `finished: <UTC>`, after the last grader run')
    p.set_defaults(fn=cmd_finish)
    p = sub.add_parser('verify', parents=[common], help='check the chain; prints one line, exit 0 only when intact')
    p.set_defaults(fn=cmd_verify)
    return ap


def main(argv=None):
    a = parser().parse_args(argv)
    if a.verb == 'run' and a.command and a.command[0] == '--':
        a.command = a.command[1:]
    try:
        return a.fn(Journal(a.run), a)
    except Refused as e:
        print(f'journal.py {a.verb}: REFUSED: {e}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
