#!/usr/bin/env python3
"""Search the full-paper reading notes (24 papers); standard library only.

Examples:
  python3 scripts/find_notes.py --list
  python3 scripts/find_notes.py --id micro-2024-vnpu --heading overview
  python3 scripts/find_notes.py --query takeaway --heading evaluation --limit 8
  python3 scripts/find_notes.py --type benchmark --heading "what the benchmark is"
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HEADING = re.compile(r'^#{2,4}\s*(\d+)\.\s*(.*)$')


def load_index():
    return json.loads((ROOT / 'data/full-paper-index.json').read_text())['papers']


def sections(text):
    """Split a note into (number, title, body) at its numbered headings."""
    out, current = [], ('', 'preamble', [])
    for line in text.split('\n'):
        match = HEADING.match(line)
        if match:
            out.append(current)
            current = (match.group(1), match.group(2).strip(), [])
        else:
            current[2].append(line)
    out.append(current)
    return [(n, t, '\n'.join(b).strip()) for n, t, b in out if b or n]


def select(rows, args):
    for row in rows:
        if args.id and row['id'] != args.id:
            continue
        if args.venue and row['venue'].lower() != args.venue.lower():
            continue
        if args.recognition and row['recognition'] != args.recognition:
            continue
        if args.type and args.type.lower() not in row['paper_type'].lower():
            continue
        yield row


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--id')
    parser.add_argument('--venue', choices=['ISCA', 'MICRO', 'HPCA', 'ASPLOS', 'MLSys', 'arXiv'])
    parser.add_argument('--recognition', choices=['best_paper', 'best_paper_runner_up', 'best_paper_candidate', 'reference_benchmark'])
    parser.add_argument('--type', help='substring of the paper type, for example benchmark or co-design')
    parser.add_argument('--heading', help='substring of a note heading, for example overview, introduction, evaluation')
    parser.add_argument('--query', nargs='+', help='all terms must appear on the same line')
    parser.add_argument('--limit', type=int, default=20, help='maximum matching lines printed with --query')
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--format', choices=['markdown', 'json'], default='markdown')
    args = parser.parse_args()

    rows = list(select(load_index(), args))
    if args.list or not (args.id or args.heading or args.query):
        if args.format == 'json':
            print(json.dumps(rows, indent=2))
        else:
            for r in rows:
                print(f"{r['id']} | {r['venue']} {r['year']} | {r['recognition']} | {r['paper_type']} | {r['title']}")
        return

    terms = [t.lower() for t in (args.query or [])]
    hits, printed = [], 0
    for row in rows:
        text = (ROOT / row['note']).read_text()
        for number, title, body in sections(text):
            if args.heading and args.heading.lower() not in title.lower():
                continue
            if terms:
                for line in body.split('\n'):
                    low = line.lower()
                    if all(t in low for t in terms):
                        hits.append({'id': row['id'], 'section': f'{number}. {title}'.strip('. '), 'line': line.strip()})
            else:
                hits.append({'id': row['id'], 'section': f'{number}. {title}'.strip('. '), 'text': body})
    if terms:
        hits = hits[:args.limit]
    if args.format == 'json':
        print(json.dumps(hits, indent=2))
        return
    for h in hits:
        if 'line' in h:
            print(f"- {h['id']} [{h['section']}] {h['line']}")
        else:
            print(f"## {h['id']}: {h['section']}\n\n{h['text']}\n")
    if not hits:
        print('no matches')


if __name__ == '__main__':
    main()
