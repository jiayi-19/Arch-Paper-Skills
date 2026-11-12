# How benchmark papers are written

Sources: MLPerf Inference (ISCA 2020), MLPerf Training (MLSys 2020), ArchGym (ISCA 2023), RobotPerf
(arXiv 2023), plus the benchmark or tool parts of Mess (MICRO 2024 runner-up), Lifetime-Aware Design
(FlexiBench, ASPLOS 2026) and PIM Pathfinding (HPCA 2024). The four benchmark papers were chosen as models for benchmark
writing and none is claimed as an award paper. Full notes are in `full-paper-notes/`.

## 1. Define the benchmark by what it guarantees

Each paper states in one sentence what the benchmark makes possible, and carries that property through
the paper with a few repeated adjectives.

| Paper | The guarantee, in short | Words that carry it |
|---|---|---|
| MLPerf Inference | comparability across systems with very different architectures | architecture-neutral, representative, reproducible |
| MLPerf Training | fair comparison while still encouraging innovation | fair, equivalent, reproducible, affordable |
| ArchGym | objective, fair and reproducible comparison of search agents through one standard interface | fair, reproducible, objective, apples-to-apples |
| RobotPerf | standardized comparison across heterogeneous hardware | vendor-agnostic, architecture-neutral, reproducible |

Short quotations that state it: "By establishing a clear boundary between submitter-owned and MLPerf-owned
components, the benchmark maintains comparability among submissions." (MLPerf Inference, Section IV).
"Enable fair comparison of competing systems while still encouraging ML innovation." (MLPerf Training,
goal 1). "Such standardization of interfaces provides baselines to objectively compare all the agents in a
fair and reproducible manner." (ArchGym, Section 4).

The properties are the point. The data format, the language of the tasks and the count of tasks come after.
RobotPerf is the weakest of the four here: its abstract has no problem sentence and no number, its
principles are only subsection headings, and some run rules are hopes.

## 2. Number the requirements and reuse them

- MLPerf Inference gives five numbered design choices in the Introduction (representative workloads,
  realistic scenarios, target quality and tail latency, permissive rules with closed and open divisions, a
  method that allows models to change) and reuses four of them as the objectives that structure its
  assessment section.
- MLPerf Training gives five goals as bullets and cites the challenge section number in each mechanism
  ("addresses the challenges in section 2.1.1 and 2.1.2").
- ArchGym states three challenges in the abstract and the Introduction ("First", "Second", "Lastly"),
  and its evaluation opens with "The insights from ArchGym are three-fold" in the same order.

## 3. Show why a benchmark is needed

Four kinds of argument appear:
1. The space is combinatorial, so any single number on one configuration misleads (MLPerf Inference, with a
   figure of the accuracy against cost frontier and a porting example where one operator differs between two
   frameworks and costs 0.8 mAP).
2. The domain has specific problems that other benchmarks never had, each measured (MLPerf Training: four
   problems, with a figure of run-to-run variance across five seeds and a worked batch-size example).
3. The first experiment of the benchmark is the proof of need (ArchGym: a sweep of 21,600 experiments shows
   up to 90 percent interquartile spread from hyperparameters, so conclusions about an algorithm are not
   trustworthy unless every baseline is tuned equally).
4. Existing tools are measured first and found wanting (Mess: every existing simulator deviates from real
   hardware on common axes) or compared on named characteristics in a table with the new one in the last
   row and an honest cross where it falls short (RobotPerf Table I).

## 4. Define the task and the rules

- **Unit of a task.** A task fixes the data or workload, a reference model or design, a quality target or
  acceptance test, the metric, and the budget (MLPerf: data set, reference model, quality threshold, scenario
  and metric, minimum number of queries). ArchGym: an environment (cost model plus workload) and an agent
  (policy plus hyperparameters) joined by one interface of actions, observations and a reward.
- **An ownership boundary.** Evaluator-owned parts (data, evaluator, task definition) and participant-owned
  parts (implementation) are named, and the paper says the boundary is what makes results comparable
  (MLPerf Inference). RobotPerf calls its version "opaque tests": the workload code is not modified and the
  input and output nodes sit outside it.
