# isca-2023-archgym: ArchGym: An Open-Source Gymnasium for Machine Learning Assisted Architecture Design

Numbering note: sections 0 to 3 follow the base template. Sections 4 to 10 are the benchmark variant. Sections 11 to 13 are the base template sections 8, 9, 10 (sentence habits, figures and tables, why it reads as strong).

## 0. Identity
- Title (confirmed from the PDF): ArchGym: An Open-Source Gymnasium for Machine Learning Assisted Architecture Design.
- Venue and year: ISCA 2023 (50th ISCA, Orlando; DOI 10.1145/3579371.3589049).
- Contribution type: framework and benchmark tool (a gym that connects search agents to architecture cost models), plus a comparative study and a dataset case study. It is closer to an evaluation environment than to a fixed task suite.
- Pages: 14 (ACM two-column; the reference list is about 3 pages). About 13k words in the dump including references.
- Full text used: https://arxiv.org/pdf/2306.08888 (v1, 15 Jun 2023).

## 1. Skeleton
Arabic numbered sections.

| Section | Role | Words | F / T |
|---|---|---|---|
| Abstract | summary | about 320 | 0 / 0 |
| 1 Introduction | problem in three challenges, system, headline findings, 5 contributions | about 1,330 (with caption and table) | 1 / 1 (Fig 1, Table 1) |
| 2 Background and Related Work | background and prior ML-for-architecture work (no separate related-work section) | about 490 | 1 / 0 (Fig 2) |
| 3 Design and Implementation (3.1 Environment, 3.2 Agent, 3.3 Interface, 3.4 Dataset Generation) | design | about 1,330 | 0 / 2 (Table 2, Table 3) |
| 4 Integration of New Algorithms | design rationale: three questions every agent answers | about 940 | 1 / 0 (Fig 3) |
| 5 Experimental Setup | methodology | about 240 | 0 / 0 |
| 6 Evaluation (opening, 6.1 Hyperparameter Lottery, 6.2 Trade-off Between ML Methods, 6.3 Analysis of Designed Hardware) | evaluation | about 350 + 1,010 + 950 + 120 | 5 / 1 (Figs 4 to 8, Table 4) |
| 7 Dataset Generation (7.1 construction, 7.2 proxy model training, 7.3 implications) | second case study | about 1,170 | 4 / 0 (Figs 9 to 12) |
| 8 Discussion on Extending ArchGym | discussion | about 330 | 0 / 0 |
| 9 Conclusion | summary | about 80 | 0 / 0 |

Total: 12 figures, 4 tables. There is no "Overview" section: Fig 1 in the Introduction plays that role and Section 3 opens with a three-component summary. Related work is folded into Section 2 together with Table 1 of prior ML-for-architecture work.

## 2. Abstract
- 12 sentences, about 320 words (the dump interleaves a copyright block, so the raw count is higher).
- Functions in order: (1) setting (ML is a prevalent approach to tame design space exploration for domain-specific architectures); (2) problem statement with a count ("poses several challenges"); (3) challenge "First": which algorithm; (4) "Second": trade-offs between performance and sample efficiency are inconclusive; (5) "Finally": no holistic framework for fair, reproducible, objective comparison; (6) approach, named: "we introduce ArchGym, an open-source gymnasium and easy-to-extend framework that connects a diverse range of search algorithms to architecture simulators"; (7) demonstration scope: multiple vanilla and domain-specific search algorithms on a memory controller, DNN accelerators, an AR/VR SoC, "over 21K experiments"; (8) the central finding: with unlimited samples, ML algorithms are equally favorable when hyperparameters are tuned; no one solution is necessarily better; (9) coined term "hyperparameter lottery" with definition; (10) secondary capability: easy data collection and aggregation; (11) case study result: proxy cost model with 0.61% RMSE and 2,000-fold reduction in simulation time; (12) artifact availability link.
- Numbers: 21K experiments (scope: the three designs in the sentence), 0.61% RMSE and 2000x (scope: the proxy cost model from the case study). The abstract says three design problems, the Introduction says four, and counts 21,600 experiments and 1.5 billion simulations; the abstract rounds down.
- System named in sentence 6, after three numbered challenges. A coined term appears in the abstract; the paper treats the term as a result.
- Quote (Abstract): "the lack of a holistic framework for fair, reproducible, and objective comparison across these methods hinders the progress".

