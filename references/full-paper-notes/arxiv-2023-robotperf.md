# arxiv-2023-robotperf: RobotPerf: An Open-Source, Vendor-Agnostic, Benchmarking Suite for Evaluating Robotics Computing System Performance

Numbering note: sections 0 to 3 follow the base template. Sections 4 to 10 are the benchmark variant. Sections 11 to 13 are the base template sections 8, 9, 10 (sentence habits, figures and tables, why it reads as strong).

## 0. Identity
- Title: RobotPerf: An Open-Source, Vendor-Agnostic, Benchmarking Suite for Evaluating Robotics Computing System Performance.
- Venue and year: arXiv preprint (cs.RO), 2023, revised January 2024. The PDF is in IEEE conference format but prints no venue line, so the venue is unknown from the paper itself.
- Contribution type: benchmark (a suite of ROS 2 benchmarks, a measurement methodology, and a first set of results on 18 hardware platforms).
- Pages: 9 (IEEE two-column; about 3 pages of references). About 6.9k words in the dump, about 4k of body text. This is the shortest of the four papers.
- Full text used: https://arxiv.org/pdf/2309.09212 (v2).

## 1. Skeleton
Roman-numeral sections.

| Section | Role | Words | F / T |
|---|---|---|---|
| Abstract | summary | 165 | 1 / 0 (Fig 1 sits beside it on page 1) |
| I Introduction | problem, gap, definition of the suite | about 700 | 0 / 0 (Fig 1 is referenced) |
| II Background and Related Work (A ROS and ROS 2, B Robotics Benchmarks) | background and comparison | about 900 | 0 / 1 (Table I) |
| III RobotPerf: Principles and Methodology (A non-functional testing, B ROS 2 integration, C platform independence, D flexible methodology, E opaque tests, F reproducibility, G metrics, H current benchmarks, I run rules) | design principles, methodology, rules | about 1,400 | 0 / 2 (Table II, Table III) |
| IV Evaluation (A heterogeneity, B hardware selection, C acceleration benefits) | evaluation | about 700 | 2 / 0 (Fig 2, Fig 3) |
| V Conclusion and Future Work | conclusion | about 120 | 0 / 0 |

Total: 3 figures, 3 tables. No overview section; Fig 1 on page 1 is the overview. The principles section and the methodology section are merged.

## 2. Abstract
- 5 sentences, about 165 words (long sentences, about 33 words each).
- Functions: (1) the system named and defined at once ("We introduce RobotPerf, a vendor-agnostic benchmarking suite ... using ROS 2 as its common baseline"); (2) what it contains: ROS 2 packages across the robotics pipeline and two benchmarking approaches, with definitions of black-box and grey-box inline; (3) tool support and adaptability to custom graphs; (4) authority: drawn from the knowledge of leading robot architects, "establishes a standardized approach"; (5) open source and a commitment to evolve with community input.
- There is no setting sentence, no problem sentence, no gap, and no result. The abstract has no numbers at all (no platform counts, no speedups). The name appears in the first sentence.
- Quote (Abstract): "RobotPerf establishes a standardized approach to robotics benchmarking."

