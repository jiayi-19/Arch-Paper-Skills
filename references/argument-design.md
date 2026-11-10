# Designing the argument

Use the paper's contribution to choose its argument. These are writing routes, not
conference stereotypes or required section headings.

| Contribution | Argument that needs establishing | Evidence that resolves it |
|---|---|---|
| New microarchitectural mechanism | A workload behavior exposes a hardware bottleneck; the proposed state or scheduling change addresses its cause. | Strong baseline, mechanism controls, bottleneck counters, overhead and stress regimes. |
| Accelerator or HW/SW co-design | Dataflow, representation, compiler, or service choices jointly change work or movement. | Common task semantics, tuned competing design spaces, compute/memory/communication accounting, full claimed execution scope. |
| Characterization or security | A previously unresolved behavior matters under a defined population or threat model. | Direct observations, controlled interventions, coverage, repeatability, defenses or implications at the demonstrated scope. |
| Benchmark or infrastructure | Existing task interfaces or tools cannot answer a concrete design question fairly or practically. | Task construction, validity and coverage, reference methods, usage examples, limits and cost. |
| Analytical/modeling method | A model captures the relevant mechanism with known assumptions more usefully than alternatives. | Derivation, independent validation, errors and ranking behavior, regimes of validity. |
| Architecture-design agent | A specified action space and feedback policy improve design outcomes under a fixed budget. | Executable acceptance, search-budget controls, failure-aware results, structural versus tuning attribution, held-out agent evaluation if learning is claimed. |

## Storyline before sentences

Express the research in a causal chain:

- **Setting:** workload, machine or service regime, and optimization objective.
- **Obstacle:** the expensive event or broken assumption, with its technical cause.
- **Alternative:** a credible existing approach and why it leaves this obstacle.
- **Insight:** a property of the workload or machine that changes the design choice.
- **Mechanism:** the state, data path, scheduling rule, representation, or interface
  that exploits the property.
- **Evidence:** experiments answering whether it works, why, at what cost, and when.
- **Scope:** the population and measurement level to which the conclusion applies.

If code confirms a mechanism but no measurements establish a benefit, write the
mechanism now and leave the empirical conclusion pending. If the main contribution
is measurement, the surprising observation may precede the mechanism or replace it.

## Introduction and motivation

The Introduction establishes the research question, technical obstacle, proposed
answer, and strongest supported findings. Background/Motivation gives readers the
concepts and causal reasoning needed to understand the method. Separate them when
that reasoning is substantial, rather than repeating the same pitch in both.

A useful paragraph chain for an architecture paper is: design goal; observable
bottleneck; failure of a reasonable alternative; exploitable observation; proposed
machine or method; scope and result; contributions. Combine or reorder paragraphs
when the argument calls for it. No fixed paragraph count is a quality criterion.

For each motivation paragraph, identify what it earns later:

| Motivation | Method requirement | Evaluation obligation |
|---|---|---|
| Fixed representation misses a behavior | Expose the relevant state/action/design freedom. | Show a case unreachable through existing knobs and compare to strong tuning. |
| Structure and configuration interact | Turn a structure into an instantiable parameterized family. | Initial-family best, new-family default/tuned points, and structural revision controls. |
| Feedback is costly or conditional | Choose fidelity and preserve uncertainty in decisions. | Quality under budget, expensive tool use, false pruning, abstention, calibration scope. |
| History access may explain apparent learning | Separate retrieval from persistent policy changes. | Equal-experience controls and held-out design tasks. |

An illustrative scenario can explain a design requirement without pretending to be
a measured result. Label it as an example. Use a measured motivation experiment only
when its protocol and input actually support the statement being made.

## Novelty and positioning

Explain what changes relative to the closest machine or method at a concrete seam:
execution ordering, data movement, state representation, allocation, communication,
verification boundary, or optimization objective. State inherited machinery and
what the contribution changes about it.

Distinguish these questions:

1. Is this instance outside the starting search space?
2. Does it differ meaningfully from closest published designs?
3. Can the current evaluator express the relevant behavior?
4. Does that behavior improve the target objective?

An affirmative answer to one does not establish the others. A paper can contribute
an important measurement or reproduction even when it proposes no new architecture.

## Contributions and evidence

Contribution items name delivered research objects or established findings. A list
of agent roles, compiler passes, or modules becomes a contribution only when the
paper establishes what research capability or mechanism they provide.

For each main statement, record enough to recover the result:

| Claim | Basis | Source/locator | Conditions | Appropriate wording |
|---|---|---|---|---|
| A mechanism reduces traffic | Measurement or validated model | Actual traffic counters and protocol | Same workload, precision, resources, traffic scope | Quantified reduction at that scope. |
| A new structure is beneficial | Controlled comparison | Mechanism toggle and tuned baselines | Matched constraints and search opportunity | Benefit attributable to the controlled change. |
| A policy transfers | Independent test | Frozen agent versions and test episodes | Unused tasks; same experience and online budget | Improvement for the observed transfer population. |

A hypothesis is an explicit design rationale, not an observed outcome. A proof
supports only its assumptions; an ablation supports only the intervention actually
performed. Related work establishes positioning, not an empirical performance result.
