# Computer Architecture Writing Skill

A complete evidence-led paper-writing workflow for **HPCA, ASPLOS, ISCA and MICRO**:
research intake, contribution routing, claim/evidence maps, sentence/paragraph plans,
drafting, figures, source checks, revision and author delivery.

## Version 2: architecture-derived analysis and tools

- **24 development papers**, six per venue, with complete Abstract and Introduction
  annotations: **48 sections, 278 paragraphs and 1,101 sentence/source-fragment units**.
- **24 inspected first figures**, with type, source page, caption measurements and
  layout metadata where recoverable.
- Transparent per-paper lexical measurements, role transitions, paragraph functions,
  p10/median/p90 distributions and an independent 48-unit annotation consistency sample.
- A full offline intake form, structured brief/evidence converter, function-level
  exemplar retrieval, style/draft/source/figure checks and independent template copy.
- TikZ mechanism/contrast diagrams, comparison/coverage tables, and actual-data vector
  plots for bars, scaling sequences, breakdowns and resource/performance tradeoffs.
- **Four new held-out source papers**, one per venue, with writer briefs, source keys,
  blind comparison tooling and an auditable evaluation protocol.

The corpus includes Best Papers, formal candidates/nominees or Best Paper Session
entries, named Influential/Test of Time award recipients and notable teaching selections.
[Paper index](references/corpus.md), [measured profile](references/corpus-profile.md),
[annotation protocol](data/annotation-protocol.md), [evaluation protocol](evals/README.md).

