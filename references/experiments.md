# Experimental methodology and results

Start from the evidence map. Fix actual workloads, inputs, numerical contract,
baselines/tuning opportunity, resource and service constraints, measurement stage,
versions, repetitions, uncertainty, budgets and failure treatment. Only then report
the question each comparison answers.

A results paragraph states the supported finding, cites the visual/table, quantifies
the important difference/population, explains the mechanism with observed evidence,
and states conditions where the result changes. A plausible untested cause remains
an interpretation. Preserve invalid and unavailable results rather than averaging
only successful outputs without disclosure.

Include an appropriate subset of: main quality/coverage, mechanism toggles, tuned
old/new spaces, overhead, sensitivity, model validation, scaling, adverse regimes and
end-to-end scope. No universal experiment count follows from this corpus. For tools,
validate the measurements or ranking decisions the tool is intended to support.
For security, state attacker capability and the defended property before performance.

Tables need metric direction, units, baseline, population and eligibility. Plots use
actual data and explicit missing-status records. See [figures](figures.md) and the
measurement/aggregation rules in [architecture evaluation](architecture-evaluation.md).