## 3. Introduction
- About 6 paragraphs and a 5-item contribution list; about 1,000 words of prose plus the Fig 1 caption and Table 1. About 49 sentences in the prose block, average 27 words (long).
- P1 (setting and gap): hardware customization, Moore's law, combinatorial design space, infeasible points, ML-driven optimization by industry and academia. Opens "Hardware customization ... has played a pivotal role". Ends with the gap sentence: "the lack of reproducible baselines hinders fair and objective comparison across different methods." That sentence is the benchmark need in one line.
- P2 (challenge 1): opens "First, selecting the most suitable algorithms and gauging the role of hyperparameters ... is still inconclusive"; gives examples of Bayesian, offline, RL for accelerators; says it is not evident whether improvements come from the algorithm or the hyperparameters. Ends with the need for "a systematic benchmarking methodology".
- P3 (challenge 2): opens "Second, while simulators have been the backbone"; lists simulator fidelity levels from cycle-accurate to proxy models and licensing limits on samples. Ends with a difficulty statement about comparing algorithms under these constraints.
- P4 (challenge 3): opens "Lastly, rendering the outcome of DSEs into meaningful artifacts such as datasets is critical". Ends by saying it is not systematically studied how to leverage exploration data agnostic to the algorithm.
- P5 (solution): "To alleviate these challenges, we introduce ArchGym (See Fig. 1)". Defines it as an open-source gymnasium to analyze and evaluate ML-driven methods, with one interface between search algorithms and performance models; says the interface is the scaffold for baselines and for datasets.
- P6 (evidence preview): "We perform more than 21,600 experiments corresponding to around 1.5 billion simulations across four architectural design space exploration problems"; five search algorithms; spreads of up to 90%, 20%, and 40% for DRAM memory controller, DNN accelerator and SoC; introduces "hyperparameter lottery" and the "equally favorable" finding. Ends with "Below we summarize the main contributions of our work".
- Contribution list: 5 bullets. (1) a framework (capability: systematic evaluation and objective comparison); (2) a finding, with the phrase "contrary to common wisdom"; (3) an argument about evaluation methodology (include the cost of hyperparameter optimization or the comparison misleads); (4) a released artifact (curated datasets for proxy cost models); (5) a finding with a number (adding diversity reduces average RMSE by up to 42x). Two of five items carry numbers or percentages; two are findings, one is a methodological recommendation.
- Problem posing: three numbered challenges (First, Second, Lastly), the same three that the abstract lists and that Section 6 later answers as three "insights". Key insight appears in P6 and the contribution list: algorithm choice matters less than hyperparameter and sample budget.
- Prior work: credited as inspiring ("noticeable performance improvement"), dismissed by one fact: results are confounded by baselines and hyperparameters. Table 1 lists seven prior ML-for-architecture works plus CompilerGym, each tied to one method and one component, with ArchGym in the last row as the general one (any ML method, any architecture component).
- Quote (Introduction, contribution 2): "contrary to common wisdom, the evaluated search algorithms are all equally favorable for architecture design space exploration".

## 4. What the benchmark is
- ArchGym does not define a closed suite; it is described as "an open-source gymnasium to analyze and evaluate various ML-driven methods for design optimization" (Intro P5) and as a "unified framework for evaluating different machine learning-based search algorithms fairly while also saving the exploration data" (Fig 1 caption). Section 3 defines it as three components: Gym Environment, Agents, Interface Signals.
- Most important property: fair, reproducible, objective comparison across search algorithms, produced by one standard interface. A second property is that each run yields a reusable artifact (dataset).
- Words carrying it: "fair", "reproducible", "objective", "apples-to-apples", "standardized", "systematic", "unified". The phrase "apples-to-apples" appears in a call to action in 6.2.
- Numbered list of requirements: no. There is a list of three "challenges" (First, Second, Lastly) and a statement of "primary objectives" in Section 3: apply ML approaches to architecture design space exploration, compare them fairly, provide infrastructure to collect exploration datasets.
- Quote (Section 4): "Such standardization of interfaces provides baselines to objectively compare all the agents in a fair and reproducible manner."

