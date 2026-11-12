"""Contracts for the full-paper notes, their index and the notes search tool; no network."""
import json
from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
NOTES = ROOT / 'references/full-paper-notes'
INDEX = json.loads((ROOT / 'data/full-paper-index.json').read_text())['papers']
PRIVATE = re.compile(r'(/scratch3|/home/|/tmp/|ArchOrchestra|Overleaf|study list|papers\.md|agentic accelerator)', re.I)


class FullPaperNotes(unittest.TestCase):
    def test_index_matches_files(self):
        ids = [p['id'] for p in INDEX]
        self.assertEqual(len(ids), 24)
        self.assertEqual(len(set(ids)), 24)
        files = {f.stem for f in NOTES.glob('*.md')} - {'README'}
        self.assertEqual(files, set(ids))
        for p in INDEX:
            self.assertTrue((ROOT / p['note']).exists())
            self.assertIn(p['recognition'], ['best_paper', 'best_paper_runner_up', 'best_paper_candidate', 'reference_benchmark'])
            if p['recognition'] != 'reference_benchmark':
                self.assertTrue(p['recognition_source'], p['id'])
            self.assertTrue(p['full_text_url'], p['id'])

    def test_overlap_ids_exist_in_first_corpus(self):
        corpus = {e['id'] for e in json.loads((ROOT / 'references/corpus.json').read_text())}
        flagged = {p['id'] for p in INDEX if p['in_abstract_intro_corpus']}
        self.assertEqual(flagged, {'asplos-2024-centauri', 'isca2024-constable', 'hpca-2025-dynamollm', 'hpca-2024-pim-pathfinding', 'micro-2024-nocap'})
        self.assertTrue(flagged <= corpus)

    def test_notes_have_template_headings_and_no_private_text(self):
        for p in INDEX:
            text = (ROOT / p['note']).read_text()
            heads = re.findall(r'^#{2,4}\s*(\d+)\.', text, re.M)
            self.assertTrue({'0', '1', '2', '3'} <= set(heads), p['id'])
            self.assertIsNone(PRIVATE.search(text), p['id'])
            self.assertTrue(text.startswith('# ' + p['id']), p['id'])

    def test_quotations_are_short(self):
        for p in INDEX:
            for line in (ROOT / p['note']).read_text().split('\n'):
                pos = [i for i, c in enumerate(line) if c == '"']
                if len(pos) % 2:
                    continue
                for a, b in zip(pos[0::2], pos[1::2]):
                    quote = line[a + 1:b]
                    if '[' in quote or '___' in quote:
                        continue
                    self.assertLessEqual(len(quote.split()), 25, (p['id'], quote[:60]))

    def test_find_notes_tool(self):
        run = lambda *a: subprocess.check_output([sys.executable, str(ROOT / 'scripts/find_notes.py'), *a], text=True)
        self.assertEqual(len(run('--list').strip().split('\n')), 24)
        rows = json.loads(run('--list', '--format', 'json', '--recognition', 'reference_benchmark'))
        self.assertEqual(len(rows), 4)
        hit = run('--id', 'micro-2024-vnpu', '--heading', 'overview')
        self.assertIn('Overview', hit)
        hits = json.loads(run('--query', 'takeaway', '--heading', 'evaluation', '--format', 'json', '--limit', '50'))
        self.assertTrue(hits)
        self.assertTrue(all('takeaway' in h['line'].lower() for h in hits))
        bench = run('--type', 'benchmark', '--heading', 'what the benchmark is')
        self.assertIn('mlperf', bench)


if __name__ == '__main__':
    unittest.main()