## 3. Introduction
- 4 paragraphs, about 700 words, long sentences (about 30 words on average). No contribution list. No bold run-in headings.
- P1 (setting): robots must run in real time within power limits; accelerating kernels on GPUs and FPGAs is a crucial tool; ends on the end of Moore's Law and Dennard scaling. Opens "In order for robotic systems to operate safely and effective..." (typo in the original).
- P2 (need): hardware-accelerated kernels need a standard software infrastructure; ROS has emerged as the choice, so robotics is "more than just individual algorithms"; ends with "the community's demand for a standardized, industry-grade benchmark to evaluate varied hardware solutions". This sentence is the problem statement. The setup for the next paragraph is the word "benchmark".
- P3 (prior work and gap): cites about 11 workshops and tutorials and then benchmarks for specific algorithms and for drones; dismisses them with a single gap: "the nuances of analyzing general ROS 2 computational graphs on heterogeneous hardware is yet to be fully understood". The credit is by listing, the dismissal is by scope (algorithm-level or one application).
- P4 (definition and method): "In this paper, we introduce RobotPerf, an open-source and community-driven benchmarking tool" assessing performance "in a standardized, architecture-neutral, and reproducible way"; then the grey-box and black-box definitions (repeated word for word from the abstract); then validation on CPUs, GPUs, FPGAs; closing with the repository link and the claim that the methodology "is currently being used in industry".
- Key insight: none stated as an insight. The idea is the choice of ROS 2 computational graphs as the unit and the two test styles.
- Challenges device: none.
- Result preview: one sentence only ("We validate the framework's capabilities by conducting benchmarks on diverse hardware platforms ... showcasing RobotPerf's utility"); no numbers.
- No roadmap paragraph.

## 4. What the benchmark is
- Definition, in the Intro P4: "an open-source and community-driven benchmarking tool designed to assess the performance of robotic computing systems in a standardized, architecture-neutral, and reproducible way". Section III repeats it more directly: "an open-source, industry-strength robotics benchmark for portability across heterogeneous hardware platforms."
- Most important property: portability and comparability across heterogeneous hardware, with fair comparison as the aim (Fig 1 caption: "fair comparisons of ROS 2 computational graphs across CPUs, GPUs, FPGAs and other accelerators"). Industry adoption (use of ROS 2) is a second property.
- Words carrying it: "vendor-agnostic" (title and abstract), "standardized", "architecture-neutral", "reproducible", "fair", "representative" (only in a subsection title, IV-A), "industry-grade", "community-driven". The phrase "architecture-neutral, reproducible" echoes the MLPerf Inference wording ("architecturally neutral, representative, and reproducible").
- Numbered list: no numbered list. Principles are the subsection headings of Section III A to F: non-functional performance testing; ROS 2 integration and adaptability; platform independence and portability; flexible methodology (grey-box and black-box); opaque performance tests; reproducibility and consistency. Section III opens by saying it "outlines the important design principles" but never numbers them.
- Quote (Section III): "RobotPerf is an open-source, industry-strength robotics benchmark for portability across heterogeneous hardware platforms."

## 5. Why a benchmark is needed
- Argument: hardware acceleration is spreading in robotics; ROS 2 is the shared software layer; but existing benchmarks measure algorithm correctness (functional) or end-to-end latency on CPUs, so there is no way to compare accelerated ROS 2 graphs on heterogeneous hardware. Section II-B restates it with about 50 citations and gives Table I.
- Evidence: Table I compares eight existing benchmarks (OMPL benchmark, MotionBenchMaker, OpenCollBench, BARN, DynaBARN, MAVBench, Bench-MR, RTRBench) with RobotPerf on seven characteristics (real-time metrics, spans pipeline categories, heterogeneous hardware, ROS 2 integration, functional testing, non-functional testing, community led). RobotPerf's row has six ticks and one cross (the cross is, by the text, functional testing; the paper says openly that it covers only non-functional testing). Other evidence is a count of workshops and the 600-company ROS adoption figure.
- Tie to requirements: Table I's columns map loosely to the principle headings in Section III (non-functional testing, ROS 2 integration, heterogeneous hardware, community led). The mapping is implied by shared words, not stated.
- No story about incomparable results or cherry-picked baselines is told. The need is a missing capability, not a fairness failure.