These are model annotations of selected papers, not human gold or statistical evidence
about all award papers. The independent sample has 40/48 exact role agreement (83.3%,
Cohen's kappa 0.806). Full source passages and captions are not redistributed: public
records contain labels, offsets, lengths, source locators and original paraphrases.

## What the measured corpus says

For these 24 selected papers, Abstract word count has median **226** and p10–p90
**163–290**; Introduction median **762**, p10–p90 **561.2–1083.3**. First-caption length
has median **21 words**, p10–p90 **6.3–50.2**. The most common inspected first-figure
category is a motivation plot (10/24). These describe the sample, not mandatory prose
lengths, placements or figure counts. Definitions and limitations are in the profile.

The argument-level lessons remain concrete: expose the residual bottleneck after
credible prior work, explain the changed mechanism, compare under explicit conditions,
validate the feedback/model at its intended scope and report the tradeoff the data support.
Use role sequences and examples to reason about information order, not to copy sentences.

## Install and invoke

For a fresh Codex skill installation:

```bash
git clone https://github.com/jiayi-19/Arch-Paper-Skills.git ~/.codex/skills/computer-architecture-writing
```

Use `$CODEX_HOME/skills/computer-architecture-writing` when configured. Preserve an
existing installation before replacement. Other skill-capable agents can load
`SKILL.md` with its relative resources. Do not include repository metadata or caches
when manually copying the skill.

```text
Use $computer-architecture-writing to develop a research argument and draft the
requested paper sections from this mechanism, source material, and verified evidence.

Use $computer-architecture-writing to revise this evaluation for fair baselines,
mechanism attribution, workload scope, uncertainty and measurement-stage qualification.
```

The workflow is generic across architecture topics and is not tailored to a particular
paper or project. The skill respects the requested edit scope and session's rendering/
publication preferences. It does not authorize experiments or remote publication itself.

## Complete workflow

1. Recover facts from notes, source/draft, or [offline intake form](assets/intake_form.html).
2. Route by contribution/motivation and construct a sourced claim/evidence map.
3. Plan paragraph functions and visuals; retrieve relevant annotated moves.
4. Draft the requested abstract, introduction, background, design and evaluation.
5. Integrate real bibliography, data-driven figures and the actual venue template.
6. Review source, rhetoric, figures and scientific evidence; interpret statistical
   outliers in context rather than forcing prose toward the corpus median.
7. Deliver the manuscript and an author report; update affected claims after changes.

Detailed [workflow](references/workflow.md); substantial-work
[report template](assets/report-template.md).

## Tools

Python **3.10+**; all tools except plotting use the standard library.
Install `requirements-figures.txt` only for Matplotlib-based plotting.

```bash
python3 scripts/intake_to_brief.py intake.json --out brief.md --ledger claims.json
python3 scripts/find_exemplars.py --function limitation --section introduction
python3 scripts/find_exemplars.py --paragraph gap --section introduction --limit 3
python3 scripts/find_exemplars.py --id isca2016-eyeriss
python3 scripts/style_metrics.py abstract.tex --section abstract
python3 scripts/check_draft.py abstract.tex --section abstract --brief brief.md
python3 scripts/check_manuscript.py paper/main.tex
python3 scripts/check_figures.py paper/main.tex
python3 scripts/prepare_paper.py --template official-kit --out independent-draft
python3 scripts/analyze_corpus.py --from-public
```

The final command reproduces all published corpus summaries without copyrighted text.
Recomputing individual lexical metrics from original source requires privately obtained
normalized passages, as specified by `--private-passages` and the annotation protocol.
Exemplar retrieval reads development data only; evaluation cases/keys are excluded.

### Figures

```bash
python3 scripts/plot_results.py results.csv --out latency.svg --kind bars \
  --data-kind measured --y-label 'Latency (ms)'
```

CSV fields: `case,method,value,status`, optional `resource` for tradeoff plots.
Statuses are `valid`, `invalid`, `not_measured`; unavailable rows have empty values.
Do not omit failures. `--normalize-to` computes candidate/baseline; label the resulting
ratio accordingly. Outputs are vector SVG/PDF plus an auditable transformation record.
[Figure guide](references/figures.md), [templates](assets/figures/).

Synthetic demonstration data are marked as synthetic and never treated as research
results. The helper checks do not compile/render a paper. A data-plot integration test
may generate a clearly marked synthetic vector image in temporary storage.

## Evaluation and testing

```bash
python3 -m unittest discover -s tests -v
python3 evals/score_outputs.py --briefs evals/writer-briefs.json \
  --outputs evals/outputs/skill --out skill-metrics.json
```

The writing holdout compares the same factual briefs and word/paragraph budgets with
and without the frozen skill. Candidate identities are randomized for a separate judge.
Fact coverage, numeric/baseline/scope errors, mechanism, evidence, positioning and economy
are scored with explicit rules. Read [the protocol](evals/README.md) for source isolation,
pretraining limits and the distinction between mechanical checks and semantic judgment.
No acceptance-rate, productivity or statistical superiority claim follows from four cases.

## Key resources

- `SKILL.md`: scope-adaptive entrypoint.
- `references/`: workflow, contribution routes, section guidance, empirical profile,
  evaluation/figure rules and the source-located exemplar index.
- `data/annotations/`: text-free per-paper sentence/paragraph and first-figure records.
- `data/corpus-stats.json`: development-only distributions, samples and move sequences.
- `data/annotation-review.json`: independent sample and disagreements.
- `assets/`: offline form, structured examples/report, TikZ/table/plot resources.
- `scripts/`: reusable workflow, analysis and source-check helpers.
- `evals/`: held-out briefs, source keys, blind comparison and score aggregation.
- `tests/`: functional contracts using synthetic fixtures.

## Attribution and rights

Adapted from workflow ideas in
[Best-Paper-Writing-Skill](https://github.com/gulucaptain/Best-Paper-Writing-Skill),
inspected at revision `b9eff99`. Its original content is CC BY 4.0; base-work MIT
attribution is retained. The architecture data, analysis, helpers and assets are
original adaptations. [NOTICE.md](NOTICE.md), [LICENSE](LICENSE),
[LICENSE-base-skill](LICENSE-base-skill).

Paper excerpts remain the property of their rights holders. Short excerpts support
commentary and instruction, not a phrase bank. Full PDFs, complete source prose,
private extraction files, credentials and personal host paths are not distributed.
