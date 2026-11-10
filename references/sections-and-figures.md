# Sections and figures

Use these section roles to avoid repetition. They are adaptable, not a fixed table
of contents or a paper-length prescription.

## Title and abstract

Name the research object and discriminating mechanism or finding. A memorable system
name is useful when the title still communicates what the work does. Novelty words
alone do not position a contribution.

An abstract usually needs the setting/problem, technical obstacle, insight and
mechanism, strongest supported result, and material scope. Choose the order that
makes the result intelligible. A measurement or benchmark paper may emphasize the
new observation or evaluation capability rather than a hardware speedup.

Keep a headline number's denominator and scope recoverable. Use only finished,
source-backed results; a result-free early draft can describe the research question
and method with explicit pending text. Avoid turning a planned protocol into a past
experiment. An important limitation belongs in the abstract if it changes the meaning
of the headline, such as kernel-only scope or a gain restricted to a workload regime.

## Introduction and Background/Motivation

See [argument design](argument-design.md). Introduction gives the problem, answer,
and evidence. Background supplies needed concepts. Motivation shows why the obvious
solution or existing abstraction is insufficient and derives design requirements.
Use an illustrative example as an illustration and a measured result as a measured
result. Keep closest-work distinctions concrete and credit inherited ideas.

## Design or mechanism

Open with the object the reader will understand: a predictor, controller, dataflow,
compiler/runtime interface, model, or design organization. Explain inputs, outputs,
state, ownership, transitions and interactions at the depth needed to reproduce the
contribution. A useful subsection chain is need -> mechanism -> expected consequence
-> cost or constraint.

For hardware, show one worked operation or state transition through the data path.
For HW/SW work, show the contract between compile-time and runtime/hardware choices.
For an agent system, show an observation, the action it justified, the resulting
hardware change, and an independent check. A transcript of reasoning is process
material; hardware measurements carry the performance claim.

Name reused mechanisms, parameter domains, legal instantiation and unsupported cases.
A diagram that labels compute/memory/network boxes needs enough explanation of what
is scheduled, transferred, retained or arbitrated to establish the actual design.

## Benchmark and methodology

A benchmark defines the task and acceptance interface independently of the evaluated
agent. Distinguish architecture family, native case, optimization task, test instance
and repetition before quoting counts. Explain baseline provenance, implementation
simplifications, edit freedom, correctness, timing and metric eligibility.

Methodology describes what this study actually did: workload selection, methods,
versions, task splits, optimization budgets, metric definitions, repetitions and
failure treatment. Results describe the findings. Separating them prevents a general
capability from being presented as an already completed experiment.

## Results, related work and conclusion

Arrange results around the questions needed for the claims. Begin with overall
quality and coverage, then explain mechanism/parameter attribution, overhead and
sensitivity. Put detailed protocol next to the result when it affects interpretation.
A result order is justified by the paper's argument, not by an expected section name.

Related work compares dimensions: assumptions, design freedom, evaluation coverage,
mechanisms, scope and cost. Credit the closest work at its first meaningful point of
comparison as well as in the dedicated discussion. Conclusion returns to what was
established, with the same scope as the abstract; it introduces no new result.

## Figure and table design

Plan each visual by the question it answers and the material needed to answer it.
A first figure can expose a bottleneck, explain a contrast, summarize a system or
show the main observation. It need not be a teaser, occupy page one, or use full width.
Use the venue's actual template and the argument's reading order.

| Visual | What makes it informative |
|---|---|
| Motivating plot | Real workload or machine measurements, conditions, units, and the observation the design exploits. |
| Mechanism diagram | Baseline and new action, data/control directions, relevant state, and a worked operation. |
| Evaluation/agent loop | Frozen task/scorer boundary, observations, editable state, acceptance and final evaluation; distinguish hardware and policy updates. |
| Performance plot | Per-workload outcomes, normalization baseline, aggregation, failures, and variability where applicable. |
| Ablation/sensitivity plot | Controlled change, held-fixed conditions, response metric, and regime where benefit disappears. |
| Coverage table | Count unit, task freedom, correctness/mechanism/timing qualifications, and unavailable metrics. |
| Pareto plot | Resource axis and performance scope, non-dominated points, feasible region and comparable evaluation conditions. |

Use one consistent encoding for a mechanism or method across figures; distinguish
alternatives without color alone. Put units on axes, specify log scales and explain
normalization. Captions state the supported takeaway plus conditions needed to read
it; a descriptive caption is appropriate when no result is being asserted.

Preserve data values in any plotting transformation and retain the underlying table.
Schematics can be drawn once the mechanism is established. Empirical plots require
real data. Missing results remain visibly pending, not smooth hypothetical curves
presented as measurements. Publication figures should be standalone vector assets
where appropriate, using actual data and standard plotting/diagramming tools.

## Sentence-level revision

Keep the actor, action and consequence visible: the directory records sharers; the
scheduler defers a transfer; a bypass avoids a buffer write. Replace a vague benefit
with a measurable effect or a mechanism explanation. Use connected paragraphs rather
than consecutive slogan sentences or parallel descriptions of components.

Technical detail belongs where it determines the mechanism, reproducibility or
interpretation. Keep names stable. Remove duplicate work between motivation and
method, and between methodology and results. Adapt rhythm and sentence length to the
argument; the corpus provides examples, not numerical quotas or a phrase bank.
