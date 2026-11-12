# isca-2020-mlperf-inference: MLPerf Inference Benchmark

Numbering note: sections 0 to 3 follow the base template. Sections 4 to 10 are the benchmark variant. Sections 11 to 13 are the base template sections 8, 9, 10 (sentence habits, figures and tables, why it reads as strong), kept after the benchmark sections so numbers do not clash.

## 0. Identity
- Title: MLPerf Inference Benchmark.
- Venue and year: ISCA 2020. The arXiv v2 text (9 May 2020) does not print a venue line, so the venue is not confirmed from the PDF itself.
- Contribution type: benchmark (benchmark suite, load generator, rules, review process, and a first round of results).
- Pages: 15 in the arXiv PDF (IEEE two-column, about 12 pages of text plus references). About 12.7k words in the dump including about 4 pages of references and a long author block (about 50 authors from about 30 organizations).
- Full text used: https://arxiv.org/pdf/1911.02549.

## 1. Skeleton
Roman-numeral sections. Approximate words, then figures (F) and tables (T).

| Section | Role | Words | F / T |
|---|---|---|---|
| Abstract | summary | 195 | 0 / 0 |
| I Introduction | problem, definition, five design choices, impact | 1,220 | 0 / 0 |
| II Inference-Benchmarking Challenges (A models, B scenarios, C systems) | motivation / background | 900 | 2 / 0 (Fig 1, Fig 2) |
| III Benchmark Design (A workloads, B quality targets, C scenarios, D tail-latency statistics) | the benchmark definition | 2,590 | 0 / 5 (Tables I to IV; two equations) |
| IV Inference Submission System (A SUT, B LoadGen, C data set, D accuracy checker) | the rules and the harness | about 1,530 | 2 / 1 (Fig 3, Fig 4, Table V) |
| V Submission-System Evaluation (A divisions and categories, B result review, C reporting) | process and enforcement | about 950 | 0 / 0 |
| VI Benchmark Assessment (A task coverage, B scenario usage, C processors and frameworks, D system diversity, E open division) | evaluation of the benchmark | 1,390 | 4 / 2 (Figs 5 to 8, Tables VI, VII) |
| VII Lessons Learned (A to E) | discussion | 830 | 0 / 0 |
| VIII Prior Art in AI/ML Benchmarking | related work, placed late | 430 | 0 / 0 |
| IX Conclusion | three summary aspects | about 520 | 0 / 0 |

Total: 8 figures, 7 tables. There is no separate "overview of design" section: Section III opens with a roadmap sentence, and Fig 3 gives the system picture.

## 2. Abstract
- 11 sentences, about 195 words, one paragraph.
- Functions in order: (1) setting (ML hardware and software demand is burgeoning); (2) setting with numbers (inference systems exploded); (3) over 100 organizations build chips, three and five orders of magnitude spread; (4) software side (dozen frameworks); (5) problem (assessing performance in an architecture-neutral, representative, reproducible manner is hard); (6) gap (clear need for industry-wide standard); (7) approach, named ("MLPerf Inference answers that call"); (8) what the paper presents (the benchmarking method); (9) mechanism: rules and best practices to ensure comparability; (10) result: more than 600 reproducible measurements from 14 organizations over 30 systems; (11) scope claim: submissions attest to flexibility and adaptability.
- Numbers: 100 organizations, 3 and 5 orders of magnitude (scope given: power consumption, performance), 30 organizations, 200 engineers, 600 measurements, 14 organizations, 30 systems. Each number is attached to its noun in the same clause; none is a speedup.
- The system is named in sentence 7, after the need has been built up for five sentences.
- Quote (Abstract): "MLPerf prescribes a set of rules and best practices to ensure comparability across systems with wildly differing architectures."