## 6. Task and rule definition
- Unit of task: a self-contained ROS 2 package (19 benchmarks in the beta: perception a1 to a5, localization b1 to b3, control c1 to c5, manipulation d1 to d6; Table III). Each has a machine-readable benchmark.yaml with its description and accepted results.
- Metrics: latency, throughput, power consumption including energy efficiency (performance per watt). Quality target or acceptance test: none, because the suite does non-functional testing only (functional correctness is not checked; the paper says the architecture could be extended).
- Measurement methods: black-box (a PlaybackNode and a MonitorNode around the node of interest; end-to-end latency from propagated message IDs; less detailed; modifies the graph) and grey-box (tracer-based probes via ros2_tracing and LTTng, average overhead 3.3 microseconds; more precise; more engineering). Table II compares them on precision, performance, flexibility, portability, ease of use, real robots.
- Fixed versus free: fixed are the benchmark package, input data (ROS 2 rosbags, including the project's own and third-party bags), and data loader and playback nodes; free are the hardware and the implementation of the node of interest ("opaque tests": the workload code is not modified, input and output nodes sit outside it). Run rules: tests in a controlled environment; clock frequency and core count recorded and reported; results are hoped to undergo peer review; avoid overfitting to specific setups by broad test scenarios. The paper states these in a stringent tone but only the first is a rule; the second is an aspiration ("we look forward to the possibility").
- Divisions, tracks, budget, submission checks, hidden data: none. Evaluator isolation: through the black-box design (the monitor sits outside the workload).

## 7. Construction and coverage
- Tasks: 19 beta benchmarks organized in four categories along the robotics pipeline (perception, localization, control, manipulation). Selection criteria are not given except that they cover the pipeline and reuse existing ROS 2 components (Table III cites the source package for each one).
- Coverage is shown by Table III (category, benchmark name, description with citation). There is no baseline or reference implementation in the MLPerf sense; reference results are the measured platform results in Fig 3.
- Reproducibility support: common rosbag formats, ament and colcon build flows, YAML description.
- Limits stated: functional testing is out of scope; the beta has no throughput values for manipulation tasks and no power values for localization tasks (Fig 3 caption); results interpretation warning in IV-C; "RobotPerf beta" is the label of the whole benchmark set.

## 8. Use and results
- What is shown: Fig 3 gives radar plots of latency, throughput and power for 18 hardware platforms (edge CPUs such as Qualcomm RB5, server CPUs such as Intel i7-8700, an FPGA board AMD Kria KR260, the NVIDIA AGX Orin dev kit, laptop-class Intel CPUs), across the four categories, split by black-box (dark) and grey-box (light) runs. Fig 2 shows perception latency on KR260 with and without a hardware accelerator (ROBOTCORE Perception), with speedups of 3.3x, 4.4x and 11.5x (173 ms to 15 ms on benchmark a5).
- Demonstration of discrimination: the argument is "no one-size-fits-all": an i7-12700H beats an NVIDIA AGX Orin on four control benchmarks but is 6.5x slower on one (c2). Then, hardware acceleration gives up to 11.5x. The section is organized by three claims about what the benchmark can do: provide comparative insight across heterogeneous platforms, guide hardware selection, and reveal the benefit of acceleration.
- Presentation: radar plots show many platforms at once, with a rank order by thermal design power in the key. The comparability across platforms is shown by putting all on the same axes; the paper does not provide a table of numbers in the text.
- Caution sentence: "results ... do not represent a generic recommendation on which hardware should be used."

## 9. Phrases worth reusing as patterns
1. "We introduce [Name], a vendor-agnostic benchmarking suite designed to evaluate [property] across a diverse range of [platforms] using [common baseline] as its common baseline."
2. "[Name] is an open-source, industry-strength [domain] benchmark for portability across heterogeneous [platforms]."
3. "[Method A] measures performance by eliminating [layers] and replacing them with [test application], and [method B], an application-specific measure that observes [internal state] with minimal interference."
4. "To ensure the reliability and reproducibility of the performance data, we adhere to a stringent set of run rules. First, ... Second, ... Finally, ..."
5. "We refrain from altering the workloads of interest and instead use specialized input and output nodes positioned outside the primary nodes. We term this methodology '[opaque tests],' a concept that [Name] adheres to when possible."
6. "Table [n] summarizes our unique contributions. It includes a selection of representative benchmarks and provides an evaluation against [Name] on essential characteristics."
7. "The results demonstrate the fallacy of a '[one-size-fits-all]' solution. For example, [platform A] outperforms [platform B] on [X] but is [N]x slower on [Y]."
8. "We stress that the results obtained here should be interpreted according to [the end application] and do not represent a generic recommendation."

## 10. What transfers to an agent benchmark
1. Coin a short name for the measurement discipline that keeps the evaluator out of the participant's code ("opaque tests") and describe both the strict and the light-touch variant with a trade-off table (Table II is a good template: precision, overhead, portability, ease of use).
2. Write the evaluation as three claims about what the benchmark can do (compare across platforms, guide selection, reveal the gain of a technique) and give each a subsection title that states the claim.
3. Use a comparison table of existing benchmarks on named characteristics with the new benchmark in the last row, and be honest where it has a cross.
- Does not transfer: the radar plots over latency, throughput and power for many boards, and the ROS 2 specific content. Also do not copy the weaker parts: aspirational run rules, no baselines, no stated task selection criteria, and an abstract without a problem statement or any number.

## 11. Sentence and paragraph habits (template 8)
- Average sentence length about 25 words overall; Introduction and Related Work sentences are about 30 words; Section III is shorter (about 18 words) because it uses short definitional sentences. Paragraphs about 100 to 200 words.
- Person and tense: present tense, "we" about 10 per 1,000 words, passive in design descriptions.
- No bold run-in headings; subsections carry lettered headings (A to I) with noun phrases. Italic or bold emphasis is not used. No bullet lists. Parentheticals about 40 (examples in brackets). Em dashes about 1, semicolons none, citation strings very long (for example 8 to 20 numbers in a row).
- Hedging: low; claims are strong in tone ("stringent", "rigorous assessment", "comprehensive") and tentative in content. Subsection titles contain adjectives that claim the property ("Fair and Representative Assessment of Heterogeneity", "Rigorous Assessment of Acceleration Benefits").
- Numbers: few, scoped in the sentence (6.5x slower on benchmark C2, 11.5x from 173 ms to 15 ms for a5, 18 platforms, 3.3 microseconds).
- Typos and grammar slips appear in the arXiv text ("safely and effective").

## 12. Figures and tables (template 9)
- First figure (Fig 1, on page 1 beside the abstract): a layered diagram of a robotic stack (application, algorithm: perception, localization, control; system: ROS 2 with rcl, rclcpp, rmw, DDS, OS; hardware: CPU, GPU, FPGA) with the benchmark's playback, input, output, monitor nodes and where grey-box and black-box tests probe. It comes first because it shows the whole benchmark in one picture. The caption is descriptive and ends with the aim (fair comparisons across accelerators).
- Fig 2 (bar chart of perception latency with and without an accelerator, with 3.3x, 4.4x, 11.5x labels) and Fig 3 (radar plots, 18 platforms, four categories) carry the argument. The Fig 3 caption is very long and includes the incompleteness note.
- Tables: Table I (existing benchmarks versus seven characteristics, tick and cross marks), Table II (grey-box versus black-box trade-offs across six criteria), Table III (the 19 beta benchmarks by category, with a one-line description and source citation).

## 13. Why it reads as strong, and what does not transfer (template 10)
- Move 1: the name plus the property words are in the title and first abstract sentence ("vendor-agnostic"), and the comparison table (Table I) places the benchmark among peers with named columns. Place: title, Abstract, II-B.
- Move 2: two measurement modes with a trade-off table, so the reader sees the cost of each rigor level. Place: III-D and Table II.
- Move 3: evaluation subsection titles state what the benchmark can be used for, and the text ends each with a bounded takeaway. Place: IV-A to IV-C. The caution sentence at the end of IV-C is a clean example of bounding a claim.
- Particular to topic, do not copy: radar plots over hardware platforms; the ROS 2 node vocabulary.
