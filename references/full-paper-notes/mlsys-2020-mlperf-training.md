# mlsys-2020-mlperf-training: MLPerf Training Benchmark

Numbering note: sections 0 to 3 follow the base template. Sections 4 to 10 are the benchmark variant. Sections 11 to 13 are the base template sections 8, 9, 10 (sentence habits, figures and tables, why it reads as strong).

## 0. Identity
- Title: MLPerf Training Benchmark.
- Venue and year: MLSys 2020 (the page footer reads "Proceedings of the 3rd MLSys Conference, Austin, TX, USA, 2020").
- Contribution type: benchmark (suite, metric, rules, reference implementations, two rounds of results).
- Pages: 14 in the arXiv v3 PDF (about 10 pages of body, the rest acknowledgements and references). About 9k words in the dump.
- Full text used: https://arxiv.org/pdf/1910.01500 (v3, 2 Mar 2020).

## 1. Skeleton
Arabic numbered sections, MLSys two-column layout, with section numbers down to the third level (2.1.1).

| Section | Role | Words | F / T |
|---|---|---|---|
| Abstract | summary | 111 | 0 / 0 |
| 1 Introduction | history argument, five goals, six actions, roadmap | 950 | 0 / 0 |
| 2 Background (2.1 Unique Challenges: 2.1.1 optimizations vs quality, 2.1.2 scale, 2.1.3 run-to-run variation, 2.1.4 diverse software; 2.2 Prior Work) | motivation and related work | about 1,450 | 1 / 0 (Fig 1) |
| 3 MLPerf Training Benchmark (3.1 suite with 3.1.1 to 3.1.5 per task, 3.2 time-to-train metric with timing rules and run counts, 3.3 quality thresholds, 3.4 references and hyperparameters) | the benchmark definition | about 2,500 | 1 / 2 (Fig 2, Table 1, Table 2) |
| 4 Benchmarking Process (4.1 submission and review, 4.2 reporting: divisions, categories, scale, scores) | rules and process | about 1,170 | 1 / 0 (Fig 3 sits here) |
| 5 Results | evaluation | 234 | 1 / 0 (Fig 4) |
| 6 Conclusions | lessons and future | about 450 | 0 / 0 |

Total: 4 figures, 2 tables. No design-overview section, no separate evaluation section beyond a short Results section. The paper says early that it focuses on "design and rationale", and the evaluation is thin by design.

## 2. Abstract
- 4 sentences, about 111 words.
- Functions: (1) setting and need (ML needs industry-standard benchmarks); (2) problem: "three unique benchmarking challenges absent from other domains", listed in the same sentence; (3) approach: "We therefore present MLPerf, an ML benchmark that overcomes these challenges"; (4) scope of evidence: quantitative analysis of efficacy across two rounds from multiple vendors.
- Numbers: none except "three" challenges and "two rounds". The abstract does not carry results numbers.
- Named in sentence 3. The three challenges are written as three clauses in one sentence, so the structure of the paper (Section 2.1) is visible before the Introduction.
- Quote (Abstract): "fair benchmarking with the same binary, code, and even hyperparameters is difficult".