## 3. Introduction
- 4 running paragraphs, then 5 numbered bold run-in items, then 2 short run-in paragraphs ("Impact", "Staying up to date"). About 1,220 words, 65 sentences.
- P1 (setting): opens "Machine learning (ML) powers a variety of applications"; ends with the numbers (over 100 companies target inference chips, about 20 target training), which sets up the claim that inference is the critical workload.
- P2 (problem): opens "Each ML system takes a unique approach to inference"; lists the combinatorial explosion of tasks, models, frameworks, libraries; ends with the requirement: the field "needs a benchmark that is architecturally neutral, representative, and reproducible." The three words are the thesis of the paper and they are stated before any prior work.
- P3 (prior work): lists AIMatrix, MLMark, AIXPRT, AI Benchmark, TBD, Fathom, DAWNBench. Credit is one sentence ("substantial contributions"); dismissal is one sentence: they were built without input from ML-system designers, so there is no consensus on models, metrics, tasks, rules. The dismissal is about process (who was in the room), not about technical failure. Detail comparison is deferred to Section VIII.
- P4 (definition and claim): "In this paper, we present MLPerf Inference, a standard ML inference benchmark suite" and says it complements MLPerf Training. Credibility statement: more than 30 organizations, over 200 engineers. Ends by promising to explain metrics, scenarios, and standardized evaluation.
- Items 1 to 5 (bold sentence, then a paragraph): (1) representative workloads for reproducibility and accessibility; (2) scenarios for realistic evaluation (four: single-stream, multistream, server, offline); (3) target qualities and tail-latency bounds; (4) permissive rules, two divisions; (5) a method that lets models change. Each item is phrased "We [verb] X", names a design decision, and gives the reason. These items double as the contribution list, but the paper calls them design choices, not "contributions". Only item 4 (division count of two) and item 2 (four scenarios) carry numbers.
- Impact paragraph (result preview): MLPerf Inference v0.5 in October 2019, over 600 submissions from 14 organizations, 595 cleared as valid after audit, four orders of magnitude of performance variation. It states the result as evidence that the metrics and scenarios discriminate between systems.
- "Staying up to date": one line, pointing to the website and a maintenance process.
- Problem posing: by counting (systems, frameworks, tasks), not by a single motivating example. Key insight: the insight is not a trick; it is the rule that the task and quality are fixed and implementation is free (paragraph before item 4: "We specify the task and the rules, but we leave implementation to submitters.").
- "Challenges" device: not in the intro; it is Section II, "Inference-Benchmarking Challenges", three challenges (diversity of models, scenarios, systems), each later answered by a design section.

## 4. What the benchmark is
- Definition (Intro P4): "a standard ML inference benchmark suite with proper metrics and a benchmarking method" to "fairly measure the inference performance of ML hardware, software, and services". A second definition appears in Section III: the benchmark defines high-level tasks, gives canonical reference models, and accepts any mathematically equivalent implementation. Section IV adds the operational definition: a submission system = system under test + Load Generator + data set + accuracy script.
- Most important property: comparability across very different architectures, with architecture neutrality as the condition for it. Other named properties: representative, reproducible, realistic, accessible.
- Words that carry it: "architecture-neutral" (and "architecturally neutral"), "representative", "reproducible", "comparability", "apples-to-apples", "fair". The word "comparability" is tied to a mechanism in Section IV: the boundary between submitter-owned and MLPerf-owned parts.
- Numbered list: yes, five numbered design choices in the Introduction (four of the five, all except the quality-target item, are reused as the objectives in the bullet list that opens Section VI). Short form: 1 representative workloads; 2 realistic scenarios; 3 target quality and tail latency; 4 permissive rules (closed and open divisions); 5 a method that allows models to change.
- Quote (Section IV): "By establishing a clear boundary between submitter-owned and MLPerf-owned components, the benchmark maintains comparability among submissions."

## 5. Why a benchmark is needed
- Argument: the ML inference space is combinatorial (Fig 2 stack picture), models trade accuracy against cost along a Pareto frontier (Fig 1), deployment scenarios differ, so any single number on any single configuration misleads. Prior benchmarks had no industry-wide input, so "no consensus".
- Evidence: counts of organizations and chips; Fig 1 (50x compute difference, 55% to 83% top-1); a concrete porting example (non-maximum suppression differs between TensorFlow and TensorFlow Lite, SSD-MobileNet-v1 drops from 23.1 to 22.3 mAP); the example that ResNet-50 is implemented in subtly different ways.
- Tie to requirements: Section II has three challenges (models, scenarios, systems) and Section III answers them in the same order in spirit: representative workloads and quality targets (models), four scenarios (deployment), a semantic-level benchmark with reference models and the LoadGen (systems). The mapping is by prose, not by a numbered table.
- No cherry-picking or moving-target story is told in detail; the "unstable baseline" idea appears in one sentence (a name such as ResNet-50 does not uniquely describe a model).

