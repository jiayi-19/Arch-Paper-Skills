---
name: computer-architecture-writing
description: Develop, draft, revise, or review HPCA, ASPLOS, ISCA, and MICRO papers with a complete intake-to-delivery workflow, annotated architecture-paper moves, empirical style profiles, figure templates, evidence checks, and notes from 24 full prize and benchmark papers on argument frames, contribution lists, overviews, design and evaluation structure and benchmark writing. Use for research storylines, paper sections, evaluations, figures and rebuttals; not ordinary code documentation or generic English proofreading.
metadata:
  short-description: Architecture writing with annotated moves and evidence checks
---

# Computer Architecture Writing

Build the argument from an actual hardware/systems problem, an exploitable insight,
a concrete mechanism, and evidence supporting its effect. Preserve the author's
research object and terminology. Use the requested edit scope; a paragraph revision
does not require restarting the complete paper workflow.

A focused paper is held together by one short numbered frame (usually three or four items) that names what
existing work lacks. The same words then become the contribution items, the design sections, the overview
labels and the evaluation questions, in the same order. About twelve of 20 prize papers in the full-paper
notes do this. Build the frame before prose: [argument frame](references/argument-frame.md). A contribution
item states a finding or a capability with an effect, not a component and a count:
[contributions](references/contributions.md).

## Full workflow and task routing

For a new or substantial paper, follow [the complete workflow](references/workflow.md):
intake/fact recovery -> contribution route -> claim/evidence map -> paragraph and
figure skeleton -> drafting -> source/visual integration -> checks -> author delivery.
For existing prose, enter at its relevant stage and preserve established facts.

| Work | Read and use |
|---|---|
| Intake JSON, free-form notes or an existing abstract | [Intake](references/intake-form.md); offline [form](assets/intake_form.html), converter and claim ledger. Recover present/vague/missing facts without blocking supported work. |
| Story, contribution type and motivation | [Routing](references/routing.md), [argument design](references/argument-design.md), [claim calibration](references/claim-calibration.md). Identify the residual technical cost and each claim's support. |
| Abstract and Introduction/Background | [Abstract](references/abstract.md), [Introduction](references/introduction.md). Use a direct, gap-led or insight-led version when it fits; offer alternatives only when useful. |
| Argument frame and contributions | [Argument frame](references/argument-frame.md), [contributions](references/contributions.md). One numbered frame reused from Introduction to evaluation. Findings and capabilities with an effect. |
| Overview, design and evaluation structure | [Whole-paper structure](references/full-paper-structure.md): length, chain and moves for the overview, design sections, evaluation, related work and conclusion, from 24 full papers. |
| Benchmark or agent-evaluation papers | [Benchmark papers](references/benchmark-papers.md): what the benchmark guarantees, ownership boundary, fixed and free conditions, enforcement evidence, what a results section proves. |
| Design and results | [Method](references/method.md), [experiments](references/experiments.md), [architecture evaluation](references/architecture-evaluation.md). Explain operations, conditions, control comparisons and costs. |
| Figures, tables and LaTeX | [Figures](references/figures.md), [LaTeX output](references/latex-output.md), [templates](assets/figures/). Use specified mechanisms and actual data. |
| Revision, related work and rebuttal | [Revision/delivery](references/revision-and-delivery.md); retain terminology and change unsupported meanings explicitly. |
| Paragraph/sentence examples and empirical style | [Corpus](references/corpus.md), [measured profile](references/corpus-profile.md), [style advice](references/style-rules.md), [sentence patterns](references/sentence-patterns.md), then retrieve by function/section. |
| Whole-paper examples | [Full-paper corpus](references/full-paper-corpus.md) and `scripts/find_notes.py`: a note for each of 24 papers covering overview, design, evaluation, figures. |
| Final review and an author's own rules | [Review checklist](references/review-checklist.md), [author preferences](references/author-preferences.md). |

## Work from the research

