#!/usr/bin/env python3
"""Hold the examinee README to its size, headings and undated overview role."""
import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
# Card #67: ceil(1,893 * 1.10 / 50) * 50; no earlier lower exam cap.
WORD_CAP = 2100
HEADINGS = {
    'What this exam proves', 'Results', 'Rules', 'Layout', 'Sitting it',
    'Submitting', 'What is in a round', 'Licence',
}


def violations(text):
    errors = []
    words = len(text.split())
    if words > WORD_CAP:
        errors.append(f'README_WORD_CAP: {words} words exceeds {WORD_CAP}')

    fence = None
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line)
        if fence:
            if (marker and marker[1][0] == fence[0] and
                    len(marker[1]) >= len(fence) and not marker[2].strip()):
                fence = None
            continue
        if marker:
            fence = marker[1]
            continue
        heading = re.match(r'^ {0,3}##(?:[ \t]+(.*?))?[ \t]*$', line)
        if heading:
            title = re.sub(r'[ \t]+#+[ \t]*$', '', heading[1] or '').strip()
            if title not in HEADINGS:
                errors.append(f'README_HEADING: line {number}: {title or "(empty)"}')
        if '|' in line and re.search(r'\b\d{4}-\d{2}-\d{2}\b', line):
            errors.append(f'README_TABLE_DATE: line {number}')

    # Preserve line breaks so a wrapped measurement phrase cannot evade the bar.
    for phrase in re.finditer(r'\b(?:measured|read)\s+on\s+20', text, re.IGNORECASE):
        number = text.count('\n', 0, phrase.start()) + 1
        wording = ' '.join(phrase[0].split())
        errors.append(f'README_DATED_PHRASE: line {number}: {wording}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('readme', nargs='?', type=Path, default=ROOT / 'README.md')
    args = parser.parse_args()
    text = args.readme.read_text(encoding='utf-8')
    errors = violations(text)
    if errors:
        print('\n'.join(errors))
        return 1
    print(f'README_OK: {len(text.split())}/{WORD_CAP} words; headings and dates pass')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
