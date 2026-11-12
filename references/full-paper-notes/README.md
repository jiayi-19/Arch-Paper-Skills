# Full-paper reading notes

One note for each of 24 papers: 20 prize-level papers (ISCA, MICRO, HPCA, ASPLOS Best Paper, Runner-up or
Candidate, 2020 to 2026) and four benchmark papers read as models for benchmark writing (MLPerf Inference,
MLPerf Training, ArchGym, RobotPerf). The abstract and introduction of the first 24 development papers are
annotated in `data/annotations/`. These notes read the whole paper, so they cover what the annotations do not:
the overview, the design sections, the evaluation, figures and sentence habits.

Metadata: `../../data/full-paper-index.json`. Search: `python3 scripts/find_notes.py --help`.

## Template

Each note follows the same headings. For the 20 prize papers: 0 Identity, 1 Skeleton, 2 Abstract, 3 Introduction,
4 Motivation and background, 5 Overview of the design, 6 Design sections, 7 Evaluation, 8 Sentence and
paragraph habits, 9 Figures and tables, 10 Why it reads as strong and what does not transfer.

The four benchmark notes keep headings 0 to 3, replace 4 to 10 with benchmark headings (what the benchmark is,
why it is needed, task and rule definition, construction and coverage, use and results, patterns to reuse, what
transfers), and then number the sentence, figure and takeaway headings 11 to 13. Use
`find_notes.py --heading` with a word from the heading and not a number.

## Limits

- The notes are model-written readings, not human gold. Word and sentence counts come from PDF text extraction
  of two-column layouts and are approximate. Some papers were read in an arXiv version that can differ from the
  camera-ready text.
- Award status comes from the official listings named in the index. Two ids (`hpca-2025-dynamollm`,
  `hpca-2024-pim-pathfinding`) take their recognition from `references/corpus.json`. The venue of
  `isca-2020-mlperf-inference` is not printed in the PDF read.
- Notes hold paraphrase, counts, patterns with blanks and short attributed quotations (at most 25 words each).
  No source passages, captions or PDFs are redistributed. Learn the argument move and do not copy the wording.
- Prose style differs. The notes record dash and semicolon counts per paper. Do not take sentence rhythm from a
  paper that is heavy in marks the author does not use.