1. Read the supplied research and requested output at sufficient depth. Distinguish
   accepted observations, model estimates, hypotheses, historical results from another
   method and planned experiments. Ask only for a missing fact needed now.
2. Build the causal chain: operating regime -> bottleneck/invalid assumption ->
   credible prior alternative -> insight -> changed state/action/representation ->
   measurable consequence -> scope. A benchmark or measurement can contribute a
   capability/finding without proposing a faster machine.
3. Map headline/supporting claims to source paths and locators, comparison conditions,
   method subsections and tests. Use an existing results table when it serves this
   purpose; do not create parallel paperwork for a small edit.
4. Retrieve two or three relevant moves by paragraph function before topic. The
   development corpus has 24 fully annotated Abstract/Introduction pairs plus first
   figures. Published annotation records are text-free; source excerpts stay short
   and attributed. Learn information order and argument logic, not reusable sentences.
   For sections after the Introduction (overview, design, evaluation, benchmark definition)
   retrieve from the 24 full-paper notes with `scripts/find_notes.py --heading overview`.
5. Draft the requested sections. Name what is stored, transferred, scheduled,
   predicted or verified and why the next step is needed. Preserve the actual source
   values. Pending results remain explicit placeholders; mechanisms absent from the
   research stay unresolved rather than being invented.
6. Check sources, claims, references, figures and terminology across the paper.
   Distribution notes are revision questions, not rules forcing the text toward an
   average. Deliver the requested files and substantive author notes, using
   [the report template](assets/report-template.md) for substantial work.

## Evidence and style boundaries

- Attribute a gain to the intervention actually controlled. Resource scaling,
  parameter tuning, new mechanisms and algorithm changes can all matter and need
  corresponding comparisons.
- Keep simulated cycles, RTL observations, synthesis estimates, postlayout PPA,
  silicon measurements and extrapolations at their actual measurement stage/scope.
- Preserve the baseline, population, precision, clock, resource/service assumptions,
  metric units and aggregation needed to interpret a headline.
- State material qualifications or adverse regimes near a claim when omitting them
  changes its meaning. Detailed failure analysis can follow in Evaluation/Discussion.
- Credit closest work with a checkable difference; verify bibliography entries and
  claims rather than manufacturing citations, completed experiments or priority.
- Annotation labels are model judgments, not human ground truth. Corpus percentiles
  describe the selected development sample. Do not infer universal conference style,
  mandatory punctuation, figure counts or acceptance guarantees.
- The four held-out cases and grading keys are evaluation-only. Do not use them for
  normal exemplar retrieval, drafting-rule development or percentile calibration.
  Read [evaluation protocol](evals/README.md) only when running the evaluation.

## Toolchain

Run from the skill directory (or use absolute script paths):

```bash
python3 scripts/intake_to_brief.py intake.json --out brief.md --ledger claims.json
python3 scripts/find_exemplars.py --function limitation --section introduction
python3 scripts/style_metrics.py abstract.tex --section abstract
python3 scripts/find_notes.py --list
python3 scripts/find_notes.py --heading overview --type system
python3 scripts/check_draft.py abstract.tex --section abstract --brief brief.md
python3 scripts/check_manuscript.py paper/main.tex
python3 scripts/check_figures.py paper/main.tex
python3 scripts/analyze_corpus.py --from-public
```

[Plotting](references/figures.md) additionally uses Matplotlib; the other helpers
use the standard library. Metric dictionaries and heuristics are transparent in
`scripts/writing_metrics.py`. Source checks neither compile nor verify scientific
truth. Preserve the user's rendering/push preferences; this skill grants no external
publication or experiment permission. Paper prose follows manuscript language;
author discussion follows the user's language. Current official venue/year rules
override remembered templates.

Attribution: [NOTICE.md](NOTICE.md). Dataset construction and source limitations:
[annotation protocol](data/annotation-protocol.md) and
[corpus maintenance](references/corpus-maintenance.md).
