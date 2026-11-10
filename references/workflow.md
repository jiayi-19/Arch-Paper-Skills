# Full writing workflow

Use the complete sequence for a new paper. Enter at the relevant stage for a local
revision; a requested paragraph edit does not require all artifacts below.

## 1. Intake and fact recovery

Accept free text, existing source/abstract, or offline `assets/intake_form.html`
export. For an existing draft, reverse-engineer problem, gap/reason, insight,
mechanism, closest work, claims and sources into a present/vague/missing table.
For JSON use `scripts/intake_to_brief.py intake.json --out brief.md --ledger claims.json`.
The converter checks structure, not truth. Consult code/results already available
before asking for facts. Missing measured results are pending evidence, not a reason
to invent a headline or block supported method drafting.

Done: requested output scope and the known/pending research facts are clear.

## 2. Route and claim calibration

Read [routing](routing.md) and [claim calibration](claim-calibration.md). Select a
contribution type and motivation. Explain the remaining technical cost after credible
prior work. Map each main claim to its mechanism subsection, experiment, source and
conditions. Keep measured, modeled, derived, planned and unavailable status explicit.

Done: every headline has support or an explicit pending marker; the route fits the
research object rather than forcing it into a hardware-speedup narrative.

## 3. Paragraph and visual skeleton

One message/function per paragraph; connect what each paragraph establishes to the
next. Read [abstract](abstract.md) and [introduction](introduction.md). Select example
moves by function with `find_exemplars.py --function limitation --section introduction`.
Use [figures](figures.md) and `assets/figure-plan.template.json` to assign each visual a
question, data requirement, location and caption takeaway. A structural schematic
can be drawn from a specified mechanism; a result plot requires actual results.

Done: the mechanism answers the established gap, and planned evidence resolves the
paper's main questions. Repetition and unsupported implications are visible before prose.

## 4. Draft the requested sections

Offer a direct, gap-led, or insight-led abstract when alternatives help; default to
one coherent requested draft rather than producing variants by habit. Develop the
Introduction, Background/Motivation, [method](method.md) and
[experiments](experiments.md) from the same claim map. Write the cause, action,
measurable consequence, and cost instead of a parallel component list. Preserve
source terminology. Related work and rebuttals follow [revision guidance](revision-and-delivery.md).

Done: every section serves its distinct argument role, and empirical sentences use
actual results with matching scope.

## 5. LaTeX and figure integration

Use [LaTeX output](latex-output.md) for an existing official template or Markdown if
no template is requested. Preserve macros, labels, bibliography and venue requirements.
Use the TikZ/table fragments and CSV-to-vector plotting tools in `assets/figures/`.
Record unavailable results explicitly. Compile or render only when allowed by the
user's workflow; source checks do not require a TeX installation.

Done: the requested source files and visuals are present and internally referenced.

## 6. Mechanical and semantic checks

Run `check_manuscript.py main.tex`, `check_draft.py abstract.tex --section abstract`,
`style_metrics.py introduction.tex --section introduction`, and
`check_figures.py main.tex` as relevant. Corpus percentiles are development-set
observations, not grammar rules or acceptance thresholds. Review and justify useful
outliers instead of homogenizing style. Inspect headline values against source data,
metric boundaries, mechanism attribution and strongest competing baselines.

Done: structural errors are fixed; warnings are reviewed; missing research evidence
and macro-heavy source limits are explicitly retained. No checker certifies truth.

## 7. Deliver and revise

Return requested manuscript files plus a compact author report for substantial work
(`assets/report-template.md`), not workflow labels inside the paper. Explain changes
that affect meaning, evidence gaps, figure data still needed and actual checks run.
Honor the user's publication permissions and render/push preferences. Update the
claim map when a result or scope changes, then revise affected headline sections.

Done: authors can review the actual draft, evidence scope and outstanding decisions.