- **What is fixed, free and prohibited.** MLPerf Inference lists each, prefers an explicit blacklist
  (retraining, pruning, caching, benchmark-aware optimization, exploiting the fixed seed) and says why:
  to encourage a wide range of techniques. MLPerf Training whitelists a small table of hyperparameters.
- **Divisions.** Closed (equivalent to the reference, comparable) and open (anything, not directly
  comparable, deviations documented). Categories such as available, preview and research.
- **Fairness argued by resource asymmetry.** MLPerf Training limits the tuning space "to be fair to submitters
  with fewer resources" and allows hyperparameter borrowing after submission, which separates tuning luck
  from design quality.
- **The comparison axis is justified.** ArchGym compares by simulator samples and not by wall-clock time,
  because time depends on implementation and parallelism.
- **Variance rules.** Number of runs set by studying the variance of the reference (MLPerf Training: 5 runs
  for vision, 10 for others, drop fastest and slowest). Number of queries computed from the tail percentile
  and confidence (MLPerf Inference).
- **A reference implementation that defines the task but is not a performance baseline.** MLPerf Training
  says so explicitly.

## 5. Show that the rules are enforced

- The evaluator sits outside participant code (the load generator and the accuracy script in MLPerf
  Inference).
- Audit tests are named (accuracy check in performance mode, caching detection, alternate seed, custom data
  sets), results go to a public repository for peer review, and a submission checker runs.
- First-round statistics are reported: about 40 issues in about 180 closed-division results, 166 released
  (MLPerf Inference).
- PIM Pathfinding validates its tool against the real machine with correlation and error numbers and repeats
  the weak spots as stated limitations.

## 6. Construction and coverage

- Selection criteria for tasks are stated: mature models with community support, open source, working across
  frameworks, coverage of different compute motifs, input from the community (MLPerf).
- A coverage table lists area, task, reference model, data set and quality target.
- A candid paragraph when the reference could not meet its own target (MLPerf Inference retrained MobileNet
  weights to be quantization friendly because the 1 percent target was unreachable otherwise).
- Limits are stated in their own section or paragraph: missing tasks, data set gaps, modeled versus measured
  performance, what is prohibited though real systems do it.

## 7. What the results section proves

The results section of a benchmark paper argues for the benchmark, not for a winner.
- MLPerf Inference: more than 600 results from 14 organizations, no leaderboard, no vendor names,
  results normalized to the slowest system, a figure that shows spreads of about 100x in single stream and
  about 10,000x over the whole range, so the benchmark discriminates.
- MLPerf Training: the evidence is progress across two rounds (1.3x faster, 5.5x more chips). The Results
  section is 234 words and the abstract has no numbers.
- ArchGym: a negative finding (no search algorithm wins once every one is tuned) is the headline, and the
  evaluation closes subsections with a bold "A call to action."
- RobotPerf: three claims, each a subsection title (compare across platforms, guide hardware selection,
  reveal the benefit of acceleration), and the sentence "no one-size-fits-all" with one example.

## 8. Patterns to reuse

- "To quantify these tradeoffs, the field needs a benchmark that is [adjective], [adjective], and
  [adjective]."
- "We specify the [task] and the rules, but we leave [implementation] to participants."
- "We prohibit [X] to ensure comparability. Although this may not reflect [realistic case], [A] and [B] matter
  most for comparability."
- "We chose [a blacklist] to encourage [diversity] and to support [neutrality]."
- "[Artifact] is not optimized for performance, so it should not be used for [comparison]. Its purpose is to
  define [the task] precisely."
- "[Summary score] is unsuited to this benchmark for two reasons. First, it implies [weighting]. Second, ..."
- "We assess the [set] against our [objectives]:" then one bullet per objective, each with a section pointer.
- "The takeaway is that future [field] requires us to report [distributions] and not [a single state-of-the-art
  claim]." (ArchGym, run-in "A call to action.")

## 9. Mistakes to avoid

- RobotPerf: an abstract that names the benchmark and says nothing about the problem or any number, run rules
  that are aspirations, no stated task selection criteria, no reference results.
- Describing the suite by its size (number of designs and tasks) and leaving out what is held fixed.
- A results section that ranks participants, which turns the benchmark paper into a leaderboard paper.
