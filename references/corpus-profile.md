# Measured architecture writing profile

Development set: 24 curated papers (six each HPCA, ASPLOS, ISCA and MICRO), complete Abstract and Introduction sections. Labels come from model-agent source reading and deterministic structural checks, not human ground truth or a random sample. Contribution bullets and standalone lead-ins are counted as source sentence/fragment units.

Coverage: 1101 labeled units in 278 paragraphs across 48 complete sections. First-figure metadata are recorded for 24 papers.

## Per-paper distributions

Quantiles use linear interpolation at (n−1)q. Complete development sections only; held-out writing briefs and outputs do not enter these distributions.

| Section / metric | n | p10 | median | p90 |
|---|---:|---:|---:|---:|
| abstract / word_count | 24 | 163.00 | 226.00 | 290.00 |
| abstract / sentence_count | 24 | 7.00 | 9.00 | 12.00 |
| abstract / paragraph_count | 24 | 1.00 | 2.00 | 3.00 |
| abstract / mean_sentence_words | 24 | 18.25 | 23.67 | 28.32 |
| abstract / numbers_per_100_words | 24 | 0.00 | 1.50 | 2.83 |
| abstract / connectors_per_100_words | 24 | 0.00 | 0.39 | 0.74 |
| abstract / hedges_per_100_words | 24 | 0.00 | 0.00 | 0.44 |
| abstract / boosters_per_100_words | 24 | 0.00 | 0.40 | 1.14 |
| abstract / trailing_participial_sentences_pct | 24 | 0.00 | 0.00 | 0.00 |
| introduction / word_count | 24 | 561.20 | 762.00 | 1083.30 |
| introduction / sentence_count | 24 | 25.30 | 35.00 | 51.70 |
| introduction / paragraph_count | 24 | 6.00 | 9.50 | 13.40 |
| introduction / mean_sentence_words | 24 | 19.17 | 21.87 | 28.56 |
| introduction / numbers_per_100_words | 24 | 0.47 | 1.49 | 3.08 |
| introduction / connectors_per_100_words | 24 | 0.11 | 0.35 | 0.68 |
| introduction / hedges_per_100_words | 24 | 0.00 | 0.07 | 0.38 |
| introduction / boosters_per_100_words | 24 | 0.00 | 0.32 | 0.68 |
| introduction / trailing_participial_sentences_pct | 24 | 0.00 | 0.00 | 5.09 |

## Annotated functions

Roles describe what a sentence primarily contributes to the argument. A secondary role may be present. Labels are context-dependent; observation/insight and mechanism/contribution boundaries can be ambiguous.

| Function | Abstract units | Introduction units |
|---|---:|---:|
| context | 28 | 112 |
| contribution | 33 | 95 |
| insight | 12 | 48 |
| limitation | 15 | 80 |
| mechanism | 54 | 142 |
| methodology | 11 | 34 |
| observation | 6 | 63 |
| prior_work | 9 | 80 |
| problem | 19 | 81 |
| result | 39 | 72 |
| roadmap | 0 | 44 |
| scope | 3 | 21 |

## First figures

Inspected type counts: motivation_plot=10, concept=6, other=2, mechanism_diagram=3, system_overview=3.

Caption word count: n=24, median=21.0, p10–p90=6.3–50.2. These are first-caption observations, not rules for all captions or template layout.

## How to use the profile

Look at function order, causal links and the needs of the actual research. A text outside p10–p90 may be appropriate. Lexical dictionaries, sentence heuristics, passive proxies and numeric-token rules are transparent in `scripts/writing_metrics.py`; they do not establish semantic quality.

Reproduce all published distributions and move sequences without copyrighted source text:

```bash
python3 scripts/analyze_corpus.py --from-public
```

To rebuild individual lexical measurements, supply privately obtained normalized/annotated source passages to `--private-passages`. Public [annotation records](../data/annotations/) contain labels, source URLs/pages, Unicode offsets, lengths, paragraph paraphrases and per-section metrics; complete source passages and captions are not redistributed. Read [the protocol](../data/annotation-protocol.md) and the two annotation-notes files for extraction/OCR boundaries and uncertainty.

## Independent annotation consistency sample

A second model agent labeled 48 systematically sampled units with the original labels withheld: 40/48 exact primary-role agreement (83.3%), Cohen’s kappa 0.806. This is model-to-model consistency on a small selected sample, not human inter-annotator reliability or proof of annotation correctness. Disagreements and rationales are retained in [the review record](../data/annotation-review.json). Labels were not automatically rewritten to maximize agreement.
