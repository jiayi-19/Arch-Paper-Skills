---
name: computer-architecture-writing
description: Develop, draft, revise, or review computer architecture research papers for HPCA, ASPLOS, ISCA, and MICRO using source-located paper exemplars and architecture-specific evidence checks. Use for paper storylines, abstracts, motivation, mechanisms, evaluation, figures, and rebuttals; not for ordinary code documentation or generic English proofreading.
metadata:
  short-description: Architecture papers grounded in mechanisms and evidence
---

# Computer Architecture Writing

Build a persuasive argument from a hardware or systems problem, a technical insight,
a concrete mechanism, and evidence that measures the claimed effect. Preserve the
author's intended contribution and established terminology.

## Choose the work

Use the user's requested scope. A paragraph edit needs a paragraph edit, not a new
paper outline. For a new story, organize the argument before drafting; for a mature
paper, diagnose and repair its existing argument. Conference membership or an award
does not prescribe one writing style.

Read only the references needed for the current work:

| Work | Reference and completion criterion |
|---|---|
| Storyline, outline, Background/Motivation, contribution | [Argument design](references/argument-design.md): each design choice answers an established problem and each main claim has identified support. |
| Abstract, Introduction, mechanism section, figures | [Sections and figures](references/sections-and-figures.md): the requested text explains its causal role and uses the same claim strength as the evidence. |
| Evaluation plan, results, quantitative claims | [Architecture evaluation](references/architecture-evaluation.md): comparisons share declared conditions; measured, modeled, and projected quantities stay distinct. |
| Rewriting, reviewer response, submission source | [Revision and delivery](references/revision-and-delivery.md): requested edits are reviewable and address the stated issue without unsupported additions. |
| Representative papers or writing examples | [Corpus guide](references/corpus.md), then retrieve selected cards with `scripts/find_exemplars.py`: transfer the argument move, retaining its applicability limits. |
| Add papers, check award provenance, inspect adaptation | [Corpus maintenance](references/corpus-maintenance.md) and [attribution](NOTICE.md): actual paper passages and recognition sources remain separately verifiable. |

## Work from the research

1. **Establish the evidence.** Read the supplied outline, manuscript, relevant code,
   configurations, results, and protocol at the depth needed for the request. Keep
   accepted results, hypotheses, planned experiments, and historical results for a
   different method distinguishable. State a narrow assumption when it permits useful
   progress; ask only when a missing fact blocks the requested writing.
2. **Form the argument.** Identify the problem and operating regime; the bottleneck
   or invalid assumption; why a reasonable existing approach leaves it unresolved;
   the insight; the mechanism; and the supported outcome. For a benchmark or measurement
   paper, the contribution can be an evaluation capability or empirical finding.
3. **Bind claims to evidence.** For substantial drafting, keep a compact ledger:
   claim; evidence basis; source path and locator; metric and comparison conditions;
   scope; missing support. An existing results table or author note can serve as this
   ledger. Do not create a second documentation system for a small edit.
4. **Retrieve suitable exemplars.** Choose by paragraph function and contribution
   type before topic. Use `python3 scripts/find_exemplars.py --help`; select two or
   three relevant cards, read the actual cards, and learn their information order.
   Exact excerpts are teaching material, not sentences to paste into the new paper.
5. **Draft or revise.** Connect the workload observation to the design choice and
   the design choice to a testable consequence. Name what moves, stores, schedules,
   predicts, or checks something; a component list alone does not explain a mechanism.
   Use the strongest wording the available evidence supports, with material scope
   near the claim. Results pending collection remain explicit drafting placeholders.
6. **Check and deliver.** Verify headline numbers against their sources, bibliography
   entries against real papers, section/figure references, and consistency of scope
   across abstract, introduction, contributions, and results. Deliver the requested
   text or source changes plus only consequential gaps or decisions for the author.
   A source checker is a limited aid, not scientific validation.

## Claim discipline

- Explain the hardware change, its operating condition, and the cost it introduces.
  Report the evidence for a benefit rather than declaring a design "novel" or
  "efficient" on the strength of a name or proposer identity.
- Keep simulated cycles, RTL observations, prelayout estimates, postlayout PPA,
  silicon measurements, and extrapolations labeled by their actual scope.
- Preserve the denominator and population of an improvement: over which baseline,
  at what clock/resource/precision, across which workloads, and with what aggregation.
- Use controls to support causal attribution. A larger array winning does not alone
  show that a new interconnect caused the gain. A functional test does not alone show
  that the proposed mechanism was implemented.
- State essential exclusions or adverse results wherever omitting them would change
  a headline's meaning. Detailed failure analysis can follow in Evaluation or Discussion.
- Credit specific closest work and explain a checkable difference. Mark an unverified
  citation or result as missing; do not manufacture bibliography records or measurements.
- Award recognition and citation fame are selection signals, not proof of writing
  quality or scientific correctness. The curated corpus is not a representative
  statistical sample; do not invent style percentiles, sentence-length targets,
  mandatory figure counts, or award-success guarantees.

## Output and workflow

Write paper prose in the manuscript's language, usually English. Discuss edits in
the user's language. Retain local terminology, macros, labels, bibliography keys,
and the requested outline unless a concrete issue warrants a proposed change.

Use an existing LaTeX project when supplied. Consult the current official instructions
for the actual venue/year when changing submission formatting; avoid transferring a
CVPR teaser or ACM/IEEE settings between conferences by habit. Follow the session's
workspace, rendering, commit, and push preferences. A request to skip local rendering
is satisfied with source checks and the authorized repository workflow. This skill
itself does not authorize publication, repository pushes, or new experiments.

Useful tools:

```bash
python3 scripts/find_exemplars.py --venue ISCA --topic memory
python3 scripts/find_exemplars.py --query 'bottleneck mechanism' --limit 3
python3 scripts/check_manuscript.py /path/to/paper/main.tex
```

Run source checks when useful for the actual change. Keep research and author-facing
notes outside anonymous submission text. Attribution and the corpus scope are in
[NOTICE.md](NOTICE.md) and [the corpus guide](references/corpus.md).