## 3. Introduction
- About 952 words, 34 sentences (the highest average sentence length of the four papers, about 28 words). Roughly 6 running paragraphs, then two bullet lists and a closing roadmap paragraph. Many semicolons in the dump are inside citation groups.
- P1: ML has revolutionized many domains; compute investment. Opens with a list of application areas with citations; ends with investment in hardware and software, which makes the next paragraph's "need" natural.
- P2: historical argument. Opens by saying more systems means a need for a comprehensive benchmark. Evidence: "History shows that benchmarks accelerate progress" (SPEC, TPC). Ends by saying the success of these inspired the formation of MLPerf. This is the credibility device: the consortium is positioned as the heir of SPEC and TPC.
- P3: why ML is different: optimizations change mathematical semantics and learning dynamics, so a fast system can be slow to reach a quality. Opens with "Unlike other computational workloads"; ends by contrasting with microbenchmarks. First statement of the technical problem.
- P4: DL is approximate and stochastic, so "equally valid solution classes" must be defined. Ends by saying the degrees of freedom need careful definition. Together with P3 it states the central problem: define what is fixed and what is free.
- P5 (prior work): microbenchmarks (DeepBench), throughput suites (Fathom, TBD), DAWNBench. Each is credited with what it does and dismissed with what it lacks: microbenchmarks "fail to reflect the complexity of real workloads", throughput suites limit innovation, DAWNBench was flexible, "however, also made it difficult to draw fair comparisons". Ends with a one-line synthesis: MLPerf combines a broad set of benchmarks (Fathom, TBD), an end-to-end metric (DAWNBench) and a broad consortium (SPEC).
- P6: five high-level goals (bullet list): fair comparison while encouraging innovation; accelerate progress; enforce reproducibility; serve commercial and research communities; keep effort affordable.
- Then "This paper focuses on the design and rationale", and a second bullet list of six things MLPerf Training does: comprehensive suite; reference implementations; equivalence rules; timing rules; open source submissions; working groups. These read as the contribution list.
- Roadmap paragraph: section by section ("In § 2 we discuss...").
- Key insight position: P3 and P4 (the quality and stochasticity problem), formalized in 2.1. The solution insight (time to a quality target plus fixed reference) first appears in the six-item list.
- Challenges device: handled in Section 2.1, not the Introduction. Abstract and Intro P3 to P4 foreshadow it.
- Contributions: two lists, 5 goals plus 6 actions, none with a number; items are capabilities and rules ("Establish ...", "Create ...", "Make ..."). The conclusion later restates three "contributions" (precise definition, reference implementations and rules, and lessons).
- Result preview: there is none in the Introduction; results appear only in Section 5. This is unusual for an architecture paper.

## 4. What the benchmark is
- Definition (Intro, after P5): "MLPerf aims to create a representative benchmark suite for ML that fairly evaluates system performance", followed by five goals. Section 3 opens by listing its four components: workloads, timing rules, quality threshold choices, reference implementations and hyperparameters. The conclusion restates it as "a suite of ML benchmarks that represent both industrial and academic use cases".
- Most important property: fairness of comparison, with innovation preserved (goal 1: fair comparison while still encouraging ML innovation). Reproducibility is goal 3.
- Words carrying it: "fair" (fair comparison, fairly, fair to submitters with smaller compute resources), "equivalent", "reproducibility", "representative", "affordable". Fairness is also tied to resource asymmetry (the hyperparameter limit protects submitters who cannot search extensively).
- Numbered list: yes, five goals as bullets. Short form: fair comparison with innovation; accelerate progress; reproducibility; serve commercial and research; affordable.
- Quote (Introduction): "Enable fair comparison of competing systems while still encouraging ML innovation."

## 5. Why a benchmark is needed
- Argument: three stages. (a) Historical: benchmarks accelerate progress (SPEC, TPC). (b) Technical: ML training has four problems that other compute benchmarks do not have (Section 2.1): optimizations that raise throughput can hurt quality; scaling changes the learning dynamics (for example ResNet-50 needs about 64 epochs at batch 4K and over 80 at 16K, about 30% more compute); run-to-run variance in epochs to quality (Fig 1, five seeds); software diversity (the same operator implemented differently, for example SGD with momentum in Caffe versus PyTorch and TensorFlow). (c) Prior work: microbenchmarks, throughput suites, DAWNBench.
- Evidence: measured on MLPerf v0.5 reference implementations (Fig 1), a worked numerical example (batch size and epochs), two equations for the momentum variants, and an observation about cuDNN offering about ten forward convolution algorithms.
- Tie to requirements: explicit back-references. Section 3.2 says the time-to-train metric addresses "§ 2.1.1 and § 2.1.2". Section 3.2.2 says the multiple runs address "§ 2.1.3". Section 3.4 says references and equivalence rules address software diversity. Section 3.3's choice of high thresholds cites 2.1.1 and 2.1.2 again. The mapping from challenge to mechanism is one to one and signaled with section numbers.
- The paper also argues against the competing ideas on benchmark type: microbenchmarks isolate and are fair but unrepresentative; throughput suites limit innovation.

