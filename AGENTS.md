# Documentation maintenance

The README is what a person reads to decide and to get a first result: what the
package is, install, one first run with its output shown, one line per command
with a link, and links. For this exam, it keeps the rules, how to sit and submit,
and the layout, including the manual build example.

It holds no flag lists, refusal catalogues, dated or machine-specific figures,
version history, or licence text beyond a pointer. A feature PR adds at most one
line to it. Existing sections that a card does not name are not rewritten as
part of a mechanical move.

Move history to `ROUNDS.md` without rewriting it. Keep inbound headings as
one-sentence link stubs, check this repo's tests and other rig-c docs (including
the site's `src/external-links.test.ts`), and repoint content-reading tests in the
same change. Use an absolute GitHub document URL for a target that is not in the
package's `files` list.

Run `python3 -B tools/check_readme.py` and
`python3 -B -m unittest discover -s tools -p 'test_readme.py' -v` after README
changes. The check holds the raw Markdown whitespace word count to 2,100 words,
the explicit `##` allowlist, and the dated-phrase/table-date restrictions. The
cap comes from the post-cut 1,893 words plus 10%, rounded up to 50; any earlier
lower cap takes precedence. Do not raise it for a feature PR or remove a content
pin to make a check pass. Keep `results.py --check` and the existing results and
manual-build documentation tests green.