## 5. Why a benchmark is needed
- Argument: published ML-for-architecture papers beat their own baselines, but it is not clear whether the gain comes from the algorithm or the hyperparameters; simulators differ in speed, accuracy and license limits so the sample budget must be part of the comparison; the data produced by searches is thrown away.
- Evidence: not measured in the Introduction; it is argued from the literature, then the paper's own sweep (21,600 experiments, up to 90% interquartile spread) is the evidence that the problem is real. This is a notable move: the evaluation that justifies the need is the benchmark's first use.
- Tie to requirements: one to one. Challenge 1 (algorithm choice and hyperparameters) leads to the interface standardization and hyperparameter sweeps; challenge 2 (simulator cost and sample budget) leads to sample efficiency as the comparison axis; challenge 3 (artifacts) leads to logged trajectories as datasets. The evaluation opening says "The insights from ArchGym are three-fold" and repeats them in the same order.
- No cherry-pick or moving-target story is told as a general benchmark argument; "reproducible baselines" is the only phrase.

## 6. Task and rule definition
- Task unit: an environment (an architecture cost model plus target workloads) and an agent (a policy plus hyperparameters). Interface: action (parameter selection), observation (state of the cost model), reward (or fitness). Section 4 explains why any search method fits: each answers three questions (how it chooses a parameter, how it uses feedback, how it balances exploration and exploitation), tabulated in Table 2 for RL, BO, ACO, GA.
- Metric and acceptance test: reward is a normalized distance to a user-defined target (Table 3 gives the formula per environment, for example |X_target - X_obs| / X_target). A design counts as optimal "as long as it meets all user-defined criteria" (footnote 2), for example latency below L, or 1 W power. Comparison axis: number of simulator samples (100, 1K, 100K, 250K), chosen because time to completion depends on implementation and parallelism ("not a fair assessment"). Distribution reporting: interquartile range across hyperparameter sweeps.
- Budget: the sample count; the paper compares a low-sample regime (up to 10,000) and a high-sample regime (about 100,000).
- Held fixed: environment, workload, reward, interface. Free: agent policy and hyperparameters (swept). The authors call for tuning baselines equally ("critical to properly tune both the algorithm and its baselines").
- Divisions, tracks, submission, audit, hidden test data: none. This is a research framework, not a competition. Fairness is by shared interface and by exhaustive hyperparameter sweeps, not by rules or review. The evaluator is not isolated from the participant: agents are the authors' adaptations of open-source implementations (DeepSwarm for ACO, scikit-optimize, ACME for RL, scikit-opt, NumPy).

## 7. Construction and coverage
- Environments: four, one per level of abstraction. DRAMGym (DRAMSys, memory controller, component level), TimeloopGym (Timeloop, DNN accelerator), FARSIGym (FARSI, AR/VR SoC), MaestroGym (Maestro, DNN mapping). Search spaces from about 1.9e7 to 1e24 (Fig 3). Selection rationale is brief: "to demonstrate ArchGym's generalizability" across component, accelerator, SoC and mapping levels.
- Agents: five (ACO, BO, GA, RL, random walker), chosen because they are commonly used in hardware design (a paragraph of citations in 3.2).
- Coverage shown by Table 3 (environment, simulator, workload, action, observation, reward) and Table 1 (prior ML-for-architecture methods).
- Baselines and reference results: no ground truth; the baseline check is a replication of GAMMA (a domain-specific genetic algorithm) versus plain GA in ArchGym: plain GA does as well or better after a roughly 4,000-run sweep.
- Limits: stated in passing: "we may have missed a lot of hyperparameter combinations" and the sample-efficiency regimes; a Discussion section (8) lists extensions (proxy models, other algorithms, hardware-aware NAS). No limitations section.

## 8. Use and results
- The paper uses the gym to show three things: (a) the hyperparameter lottery (Figs 4 to 6): in DRAMGym the interquartile spread is up to 90%, and each algorithm finds at least one winning configuration; (b) sample efficiency regimes (Fig 7): RL is poor at low samples and improves at high sample counts, simple algorithms stay competitive, and the bottleneck is the slow cost model, not the algorithm; (c) dataset aggregation (Figs 9 to 12): a diverse dataset from several agents lowers proxy-model RMSE by up to 42x (average) and gives a 2,000x faster cost model with 0.61% RMSE.
- Discrimination: the result is that algorithms do not separate under fair tuning. This is a negative finding, offered as the benchmark's insight. It also marks the paper as a methodology argument about how to compare algorithms.
- Presentation: box and violin style plots per environment (Fig 4, Fig 5), line plots by sample budget (Fig 7), a table of designed hardware parameters per agent (Table 4), then calls to action with run-in labels.