## 6. Task and rule definition
- Task: a high-level task (for example image classification) plus one canonical reference model with FP32 weights, a public data set, a quality target (for example within 1% of FP32 accuracy; 98% for MobileNet), a scenario with a metric and a latency bound, and a minimum query count (Tables I to V).
- Scenarios: single-stream (90th-percentile latency), multistream (number of streams under a latency bound), server (Poisson arrivals, queries per second under a latency bound), offline (throughput). Latency bounds per task in Table III. Statistical rule: the number of queries is computed from tail percentile, confidence 99%, margin one twentieth of the gap to 100% (equations 1 and 2); for example 270K queries for a 99th percentile bound; minimum run time 60 s; five runs for server, minimum reported.
- Held fixed: task, data set, LoadGen, accuracy script, quality target, query timing rules, reference weights (no retraining), scenarios. Free: implementation, framework, hardware, batching, numerical format from a pre-registered approved list (INT4 to FP32), mathematically equivalent transformations, fusing, sparse replacement. Prohibited: retraining, pruning, caching, benchmark-aware or data-set-aware optimizations, exploiting the fixed random seed. The paper uses an explicit blacklist rather than a whitelist, and says why (to encourage a wide range of techniques).
- Divisions: closed (same model, equivalent, no retraining, comparable) and open (any model, may change quality target; not directly comparable; must document deviations). Categories: available, preview, research (RDO).
- Fairness enforcement: the LoadGen sits outside submitter code and generates traffic, timing and logs; an accuracy script checks outputs; four audit tests (accuracy verification in performance mode, on-the-fly caching detection, alternate random seed, custom data sets); submissions with code and logs go to a public repository for peer review; a submission checker script. Reported outcome: about 40 issues in about 180 closed-division results; 166 released.
- Evaluator isolation: yes in structure. Fixed components (data set, LoadGen, accuracy script) are MLPerf-owned; the system under test is submitter-owned; the LoadGen can self-check whether its source was modified. Hidden data: not hidden; the custom data set audit plays that role.
- No summary score by design (V-C): weighting tasks is "highly subjective", and systems may not target every task.

## 7. Construction and coverage
- Tasks: five (image classification heavy and light, object detection heavy and light, machine translation), 20 benchmark versions counting four scenarios each. Selection criteria: mature models with community support, open source, workable across frameworks, covers CNNs and RNNs, comes from the training suite where possible (ResNet-50 v1.5, SSD-ResNet-34, GNMT), and input from members including customers and vendors (the scenario list came from a membership survey).
- Coverage shown by Table I (area, task, reference model, parameters and operations, data set, quality target) and Table II (scenarios with real examples). Coverage of results is shown again in VI by Fig 5 and Tables VI, VII.
- Baselines: reference models in TensorFlow, PyTorch, ONNX at FP32; for MobileNet the authors also trained quantization-friendly weights and published INT8 versions, because the 1% accuracy target was unreachable without retraining. The text says what failed and what they did (a candid paragraph in III-B).
- Own limits are stated in VII: missing tasks (speech, recommendation, transformers), data-set gap (no public large-image detection set, so COCO was upscaled to 1,200 x 1,200), modeled versus measured performance, untimed preprocessing, caching and retraining prohibited though real systems do both, and open items for later versions.

## 8. Use and results
- What is shown: the first call for submissions (October 2019). Over 600 results from 14 organizations; 595 cleared; 429 of them in the open division; anonymous systems labeled A to K in plots.
- How it shows discrimination: Fig 5 (task mix is balanced, most popular model only about three times the least popular), Fig 6 (server throughput divided by offline throughput for 11 systems: some lose about 10%, some 50% or more; NMT loses 39 to 55%, ResNet-50 3 to 35%), Fig 7 (all five processor classes), Fig 8 (single-stream and offline spreads of about 100x; whole range about 10,000x).
- Presentation for comparability: results normalized to the slowest system per scenario; no leaderboard; no named vendors in the paper's plots; each assessment sub-section maps to one of the design choices (four of the five).
- The results section is therefore an evidence argument for the benchmark's design (coverage, discrimination, flexibility), not a ranking.

