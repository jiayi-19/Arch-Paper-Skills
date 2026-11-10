# Architecture evaluation: what a result means

Read when planning experiments or writing quantitative claims. Select checks for the
actual contribution; a measured software prototype need not pretend to be an ASIC.

## Declare the comparison

Before a performance paragraph, know the workload and inputs, correctness contract,
precision, baseline, tunable design freedom, resource constraint, clock, measurement
boundary, methodology, and budget. In text, state what materially changes the result;
keep the full reproducible setup in a table or protocol reference.

Tuned baselines receive the declared opportunity to tune. Compare same-capacity,
same-area, same-power, or a Pareto frontier as appropriate, naming which constraint
is held fixed. An iso-area study and an unconstrained best-performance study answer
different questions and can both be useful when labeled.

## Measurement levels

| Evidence | Supported wording | Further evidence needed for a stronger claim |
|---|---|---|
| Roofline or analytical model | Modeled bound or estimate with assumptions. | Validation against relevant implementations and interaction regimes. |
| Architectural simulation | Simulated metric for supported semantics/configuration. | Structural coverage and implementation validation for PPA/realism claims. |
| RTL simulation | Functional/cycle observations for specified interfaces, inputs, and counters. | Mechanism conformance, scope, implementation and physical qualification. |
| Synthesis and STA | Area/timing under named library, constraints and memory assumptions. | Place-and-route or silicon for claims requiring those effects. |
| Place-and-route | Physical implementation metrics at the reported corners and stage. | Silicon characterization for measured-chip claims. |
| Hardware observation | Measurements on the actual tested hardware and input population. | Population/operating-condition coverage for broader generalization. |
| Projection | Derived estimate with a named model and reference points. | Direct measurement of the projected target to call it observed. |

Functional validity, faithful realization of a proposed mechanism, timing eligibility,
and metric scope are separate checks. Native kernels or individual operators do not
by themselves establish whole-model or full-system performance. A synthesized design
may use black-box memories; explain what their area and energy accounting includes.

## Quantities and aggregation

For a lower-is-better quantity, speedup or improvement ratio is baseline/candidate.
A reduction is (baseline-candidate)/baseline. State the chosen convention; "2x lower"
is ambiguous. At a fixed clock, latency = cycles/frequency only when the cycle scope
includes the claimed service. A higher Fmax does not automatically give the same
workload throughput because of stalls, transfer bandwidth, and service constraints.

Energy is time-integrated power; EDP = energy x delay and ADP = area x delay.
State units and scope. Peak TOPS, effective throughput, useful operations, sparse
operations, and end-to-end latency are different quantities. Disclose actual memory
bandwidth, traffic, batch, sparsity conditions, numerical error, and host work where
these govern the result.

Use the geometric mean for positive multiplicative ratios when justified, with
per-task ratios, population and failure policy. A geomean of per-task ratios is not
the ratio of arithmetic means. Keep zero, missing, invalid, and timing-ineligible
results explicit. Report success/coverage alongside quality; do not remove failures
silently or insert a fabricated fallback score. An "up to" value names its case and
is accompanied by distribution or aggregate information when claiming broad benefit.

## Mechanism and design-space attribution

Show the proposed causal path with appropriate counters or interventions:

workload condition -> bottleneck event -> mechanism action -> changed work or traffic
-> performance/resource effect.

Examples of informative controls include disabling the new policy while retaining
its structures; comparing equal resource budgets; tuning both old and new families;
measuring useful rather than issued work; and perturbing the workload feature the
mechanism exploits. Explain overheads: metadata, buffers, ports, queues, control,
arbitration, refill, compiler cost, and any slower critical path.

For two coupled knobs, a crossed study helps distinguish an interaction from a joint
change. Comparing only two diagonally opposite configurations does not isolate each
knob's contribution. An ablation that destroys baseline functionality answers an
acceptance question rather than measuring the independent value of a role.

## Coverage, approximation, and tools

Explain which architectural behavior a model consumes and which interactions remain
outside it. Measured neighbors support a conditional interval only with an argument
placing the target between them; endpoint ordering alone does not prove containment.
Report violations, uninformative intervals and abstention. Search-time estimates
remain distinct from independently obtained final target measurements.

Validate models with independent points spanning the relevant regimes. Where ranking
is the purpose, examine ranking errors as well as point error. A later final test
cannot establish that early pruning never discarded good designs. Do not compose
unrelated per-component bounds without a supported whole-design argument.

## Workload and measurement studies

Document selection, input distributions, repetitions, warm-up, sampling, simulator
versions, compiler options and operating conditions as relevant. Explain errors and
confidence intervals in terms of actual variation. Counter-based observations and
empirical characterization are valid contributions when their population and causal
limits are clear. Security work additionally states the threat model, capabilities,
physical/software access, success definition, defenses, and observed failure regime.

## Agents, automated design, and persistent updates

Separate the algorithm, permitted hardware edits, evaluation access, and runtime
budget. Count repairs, failed candidates, model/tool calls, elapsed time and online
cost consistently. Baseline qualification or independent final grading outside the
online budget must be explicit for every compared method.

Distinguish hardware warm-start, retrieved experience, and persistent strategy
inheritance. For improvement claims, freeze development/test task partitions, model,
scorer, experience and policy versions. Compare a static agent, equal-experience
retrieval, and the updated policy when the claim needs all three. A narrower pilot
with two arms supports its actual comparison, not an unrun three-arm claim.

A successful policy patch establishes an update occurred. Held-out outcomes establish
whether it helped. One within-family update does not establish cross-family transfer,
multiple recursive generations, or accelerating self-improvement. Keep outer-loop
training/development costs separate from online design costs.

## Writing a results paragraph

Lead with the supported finding, cite the figure/table, state the important magnitude
and population, explain the mechanism using measured evidence, and state the regime
where the outcome changes. A plausible explanation without a control is identified as
an interpretation rather than a demonstrated cause. Include losses when they define
the tradeoff or qualify the main conclusion.
