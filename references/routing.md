# Contribution and motivation routing

Choose the research object before a paragraph template. Routes are adaptable guidance,
not empirically proven conference-wide categories. The development corpus has stronger
coverage of mechanisms, tools and characterization than benchmarks or formal proofs.

| Contribution | Argument route | Useful examples |
|---|---|---|
| Microarchitectural mechanism | observed bottleneck -> prior residual cost -> exploitable property -> state/action -> controlled consequence | Constable, DIP, UCP, DVR |
| Accelerator | workload computation/movement -> limiting resource -> dataflow/organization -> constraints -> accounting and implementation | Eyeriss, DianNao |
| Hardware/software co-design | abstraction/interface mismatch -> joint representation/change -> legal construction -> search/runtime choice -> costs | TensorIR, Centauri, GhostRider |
| Characterization/security | invariant or unexplained behavior -> observation apparatus -> controlled population -> findings -> tested implication | RowHammer, PIM Pathfinding |
| Modeling/tool | decision unavailable or expensive -> abstraction -> assumptions -> independent validation -> enabled design study | Wattch, McPAT, CACTI6, SimPoint |
| Benchmark/resource | missing comparable task capability -> construction principle -> task freedom/acceptance -> coverage -> demonstrated use | Derived guidance; no dedicated benchmark exemplar in this development set |
| Formal/analytical | precise question -> assumptions -> statement/bound -> attainability or proof -> implication and validation | Mind the Gap for bounds; theorem-only route is derived guidance |
| Re-examination | credited belief/proxy -> competing explanations -> discriminating test -> changed conclusion | UCP proxy distinction; full-paper re-examination guidance is derived |

Motivation can be cost, tradeoff, representation/capability gap, unexplained observation,
or a prior assumption failing in a new regime. State the technical reason for the
problem. A trend alone does not explain why a specific mechanism is needed.

Select examples by paragraph function (`--function`), section, contribution type,
venue or topic. A memory paper can provide a useful model-validation move for a
processor paper. Carry over the information order and evidentiary logic, not its claims.