## 6. Task and rule definition
- Task: a benchmark is a data set, a model (named reference), and a quality threshold (Table 1: seven tasks such as ResNet-50 v1.5 on ImageNet at 74.9% Top-1, SSD at 21.2 mAP, Mask R-CNN, GNMT, Transformer, NCF at 0.635 HR@10, MiniGo at 40.0% move prediction). Metric: wall-clock time to train to the quality target.
- Timing rules: timing starts when the system first touches training or validation data and stops when the quality target is reached on validation data. Excluded: system initialization; model creation and initialization (up to 20 minutes); data reformatting (once-only), with the added rule that any per-training data processing may not be moved into reformatting.
- Run count: vision tasks require 5 runs (90% of entries within 5%); others 10 runs (within 10%); fastest and slowest dropped, arithmetic mean reported.
- Held fixed: model and training procedure (mathematically equivalent to the reference), data set, quality metric, parameter initialization, optimizer schedule, data traversal (closed division). Free: framework, numerics, system size, a small whitelist of hyperparameters (Table 2: batch size, learning rate schedule parameters, and a few model-specific ones). Hyperparameter borrowing is allowed: after submission, a submitter may adopt another submitter's hyperparameters for the same benchmark and resubmit with no other changes. The paper reports that borrowing worked across numerics, architectures and software, which it uses as evidence that hyperparameters are portable.
- Divisions: closed (equivalence to reference; restricted hyperparameters) and open (different models, optimizers, augmentations allowed). Categories: available, preview, research. System type: on-premises or cloud. Scale reporting: number of chips or a cloud-scale metric derived from host processors, memory and accelerators (verified to correlate with cost across three cloud providers); optional in v0.5 and v0.6.
- Fairness enforcement: reference implementations (explicitly not for performance comparison, only to define the model and training procedure and to set thresholds); equivalence rules; peer review before publication, with notification of noncompliance and the right to resubmit; public submission code and logs. No audit tests in this paper (those are in the Inference paper). Evaluator isolation: not described; the logs are the evidence.
- Reasoned choices: high quality thresholds chosen on purpose (to stop quality-reducing optimizations and to reduce variance, which is much higher early in training; Fig 2 shows noise in the first 30 epochs). No single summary score, for two reasons stated in 4.2.4 (weighting is not universally representative; a submitter may decline to report all benchmarks).