## 9. Phrases worth reusing as patterns
1. "[Prior method] has shown [benefit], but the lack of [reproducible baselines] hinders [fair and objective comparison]."
2. "First, [challenge 1] is still inconclusive. ... Second, [challenge 2]. ... Lastly, [challenge 3]."
3. "To alleviate these challenges, we introduce [Name], an open-source [gymnasium] to analyze and evaluate [methods]."
4. "Since all agents interact with [Name] through the same interface, we can additionally record [each interaction]."
5. "We coin the term '[term]' to describe [the chance for X to Y] provided [condition]."
6. "[Name] reinforces using the same interface between [A] and [B], enabling effective mapping of [variety of A]."
7. "The takeaway is that future [field] requires us to report [distributions] rather than [the state-of-the-art claim]." (run-in "A call to action.")
8. "We use [metric] as a normalization metric to compare the trade-offs between [methods], because [domain reason]."

## 10. What transfers to an agent benchmark
1. Phrase the need as a three-part "First, Second, Lastly" list in both the abstract and the Introduction, and answer it with three evaluation insights in the same order. This makes the paper skimmable and ties evaluation to need.
2. Let the first experiment show why the field needs the benchmark: a hyperparameter or seed sweep that shows large spread, then say that conclusions about a method are not trustworthy without tuning every baseline equally. For an agent benchmark, a spread across seeds, prompts, or budgets plays this role.
3. Name the comparison axis and justify it against the alternative (sample count instead of wall-clock time) with the reason the alternative is unfair. Also turn each run into a reusable artifact (dataset) so the benchmark is not only a scoreboard.
- Does not transfer: the gym interface (action, observation, reward) and the five classical search algorithms; the claim that algorithms are equal is specific to these search problems and agents of this type.

## 11. Sentence and paragraph habits (template 8)
- Average sentence length about 22 words (abstract about 21, Intro about 27, Sections 3 to 4 about 21 to 22, 6.1 about 21, 7 about 25). Paragraphs about 120 to 200 words.
- Person and tense: "we" about 12 per 1,000 words; present tense for the framework, past for experiments. The Introduction is heavy with citation numbers in square brackets.
- Run-in bold headings in Evaluation and Section 7 ("Significant statistical variations.", "Effectiveness of domain specific operators.", "Implications.", "A call to action.", "Low sample count.", "Higher sample count.", "Time to Completion.", "Dataset size matters.", "Dataset diversity matters.", "Narrowing the gap between speed and accuracy."). "Implications." and "A call to action." recur in both 6.1 and 6.2.
- Lists: contribution bullets in the Introduction; no other lists. Parentheticals frequent (about 120, with many "e.g." and "i.e."). Em dashes: none; en dashes only in ranges; semicolons about 4. Hedging: "we believe", "it is commonly known", "in all likelihood", "may". Some grammatical slips remain in the text (for example "is the results").
- Numbers: with scope ("up to 90% statistical spread (measured as the interquartile range)", footnote defines the measure).

## 12. Figures and tables (template 9)
- First figure (Fig 1, Introduction): the two-component architecture (ArchitectureFoo environment and Agent) with interface signals and the dataset arrow. It comes first because the abstract's "framework" is abstract until the reader sees the two boxes. The caption is long (about 120 words), descriptive, and states the benefit at the end ("researchers ... can compare ... in a consistent and systematic manner").
- Fig 4 (hyperparameter lottery on DRAMGym across three objectives and four traces) carries the central claim; the star marks the best design per agent. Fig 7 (mean normalized reward versus number of samples) carries the second claim. Fig 12 gives the 2,000x speedup and the RMSE.
- Tables: Table 1 (prior work, method and component), Table 2 (similarities among RL, BO, ACO, GA: policy, feedback, hyperparameters), Table 3 (gym environments: simulator, workload, action, observation, reward), Table 4 (designed parameters per agent). Table 2 is the conceptual table that justifies the interface.

## 13. Why it reads as strong, and what does not transfer (template 10)
- Move 1: three numbered challenges stated identically in the abstract and the Introduction, then three "insights" at the start of Section 6 in the same order. Place: Abstract, Introduction P2 to P4, Section 6 opening.
- Move 2: a coined term for the surprising result ("hyperparameter lottery"), defined in the abstract, in the Introduction with a footnote, and used as a subsection title in 6.1. Place: Abstract, Introduction P6, 6.1.
- Move 3: a run-in "A call to action." closes each evaluation subsection and converts the result into a rule for the community. Place: 6.1 and 6.2.
- Particular to topic, do not copy: the RL and Bayesian optimization vocabulary and the claim of equal merit.