## 9. Phrases worth reusing as patterns
1. "To quantify these tradeoffs, the field needs a benchmark that is [adjective], [adjective], and [adjective]."
2. "We specify the [task] and the rules, but we leave [implementation] to submitters."
3. "We [prohibit X] to ensure comparability. Although this restriction may fail to reflect [realistic case], [requirement A] and [requirement B] are most important for comparability."
4. "By establishing a clear boundary between [owner A] and [owner B] components, the benchmark maintains [property]."
5. "We chose [an explicit blacklist] to encourage [diversity] and to support [neutrality]."
6. "[Metric] is [N] per [unit] subject to [bound]; no more than [x]% of queries may exceed the bound."
7. "We assess the [set] on the basis of our [objectives]: [bullet per objective, each with its section pointer]."
8. "[Benchmark] provides no summary score. [Reason about weighting] ... averaging across all tasks makes no sense."

## 10. What transfers to an agent benchmark
1. State the three adjectives (architecture-neutral, representative, reproducible) in the Introduction before prior work, then use each adjective as a section-level obligation; for us, replace with the properties the agent benchmark must keep (for example evaluator-neutral, representative of design tasks, reproducible).
2. Draw an explicit ownership boundary: benchmark-owned parts (evaluator, task definition, data) versus participant-owned parts (the agent and how it works). Say that the boundary is what makes results comparable, then list what is fixed and what is free, and give a blacklist of prohibited moves.
3. Report the audit statistics of the first round (about 40 issues in about 180 results, 166 released) and the audit tests themselves; show that rules are enforced, not only written.
- Does not transfer: the latency-bounded query scenarios and the statistics for query counts (equations for tail-latency confidence) are specific to inference serving.

## 11. Sentence and paragraph habits (template 8)
- Average sentence length: about 19 words (abstract 17.7, intro 18.8, III 20.4, VI 21.4, VII-IX 16 to 25). Paragraphs about 100 to 170 words, five to eight sentences; topic sentence first.
- Person and tense: first-person plural, present tense for the benchmark ("MLPerf defines"), past tense for what the authors did ("we surveyed", "we selected"). About 25 "we" per 1,000 words in design sections.
- Bold run-in headings in the Introduction (five numbered items) and italics-style run-in heads inside III and IV ("Allowed techniques.", "Prohibited techniques.", "Single-stream.", "Multistream.", "Server.", "Offline."). The scenario and rule paragraphs each start with the run-in name, one definition sentence, a real example, and the metric.
- Lists: one bullet list (assessment objectives in VI). Parentheticals are heavy: about 135 in the body (examples inside parentheses). Em dashes about 10, semicolons about 12 in the body (one or two per section). Hedging is light: "nearly intractable", "likely", "possibly", "may"; claims about coverage are made with "suggests" and "indicates".
- Numbers: stated with their unit and scope in the same sentence ("90th-percentile latency", "99% confidence"); ratios written as "10,000x" or "about 10,000x" with the orders-of-magnitude phrase beside it.
- Candid sentences: the paper writes down what failed ("the accuracy loss was unacceptable without retraining", "GNMT garnered no multistream submissions").

## 12. Figures and tables (template 9)
- First figure (Fig 1, in Section II): accuracy versus compute for image models; shows that no single model is optimal and the design space is a Pareto frontier. It comes first because it justifies the need for quality targets and for choosing reference models. Caption is descriptive with a one-clause takeaway ("No single model is optimal").
- Fig 2 (stack diversity picture) states its takeaway in the caption (options at every level make benchmarking hard). Fig 3 and Fig 4 explain the LoadGen (numbered steps 1 to 7 in the caption; timing diagrams for four scenarios). Fig 6 (server versus offline throughput) is the figure that carries the finding that unconstrained throughput misleads.
- Tables: Table I is the coverage table (task, reference model, data set, quality target); Table II is the scenario definition table; Table III the latency bound table; Tables IV and V the statistical and query counts; Table VI the coverage of submissions; Table VII framework versus hardware matrix. Table captions are full sentences in small caps and often include the takeaway ("each one reflects critical commercial and research use cases").

## 13. Why it reads as strong, and what does not transfer (template 10)
- Move 1: three adjectives, stated once in the Introduction (P2) and held as obligations through the whole paper. Place: Introduction P2 and Sections III and VI headings.
- Move 2: each design choice has a reason, a number, and an audit. For example the quality target (III-B) states the rule, the example (ResNet-50 75.70% minimum), the failure that forced a change (MobileNet), and the fix. Place: III-B.
- Move 3: the assessment (VI) uses four of the Introduction's five items as its test, so the evidence maps one-to-one onto the claims. Place: start of VI, the bullet list.
- Particular to topic, do not copy: the long statistical derivation of query counts and the four serving scenarios.