## 7. Construction and coverage
- Tasks: seven, chosen "primarily based on commercial and research relevance", with feedback from tens of organizations, covering vision, language, recommendation and reinforcement learning; compact to keep the suite affordable. Each task has its own short subsection (3.1.1 to 3.1.5): what the task is, which data set and metric, which model and why (for example ResNet-50 v1.5 because several variants made earlier claims incomparable; GNMT included as the only RNN; MiniGo chosen to keep the suite ML-oriented rather than simulator-oriented; NCF's data set was too small so v0.7 will use a synthetic data set).
- Coverage view: Table 1 (benchmark, data set, model, quality threshold). There is no table by category of compute motif; the text says the models represent "diverse compute motifs".
- Baselines and references: PyTorch or TensorFlow reference per benchmark with scripts for data download and preprocessing; thresholds set by experiments on the references; run counts set by studying the reference implementations' variance.
- Own limits: a lessons list in the conclusion (data set size must be realistic for memory behavior; startup time should be excluded for small data sets; hyperparameters are portable at similar scale; optimizer variations affect convergence); future work (power measurement for on-premises systems, synthetic data for NCF, adding benchmarks) is stated.

## 8. Use and results
- Results are about the benchmark's effect on the field over two rounds (v0.5, v0.6, six months apart, same hardware). The best 16-chip results improved by an average of 1.3x even though quality targets were raised (Fig 3a and Fig 3b); the number of chips for the best overall result grew by an average of 5.5x (Fig 4). The text says part of the gain came from rule changes (for example allowing LARS) and part from implementations, and that the authors "believe" much went into software infrastructure.
- How results demonstrate that the benchmark discriminates: they do not compare vendors. The evidence is progress, not ranking.
- Presentation: two small bar charts and a quality-target table; no vendor names. The Results section is 234 words, much shorter than the design sections. The paper makes it clear (Abstract and Section 1) that it is a design-and-rationale paper.

## 9. Phrases worth reusing as patterns
1. "[Problem class] presents [N] unique challenges absent from other domains: [challenge 1], [challenge 2], and [challenge 3]."
2. "[Mechanism] overcomes the challenges in § x and § y by preventing [bad behavior] while still allowing [flexibility]."
3. "We chose [higher thresholds] for two reasons: First, we must prevent [bad effect]. Second, we must minimize [variance source]."
4. "[Artifact] are not optimized for performance (meaning they should not be used for [comparison]), as their main purpose is to define [the task precisely]."
5. "To keep the suite affordable, we selected a compact but representative set of [N] benchmarks."
6. "[Summary score] is unsuited to [benchmark] for two main reasons. First, it implies [weighting]. Second, it becomes less meaningful if [participants omit parts]."
7. "[Rule] to balance the need to [tune per system] with limiting [search space] to be fair to submitters with [fewer resources]."
8. "We determined the number of runs by studying the behavior of the reference implementations."

## 10. What transfers to an agent benchmark
1. Pair every challenge with a named mechanism and cite the challenge section in the mechanism section ("addresses the challenges in § 2.1.1 and § 2.1.2"). In an agent benchmark: stochastic agents, budget differences, and test-set leakage each get a numbered challenge and a numbered rule.
2. Use a reference implementation that defines the task and thresholds but is stated not to be a performance baseline, and let the metric be time or cost to a fixed quality target; this keeps speed claims from hiding quality loss.
3. Justify a fairness rule by resource asymmetry (restrict the tuning space to be fair to smaller teams) and allow a post-submission borrowing step so that tuning luck is separated from design quality.
- Does not transfer: the closed list of seven ML models and the ML-specific hyperparameter table (Table 2).

## 11. Sentence and paragraph habits (template 8)
- Average sentence length: about 26 words (abstract 28, intro 28, background 22, results 21, conclusion 29). Long, comma-rich sentences with a final purposive clause. Paragraphs about 100 to 180 words.
- Person and tense: mostly impersonal present ("MLPerf provides", "Timing begins when"); "we" is used for decisions ("We chose", "We determined", "We exclude"), about 5 to 8 per 1,000 words, much lower than the Inference paper.
- No bold run-in headings; subsection headings carry structure (numbered to the third level). Bullet lists are used for goals, actions and conclusion points. Parentheticals are common (about 70), semicolons are few outside citations, em dashes about 5, no italics emphasis noted.
- Hedging: modest ("somewhat portable", "we believe"). Some typos remain in the arXiv text ("to to", "hyperparamter").
- Numbers: with scope in the same sentence ("5 runs to ensure 90% of entries from the same system are within 5%").

## 12. Figures and tables (template 9)
- First figure (Fig 1, Section 2.1.3): number of epochs to reach the target for five random seeds on NCF and MiniGo. It comes first because it is measured evidence for run-to-run variation, the challenge that most distinguishes ML training. Caption is descriptive and adds an observation about MiniGo (variability even with fixed seed).
- Fig 2 (accuracy curves of ResNet-50 over 100 epochs, five seeds, dashed target line) supports the choice of high thresholds. Fig 3 and Fig 4 carry the results (speedup, quality-target change, chips).
- Tables: Table 1 lists benchmarks with data set, model, threshold; Table 2 lists modifiable hyperparameters per model. Both are lookup tables for the rules, not result tables. Captions are short noun phrases.

## 13. Why it reads as strong, and what does not transfer (template 10)
- Move 1: open with history (SPEC and TPC) to claim a role, then show why ML needs something different. Place: Introduction P2 to P4.
- Move 2: four numbered challenges with measured figures, then one rule per challenge with explicit back-references. Place: 2.1.1 to 2.1.4 and 3.2 to 3.4.
- Move 3: the rationale is given for each fairness knob (thresholds, run counts, borrowing, scale reporting, no summary score), usually "for two reasons" with first and second. Place: 3.3, 4.2.4.
- Particular to topic, do not copy: ML-specific details about stochastic training dynamics and per-task model descriptions.
